# analysis gte large check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gte-large-check_20260514T134036_result.json`
- **Structured JSON:** [`fcf2dfd0d34cbc4837da.json`](../../sessions/fc/fcf2dfd0d34cbc4837da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。

## 排查结果

**gte-large embedding 文件确实异常，需要重新生成。**

| Encoder | 文件大小 | embeddings 数量 | embed_dim |
|---------|---------|----------------|-----------|
| e5-large | 2.1G | 54,809 | 1024 |
| bge-m3 | 1.1G | 54,809 | 1024 |
| **gte-large** | **402K** | **10** | 1024 |

**原因**：gte-large 文件只包含 10 条 embedding（而非完整的 54,809 条）。文件格式正确、没有截断，但生成过程极早就中止了——只处理了第一个 batch 的数据就停了。可能是脚本报错退出或被手动中断。

**模型路径**显示 gte-large 是从 ModelScope 下载的（`/root/autodl-tmp/.hf_cache/modelscope_models/gte-large/damo/...`），模型本身加载没问题，问题出在生成循环中。

**需要重新运行 gte-large 的 embedding 生成。**

---
