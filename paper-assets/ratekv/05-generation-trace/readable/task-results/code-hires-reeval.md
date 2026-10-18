# code hires reeval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hires_reeval_20260514T064153_result.json`
- **Structured JSON:** [`5c218e13dcfb154767b6.json`](../../sessions/5c/5c218e13dcfb154767b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Hires reeval 完成。Hard blocker 已解除。

## 最终结果（当前 eval_ppl.py, MD5: 26d218ac）

| 配置 | PPL | vs Baseline | vs 旧数字 |
|------|-----|-------------|-----------|
| **Baseline bf16** | 9.8106 | — | 旧 8.819 (+0.99) |
| **Uniform 4-bit bf16** | 15.4454 | +5.6348 | 旧 fp16 15.45 (一致) |
| **Hires MCKP bf16** | 10.9131 | +1.1025 | 旧 9.569 (+1.34) |

关键发现：
- **旧 eval 确实低估了 ~1.0 PPL**，baseline 从 8.819→9.8106，hires 从 9.569→10.9131
- Hires MCKP 相对 uniform 4-bit 的降级减少了 **80.4%** (1.10/5.63)
- Uniform 4-bit bf16 与 fp16 的 PPL 几乎无差异（15.4454 vs 15.45）
- 结果文件已保存到服务器 `/root/ratekv/hires_reeval_results.json`

---
