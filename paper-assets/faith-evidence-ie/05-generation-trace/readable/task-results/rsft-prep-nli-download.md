# rsft prep nli download

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rsft-prep_nli-download_20260515T010828_result.json`
- **Structured JSON:** [`9f57d52e7c3641479cb7.json`](../../sessions/9f/9f57d52e7c3641479cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报：

| 项目 | 状态 |
|------|------|
| **NLI 模型** (`cross-encoder/nli-deberta-v3-base`) | 已下载成功，缓存在 `/root/autodl-tmp/.hf_cache` |
| **RSFT 代码文件** | 三个文件均存在且是今天更新的版本：`rsft_generate.py` (08:06)、`rsft_score_filter.py` (08:04)、`rsft_trainer.py` (07:25) |
| **generate 进度** | `generations.jsonl` 已有 **1744 行**，文件 ~16MB，最后写入时间 09:08，正在持续生成中 |
| **sentence-transformers** | 已安装（`/root/miniconda3/lib/python3.12/site-packages/sentence_transformers`），无需额外安装 |

一切就绪，generate 完成后可直接运行 score_filter。

---
