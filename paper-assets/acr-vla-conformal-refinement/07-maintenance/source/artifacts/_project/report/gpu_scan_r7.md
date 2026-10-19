# GPU Scan R7 — 2026-05-25 03:22 (Asia/Shanghai)

扫描全部 5 台服务器、收割已完成实验、识别空闲算力与异常。

---

## 1. 各服务器 GPU 状态表

### 1.1 bjb1-18228 (4 GPU)  —— π0.5 CRM 训练 + long precompute
| GPU | Util | Mem (MiB) | 运行实验 | PID | etime |
|-----|------|-----------|----------|-----|-------|
| 0 | 10% | 580 | train-crm-pi05-unified-3suite-r2 (主进程显存占用小，主要在 GPU 3) | 326315 | 8h44m |
| 1 | 0% | 0 | idle（tmux `long-vla-s47` 残留，Python 已退出） | — | — |
| 2 | 0% | 0 | idle | — | — |
| 3 | 23% | 9883 | precompute pi05 long K=10 + 训练 forward（实际跑训练的 GPU） | 114507 | **1d23h** (~47h) |

**注意**：precompute 已跑 ~47 小时，疑似挂死或仍在最后阶段，需要检查实际进度。

### 1.2 bjb1-32546 (6 GPU)  —— 各种 eval
| GPU | Util | Mem (MiB) | 运行实验 | PID | etime |
|-----|------|-----------|----------|-----|-------|
| 0 | 0% | 2 | **idle**（A1 baseline 已停） | — | — |
| 1 | 17% | 2383 | eval-supp-adapt-tau025-obj-s50 (adaptive CRM) | 567066 | 1h48m |
| 2 | 0% | 2 | idle | — | — |
| 3 | 0% | 2 | idle | — | — |
| 4 | 0% | 2 | idle | — | — |
| 5 | 0% | 2 | idle | — | — |

### 1.3 bjb2-28827 (6 GPU)  —— pi05 reconvla s42
| GPU | Util | Mem (MiB) | 运行实验 | PID | etime |
|-----|------|-----------|----------|-----|-------|
| 0 | 0% | 1 | idle | — | — |
| 1 | 20% | 14663 | eval-pi05-reconvla-spatial-s42 (日志中有 OOM 历史，进程仍在) | 388593 | 1h04m |
| 2 | 21% | 13966 | eval-pi05-reconvla-goal-s42 | 393794 | 58m |
| 3 | 21% | 14088 | eval-pi05-reconvla-object-s42 | 394198 | 58m |
| 4 | 0% | 1 | idle | — | — |
| 5 | 0% | 1 | idle | — | — |

### 1.4 cqa1-32758 (6 GPU)  —— **全部空闲**
| GPU | Util | Mem (MiB) | 运行实验 |
|-----|------|-----------|----------|
| 0–5 | 0% | 0 | **全部 idle**（仅 jupyter/tensorboard 系统进程） |

### 1.5 bjb2-40593 (1 GPU)  —— K=5 spatial
| GPU | Util | Mem (MiB) | 运行实验 | PID | etime |
|-----|------|-----------|----------|-----|-------|
| 0 | 1% | 3827 | **eval-adaptive-k5-spatial-s42 仍在跑** | 289696 | 2h25m |

---

## 2. 已完成等待收割的实验

