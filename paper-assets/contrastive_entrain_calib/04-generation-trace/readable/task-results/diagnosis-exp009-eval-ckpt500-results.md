# diagnosis exp009 eval ckpt500 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp009-eval-ckpt500-results_20260520T092809_result.json`
- **Structured JSON:** [`fc31f251433fa7fc6b23.json`](../../sessions/fc/fc31f251433fa7fc6b23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-009 ckpt-500 Eval Results

| Metric | Value |
|--------|-------|
| **ToF** | 0.0663 |
| **NoF** | 0.9337 |
| **SYCONScore** | 0.1238 |
| Samples | 362 (valid=181, invalid=181) |
| Model | Qwen3-8B + LoRA (exp009 checkpoint-500) |
| Eval time | 7671s (~2.1h) |

**结论：ckpt-500 效果很差。** NoF 很高（0.93，几乎不翻转）但 ToF 极低（0.07，该翻也不翻），说明模型变得过度保守/顽固，对 valid correction 也拒绝接受。SYCONScore 0.1238 远低于可用水平。

---

## exp-012 Llama Probe Ablation Details

### 每层 AUROC（dSYC direction, 5-fold CV）

| Layer | AUROC (mean ± std) |
|-------|-------------------|
| **L16** | **0.7778 ± 0.036** ← best single layer |
| L17 | 0.7227 ± 0.042 |
| L18 | 0.7182 ± 0.040 |
| L19 | 0.7161 ± 0.039 |
| L20 | 0.7292 ± 0.039 |
| L21 | 0.7268 ± 0.036 |
| L22 | 0.7318 ± 0.036 |
| L23 | 0.7305 ± 0.034 |
| L24 | 0.7270 ± 0.035 |
| L25 | 0.7366 ± 0.034 |
| L26 | 0.7355 ± 0.033 |
| L27 | 0.7326 ± 0.035 |
| L28 | 0.7329 ± 0.035 |
| L29 | 0.7310 ± 0.035 |
| L30 | 0.7323 ± 0.034 |
| L31 | 0.7454 ± 0.038 |

### Multi-layer probe
- **AUROC: 0.8128 ± 0.032**（16层拼接，5-fold: 0.857/0.836/0.814/0.789/0.768）

### Random direction baseline（L16, 10 seeds）
- Mean AUROC: **0.5301 ± 0.055**（范围 0.455–0.611）
- **Δ(dSYC vs random) = 0.2477**，dSYC direction 显著优于随机方向

### 关键发现
- L16 是最佳单层（0.778），L31 次之（0.745），中间层相对平坦（0.716–0.737）
- Multi-layer 拼接比最佳单层提升 ~3.5 个点（0.813 vs 0.778）
- Random baseline 在 chance 附近（0.530），确认 dSYC direction 非偶然

---
