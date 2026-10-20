# diagnose plan 002 qwen3 1 7b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-qwen3-1_7b_20260514T211526_result.json`
- **Structured JSON:** [`95bd8dd4e07f6d195350.json`](../../sessions/95/95bd8dd4e07f6d195350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diag-qwen3-1_7b-sighup.md`。

**总结**：

| 项目 | 结论 |
|------|------|
| **直接原因** | 两个进程同时收到 SIGHUP (exit 129)，无任何 Python/CUDA/OOM 错误 |
| **根因** | SSH 会话断开 → 内核向前台进程组广播 SIGHUP → 两个 shard 同时被杀 |
| **数据损失** | ~100 seeds 的生成结果因 Python 缓冲区未 flush 全部丢失 |
| **附带问题** | 两个 shard 都在 cuda:0 上运行（未指定 `--device cuda:1`） |
| **修复** | ① tmux/nohup 隔离进程 ② s1 指定 `--device cuda:1` ③ 脚本加 `f.flush()` 防崩溃丢数据 |

---
