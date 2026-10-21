# analysis exp012 r1024 tau cond

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp012_r1024_tau_cond_20260514T234320_result.json`
- **Structured JSON:** [`7ab46636c0d61be7ce9d.json`](../../sessions/7a/7ab46636c0d61be7ce9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果：

```
NER full (n=529):
  Signal       |   ρ    |   τ
  voting_conf  | 0.3792 | 0.2805
  SJ           | 0.3599 | 0.2646
  EM           | 0.2945 | 0.2208
  FK           | 0.2665 | 0.1974
  logprob      | 0.2052 | 0.1478

NER conditional (n=477):
  Signal       |   ρ    |   τ
  SJ           | 0.3113 | 0.2257
  EM           | 0.3596 | 0.2735
  voting_conf  | 0.3000 | 0.2189
  FK           | 0.1761 | 0.1284
  logprob      | 0.1538 | 0.1111

RE full (n=397):
  Signal       |   ρ    |   τ
  voting_conf  | 0.3498 | 0.2663
  FK           | 0.2752 | 0.2117
  logprob      | 0.2662 | 0.1951
  SJ           | 0.2503 | 0.1878
  EM           | 0.1344 | 0.1081

RE conditional (n=238):
  Signal       |   ρ    |   τ
  EM           | 0.4165 | 0.3256
  SJ           | 0.2457 | 0.1811
  voting_conf  | 0.2409 | 0.1780
  FK           | 0.1139 | 0.0876
  logprob      | 0.0112 | 0.0051
```

关键发现：
- NER conditional 中 **EM 跃升为最强信号**（ρ=0.360），超过 voting_conf（0.300）和 SJ（0.311）
- RE conditional 中 **EM 大幅跃升**（ρ=0.417，full 仅 0.134），成为最强信号
- RE conditional 中 logprob 几乎无效（ρ=0.011）
- conditional 子集：NER n=477（排除 52 个 greedy_F1=0），RE n=238（排除 159 个）

---
