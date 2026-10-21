# infra cqa1 disk cleanup

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cqa1_disk_cleanup_20260518T021820_result.json`
- **Structured JSON:** [`70eb76386be825da8c9c.json`](../../sessions/70/70eb76386be825da8c9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：磁盘从 97%（假设之前）降到 16%（39G/250G），释放了约 61G。**

保留的内容：
- Qwen 系列（20G）
- Qwen2.5-14B-Instruct-AWQ（9.4G）
- Pythia-1.4B（5.5G + hub 2.8G）
- 所有正在运行实验的数据和结果
- 所有 exp_024_arxiv、exp_arXiv_qwen7b 源数据

删除的内容：
- LLaMA-3.1-8B（30G）
- Mistral-7B-v0.3（28G）
- OLMo-1B（4.4G）
- Dataset 缓存（c4, arxiv-summarization, wikipedia）

---
