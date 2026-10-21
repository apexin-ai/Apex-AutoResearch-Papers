# exec westb split gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_westb_split_gpu_20260522T003726_result.json`
- **Structured JSON:** [`f5ef47f573c44a517e94.json`](../../sessions/f5/f5ef47f573c44a517e94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v7 已成功启动并在 GPU 0 上开始推理（第 1 题，2.11s/it）。

## 最终结果

| 指标 | 值 |
|------|-----|
| **v6 (cka_only_20)** | 317/500 时被 kill |
| **v7 (cka_only_20 重启)** | PID **133850**，GPU 0，12.9GB VRAM，已开始推理 |
| **standard_25** | PID 104592，383/500，GPU 1，19.2GB VRAM |

**GPU 最终分配：**
- **GPU 0**: eval_math500_sft_cka_only_20_v7 (PID 133850) — 独占
- **GPU 1**: eval_math500_sft_standard_25 (PID 104592) — 独占

两个 eval 各占一张卡，v7 首题 2.1s/it（之前共享 GPU 时约 100s+ 平均），预计 ~2-3h 内完成 500 题。standard_25 剩 117 题，独占 GPU 后也会加速，预计 ~2-3h 完成。

---
