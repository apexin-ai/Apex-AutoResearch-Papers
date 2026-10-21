# ssh a1 zombie fix restart

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a1_zombie_fix_restart_20260520T082320_result.json`
- **Structured JSON:** [`b53d8e978f28707575b5.json`](../../sessions/b5/b53d8e978f28707575b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功恢复并运行。

## 汇总

| 项目 | 结果 |
|------|------|
| **崩溃原因** | 日志无 Python traceback，训练在 step 6870 处突然中断。进程被信号杀死（非 Python 异常）。dmesg 无权限，无法确认是否 OOM killer。最可能是系统内存压力导致 OOM kill（4个训练任务同时运行，每个占 ~4.5GB RSS + dataloader workers）。 |
| **Kill 结果** | PID 181881(bash) + 181885(timeout) + 181886(残留 Python) 全部已杀，GPU 3 显存释放至 0 MiB |
| **新 PID** | 185994 |
| **验证** | 从 step 6000 成功 resume，GPU 3 占用 13385 MiB，step 6001 loss=0.2738, step 6004 loss=0.2865，lr=2.34e-05，与崩溃前水平一致，训练正常 |

---
