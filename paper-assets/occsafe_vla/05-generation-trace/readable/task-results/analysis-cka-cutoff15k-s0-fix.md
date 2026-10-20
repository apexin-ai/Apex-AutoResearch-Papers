# analysis cka cutoff15k s0 fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_cutoff15k_s0_fix_20260525T062612_result.json`
- **Structured JSON:** [`b8ea8dd9e1fecf8eda25.json`](../../sessions/b8/b8ea8dd9e1fecf8eda25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cutoff_15k_s0 (seed 42) checkpoint 不存在。** 两台服务器上都没有。

现有 cutoff_15k checkpoints：
- `cutoff_15k_s1` (seed 43) — 10894 和 34685 都有
- `cutoff_15k_s2` — 仅 34685
- `cutoff_15k_s2_v2` — 仅 34685

现有 s0 checkpoints（seed 42）：
- `vanilla_retrain_s0` ✓
- `full_occ_retrain_s0` ✓
- `full_occ_ln_s0` ✓
- `ablation_occ_detach_s0_retrain` ✓

**cutoff_15k_s0 从未训练过，无法进行 same-seed CKA 对比。**

两个选项：
1. **先训练 cutoff_15k_s0**（seed 42, cutoff at 15k steps, ~50k total），然后再跑 CKA
2. **用现有 cutoff_15k_s1** 跑 CKA，接受 cross-seed confound，作为初步参考

需要哪个方向？

---
