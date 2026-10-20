# fix kill duplicate processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_duplicate_processes_20260513T235323_result.json`
- **Structured JSON:** [`73174fa7f6b88440024d.json`](../../sessions/73/73174fa7f6b88440024d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 杀掉的 PID
- **PID 134450** — semantic_only nohup python 进程（PPID=134445）
- **PID 134886** — full_s1 nohup python 进程（PPID=134881）
- **PID 134445, 134881** — 对应的 nohup bash wrapper

### 2. 输出文件损坏情况
轻微损坏，各 1 行截断 JSON，已清理：
- `phase2_scierc_semantic_only.jsonl`: 清理后 37 行，删除 1 行（`H01-1049_sent5` 截断）
- `phase2_scierc_full_s1.jsonl`: 清理后 33 行，删除 1 行（`INTERSPEECH_2013_21_abs_sent5` 截断）
- 两个文件均 **0 duplicates**，无需重跑

### 3. 修复后进程状态
每个实验只剩 tmux 内的进程，正常运行：
- **semantic_only**: PID 134207 (PPID 134206→134202→106527 tmux), GPU 0
- **full_s1**: PID 134598 (PPID 134597→134593→106527 tmux), GPU 1

### 4. GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 41788 / 97887 MiB | 93% |
| 1 | 16489 / 97887 MiB | 84% |

GPU 1 显存从之前跑两个进程降到了 16GB（nohup 进程释放了显存），两个实验各占一块 GPU 正常运行。

---
