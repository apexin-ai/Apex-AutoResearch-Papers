# analysis exp 004 reduced lora

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-reduced-lora_20260523T082657_result.json`
- **Structured JSON:** [`7d79c870b266bce0ec0b.json`](../../sessions/7d/7d79c870b266bce0ec0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键结论：

- **训练正常完成**：8000/8000 steps，EXIT_CODE=0，耗时 15.7h
- **checkpoint-8000 存在**（adapter 245MB）
- **SYCONScore 轨迹**：全部 checkpoint 均显著 > vanilla baseline (0.056)，peak 在 ckpt-7000 = **0.3257**，ckpt-7500 = 0.3043（略有回落）
- **ckpt-7500 eval 已完成**：SYCONScore=0.3043, ToF=0.1878, NoF=0.8011
- **ckpt-8000 eval 未完成**（目录为空）
- **无 W&B logging**
- **conclusion: success** — Reduced-LoRA（0.74% 可训练参数）仍然有效，支持 "per-token SFT supervision granularity 是关键因素，而非 LoRA capacity" 的假设

报告已写入 `artifacts/exp004_reduced_lora_analysis.md` 并注册。

---
