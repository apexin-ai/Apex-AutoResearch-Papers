# ssh exp017 investigate and start

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp017_investigate_and_start_20260523T065425_result.json`
- **Structured JSON:** [`971d0537b9fce2e6c672.json`](../../sessions/97/971d0537b9fce2e6c672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查结果：

### 1. cuda:3 占用
两个 `test_dry.py` 进程占满 GPU 3：
- PID 308617: 73530 MiB
- PID 310192: 23482 MiB
- 总计 ~97 GB，与报告一致

这不是 exp-014 残留，而是 `test_dry.py` 测试脚本。**不属于明确可 kill 的范畴，需要你确认是否 kill。**

### 2. MCMC 参数确认
`run_exp017.py` 第 108 行：`num_warmup=2000, num_samples=4000, num_chains=4` — 参数正确。

### 3. 当前 GPU 分配
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | exp-014 (×2 instances) | Running |
| 1 | exp-015 | Running |
| 2 | exp-016 | Running |
| 3 | test_dry.py (×2) | 占满 97GB |

**需要你确认：是否 kill 掉 cuda:3 上的两个 `test_dry.py` 进程（PID 308617, 310192）以释放显存给 exp-017？**

---
