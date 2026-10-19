# code extract activations large

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract_activations_large_20260520T211034_result.json`
- **Structured JSON:** [`afb65eaad96439ecb2e8.json`](../../sessions/af/afb65eaad96439ecb2e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建，语法正确。关键改动：

1. **Hook 替代 output_hidden_states** — 只对目标层注册 `register_forward_hook`，hook 中立即 `.detach().cpu().float()`，推理时不传 `output_hidden_states=True`。hooks 在 `finally` 块中清理。
2. **量化** — `--quantization int4/int8`，通过 `BitsAndBytesConfig` 配置 NF4 双重量化或 LLM.int8。
3. **架构自适应** — `get_layer_modules()` 依次尝试 `model.model.layers` / `model.transformer.h` / `model.gpt_neox.layers`。
4. **增量保存与断点续传** — `--save_interval N` 每 N 条保存一次；启动时自动检测已有 `.pt` 文件并从断点恢复。
5. **输出格式完全兼容** — 同样的 `layer{i}_{lang}.pt`，同样的 `{"activations", "labels"}` 结构。

---
