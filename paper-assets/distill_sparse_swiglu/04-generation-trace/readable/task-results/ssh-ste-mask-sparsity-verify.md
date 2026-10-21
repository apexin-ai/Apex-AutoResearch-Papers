# ssh ste mask sparsity verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ste_mask_sparsity_verify_20260520T184606_result.json`
- **Structured JSON:** [`1552c1aac554e78f41e2.json`](../../sessions/15/1552c1aac554e78f41e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰。完整结论如下：

---

## STE 30% Per-Layer Mask Sparsity — 确认问题严重

**STE predictor (s42, uniform, target=0.30)**:

| Layer | Actual | Layer | Actual | Layer | Actual | Layer | Actual |
|-------|--------|-------|--------|-------|--------|-------|--------|
| 0 | 0.172 | 8 | 0.207 | 16 | **0.098** | 24 | 0.207 |
| 1 | 0.180 | 9 | 0.215 | 17 | **0.090** | 25 | 0.277 |
| 2 | 0.266 | 10 | 0.191 | 18 | 0.293 | 26 | 0.277 |
| 3 | 0.266 | 11 | 0.219 | 19 | 0.156 | 27 | 0.301 |
| 4 | 0.242 | 12 | 0.191 | 20 | 0.148 | 28 | 0.285 |
| 5 | 0.188 | 13 | **0.109** | 21 | 0.215 | 29 | 0.289 |
| 6 | 0.168 | 14 | 0.191 | 22 | 0.188 | 30 | 0.238 |
| 7 | 0.195 | 15 | **0.121** | 23 | 0.168 | 31 | 0.301 |

**Model-level: 0.208（目标 0.300）**

Layer 13-17 最严重，sparsity 只有 9-12%，意味着保留了 88-91% 的 neurons。

### 根因确认

`_uniform_topk_masks`（evaluate.py:146）用 `(s >= thr)` 做 mask。STE predictor 的 sigmoid 输出大量饱和在接近 1.0，导致大量 neurons 共享相同 score，`>=` 把所有 tied scores 全部保留。

### KL+Gumbel predictor 对比——无此问题

| 配置 | 所有层 sparsity 范围 | Model-level |
|------|---------------------|-------------|
| KL s42 uniform | 0.289 – 0.301 | **0.296** |
| KL s123 uniform v2 | 0.301（全部） | **0.300** |

KL predictor 的 scores 分布良好，无 tied-score 问题。

### 影响

STE 30% eval 的所有指标（PPL 8.41, ARC 48.5%, MMLU 44.0% 等）实际是在 **~20.8% sparsity** 下取得的，不是 30%。与 KL predictor（实际 ~30%）的对比不公平。

---

## KL50 s456 Eval 结果

已完成（2026-05-21 01:34）:

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | 12.01 |
| ARC-C (acc_norm) | 36.9% |
| WinoGrande | 64.0% |
| MMLU | 28.0% |
| GSM8K | 3.5% |
| HellaSwag (acc_norm) | 59.5% |
| PIQA (acc_norm) | 68.0% |

---
