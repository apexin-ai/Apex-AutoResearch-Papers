# ops multi exp status check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_multi_exp_status_check_20260517T133246_result.json`
- **Structured JSON:** [`f5fb938370099c04940d.json`](../../sessions/f5/f5fb938370099c04940d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|---|---|
| **exp_arXiv_llama8b** (cuda:1) | 正在生成 depth 5，110/275 batches (~40%)。depth 4 已完成。~6.1s/it |
| **exp_wiki_llama8b** (cuda:2) | 刚启动 depth 1，25/625 batches (~4%)。5000 samples，~6.4s/it |
| **exp_arXiv_olmo** (cuda:0) | 进程在跑（tmux session `exp_arXiv_olmo`） |
| **Qwen2.5-7B 下载** | 进行中，6/14 files fetched。目录已有 config/tokenizer 文件，模型权重正在下载 |
| **Mistral-7B 路径** | `/root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3/`，含 3 个 safetensors 分片，完整可用 |
| **Mistral arXiv 数据** | `data/exp_arXiv_mistral7b/depth_0.jsonl` 已就绪，2200 行 |

---
