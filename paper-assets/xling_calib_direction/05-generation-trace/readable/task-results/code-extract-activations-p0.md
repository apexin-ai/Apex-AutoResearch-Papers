# code extract activations p0

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract-activations-p0_20260521T070139_result.json`
- **Structured JSON:** [`86fbde81d5e1eebcd8e6.json`](../../sessions/86/86fbde81d5e1eebcd8e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法通过，`--help` 正常输出。

脚本已写入 `/root/xling_calib_direction/code/extract_activations.py`，核心设计：

- **Hook-based 提取**：`register_forward_hook` 只在目标层捕获 last-token hidden state，避免 94 层全量 OOM
- **层采样**：`--layer_interval 4`（默认）或 `--layers` 手动指定，覆盖 interval
- **Batch 推理**：left-padding tokenizer + batched forward，`--batch_size` 控制
- **分层 split**：按 correct/incorrect 做 stratified 70/30 split（`train_test_split(stratify=labels)`），极端分布时自动回退
- **输出格式**：`activations/{model_name}/L{idx}/{lang}_{train,eval}.npy` + `{lang}_{train,eval}_labels.npy` + `metadata.json`
- **内存管理**：逐语言处理，处理完释放 + `torch.cuda.empty_cache()`
- **模型加载**：GPTQ/AWQ 由 HuggingFace `from_pretrained` 自动检测，无需额外 flag
- 复用 MVP 的数据加载（`load_mmlu`）、prompt 构建（`build_prompt`）、架构适配（`get_layer_modules`）、final norm 逻辑

---
