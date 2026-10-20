# check running exp status v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_exp_status_v2_20260524T101547_result.json`
- **Structured JSON:** [`47680c8183555e9fda75.json`](../../sessions/47/47680c8183555e9fda75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. code_domain_olmo (PID 167297, cuda:1)

| 项目 | 值 |
|------|-----|
| 状态 | **RUNNING** |
| 已运行 | 53 min |
| 当前阶段 | Phase 1 生成 depth chain, **depth 4: 301/344 (87.5%)** |
| GPU | 68% util, 5.8/97.9 GB |

进度详情：5500 samples, max_depth=5, depth 1-3 已完成。depth 4 还剩 ~43 batches (~1.5 min)。之后还需 depth 5 生成 (~14 min) + scoring + eval。**预计剩余 ~30-35 min。**

### 2. gemma27b_filtering (PID 169724, cuda:3)

| 项目 | 值 |
|------|-----|
| 状态 | **RUNNING** |
| 已运行 | 29 min |
| 当前阶段 | binary_ours seed=123, eval 阶段 (loglikelihood 20%/96336) |
| GPU | 85% util, 10.8/97.9 GB |
| 总任务 | 3 strategies × 3 seeds = 9 runs |
| 已完成 | 4/9 |

已产出指标：

| Strategy | Seed | MMLU | HellaSwag |
|----------|------|------|-----------|
| no_filter | 42 | 0.596 | 0.664 |
| no_filter | 123 | 0.595 | 0.662 |
| no_filter | 456 | 0.596 | 0.663 |
| binary_ours | 42 | **0.597** | **0.677** |

binary_ours 在 HellaSwag 上比 no_filter 高 **+1.3pp**，MMLU 基本持平。每个 run 约 7 min，还剩 5 个 run。**预计剩余 ~35 min。**

---
