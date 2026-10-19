# D139 Status Scan — 2026-05-25

扫描时刻：2026-05-25 ~03:30 UTC（北京时间约 11:30）。覆盖 5 台服务器：bjb2-28827、cqa1-32758、bjb1-32546、bjb1-18228、bjb2-40593。

---

## 1. D139 种子扩展（12 实验）逐个状态

D139 = 6 adaptive_conformal_crm (τ=0.25, norm=0.2) + 6 vla_only baseline，跨 3 benchmark (object / spatial / goal) × 2 seeds (48, 49)。

| # | exp_id | server | GPU | mode | bench | seed | status | SR | trigger_rate |
|---|--------|--------|-----|------|-------|------|--------|------|-------------|
| 1 | eval-supp-adapt-tau025-object-s48 | bjb2-28827 | — | adaptive | object | 48 | DONE 02:31 | **0.760** | 0.0388 |
| 2 | eval-supp-adapt-tau025-object-s49 | bjb2-28827 | — | adaptive | object | 49 | DONE 02:30 | **0.740** | 0.0417 |
| 3 | eval-supp-adapt-tau025-spatial-s48 | bjb2-28827 | — | adaptive | spatial | 48 | DONE 02:00 | **0.810** | 0.1977 |
| 4 | eval-supp-adapt-tau025-spatial-s49 | bjb2-28827 | — | adaptive | spatial | 49 | DONE 01:58 | **0.820** | 0.1952 |
| 5 | eval-supp-adapt-tau025-goal-s48 | bjb2-28827 | — | adaptive | goal | 48 | DONE 01:55 | **0.845** | 0.0894 |
| 6 | eval-supp-adapt-tau025-goal-s49 | bjb2-28827 | — | adaptive | goal | 49 | DONE 02:05 | **0.815** | 0.0886 |
| 7 | eval-supp-vla-only-object-s48 | cqa1-32758 | — | vla_only | object | 48 | DONE 03:01 | **0.790** | — |
| 8 | eval-supp-vla-only-object-s49 | cqa1-32758 | — | vla_only | object | 49 | DONE 02:58 | **0.755** | — |
| 9 | eval-supp-vla-only-spatial-s48 | cqa1-32758 | — | vla_only | spatial | 48 | DONE 02:31 | **0.795** | — |
| 10 | eval-supp-vla-only-spatial-s49 | cqa1-32758 | — | vla_only | spatial | 49 | DONE 02:40 | **0.785** | — |
| 11 | eval-supp-vla-only-goal-s48 | cqa1-32758 | — | vla_only | goal | 48 | DONE 02:34 | **0.850** | — |
| 12 | eval-supp-vla-only-goal-s49 | cqa1-32758 | — | vla_only | goal | 49 | DONE 02:34 | **0.820** | — |

**结论：12/12 全部完成。** 全部 n_rollouts=20。

### Adaptive vs VLA-only Δ（D139）
| benchmark | seed | adaptive SR | vla_only SR | Δ |
|-----------|------|-------------|-------------|----|
| object  | 48 | 0.760 | 0.790 | **-0.030** |
| object  | 49 | 0.740 | 0.755 | **-0.015** |
| spatial | 48 | 0.810 | 0.795 | **+0.015** |
| spatial | 49 | 0.820 | 0.785 | **+0.035** |
| goal    | 48 | 0.845 | 0.850 | **-0.005** |
| goal    | 49 | 0.815 | 0.820 | **-0.005** |

注：object/goal 微负差，spatial 正差；trigger_rate 在 object/goal 较低（4–9%），spatial 较高（20%）。

---

## 2. bjb2-28827 与 cqa1-32758 GPU 占用

### bjb2-28827 (6× RTX 4090, 24GB)
| GPU | util | used MiB | status |
|-----|------|----------|--------|
| 0 | 0% | 1 | **IDLE** |
| 1 | 0% | 1 | **IDLE** |
| 2 | 20% | 13966 | busy — `eval-pi05-reconvla-goal-s42`（02:24 启动，PID 393794，105:31 CPU） |
| 3 | 20% | 14088 | busy — `eval-pi05-reconvla-object-s42`（02:24 启动，PID 394198，105:26 CPU） |
| 4 | 0% | 1 | **IDLE** |
| 5 | 0% | 1 | **IDLE** |

tmux: `eval-pi05-reconvla-goal-s42`, `eval-pi05-reconvla-object-s42`（D139 全部 6 个 adapt 任务已落盘，tmux 已退出）

### cqa1-32758 (6× RTX 4090 D)
| GPU | util | used MiB | status |
|-----|------|----------|--------|
| 0–5 | 0% | 0 | **全部 IDLE** |

