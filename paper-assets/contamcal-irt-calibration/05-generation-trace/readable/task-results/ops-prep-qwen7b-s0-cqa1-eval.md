# ops prep qwen7b s0 cqa1 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-qwen7b-s0-cqa1-eval_20260520T202810_result.json`
- **Structured JSON:** [`9e8f0d5d3c45d86130a0.json`](../../sessions/9e/9e8f0d5d3c45d86130a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. eval 环境就绪状态

| 项目 | 状态 |
|------|------|
| evaluate.py | `/root/contamcal-irt-calibration/exp001/evaluate.py` — md5=`001a9bc23f808c47d25ef9eaeecb81f1`, 37591 bytes，与 reference hash 一致 (C009) |
| MMLU 数据集 | 已缓存，14042 test + 1531 val |
| ARC-Challenge 数据集 | 已缓存，1172 test + 299 val |
| Python/conda | `/root/miniconda3/bin/python` (conda base) |
| GPU | RTX 4090D 24GB，cuda:0 当前在训练 (PID 389216, 20GB) |

### 2. 脚本路径

- MMLU: `/root/contamcal-irt-calibration/scripts/eval_qwen7b_s0_mmlu_cqa1.sh`
- ARC: `/root/contamcal-irt-calibration/scripts/eval_qwen7b_s0_arc_cqa1.sh`

两个脚本均遵守 C004 (显式 CUDA_VISIBLE_DEVICES=0)、C006 (lora_alpha=32 检查)、C009 (evaluate.py md5 校验)。输出到 `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_{dosage}_s0/`。已有结果会自动跳过。

### 3. 需注意的问题

- **d100_s0 尚未完成训练**：d000-d050 的 lora_adapter 已就绪，d100_s0/lora_adapter/ 目录为空。脚本会自动 SKIP 未就绪的 checkpoint，等 d100 训练完写出 adapter_config.json 后可重跑补上。
- **运行方式**：训练完成后，先跑 MMLU 再跑 ARC（串行），预计 MMLU ~10min/dosage × 5 + ARC ~5min/dosage × 5 ≈ 75min 总计。

---
