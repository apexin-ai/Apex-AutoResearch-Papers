# ssh rsft code verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-code-verify_20260514T235032_result.json`
- **Structured JSON:** [`096f38e15cb81f4ca3f5.json`](../../sessions/09/096f38e15cb81f4ca3f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RSFT 代码就绪状态总结

**3 个文件全部就位**，`--help` dry-run 全部通过，所有内部依赖 import 正常。

### 需修复的问题（3 项）

| 优先级 | 问题 | 说明 |
|--------|------|------|
| **CRITICAL** | `rsft_generate.py` `--quantize` 默认 True | 4-bit + `merge_and_unload()` 在 RTX 5090 上触发 CUBLAS 错误，必须改为默认 False |
| **CRITICAL** | score_filter → trainer 数据格式不兼容 | score_filter 输出 JSON array + `{messages, scores.ced_reward}` 结构；trainer 期望 JSONL + `{input, output, ced_score}` 结构。**两处不兼容** |
| **MODERATE** | NLI 模型未预下载 | `cross-encoder/nli-deberta-v3-base` 本地不存在，score_filter 需要它做 CED 打分 |

### 正常的部分

- 模型路径 (`Qwen3-4B`, `sft_output`) 均存在且有效
- `rsft_trainer.py` 的 `--quantize` 正确默认 False
- CED reward 模块、DocREDProcessor、parse_model_output 等依赖全部可导入
- 参数设计合理（N=8, temperature=0.7, top_pct=25, LoRA r=64/α=128）

### 当前 GPU 占用

4 张卡全部被遗留 GRPO eval 和 diversity_probe 占用，RSFT 需等任务完成。

---
