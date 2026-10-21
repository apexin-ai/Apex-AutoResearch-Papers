# diag wave1 rescue

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_wave1-rescue_20260517T062033_result.json`
- **Structured JSON:** [`37a0d687e30a485edcd5.json`](../../sessions/37/37a0d687e30a485edcd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 状态
两张 RTX PRO 6000 (98GB each) **均空闲**，0MiB 使用，0% utilization。

### plan018-random-b01-s45 (Random β=0.1 s45)
**状态：中途崩溃** — 在 step 209/500 (42%) 因 `/` 根分区满 (`No space left on device`) 崩溃。
- 存在 checkpoint-200，无 checkpoint-500
- 训练脚本无 resume 支持，根据 C012 需**从 base model 重新训练**

### sweep-random-b005-s42 (Random β=0.05 s42)
**状态：中途崩溃** — 在 step 301/500 (60%) 因同样的磁盘满错误崩溃。
- 存在 checkpoint-300，无 checkpoint-500
- config 文件 `grpo_additive_random_b005.yaml` 存在但 `output_dir` 指向旧实验路径，需修正
- 同样需**从 base model 重新训练**

### 根因与修复
`/tmp/dryrun` 目录占用 21G 撑满了 30G 根分区。**已清理**，根分区恢复到 31% (21G 可用)。`/root/autodl-tmp` 有 31G 可用。

### 重启前需要做的
1. 删除两个失败实验的 checkpoint 释放 autodl-tmp 空间（plan018_random_b01_s45 占 16G，sweep_random_b005_s42 占 16G）
2. 为 sweep_random_b005_s42 修正 config（output_dir 指向错误路径）
3. 两个实验可并行各占一张 GPU 重训

需要我执行清理和重启吗？

---
