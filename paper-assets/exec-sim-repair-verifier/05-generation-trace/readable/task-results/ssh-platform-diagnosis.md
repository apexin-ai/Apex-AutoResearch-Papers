# ssh platform diagnosis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_platform-diagnosis_20260519T223525_result.json`
- **Structured JSON:** [`abb0fb01e5f7a8ce16e9.json`](../../sessions/ab/abb0fb01e5f7a8ce16e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结论：

---

## 诊断结果

### 1. 平台级 wall-time 限制
**无显式平台限制。** cgroup 显示 `0::/`（根 cgroup），SeetaCloud 容器层面无可见的 wall-time cap。所有超时来自 `submit_training_job` wrapper 的 `timeout` 命令。

### 2. submit_training_job timeout 设置
- **当前运行的 eval job**: `timeout 86400`（24h）— 从 ps aux 中的进程命令行直接可见
- **已死的两个训练 job**: 推算为 `timeout 28800`（8h）— 两个 job 分别在 7h51m 和 7h50m 时被杀，加上模型加载/数据预处理的启动时间约 8-10 分钟，总进程时间 ≈ 8h

### 3. 进程被杀原因

| Job | EXIT_CODE | 死亡时间 (UTC) | 进度 | 原因 |
|-----|-----------|---------------|------|------|
| cls8b-repo-s456-train-v2 | **124** | ~06:00 May 20 | 2320/6633 (35%) | `timeout` 命令超时 SIGTERM |
| deepseek-cls-repo-s456-train-v3 | **124** | ~06:22 May 20 | 2333/6489 (36%) | `timeout` 命令超时 SIGTERM |
| qwen3-8b-cwm-repo-s123-train | **无 exit file** | 04:24+ May 20 | eval 22% | **SIGKILL**（trap 未触发，可能 OOM） |

- EXIT_CODE=124 = `timeout` 命令专属退出码，不是 OOM 也不是平台杀
- qwen3 job 更可疑：无 exit file、无 EXIT_CODE、进程消失 — 说明是 SIGKILL（trap 无法捕获），很可能是 OOM killer

### 4. GPU 状态

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 0MiB | 0% | **空闲** |
| 1 | 0MiB | **100%** | **异常** — 无进程但满利用率，phantom compute 残留 |
| 2 | 29.6GB | 85% | 在用 (deepseek-cwm-repo-s42-seq4096-eval) |
| 3 | 0MiB | 0% | **空闲** |

GPU 0/3 可用。**GPU 1 需要 `nvidia-smi -r` 重置**或等它自行恢复，否则可能影响后续任务。

---
