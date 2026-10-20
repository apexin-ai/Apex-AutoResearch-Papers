# fix plan 011 bf16 g8 step eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_011_bf16_g8_step_eval_20260515T195613_result.json`
- **Structured JSON:** [`57bbb95087d4f7c995ab.json`](../../sessions/57/57bbb95087d4f7c995ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Orphan 清理**: 已完成。pid 247234 是 bash wrapper，实际 GPU 进程在子进程树中（父进程 246980/247239 不断重启子进程）。已 kill -9 整个进程树（246980, 247239, 248423, 248424, 247234）。

**cuda:1 状态**: 完全空闲，0 MiB / 32607 MiB。可用。

**GPU 全局状态**:
| GPU | 已用 | 总量 |
|-----|------|------|
| 0 | 16287 MiB | 32607 MiB |
| 1 | **0 MiB** | 32607 MiB |
| 2 | 22189 MiB | 32607 MiB |
| 3 | 20093 MiB | 32607 MiB |

**空产物目录**: `/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30` 已删除。

**Eval 脚本内容** (`/root/autodl-tmp/freige/scripts/eval_plan_011_steps.sh`):

```bash
#!/bin/bash
set -e

CKPT_BASE="/root/autodl-tmp/grpo_ced_g8_bf16"
BASE_MODEL="/root/autodl-tmp/models/Qwen3-4B"
SFT_ADAPTER="/root/autodl-tmp/sft_output"
DATA_PATH="/root/autodl-tmp/data/docred"
OUTPUT_BASE="/root/autodl-tmp/eval_results/plan_011_bf16_g8"

cd /root/autodl-tmp

for STEP in 30 50 70; do
    CKPT_DIR="${CKPT_BASE}/checkpoint-${STEP}"
    OUTPUT_DIR="${OUTPUT_BASE}_step${STEP}"

    if [ ! -d "$CKPT_DIR" ]; then
        echo "=== SKIP step ${STEP}: checkpoint not found at ${CKPT_DIR} ==="
        continue
    fi

    python -m freige.eval.inference \
        --model_path "$CKPT_DIR" \
        --sft_adapter "$SFT_ADAPTER" \
        --base_model "$BASE_MODEL" \
        --data_path "$DATA_PATH" \
        --split dev \
        --batch_size 16 \
        --max_new_tokens 1024 \
        --seed 42 \
        --output_dir "$OUTPUT_DIR" \
        --no-quantize

    echo "=== Step ${STEP} DONE ==="
done
```

脚本循环评估 step 30/50/70 三个 checkpoint，每个调用 `freige.eval.inference`。可以用 `submit_training_job` 重提交到 cuda:1。

---
