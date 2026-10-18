# analyze llama hires mckp results

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama_hires_mckp_results_20260514T215502_result.json`
- **Structured JSON:** [`ce6c5d7a9997b1da45c6.json`](../../sessions/ce/ce6c5d7a9997b1da45c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/negative.

**摘要：**

| Method | WikiText-2 PPL |
|---|---|
| BF16 baseline | 8.0922 |
| Hires MCKP (k=2, max_2bit=2) | **8.5042** |
| Uniform 4-bit | 8.4701 |
| Std MCKP (reference) | 8.4498 |

**Hires concentration=0.5749**（与预期 0.57 一致），bit 分布 253×4 + 2×2 + 1×8，2-bit heads = `(26,0)`, `(31,7)`。

**关键结论：**
1. **Hires MCKP vs Uniform = -0.0341（-9%，FAIL）**：与 standard profiling 的 +0.2% 相反，hires 选出的 2-bit heads 比 standard 更差。负面发现。
2. **Table 1 = 8.45 无需更新**：hires MCKP PPL 8.5042 与 8.4498 差 0.054，< 0.065 seed variance（但接近阈值 84%）。建议在论文里加脚注说明 hires profiling 在 Llama 上反而劣化 MCKP allocation。
3. **Uniform 4-bit 一致性**：8.4701 vs std 8.469（diff 0.001）→ eval pipeline 稳定。

---
