# analysis d102 rerun gpt2m s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_rerun_gpt2m_s43_20260521T180952_result.json`
- **Structured JSON:** [`20c92401cadd135107fc.json`](../../sessions/20/20c92401cadd135107fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果总结：

## d102 重分析对比

| 指标 | 旧值 (perplexity + 3x_sigma_drift) | 新值 (mauve + true_3sigma_d105) |
|------|-----|-----|
| **PermG fwd** | **6/8** | **6/8** (不变) |
| PermG rev | 6/8 | 4/8 |
| TY forward | 5/8 | 2/8 |
| threshold_onset | 8/8 | 1/8 |
| diff_xcorr fwd | 2/8 | 7/8 |
| naive_xcorr fwd | 0/8 | 6/8 |
| K≥3 | — | 6/8 |
| K≥4 | 0/8 | 2/8 |

**核心结论：PermG forward 6/8 不变**，GPT-2m 的 canary 检测力在 d102 标准下稳健。

差异原因：
1. **threshold_onset 8/8→1/8**：`true_3sigma_d105`（BH-FDR 校正）远比 `3x_sigma_drift`（简单幅值检查）严格
2. **naive/diff xcorr 大幅上升**：旧脚本可能未应用 D111 方向滤波器，导致显著对被错误分配；d102 脚本在 8-pair（mauve 替换 perplexity）配置下 xcorr 对检出更多
3. **PermG rev 6/8→4/8**：mauve 两对 reverse 不显著，降低了反向总数

---
