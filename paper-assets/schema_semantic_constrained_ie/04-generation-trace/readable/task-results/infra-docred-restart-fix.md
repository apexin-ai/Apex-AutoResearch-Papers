# infra docred restart fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_docred_restart_fix_20260513T193319_result.json`
- **Structured JSON:** [`a4ee50e3a732f5f0c891.json`](../../sessions/a4/a4ee50e3a732f5f0c891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态正常，无需清理或重新提交。**

| 项目 | 状态 |
|------|------|
| **PID 113148** (wrapper bash) | **ALIVE**, 运行 3 分钟 |
| **PID 113153** (python3 run_extraction_docred.py) | **ALIVE**, GPU 1 上占用 18262 MiB，正在提取 |
| **PID 112577** (旧 dry-run) | **DEAD**，已自行退出，无需清理 |
| **PID 110681** (run_extraction.py schema) | **ALIVE**, GPU 0 上占用 16516 MiB，独立任务 |

**进度**:
- Resume 起点: 265 docs
- 当前已处理: **281 docs**（3 分钟内新增 16 条）
- 剩余: **717 docs** (总目标 998)
- 速率约 ~5 docs/min，预计还需 ~2.5 小时完成

**GPU 分配**:
- GPU 0: 16525/97887 MiB — PID 110681 (schema extraction)
- GPU 1: 18553/97887 MiB — PID 113153 (DocRED extraction) ✅

**结论**: 之前的 PID 113148 并没有被 SIGHUP kill，它是一个新提交的进程（只跑了 3 分钟）。DocRED 全量提取正在正常运行，使用 `--device cuda:0` + `CUDA_VISIBLE_DEVICES=1`，参数正确。无需任何操作，等待完成即可。

---
