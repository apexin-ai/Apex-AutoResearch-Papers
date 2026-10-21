# analysis table3 r1 8b 60 20 20

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table3_r1_8b_60_20_20_20260518T172824_result.json`
- **Structured JSON:** [`29feb7f5d15e055b0f4e.json`](../../sessions/29/29feb7f5d15e055b0f4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下（完整 JSON 已保存至服务器 `artifacts/table3_r1_8b_60_20_20/results.json`）：

```
R1-8B (W=3, L14, 60/20/20, PCA=100d, 10k bootstrap):
  n_test = 1961 steps from 43 traces
  HS Prec: 0.629 [0.495, 0.766]
  Text Prec: 0.429 [0.301, 0.571]
  ΔPrec: +0.201pp, p<0.0001

  HS BA: 0.823 [0.776, 0.869]
  Text BA: 0.648 [0.586, 0.709]
  ΔBA: +0.175pp, p<0.0001

  HS FPR: 0.158 [0.096, 0.225]
  Text FPR: 0.237 [0.161, 0.322]
  ΔFPR: -0.079pp, p=0.0140

  HS AUROC: 0.903 [0.864, 0.941]
  Text AUROC: 0.719 [0.640, 0.794]
  ΔAUROC: +0.184pp, p<0.0001

  HB (3 tests: Prec, BA, FPR): 3/3 pass
```

配置细节：
- 209 traces → split 125/41/43, train+val=166 用于训练, test=43 traces (1961 steps)
- PCA explained variance: 49.5%
- HB adj p-values: Prec<0.0001, BA<0.0001, FPR=0.0140
- 全部 4 个指标 HS 显著优于 text baseline

---
