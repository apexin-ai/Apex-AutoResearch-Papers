# ssh exp015 diagnose stuck

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp015_diagnose_stuck_20260523T071908_result.json`
- **Structured JSON:** [`247591744e3252755cad.json`](../../sessions/24/247591744e3252755cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：实验没有卡住，正在正常运行。**

诊断摘要：

| 项目 | 结果 |
|------|------|
| PID 291457 | bash 父 shell，State=S（sleeping）— 正常等待子进程 |
| PID 291466 | python 实际进程，**State=R（running）**，RSS=7.8GB，1112 线程 |
| GPU 1 | PID 291466 占用 73562 MiB — 正常 |
| 进度 | **9/20 seeds 已完成**（seed 0-8），当前正在跑 seed=9 |
| 日志 | `/root/runs/gated_mfrm_judge_bias/exp-015.log`，最后输出 `[10/20] seed=9` |

你之前看到 CPU=0.0% 是因为查的是 PID 291457（bash shell），而实际 python 进程是 PID 291466。每个 seed 两种方法各需 ~240s + ~340s ≈ 10 分钟，20 seeds 总计约 3.3 小时，目前运行一半左右，预计还需 ~1.8h 完成。

**不需要 kill，让它继续跑。**

---
