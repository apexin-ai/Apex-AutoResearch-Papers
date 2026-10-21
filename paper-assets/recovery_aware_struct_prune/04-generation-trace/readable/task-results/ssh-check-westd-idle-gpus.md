# ssh check westd idle gpus

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_idle_gpus_20260524T015238_result.json`
- **Structured JSON:** [`e22ff3a2e7403ddb6a72.json`](../../sessions/e2/e22ff3a2e7403ddb6a72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总 (westd-32935)

| GPU | 显存占用 | GPU利用率 | 状态 | 任务 | 已运行 |
|-----|---------|-----------|------|------|--------|
| 0 | 18543/97887 MiB | 97% | **BUSY** | eval_math500_sft_standard_25_fixed_v2 (PID 166245) | 4h42m |
| 1 | 19225/97887 MiB | 98% | **BUSY** | eval_math500_grpo_rasp_alpha2p0_20_fixed (PID 168524) | 4h23m |
| 2 | 16993/97887 MiB | 97% | **BUSY** | eval_math500_sft_rasp_alpha2p0_20_fixed (PID 171964) | 3h40m |
| 3 | 0/97887 MiB | 0% | **IDLE** | — | — |

**结论：**
- **GPU 3 空闲**，确认 grpo_cka_only_25_fixed 已完成。
- GPU 1 仍在跑 grpo_rasp_alpha2p0_20_fixed（已运行 4h23m，尚未完成）。
- GPU 0-2 三张卡都在满负荷跑 eval_math500，暂无空闲。

当前可调度：仅 **GPU 3**。

---
