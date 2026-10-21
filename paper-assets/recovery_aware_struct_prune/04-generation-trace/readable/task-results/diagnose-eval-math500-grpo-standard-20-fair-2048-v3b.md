# diagnose eval math500 grpo standard 20 fair 2048 v3b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_grpo_standard_20_fair_2048_v3b_20260523T143304_result.json`
- **Structured JSON:** [`182f614b108e1af73478.json`](../../sessions/18/182f614b108e1af73478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败原因：GPU 2 异常挂起

进程在第 15/500 题（~8分钟）时被静默杀死（无 Python traceback = 收到 SIGKILL），日志文件仅 10 行，无任何错误信息。

**关键证据 — GPU 2 状态异常：**
```
GPU 2: 0MiB memory / 100% GPU-Util / 无关联进程
```
GPU-Util 100% 但显存为 0 且无进程，这是典型的 **GPU hang/fault 状态**（可能是 Xid 错误）。进程被驱动层强制终止。

### 排除项
| 检查项 | 状态 |
|--------|------|
| 系统内存 | ~1TB 总量，570GB 空闲 — 非 OOM |
| 磁盘空间 | `/root/autodl-tmp` 131GB 可用 — 充足 |
| 模型路径 | 存在，model.safetensors 12GB ✓ |
| 输出文件 | 不存在，无部分结果 |
| GPU 显存 | 97GB，12GB 模型应绑绑有余 |

### 重试建议

1. **GPU 2 需要重置**才能恢复正常。执行 `nvidia-smi -r` 或重启实例。
2. **更快的替代方案**：改用空闲 GPU 重试。当前 GPU 1 和 GPU 3 均空闲（0% util, 0MiB）。将 `CUDA_VISIBLE_DEVICES=2` 改为 `CUDA_VISIBLE_DEVICES=1` 或 `CUDA_VISIBLE_DEVICES=3` 即可直接重试，无需修改其他参数。
3. 命令本身无问题，不需要改参数或清理磁盘。

---
