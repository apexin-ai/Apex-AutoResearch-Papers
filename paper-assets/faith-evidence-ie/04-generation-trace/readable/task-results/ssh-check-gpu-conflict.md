# ssh check gpu conflict

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_conflict_20260516T053100_result.json`
- **Structured JSON:** [`3630ff931761665f1f41.json`](../../sessions/36/3630ff931761665f1f41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

### 各 GPU 占用

| GPU | 显存占用 | GPU Util | 进程 |
|-----|----------|----------|------|
| 0 | 21706 / 32607 MiB | 86% | PID 296737 (10846M) + PID 297195 (10846M) |
| 1 | 10149 / 32607 MiB | 34% | PID 303070 (10140M) — sft_baseline_d076_reeval, 运行 4m |
| 2 | 10855 / 32607 MiB | 50% | PID 298023 (10846M) — rsft_ced_s42_reeval, 运行 1h07m |
| 3 | 11091 / 32607 MiB | 47% | PID 291008 (11082M) — rsft_flat_nli_s43_reeval_r2, 运行 2h26m |

### 双进程冲突确认

两个 PID 均存活：
- **296732** (reeval_flat_nli_s42): 运行 1h14m, 子进程 PID 296737 占 GPU 0
- **297190** (reeval_ced_s44): 运行 1h12m, 子进程 PID 297195 占 GPU 0

两者共用 cuda:0，合计 ~21.7GB / 32GB，未 OOM。

### 日志状态

- **reeval_flat_nli_s42**: 87/247 (35%), ~50s/it，无错误
- **reeval_ced_s44**: 88/247 (36%), ~55s/it，无错误

两个都在正常推进，没有 OOM 或报错。

### 分析与建议

**当前不需要 kill。** 原因：
1. 两个 eval 各占 ~10.8GB，合计 21.7GB 在 32GB 内，没有 OOM 风险
2. 都已完成 ~35%，kill 重启会浪费已有进度
3. **4 张 GPU 全部被占用**（GPU 1/2/3 各有一个 eval），没有空闲卡可迁移
4. GPU 0 利用率 86% 说明两者在争抢算力，速度比独占慢约 40-50%，但都在推进

**预计完成时间**：按当前速度，两者各剩 ~160 batch × ~55s ≈ 2.5h，约 16:00 UTC 完成。

**根因**：提交时未检查 cuda:0 是否已有任务，两个 eval 被分配到同一张卡。后续应在提交前 `nvidia-smi` 确认目标 GPU 空闲（C001 约束）。

---
