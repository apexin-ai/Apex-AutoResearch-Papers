# prep download internlm deepseek

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_download_internlm_deepseek_20260521T102248_result.json`
- **Structured JSON:** [`989d0cbd1d45a8afacff.json`](../../sessions/98/989d0cbd1d45a8afacff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**下载状态**（均后台 nohup 运行）：
| 模型 | PID | 大小 | 速度 | 预计完成 |
|------|-----|------|------|---------|
| InternLM2.5-7B-Chat | 149391 | ~14GB (8 shards) | ~800kB/s | ~2-3h |
| DeepSeek-LLM-7B-Chat | 149538 | ~18GB (2 shards) | ~870kB/s | ~3-4h |

**model_paths.py 已更新**：
- `MODEL_PATH_MAP`: 添加了 `internlm/internlm2_5-7b-chat` → ModelScope 本地路径，`deepseek-ai/deepseek-llm-7b-chat` → ModelScope 本地路径
- `MODEL_DISPLAY_NAMES`: InternLM2.5-7B、DeepSeek-7B，含 HF repo ID / 目录名 / 全路径等多种变体

**vLLM 兼容性**：
- InternLM2.5：基于 InternLM2 架构，vLLM 0.9.x 支持，需 `trust_remote_code=True`
- DeepSeek-LLM-7B：标准 LlamaForCausalLM 架构，vLLM 完全兼容

**监控命令**：
```bash
tail -3 /tmp/download_internlm.log
tail -3 /tmp/download_deepseek.log
```

---
