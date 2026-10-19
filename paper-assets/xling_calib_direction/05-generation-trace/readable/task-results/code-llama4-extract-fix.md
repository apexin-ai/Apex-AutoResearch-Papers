# code llama4 extract fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama4_extract_fix_20260521T135142_result.json`
- **Structured JSON:** [`294b5728d7994a8d3a9e.json`](../../sessions/29/294b5728d7994a8d3a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed — `compressed_tensors` and `get_balanced_memory` are completely gone from `extract_activations.py`.

## 结果

### 1. 修改摘要

**extract_activations_large.py** (7 处修改, 433→~470 行):
- `import AutoConfig` 加入
- `--model_type` 参数 (auto / causal_lm / image_text_to_text)
- `load_model()`: 自动检测 `ConditionalGeneration` 架构 → 使用 `AutoModelForImageTextToText`
- `get_layer_modules()`: 加入 `model.language_model.model.layers` 路径
- `get_final_norm()`: 加入 `model.language_model.model.norm` 路径
- `main()`: 传 model_type, `num_hidden_layers` 回退到 `text_config`

**extract_activations.py** (2 处修改, 547→475 行):
- 删除 `_is_compressed_tensors()` 函数
- `load_model()`: 删除 CPU decompression / `get_balanced_memory` / `dispatch_model`，直接用 `device_map=auto`

### 2. CPU 验证
- 语法检查: 两个文件都 SYNTAX OK
- `--help`: 两个文件参数解析正常，`--model_type` 显示在 extract_activations_large.py 的帮助中

### 3. run_plan002.sh
已创建，使用 `extract_activations_large.py` + `--dtype float16` + 13 层 + 20 语言

### 4. 剩余风险（需 GPU 验证）
- **`model.device` 兼容性**: `AutoModelForImageTextToText` + `device_map="auto"` 时 `.to(model.device)` 是否正确路由 inputs — 理论上没问题（embedding 在第一个 GPU），但只有 GPU 加载后才能确认
- **`out.logits` 结构**: Llama4 的 MoE 输出是否标准 `logits` 属性
- **compressed_tensors 自动解压**: transformers 是否在 `device_map="auto"` 下透明处理 W4A16 解压，不触发 OOM
- **48 层模型的显存占用**: 4 卡 × 80G 是否足够 W4A16 + FP16 activations

---
