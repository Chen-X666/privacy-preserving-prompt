# Privacy-Preserving Prompt Tuning for Large Language Model

| Symbol | 🌟 | ⬜️ | ⬛️ |
| --- | --- | --- | --- |
| Description | Inspiration | White-box method | Black-box method |

## Attacker Methodology

<div align="center"><img src="https://github.com/Chen-X666/privacy-preserving-prompt/blob/main/attack_processing.png" height="600px"/></div>


### Prompt Injection Attacks (PIA)
| Paper | Year |   Source              |  Attack Prompt Type  |   Tasks   |
|-------|------|-----------------------|----------------------|-----------|
| ⬛️Effective Prompt Extraction from Language Models  |  2024.02   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2307.06865) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://anonymous.4open.science/r/prompt-extraction-83C1)  | Instruction Prompt | Information Extration | 
| ⬛️Prompt Stealing Attacks Against Large Language Models  |  2024.02   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2402.12959)  | Role-Based Prompt, Direct Prompt, In-Context Prompt | Q&A |
| 🌟⬛️TrojLLM: A Black-box Trojan Prompt Attack on Large Language Models  |  (NeurIPS, 2023)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2306.06815) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/UCF-ML-Research/TrojLLM)  | Instruction prompt | Classification | 
| 🌟⬛️Ignore Previous Prompt : Attack Techniques For Language Models  |  (NeurIPS, 2022)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2211.09527) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/agencyenterprise/PromptInject)  | Instruction prompt, In-context learning |
| 🌟⬜️BadPrompt: Backdoor Attacks on Continuous Prompts  |  (NeurIPS, 2022)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2211.14719) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/papersPapers/BadPrompt)  | Instruction prompt|
| ⬜️PromptAttack: Prompt-based Attack for Language Models via Gradient Search  |  (NLPCC, 2022)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2209.01882)  | Instruction prompt |


### Membership Inference Attacks (MIA)
| Paper | Year |  Source         |
|-------|------|-----------------|
| 🌟⬛️Do Membership Inference AttacksWork on Large Language Models?  |  2024.02   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2402.07841) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](http://github.com/iamgroot42/mimir)  |
| ⬛️Assessing Privacy Risks in Language Models: A Case Study on Summarization Tasks  |  2023.10   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2310.13291)  |
| ⬛️Beyond Memorization: Violating Privacy Via Inference with Large Language Models  |  2023.10   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2310.07298) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](http://github.com/iamgroot42/mimir)  |
| ⬜️Extracting Training Data from Large Language Models  |  (USENIX Security, 2021)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf)  | Model Memory |

## Protector Methodology

### Differential Privacy (DP)
| Paper | Year |  Source          |  Tasks  | Defense |
|-------|------|------------------|---------|---------|
| 🌟⬛️Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation  |  (ICLR, 2024)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2309.11765) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/microsoft/dp-few-shot-generation)  | Classification, Information Extraction | 
| 🌟⬛️DP-OPT: Make Large Language Model Your Privacy-Preserving Prompt Engineer  |  (ICLR, 2024)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2312.03724) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/VITA-Group/DP-OPT)  | Sentiment Classification |
| 🌟⬛️Privacy-Preserving In-Context Learning For Large Language Models  |  (ICLR, 2024)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2305.01639)  |  Classification, Document Q&A, Dialog Summarization |
| ⬛️On the Privacy Risk of In-context Learning  |  (TrustNLP, 2024))   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://trustnlpworkshop.github.io/papers/13.pdf)  |  Classification, Generation |  MIA 
| ⬛️InferDPT: Privacy-preserving Inference for Black-box Large Language Models  |  2023.12   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2310.12214) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/mengtong0110/InferDPT) |  Classification, Generation |
| 🌟⬛️⬜️Flocks of Stochastic Parrots: Differentially Private Prompt Learning for Large Language Models  | (NeurIPS, 2023)  | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2305.15594)  | Classification |
| 🌟⬛️Locally Differentially Private Document Generation Using Zero Shot Prompting  |  (EMNLP, 2023)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://aclanthology.org/2023.findings-emnlp.566) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/SaitejaUtpala/dp_prompt)  | Text Classification | 
| ⬜️Privacy-Preserving Prompt Tuning for Large Language Model Services  | 2023.05  | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2305.06212)  | Sentiment Classification, Document Q&A |


### Secure Multi-Party Computing (SMPC)
| Paper | Year |   Source     |    Tasks   | Defence |
|-------|------|--------------|------------|---------|
| ⬜️SecFormer: Towards Fast and Accurate Privacy-Preserving Inference for Large Language Models  |  2024.01   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2401.00793)  | Classification, Semantic Similarity, Linguistic Acceptability | Model Inside |
| ⬜️LLMs Can Understand Encrypted Prompt: Towards Privacy-Computing Friendly Transformers  |  2023.05   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2305.18396)  | Classification | Model Inside |

### Anonymization Techniques
| Paper | Year |  Source     |  Tasks   | Defence |
|-------|------|-------------|----------|---------|
| ⬛️ProPILE: Probing Privacy Leakage in Large Language Models  |  (NeurIPS, 2023)  | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2307.01881) | PII | ALL?
| ⬛️Hide and Seek (HaS): A Lightweight Framework for Prompt Privacy Protection  |  2023.09   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2309.03057)  [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/alohachen/Hide-and-Seek) | PII | ALL? 

### Other Methods
| Paper | Year |  Source               | Tasks | Method Keyword |
|-------|------|-----------------------|-------|----------------|
| ⬛️SEmojiCrypt: Prompt Encryption for Secure Communication with Large Language Models  |  2024.02   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2402.05868) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/agiresearch/EmojiCrypt)  |  Classification | Emoji |
| ⬜️Privatelora For Efficient Privacy Preserving LLM  |  (CoRR, 2023)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2311.14030) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/alipay/private_llm)  | | LoRA 
| Recovering from Privacy-Preserving Masking with Large Language Models  |  2023.12   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2309.08628) |  |[MASK] 

### Related Survey
| Paper | Year |  Source               |
|-------|------|-----------------------|
A Survey on Large Language Model (LLM) Security and Privacy: The Good, the Bad, and the Ugly | 2023.12 | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2312.02003) 
Privacy in Large Language Models: Attacks, Defenses and Future Directions | 2023.10 | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2310.10383) 
Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | 2023.05 | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2302.12173) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/greshake/llm-security)  | 
Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | 2023.05 | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2302.12173) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/greshake/llm-security)  | 
Privacy-Preserving Large Language Models (PPLLMs) | 2023.01 | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://www.researchgate.net/publication/372607103_Privacy-Preserving_Large_Language_Models_PPLLMs) [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/greshake/llm-security)  | 

### Fine-tuning
| Paper | Year |  Source               | 
|-------|------|-----------------------|
| SentinelLMs: Encrypted Input Adaptation and Fine-tuning of Language Models for Private and Secure Inference  |  (AAAI, 2024)   | [![Static Badge](https://img.shields.io/badge/paper-%23B31B1B?logo=arxiv&labelColor=grey)](https://arxiv.org/abs/2312.17342)  [![Static Badge](https://img.shields.io/badge/code-black?logo=github)](https://github.com/abhijitmishra/sentinellm-aaai2024)  
