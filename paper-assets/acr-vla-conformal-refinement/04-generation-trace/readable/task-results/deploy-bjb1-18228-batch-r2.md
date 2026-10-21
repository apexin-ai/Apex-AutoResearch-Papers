# deploy bjb1 18228 batch r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-batch-r2_20260528T061736_result.json`
- **Structured JSON:** [`401d0186adbb150668ce.json`](../../sessions/40/401d0186adbb150668ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署结果

**全部 4 个实验无法按计划部署，原因如下：**

### 问题 1：GPU 被占用（C001 约束）

| GPU | 显存占用 | PID | 状态 |
|-----|---------|-----|------|
| cuda:0 | 12757 MiB | 982389 | **占用** |
| cuda:1 | 1 MiB | — | 空闲 |
| cuda:2 | 13120 MiB | 983106 | **占用** |
| cuda:3 | 10429 MiB | 983396 | **占用** |

cuda:0/2/3 上有 python 进程在跑，按 C001 约束禁止提交。

### 问题 2：evaluate.py 不存在

唯一空闲的 cuda:1 已提交但立即失败——`/root/acr-vla-conformal-refinement/evaluate.py` 不存在（EXIT_CODE=2）。

项目目录下实际有的脚本：
- `run_eval_gpu.py`
- `benchmark_batched.py`
- `smoke_test.py`
- `scripts/` 目录

### 需要你确认

1. **GPU 占用**：cuda:0/2/3 上的进程是否可以 kill？还是等它们跑完？
2. **正确的评估命令**：应该用 `run_eval_gpu.py` 还是其他脚本？请提供正确的命令。

---
