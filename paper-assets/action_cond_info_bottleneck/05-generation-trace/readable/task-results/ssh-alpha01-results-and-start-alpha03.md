# ssh alpha01 results and start alpha03

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_alpha01-results-and-start-alpha03_20260517T031816_result.json`
- **Structured JSON:** [`701bdb2fb8c672bd4524.json`](../../sessions/70/701bdb2fb8c672bd4524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 结果汇总

### 1. alpha=0.1 libero_spatial success_rate

**Overall: 56.20% (281/500)**

| Task | Success Rate |
|------|-------------|
| 0 | 84% (42/50) |
| 1 | 56% (28/50) |
| 2 | 66% (33/50) |
| 3 | 80% (40/50) |
| 4 | 34% (17/50) |
| 5 | 0% (0/50) |
| 6 | 86% (43/50) |
| 7 | 46% (23/50) |
| 8 | 56% (28/50) |
| 9 | 54% (27/50) |

### 2. alpha=0.3 启动状态
- **成功启动**，PID **872669**，tmux session `alpha_sweep_03`
- 运行命令：`eval_acib.py --scoring_alpha 0.3 --out_dir /root/autodl-tmp/v7_alpha_sweep/alpha_0.3`

### 3. alpha=0.0 状态
- **仍在运行**，PID 837180，已运行 ~21 分钟
- 评估全部 4 个 suite（spatial/object/goal/10），预计还需较长时间

### 4. GPU 进程状态

| GPU | PID | Task | Memory |
|-----|-----|------|--------|
| 0 | 837180 | alpha=0.0 (4 suites) | 5084 MiB |
| 1 | 872669 | alpha=0.3 (spatial) | 780 MiB (加载中) |

---
