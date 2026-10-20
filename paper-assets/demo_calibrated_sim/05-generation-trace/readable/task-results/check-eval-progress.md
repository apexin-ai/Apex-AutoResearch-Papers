# check eval progress

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress_20260512T223709_result.json`
- **Structured JSON:** [`157ec70cf8cc28515919.json`](../../sessions/15/157ec70cf8cc28515919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## H-gate Eval 进度报告

### hgate-dpo002 (dpo_eval_v2, GPU:3, port 8001)

| 阶段 | 状态 | 变体完成 |
|------|------|---------|
| run_1 | **已完成** | 6/6 |
| run_2 | 进行中 | 1/6 (第2变体执行中) |
| run_3 | 未开始 | — |
| run_4 | 未开始 | — |

**总进度: 7/24 变体 ≈ 29%**

run_1 已有结果 (H-gate):
- H1: **PASS** (politeness=0.489, threshold>0.3)
- H2: **FAIL** (calibrated variants 的 politeness 反而升高，未达到 30% 改善)
- H3: **FAIL** (aave/indian_english completion 低于 80% baseline retention)
- baseline completion=22.2%, politeness=0.489

---

### hgate-dpo003 (dpo_eval_v3, GPU:2, port 8002)

| 阶段 | 状态 | 变体完成 |
|------|------|---------|
| run_1 | 进行中 | 2/6 (第3变体执行中) |
| run_2 | 未开始 | — |
| run_3 | 未开始 | — |
| run_4 | 未开始 | — |

**总进度: 2/24 变体 ≈ 8%**

---

### 时间估算

根据 dpo002 run_1 的实际数据，每变体耗时 17~50 分钟（平均 ~28 min），**每轮 run ≈ 2.5~3 小时**。

| 实验 | 已运行 | 剩余变体 | 预估剩余时间 |
|------|--------|---------|-------------|
| dpo002 | ~3.5h (从03:06) | 17 | **~8 小时** |
| dpo003 | ~1.3h (从05:17) | 22 | **~10 小时** |

原估计 ~80min/实验偏差较大，实际 4 runs × 6 variants 总耗时约 **10-12 小时/实验**。

---

### GPU 利用

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 2 | 43% | 21.6/24.0 GB | hgate-dpo003 vLLM |
| 3 | 45% | 21.6/24.0 GB | hgate-dpo002 vLLM |
| 0,1 | 0-36% | ~11 GB | 其他项目 (rl-active-probe-fl) |
| 5 | 100% | 9.3 GB | 其他项目 |
| 4 | 0% | 空闲 | — |

### 错误

两个实验各出现 **1 次 ContextWindowExceededError**（16385 > 16384 tokens）。tau-bench 已处理，该 episode 标记失败，不阻塞后续执行。非致命。

---
