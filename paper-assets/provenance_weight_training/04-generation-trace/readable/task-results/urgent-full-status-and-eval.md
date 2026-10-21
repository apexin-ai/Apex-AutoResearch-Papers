# urgent full status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_full_status_and_eval_20260523T084611_result.json`
- **Structured JSON:** [`f72c558f4bab9064ebbc.json`](../../sessions/f7/f72c558f4bab9064ebbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验的 12 个 eval 均已完成，无需启动新任务。GPU 当前空闲。

## 完整结果表

| 实验 | holdout_ppl | owt_ppl | wiki_ppl |
|------|-------------|---------|----------|
| rho03_adaptive_seed456_r2 | 17.424 | 18.115 | 15.161 |
| rho03_uniform_seed456 | 17.419 | 18.109 | 15.168 |
| bs8_nmin4_adaptive_seed123 | 17.631 | 18.338 | 15.353 |
| bs8_nmin4_uniform_seed123 | 17.687 | 18.370 | 15.385 |

**关键观察：**
- rho03 配置（bs4）全面优于 bs8_nmin4 配置，三个数据集差距一致（~0.2 ppl）
- adaptive vs uniform 差异极小：rho03 组差异 < 0.01 ppl，bs8 组 adaptive 略优（~0.05 ppl）
- GPU 全部空闲，无进程在跑

---
