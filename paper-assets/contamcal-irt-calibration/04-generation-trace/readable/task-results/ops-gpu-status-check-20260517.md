# ops gpu status check 20260517

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260517_20260517T022947_result.json`
- **Structured JSON:** [`107b6817240141ba8d2a.json`](../../sessions/10/107b6817240141ba8d2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态：全部 6 块 GPU (cuda:0-5) 完全空闲
- 0 MiB 显存占用，0% 利用率，无任何计算进程

### 进程状态：全部 6 个 PID 已终止
| PID | 任务 | 状态 |
|-----|------|------|
| 907482 | Fisher heatmap, cuda:2 | **已终止**（无输出图片，仅有脚本文件） |
| 825638 | Llama d005 eval, cuda:0 | **完成** ✓ |
| 830115 | Llama d000 MMLU signals s4, cuda:1 | **完成** ✓ |
| 822390 | Llama d025 eval, cuda:3 | **完成** ✓ |
| 842929 | Llama d005 MMLU signals, cuda:4 | **完成** ✓ |
| 831033 | Llama d100 eval, cuda:5 | **完成** ✓ |

### 已产出结果
**Llama eval（全部完成，有 `.done` 标记）**：
- `Llama-3.2-3B_d005_s42_aligned/` — 完成于 04:57，包含 mmlu/arc/gsm8k/humaneval + correctness_matrix
- `Llama-3.2-3B_d025_s42_aligned/` — 完成于 04:29
- `Llama-3.2-3B_d100_s42_aligned/` — 完成于 05:26

**Llama signals（全部完成）**：
- `Llama-3.2-3B_d000_s42/` — s1/s2/s4 三个信号 × 3 benchmarks (mmlu/gsm8k/arc) + merged
- `Llama-3.2-3B_d005_s42/` — 同上完整
- `Llama-3.2-3B_d025_s42/` — 同上完整
- `Llama-3.2-3B_d100_s42/` — 同上完整

**Fisher heatmap (PID 907482)**：脚本存在 (`run_fisher_heatmap.py` 修改于 03:57)，但 artifacts 目录中**未找到 heatmap 输出图**。可能是跑完后崩溃、被 kill、或输出到了其他位置。

### tmux：无活跃 session

### 关键发现
**全部 6 块 GPU 自 ~05:26（约 5 小时前）处于完全空闲状态。** Llama eval 和 signals 任务全部正常完成有结果。Fisher heatmap 任务需要确认输出位置或是否需要重跑。

需要我立即启动下一批实验吗？按 C007 优先级，应先安排 0.5B/1.5B s123 signals（如果还有未完成的）。

---