### 2.1 pi05 vla_only (bjb1-32546 / bjb2-28827)
| exp_id | success_rate | 日志路径 |
|--------|--------------|----------|
| eval-pi05-vla-only-object-s42 | **100.0% (200/200)** | bjb1-32546:logs/eval-pi05-vla-only-object-s42.log |
| eval-pi05-vla-only-spatial-s42 | **98.0% (196/200)** | bjb1-32546:logs/eval-pi05-vla-only-spatial-s42.log |
| eval-pi05-vla-only-goal-s42 | **98.0% (196/200)** | bjb1-32546:logs/eval-pi05-vla-only-goal-s42.log |
| eval-pi05-vla-only-spatial-s43 | **97.5% (195/200)** | bjb1-32546:logs/eval-pi05-vla-only-spatial-s43.log |
| eval-pi05-vla-only-goal-s43 | **97.5% (195/200)** | bjb1-32546:logs/eval-pi05-vla-only-goal-s43.log |
| eval-pi05-vla-only-object-s43 | **98.5% (197/200)** | bjb2-28827:logs/eval-pi05-vla-only-object-s43.log |
| eval-pi05-vla-only-object-s42-v2 | 96.5% (193/200) (含 Traceback) | bjb1-32546 |
| eval-pi05-vla-only-spatial-s43-v2 | 96.0% (192/200) (含 Traceback) | bjb1-32546 |
| eval-pi05-vla-only-goal-s42-v2 | 95.5% (191/200) (含 Traceback) | bjb1-32546 |
| eval-pi05-vla-only-goal-s43-v2 | 97.0% (194/200) (含 Traceback) | bjb1-32546 |
| eval-pi05-vla-only-object-s43-v2 | 86.5% (173/200) (含 Traceback) | bjb2-28827 |

注：`-v2` 日志虽含 Traceback 但仍跑完，可能是单 task 异常被 catch 后继续。需要比对 json 输出文件确认。

### 2.2 supp vla_only baseline (bjb1-18228 / cqa1-32758)
| exp_id | success_rate | 日志 |
|--------|--------------|------|
| eval-supp-obj-vla-only-s50 | 74.0% (148/200) | bjb1-18228 |
| eval-supp-spatial-vla-only-s42 | 80.0% (160/200) | bjb1-18228 |
| eval-long-vla-only-s47 (K=1) | **59.5% (119/200)** | bjb1-18228:/tmp/eval_long_vla_s47.log |
| eval-supp-vla-only-obj-s48 | 79.0% (158/200) | cqa1-32758 |
| eval-supp-vla-only-obj-s49 | 75.5% (151/200) | cqa1-32758 |
| eval-supp-vla-only-spatial-s48 | 79.5% (159/200) | cqa1-32758 |
| eval-supp-vla-only-spatial-s49 | 78.5% (157/200) | cqa1-32758 |
| eval-supp-vla-only-goal-s48 | 85.0% (170/200) | cqa1-32758 |
| eval-supp-vla-only-goal-s49 | 82.0% (164/200) | cqa1-32758 |
| eval-supp-vla-only-spatial-s47 | 80.0% (160/200) | cqa1-32758 |
| eval-supp-long-vla-only-s47 | 58.5% (117/200) | cqa1-32758 |

### 2.3 adaptive_conformal_crm（tau=0.25, norm=0.2）
| exp_id | success_rate | 日志 |
|--------|--------------|------|
| eval-supp-adapt-tau025-obj-s48 | 76.0% (152/200) | bjb2-28827 |
| eval-supp-adapt-tau025-obj-s49 | 74.0% (148/200) | bjb2-28827 |
| eval-supp-adapt-tau025-goal-s49 | 81.5% (163/200) | bjb2-28827 |
| eval-supp-adapt-tau025-spatial-s48 | 81.0% (162/200) | bjb2-28827 |
| eval-supp-adapt-tau025-spatial-s49 | 82.0% (164/200) | bjb2-28827 |
| eval-supp-adapt-tau025-spatial-s47 | 81.5% (163/200) | cqa1-32758 |
| eval-supp-long-adapt-tau025-s47 | 56.5% (113/200) | cqa1-32758 |

### 2.4 其它 baseline (cqa1-32758)
| exp_id | success_rate |
|--------|--------------|
| eval-supp-reconvla-spatial-s47 | 81.0% (162/200) |
| eval-supp-k2mean-spatial-s47 | 81.0% (162/200) |

---

## 3. 空闲 GPU 列表（可立即派活）

| 服务器 | 空闲 GPU | 数量 |
|--------|----------|------|
| bjb1-18228 | 1, 2 | 2 |
| bjb1-32546 | 0, 2, 3, 4, 5 | 5 |
| bjb2-28827 | 0, 4, 5 | 3 |
| cqa1-32758 | 0, 1, 2, 3, 4, 5 | **6（全闲）** |
| bjb2-40593 | — | 0 |
| **合计** | | **16 张** |

