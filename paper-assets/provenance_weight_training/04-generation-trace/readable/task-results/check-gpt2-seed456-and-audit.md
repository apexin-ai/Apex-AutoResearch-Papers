# check gpt2 seed456 and audit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpt2_seed456_and_audit_20260521T035535_result.json`
- **Structured JSON:** [`5a94ef2d12a2c331b640.json`](../../sessions/5a/5a94ef2d12a2c331b640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
gpt2_adaptive_seed456 状态: 训练中 step 4980/6103 (82%)
已运行: 3h11m, 速度 ~2.27s/step, ETA ~42分钟
已有 checkpoints: 3500, 4000, 4500（无 final/）
注意: 此实验使用了 --save_only_model，但是从头训练，不受 resume 问题影响

全局 resume 排查 (20个实验使用过 resume):

❌ 因 resume + save_only_model 失败 (optimizer state loss):
- gpt2_adaptive_seed123: resume from checkpoint-2500, conclusion=failed, save_only_model=是
- adaptive_tau08_scratch_seed42: resume from checkpoint-3500, conclusion=failed, save_only_model=是
  → 两者已有 _v2 从头重跑版本 (RUNNING)

❌ 因其他原因失败:
- uniform_1_7b_seed42: resume from checkpoint-3000, conclusion=failed, save_only_model=否
- threshold_q07_seed42: resume from checkpoint-5500 (via shell script), conclusion=failed, save_only_model=否 (GPU占用导致)

⚠️ 标记 success 但有 degradation 记录:
- grid_b0_2_seed456: resume from checkpoint-5500, conclusion=success, save_only_model=是 (metrics记录LR reset degradation)
- grid_b0_2_seed123: resume from checkpoint-5500, conclusion=success, save_only_model=是 (同上)

✅ Resume 且 success 无异常 (save_only_model=是):
- ess_only_seed456_r2, ess_only_seed123_r2, grid_b0_3_seed123_r2,
  grid_b5_0_seed456, grid_b3_0_seed456, grid_b2_0_seed456,
  random_reweight_seed456, uniform_seed456, uniform_seed123, uniform_seed42
- contamination_60_random_seed42 (metrics记录resume from checkpoint-1000)

✅ Resume 且 success (save_only_model=否):
- detect_remove_q05_seed456, adaptive_1_7b_seed42,
  contamination_60_grid_b0_3_seed42

总结: save_only_model + resume 组合共12个实验，其中2个明确失败、2个有degradation记录但标记success（建议复查 grid_b0_2_seed456 和 grid_b0_2_seed123 的 eval 结果是否用了 pre-resume checkpoint）。
```

---
