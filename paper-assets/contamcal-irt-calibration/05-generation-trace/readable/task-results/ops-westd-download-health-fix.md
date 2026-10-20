# ops westd download health fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-download-health-fix_20260518T084301_result.json`
- **Structured JSON:** [`59c05fcc3a053ae3dd22.json`](../../sessions/59/59c05fcc3a053ae3dd22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 进程状态
| 模型 | PID | 状态 | 进度 |
|------|-----|------|------|
| **Qwen2.5-7B** | 5064 | **活跃下载中** | 2/4 shards 完成，shard 1 @2.5G, shard 3 @1.9G（剩余 ~2.8G） |
| **Qwen2.5-14B** | 5066 | 活跃下载中 | 2/8 shards 完成，6 shards 并行下载中 |
| **Gemma-2-9b** | 6380 | 活跃下载中 | ~10G 已下载，8 shards 进行中 |
| **Phi-4** | ~~8159~~ | **已暂停** | 1.6G partial 文件保留，断点续传安全 |
| **OLMo-2-7B** | ~~8168~~ | **已暂停** | 13G partial 文件保留（含 1 完成 shard），断点续传安全 |

### 已执行优化
- Kill 了 Phi-4 和 OLMo-2 下载进程，释放带宽给 Batch 1（7B/14B/Gemma）
- 清理了对应 screen 会话
- Partial 文件完好，7B 完成后可用 `hf download` 断点续传恢复

### 7B 预计完成时间
剩余 ~2.8G，带宽从 5 路降到 3 路，预计 20-40 分钟内完成。

---
