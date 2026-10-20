# infra cleanup and verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup_and_verify_20260513T180057_result.json`
- **Structured JSON:** [`3a82693eb19437f00796.json`](../../sessions/3a/3a82693eb19437f00796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | Qwen3-8B 模型 | **READY** — `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`（5 safetensors, 16G），软链接 `/root/autodl-tmp/models/Qwen3-8B-link` 已创建 |
| 2 | SciERC train.json | **READY** |
| 3 | SciERC test.json | **READY** |
| 4 | SciERC ontology_constraints.json | **READY** |
| 5 | DocRED dev.json | **READY** |
| 6 | DocRED ontology_constraints_docred.json | **READY** |
| 7 | run_extraction.py | **READY** |
| 8 | run_extraction_docred.py | **READY** |
| 9 | violation_checker.py | **READY** |
| 10 | violation_checker_docred.py | **READY** |
| 11 | 被 kill 的进程 | PID 102092（重复 Qwen3-8B 下载）+ PID 102087（其父 bash） |
| 12 | 剩余下载进程 | **无** — 模型已完整，无需继续下载 |

所有实验前置条件已就绪，可以开始实验。

---
