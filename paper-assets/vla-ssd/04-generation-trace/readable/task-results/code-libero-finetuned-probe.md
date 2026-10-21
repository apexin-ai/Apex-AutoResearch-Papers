# code libero finetuned probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_finetuned_probe_20260519T072300_result.json`
- **Structured JSON:** [`d98d00021baa6eb2a766.json`](../../sessions/d9/d98d00021baa6eb2a766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册。

**任务状态**：
- **实验 ID**：`finetuned_probe_profile`，状态 RUNNING
- **PID**：118788 on westd-19183 (cuda:0)
- **脚本**：`/root/vla-ssd/scripts/libero_finetuned_probe_profile.py`
- **日志**：`/root/autodl-tmp/vla-ssd/results/finetuned_probe_profile.log`

**Pipeline**：
1. Phase 1 (Feature Extraction)：从 fine-tuned checkpoint 提取 32 层 hidden states，10 tasks × 50 demos × 10 instructions = 5000 forward passes，~22 fwd/s，估计 ~40 分钟
2. Phase 2 (LOOCV Probe)：对 32 层 × 2 token positions 做 10-fold leave-one-task-out CV (PCA256 + LogReg)，估计 ~10 分钟

**结果输出**：`/root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json`，含 per_layer_accuracy (L0-L31)、LOOCV mean/std、4-condition comparison table。

---
