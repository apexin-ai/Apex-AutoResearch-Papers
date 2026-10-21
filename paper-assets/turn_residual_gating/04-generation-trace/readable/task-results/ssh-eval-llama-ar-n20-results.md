# ssh eval llama ar n20 results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_llama_ar_n20_results_20260522T080809_result.json`
- **Structured JSON:** [`096aad65dccfeed5bb5b.json`](../../sessions/09/096aad65dccfeed5bb5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)，cron 不存在（可能已被删除或未创建）。

## eval_llama_ar_n20 结果汇总 (N=20, T=4)

| Condition | GAR-ours mid (mean±std) | median | GAR-dongre mid (mean±std) | PPL | Spikes(>0.1) |
|-----------|------------------------|--------|--------------------------|-----|-------------|
| **Base** | 0.0101±0.0042 | 0.0093 | 0.0055±0.0008 | 1.29±0.07 | 0/60 |
| **LoRA-only** | 0.0353±0.0399 | 0.0184 | 0.0202±0.0118 | 1.42±0.07 | 5/60 |
| **TG** | 0.0428±0.0523 | 0.0179 | 0.0185±0.0097 | 1.44±0.08 | 4/60 |

### N=20 vs N=5 对比

| | N=5 GAR-ours | N=20 GAR-ours | N=5 PPL | N=20 PPL |
|--|-------------|--------------|---------|---------|
| Base | 0.0082 | 0.0101 | 1.27 | 1.29 |
| TG | 0.0388 | 0.0428 | 1.41 | 1.44 |
| LoRA-only | 0.0617 (T=10) | 0.0353 (T=4) | 1.32 | 1.42 |

### 关键发现

1. **GAR-ours 的 mean 被 spikes 严重拉高**：TG 和 LoRA-only 的 std > mean，median 仅 ~0.018（两者接近）。Mean 上 TG>LoRA-only 的优势主要来自不同的 spike 分布，而非稳定的系统性提升。

2. **GAR-dongre 更稳定**：LoRA-only dongre (0.0202) 略高于 TG dongre (0.0185)，差异不大。

3. **Base 很稳定**：无 spikes，GAR-ours 0.0101 与 N=5 的 0.0082 一致。

4. **PPL 一致**：N=20 和 N=5 的 PPL 差异在合理范围内。

---
