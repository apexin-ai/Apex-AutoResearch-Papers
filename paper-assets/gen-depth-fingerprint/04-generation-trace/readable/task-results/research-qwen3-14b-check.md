# research qwen3 14b check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen3-14b-check_20260520T105334_result.json`
- **Structured JSON:** [`584d0f4cf857e49e3188.json`](../../sessions/58/584d0f4cf857e49e3188.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载已在运行，正在并行下载多个 shard。

## 结果报告

### Qwen3-14B-Base 状态
- **存在** — HuggingFace: [`Qwen/Qwen3-14B-Base`](https://huggingface.co/Qwen/Qwen3-14B-Base)，ModelScope: [`Qwen/Qwen3-14B-Base`](https://modelscope.cn/models/Qwen/Qwen3-14B-Base)
- **参数量**: 14B
- **FP16 显存需求**: ~29GB（≤ 30GB，4x RTX 5090 32GB 充足）
- **License**: Apache 2.0，无需申请

### 操作结果
- Qwen2.5-14B 下载已终止（PID 190263 killed，仅下载了 2.8G）
- **Qwen3-14B-Base 下载已启动**，PID: **190641**
  - 通过 ModelScope CDN 下载，共 8 个 shard（每个 ~3.6GB，总计 ~28GB）
  - 日志: `/tmp/download_qwen3_14b_base.log`
  - 存储路径: `/root/autodl-tmp/models/Qwen3-14B-Base/`

### 注意
当前 ModelScope 下载速度较慢（~450kB/s），可能需要数小时。后续可用 `tail -3 /tmp/download_qwen3_14b_base.log` 监控进度。

---
