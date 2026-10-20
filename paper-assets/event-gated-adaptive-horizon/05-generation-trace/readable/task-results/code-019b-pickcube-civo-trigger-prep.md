# code 019b pickcube civo trigger prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_019b-pickcube-civo-trigger-prep_20260516T235335_result.json`
- **Structured JSON:** [`9b20939ca812cd721d49.json`](../../sessions/9b/9b20939ca812cd721d49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成。** 脚本已更新至 `artifacts/scripts/exp_019b_pickcube_civo_trigger.sh`，验证结果：

- Dry-run 在 bjb1-45299 cuda:1 上成功启动（`[ManiSkill GPU] CVD=None, requested=cuda:1, resolved=cuda:1`）
- 模型参数量 16,986,162（含 dt_emb），对比 019a baseline 的 16,507,690（纯 DreamerV3），增量 ~478K 来自 gate 模块
- `unset CUDA_VISIBLE_DEVICES` 已包含，避免 SAPIEN IndexError
- 默认 CUDA_ID=1，Main Agent 提交时可直接用或覆盖

提交命令参考（供 Main Agent 使用）：
```
bash /root/autodl-tmp/event-gated-adaptive-horizon/../../artifacts/scripts/exp_019b_pickcube_civo_trigger.sh
```
或等效的 inline command：
```
unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:1 --compile False --checkpoint_every 25000 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_019b_pickcube_civo_trigger
```

---
