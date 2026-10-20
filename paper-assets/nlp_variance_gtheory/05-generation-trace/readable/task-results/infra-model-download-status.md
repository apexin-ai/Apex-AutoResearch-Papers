# infra model download status

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model_download_status_20260521T002937_result.json`
- **Structured JSON:** [`3d7973b272cd20834a01.json`](../../sessions/3d/3d7973b272cd20834a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型下载状态：

| 模型 | 状态 | 大小 | 本地路径 |
|------|------|------|----------|
| Qwen/Qwen3-8B-Instruct | **未完成** | 4KB（仅 .mdl 元数据） | — |
| google/gemma-2-9b-it | **完成** | 18GB | `/root/autodl-tmp/.hf_cache/LLM-Research/gemma-2-9b-it/` |
| mistralai/Mistral-7B-Instruct-v0.3 | **未完成** | 11GB（部分） | — |

详情：
- **Qwen3-8B-Instruct**：ModelScope 下载失败或中断，目录只有元数据文件，temp 目录也为空，无下载进程运行
- **gemma-2-9b-it**：ModelScope 下载完整，config.json + 4/4 safetensors + tokenizer 齐全
- **Mistral-7B-Instruct-v0.3**：HF hub 下载不完整，snapshot 中缺 `model-00002-of-00003.safetensors`，有 2 个 `.incomplete` blob 文件；ModelScope 目录为空

磁盘：`/root/autodl-tmp/` 使用 89GB / 350GB (26%)

---