D139 vla_only 6 个任务全部完成，无残留进程。

---

## 3. τ-sweep 和 K-sweep 进展

### τ-sweep（spatial s42, norm=0.2，bjb1-32546）
| τ | SR | trigger_rate | status |
|-----|------|--------------|--------|
| 0.10 | 0.790 | 0.7517 | DONE 01:15 |
| 0.15 | 0.805 | 0.4065 | DONE |
| 0.20 | 0.810 | 0.2662 | DONE 01:10 |
| 0.25 | 0.795 | 0.1965 | DONE 01:09（K=1 写入） |
| 0.30 | 0.805 | 0.1674 | DONE 01:14 |
| 0.35 | 0.800 | 0.1217 | DONE |

**6/6 τ 值完成。** SR 在 0.79–0.81 之间窄幅波动，trigger_rate 随 τ 增大单调下降。

### K-sweep（spatial s42, τ=0.25, norm=0.2）
| K | server | status | SR | trigger_rate |
|---|--------|--------|------|--------------|
| K=1 | bjb1-32546 | DONE 01:09 | **0.795** | 0.1965 |
| K=2 (mean) | — | 历史已存（早期实验） | — | — |
| K=5 | bjb2-40593 | **RUNNING** — 2h33min elapsed，6/10 任务完成 | (部分: 19+18+20+20+13+0 = 90/120 = 0.75 中段) | — |

K=5 当前进度：
- 已完成 6 task: 95%, 90%, 100%, 100%, 65%, 0% → 90/120 = 0.750
- 在第 7 task（pick_up_the_black_bowl_next_to_the_cookie_box…）
- 预计还需 ~1h40min 完成全部 10 task

### 其他正在运行的相关任务
- bjb1-32546 GPU 1：`eval-supp-adapt-tau025-obj-s50`（seed 50 扩展，01:33 启动，~2h 已 8 task 完成）

---

## 4. π0.5 CRM 训练进度（bjb1-18228）

- **进程**: PID 326310 (wrapper) / 326315 (python)，ELAPSED 8h 51m，tmux `train-crm-pi05-unified-3suite-r2`
- **配置**: benchmark=object+spatial+goal, obs_dim=2048, epochs=50, batch_size=256, lr=1e-3
- **当前**: Epoch 25/50（已写完 epoch 24/50，正在 epoch 25 batch 150/684）
- **train_loss**: 0.0085（epoch 24）
- **val_loss best**: **0.004854 @ epoch 24**（每 epoch 都在小幅刷新 best；epoch 21→22→23→24 = 0.004986 → 0.004997 → 0.004856 → 0.004854）
- **检查点**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/`
- **ETA**: 当前 ~50% 进度，预计还需 ~8.5–9 小时（即 ~12:30 UTC / 北京 ~20:30 完成）
- **timeout 设置**: 43200s = 12h（剩余预算 ~3h，可能不够；若到 epoch 35 时仍无收敛迹象需重启或延长 timeout）

### 同台服务器其他占用
- GPU 3：`eval-long-vla-s47`（PID 307456，K=1, n=20）
- GPU 1, 2：IDLE
- **遗留进程警示**: PID 114507 `train_crm.py --precompute --model pi05 --benchmark long --K 10`（May 23 启动，3728 min CPU，17 GB RES）—— 应是已僵尸的 precompute 任务，建议确认后清理

---

## 5. 空闲 GPU 列表

| server | idle GPU 数 | idle index |
|--------|-------------|------------|
| bjb2-28827 | **4** | 0, 1, 4, 5 |
| cqa1-32758 | **6** | 0, 1, 2, 3, 4, 5 |
| bjb1-32546 | **5** | 0, 2, 3, 4, 5 |
| bjb1-18228 | **2** | 1, 2 |
| bjb2-40593 | 0 | — |
| **合计** | **17** | |

**可立即下发任务的最佳目标**: cqa1-32758（6 张全空）、bjb1-32546（5 张空）。

---

## 总结

1. **D139 12 实验 100% 完成**——adaptive vs vla_only 在 object/goal 上略负差，仅 spatial 正差，复合 trigger_rate pattern。
2. **τ-sweep 6/6 完成**——SR 平坦（0.79–0.81），trigger_rate 随 τ 单调下降，确认 τ 主要控制 CRM 触发频率而非 SR。
3. **K-sweep K=1 完成，K=5 进行中**（~60% 完成，1h40min 后落盘）。
4. **π0.5 CRM 训练 50% 进度**，val_loss 仍在缓慢下降，预计 ~9h 后完成；timeout 预算 ~3h 不足，需提前决定是否续期。
5. **17 张空闲 GPU 可用**，主要集中在 cqa1-32758 和 bjb1-32546。
