# exp plan 015 olmo wild calibration

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_015_olmo_wild_calibration_20260515T224354_result.json`
- **Structured JSON:** [`c3f847237eafded81efe.json`](../../sessions/c3/c3f847237eafded81efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**OLMo wild calibration:**
| 指标 | OLMo | Pythia | GPT-2 XL |
|------|------|--------|----------|
| CV accuracy | 78.93% ± 0.39% | 78.78% ± 0.56% | 84.12% ± 0.40% |
| WikiText d0% | 98.53% | 100% | 99.27% |
| C4 d0% | 95.28% | 79.76% | 77.62% |
| C4 FPR (非d0) | 4.72% | 20.24% | 22.38% |

**C4 depth 分布:**
| depth | OLMo | Pythia | GPT-2 XL |
|-------|------|--------|----------|
| d0 | 95.28% | 79.76% | 77.62% |
| d1 | 2.92% | 19.68% | 9.04% |
| d2 | 0.50% | 0.34% | 3.72% |
| d3 | 1.30% | 0.22% | 9.62% |

**关键发现:** OLMo 的 C4 d0 率(95.28%)远高于预期的 75-82%。原因是 OLMo 的 d1-d3 递归生成特征与 d0 差异更大，RF 学到更宽的 d0 决策边界，导致更多 C4 文本被正确归类为 d0（FPR 仅 4.72%，远低于 Pythia 和 GPT-2 XL 的 ~20%）。

WikiText d0 率 98.53% 略低于另外两个模型，但仍然非常高（8/546 被误分类）。

结果已保存至 `results/plan_015_wild_data/olmo_wild_calibration.json`。

---
