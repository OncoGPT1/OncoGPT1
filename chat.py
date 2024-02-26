##/bin/python
import os, json, itertools, bisect, gc
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, LlamaTokenizer
import transformers
import torch
from accelerate import Accelerator
import accelerate
import time

model = None
tokenizer = None
generator = None
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def load_model(model_name, eight_bit=0, device_map="auto"):
    global model, tokenizer, generator
    print(model_name+" is loading ...")
    if device_map == "zero":
        device_map = "balanced_low_0"
    gpu_count = torch.cuda.device_count()
    tokenizer = transformers.LlamaTokenizer.from_pretrained(model_name)
    model = transformers.LlamaForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
        load_in_8bit=False,
        cache_dir="cache"
    ).cuda()
    generator = model.generate

load_model("./OncoGPT/")
First_chat = "OncoGPT: I am OncoGPT, what medical questions do you have?"

print(First_chat)
history = []
history.append(First_chat)

def go():
    invitation = "OncoGPT: "
    human_invitation = "Patient: "
    msg = input(human_invitation)
    history.append(human_invitation + msg)

    fulltext = "If you are a doctor, please answer the medical questions based on the patient's description. \n\n" + "\n\n".join(history) + "\n\n" + invitation
    generated_text = ""
    gen_in = tokenizer(fulltext, return_tensors="pt").input_ids.cuda()
    in_tokens = len(gen_in)
    with torch.no_grad():
            generated_ids = generator(
                gen_in,
                max_new_tokens=128,
                use_cache=True,
                pad_token_id=tokenizer.eos_token_id,
                num_return_sequences=1,
                do_sample=True,
                repetition_penalty=1.1, # 1.0 means 'off'. unfortunately if we penalize it it will not output Sphynx:
                temperature=0.1, # default: 1.0
                top_k = 40, # default: 50
                top_p = 0.75, # default: 1.0
                early_stopping=True,
            )
            generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0] # for some reason, batch_decode returns an array of one element?
            text_without_prompt = generated_text[len(fulltext):]
    response = text_without_prompt
    response = response.split(human_invitation)[0]
    response.strip()
    print(invitation + response)
    history.append(invitation + response)

while True:
    go()
