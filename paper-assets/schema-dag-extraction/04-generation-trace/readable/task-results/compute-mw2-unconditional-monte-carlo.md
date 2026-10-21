# compute mw2 unconditional monte carlo

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_mw2_unconditional_monte_carlo_20260516T173235_result.json`
- **Structured JSON:** [`01a3c2c66b80d7be1220.json`](../../sessions/01/01a3c2c66b80d7be1220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无错误。

---

**MW2 产出汇总：**

| 项目 | 值 |
|------|-----|
| Unconditional pair r² input | 0.013 |
| Unconditional simulated batch R² (analytical) | 0.042 |
| Unconditional simulated batch R² (MC median) | 0.044 |
| Unconditional simulated batch R² (MC mean) | 0.053 |
| 95% CI | [0.001, 0.151] |
| Simulation 参数 | n_batches=100, n_pairs_per_batch=28, n_iter=10,000, EF=3.35 |
| 与 observed R²=0.218 的比值 | ~5× gap |
| 对比：conditional simulated R² | 0.219 (matches observed) |

**Appendix M 更新**：将 "drops to ≈0.01" 和 "~20× gap" 修正为基于正确 MC simulation（保持 EF=3.35 batch 结构）的 "0.044 [95% CI: 0.001–0.151]" 和 "~5× gap"。之前 worker 错误地用了 EF=1（无相关结构），实际上 batch 内 SCS 相关性是 batch 组成的固有属性，应当保持不变。

编译通过，19 页 PDF 输出正常。

---
