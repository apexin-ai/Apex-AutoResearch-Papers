# analysis r17 lora rank8 lp compression

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r17_lora_rank8_lp_compression_20260517T073317_result.json`
- **Structured JSON:** [`7169924631067c866776.json`](../../sessions/71/7169924631067c866776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果保存在 `output/r17_analyses/lp_compression_comparison.json`。

## 结果汇总

### Cumulative Logprob

| Dataset | Degen% | Med LP Range (nats) | Tied Frac | ρ(LP,F1) mean | ρ(LP,F1) median | n |
|---------|--------|--------------------:|----------:|--------------:|----------------:|--:|
| SciERC rank=8 | 3.3% | 10.26 | 0.2% | 0.115 | 0.182 | 506 |
| SciERC full rank | 11.6% | 6.48 | 0.5% | 0.091 | 0.170 | 448 |
| Few-NERD | 19.0% | 3.61 | 10.8% | 0.408 | 0.615 | 3885 |

### Mean Logprob (length-normalized)

| Dataset | Degen% | Med LP Range | Tied Frac | ρ(LP,F1) mean | ρ(LP,F1) median | n |
|---------|--------|-------------:|----------:|--------------:|----------------:|--:|
| SciERC rank=8 | 3.3% | 0.0569 | 0.9% | 0.240 | 0.316 | 506 |
| SciERC full rank | 11.6% | 0.0413 | 1.1% | 0.182 | 0.285 | 448 |
| Few-NERD | 19.0% | 0.0580 | 17.0% | 0.499 | 0.661 | 3885 |

### 关键发现

**与预期相反：rank=8 LP 并未压缩，反而更分散。**

1. **LP range**: rank=8 的 median LP range 比 full rank 更大（cumulative: 10.26 vs 6.48; mean: 0.057 vs 0.041），说明 rank=8 产生的 logprob 变异更大而非更小
2. **Within-instance ρ(LP, F1)**: rank=8 略高于 full rank（mean 0.24 vs 0.18），LP 对质量的区分力反而稍好
3. **Degeneracy**: rank=8 显著低于 full rank（3.3% vs 11.6%），说明 rank=8 模型输出更多样
4. **真正的问题在 SciERC vs Few-NERD**：两个 SciERC 配置的 ρ 都很弱（~0.1-0.3），而 Few-NERD 达到 0.5-0.66，表明 LP 区分力差是 SciERC 任务特性，而非 rank 造成的

**结论**：rank=8 的 LP selection failure 不是因为"LP 压缩"导致无法区分样本，而是与 full rank 相同的根源问题——SciERC 上 LP 本身就不 track entity-level F1（可能因为 SciERC 的实体提取对 token-level confidence 不敏感）。

---
