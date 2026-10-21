# code d37g task degradation eval

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d37g_task_degradation_eval_20260521T065805_result.json`
- **Structured JSON:** [`e9ed11d2686f2c11a760.json`](../../sessions/e9/e9ed11d2686f2c11a760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both dry-runs passed. The degradation signal is already visible even on 2 samples:
- **Baseline (pretrained)**: PPL=14.63, Acc=0.459, rep_2=0.089
- **α=0.50 gen_10**: PPL=23.13, Acc=0.427, rep_2=0.142

---

## 汇报

### 脚本
`/root/autodl-tmp/distrib_canary_collapse/eval_task_degradation.py` — 190 行，三项指标（perplexity, next-token accuracy, repetition rate），支持 `--dry_run`。

### 可用 Checkpoints（s42_fp32 主线，有 gen_10）
| α | 实验目录 |
|---|---------|
| 0.05 | a005_s42_fp32_v3_d080 |
| 0.10 | a010_s42_fp32 |
| 0.25 | a025_s42_fp32 |
| 0.30 | a030_s42_fp32 |
| 0.35 | a035_s42_fp32 |
| 0.40 | a040_s42_fp32 |
| 0.45 | a045_s42_fp32 |
| 0.46 | a046_s42_fp32 |
| 0.48 | a048_s42_fp32 |
| **0.50** | a050_s42_fp32 |
| 0.52 | a052_s42_fp32 |
| 0.60 | a060_s42_fp32_v4 |
| 0.65 | a065_s42_fp32 |
| 0.70 | a070_s42_fp32 |
| 0.75 | a075_s42_fp32 |

**+ 3 个 C4 实验** (c4_a025/a050/a075_s42_fp32)，**+ baseline** (results/baseline_pythia410m)。

共 **19 个 checkpoint** 需评估（1 baseline + 15 wikitext α + 3 C4 α）。

### 预估 GPU 时间
基于 dry-run 外推（CPU 上 2 samples ≈ 14s，GPU 上 500 samples 考虑 batch 并行）：
- **PPL+Acc (500 samples, batch=8)**: ~15-20s/checkpoint on GPU
- **Generation (100 samples)**: ~2-3 min/checkpoint on GPU (sequential generation)
- **总计每 checkpoint**: ~3-4 min
- **19 checkpoints 总计**: **~60-75 min** on single GPU

### 显存需求
Pythia-410M fp32 = 1.6GB，推理 overhead ~1GB → **~3GB VRAM**，6× 98GB GPU 完全够用。

---
