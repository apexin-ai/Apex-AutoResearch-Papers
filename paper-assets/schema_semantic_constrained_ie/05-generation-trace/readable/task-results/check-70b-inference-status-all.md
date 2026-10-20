# check 70b inference status all

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_70b_inference_status_all_20260522T035902_result.json`
- **Structured JSON:** [`76ce1b2096cb45021e97.json`](../../sessions/76/76ce1b2096cb45021e97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 70B LoRA 推理状态汇总

### 进程状态：两个 unconstrained 推理任务正在运行

| 任务 | PID | GPU | 启动时间 | 状态 |
|------|-----|-----|---------|------|
| SciERC unconstrained | 878492 / 880000 | GPU 0 | 10:16 / 10:19 | **运行中** (101% CPU) |
| DocRED unconstrained | 881090 | GPU 1 | 10:32 | **运行中** (101% CPU) |

> 注意：SciERC 有两个进程（PID 878492 和 880000），看起来是先启动了一个无 `--skip_on_error` 的，又启动了一个带 `--skip_on_error` 的，两个都在跑且都写同一个输出文件。

### 输出文件行数

| 文件 | 行数 | 大小 |
|------|------|------|
| `scierc_unconstrained.jsonl` | **344 行** | 645 KB |
| `docred_unconstrained.jsonl` | **62 行** | 662 KB |

### S1 constrained 输出
- `scierc_s1.jsonl` — **不存在**
- `docred_s1.jsonl` — **不存在**

S1 constrained 推理尚未开始。

### GPU 使用

| GPU | 利用率 | 显存使用 |
|-----|--------|---------|
| GPU 0 | 94% | 79,190 / 97,887 MiB |
| GPU 1 | 80% | 40,921 / 97,887 MiB |

两块 GPU 都在满负载工作。

### 其他
- 有一个 `docred_200_monitor.sh` 监控脚本在 tmux pts/3 中运行（每 600 秒轮询一次）
- DocRED 日志正常，全部是 `pad_token_id` 的常规 warning，无报错
- tmux session `llama_beam` 存在（自 May17）

---
