# code attention visualization

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_attention_visualization_20260519T114246_result.json`
- **Structured JSON:** [`1920f1b8ad637a3f11b4.json`](../../sessions/19/1920f1b8ad637a3f11b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数解析正常。脚本已写入 `/root/turn_residual_gating/src/attention_heatmap.py`。

功能概要：
- 对每组对话 tokenize → `detect_turn_boundaries` 获取 goal token 位置和 assistant turns
- Forward pass with `output_attentions=True`，支持 gates 加载（复用 `load_gates` / `register_gating_hooks`）
- 对每个 assistant turn 的 last token，提取所有层所有 head 对 goal tokens 的平均 attention weight → `[num_turns, num_layers]` 矩阵
- 多组对话取均值，输出 PDF/PNG heatmap + JSON 原始数据
- `--label` 参数用于标注条件名（Base/TG/UG/LoRA-only）
- 四个条件的 2×2 组合图可通过 `plot_2x2_heatmaps()` 函数调用（已内置但需外部脚本组合调用，或后续扩展 CLI）

---
