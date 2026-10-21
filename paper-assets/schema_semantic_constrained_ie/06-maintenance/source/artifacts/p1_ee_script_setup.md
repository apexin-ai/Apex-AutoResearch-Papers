# P1 EE FT Script Setup Report

Server: westd-21461 | Date: 2025-05-19

## Phase 1: File Check Results

### 1. Kill residual processes
```
pkill -f train_lora_wikievents -> exit -1 (no matching process)
```

### 2. Script existence
| File | Status | Size | Modified |
|------|--------|------|----------|
| `run_constrained_extraction.py` | EXISTS | 41098 | May 18 19:48 |
| `eval_event_extraction.py` | EXISTS | 6984 | May 17 23:03 |
| `violation_checker_wikievents.py` | EXISTS | 14445 | May 18 04:09 |
| `scripts/train_lora_wikievents.py` | EXISTS | - | - |

**All 4 scripts exist. No missing files.**

### 3. Test data
```
/root/schema_semantic_constrained_ie/data/wikievents/test.jsonl  (1087406 bytes, May 18)
/root/schema_semantic_constrained_ie/data/wikievents/test_5docs.jsonl
/root/schema_semantic_constrained_ie/data/processed_data/test.json
```

### 4. Ontology constraints
```
/root/schema_semantic_constrained_ie/data/wikievents/ontology_constraints_wikievents.json
/root/schema_semantic_constrained_ie/data/wikievents/aida_ontology_cleaned.csv
/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json
```

### 5. SFT training data
```
data/sft/wikievents_sft_train.jsonl  (1817764 bytes, May 19)
data/sft/wikievents_sft_dev.jsonl    (173780 bytes, May 19)
```

### 6. Checkpoints directory
Empty (training not yet run).

### 7. Model
Qwen/Qwen3-8B cached in `/root/.cache/huggingface/hub/models--Qwen--Qwen3-8B`.

### 8. Outputs directory
EXISTS with many prior experiment outputs.

## Actual Paths Used

| Resource | Path |
|----------|------|
| Test data | `data/wikievents/test.jsonl` |
| Constraints | `data/wikievents/ontology_constraints_wikievents.json` |
| Train data | `data/sft/wikievents_sft_train.jsonl` |
| Dev data | `data/sft/wikievents_sft_dev.jsonl` |
| LoRA output | `checkpoints/qwen3_8b_lora_wikievents/` |
| Merged output | `checkpoints/qwen3_8b_lora_wikievents_merged/` |

## Script Written

Location: `/root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh`

```bash
#!/bin/bash
set -eo pipefail

# 环境
source /root/miniconda3/bin/activate
export CUDA_VISIBLE_DEVICES=0
export WANDB_DISABLED=true

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

## Dry-run Results

```
python3: /root/miniconda3/bin/python3
Python 3.12.3
torch OK 2.8.0+cu128
cuda True
```

Environment verified. 2 GPUs available (script uses GPU 0 only).

## Missing Files

**None.** All scripts, data, constraints, and model are present. All 5 steps can execute.
