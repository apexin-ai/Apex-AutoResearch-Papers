# ops check training status loop2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-status-loop2_20260513T233646_result.json`
- **Structured JSON:** [`c4f0874ccc729e28fcc3.json`](../../sessions/c4/c4f0874ccc729e28fcc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan001-r2 Status
- PID 84901: **running** (elapsed 56m25s)
- Total steps completed: **441/500**
- Last metrics (step 441): prove_rate=0.875, isr=0.875, reward=0.875
- Recent trend (steps 437-441): prove_rate 波动 0.625~1.0, 均值高位
- Conclusion: **仍在运行，预计约 10 分钟内完成**

## plan005 Status
- PID 85790: **running** (elapsed 54m25s, bash wrapper)
- Total steps completed: **376/500**
- Last metrics (step 376): prove_rate=0.875, isr=0.136, reward=0.801
- Recent trend (steps 372-376): prove_rate 0.5~1.0, isr 很低 (0.13~0.38), STA 信号贡献弱
- Conclusion: **仍在运行，预计约 20 分钟内完成**

## Server Health
- GPU 0: 80323/97887 MiB (82%), utilization 87%
- GPU 1: 80355/97887 MiB (82%), utilization 90%
- Disk: root=27% (22G free), autodl-tmp=68% (82G free)
- 两块 GPU 都在满载训练，服务器状态正常

---
