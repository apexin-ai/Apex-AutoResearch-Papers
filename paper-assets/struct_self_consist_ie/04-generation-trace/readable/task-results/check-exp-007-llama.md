# check exp 007 llama

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_007_llama_20260514T141019_result.json`
- **Structured JSON:** [`7e774380fa485cdfd89d.json`](../../sessions/7e/7e774380fa485cdfd89d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

## exp_007_llama_inference 状态

**已完成** (EXIT_CODE=0)，551 实例全部处理，耗时 ~17 分钟。

### 关键指标（LLaMA-3.1-8B, N=8, T=1.0）

| | NER | RE |
|---|---|---|
| Greedy F1 | 0.660 | 0.434 |
| Oracle F1 | 0.781 | 0.568 |
| Headroom | +0.121 | +0.135 |
| ρ_sj (full) | **0.363** | 0.299 |
| ρ_fk (full) | 0.327 | 0.305 |
| ρ_logprob (full) | 0.183 | 0.288 |
| ρ_sj (cond) | 0.311 | **0.405** |
| Sample F1=0 % | 11.6% | 41.2% |

**Verdict: FAIL** — RE ρ_sj_full=0.299 < 0.40 阈值；RE 41.2% 样本 F1=0。

与 Qwen3-8B 对比：LLaMA 的 NER ρ_sj 略低（0.363 vs Qwen 0.398），RE 也更弱（0.299 vs 0.277-0.380）。logprob baseline 在 LLaMA 上显著更弱（NER 0.183 vs Qwen 0.237）。

### GPU 状态

4 张 RTX 5090 全部空闲（0% 利用率，2MiB 显存），均可用。

---
