# Memory — event-gated-adaptive-horizon

## Humanoid 环境不适用于 CIVO 隔离 (2026-05-29)

exp_humanoid_baseline_s0 结果：标准 DreamerV3 (dt=1, no gate) 在 Humanoid Walk (21 DoF) 上 NVE=12.97×，baseline 自身严重 value overestimation。**Humanoid 不能作为 CIVO 隔离实验的 clean baseline**——baseline 本身就 CIVO-prone，008d 的 NVE 升高无法归因于 dt_emb conditioning。

CIVO 论文 scope 应限定在 "baseline-healthy environments"（Walker/Cheetah baseline NVE < 1.0×）。

## 跨环境 CIVO onset 统计 (D171 数据锁定)

- Walker 008d: 3/5 onset (60%), NVE_peak 1.53×–4.72×, 2 sub-threshold
- Cheetah 008d: 3/4 onset (75%), NVE_peak median 2.3× [0.31, 127.6]
- Cartpole 008d: 0/3 onset, NVE < 0.1×
- 控制实验: trained dt_emb 6/9 onset vs removed 0/4 vs untrained 0/4 vs frozen 0/10

## EGL 设备 ID 与 CUDA 设备对应 (2026-05-29)

exp_quadruped_baseline_s0 失败原因: MUJOCO_EGL_DEVICE_ID=1 但实际只有 device 0 可用。修复: MUJOCO_EGL_DEVICE_ID 必须与 CUDA 设备号匹配，且该物理设备必须存在。

## D177: Humanoid 008d 取消

Director 决策: humanoid baseline 自身 CIVO-prone → 取消 exp_humanoid_008d_s0。

## 串行实验链 (westd-51268 cuda:0)

实验链: humanoid_baseline ✅(negative) → quadruped_baseline_r2 (RUNNING) → quadruped_008d (待 baseline 结果)
无自动串行机制，靠 cron 回调手动推进。
