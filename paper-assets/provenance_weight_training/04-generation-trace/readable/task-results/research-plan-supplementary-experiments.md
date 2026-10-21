# research plan supplementary experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_supplementary_experiments_20260520T092755_result.json`
- **Structured JSON:** [`dc144a37a066eba5bc46.json`](../../sessions/dc/dc144a37a066eba5bc46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成分析并写入 memory.md 的"补充实验规划"部分。

**核心结论**：论文证据链整体扎实，最值得补的 3 个实验按优先级：

1. **batch_size=16 adaptive+uniform (cuda:2, ~7h)** — 补全 n_min 自动缩放的第三个验证点，直接支撑 "set once, works across scales"
2. **ρ=0.6 random reweight (cuda:3, ~3.6h)** — 补全高污染下的四层消融层级
3. **D&R q02/q08 或 ModernBERT detector (~9h)** — 用 #1/#2 完成后释放的 GPU 跑

---
