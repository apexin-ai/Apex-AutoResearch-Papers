# exp review p1d table3 6gen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p1d-table3-6gen_20260515T134117_result.json`
- **Structured JSON:** [`0848a7bada473696c9b5.json`](../../sessions/08/0848a7bada473696c9b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

**6-gen LOGO single baselines (3-class, class-balanced downsample)**

| Baseline | 100/3 F1 | 100/3 CI | 200/6 F1 | 200/6 CI | Delta |
|---|---|---|---|---|---|
| AvgLogProb | **0.737** | [0.732, 0.742] | **0.737** | [0.732, 0.743] | +0.0005 |
| FastDetectGPT | **0.688** | [0.683, 0.693] | **0.688** | [0.683, 0.693] | -0.0002 |
| LD Score | **0.655** | [0.649, 0.660] | **0.654** | [0.648, 0.659] | -0.0011 |
| Binoculars | **0.416** | [0.411, 0.422] | **0.417** | [0.411, 0.422] | +0.0003 |

**关键结论**：超参 100/3 vs 200/6 对所有 single baseline 的影响 < 0.002 pp，完全可忽略。可以直接回应 M6 的超参质疑。

与 5-gen 口径对比变化（新 6-gen 值 vs 旧 5-gen 值）：
- AvgLogProb: 0.737 vs 0.765（含 qwen3-8b 后下降）
- FDG: 0.688 vs 0.627（上升，旧值可能是不同 pipeline）
- LD: 0.655 vs 0.721（下降）
- Bino: 0.417 vs 0.579（大幅下降）

结果已保存到 `results/review_p1d_6gen_baselines.json`，registry 已更新为 DONE。

---
