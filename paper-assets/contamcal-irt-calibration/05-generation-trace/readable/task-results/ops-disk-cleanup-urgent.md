# ops disk cleanup urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-urgent_20260515T025330_result.json`
- **Structured JSON:** [`f3d52352dac8e80dc9b6.json`](../../sessions/f3/f3d52352dac8e80dc9b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

### 清理前后对比

| | 清理前 | 清理后 |
|---|---|---|
| 根分区使用 | 26G / 30G (86%) | 23G / 30G (75%) |
| 可用空间 | 4.3GB | 7.6GB |

### 清理内容

| 操作 | 释放空间 |
|---|---|
| `/root/.cache/huggingface` → 数据盘软链 | ~4.1GB |
| conda pkgs 缓存清理 | ~107MB |
| vllm cache 清理 | ~68MB |
| /tmp 空 UUID 目录清理 | inodes |
| pip cache | 已空，无需清理 |

HF cache 软链已生效：`/root/.cache/huggingface -> /root/autodl-tmp/.hf_cache_system`。后续任何使用默认 HF cache 路径的进程都会写入数据盘。

---
