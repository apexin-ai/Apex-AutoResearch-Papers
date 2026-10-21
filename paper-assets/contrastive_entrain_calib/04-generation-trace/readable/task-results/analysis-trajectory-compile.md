# analysis trajectory compile

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_trajectory-compile_20260521T103757_result.json`
- **Structured JSON:** [`2a5ac35fc2a41e9de978.json`](../../sessions/2a/2a5ac35fc2a41e9de978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。轨迹数据表已保存到两处：

1. **`artifacts/trajectory_data_complete.md`** — 完整版，含 9 个方法的逐 checkpoint 数据
2. **`memory.md`** 末尾 — best checkpoint 汇总表

关键结论：
- **ACT (exp-004) 是唯一显著超越 vanilla 的方法**，ckpt-7000 SYCONScore=0.2858 (+114%)，ckpt-8000 约 0.3013 (+126%)
- **R3-GRPO s1** 在 ckpt-6500 意外出现 0.1529 (+14.5%)，是此前未知的新高点（之前认为 ckpt-4500 的 0.1337 是峰值）
- **R3-GRPO s2** 始终低于 baseline，两个 eval 仍在 RUNNING
- 其余 5 种方法全部 negative（probe reward trap / mode collapse / 净负效果）

**待补数据：** exp-003-eval-ckpt8000 (RUNNING)、exp-003-s2 ckpt2500/3500 (RUNNING)、exp-004 ckpt500/2000/8000 (未提交独立 eval)

---
