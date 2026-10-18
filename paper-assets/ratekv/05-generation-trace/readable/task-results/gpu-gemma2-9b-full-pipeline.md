# gpu gemma2 9b full pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma2_9b_full_pipeline_20260514T134705_result.json`
- **Structured JSON:** [`7212444b8ccdc6281dca.json`](../../sessions/72/7212444b8ccdc6281dca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务在运行，正在等待模型下载。状态总结：

**已完成：**
- 脚本 `run_gemma2_full_pipeline.py` 已写好并上传到 `/root/ratekv/`
- Gemma-2 架构已验证：42 层, 8 KV heads/layer (GQA 2:1), head_dim=256, softcap=50.0
- Dry-run 通过
- 训练任务已提交（tmux session: `gemma2_9b_full_pipeline`）
- 脚本自动等待模型下载完成后启动 5-phase pipeline

**关键适配：**
- `head_dim=256`（非 `hidden_size//num_heads=224`，这会导致 Llama/Qwen 版的 patch_attention 崩溃）
- 添加了 `attn_logit_softcapping` (tanh soft-cap at 50.0)
- 使用 `query_pre_attn_scalar` 作为 scaling（不是 `1/sqrt(head_dim)`）
- sliding_window 通过 model 自身的 4D attention mask 处理

**架构更正：** 任务描述说 "GQA 8:1, 16 KV heads/layer"，实际是 **GQA 2:1, 8 KV heads/layer**（336 total heads）。

**等待中：** ModelScope 下载 ~36GB，当前速度 ~3 MB/s，预计 3-4 小时完成。下载完成后 pipeline 自动启动，profiling + eval 再需 ~3-5h，总计 ~6-9h。

---
