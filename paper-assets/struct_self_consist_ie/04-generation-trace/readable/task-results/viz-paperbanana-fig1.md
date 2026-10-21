# viz paperbanana fig1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_paperbanana_fig1_20260523T133615_result.json`
- **Structured JSON:** [`34a77211f1b32d84f4e4.json`](../../sessions/34/34a77211f1b32d84f4e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**：
- PaperBanana 因 Gemini 模型 API 不兼容（`gemini-2.0-flash` 已弃用，`gemini-2.5-flash` 图像生成失败）无法使用，改用手写 matplotlib
- 手写 1 轮调试 + 1 轮微调，共 2 次迭代
- 最终图：16×5.6 英寸，300 DPI，三面板结构
  - Panel 1（蓝）：Input x → N samples → S，High/Low S 相关性，AUROC/ρ 指标，✓ Effective Quality Estimation
  - Panel 2（橙）：相同分数 S=0.73 的 bracket 标注，instance-level signal 解释，✗ Selection Fails
  - Panel 3（绿）：PER/LOC/ORG 实体网格 + 频率行，θ=2/N 阈值线，+1.4 pp
  - 顶部连接：红色 "Correlation–Selection Gap" banner + 绿色 "Resolution" banner
- `fig_overview.png` (388KB) 和 `fig_overview.pdf` (57KB) 已覆盖原文件
- LaTeX 编译通过

---
