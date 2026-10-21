# ops westb monitor disk and progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_monitor_disk_and_progress_20260519T070754_result.json`
- **Structured JSON:** [`9095b843da36b6a8c4c6.json`](../../sessions/90/9095b843da36b6a8c4c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控汇总

### 1. 磁盘空间
- **可用：9.5GB / 250GB（97% 使用）**
- seed123 当前仅写了 40KB（2 个 completions parquet 文件），GRPO 训练不保存中间 checkpoint（只存 completions），**磁盘暂无风险**
- 但余量紧张（9.5GB），100 步训完后如果保存最终 checkpoint（约 12GB），空间不够

**可清理候选**（仅报告，不删除）：
| 目录 | 大小 | 说明 |
|---|---|---|
| `pruned_unstructured_20/` | 15G | 未剪枝的 unstructured baseline |
| `grpo_unstructured_20/` | 15G | unstructured GRPO 训练产物（eval 正在读，暂不动） |
| `sft_*` 系列（6个×12G） | ~72G | SFT 中间产物，如已不再需要可清理 |

### 2. seed123 训练进度
- **29/100 步，进度 29%**
- 速度：~416 秒/步
- 已运行 3h22m，预估剩余 **~8h12m**
- GPU cuda:1 占用 67.9GB/97.9GB，100% 利用率，运行正常

### 3. unstructured GSM8K eval
- **PID 865250 存活**，CPU 100%，已运行约 143 分钟
- GPU cuda:0 占用 17.7GB/97.9GB，83% 利用率
- 日志文件为空（eval 可能完成后一次性写结果），进程在跑说明还没结束

### 风险提示
- **磁盘是主要风险**：seed123 训完后保存 checkpoint 需约 12GB，当前仅剩 9.5GB。需要在训练完成前（~8h 后）清理至少 3GB 空间，或确认脚本是否会自动保存 checkpoint。

---
