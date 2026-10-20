# monitor hgate dpo003 merged progress

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_hgate-dpo003-merged-progress_20260513T054541_result.json`
- **Structured JSON:** [`0e1cd52345afeef41298.json`](../../sessions/0e/0e1cd52345afeef41298.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 进程状态
- PID 688636: **存活**，已运行 4h00m03s
- 结构：4 runs（每 run 6 variants × 20 tasks = 120 tasks），双 GPU 并行

### 进度

| Run | 状态 | 进度 | 备注 |
|-----|------|------|------|
| Run 1 | **完成** | 120/120 | 结果已保存 |
| Run 2 | 运行中 | ~105/120 (87%) | 第6个 variant，task 5/20 |
| Run 3 | **完成** | 120/120 | 结果已保存 |
| Run 4 | 运行中 | ~103/120 (86%) | 第6个 variant，task 3/20 |

**总进度：~448/480 (93%)**

### 已完成 Runs 的 H-gate 结果

| | Run 1 | Run 3 |
|---|---|---|
| **H1** (baseline quality) | **PASS** (politeness=0.475) | **PASS** (politeness=0.532) |
| **H2** (calibration improvement ≥30%) | **FAIL** | **FAIL** |
| **H3** (task completion retention ≥80%) | **FAIL** | **FAIL** |
| Baseline completion | 27.8% | 40% |
| Best calibrated completion | 30% (single_dim_politeness) | 35% (single_dim_politeness) |

**核心问题**：H2 全部 variant 的 politeness calibration 为负改善（校准后 politeness rate 反而更高，远离目标值）。H3 也因 completion 下降而失败。

### GPU 占用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 21% | 15.1/24.6 GB |
| GPU 1 | 31% | 16.2/24.6 GB |
| **GPU 2** | **100%** | **22.1/24.6 GB** |
| **GPU 3** | **95%** | **22.1/24.6 GB** |
| GPU 4-5 | 0% | 空闲 |

GPU 0/1 跑的是 vLLM serving，GPU 2/3 满负载推理，符合预期。

### Mistral-7B 下载状态
**已存在**：`/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/`

### 预估剩余时间
每个 variant round 约 18-20 分钟。Run 2 和 Run 4 各剩 ~15 个 task，预计 **15-20 分钟内全部完成**。

---
