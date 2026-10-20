# code pickcube tcn prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pickcube_tcn_prep_20260520T120456_result.json`
- **Structured JSON:** [`293976ae7c0eaaa7df84.json`](../../sessions/29/293976ae7c0eaaa7df84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整分析和启动命令。

---

```
=== PickCube TCN 配置 ===
config_section: maniskill
task_name: maniskill_PickCube-v1
obs_type: state (MLP, 42 dims)
encoder: {mlp_keys: '.*', cnn_keys: '$^'}
decoder: {mlp_keys: '.*', cnn_keys: '$^'}
action_repeat: 1
envs: 1
time_limit: 200
steps: 210000 (与 019b 实际运行步数一致)

=== TCN 兼容性 ===
tcn_sigma 可用: YES
原因: TCN 在 networks.py:257 的 RSSM.img_step 中注入 dt_emb 噪声，
      环境无关。只需 gate_fixed_dt>0 确保 dt_emb 存在即可。

=== σ 建议 ===
推荐值: 0.2
理由: PickCube CIVO 强度中等偏低 (NVE peak 3.78 / baseline avg ~2.3 ≈ 1.6x)，
      与 Walker 类似。Walker σ=0.5 已被标记为 overdose。σ=0.2 更安全。

=== 当前 GPU 占用 ===
cuda:0 — exp_030b_tcn_cheetah_s0_sigma05 (运行中)
cuda:1 — exp_027_tcn_walker_s1 σ=0.5 (210K 步，即将完成)

=== 完整启动命令 ===
```

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && nohup env LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --steps 210000 --seed 0 --device cuda:1 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_031_tcn_pickcube_s0_sigma02 > logdir/exp_031_tcn_pickcube_s0_sigma02.log 2>&1 &
```

```
=== 注意事项 ===
- 不用 CUDA_VISIBLE_DEVICES — SAPIEN/resolve_physical_device() 会自动清除 CVD 并直接映射 --device cuda:1
- 不用 MUJOCO_GL/MUJOCO_EGL_DEVICE_ID — ManiSkill3 用 SAPIEN 不用 MuJoCo
- --compile False 必须 — torch.compile 与 ManiSkill3 不兼容
- obs_mode=state → render_backend=cpu（envs/maniskill.py 自动处理），无 GPU 渲染开销
- 等 exp_027_tcn_walker_s1 退出后再启动，否则 cuda:1 显存冲突
```

---
