# exp de bootstrap parallel

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_de-bootstrap-parallel_20260523T035641_result.json`
- **Structured JSON:** [`219b968283f7a03ed251.json`](../../sessions/21/219b968283f7a03ed251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

### 1. 旧进程 Kill 确认
| PID | 进程 | 状态 |
|-----|-------|------|
| 496671 | DE probe serial | killed (defunct → SIGKILL) |
| 507589 | Gemma XNLI bootstrap 主进程 | killed |
| 507351 | Gemma XNLI bootstrap 包装进程 | killed |
| 507591-507636 | 64 个 orphaned multiprocessing workers | 全部 killed |

CPU load：852 → 10.43（1min avg）

### 2. Gemma XNLI 基础 Probe 结果（完好）
| 方向 | Peak bal_acc | Peak layer |
|------|------------|------------|
| EN→EN | 0.9563 | L20 |
| ZH→ZH | 0.8896 | L24 |
| EN→ZH | 0.8944 | L28 |
| ZH→EN | 0.9752 | L21 |

### 3. Dry Run 结果（Llama EN↔DE, 1 seed）
| 方向 | bal_acc | Peak layer |
|------|--------|------------|
| EN→EN | 0.7647 | L10 |
| DE→DE | 0.7610 | L13 |
| EN→DE | 0.6691 | L10 |
| DE→EN | 0.6654 | L25 |
| Asymmetry | -0.37pp | p=1.0 (n=1, 无统计意义) |

### 4. Full n=2000 已启动
- **PID**: 538586
- **Registry**: `de_bootstrap_parallel_114` → RUNNING
- **输出**: `data/llama31/de_bootstrap_n2000_results.json`
- **日志**: `logs/de_bootstrap_n2000_parallel.log`

### 5. 清理
- `de_bootstrap_dryrun.json` 已删除

---
