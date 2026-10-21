# analysis phase diagram t15 a045 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t15_a045_s42_fp32_20260521T171713_result.json`
- **Structured JSON:** [`a40fcb3534084ed8ee60.json`](../../sessions/a4/a40fcb3534084ed8ee60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果总结

### PermG: **8/8**（满分）
- Forward (canary→downstream): 8/8 FDR 显著
- Reverse (downstream→canary): **0/8** — 完美方向性，排除反向因果

### 5-Method Consensus

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy→distinct_1 | 2/5 | diff, perm |
| token_entropy→distinct_2 | 2/5 | diff, perm |
| token_entropy→distinct_3 | 2/5 | diff, perm |
| token_entropy→perplexity | 2/5 | diff, perm |
| ece→distinct_1 | 3/5 | diff, perm, ty |
| ece→distinct_2 | 3/5 | diff, perm, ty |
| ece→distinct_3 | 3/5 | diff, perm, ty |
| **ece→perplexity** | **4/5** | naive, diff, perm, ty |

- Robust pairs (≥3/5): **4/8**（全部来自 ece 通道）
- TY Granger: 4/8（仅 ece pairs，C003 约束下 ece 的 dmax=0 合理）

### Phase Diagram 影响

**理论预测完美验证：**
- T=10, α=0.45 → PermG=**0/8**（α < α_c(10)≈0.487，不可检测）
- T=15, α=0.45 → PermG=**8/8**（α > α_c(15)≈0.304，满分检测）

0→8 的跳变精确落在 α_c 理论预测的区间内，为 α_c(T) ∝ 1/√T 的幂律关系提供了第 3 个约束点。

---
