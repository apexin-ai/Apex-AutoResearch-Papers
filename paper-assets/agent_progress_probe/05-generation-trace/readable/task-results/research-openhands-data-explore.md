# research openhands data explore

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openhands_data_explore_20260514T081819_result.json`
- **Structured JSON:** [`e39ffce9bf3ea24a1d6f.json`](../../sessions/e3/e39ffce9bf3ea24a1d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**数据格式差异**：OpenHands 使用 OpenAI function calling API 格式（`assistant` + `tool` role, 结构化 `tool_calls`），SWE-agent 使用扁平文本格式（`ai` + `user` role, 命令嵌入三反引号）。这是核心差异。

**Pipeline 复用性**：

| 组件 | 评级 | 工作量 |
|------|------|--------|
| `window_extractor.py` | 可直接复用 | ~0 行 |
| `generate_embeddings.py` | 可直接复用 | ~5 行 |
| `probe_model.py` / `train_probe.py` | 完全复用 | 0 行 |
| `data_loader.py` | 需适配 | ~200 行（写 adapter） |
| `labeling_functions.py` | 需适配 | ~50 行 |
| **总计** | | **~270 行, 1-2 天** |

**推荐方案**：写一个 `openhands_adapter.py` 将 OpenHands 格式转为现有 `Trajectory`/`Step` 接口，下游 pipeline 无需修改。

**关键风险**：OpenHands 解决率 47.9%（远高于 SWE-agent 16.7%），label 分布会显著不同，probe 可能需要重新标定。

详细报告见 `artifacts/openhands_format_analysis.md`。

---
