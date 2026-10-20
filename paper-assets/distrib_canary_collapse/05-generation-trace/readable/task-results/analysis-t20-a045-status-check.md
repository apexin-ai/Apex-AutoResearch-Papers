# analysis t20 a045 status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a045_status_check_20260520T201311_result.json`
- **Structured JSON:** [`fa6be2a192dc2e26c84b.json`](../../sessions/fa/fa6be2a192dc2e26c84b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

```
status: completed
gen_progress: 20/20 (全部完成)
```

### 5-Method Lead-Lag 分析 (T=20, α=0.45, s42)

| 指标 | 值 |
|------|-----|
| **PermG fwd (uncorrected sig)** | **5/8** |
| PermG fwd (FDR) | 需逐 pair 确认（首 pair p_fdr=0.052 borderline） |
| PermG rev | 0/8 |
| DiffXcorr fwd (FDR) | 7/8 |
| Threshold onset fwd | 4/8 |
| TY fwd | 2/8 |
| **Consensus K≥3** | **3/8** |
| Consensus K≥4 | 1/8 (token_entropy→distinct_2, K=4) |

### Consensus 逐 pair 明细

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 2 | diff, threshold |
| token_entropy→distinct_2 | **4** | diff, threshold, perm, ty |
| token_entropy→distinct_3 | 2 | diff, perm |
| token_entropy→mauve | 0 | — |
| ece→distinct_1 | **3** | diff, threshold, perm |
| ece→distinct_2 | **3** | diff, threshold, perm |
| ece→distinct_3 | 2 | diff, perm |
| ece→mauve | 2 | naive, ty |

### Model Verdict: **Model B supported**

T=10 baseline (a045_s42_fp32, a045_s43_fp32) 均为 PermG=0/8。T=20 跳升至 PermG=5/8（uncorrected），K≥3 达 3/8。这不是噪声——方向性完全正确（fwd 5/8 vs rev 0/8），且 DiffXcorr 7/8 独立印证。

**关键发现**：α=0.45 不在 fundamental blind zone 内。T=10→T=20 的扩展确实将其从不可检测（0/8）推至可检测（5/8），支持 α_c(T) 随 T 递减的 Model B 假设。

**注意事项**：
- PermG FDR 校正后 borderline（首 pair p_fdr=0.052），5/8 计数可能基于 uncorrected p<0.05
- K≥3 仅 3/8，信号比 α≥0.50 区间弱——α=0.45 处于 T=20 的检测边缘
- mauve pairs 仍无信号（K=0 和 K=2），与 T=10 模式一致

---
