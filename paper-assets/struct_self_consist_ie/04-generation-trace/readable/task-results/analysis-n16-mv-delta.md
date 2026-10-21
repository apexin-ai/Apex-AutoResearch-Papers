# analysis n16 mv delta

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n16_mv_delta_20260523T002046_result.json`
- **Structured JSON:** [`7ed05ac8a2a35520e7db.json`](../../sessions/7e/7ed05ac8a2a35520e7db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了：

```
=== FewNERD Pretrained N=16 (seed=42) ===
greedy_f1: 0.5109
mv_f1:     0.5538
mv_delta:  +4.28pp
lp_f1:     0.4995
lp_delta:  -1.14pp
oracle_f1: 0.6433
degeneracy_rate: 7.5%  (2831/37648)
sj_rho: 0.453
lp_rho: 0.192

=== N=8 vs N=16 对比 ===
| Metric          |    N=8 |   N=16 | Trend    |
|-----------------|--------|--------|----------|
| greedy_f1       | 0.5116 | 0.5109 | ~same    |
| mv_f1           | 0.5552 | 0.5538 | ~same    |
| mv_delta_pp     | +4.36  | +4.28  | -0.07    |
| lp_f1           | 0.5016 | 0.4995 | ~same    |
| degeneracy_%    | 12.2%  |  7.5%  | -4.68pp  |
| oracle_f1       | 0.6169 | 0.6433 | +2.6pp   |
| oracle_headroom | 0.1053 | 0.1324 | +2.7pp   |
| sj_rho          | 0.436  | 0.453  | +1.7pp   |
| lp_rho          | 0.188  | 0.192  | +0.4pp   |
```

关键发现：
- **MV F1 = 0.5538**，比 greedy +4.28pp，与 N=8 的 +4.36pp 基本持平
- **LP selection 无效**：lp_f1 < greedy_f1（-1.14pp），选最高 logprob 的样本反而更差
- **degeneracy 显著下降**：N=8→N=16 从 12.2% 降到 7.5%（更多采样 → 更多多样性）
- **oracle headroom 增大**：N=16 的 oracle_f1 比 N=8 高 2.6pp，但 MV 没能利用这些额外多样性——MV F1 几乎没变
- 结论：N=8→N=16 加倍采样后，diversity 提升了（degeneracy↓, oracle↑），但 MV construction 没有受益，说明 MV 的天花板不在采样数量上

---
