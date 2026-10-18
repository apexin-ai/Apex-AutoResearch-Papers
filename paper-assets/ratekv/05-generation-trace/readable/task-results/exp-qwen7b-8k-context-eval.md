# exp qwen7b 8k context eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen7b_8k_context_eval_20260515T130830_result.json`
- **Structured JSON:** [`e9ef7a1202a59b799ead.json`](../../sessions/e9/e9ef7a1202a59b799ead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| Method | 8K PPL | 2K PPL | 变化 |
|--------|--------|--------|------|
| Baseline (bf16) | **6.97** | 9.81 | 更长上下文 → 更低 PPL（正常） |
| Constrained MCKP (k=8) | **8.59** | 10.89 | MCKP 在 8K 下依然稳健 |
| Uniform 4-bit | **77.75** | 15.45 | 灾难性退化（5× → 11× baseline） |

**关键发现**：
- MCKP improvement over uniform: **97.7%** (8K) vs 80.8% (2K) — concentration-dependent benefit 在长上下文下**大幅放大**
- Uniform 4-bit 在 8K 下完全崩溃（PPL 77.75），因为敏感 head 的量化误差在更长序列上累积
- MCKP 通过保护敏感 head（L0 用 8-bit），PPL 仅从 6.97 升到 8.59（+23%），而 uniform 升了 1014%

结果已保存到 `/root/ratekv/artifacts/qwen7b_8k_spotcheck_results.json`，registry 状态已更新为 DONE/success。

---
