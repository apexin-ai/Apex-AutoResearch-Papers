# analysis confidence margin rebuttal v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confidence-margin-rebuttal-v2_20260520T033050_result.json`
- **Structured JSON:** [`521afe6fd73178ea81e5.json`](../../sessions/52/521afe6fd73178ea81e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Borderline 假说被反转**——三个架构一致显示 hurt 样本（而非 helped 样本）集中在 decision boundary 附近：

| Arch | Helped margin (mean) | Hurt margin (mean) | Cohen's d | p |
|------|---------------------|--------------------|-----------|----|
| GDN (h12-1) | 2.46 | 1.05 | 1.45 | 5.6e-100 |
| RetNet (h3-1) | 2.48 | 1.29 | 1.39 | 5.0e-77 |
| HGRN2 (h3-1) | 2.50 | 1.48 | 1.22 | 4.9e-63 |

解读：
- **Helped 样本**：pure model 以高 confidence 犯错（margin ~2.5）→ attention 纠正了"自信的错误"
- **Hurt 样本**：pure model 勉强答对（margin ~1.0-1.5）→ attention 扰乱了 borderline-correct 的预测
- 效应量极大（Cohen's d > 1.2），与之前 surface features/perplexity 无信号形成对比
- **Rebuttal 价值**：attention 的 per-example 效应并非完全 opaque——confidence margin 是强预测信号，只是这个信号方向与直觉相反

结果已存入 `artifacts/paper_data/confidence_margin_analysis.json` 并注册。

---
