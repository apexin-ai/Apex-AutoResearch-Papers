# launch alpha3 westb1 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_alpha3_westb1_v2_20260522T080610_result.json`
- **Structured JSON:** [`3466ccaf570be369cd15.json`](../../sessions/34/3466ccaf570be369cd15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都被占用：

| GPU | PID | 进程 | 显存 | 运行时间 |
|-----|-----|------|------|----------|
| 0 | 162850 | `sft_recovery.py` α=3.0（带 `--gpu 0` 旧参数） | 51.5 GiB | 18min |
| 1 | 164710 | `train_grpo_v5.py` cka_only_20 | 58.5 GiB | 8min |

两个问题：

1. **GPU 1 不空闲** — 正在跑 cka_only_20 的 GRPO，无法立即启动 α=3.0 pipeline。
2. **GPU 0 上已有一个 α=3.0 SFT** — 但用了旧的 `--gpu 0` 参数（你提到的 bug）。这个跑了 18 分钟的结果可能不可靠。

需要你决定：
- 等 GPU 1 的 GRPO 跑完再启动？
- 还是 kill 掉某个进程腾出 GPU？

---
