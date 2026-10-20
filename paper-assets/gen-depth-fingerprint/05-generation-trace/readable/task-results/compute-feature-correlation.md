# compute feature correlation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_feature-correlation_20260517T211035_result.json`
- **Structured JSON:** [`b61368e65189360df5cb.json`](../../sessions/b6/b61368e65189360df5cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果摘要** (N=27,529, 6 generators):
- **高相关簇**: TTR 与 Hapax (r=0.97)，两者与 $\bar{H}$ 也高度相关 (0.86, 0.81)
- **独立特征**: $H_{\max}$, $\tau$, $H_{\min}$ 与其他特征的 |r| 均 < 0.27

**产出**:
- `appendix_feature_correlation.tex` 已创建，含 `\section` 标题、table、说明文字
- `main.tex` 已在 Feature Ablation 之后插入 `\input{appendix_feature_correlation}`
- artifact 已注册 (`art_20260517_9346e5`)

---
