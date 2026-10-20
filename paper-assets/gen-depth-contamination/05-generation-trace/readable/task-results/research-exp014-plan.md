# research exp014 plan

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp014_plan_20260525T063111_result.json`
- **Structured JSON:** [`d2b96a697697b00d6f19.json`](../../sessions/d2/d2b96a697697b00d6f19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已保存到两个位置：

1. **`artifacts/exp014_plan.md`** — 完整实验方案（Worker 可直接执行）
2. **`memory.md`** — 摘要段落

方案要点：

**数据**：FineWeb CC-MAIN-2025-26 streaming 采 50K English docs（避免自己处理 raw CC 的 HTML 清洗/语言检测/去重）

**Depth 预测**：复用现有 15D feature pipeline + Qwen-1.5B scorer → OBD-LightGBM（在 exp-017 C4 continuation 数据上全量训练后推断）

**AlignScore 结论**：不适用。它需要 source-claim pair 做 factual consistency 评分，不是通用文本质量指标。

**独立质量指标（9 个）**：
- GPU 指标：GPT-2 Large perplexity、MAUVE（per depth bin）
- CPU 指标：MTLD、vocd-D、TTR、hapax ratio、3/4-gram repetition rate、Zipf coefficient
- 其中 MTLD / vocd-D / GPT-2 PPL / rep rate / MAUVE / Zipf 与 OBD 的 15D 特征完全独立

**资源**：单卡 ~6h，~4GB 磁盘，3 个额外 pip 包

**关键注意事项**：
- CC 文本必须截断到 256 tokens（与训练数据对齐）
- self-BLEU 计算方式与训练时不同（全 pool vs 同 depth），如 OBD 泛化异常可降为 14D
- TTR / hapax_ratio 与 OBD 特征有 overlap，分析时需标注

---
