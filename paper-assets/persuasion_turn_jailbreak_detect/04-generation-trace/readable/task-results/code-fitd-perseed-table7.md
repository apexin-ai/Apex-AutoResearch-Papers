# code fitd perseed table7

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fitd-perseed-table7_20260521T140517_result.json`
- **Structured JSON:** [`6a609fe8720f74e6c183.json`](../../sessions/6a/6a609fe8720f74e6c183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存。汇总：

### FITD Table 7 per-seed 结果

**数据来源**：`per_sample_predictions/fitd_ood_per_sample.json`（由 exp35 使用 plan_002 production checkpoints 生成，今天 04:28 运行）

| Method | K=1 | K=2 | K=3 | K=5 | Full |
|--------|-----|-----|-----|-----|------|
| 9-class (ours) | 1.000±.000 | 1.000±.000 | -- | -- | 1.000±.000 |
| Vanilla DeBERTa | .954±.039 | .952±.061 | -- | -- | .994±.009 |
| TF-IDF LR | 1.000 | -- | -- | -- | 1.000 |

### 偏差标记

Vanilla 所有列的 3-seed 均值与当前 Table 7 值有显著偏差：

| 列 | Table 7 现值 | 3-seed mean | Δ | 原因 |
|----|-------------|-------------|---|------|
| K=1 | .990 | .954 | .036 | 现值仅用 seed 42（.990） |
| K=2 | 1.000 | .952 | .048 | 现值仅用 seed 42（1.000） |
| Full | 1.000 | .994 | .006 | 现值仅用 seed 42（1.000） |

**根因**：Table 7 FITD 部分之前只用了 seed 42 的结果填入。seed 456 的 vanilla 表现明显低于其他两个 seed（K1=.900, K2=.866, Full=.981），拉低了均值。

9-class 三个 seed 全部 1.000，无偏差。

### LaTeX 建议行
```
9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & -- & -- & 1.000$\pm$.000 \\
Vanilla DeBERTa & .954$\pm$.039 & .952$\pm$.061 & -- & -- & .994$\pm$.009 \\
```

产出文件：`/root/persuasion_turn_jailbreak_detect/results/exp41_fitd_table7_perseed.json`

---
