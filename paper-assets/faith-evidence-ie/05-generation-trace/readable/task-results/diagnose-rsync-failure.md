# diagnose rsync failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_rsync-failure_20260520T075439_result.json`
- **Structured JSON:** [`0e2744a0ef74ad9a8acd.json`](../../sessions/0e/0e2744a0ef74ad9a8acd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Phase 1-3 完成。汇总：**

| 项目 | 结果 |
|------|------|
| **失败原因** | 首次 rsync 被 SSH 超时中断 — 日志仅 64 行，无错误信息、无完成摘要，rsync 在列出小文件后就断了，大文件（safetensors、模型权重）未传输 |
| **目标盘现状** | 594M / 350G（仅目录结构 + lock 文件 + 小脚本） |
| **源服务器** | SSH 连通正常，208G 数据完好 |
| **重启 rsync** | PID=5150，nohup 后台运行，增量模式（已传的小文件会跳过） |

3 分钟后首次检查传输进度。

---
