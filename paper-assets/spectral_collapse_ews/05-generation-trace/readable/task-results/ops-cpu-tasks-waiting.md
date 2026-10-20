# ops cpu tasks waiting

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cpu_tasks_waiting_20260517T160332_result.json`
- **Structured JSON:** [`10df7319939a19cea84a.json`](../../sessions/10/10df7319939a19cea84a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Task 1: Phase 0 统计分析

**eff_rank 每代变化（Gen 2 峰值后）：**
| Gen | Delta |
|-----|-------|
| 2→3 | -3.13 |
| 3→4 | -7.64 |
| 4→5 | -6.46 |
| 5→6 | -6.21 |
| 6→7 | -8.80 |
| 7→8 | -7.44 |
| 8→9 | -8.31 |

趋势：**近似线性下降**，每代 ~6-9，略有加速（后期 7-8.3 vs 早期 3-7.6）

**log_det 每代变化（Gen 2 峰值后）：**
| Gen | Delta |
|-----|-------|
| 2→3 | -29.36 |
| 3→4 | -35.52 |
| 4→5 | -34.88 |
| 5→6 | -35.00 |
| 6→7 | -30.98 |
| 7→8 | **-52.07** |
| 8→9 | **-44.55** |

趋势：Gen 2-6 大致恒定 ~30-35/gen，但 **Gen 7→8、8→9 出现加速**（-52、-45），Phase 0 后期 log_det 下降在加速

**ppl 每代增长：**
| Gen | Abs Delta | Pct |
|-----|-----------|-----|
| 0→1 | +1.83 | +19.2% |
| 1→2 | +2.20 | +19.3% |
| 2→3 | +2.67 | +19.7% |
| 3→4 | +3.55 | +21.8% |
| 4→5 | +4.79 | +24.2% |
| 5→6 | +6.32 | +25.7% |
| 6→7 | +7.98 | +25.8% |
| 7→8 | +10.40 | +26.7% |
| 8→9 | +14.03 | +28.5% |

趋势：**指数加速确认**。绝对增量从 1.83 涨到 14.03，增长率从 19% 升至 28.5%

**HellaSwag 每代变化：**
| Gen | Delta |
|-----|-------|
| 0→1 | -0.023 |
| 1→2 | -0.014 |
| 2→3 | -0.010 |
| 3→4 | -0.010 |
| 4→5 | -0.012 |
| 5→6 | -0.013 |
| 6→7 | -0.012 |
| 7→8 | -0.009 |
| 8→9 | -0.009 |

趋势：**近似线性，略有减速**（~0.009-0.013/gen），初始下降最大（Gen 0→1: -0.023）后趋于稳定

---

## Task 2: launch_exp_004.sh
创建成功：`/root/spectral_collapse_ews/scripts/launch_exp_004.sh` (249 bytes, rwxr-xr-x)

---

## Task 3: 5-panel figure
已有绘图脚本运行成功。输出路径：
- `/root/spectral_collapse_ews/paper/figures/phase0_spectral_trajectory.pdf`
- `/root/spectral_collapse_ews/paper/figures/phase0_spectral_trajectory.png`

注意：现有脚本输出到 `paper/figures/` 而非 `figures/`，使用的数据与提供数据一致（HellaSwag 仅到 Gen 5）。

---

## Task 4: exp_005 controller
- `phase1_adaptive_seed42_results.json` **尚未生成**
- checkpoint 目录：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/adaptive_seed42/` 已有 **gen_0** 和 **gen_1**（gen_1 最后更新 May 17 22:45）
- Gen 2 尚未完成，controller 状态待 gen_2 产出后才能查看

---
