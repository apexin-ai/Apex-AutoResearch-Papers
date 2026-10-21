# ops check bjb1 18228 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb1-18228-status_20260515T050057_result.json`
- **Structured JSON:** [`832a538cd0245e06b358.json`](../../sessions/83/832a538cd0245e06b358.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

## bjb1-18228 进程状态

### 关键 PID
- **PID 253085 (eval-acr-spatial-v4-small)** — **已死亡**，ps 未找到该进程
- **PID 270097 (eval-acr-spatial-v4-obs-only-r2)** — **已死亡**，ps 未找到该进程

### 实验相关进程
**无任何实验进程在运行。** `ps aux` 输出中没有任何 python eval/libero/acr 相关进程。服务器上只有系统服务（sshd、supervisord、jupyter-lab、tensorboard、autopanel、proxy）。

### GPU 使用
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | 0 MiB | 24564 MiB | 0% |
| 1 | 0 MiB | 24564 MiB | 0% |
| 2 | 0 MiB | 24564 MiB | 0% |
| 3 | 0 MiB | 24564 MiB | 0% |

4 张卡全部空闲，无任何 GPU 负载。

### Sentinel 文件
无 sentinel 文件。

### Tmux
存在 tmux socket 目录，但无法用 read-only 模式列出 session 详情。

### 结论
**两个实验进程均已终止，所有 GPU 空闲。** kill-restart Worker 在被取消前很可能已经 kill 了这些进程。服务器当前无任何实验在运行。

---
