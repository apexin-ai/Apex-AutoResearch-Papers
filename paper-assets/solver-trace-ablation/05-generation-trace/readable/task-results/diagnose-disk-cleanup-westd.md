# diagnose disk cleanup westd

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_disk-cleanup-westd_20260515T135142_result.json`
- **Structured JSON:** [`5b3508e952f90ca0b7a4.json`](../../sessions/5b/5b3508e952f90ca0b7a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 磁盘状态：**不需要清理**

| 存储位置 | 总大小 | 已用 | 可用 | 使用率 |
|----------|--------|------|------|--------|
| /root/autodl-tmp (XFS 数据盘) | 250GB | ~17GB | ~234GB | 7% |
| overlay (/) | 30GB | 9.1GB | 21GB | 31% |

之前的 250G/250G 满盘问题已被解决（可能之前已清理过）。当前可用空间充足。

### 磁盘使用明细

| 目录 | 大小 | 说明 |
|------|------|------|
| models/Qwen3-4B | 7.6G | base model |
| models/Qwen3-4B-ms | 7.6G | 同一模型的 ModelScope 副本（重复） |
| outputs/ | 207M | 实验输出（无大 checkpoint，仅 logs） |
| .ms_cache | 703M | ModelScope 缓存 |
| .hf_cache | 105M | HuggingFace 缓存 |

### 两个实验已经在跑

两个实验**已经被提交并在运行中**：

| 实验 | GPU | PID | 当前步数 | 目标步数 |
|------|-----|-----|----------|----------|
| plan001_exec_only_s43_1000_r2 | GPU 0 (80GB/98GB) | 363697 | step 8 | 1000 |
| plan001_exec_only_s44_1000_r2 | GPU 1 (80GB/98GB) | 363845 | step 5 | 1000 |

两张 GPU 利用率 94%，训练正常进行中。

### 可选清理（不影响训练，无需立即执行）

| 项目 | 大小 | 建议 |
|------|------|------|
| models/Qwen3-4B-ms（重复副本） | 7.6GB | 确认不再需要后可删 |
| .ms_cache | 703MB | 模型已下载完可清 |

**结论**：磁盘空间充足（234GB 可用），足够跑两个实验。两个实验已在运行中，无需额外操作。

---
