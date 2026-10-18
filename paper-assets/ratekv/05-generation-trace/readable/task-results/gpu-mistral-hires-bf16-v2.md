# gpu mistral hires bf16 v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_mistral_hires_bf16_v2_20260514T211111_result.json`
- **Structured JSON:** [`75d8c45871f562042c6d.json`](../../sessions/75/75d8c45871f562042c6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

- **模型下载**：ModelScope 404 失败，改用 HuggingFace 下载成功，模型在 `/root/autodl-tmp/models/Mistral-7B-v0.3`（3 个 safetensors 分片，共 ~13.7GB）
- **config.json**：HuggingFace 官方版本自带 `model_type: "mistral"`，无需修复
- **模型验证**：model_type=mistral, num_layers=32, num_kv_heads=8
- **实验 `mistral_hires_bf16_2bitonly_v4`** 已在 westd-37397 的 cuda:1 上运行
  - Baseline PPL: 5.8702
  - 进度：1/256 heads，ETA ~129 min
  - 日志：`~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log`
  - tmux session：`mistral_hires_bf16_2bitonly_v4`

注意：`submit_training_job` 设置了 `CUDA_VISIBLE_DEVICES=1`，所以脚本内需用 `--gpu cuda:0`（而非 cuda:1）。

---
