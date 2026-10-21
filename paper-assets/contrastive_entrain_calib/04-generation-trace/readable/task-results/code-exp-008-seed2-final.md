# code exp 008 seed2 final

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-seed2-final_20260524T133348_result.json`
- **Structured JSON:** [`d420a9fd9cd86ec5af9d.json`](../../sessions/d4/d420a9fd9cd86ec5af9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，结果汇总：

- **step 10** (21:44:01): loss=2.0705, sft=2.0698, R3=0.6247, S(t)=0.6317
- **step 20** (21:44:36): loss=1.7959, sft=1.8070, R3=0.4335, S(t)=0.3215
- **Step 耗时**: ~3.5s/step（10 steps 用了 ~35s）
- S(t) 从 0.63 降到 0.32（probe score 快速下降，符合预期）

**预估完成时间**: 2000 steps × 3.5s ≈ 117 min ≈ 2 小时（不含 probe retrain 间歇，retrain 每100步一次会额外增加时间）。

---
