# analysis gar definition robustness v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gar_definition_robustness_v2_20260524T061033_result.json`
- **Structured JSON:** [`6008292196596419c4b8.json`](../../sessions/60/6008292196596419c4b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：情况 B — raw attention 未保存，需要 GPU 重新推理

### 现有数据结构

所有 JSON 结果（`*_ar_n50.json`、`*_gar.json`）只保存了聚合后的 GAR 值：
- `gar_curves`: per-conversation per-turn 的标量 GAR
- `avg_gar_per_turn`, `mid_turns_avg_gar`, `per_conv_mid_gar`
- **没有** per-token attention weights、`goal_positions`、`query_positions`

### 现有 GAR 定义（`turn_utils.py:142-163`）

| 参数 | `ours` 变体 | `dongre` 变体 |
|------|-------------|---------------|
| **goal** | system prompt + first user query 的全部 token | system prompt only |
| **query** | 每个 assistant turn 的 **last token** | 每个 assistant turn 的 **all tokens** |

### 替代定义鲁棒性分析需要什么

4 种 GAR 定义 = 不同的 `(goal_positions, query_positions)` 组合。attention weights 在 `GARMeasurer` 中通过 hook 在 forward pass 中捕获后，可以对同一 attention matrix 调用多次 `compute_gar()` 使用不同 positions。

**好消息：不需要 4x GPU 时间。** 每个 conversation 只需 1 次 forward pass，然后用 4 组不同 positions 重算 GAR。

### 所需修改

1. **`turn_utils.py`**: `detect_turn_boundaries` 增加返回 `assistant_first_token_positions` 和 `system_only_goal_positions`
2. **写一个新 eval 脚本**（或修改 `eval_phase2_gar.py`）：每次 forward pass 后计算 4 种 GAR

### 资源估算

| 项目 | 估算 |
|------|------|
| 模型 | Base / TG(s42) / SS(s42) — 3 个 |
| conversations/模型 | 50（已有 `eval_200.json` 数据集） |
| forward pass | ~2 sec/conv × 50 = ~100 sec/model |
| 模型加载 | ~1-2 min/model |
| **总 GPU 时间** | **~10-15 分钟** |
| GPU 需求 | 1× GPU（Qwen2.5-7B + eager attention） |

需要我写脚本提交到服务器运行吗？

---
