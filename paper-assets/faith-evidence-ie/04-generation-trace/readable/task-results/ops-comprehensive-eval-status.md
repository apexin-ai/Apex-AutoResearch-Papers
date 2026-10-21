# ops comprehensive eval status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_comprehensive_eval_status_20260516T123535_result.json`
- **Structured JSON:** [`19a758b2b056ef1b3f62.json`](../../sessions/19/19a758b2b056ef1b3f62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 / 32607 MiB | 0% | **空闲** |
| 1 | 23292 / 32607 MiB | 89% | 2个进程 (PID 337844 + 340116) |
| 2 | 18475 / 32607 MiB | 66% | 1个进程 (PID 335357) |
| 3 | 17883 / 32607 MiB | 62% | 1个进程 (PID 339692) |

### 各 Eval 状态

| # | 实验 | GPU | 状态 | 进度 | 预计剩余 |
|---|------|-----|------|------|---------|
| 1 | plan_006_qwen3_1_7b_no_evidence_eval_v3 | cuda:1 (PID 337844) | **运行中** | 105/247 (43%) | ~71 min |
| 2 | plan_006_qwen3_8b_no_evidence_eval_v2 | cuda:2 (PID 335357) | **运行中** | 186/247 (75%) | ~28 min |
| 3 | plan_016_llama_3_1_8b_no_evidence_eval | cuda:3 (PID 339692) | **运行中** | 93/247 (38%) | ~51 min |
| 4 | plan_016_llama_3_1_8b_sft_eval | cuda:1 (PID 340116) | **运行中** | 52/247 (21%) | ~110 min |
| 5 | plan_007_redocred_4b_sft_eval | — | **失败** | — | — |

### 失败详情

**plan_007_redocred_4b_sft_eval**: `HFValidationError` — tokenizer 加载时把本地路径 `/root/autodl-tmp/models/Qwen/Qwen3-4B` 当成 HuggingFace repo id 校验，导致报错。可能是 `huggingface_hub` 版本升级后对本地路径的处理变了，需要在 `from_pretrained` 调用时确保传入的是合法本地路径格式（或设置 `local_files_only=True`）。

### 备注
- 所有运行中的 eval 尚未产出 metrics（结果目录为空，推理阶段尚未完成）
- GPU 0 完全空闲，可用于重跑 redocred eval
- cuda:1 上同时跑了 1.7B (5.4GB) 和 llama-8B (17.9GB)，合计 23.3GB / 32.6GB，利用率 89%

---
