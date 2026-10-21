# ssh check disk volumes

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-disk-volumes_20260513T175652_result.json`
- **Structured JSON:** [`09e6c84252c28172fe83.json`](../../sessions/09/09e6c84252c28172fe83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 存储报告

### 挂载点总览

| 挂载点 | 总容量 | 已用 | 可用 | 用途 |
|--------|--------|------|------|------|
| `/` (overlay) | 30G | 16G | **15G** | 系统根分区 |
| `/root/autodl-tmp` | 169G | 86G | **84G** | 数据盘 |
| `/dev/shm` | 240G | ~0 | 240G | 共享内存（tmpfs，不可持久化） |
| `/autodl-pub` | 7.0T | 6.7T | 313G | 公共只读数据集 |

### 关键发现

- **`/root/autodl-fs/` 不存在** — 此实例未开通网络文件系统
- **`/root/data/` 不存在**
- **autodl-tmp 实际有 84G 可用**，不是之前说的 7.3G（可能之前是不同时间点的快照）
- autodl-tmp 当前大项占用：`.hf_cache/` 42G、`models/` 24G

### 建议

- **HF_HOME** → `/root/autodl-tmp/.hf_cache`（当前已是）
- **checkpoint 输出** → `/root/autodl-tmp/`（唯一可写数据盘，84G 可用，够用）
- 没有额外大容量盘。如果空间不够，清理 `.hf_cache` 和 `models` 中不再需要的模型是最快的释放方式。

---
