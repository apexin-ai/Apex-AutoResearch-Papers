# check seed456 progress

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed456_progress_20260514T100206_result.json`
- **Structured JSON:** [`2283acea532f9e043a23.json`](../../sessions/22/2283acea532f9e043a23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## seed=456 实验进度汇总

### 实验 1: `chain_cuda0_seed456` (GPU 0) — uncurated_seed456
| 项目 | 状态 |
|------|------|
| tmux session | ✅ 运行中 |
| 当前进度 | **Gen 4/7**，步骤 [3/5] Training student |
| 已保存结果 | gen_0 ~ gen_5（含中间目录） |
| Gen 3 指标 | PPL=59.08, RankMe=431.32, kNN=0.988 |
| 预估剩余 | uncurated 还剩 ~3 gen ≈ **75-90 min**，之后自动接 rgds_seed456（7 gen ≈ 3-3.5h） |

### 实验 2: `medium_external_seed456` (GPU 1) — external_seed456
| 项目 | 状态 |
|------|------|
| tmux session | ✅ 运行中 |
| 当前进度 | **Gen 5/7**，步骤 [3/5] Training student |
| 已保存结果 | gen_0 ~ gen_6（含中间目录） |
| Gen 4 指标 | PPL=60.91, RankMe=422.54, kNN=0.988 |
| 预估剩余 | external 还剩 ~2 gen ≈ **50-60 min**，之后 `auto_seed456_cuda1` 自动启动 random50_seed456（7 gen ≈ 3-3.5h） |

### `auto_seed456_cuda1`
- ✅ 运行中，正在轮询等待 `medium_external_seed456` 完成（每分钟检查一次）

### GPU 使用
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | **35%** | 71.6 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | **0%** | 28.7 / 97.9 GB |

### 异常
- **GPU 1 利用率瞬时 0%**：external 实验 log 显示正在 training，但 nvidia-smi 快照抓到了 batch 间隙。显存已分配 28.7GB，模型在跑，不是问题。
- 无 OOM、无进程崩溃、无磁盘异常。
- 两个 medium 实验均未产出 `all_results.json`（尚未跑完全部 7 gen）。

---
