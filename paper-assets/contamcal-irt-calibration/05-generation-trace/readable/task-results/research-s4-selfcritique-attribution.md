# research s4 selfcritique attribution

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_s4_selfcritique_attribution_20260517T045829_result.json`
- **Structured JSON:** [`5c297598466080cfedc9.json`](../../sessions/5c/5c297598466080cfedc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/s4_attribution_report.md`。

核心发现：

1. **`wust2025selfcritique` 是幻觉引用** — "Wüst, Hoffmann, & Pang" 这些作者和声称的论文标题不存在。

2. **arXiv 2510.09259 实际是**：Tao et al. "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models" (ICLR 2026)。方法也叫 "Self-Critique"，也用 entropy 做 contamination detection，但机制完全不同（RL policy collapse 而非 binary YES/NO self-evaluation）。

3. **S4 本质是原创方法**，组合了两个已有 idea：
   - LLM self-evaluation 能力 (Kadavath et al. 2022)
   - Entropy/confidence 作为 memorization 信号（MIA 文献标准做法）

4. **建议处理方式**：删除幻觉引用，改为 cite Tao et al. (ICLR 2026) 作为 concurrent/related work + Kadavath et al. (2022) 作为 self-evaluation 基础，将 S4 的具体实现定位为本文贡献。

---
