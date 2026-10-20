# diag full gpu audit 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full_gpu_audit_19828_20260518T234937_result.json`
- **Structured JSON:** [`28ef0004ec2037b4c420.json`](../../sessions/28/28ef0004ec2037b4c420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (westd-19828)

### cuda:0 — scale_14b (Pythia-1.4B, α=0.50, s42)
| 项目 | 值 |
|------|-----|
| PID | 369475 |
| 显存 | 36736 / 97887 MiB (37.5%) |
| GPU 利用率 | 94% |
| 运行时间 | 7h15m |
| 进度 | gen_10/10 — checkpoint 刚写入 (07:50)，正在训练最后一代或计算 metrics |
| all_metrics.json | **不存在** |
| 状态 | **运行中，接近完成** |
| 可用性 | **不可用** — 进程仍在占用 |

### cuda:1 — smollm3_fp32 (SmolLM3-3B, α=1.0, s42, fp32)
| 项目 | 值 |
|------|-----|
| PID | 399353 |
| 显存 | 37598 / 97887 MiB (38.4%) |
| GPU 利用率 | 98% |
| 运行时间 | 1h55m |
| 进度 | gen_1/10 — gen_1 已有 synthetic_data，正在训练 gen_2 |
| all_metrics.json | **不存在** |
| 状态 | **运行中，早期阶段**，预计还需 ~8h |

### 其他
- **PID 395612**: 已确认不存在，无孤儿进程
- **闲置 tmux sessions**: `generalize_opt1b_wiki_a100_s42` 和 `generalize_pythia410m_wiki_a100_s42` (May 17 创建，已完成，shell 空闲)
- **gen_10 metrics**: 尚未生成，scale_14b 完成后再读取
- **cuda:0 预计释放**: scale_14b 在 gen_10 最后阶段，预计 30min-1h 内完成

---
