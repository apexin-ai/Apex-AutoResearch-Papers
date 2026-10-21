# ops restart stuck downloads

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-stuck-downloads_20260518T145048_result.json`
- **Structured JSON:** [`ff7b534463fd561e3a3b.json`](../../sessions/ff/ff7b534463fd561e3a3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gemma 也在增长了（0 → 10MB）。两个下载都在正常推进。

## 汇报

| 模型 | 旧 PID | 操作 | 新 PID | 状态 |
|---|---|---|---|---|
| OLMo-2 | 19571 | killed + 清 lock/incomplete + 重启 | **35305** | 下载中，~2.8 MB/s |
| Gemma | 6380 | killed + 清 lock/incomplete + 重启 | **35312** | 下载中，刚开始写入 |
| Phi-4 | 19608 | 未动 | 19608 | 继续运行 |

第一次重启因 `--resume-download` 参数不存在而失败，第二次 Gemma 缺 token 403。第三次两个都卡在旧 lock 文件上。最终清理了 `.cache/` 下的 `.lock` 和 `.incomplete` 文件后成功启动，加了 `--max-workers 1` 降低并发。OLMo-2 已有 ~19G 缓存（6 个 shard 中部分已完成），Gemma 已有 ~26G 缓存（18 个文件中部分已完成），剩余文件正在下载。

---
