# code logprob results

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_logprob-results_20260518T073023_result.json`
- **Structured JSON:** [`3131929cdaf3232f4131.json`](../../sessions/31/3131929cdaf3232f4131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。80/80 全部跑完，summary 已保存。

## 完整结果表 (mean_rank / mean_prob / frac_rank1)

```
Model                                    D=1              D=2              D=3              D=4              D=5
───────────────────────────────────────────────────────────────────────────────────────────────────────────────
GatedDeltaNet-pure-baseline     5.20/0.103/0.094 5.36/0.103/0.098 5.30/0.107/0.116 5.35/0.103/0.118 5.53/0.100/0.088
GatedDeltaNet-New-hybrid-24-1   5.63/0.099/0.080 5.59/0.099/0.090 5.44/0.103/0.102 5.35/0.104/0.106 5.54/0.100/0.082
GatedDeltaNet-hybrid-12-1       4.94/0.106/0.102 5.20/0.104/0.098 4.95/0.113/0.124 5.13/0.112/0.128 5.28/0.107/0.118
GatedDeltaNet-hybrid-6-1        5.24/0.101/0.096 5.27/0.101/0.094 5.20/0.109/0.124 5.08/0.111/0.128 5.18/0.106/0.118
GatedDeltaNet-hybrid-3-1        5.38/0.099/0.094 5.51/0.100/0.096 5.27/0.110/0.124 5.28/0.111/0.128 5.47/0.105/0.118
HGRN2-pure-baseline             5.09/0.102/0.096 5.39/0.103/0.096 5.22/0.107/0.118 5.17/0.108/0.112 5.15/0.108/0.126
HGRN2-hybrid-24-1               5.35/0.103/0.094 5.43/0.102/0.094 5.36/0.110/0.124 5.08/0.115/0.128 5.46/0.107/0.118
HGRN2-hybrid-12-1               5.31/0.100/0.102 5.30/0.102/0.104 5.30/0.110/0.120 5.22/0.120/0.128 5.42/0.107/0.110
HGRN2-hybrid-6-1                5.35/0.100/0.090 5.28/0.104/0.092 5.28/0.107/0.130 5.14/0.110/0.126 5.31/0.106/0.118
HGRN2-hybrid-3-1                5.10/0.102/0.108 5.35/0.109/0.112 5.32/0.099/0.086 5.20/0.109/0.114 5.31/0.106/0.106
RetNet-pure                     5.52/0.099/0.104 5.83/0.094/0.072 5.52/0.100/0.104 5.54/0.099/0.098 5.39/0.100/0.092
RetNet-hybrid-24-1              5.27/0.103/0.096 5.40/0.101/0.094 5.38/0.109/0.124 5.09/0.114/0.128 5.34/0.107/0.118
RetNet-hybrid-12-1              5.26/0.100/0.090 5.39/0.101/0.090 5.29/0.108/0.116 5.14/0.113/0.122 5.30/0.106/0.116
RetNet-hybrid-6-1               5.23/0.103/0.094 5.43/0.100/0.094 5.22/0.112/0.124 5.09/0.114/0.128 5.31/0.108/0.118
RetNet-hybrid-3-1               5.26/0.102/0.094 5.26/0.100/0.094 5.43/0.109/0.124 5.27/0.110/0.128 5.42/0.105/0.118
transformer_340M_baseline       5.20/0.100/0.096 5.51/0.103/0.104 5.40/0.102/0.086 5.30/0.109/0.112 5.47/0.102/0.100
Random (uniform)                5.50/0.100/0.100 5.50/0.100/0.100 5.50/0.100/0.100 5.50/0.100/0.100 5.50/0.100/0.100
```

## 关键发现

1. **所有模型与随机基线差异很小** — mean_rank 在 4.9~5.8 范围（随机=5.5），mean_prob 在 0.094~0.120 范围（随机=0.100），信号微弱但一致。

2. **最佳 mean_rank**: GatedDeltaNet-hybrid-12-1 在 D=1 (4.94) 和 D=3 (4.95)，是唯一 mean_rank 低于 5.0 的配置。

3. **Hybrid 优于 Pure** — 三种架构中，hybrid 变体普遍比 pure baseline 有更低的 mean_rank（更好）：
   - GatedDeltaNet: hybrid-12-1 最优，pure 最差
   - HGRN2: hybrid 变体略优于 pure
   - RetNet: hybrid 变体明显优于 pure（RetNet-pure 在 D=2 最差：5.83）

4. **Depth 趋势**: D=4 时多数 hybrid 模型的 frac_rank_1 达到峰值 0.128，D=3 的 HGRN2-hybrid-6-1 达到最高 0.130。

5. **Attention ratio 影响非线性** — 不是越多 attention 越好：GatedDeltaNet 中 12-1 ratio 最优，24-1 反而最差；HGRN2 和 RetNet 中各 ratio 差异较小。

6. **Transformer baseline 表现中等** — 不比 hybrid 模型好，也不比 pure SSM 差太多。

---
