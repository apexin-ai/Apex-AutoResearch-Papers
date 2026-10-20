# analysis exp017 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp017_bootstrap_ci_20260513T064414_result.json`
- **Structured JSON:** [`adab6e753ab21c1d88a4.json`](../../sessions/ad/adab6e753ab21c1d88a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到本地。以下是 4-model bootstrap CI 汇总：

---

## exp-017 Qwen-1.5B-cont（关键结果）

```
Qwen-cont 1v2: AUC=0.6112, CI=[0.6015, 0.6213], p<0.002
  → CI lower 0.6015 > 0.60 → K*=2 ROBUST

Qwen-cont 2v3: AUC=0.5609, CI=[0.5511, 0.5712], p<0.002
Qwen-cont 3v4: AUC=0.5409, CI=[0.5308, 0.5508], p<0.002
Qwen-cont 4v5: AUC=0.5141, CI=[0.5035, 0.5255], p=0.006
```

**CI 下界 0.6015 刚好跨过 0.60 阈值，K\*=2 统计稳健，但非常边缘（仅超 0.0015）。**

## 4-model 对比（1v2 pair）

| Model | AUC 1v2 | 95% CI | p-value | K\*=2 |
|-------|---------|--------|---------|-------|
| Qwen-1.5B-rewrite | 0.6955 | [0.6859, 0.7041] | <0.002 | robust |
| Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | <0.002 | robust |
| OLMo-1B | 0.6145 | [0.6045, 0.6247] | <0.002 | robust |
| **Qwen-1.5B-cont** | **0.6112** | **[0.6015, 0.6213]** | **<0.002** | **robust (边缘)** |

JSON 已存至 `artifacts/bootstrap_ci_4model.json`。

---
