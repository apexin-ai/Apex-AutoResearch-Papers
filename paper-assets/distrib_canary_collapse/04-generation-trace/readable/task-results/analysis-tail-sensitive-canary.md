# analysis tail sensitive canary

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tail_sensitive_canary_20260520T082509_result.json`
- **Structured JSON:** [`38b8313ff20a78fa45b1.json`](../../sessions/38/38b8313ff20a78fa45b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册 (art_20260520_fe6257)。

## 结果摘要

### FDR-significant 检出

| Canary | α=0.00 | α=0.10 | α=0.25 | α=0.50 |
|--------|--------|--------|--------|--------|
| effective_rank | 0/4 | 0/4 | **2/4** | 0/4 |
| token_entropy | 0/4 | 0/4 | 1/4 | **1/4** |
| ttr | N/A | 0/4 | 0/4 | 0/4 |
| hapax_ratio | N/A | 0/4 | 0/4 | 0/4 |

### 核心发现

**1. effective_rank 在 α=0.10 有强 suggestive signal**
- effective_rank → distinct_1: raw p=0.0066, p_FDR=0.082（差 0.03 过 FDR）
- 与 null baseline (α=0.00, p=0.070) 相比，分离度 10.7×
- 比 token_entropy 在同一 α 敏感 2.5–3.5×

**2. Blind zone 缩小**
- 保守结论（FDR 通过）：[0, 0.45] → **[0, 0.25)**，effective_rank 在 α=0.25 FDR-sig
- Suggestive 结论：effective_rank 在 α=0.10 raw p=0.007 + 10× null separation → blind zone 可能缩小到 **[0, 0.10)**，待多 seed 确认

**3. TTR / hapax_ratio**
- TTR 被 effective_rank 完全支配，无额外价值
- hapax_ratio 有互补性：对 mauve 敏感（α=0.10: p=0.026），但对 distinct 不敏感

**4. 建议下一步**
- 多 seed 验证 effective_rank 在 α=0.10 的信号
- 将 effective_rank 加入标准 canary 集
- hapax_ratio 作为 supplementary canary 用于 diversity monitoring

---
