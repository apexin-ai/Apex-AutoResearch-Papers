# diagnose eval pi05 random long postfix failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_long_postfix_failures_20260524T140730_result.json`
- **Structured JSON:** [`a689b24678314c65ff30.json`](../../sessions/a6/a689b24678314c65ff30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有三个实验都已正常完成，没有异常退出。**

日志显示每个实验都跑完了全部 10 个 task (T0-T9)，输出了 RESULT 行并保存了 JSON 文件：

| 实验 | 服务器 | 状态 | 结果 |
|------|--------|------|------|
| random k=0.85 seed42 | westd-41074 | **已完成** | SR=45.2%, 保存至 `pi05_random_k0.85_libero_10_seed42.json` |
| random k=0.95 seed42 | westd-41074 | **已完成** | SR=63.2%, 保存至 `pi05_random_k0.95_libero_10_seed42.json` |
| random k=0.70 seed42 | westd-38929 | **已完成** | SR=65.8%, 保存至 `pi05_random_k0.70_libero_10_seed42.json` |

日志中无任何 error / traceback / OOM / signal。进程被标记为 "failed" 或 "miss heartbeat" 很可能是因为 **进程已正常退出（return code 0），但监控系统把进程结束误判为异常**。所有结果文件都已写入，不需要重跑。

---
