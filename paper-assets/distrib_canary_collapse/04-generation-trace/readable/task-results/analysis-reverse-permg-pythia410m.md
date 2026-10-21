# analysis reverse permg pythia410m

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reverse_permg_pythia410m_20260517T123236_result.json`
- **Structured JSON:** [`36429eafa21cecdcee7c.json`](../../sessions/36/36429eafa21cecdcee7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。

## 结果

```
Reverse PermG (H0: downstream does NOT Granger-cause canary)
Pair                         |   F_stat |    p_raw |    p_fdr | sig
----------------------------------------------------------------------
token_entropy <- distinct_1  |   0.4907 |   0.4965 |   0.5777 | N
token_entropy <- distinct_2  |   0.4953 |   0.4765 |   0.5777 | N
token_entropy <- distinct_3  |   0.4193 |   0.5055 |   0.5777 | N
token_entropy <- mauve       |   0.1121 |   0.7353 |   0.7353 | N
ece <- distinct_1            |  59.6706 |   0.0320 |   0.0959 | N
ece <- distinct_2            |  37.5922 |   0.0320 |   0.0959 | N
ece <- distinct_3            |  25.2940 |   0.0360 |   0.0959 | N
ece <- mauve                 |   0.7923 |   0.4026 |   0.5777 | N

Summary: 0/8 significant (FDR q<0.05)
```

**对比：**
- Forward: **6/8 significant** (entropy/ece → distinct_1/2/3 全显著，mauve 两对不显著)
- Reverse: **0/8 significant**

符合预期：因果方向是单向的 (canary → downstream)，reverse 方向无显著性。注意 ece ← distinct_1/2/3 的 raw p 在 0.032-0.036 边缘，但 FDR 校正后全部 >0.05，进一步确认 forward 方向的因果关系不是双向反馈。

结果 JSON 已保存至 `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/reverse_permg_results.json`。

---
