---
library_name: peft
model_name: lora_adapter
tags:
- base_model:adapter:/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B
- lora
- sft
- transformers
- trl
licence: license
pipeline_tag: text-generation
base_model: /root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B
---

# Model Card for lora_adapter

This model is a fine-tuned version of [None](https://huggingface.co/None).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="None", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 



This model was trained with SFT.

### Framework versions

- PEFT 0.19.0
- TRL: 1.4.0
- Transformers: 4.57.6
- Pytorch: 2.11.0
- Datasets: 4.8.4
- Tokenizers: 0.22.2

## Citations



Cite TRL as:
    
```bibtex
@software{vonwerra2020trl,
  title   = {{TRL: Transformers Reinforcement Learning}},
  author  = {von Werra, Leandro and Belkada, Younes and Tunstall, Lewis and Beeching, Edward and Thrush, Tristan and Lambert, Nathan and Huang, Shengyi and Rasul, Kashif and Gallouédec, Quentin},
  license = {Apache-2.0},
  url     = {https://github.com/huggingface/trl},
  year    = {2020}
}
```