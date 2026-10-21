# Ghost 实验修复 + 未追踪进程注册 + 新实验部署报告

**日期**: 2026-05-17 21:31 UTC

---

## 子任务 1: Ghost 实验修复

| 字段 | 值 |
|------|-----|
| exp_id | eval-obs-only-object-norm01-seed45 |
| 原状态 | RUNNING (ghost) |
| 新状态 | DONE |
| conclusion | failed |
| 原因 | PID 474319 on bjb1-18228 cuda:0 已死 28h+，GPU 空闲 |
| notes | PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated. |

**结果**: 成功修复。Registry 已更新为 DONE/failed。

---

## 子任务 2: 未追踪进程注册

### 2.1 eval-obs-only-object-norm005-seed43-r2
| 字段 | 值 |
|------|-----|
| server | bjb1-32546 |
| GPU | cuda:0 |
| PID | 433500 |
| PID 验证 | ✅ 进程活跃，命令匹配 |
| nvidia-smi | ✅ PID 433500 on GPU 0 |
| Registry | ✅ RUNNING |
| Cron | ✅ 已注册 (interval=120s) |

### 2.2 eval-obs-only-object-norm003-seed43
| 字段 | 值 |
|------|-----|
| server | bjb1-18228 |
| GPU | cuda:1 |
| PID | 621127 |
| PID 验证 | ❌ 进程已死 |
| nvidia-smi | ❌ GPU 1 无进程，bjb1-18228 全部 4 GPU 空闲 |
| Registry | DONE (failed) |
| Cron | 未注册（进程已死） |
| notes | PID 621127 on bjb1-18228 cuda:1 died. Ghost experiment discovered during registration attempt. |

**⚠️ 发现**: 该进程在注册时已死，标记为 DONE/failed。需要重新部署。

### 2.3 eval-perdof-object-norm02-seed47
| 字段 | 值 |
|------|-----|
| server | bjb2-28827 |
| GPU | cuda:2 |
| PID | 404983 |
| PID 验证 | ✅ 进程活跃，命令匹配 |
| nvidia-smi | ✅ PID 404983 on GPU 2 |
| Registry | ✅ RUNNING |
| Cron | ✅ 已注册 (interval=120s) |

### 2.4 eval-random-selection-object-seed42
| 字段 | 值 |
|------|-----|
| server | bjb2-40593 |
| GPU | cuda:0 |
| PID | 395256 |
| PID 验证 | ✅ 进程活跃，命令匹配 |
| nvidia-smi | ✅ PID 395256 on GPU 0 |
| Registry | ✅ RUNNING |
| Cron | ✅ 已注册 (interval=120s) |

**汇总**: 3/4 进程成功注册为 RUNNING + cron。1/4 (norm003-seed43) 发现已死，标记为 DONE/failed。

---

## 子任务 3: 部署 perdof ε=0.2 seed45 on bjb1-18228 cuda:0

| 字段 | 值 |
|------|-----|
| exp_id | eval-perdof-object-norm02-seed45-deploy |
| server | bjb1-18228 |
| GPU | cuda:0 |
| tmux session PID | 632156 |
| python PID | 632167 |
| hypothesis | perdof CRM (ε=0.2) seed45 on LIBERO-Object |
| Cron | ✅ 已注册 (interval=120s) |
| 部署验证 | ✅ python 进程活跃，SmolVLA 模型正在加载中 |

**注意**: 部署时发现 bjb1-18228 cuda:1 上已有一个 eval-perdof-object-norm02-seed45-r2 (PID 631702) 在运行，这不在本次任务列表中。

---

## 需要后续关注

1. **eval-obs-only-object-norm003-seed43** 需要重新部署（PID 621127 已死）
2. **eval-perdof-object-norm02-seed45-deploy** 需要确认模型加载完成后 GPU 正常使用
3. bjb1-18228 上 eval-perdof-object-norm02-seed45-r2 (cuda:1) 是否在 registry 中追踪？
