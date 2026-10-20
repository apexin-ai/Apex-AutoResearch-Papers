# analysis 4b cls cwm paired bootstrap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-cls-cwm-paired-bootstrap_20260512T170544_result.json`
- **Structured JSON:** [`bd5d18eda8c2688b1592.json`](../../sessions/bd/bd5d18eda8c2688b1592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出文件已生成。修正后的结果：

### 4B CLS vs CWM（5 seeds）
| 指标 | 值 |
|------|-----|
| Paired diffs | 0.32, 2.32, 0.90, 2.33, 0.37 |
| Mean gap | **1.25pp** |
| Std | 1.01 |
| Paired t | **t=2.77, p=0.0253**（单侧）|
| Bootstrap 95% CI | **[0.46, 2.04]pp** |
| Cohen's d | 1.24（large effect）|
| TOST p（±2pp） | 0.0855（不等价，差异是真实的）|

### 8B CLS vs CWM（3 seeds）
| 指标 | 值 |
|------|-----|
| Mean gap | **2.26pp** |
| Paired t | **t=8.60, p=0.0066**（单侧）|
| Bootstrap 95% CI | **[1.80, 2.71]pp** |
| Cohen's d | 4.97 |

### Scaling 趋势
- Gap 从 4B 的 1.25pp 增长到 8B 的 2.26pp（+1.01pp）
- P(8B gap > 4B gap) = **0.988**

4B 的 t=2.77, p=0.0253 与 Reviewer 独立计算（t=2.77, p≈0.025）完全一致。两个 scale 下 CLS 优势均显著，且随模型规模放大。

**注意**：JSON 中 narrative 里 8B gap 写的 2.42pp 与实际计算值 2.26pp 不一致——这是任务模板中的原始文本，实际数据以计算结果 2.26pp 为准。如需修正 narrative 文本请告知。

---
