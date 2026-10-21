# diagnose exp1 isr b03 s42 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp1-isr-b03-s42-1000_20260515T092630_result.json`
- **Structured JSON:** [`3ab812ad64a4f0f34ce3.json`](../../sessions/3a/3ab812ad64a4f0f34ce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Root Cause（两个实验相同）

**磁盘满：`/root/autodl-tmp/` 250G/250G (100%)，保存 checkpoint 时写入 safetensors 文件失败。**

错误：`safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)`

两个实验在 `_save_checkpoint` 时 crash：
- `exp1-isr-b03-s42-1000`：step 50 保存时崩溃（仅训练了 ~7 分钟）
- `plan018-additive-random-b01-s42-1000`：step 400 保存时崩溃（训练了 ~54 分钟）

### Checkpoint 状态

| 实验 | Checkpoint | 完整性 |
|------|-----------|--------|
| exp1-isr-b03-s42-1000 | checkpoint-50 (4.7G) | **不完整** — 只有 2/4 safetensors shard（缺 shard 3、4），不可用 |
| plan018-additive-random-b01-s42-1000 | checkpoint-350 (16G) | **可能完整**（需验证） |
| plan018-additive-random-b01-s42-1000 | checkpoint-400 (14G) | **不完整** — 只有 3/4 shard，不可用 |

注意：plan018 有 2 个 checkpoint，说明 `save_total_limit` 可能未设为 1，违反 **C003**。

### 磁盘空间分析

当前 `/root/autodl-tmp/outputs/` 下大户：
- `exp1_random_b03_s43_r4`: 31G
- `exp1_random_b03_s44_r2`: 31G
- `plan002_additive_b01_s42_1000`: 31G
- `plan004_fast_isr_s42`: 31G
- `plan009_sft_baseline_s43`: 30G
- `plan009_sft_baseline_s44`: 30G
- `plan018_additive_random_b01_s42_1000`: 29G
- `exp1_random_b03_s43_r2`: 15G

共 ~228G 被 outputs 占用。

### 修复建议

1. **清理磁盘**：需要先清理不再需要的旧 checkpoint。按 C010/C011，删前必须检查 registry 状态，不能删 `conclusion=success` 且 `needs-re-eval` 的 checkpoint。
2. **删除不完整的 checkpoint**：
   - `exp1_isr_b03_s42_1000/checkpoint-50`（不完整，4.7G）
   - `plan018_additive_random_b01_s42_1000/checkpoint-400`（不完整，14G）
3. **确认 save_total_limit=1**：plan018 保存了 checkpoint-350 和 checkpoint-400，说明配置有问题。
4. 清出足够空间后才能重试。

**不能直接重试**，必须先清磁盘。需要你确认哪些旧实验可以清理。

---
