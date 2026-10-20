# ops cqa1 disk cleanup yi download

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-disk-cleanup-yi-download_20260522T181137_result.json`
- **Structured JSON:** [`a2aa08ad935b2115755c.json`](../../sessions/a2/a2aa08ad935b2115755c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。报告如下：

---

### 报告

**models/LLM-Research/ 内容**（6.0GB）：
- `Llama-3___2-3B/` — ModelScope 格式的 Llama-3.2-3B
- `Meta-Llama-3___2-3B/` — 关联元数据目录
- 未删除（等 Director 决定）

**磁盘清理**：
- 删除 `llama3-8b-tmp/`（15GB）→ 可用空间从 14GB 增至 28GB

**Yi-1.5-9B 下载**：成功
- 路径：`/root/autodl-tmp/.hf_cache/Yi-1.5-9B/`
- 4 个 safetensors 分片（4.6G + 4.7G + 4.7G + 2.6G = ~16.6GB）
- 验证通过：`LlamaForCausalLM, hidden=4096, layers=48, vocab=64000`
- 来源：hf-mirror.com，耗时约 15 分钟

**最终磁盘**：169GB 总量，158GB 已用，12GB 可用（94%）

---
