# ssh p1 ee patch offline env

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_ee_patch_offline_env_20260518T203948_result.json`
- **Structured JSON:** [`901fe89d5bafe12b63ba.json`](../../sessions/90/901fe89d5bafe12b63ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。完整脚本内容：

```bash
#!/bin/bash
set -eo pipefail

# 环境
source /root/miniconda3/bin/activate
export CUDA_VISIBLE_DEVICES=0
export WANDB_DISABLED=true
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1

PROJECT=/root/schema_semantic_constrained_ie
cd "$PROJECT"

echo "=== ENV CHECK ==="
echo "python3: $(which python3)"
python3 --version
echo "torch: $(python3 -c 'import torch; print(torch.__version__)')"
echo "CUDA: $(python3 -c 'import torch; print(torch.cuda.is_available())')"
nvidia-smi
echo "pwd: $(pwd)"

echo "=== STEP 1: TRAINING ==="
python3 scripts/train_lora_wikievents.py 2>&1
echo "=== TRAINING DONE ==="
ls -la checkpoints/qwen3_8b_lora_wikievents/ || { echo "FATAL: no LoRA checkpoint"; exit 1; }
ls -la checkpoints/qwen3_8b_lora_wikievents_merged/ || { echo "FATAL: no merged checkpoint"; exit 1; }

echo "=== STEP 2: UNCONSTRAINED INFERENCE ==="
python3 run_constrained_extraction.py \
    --dataset wikievents \
    --mode unconstrained \
    --model_path checkpoints/qwen3_8b_lora_wikievents_merged \
    --data_path data/wikievents/test.jsonl \
    --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl \
    --device cuda:0 2>&1

echo "=== STEP 3: CONSTRAINED INFERENCE (full_s1) ==="
python3 run_constrained_extraction.py \
    --dataset wikievents \
    --mode full_s1 \
    --model_path checkpoints/qwen3_8b_lora_wikievents_merged \
    --data_path data/wikievents/test.jsonl \
    --constraints_path data/wikievents/ontology_constraints_wikievents.json \
    --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl \
    --device cuda:0 2>&1

echo "=== STEP 4: EVAL ==="
python3 eval_event_extraction.py \
    --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl \
    --output_path outputs/eval_report_unconstrained.json 2>&1
python3 eval_event_extraction.py \
    --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl \
    --output_path outputs/eval_report_full_s1.json 2>&1

echo "=== STEP 5: VIOLATION CHECK ==="
python3 violation_checker_wikievents.py \
    --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl \
    --constraints_path data/wikievents/ontology_constraints_wikievents.json \
    --output_path outputs/violation_report_ft_unconstrained.json 2>&1
python3 violation_checker_wikievents.py \
    --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl \
    --constraints_path data/wikievents/ontology_constraints_wikievents.json \
    --output_path outputs/violation_report_ft_full_s1.json 2>&1

echo "=== ALL STEPS COMPLETE ==="
```

两行环境变量已正确插入在 `export WANDB_DISABLED=true` 之后。

---
