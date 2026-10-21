# research qualitative case study

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qualitative_case_study_20260521T024752_result.json`
- **Structured JSON:** [`cde239c6ddd07cc14b75.json`](../../sessions/cd/cde239c6ddd07cc14b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

## 结果汇报

### 选择的文档和理由

| Case | Doc ID | 来源 | 选择理由 |
|------|--------|------|----------|
| **A** | 2468 | C4 (Qwen-1.5B) | **典型 K\*=2**：depth 0 是碎片化的度假公寓列表标题，depth 1 转为连贯的房产描述散文，depth 2-3 生成几乎相同的房产细节。Mean surprisal 从 3.43 骤降至 ~2.10 后不再变化。 |
| **B** | 3000 | C4 (Qwen-1.5B) | **事实退化**：depth 0 是关于历史石碑（Slaughter Stone）的真实描述，depth 1 完全虚构了 Glastonbury 传说，depth 2-3 继续编造。TTR 从 0.745 降至 ~0.56-0.67。 |
| **C** | 1079 | arXiv (Qwen-1.5B) | **域特异性坍缩**：depth 0 是多重图异质性的 ML 摘要，depth 1 仍保持主题，depth 2 退化为 `\section*{Acknowledgements}` 等 LaTeX 模板，depth 3 全是虚构致谢。 |

### 关键特征值对比

| 特征 | Case A (d0→d1→d2→d3) | Case B | Case C |
|------|----------------------|--------|--------|
| TTR | 0.683→0.659→0.628→0.604 | 0.745→0.565→0.616→0.667 | 0.697→0.685→0.812→0.663 |
| Mean Surp. | **3.434**→2.098→2.091→2.155 | **3.263**→2.063→2.152→1.986 | 1.920→1.970→2.265→2.024 |
| Freq. Ent. | 5.767→6.599→6.631→6.682 | 6.049→6.303→6.348→5.680 | 6.903→6.701→5.590→5.824 |

### 产出文件

`.tex` 文件已写入 `artifacts/case_study_qualitative.tex` 并注册（`art_20260521_fe66c0`）。格式为 `\subsection` + 3 个 `\paragraph`，每个包含特征表 + 4 段文本摘录，适合直接 `\input` 到 appendix。

---
