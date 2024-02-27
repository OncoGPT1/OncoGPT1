<div align=center>
<img src="https://github.com/OncoGPT1/OncoGPT1/blob/main/fig/logo.png" width="180) height="105">  
</div>  

# **OncoGPT: A Medical Conversational Model Tailored with Oncology Domain Expertise on a Large Language Model Meta-AI (LLaMA)**
Fujian Jia<sup>1,* </sup>, Xin Liu<sup>1,* </sup>, Lixi Deng<sup>1,*</sup>, Jiwen Gu<sup>1</sup>, Chunchao Pu<sup>1</sup>, Tunan Bai<sup>1</sup>, Mengjiang Huang<sup>2</sup>, Yuanzhi Lu<sup>3,§</sup>, Kang Liu<sup>1,§</sup>  

1, Shenzhen Kanghua Juntai Biotech Co. Ltd., B 215, Unit No.7, Shahe Rd W, Nanshan, Shenzhen, Guangdong Province 518063, China.  

2, Department of Nutrition and Graduate Group in Nutritional Biology, University of California, Davis, CA 95616, USA.  

3, Department of Pathology, The First Affiliated Hospital of Jinan University, Tianhe Qu, Guangzhou 510632, China.  


![image](https://github.com/OncoGPT1/OncoGPT1/blob/main/fig/oncogpt.png)

## Setup:
In a conda env with pytorch available, run:  
```
pip install -r requirements.txt 
```

## Data and model:
### 1. OncoGPT Dataset:
180k real conversations between patients and doctors of OncoGPT. [OncoGPT-50k](https://github.com/OncoGPT1/OncoGPT1/blob/main/data/OncoGPT_demo.rar)  
Real conversations between patients and doctors for test data. [test](https://github.com/OncoGPT1/OncoGPT1/blob/main/data/test.json)    
100k real conversations between patients and doctors from ChatDoctor. [HealthCareMagic-100k](https://drive.google.com/file/d/1lyfqIwlLSClhgrCutWuEe_IACNq6XNUt/view?usp=sharing)  
Stanford Alpaca data for basic conversational capabilities. [Alpaca](https://github.com/OncoGPT1/OncoGPT1/blob/main/data/alpaca.json)  

### 2. Model Weights:
Place the model weights file in the ./pretrained folder.
How to fine-tuning
Fine-tuning with Lora

```
    WANDB__SERVICE_WAIT=300 python finetune.py \
    base_model: str = "",  # pretainded OncoGPT \
    data_path: str = "OncoGPT_180k.json", \
    output_dir: str = "./OncoGPT", \
    batch_size: int = 128, \
    micro_batch_size: int = 4, \
    num_epochs: int = 3, \
    learning_rate: float = 3e-4, \
    cutoff_len: int = 256, \
    val_set_size: int = 2000, \
    lora_r: int = 8, \
    lora_alpha: int = 16, \
    lora_dropout: float = 0.05 \
```

## How to inference
You can build a OncoGPT model on your own machine and communicate with it.  
``` 
python chat.py  
```  
To apply for OncoGPT, please register for hugging face and fill out this form. [Link](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__j-jygVUOEpYSTEzR0ZQUVMzUjdSMkExUkVYTVhGVS4u)  

## Examples  
```
Patient:Lung cancer, the liver has also spread, and small cell carcinoma. The current symptoms are cough, cough and chest pain. I just started chemotherapy yesterday. Can my father be cured?  
OncoGPT:Hi, Thanks for writing in. Small cell carcinoma of the lung is an aggressive form of cancer with poor prognosis. Chemotherapy is the mainstay of treatment in such cases. There is no guarantee for cure, however, in selected cases, long term remissions have been reported. So he needs to continue his chemotherapy and see how well it works.  
```

## Overview
OncoGPT is a specialized large linguistic dialogue model tailored for oncology-related queries. We used Meta’s popular public LLaMA-7B model as the platform for development and evaluation. By training the LLaMA-7B base model with 52K instruction data from Stanford University's publicly available Alpaca model and incorporating 100K patient-physician conversations from an online medical consultation website (from ChatDoctor LLM), the model successfully acquired general medical conversation abilities. Subsequently, the model underwent further refinement using our established 180K+ genuine doctor-patient oncology dialogue dataset, resulting in the creation of OncoGPT.  

## Patient-physician Conversation Dataset
To collect a dataset of patient-physician conversations. We investigated common doctor-patient dialogue websites, including Chinese data, and finally obtained 180K data，In patient-physician conversations, the patient's descriptions of disease symptoms are often colloquial and cursory. We filtered these data both manually and automatically, removed the identity information of the doctor and patient, removed low quality questions and used language tools to correct grammatical errors. In addition, we selected 737 questions to test the model and manually divided them into research and therapeutic questions to evaluate the model effect.

## Future updates  
Subsequent updates to the Oncogpt 180K full database, interactive demo, and version 2.0 with automated reference checking and citation fuction, are on the road.

## Limitations
We emphasize that ChatDoctor is for academic research only and any commercial use and clinical use is prohibited. There are three factors in this decision: First, ChatDoctor is based on LLaMA and has a non-commercial license, so we necessarily inherited this decision. Second, our model is not licensed for healthcare-related purposes. Also, we have not designed sufficient security measures, and the current model still does not guarantee the full correctness of medical diagnoses.
## Reference
OncoGPT: A Medical Conversational Model Tailored with Oncology Domain Expertise on a Large Language Model Meta-AI (LLaMA)
