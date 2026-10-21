# infra codellama model check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_codellama-model-check_20260516T111311_result.json`
- **Structured JSON:** [`7f8586bd868b3f424019.json`](../../sessions/7f/7f8586bd868b3f424019.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CodeLlama-13B 模型文件完整（3个 safetensors shard 齐全）。

## 汇报

### 模型状态
| 模型 | 状态 | 路径 |
|------|------|------|
| CodeLlama-13B-Instruct-hf | ✓ 已就绪 | `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/` (25GB, 3个safetensors完整) |
| CodeLlama-7B-Instruct-hf | ⏳ 下载中 | `/root/autodl-tmp/models/CodeLlama-7b-Instruct-hf/` (PID=268545, ~3.5MB/s) |

### 磁盘空间
- `/root/autodl-tmp/`: 250GB 总量，65GB 可用（下载 7B 约需 14GB，充足）

### 训练脚本兼容性
- `train/train_sft.py` 使用 `AutoTokenizer` + `AutoModelForCausalLM`，通过 `--model_path` 传入路径，对 CodeLlama 完全兼容
- 已处理 `pad_token=None` 的情况（会自动设为 `eos_token`）
- CodeLlama 有 chat_template（`[INST]...[/INST]` 格式），`apply_chat_template` 可正常工作

### 下载日志
- 日志路径: `/tmp/codellama7b_download.log`
- 可用 `tail -10 /tmp/codellama7b_download.log` 查看进度
- 预计 ~45 分钟完成

### 需要注意
- 下载完成后，模型文件会在 `cache_dir` 下的 ModelScope 子目录结构中，实际路径可能是 `/root/autodl-tmp/models/CodeLlama-7b-Instruct-hf/AI-ModelScope/CodeLlama-7b-Instruct-hf/`，启动训练时需确认最终路径并传给 `--model_path`

---
