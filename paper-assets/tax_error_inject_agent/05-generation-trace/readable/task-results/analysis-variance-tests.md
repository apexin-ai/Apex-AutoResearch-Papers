# analysis variance tests

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_variance-tests_20260515T031800_result.json`
- **Structured JSON:** [`205e9036279fb412c30a.json`](../../sessions/20/205e9036279fb412c30a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已写入 `artifacts/variance_tests_levene_bootstrap.json`。

关键结果摘要：

| 检验 | 统计量 | p 值 |
|------|--------|------|
| **Levene 3-group (mean)** | 2.536 | 0.159 |
| **Brown-Forsythe 3-group** | 0.177 | 0.842 |
| **Pairwise Levene: TaxEI vs Vanilla** | 5.204 | 0.085 |
| **F-test: TaxEI vs Vanilla** | 6.953 | 0.252 |
| **Bootstrap P(SD_TaxEI > SD_Vanilla)** | — | 0.688 |
| **Bootstrap P(SD_Random > SD_Vanilla)** | — | 0.699 |

**观测 SD**: Vanilla 3.26pp, Random 6.86pp, TaxEI 8.60pp

所有形式检验均不显著（p > 0.05），符合预期——n=3 时这些检验功效极低。Pairwise Levene TaxEI vs Vanilla 的 p=0.085 是最接近显著的。Bootstrap 显示 ~69% 概率 TaxEI/Random 的 SD 大于 Vanilla，方向一致但因 n=3 远不足以达到统计确定性。

---
