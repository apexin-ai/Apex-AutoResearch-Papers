# 失败实验根因 + GPU 共享状态报告 (2026-05-19 22:40)

## 第一部分：5 个失败实验根因

### 统一失败原因

所有 5 个实验的 `failure_reason` 完全相同：

> **startup recovery: RUNNING with no cron and no server/pid info**

含义：实验在 registry 中被注册为 RUNNING 状态，但从未实际部署到服务器（无 tmux session、无进程、无 PID 记录）。在 14:00-14:32 的 startup recovery 扫描中，系统检测到这些"僵尸"条目并标记为 failed。

**原定服务器均为 bjb2-28827。日志文件（.json 产出）从未生成。**

| 实验名 | 失败原因 | 原因一句话 |
|--------|---------|-----------|
| eval-obs-only-spatial-norm02-k5-seed45 | startup recovery | 注册后未部署，无进程无日志 |
| eval-obs-only-spatial-norm02-k5-seed44 | startup recovery | 同上 |
| eval-random-selection-object-k5-seed45 | startup recovery | 同上 |
| eval-random-selection-object-k5-seed44 | startup recovery | 同上 |
| eval-random-selection-object-k5-seed43 | startup recovery | 同上 |

### 当前状态：已全部重新启动

所有 5 个实验已被重新部署，正在运行中：

| 实验 | 重新部署服务器 | 当前进度 | tmux session |
|------|---------------|---------|-------------|
| obs-only-spatial-k5-seed44 | bjb2-28827 (GPU 2) | task 4/10, 已完成: 80%→100%→0%→50% | eval-vla-only-spatial-seed44 附近 |
| obs-only-spatial-k5-seed45 | bjb2-28827 (GPU 5) | task 4/10, 已完成: 90%→100%→0%→30% | 类似 |
| random-selection-object-k5-seed43 | bjb2-28827 (GPU 1) | task 3/10, 0%→10%→20% | eval-random-selection-object-k5-seed43 |
| random-selection-object-k5-seed44 | bjb1-32546 | task 3/10, 0%→10%→10% | eval-random-selection-object-k5-seed44 |
| random-selection-object-k5-seed45 | bjb1-32546 | task 3/10, 0%→10%→10% | eval-random-selection-object-k5-seed45 |

**结论：无需重试，已在运行。** 预计各实验还需 2-4 小时完成。

---

## 第二部分：GPU 共享状态

### 1. bjb1-32546 cuda:4 — 两实验共享

| 指标 | 值 |
|------|-----|
| GPU 型号 | RTX 4090 (24GB) |
| 显存占用 | 3881 MiB / 24564 MiB (16%) |
| GPU 利用率 | **82%** |
| 进程数 | 2 (PID 755612 + 755878，各 ~1923 MiB) |

| 实验 | tmux session | 进度 |
|------|-------------|------|
| eval-obs-only-object-default-seed48-r2 | eval-obs-only-default-seed48-t16 | task 8/10 (orange_juice), 正常运行 |
| eval-perdof-object-norm005-seed45-r2 | eval-perdof-norm005-seed45-t16 | task 8/10 (chocolate_pudding → orange_juice), 正常运行 |

**评估：运行正常，效率良好。** 显存仅用 16%，GPU 利用率 82%，两个实验互不干扰。4090 余量充足，共享无瓶颈。

### 2. bjb2-40593 cuda:0 — 两实验共享

| 指标 | 值 |
|------|-----|
| GPU 型号 | RTX 4090 D (24GB，单卡机) |
| 显存占用 | 6296 MiB / 24564 MiB (26%) |
| GPU 利用率 | **99%** |
| 进程数 | 2 (PID 503784: 3251 MiB + PID 508930: 3011 MiB) |

| 实验 | tmux session | 进度 |
|------|-------------|------|
| eval-obs-only-spatial-norm02-seed43 | eval-spatial-obs-only-norm02-seq | task 7/10 (spatial), 正常运行 |
| eval-random-selection-object-seed46-r2 | eval-random-selection-seed46-t16 | task 5/10 (object), 正常运行 |

**评估：GPU 利用率 99%，已饱和。** 显存余量足够（74% 空闲），但 compute 完全占满。两个实验在争抢算力，单实验速度约降 40-50%。由于是单卡机无法分离，只能等其中一个先完成后另一个恢复全速。

---

## 第三部分：空闲 GPU 资源

### bjb2-28827 (6x RTX 4090)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 4255 MiB (17%) | 20% | 1 实验运行中 |
| 1 | 2375 MiB (10%) | 15% | 1 实验运行中 |
| 2 | 6519 MiB (27%) | 99% | 2 实验共享 |
| **3** | **1 MiB (0%)** | **0%** | **完全空闲** |
| 4 | 3560 MiB (15%) | 17% | 1 实验运行中 |
| 5 | 4148 MiB (17%) | 18% | 1 实验运行中 |

### bjb1-32546 (6x RTX 4090)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 3032 MiB (12%) | 18% | 1 实验运行中 |
| **1** | **2 MiB (0%)** | **0%** | **完全空闲** |
| 2 | 4255 MiB (17%) | 25% | 1 实验运行中 |
| 3 | 4255 MiB (17%) | 24% | 1 实验运行中 |
| 4 | 3881 MiB (16%) | 82% | 2 实验共享 |
| 5 | 4255 MiB (17%) | 27% | 1 实验运行中 |

**可用空闲 GPU：bjb2-28827 cuda:3, bjb1-32546 cuda:1**

---

## 建议

1. **5 个失败实验无需重试** — 已全部重新部署并正在运行
2. **bjb1-32546 cuda:4 共享可接受** — 82% 利用率，显存充裕，不影响实验质量
3. **bjb2-40593 cuda:0 共享有瓶颈** — 99% compute 饱和，但两个实验都已过半，不建议中断迁移，等自然完成
4. **空闲 GPU 可用于新任务**：bjb2-28827 cuda:3 和 bjb1-32546 cuda:1 完全空闲，可立即部署新实验
