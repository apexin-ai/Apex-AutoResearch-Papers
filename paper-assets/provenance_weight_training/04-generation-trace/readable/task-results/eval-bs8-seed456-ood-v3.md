# eval bs8 seed456 ood v3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bs8_seed456_ood_v3_20260523T225159_result.json`
- **Structured JSON:** [`a3714393a6c59742e1b3.json`](../../sessions/a3/a3714393a6c59742e1b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## B=8 seed456 完整 eval

| Metric | Adaptive | Uniform | Δ (A-U) |
|--------|----------|---------|---------|
| Holdout PPL | 17.646 | 17.702 | -0.056 |
| OWT PPL | 18.322 | 18.393 | -0.071 |
| Wiki PPL | 15.299 | 15.354 | -0.055 |

OOD 一致性: **方向完全一致**。Adaptive 在所有三个数据集上均优于 Uniform，差异幅度也一致（Δ PPL 在 -0.055 ~ -0.071 范围内）。OOD 泛化趋势与 holdout 一致，adaptive weighting 的优势不限于训练分布内数据。

之前两次失败原因：wiki eval 比 OWT 慢 2-3x（27M tokens vs 6.77M, ~420s vs ~180s），ssh_execute 30s 超时导致 tee 管道断开，进程继续运行但输出丢失。这次用 nohup + 文件重定向解决。

---
