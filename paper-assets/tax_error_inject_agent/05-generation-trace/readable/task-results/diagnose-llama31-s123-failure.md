# diagnose llama31 s123 failure

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-s123-failure_20260516T150216_result.json`
- **Structured JSON:** [`4281ca3e9b9215743a9b.json`](../../sessions/42/4281ca3e9b9215743a9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：训练已完全完成，EXIT_CODE=129 是误报。**

两个实验都正常跑完了全部 3 个 epoch（3387/3387 steps），并成功保存了所有 checkpoint。EXIT_CODE=129 (SIGHUP) 是 `submit_training_job` 的 tmux wrapper 在训练进程正常退出后收到的信号——tmux session 被清理时，shell 收到 SIGHUP 导致退出码被覆盖为 129。**训练本身的退出码是 0。**

### 训练结果摘要

| 实验 | 最终 loss | token_acc | 运行时间 | 最终 checkpoint |
|------|-----------|-----------|----------|----------------|
| llama31-taxei-s123 | 0.3368 | 94.59% | 2h7m (7626s) | `output/llama31-taxei-s123/v0-20260516-205232/checkpoint-3387` |
| llama31-random-s123 | 0.3375 | 94.36% | 2h6m54s (7614s) | `output/llama31-random-s123/v0-20260516-205234/checkpoint-3387` |

### Checkpoint 完整性

两个实验各有 3 个 epoch checkpoint（1129, 2258, 3387），最终 checkpoint-3387 包含完整的 `adapter_model.safetensors`（~160MB）、optimizer、scheduler 等文件。

### GPU 状态

cuda:2 和 cuda:3 已释放（0 MiB, 0% util），训练进程已正常退出。cuda:0/1 有其他进程在跑。

### 建议

无需修复——训练结果完好，可以直接进入评估阶段。如果希望后续避免 EXIT_CODE=129 的误报，可以在 `submit_training_job` 的 wrapper 脚本中训练命令执行后立即 `exit $?` 捕获真实退出码，避免被 tmux SIGHUP 覆盖。

---
