# GPU 进程状态 — 2026-05-24 10:15

## cqa1-33015 — 4×RTX 4090 D (24GB)

| GPU | 显存占用 | 利用率 | 进程 | PID | 启动时间 | 状态 |
|-----|---------|--------|------|-----|---------|------|
| 0 | 1 MiB | 0% | — | — | — | 空闲 |
| 1 | 1 MiB | 0% | — | — | — | 空闲 |
| 2 | 1 MiB | 0% | — | — | — | 空闲 |
| 3 | 10294/24564 MiB | 42% | eval_pi05_l2norm_k085_goal_seed43 | 617677 | 09:02 | ✅ 确认运行中，Task 8/10 (put the bowl on the plate) ep=20, 总 SR ~91.2% |

### 特别关注项
- **eval_pi05_random_k095_object_seed42_v2** — ✅ **已完成**（09:58 today）。SR=74.0% (370/500)，耗时 119.6 min。结果：`pi05_random_k0.95_libero_object_seed42.json`。**fig_method_gap 阻塞项已解除。**
- **eval_pi05_l2norm_k085_goal_seed43** — ✅ 确认在 GPU 3 运行中。
- tmux session `eval_pi05_l2norm_k03_goal_seed42`（CUDA_VISIBLE_DEVICES=2）仍存在但 GPU 2 空闲，eval 已结束。

---

## westd-27271 — 2×RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 进程 | PID | 启动时间 | 状态 |
|-----|---------|--------|------|-----|---------|------|
| 0 | 15964/97887 MiB | 68% | eval_openvla_l2norm_k05_goal_seed42_v2 | 486402 | 08:14 | ✅ 确认运行中，Task 5/10 ep=30 |
| 1 | 15964/97887 MiB | 67% | eval_openvla_random_k05_goal_seed42 | 500676 | 09:05 | ✅ 确认运行中，Task 3 完成 (SR=64%)，进入 Task 4 |

### 特别关注项
- **eval_openvla_random_k05_goal_seed42** (pid=500676) — ✅ 确认运行中（GPU 1）。
- **eval_openvla_l2norm_k05_goal_seed42_v2** — ✅ 确认运行中（GPU 0），此为之前 failed 版本的重试。
- 后台运行 `auto_deploy_openvla_baselines.sh`（PID 295287）。

---

## westd-41074 — 4×RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 进程 | PID | 启动时间 | 状态 |
|-----|---------|--------|------|-----|---------|------|
| 0 | 10548/97887 MiB | 46% | eval_pi05_random_k095_goal_seed43 | 363766 | 09:51 | ✅ 确认运行中 |
| 1 | 10490/97887 MiB | 37% | eval_pi05_l2norm_k07_goal_seed43 | 345089 | 09:38 | ✅ 确认运行中 |
| 2 | 10670/97887 MiB | 47% | eval_pi05_l2norm_k05_long_seed43 (libero_10) | 363842 | 09:51 | ✅ 确认运行中 |
| 3 | 10532/97887 MiB | 50% | eval_pi05_random_k085_goal_seed43 | 318964 | 08:56 | ✅ 确认运行中，Task 8/10 SR=58% |

### 特别关注项
- **eval_pi05_random_k085_spatial_seed42_postfix** — ❌ **进程已结束**。日志 `v3.log` 显示 `Terminated / EXIT_CODE=129`（被 kill），终止于 00:59 today。cuda:2 现已被其他实验占用。

---

## westd-38929 — 4×RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 进程 | PID | 启动时间 | 状态 |
|-----|---------|--------|------|-----|---------|------|
| 0 | 1 MiB | 0% | — | — | — | 空闲（eval_xvla_l2norm_k05_goal_seed43 已于 06:52 完成） |
| 1 | 1 MiB | 0% | — | — | — | 空闲 |
| 2 | 4856/97887 MiB | 1% | eval_xvla_random_k085_goal_seed42 | 674830 | 09:10 | ✅ 确认运行中，ep 36/50 on current task |
| 3 | 4938/97887 MiB | 1% | eval_xvla_random_k085_spatial_seed42 | 674970 | 09:10 | ✅ 确认运行中，ep 15/50 on current task |

### 特别关注项
- **eval_xvla_random_k085_goal_seed42** — ✅ 确认在 cuda:2 运行中。
- **cuda:0**: `eval_xvla_l2norm_k05_goal_seed43` 已于 06:52 完成，结果已保存。GPU 空闲。
- **cuda:1**: 空闲，无进程。
- **cuda:3**: X-VLA random k0.85 spatial seed42 运行中（不是 goal，是 spatial）。

---

## 汇总

| 服务器 | 活跃 GPU | 空闲 GPU | 运行实验数 |
|--------|---------|---------|-----------|
| cqa1-33015 | 1/4 | 3 | 1 |
| westd-27271 | 2/2 | 0 | 2 |
| westd-41074 | 4/4 | 0 | 4 |
| westd-38929 | 2/4 | 2 | 2 |
| **总计** | **9/14** | **5** | **9** |

### 可用 GPU 资源
- cqa1-33015: GPU 0, 1, 2 — 3×RTX 4090 D (24GB)
- westd-38929: GPU 0, 1 — 2×RTX PRO 6000 Blackwell (96GB)
