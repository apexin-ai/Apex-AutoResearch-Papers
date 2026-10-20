# prep 3B d000 v2 retrain

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_3B_d000_v2_retrain_20260514T161519_result.json`
- **Structured JSON:** [`cc4c97c0080af1657237.json`](../../sessions/cc/cc4c97c0080af1657237.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正式开始。

**汇报：**
- **GPU**: cuda:5
- **PID**: 405515
- **tmux session**: `exp_001_sft_3B_d000_v2`
- **总步数**: 3125 步 (50000 samples / batch_size 1 / grad_accum 16 = 3125)
- **当前速度**: ~4.8s/step
- **预计训练时间**: 3125 × 4.8s ≈ **4.2 小时**（约 04:30 完成）
- **超参确认**: lr=5e-5, lora_alpha=16, r=16, batch=1, grad_accum=16, max_seq_len=2048
- **日志**: `~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_v2.log`

---
