# knowledge paper patch audit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper-patch-audit_20260514T184018_result.json`
- **Structured JSON:** [`f9d20db789fda6a1d758.json`](../../sessions/f9/f9d20db789fda6a1d758.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**论文当前只覆盖 3 个模型，Yi-1.5 和 Gemma-2 完全缺失。** 需要修改的位置共 ~40 处，分布在 7 个 LaTeX 文件中。

关键分类：

| 优先级 | 类别 | 位置数 | 阻断 |
|--------|------|--------|------|
| P0 | D048 concentration 数值 (0.59-0.66) | 4 处 | D048 结果 |
| P0 | 0.50 threshold diagnostic | 3 处 | D048 结果 |
| P1 | Yi-1.5 新增 (D047 反例) | ~12 处 | 无 |
| P1 | Gemma-2 新增 | ~5 处 | 无 |
| P1 | "三个模型"→"五个模型" | ~15 处 | 无 |
| P2 | Spike vs Spread 新段落 | 1 处 (analysis.tex §5.1) | 无 |
| P2 | 图表更新 (heatmap 3→5 panels) | 1-2 处 | 无 |

**最大风险**：D048 float32 结果若 < 0.50，Qwen 的 concentration 跌破阈值，Claim 3 的 0.50 diagnostic 全线崩塌（当前 5/5 正确分类依赖 Qwen > 0.50）。需要备选方案：降阈值 / 换连续关系 framing / 引入绝对 distortion magnitude 作为辅助指标。

详细清单含每个文件的行号和原文摘录，已写入 `artifacts/paper_patch_audit.md`。

---
