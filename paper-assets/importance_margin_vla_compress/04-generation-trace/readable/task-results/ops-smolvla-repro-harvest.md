# ops smolvla repro harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_smolvla_repro_harvest_20260522T110248_result.json`
- **Structured JSON:** [`de70442fe76502753d6c.json`](../../sessions/de/de70442fe76502753d6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture assembled. Here are the results.

## SmolVLA 官方权重实验结果 (libero_object, 500 episodes, seed=42)

### Remove (true_removal) — 完整结果

| 实验 | Method | Mode | k | SR | Episodes | 备注 |
|------|--------|------|---|-----|----------|------|
| baseline | none | — | 1.0 | **57.2%** | 500/500 | 官方权重 `smolvla_libero` |
| random_k095 | random | remove | 0.95 | **0.0%** | 500/500 | |
| random_k090 | random | remove | 0.9 | **0.0%** | 500/500 | |
| random_k070 | random | remove | 0.7 | **0.0%** | 500/500 | |
| random_k050 | random | remove | 0.5 | **0.0%** | 500/500 | |
| random_k030 | random | remove | 0.3 | **0.0%** | 500/500 | |
| l2norm_k095 | l2_norm | remove | 0.95 | **0.4%** | 500/500 | 仅 2 eps 成功 |
| l2norm_k090 | l2_norm | remove | 0.9 | **0.0%** | 500/500 | |
| l2norm_k070 | l2_norm | remove | 0.7 | **0.0%** | 500/500 | |
| l2norm_k050 | l2_norm | remove | 0.5 | **0.0%** | 500/500 | |
| l2norm_k030 | l2_norm | remove | 0.3 | **0.0%** | 500/500 | |

### Replace (zero_mask) — 缺失

**Replace/zero_mask 实验完全没有运行。** 之前的 Worker 所有实验都用了 `method="true_removal"`（物理删除 token），没有做 `zero_mask`（token 置零但保持 sequence length 不变）。

### 当前运行的进程

服务器上有 2 个 **Pi0.5** baseline 实验在跑（不是 SmolVLA）：
- GPU 0: `pi05 baseline libero_goal seed42` — 已完成 T0(0%) T1 进行中(0/40)
- GPU 2: `pi05 baseline libero_10 seed42` — 已完成 T0(0%) T1 进行中(0/10)

这两个 Pi0.5 实验目前 SR=0%，与 SmolVLA 实验无关。

### 诊断结论

**无法回答 "position shift vs token info loss" 问题**——因为 Replace 实验缺失。

现有 Remove 结果表明：SmolVLA 对 true_removal 极度脆弱，即使只删 5% token（k=0.95），SR 就从 57.2% 直接跌到 0%。但这不能区分原因：
- true_removal 同时改变了 sequence length（position shift）和 token content
- 需要 zero_mask 实验来分离这两个因素

代码已经支持 zero_mask mode — `geometric_prior_pruning.py:122` 中 `else` 分支会做 `tokens * mask`（保持 seq len）。只需把 `method` 参数从 `"true_removal"` 改成任意其他值（如 `"zero_mask"`）即可。

**需要补跑的实验：**
- Replace(zero_mask) random k=0.95
- Replace(zero_mask) random k=0.9

---
