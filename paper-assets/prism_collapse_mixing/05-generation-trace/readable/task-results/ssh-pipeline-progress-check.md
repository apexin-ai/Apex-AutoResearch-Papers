# ssh pipeline progress check

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pipeline-progress-check_20260515T230711_result.json`
- **Structured JSON:** [`6543715cfbaa8c4875d0.json`](../../sessions/65/6543715cfbaa8c4875d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline 状态汇总

**进程**: PID 197985 存活，已运行 **2h30m**

**当前阶段**: **Gen 2 — synthesis（合成数据生成）**
- `seed42` (Gen2 seed44): **~20%**，速度 ~12,943 tok/s，预计剩余 **~1h43m**
- `seed137` (Gen2 seed139): **~20%**，速度 ~13,209 tok/s，预计剩余 **~1h41m**
- 两个 seed 在 cuda:0 上并行生成，各需生成 100M tokens

**GPU 使用**:
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 50% | 10.6 / 95.6 GB |
| cuda:1 | 71% | 10.6 / 95.6 GB |

**已完成**:
- Gen 0: 信号计算完成（signals_gen0_seed42.json, signals_gen0_seed137.json）
- Gen 1: 完整流程完成（训练 + 信号计算，signals_gen1_seed42/137.json，checkpoints 已产出）
- Gen 1 可视化图表已生成（fig_corpus_trends.pdf, fig_rho_decay.pdf, fig_signal_distributions.pdf）

**剩余工作估算**（Gen 2 起）:
| 阶段 | 预计耗时 |
|------|----------|
| Gen 2 synthesis（当前） | 剩余 ~1h43m |
| Gen 2 mixing + training | ~1-2h |
| Gen 2 signal compute | ~10-20min |
| Gen 3 完整流程 | ~3-4h |

**预计总剩余时间**: **~6-8h**

---
