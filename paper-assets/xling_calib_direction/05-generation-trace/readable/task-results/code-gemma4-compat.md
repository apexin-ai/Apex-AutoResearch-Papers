# code gemma4 compat

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma4-compat_20260521T090622_result.json`
- **Structured JSON:** [`97908a9a6a29eade6d8c.json`](../../sessions/97/97908a9a6a29eade6d8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改已正确就位。总结变更：

| 位置 | 修改 |
|------|------|
| L48 import | 添加 `AutoConfig` |
| L95 parse_args | 新增 `--model_type {auto, causal_lm, conditional_generation}` |
| L168 | 新增 `_is_conditional_generation()` — 从 config.architectures 检测 |
| L174 load_model | 接受 `model_type` 参数，conditional_generation 时用 `AutoModelForVision2Seq` 加载 |
| L202 get_layer_modules | 新增 `model.model.language_model.layers` 路径（Gemma4 text decoder） |
| L225 get_final_norm | 新增 `model.model.language_model.norm` 路径 |
| L317-321 main() | `load_model` 传入 `model_type`；从 `text_config`（若存在）读 `num_hidden_layers` / `hidden_size` |

对现有 CausalLM 模型完全向后兼容——`model_type=auto` 时，无 `ConditionalGeneration` 架构的模型走原路径，`getattr(config, 'text_config', config)` 回退到 config 自身。

---
