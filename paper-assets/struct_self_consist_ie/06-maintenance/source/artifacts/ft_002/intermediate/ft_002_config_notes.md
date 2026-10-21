train_config_v2.yaml on autodl-5090:/root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml

Changes vs ft_001:
- LoRA rank: 16 → 32, alpha: 32 → 64 (trainable params: ~43M → 87.3M)
- Epochs: 3 → 5 (total steps: 585)
- Added relation direction hint to prompt: "For relations, head is the subject entity and tail is the object entity."
- Data backup: llmfactory_{train,dev}_v1.json