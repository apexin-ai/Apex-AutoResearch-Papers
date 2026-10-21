# ssh docred progress check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_docred_progress_check_20260514T061257_result.json`
- **Structured JSON:** [`e1e44db2a9c450f8b021.json`](../../sessions/e1/e1e44db2a9c450f8b021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_project_file` 只允许写白名单文件，不能写 artifacts/ 下的文件。我直接把结果报告在这里。

## DocRED Progress Check - Loop 3 (2026-05-14)

| 实验 | 进度 | 百分比 | PID | 运行时间 | CPU | GPU |
|------|------|--------|-----|----------|-----|-----|
| grammar_only | 752/998 docs | **75.4%** | 150766 | 4h18m45s | 100% | GPU0: 86%, 17535/97887 MiB |
| full_s1 | 617/998 docs | **61.8%** | 157042 | 2h56m55s | 0.0% | GPU1: 85%, 17487/97887 MiB |

### 预估剩余时间

- **grammar_only**: 752 docs / 258.75 min ≈ 2.91 docs/min → 剩余 246 docs → **~1h25m**
- **full_s1**: 从 doc 87 resume，本轮处理 530 docs / 176.9 min ≈ 3.0 docs/min → 剩余 381 docs → **~2h07m**

### 注意事项

- PID 157042 (full_s1) 的 CPU 为 0.0%、RSS 仅 3.5MB，说明该 PID 是 bash/tmux 包装进程，实际 Python 推理进程是其子进程。GPU1 利用率 85% 确认推理正在正常运行。
- 两块 GPU 均正常工作，显存占用约 17.5GB/98GB。

---
