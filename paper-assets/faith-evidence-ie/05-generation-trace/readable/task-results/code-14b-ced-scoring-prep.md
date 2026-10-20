# code 14b ced scoring prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-ced-scoring-prep_20260520T170537_result.json`
- **Structured JSON:** [`4c79a8af620a2069fea4.json`](../../sessions/4c/4c79a8af620a2069fea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇报如下：

---

## 1. 当前 generation 数据状态

| 文件 | 行数 | unique docs | 说明 |
|------|------|-------------|------|
| `generations.jsonl` | 22,688 | 2,836 | 主文件，r4 --resume 持续追加 |
| `generations_old.jsonl` | 14,976 | 1,872 | 旧备份，完全被 generations.jsonl 包含 |
| progress.json | — | 2,836 completed | 剩余 191 docs |

每 doc 8 个候选样本。完成后预计 3027 × 8 = 24,216 行（与 4B 的 24,216 一致）。

## 2. 数据合并方案

**不需要合并**。`generations_old.jsonl` 的 1,872 docs 全部已在 `generations.jsonl` 中（overlap=1872, only_old=0）。r4 --resume 直接往 `generations.jsonl` 追加，是单一数据源。

## 3. CED scoring 脚本

已有现成脚本：`/root/autodl-tmp/freige/scripts/plan017/step2_ced_score_14b.sh`

```bash
#!/bin/bash
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/freige

export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

python -m freige.training.rsft_score_filter \
    --input_dir "/root/autodl-tmp/rsft_generations_14b" \
    --output_path "/root/autodl-tmp/rsft_scored_14b" \
    --nli_model_path "cross-encoder/nli-deberta-v3-base" \
    --selection_strategy top_k \
    --top_k 1 \
    --scoring_mode ced
```

参数与 4B scoring 完全一致。NLI 模型已缓存在 HF_HOME。脚本无需修改。

运行方式（遵守 C001/C002）：
```bash
# 先 nvidia-smi 确认目标 GPU 空闲
GPU=X bash /root/autodl-tmp/freige/scripts/plan017/step2_ced_score_14b.sh
```

## 4. 预估运行时间

CED scoring 瓶颈是 NLI DeBERTa 推理，与 generation 模型大小无关。14B 和 4B 数据量相同（~24K records），预估 **15-30 分钟**（单 GPU，DeBERTa-base 推理 24K 条文本对）。

## 5. 参考：4B CED scoring 结果

- 24,216 records → 选出 3,014 docs（top_k=1，12 docs 因 f1 < 0.1 被过滤）
- selected 平均 f1: 0.676, ced: 0.676, combined: 0.741

---
