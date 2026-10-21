# diagnose exp 010 mistral

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-010-mistral_20260517T033825_result.json`
- **Structured JSON:** [`634d0b4ab40fd5dbfb8c.json`](../../sessions/63/634d0b4ab40fd5dbfb8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 根因

**vLLM 0.20.2 从 `consolidated.safetensors`（Mistral 原生格式）加载模型时，忽略了 `--max-model-len 8192` 参数，实际使用 `max_model_len=4096`。** 脚本请求 `max_tokens=4096`（输出），加上 prompt（240-360 tokens），总 tokens 超过 4096 限制，导致所有请求返回 400 错误。

### 关键日志摘录

```
# vLLM 实际使用的参数（注意 max_model_len 是 4096，不是脚本指定的 8192）
non-default args: {'max_model_len': 4096, 'gpu_memory_utilization': 0.9}
Using max model len 4096

# 每个请求都失败
This model's maximum context length is 4096 tokens. However, you requested 4096 output 
tokens and your prompt contains 261 input tokens, for a total of 4357 tokens.

# vLLM 最终自行关闭，pipeline 持续重连失败
EngineCore: Shutdown complete
SICA pipeline failed: Connection error.
```

### 模型文件状态

模型在 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/`，文件完整：
- `model-00001-of-00003.safetensors` — 4.7GB
- `model-00002-of-00003.safetensors` — 4.7GB  
- `model-00003-of-00003.safetensors` — 4.3GB
- `consolidated.safetensors` — 14GB

大小略低于 notes 记录的 4.95+5.00+4.55GB，但 `config.json` 正常（`max_position_embeddings: 32768`）。问题不在模型损坏。

### 问题机制

`params.json`（Mistral 原生格式）不含 `max_seq_len` 字段。vLLM 优先从 `consolidated.safetensors` 加载，读取 `params.json` 时无法确定上下文长度，回退到 4096 默认值，覆盖了 CLI 参数。

### GPU 状态

GPU 正常，空闲（0MiB 显存占用），无进程运行。

### 修复方案

**方案 A（推荐）**：删除 `consolidated.safetensors`，强制 vLLM 使用分片格式 + `config.json`（其中 `max_position_embeddings=32768`），此时 `--max-model-len 8192` 应能正确生效。

```bash
rm /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/consolidated.safetensors
```

**方案 B（保守）**：在脚本中将 `--max-tokens` 从 4096 改为 2048，在 4096 上下文限制内也能运行，但输出质量可能下降。

**方案 C**：在 vLLM 启动参数中添加 `--config-format hf`（如果该版本支持），显式指定使用 HuggingFace 格式配置。

---
