# urgent kill cuda3 and fix

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_kill-cuda3-and-fix_20260512T134728_result.json`
- **Structured JSON:** [`f050d5fa785a66255da3.json`](../../sessions/f0/f050d5fa785a66255da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. cuda:3 进程
- **PID 115081** — `test_correction_feasibility.py --gpu 3` (Qwen3-14B-AWQ, 11426 MiB) → 已杀掉，GPU 3 已清空 (0 MiB)

### 2. GPU 2-5 清理
- GPU 2: VLLM (democalib 项目，非本项目) → 保留
- GPU 5: run_mvp.py (democalib 项目，非本项目) → 保留
- 无其他本项目进程需要清理

### 3. 脚本修复
**无需修复** — 所有 src/*.py 已经使用正确的 device_map：

| 文件 | device_map 用法 |
|------|----------------|
| `collect_trajectories.py:107` | `device_map=f"cuda:{gpu}"` |
| `eval_alfworld.py:49` | `device_map=f"cuda:{gpu}"` |
| `generate_corrections.py:58` | `device_map=f"cuda:{gpu}"` |
| `test_correction_feasibility.py:235` | `device_map=f"cuda:{args.gpu}"` |
| `test_correction_feasibility_replay.py:112` | `device_map=f"cuda:{gpu}"` |
| `classify_errors.py:249` | `device_map=device` (device=`f"cuda:{gpu}"`) |

零处 `device_map="auto"`，零处硬编码 `cuda:[2-9]`。

### 4. 最终 GPU 状态

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| 0 | 7763 MiB | collect_trajectories.py (本项目) |
| 1 | 0 MiB | 空闲 |
| 2 | 22103 MiB | VLLM democalib |
| 3 | **0 MiB** | **已清空** |
| 4 | 0 MiB | 空闲 |
| 5 | 18736 MiB | run_mvp.py democalib |

---
