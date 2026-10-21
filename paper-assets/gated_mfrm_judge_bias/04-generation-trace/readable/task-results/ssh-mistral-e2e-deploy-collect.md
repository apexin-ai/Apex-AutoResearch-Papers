# ssh mistral e2e deploy collect

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mistral_e2e_deploy_collect_20260524T060635_result.json`
- **Structured JSON:** [`25c7ff802eb217d62c90.json`](../../sessions/25/25c7ff802eb217d62c90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态总结：
- **下载进度**：12/14 shards 完成（52G），shard 11 正在 aria2c 重新下载（42%，ETA ~3 min），shard 12/13 缺失
- **磁盘**：/root/autodl-tmp 250G 已用 235G，剩余 16G（够用，还需约 10G）
- **自动化管道已在运行**：download_mistral_v3.sh → deploy_mistral_vllm.sh → auto_start_mistral_collect.sh
- **其他进程正常**：exp017 on cuda:0, vLLM Llama on cuda:1 port 8001, 4 个 collect.py (sonnet/gemini/deepseek/qwen3)

4.5 分钟后回来检查下载是否完成。

---
