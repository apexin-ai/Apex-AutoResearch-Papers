# cpu llama bootstrap n2000 restart

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_llama-bootstrap-n2000-restart_20260522T135606_result.json`
- **Structured JSON:** [`87805fa7e748f217d327.json`](../../sessions/87/87805fa7e748f217d327.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程正常运行中，无需重启。**

PID 465851 (`train_probe_fast.py`) 状态：

| 方向 | 状态 | 耗时 |
|------|------|------|
| en_en | ✅ 完成 | 80.5 min |
| zh_zh | ✅ 完成 | 95.6 min |
| en_zh | ✅ 完成 | 120.8 min |
| zh_en | 🔄 进行中 | 818/2000 tasks (35.6 min) |

zh_en 方向已完成约 41%，按速率预计还需 ~50 分钟完成。输出文件会在全部 4 个方向跑完后才写入 `data/llama31/probe_results_bootstrap_n2000.json`。

Qwen 的对应文件已完成（22KB，21:08 生成）。

---
