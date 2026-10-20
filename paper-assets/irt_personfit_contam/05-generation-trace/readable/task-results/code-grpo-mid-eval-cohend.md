# code grpo mid eval cohend

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-mid-eval-cohend_20260521T112250_result.json`
- **Structured JSON:** [`f92976323c50cc3eda98.json`](../../sessions/f9/f92976323c50cc3eda98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇总

### Task B: Cohen's d（完成）

| | lz\* (overall) | Cohen's d | 95% CI | n_items |
|---|---|---|---|---|
| Clean (n=10) | mean=8.684, sd=0.735 | — | — | 14042 |
| **Contam 15%** | 3.849 | **6.575** | [4.514, 15.199] | 14042 (seen=2106) |
| **Contam 50%** | 7.289 | **1.897** | [1.041, 4.923] | 14042 (seen=7021) |

两个 contam 条件的 effect size 都很大（远超 d=0.8 的 "large" 门槛）。contam_15 偏离 clean 均值 6.6 个标准差，contam_50 偏离 1.9 个标准差。n_items=14042 与 GRPO setup 一致。

结果已保存到 `/root/autodl-tmp/ctrl_contam_pilot/results/cohens_d_n10.json`。

### Task A: GRPO 中间 eval（阻塞 → 已修复）

**发现问题**：GRPO 训练在 step 2628/14042 处中止（进程不存在），`save_strategy="epoch"` 导致无任何 checkpoint 保存，训练进度全部丢失。

**已采取措施**：
1. 修改 `train_grpo.py`：`save_strategy="steps"`, `save_steps=3000`, `save_total_limit=3`
2. 在 cuda:0 上重启训练（PID 130586），日志 `grpo_run3.log`
3. wandb 不可用，当前用 `WANDB_MODE=disabled` 运行

**下一步**：第一个 checkpoint（step 3000）预计约 4-5 小时后可用，届时可在空闲 GPU 上跑 `eval_with_ht.py --stage grpo`。

---
