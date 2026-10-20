# ops d084 kill orphan and submit signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d084-kill-orphan-and-submit-signals_20260515T231551_result.json`
- **Structured JSON:** [`b925819d18d5b228e0c2.json`](../../sessions/b9/b925819d18d5b228e0c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### 1. Orphan Kill
**ALREADY_DEAD** — PID 630891 不存在，已自行退出。

### 2. d025_v3 Checkpoint
路径：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter/`
- `adapter_model.safetensors` 存在，checkpoint 有效
- 训练步数：checkpoint-3384

### 3. d000 Ref 模型
**d000_s42 已就绪**：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_model.safetensors`（可用作 ref）

### 4. 阻塞：cuda:3 被占用

**无法提交 signals 任务。** cuda:3 当前有活跃进程：

| PID | 运行时间 | 任务 | 显存 |
|-----|---------|------|------|
| 654072 | ~1min | `compute_signals.py` d000_v2_s42 / s2 / gsm8k | 7820 MiB |

这是另一个 signals 任务，不是残留进程。按 C001/C002 约束，不能在 GPU 有同类进程时提交新任务。

**建议**：等 PID 654072 完成后再提交 d025_v3 signals 到 cuda:3。需要 Director 决定是等待还是换其他 GPU。

---
