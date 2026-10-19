# audit server status check 20260519b

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_server-status-check-20260519b_20260519T115339_result.json`
- **Structured JSON:** [`b4aa447c27d9c2b4d2fc.json`](../../sessions/b4/b4aa447c27d9c2b4d2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

# 4 台服务器实验状态全面排查报告

## 1. bjb1-32546 (6x RTX 4090)

### GPU 状态
| GPU | Util | Mem Used / Total | 占用实验 |
|-----|------|------------------|----------|
| 0 | 25% | 5168 / 24564 MiB | argmin-k5-seed42 |
| 1 | 21% | 1987 / 24564 MiB | spatial-obs-only-norm02-seed45 |
| 2 | 25% | 5168 / 24564 MiB | argmin-k5-seed43 |
| **3** | **0%** | **2 / 24564 MiB** | **空闲** |
| 4 | 99% | 4818 / 24564 MiB | perdof-norm005-seed45 + obs-only-default-seed48 **共享!** |
| 5 | 26% | 5168 / 24564 MiB | argmin-k5-seed45 |

### Tmux Sessions (6)
`eval-argmin-object-k5-seed42`, `eval-argmin-object-k5-seed43`, `eval-argmin-object-k5-seed45`, `eval-obs-only-default-seed48-t16`, `eval-perdof-norm005-seed45-t16`, `eval-spatial-obs-only-norm02-seed45`

### 实验状态
| 实验 | 状态 | GPU | 运行时间 | 备注 |
|------|------|-----|----------|------|
| argmin-k5-seed42 (883706) | **运行中** | 0 | 18h02m | |
| argmin-k5-seed43 (883975) | **运行中** | 2 | 17h59m | |
| argmin-k5-seed45 (884249) | **运行中** | 5 | 17h56m | |
| spatial-obs-only-norm02-seed45 (758847) | **运行中** | 1 | | |
| obs-only-default-seed48-r2 (755878) | **运行中** | 4 | ~10h | 与 perdof 共享 GPU4 |
| perdof-norm005-seed45-r2 (755612) | **运行中** | 4 | ~10h | 与 default-seed48 共享 GPU4 |
| **perdof-norm003-seed48** | **已完成 SR=0.13** | - | - | JSON 已写入 |

### 空闲 GPU: **GPU 3**
### 已完成未收割: `eval_object_perdof_norm003_seed48.json` — **SR=0.13**

---

## 2. bjb2-28827 (6x RTX 4090)

### GPU 状态
| GPU | Util | Mem Used / Total | 占用实验 |
|-----|------|------------------|----------|
| 0 | 0% | 1923 / 24564 MiB | perdof-norm005-seed45 (CPU 阶段) |
| 1 | 17% | 3749 / 24564 MiB | argmin-k5-seed44 |
| 2 | 99% | 4777 / 24564 MiB | obs-only-norm003-seed44 + random-selection-seed46 **共享!** |
| 3 | 19% | 1987 / 24564 MiB | spatial-obs-only-norm02-seed44 |
| 4 | 17% | 1887 / 24564 MiB | reconvla-k5-seed42 |
| 5 | 19% | 1923 / 24564 MiB | perdof-norm03-seed43 |

### Tmux Sessions (7)
`eval-argmin-object-k5-seed42`, `eval-argmin-object-k5-seed44`, `eval-obs-only-norm003-seed44-t16`, `eval-perdof-norm005-seed45-t16`, `eval-perdof-norm03-seed43-t16`, `eval-random-seed46-t16`, `eval-spatial-obs-only-norm02-seed44`

### 实验状态
| 实验 | 状态 | GPU | 运行时间 | 备注 |
|------|------|-----|----------|------|
| obs-only-norm003-seed44 (657432) | **运行中** | 2 | ~14h | 与 random-seed46 共享 GPU2 |
| perdof-norm03-seed43 (657632) | **运行中** | 5 | ~14h | |
| perdof-norm005-seed45 (664406) | **运行中** | 0 | ~14h | GPU util=0%，在 CPU/sim 阶段 |
| random-selection-seed46 (693631) | **运行中** | 2 | ~10h | 与 norm003-seed44 共享 GPU2 |
| spatial-obs-only-norm02-seed44 (697045) | **运行中** | 3 | ~10h | |
| reconvla-k5-seed42 (718580) | **运行中** | 4 | ~8h | |
| argmin-k5-seed44 (758237) | **运行中** | 1 | 3h33m | |

### 空闲 GPU: **无**
### 已完成未收割: 无（bjb2-28827 上的 `eval_spatial_obs_only_norm02_k5_seed42.json` SR=0.35 是历史结果）

---

## 3. bjb1-18228 (4x RTX 4090)

### GPU 状态
| GPU | Util | Mem Used / Total | 占用实验 |
|-----|------|------------------|----------|
| 0 | 22% | 3804 / 24564 MiB | obs-only-norm005-seed48 |
| **1** | **0%** | **1 / 24564 MiB** | **空闲** |
| 2 | 22% | 3804 / 24564 MiB | perdof-norm005-seed47 |
| 3 | 21% | 3804 / 24564 MiB | perdof-norm003-seed47 |

### Tmux Sessions (3)
`eval-obs-only-object-norm005-seed48`, `eval-perdof-object-norm003-seed47`, `eval-perdof-object-norm005-seed47`

### 实验状态
| 实验 | 状态 | GPU | 运行时间 | 备注 |
|------|------|-----|----------|------|
| obs-only-norm005-seed48 (989965) | **运行中** | 0 | 5h58m | |
| perdof-norm005-seed47 (990235) | **运行中** | 2 | 5h58m | |
| perdof-norm003-seed47 (990503) | **运行中** | 3 | 5h58m | |
| **lto-splitA-vla-only-r3** (989694) | **已完成 SR=0.14** | - | PID 已死 | tmux session 已消失 |

### 空闲 GPU: **GPU 1**
### 已完成未收割: `eval_lto_splitA_vla_only_r3.json` — **SR=0.14**

---

## 4. bjb2-40593 (1x RTX 4090 D)

### GPU 状态
| GPU | Util | Mem Used / Total | 占用实验 |
|-----|------|------------------|----------|
| 0 | 88% | 7286 / 24564 MiB | spatial-obs-only-norm02-seed43 + random-selection-seed46 **共享!** |

### Tmux Sessions (2)
`eval-random-selection-seed46-t16`, `eval-spatial-obs-only-norm02-seq`

### 实验状态
| 实验 | 状态 | GPU | 运行时间 | 备注 |
|------|------|-----|----------|------|
| spatial-obs-only-norm02-seed43 (508930) | **运行中** | 0 | ~10h | 与 random-seed46 共享唯一 GPU |
| random-selection-seed46 (503784) | **运行中** | 0 | ~10h | 与 spatial 共享唯一 GPU |
| **scalar-seed45-r2** | **已完成 SR=0.07** | - | tmux 已消失 | JSON 19:40 写入 |

### 空闲 GPU: **无**（单卡，两任务共享）
### 已完成未收割: `eval_object_scalar_seed45_r2.json` — **SR=0.07**

---

## 汇总

### 空闲 GPU（可立即调度新实验）
| 服务器 | GPU | 显存 |
|--------|-----|------|
| bjb1-32546 | GPU 3 | 24564 MiB |
| bjb1-18228 | GPU 1 | 24564 MiB |

### 已完成未收割实验
| 服务器 | 实验 | SR |
|--------|------|-----|
| bjb1-32546 | perdof-norm003-seed48 | **0.13** |
| bjb1-18228 | lto-splitA-vla-only-r3 | **0.14** |
| bjb2-40593 | scalar-seed45-r2 | **0.07** |

### GPU 共享冲突（可能互相拖慢）
| 服务器 | GPU | 共享实验 | 当前 util |
|--------|-----|----------|-----------|
| bjb1-32546 | GPU 4 | perdof-norm005-seed45 + obs-only-default-seed48 | 99% |
| bjb2-28827 | GPU 2 | obs-only-norm003-seed44 + random-selection-seed46 | 99% |
| bjb2-40593 | GPU 0 | spatial-obs-only-norm02-seed43 + random-selection-seed46 | 88% |

---
