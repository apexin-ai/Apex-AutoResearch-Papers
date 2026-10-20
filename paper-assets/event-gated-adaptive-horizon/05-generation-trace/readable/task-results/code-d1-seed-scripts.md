# code d1 seed scripts

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d1-seed-scripts_20260516T133257_result.json`
- **Structured JSON:** [`5f10c10bba8f60c958cb.json`](../../sessions/5f/5f10c10bba8f60c958cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已创建并通过语法检查：

```
/root/autodl-tmp/event-gated-adaptive-horizon/scripts/
├── exp_001_baseline_s2.sh      # baseline, H=15, 500K steps, seed=2
├── exp_008d_civo_trigger_s2.sh # gate+subsample+dt=2, H=8, 105K steps, seed=2
└── exp_018_full_sgs_s2.sh      # 同 008d + full_sgs=True, 105K steps, seed=2
```

所有 flag 名已与 `configs.yaml` 核对一致（`gate_enabled`, `gate_fixed_dt`, `gate_subsample_max_dt`, `imag_horizon`, `full_sgs`）。提交时按实际 GPU 分配调整 `cuda:N` 和 `MUJOCO_EGL_DEVICE_ID`。

---
