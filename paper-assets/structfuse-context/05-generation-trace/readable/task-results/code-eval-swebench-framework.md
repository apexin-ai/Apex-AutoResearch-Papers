# code eval swebench framework

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_swebench_framework_20260512T220532_result.json`
- **Structured JSON:** [`fce88b4960134b3d677b.json`](../../sessions/fc/fce88b4960134b3d677b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

### Part A: M1 提取状态

| 指标 | 值 |
|------|-----|
| 进程 PID 577864 | **运行中**，已运行 1h18m |
| 已完成 repo | **14 / 131** (10.7%) |
| 已产出 JSON 文件 | **1713** |
| 已跳过 instance | **660** (skip_log.jsonl) |
| 磁盘 /root/autodl-tmp/ | 102G / 169G (60%，剩余 68G) |
| 最新日志 | 正在处理 `Suor/funcy`, `oauthlib/oauthlib`, `agronholm/typeguard` |

按当前速率（14 repo / 1.3h），预计总耗时 ~12h（比预期 36h 快不少，可能小 repo 先完成）。

### Part B: eval_swebench.py

已创建 `/root/structfuse/scripts/eval_swebench.py`，`--help` 验证通过。框架包含：
- 完整 argparse（9 个参数）
- `compute_bootstrap_ci()` — 10000 resamples, percentile method, seed=42
- 单 instance 评估流程（checkout → retrieve → context → patch → verify）
- 异常隔离（单 instance 失败不中断）
- 输出 `results.jsonl` + `summary.json`
- 4 处 TODO placeholder 已标注（retriever 加载、文件检索、LLM agent、测试验证）

---
