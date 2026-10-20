# TCN 消融实验命令清单

## 1. 代码兼容性确认

**结论：TCN 对环境完全无关，Cheetah 无需任何代码修改。**

TCN 实现位置（服务器端代码，bjb1-45299）：
- `networks.py:241` — `RSSM.img_step(self, prev_state, prev_action, dt=None, sample=True, tcn_sigma=0.0)`
- `networks.py:256-258` — 噪声注入逻辑：
  ```python
  if tcn_sigma > 0:
      dt_emb = dt_emb + tcn_sigma * dt_emb.detach().std() * torch.randn_like(dt_emb)
  ```
- `models.py:691` — `_imagine` 传递：`dynamics.img_step(state, action, dt=prev_dt, tcn_sigma=getattr(config, "tcn_sigma", 0.0))`
- `configs.yaml:131` — 默认值 `tcn_sigma: 0.0`

TCN 仅在 imagination rollout 中对 `dt_embedding` 添加高斯噪声，不涉及任何环境特定逻辑。Walker Walk (obs: height+orientations+velocity, 24维) 和 Cheetah Run (obs: position+velocity, 17维) 都使用 `dmc_proprio` 配置，区别只在 obs 维度（由 encoder 自动处理）。

## 2. 实验命令

### 命令模板

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES={GPU_ID} LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio {EXPERIMENT_ARGS} --logdir logdir/{EXP_NAME}"
```

### Walker 多 seed（验证 σ=0.2 跨 seed 鲁棒性）

**exp_029a_tcn_walker_s1_sigma02**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029a_tcn_walker_s1_sigma02"
```

**exp_029b_tcn_walker_s2_sigma02**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02"
```

### Cheetah TCN（跨环境验证）

**exp_030a_tcn_cheetah_s0_sigma02**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02"
```

**exp_030b_tcn_cheetah_s0_sigma05**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_030b_tcn_cheetah_s0_sigma05"
```

### 剂量响应（σ=0.1 低噪声）

**exp_029c_tcn_walker_s0_sigma01**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01"
```

### 非 CIVO 对照（dt=1，无时间抽象）

**exp_029d_tcn_walker_s0_dt1_control**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 1 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s0_dt1_control"
```

## 3. GPU 要求

| 实验 | 显存需求 | 推荐 GPU |
|------|----------|----------|
| 所有实验 | ~4-5 GB | 任意 ≥8GB GPU（RTX 3060/4060 及以上） |

`dmc_proprio` 用纯 MLP encoder/decoder（无 CNN），模型参数 ~17M，batch_size=16×batch_length=64，显存占用很低。单卡可同时跑 2 个实验（分别占 cuda:0 和 cuda:1）。

## 4. 注意事项

1. **MUJOCO_EGL_DEVICE_ID**：必须设为 0（即使 CUDA_VISIBLE_DEVICES 指定了其他物理 GPU，EGL 设备 ID 始终用 0）
2. **LD_PRELOAD**：AutoDL 环境需要 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` 避免 libstdc++ 版本冲突
3. **CUDA_VISIBLE_DEVICES**：调整为实际可用 GPU 编号。如果服务器有 2 GPU，可分配 0 和 1 并行跑
4. **`--device cuda:0`**：进程内部始终用 `cuda:0`，通过 `CUDA_VISIBLE_DEVICES` 控制物理 GPU 映射
5. **`--gate_subsample_max_dt 2`**：显式指定以保持命令可读性。注意：省略此参数时 `gate_subsample_max_dt=0` + `gate_fixed_dt=2` 会 fallback 到 `effective_max_dt=2`（`models.py:218-222`），行为完全等价。当前在跑的 σ=0.2 s0 虽未显式指定此参数，配置无误
6. **dt=1 对照组**：`--gate_fixed_dt 1 --gate_subsample_max_dt 1` 表示无时间抽象，dt_embedding 退化为常量，TCN 噪声仍然注入但预期无 CIVO 可抑制
7. **logdir 命名**：统一用 `logdir/exp_XXX_...` 前缀，保持与 registry 一致

## 5. 实验设计理据

| 实验 | 目的 | 验证假设 |
|------|------|----------|
| 029a/b | 多 seed | σ=0.2 的 CIVO 抑制不是 seed 偶然 |
| 030a | 跨环境 | TCN 环境无关性（Cheetah σ=0.2） |
| 030b | 跨环境+剂量 | Cheetah 下 σ=0.5 是否也过强 |
| 029c | 剂量响应 | σ=0.1 是否足够抑制 CIVO |
| 029d | 必要性对照 | dt=1 无 CIVO 时 TCN 是否 neutral |
