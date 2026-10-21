# diag exp008 oom v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp008-oom-v2_20260518T184442_result.json`
- **Structured JSON:** [`e8a191ec64b008466f59.json`](../../sessions/e8/e8a191ec64b008466f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `/root/contrastive_entrain_calib/artifacts/exp-008/diag_oom_v2.md`。

**结论**：exp-008 实际并未失败。PID 42424 是第一次正常启动的实例，仍在 GPU 3 上活跃训练（step 80+，22658 MiB，47% util）。OOM 来自第二次重复启动的实例，因 GPU 3 已被第一次运行占用 22 GB 而无法再加载 Qwen3-8B。无需干预，当前训练正常进行中。

---
