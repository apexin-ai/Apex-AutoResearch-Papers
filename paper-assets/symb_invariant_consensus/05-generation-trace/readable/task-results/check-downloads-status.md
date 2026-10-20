# check downloads status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_downloads-status_20260516T200629_result.json`
- **Structured JSON:** [`2b045a25bdd7f0d8720d.json`](../../sessions/2b/2b045a25bdd7f0d8720d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 任务 | 状态 | 详情 |
|------|------|------|
| **LLaMA-3.1-8B-Instruct** | ✅ 已完成 | PID 186855 已退出。14G，4 个 safetensors 分片 + config.json + tokenizer.json 齐全。路径: `.../Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` |
| **Mistral-7B-Instruct-v0.3** | 🔄 进行中 | PID 236801 仍在运行。当前 1.1G（完整约 15G）。日志显示 2/15 文件已拉取（小文件），大 safetensors 正在下载中。进度 ~7%。未设 HF_TOKEN，速率受限。 |
| **exp-002 k_sensitivity** | 🔄 进行中 | 正在跑第 13/60 题（当前 K=6）。总计 360 runs，已完成 12 runs ≈ **3.3%**。当前批次 ETA 26.7 min（48 题剩余，avg 33.4s/题）。总剩余约 **3.2 小时**（假设各 K 值耗时相近）。 |

**注意事项:**
- LLaMA 模型路径多了两层 ModelScope 嵌套（`LLM-Research/Meta-Llama-3___1-8B-Instruct/`），加载时需用完整路径或做 symlink
- Mistral 下载未认证（`unauthenticated requests`），可能被限速，预计还需较长时间

---
