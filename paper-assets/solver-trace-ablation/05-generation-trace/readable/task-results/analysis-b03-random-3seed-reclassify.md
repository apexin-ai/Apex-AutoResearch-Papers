# analysis b03 random 3seed reclassify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_b03-random-3seed-reclassify_20260515T182051_result.json`
- **Structured JSON:** [`cd20df95726584a656be.json`](../../sessions/cd/cd20df95726584a656be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 registry 全部更新完成。

## 结果汇总

### β=0.3 Random 三 seed 标准 classify_h7 taxonomy

| Seed | Proved | H7 | H1 | H8 | Genuine | Gen% |
|------|--------|-----|-----|-----|---------|------|
| s42 (plan017) | 48 | 4 | 44 | 0 | 0 | 0.0% |
| s43 (exp1-r4) | 92 | 7 | 82 | 0 | 3 | 3.3% |
| s44 (exp1-r2) | 23 | 0 | 23 | 0 | 0 | 0.0% |

### 新旧对比

| Experiment | Field | Old | New | Change |
|---|---|---|---|---|
| plan017-s42 | H7 | 0 | **4** | +4 (H7a 从 H1 拆出) |
| plan017-s42 | H1 | 48 | **44** | -4 |
| plan017-s42 | genuine | 0 | 0 | — |
| exp1-s43-r4 | H7 | 7 | 7 | — |
| exp1-s43-r4 | H1 | 82 | 82 | — |
| exp1-s43-r4 | genuine | 3 | 3 | — |
| exp1-s44-r2 | H7 | 0 | 0 | — |
| exp1-s44-r2 | H1 | 23 | 23 | — |
| exp1-s44-r2 | genuine | 0 | 0 | — |

唯一变化：plan017-s42 有 4 个样本从 H1 重分类为 H7a（多前提中有单前提文本匹配结论的情况，之前旧版本未检测到）。s43 和 s44 的结果与之前完全一致。三个实验均 H8=0。JSON 审计文件已保存至 `/root/autodl-tmp/outputs/h7_classification/random_b03_3seed_classify.json`。

---