cqa1-32758 整机闲置，是当前最大算力空窗，建议尽快派任务。

---

## 4. π0.5 CRM 训练进度（bjb1-18228）

`train-crm-pi05-unified-3suite-r2`（object+spatial+goal 联合训练，obs_dim=2048, batch=256, epoch=50, lr=1e-3）

- 已完成：**epoch 24 / 50**，约 8h44m
- 最近 val_loss 走势：
  - epoch 21 → 0.004986 (new best)
  - epoch 22 → 0.004997
  - epoch 23 → **0.004856 (current best)**
  - epoch 24 进行中，batch 650/684
- train_loss 已平台到 0.0085 左右
- 剩余 ~26 epoch，按当前节奏估算还需 ~9–10h，应在今天傍晚完成

---

## 5. 异常 / 需要注意的事项

1. **bjb1-32546 GPU 0 A1 baseline object s42 已停**：GPU idle、无 python 进程、`/tmp/agent-ml-exit/` 无 `eval-a1-baseline-object-s42.exit`。与"A1 已放弃 D137"一致。
2. **bjb1-18228 GPU 3 precompute 跑 47 小时**：PID 114507 (`--precompute --model pi05 --benchmark long --K 10`) 已跑近 2 天。需要确认是否真的在产出 cache 还是已挂死。建议下次扫描时对比 cache 目录文件数/大小变化。
3. **bjb2-28827 GPU 1 spatial reconvla s42 日志有 OOM**：log 尾部记录 `torch.OutOfMemoryError: CUDA out of memory. ... Process 388593 has 14.30 GiB in use`。但 PID 388593 仍存活、显存 14.6GB、GPU util 20%，似乎在 OOM 之后又恢复运行。需要确认输出是否完整。
4. **bjb1-18228 两个旧 supp 日志疑似未跑完**：
   - `eval-supp-long-vla-only-s47-r2.log`（30 行，无 success rate，无 exit file）
   - `eval-supp-goal-vla-only-s47.log`（50 行，无 success rate，无 exit file，停在 task 9/10）
   时间戳均 May 24 16:32，应该已经死了。`long-vla-only-s47` 主结果已由 `/tmp/eval_long_vla_s47.log` (59.5%) 顶替；`goal-vla-only-s47` 需要补跑。
5. **cqa1-32758 4 个 long-s46-r2 任务全部失败**：`eval-supp-long-{adapt-tau025,crm-norm005,k2mean,reconvla}-s46-r2.log` 每个仅 14–16 行（无 success rate，无 exit file，无 Traceback——意味着启动后立刻挂掉或被 kill）。需要在闲置的 cqa1 GPU 上重跑。
6. **`-v2` 系列日志 Traceback**：bjb1-32546 / bjb2-28827 的 v2 系列 pi05 vla_only 日志都有 Traceback，但都打出了 Overall success rate。可能是单 task 失败后被 catch 然后继续——结果可信度低于 non-v2，使用前确认 JSON 输出。
7. **bjb2-40593 K=5 spatial s42 仍在跑**（2h25m），日志显示已完成 5 个 task（95/90/100/100/65% — 平均 ~90%），当前在 task 6 (`pick_up_the_black_bowl_on_the_ramekin`，0/15，疑似零成功率拖慢整体）。预计还需 1–1.5h 完成。

---

## 6. 建议操作（仅建议，不执行）

- 派 cqa1-32758 跑 long-s46-r2 的 4 个失败任务（每 GPU 一个），同时补 `goal-vla-only-s47` 一个。
- 在 bjb1-32546 GPU 0/2/3/4/5 上启动新任务（5 张 idle 4090）。
- 在 bjb2-28827 GPU 0/4/5 上启动新任务。
- 检查 bjb1-18228 precompute 进度（cache 目录文件数），决定是否 kill。
- bjb2-40593 等 K=5 spatial s42 跑完后收 result（约 1–1.5h 内）。

