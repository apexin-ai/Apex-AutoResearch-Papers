# analysis w4 pruned head overlap

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4_pruned_head_overlap_20260515T130430_result.json`
- **Structured JSON:** [`a873f2fb9352ec2bbc3e.json`](../../sessions/a8/a873f2fb9352ec2bbc3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W4 分析完成。

**核心结论**：Importance pruning 具有明确的 structural specificity——它选择性移除 **低 Gini（注意力分散型）** heads。

| 模型 | Δ Gini (pruned − retained) | p-value 范围 | rank-biserial r |
|------|---------------------------|-------------|-----------------|
| DeepSeek | −0.062 ~ −0.071 | 1e-56 ~ 1e-37 | 0.72–0.76 |
| Qwen | −0.051 ~ −0.059 | 1e-41 ~ 1e-28 | 0.62–0.65 |

**交付物**：
- 服务器：`analysis_output/w4_pruned_head_overlap.json`（含全部 per-head Gini + Frobenius 数据）
- 服务器：3 张 PNG（violin plots × 2 模型 + scatter plot）
- 本地报告：`artifacts/w4_pruned_head_overlap/report.md`

**机制解释**：低 Frobenius norm 的 heads 注意力权重小且分散（低 Gini），被 importance pruning 优先移除。剩余 heads 以 high-Gini "尖锐注意力" 为主，这种非均匀的计算基底变化可能是 compound interaction 超加性退化的机制之一。

---
