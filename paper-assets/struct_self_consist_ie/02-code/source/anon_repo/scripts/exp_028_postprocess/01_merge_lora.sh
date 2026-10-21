#!/bin/bash
# Merge LoRA adapter into base model using LLaMA Factory export
# Input: checkpoints/qwen3-8b-fewnerd-5epoch-lora/ (best checkpoint, load_best_model_at_end=true)
# Output: checkpoints/qwen3-8b-fewnerd-5epoch-merged/
set -e

source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

# The export config already exists at export_config_fewnerd_5epoch.yaml
# It points to the correct adapter and output paths
echo "Merging LoRA adapter to full model..."
echo "  Base model: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
echo "  Adapter: checkpoints/qwen3-8b-fewnerd-5epoch-lora/"
echo "  Output: checkpoints/qwen3-8b-fewnerd-5epoch-merged/"

llamafactory-cli export export_config_fewnerd_5epoch.yaml

echo "Merge complete. Verifying output..."
ls -la checkpoints/qwen3-8b-fewnerd-5epoch-merged/config.json
echo "Done."
