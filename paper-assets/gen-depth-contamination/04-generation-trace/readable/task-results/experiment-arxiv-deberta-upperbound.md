# experiment arxiv deberta upperbound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_arxiv-deberta-upperbound_20260520T031015_result.json`
- **Structured JSON:** [`94d9b1ea5753e5edfd30.json`](../../sessions/94/94d9b1ea5753e5edfd30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，已加载 13200 samples，正在 tokenize。

**实验信息汇总：**

| 项 | 值 |
|---|---|
| exp_id | `exp_deberta_arxiv_qwen1b5` |
| PID | 276481 |
| GPU | cuda:1 (RTX 4090 D) |
| 脚本 | `scripts/run_deberta_arxiv.py` |
| 日志 | `~/runs/gen-depth-contamination/exp_deberta_arxiv_qwen1b5.log` |
| 数据 | 13200 samples (2200 docs × 6 depths), arXiv domain, Qwen-1.5B scorer |
| 超参 | 5-fold GroupKFold, 3 epochs, BS=16, grad_accum=2, LR=2e-5, N_BOOT=10000, θ=0.60 |
| 输出 | `results/exp_deberta_arxiv/arxiv_qwen1b5.json` |

**与 wiki 版本的差异：**
- `EXPERIMENTS` 指向 `data/exp_024_arxiv/`
- `N_BOOT` 从 1000 改为 10000（更精确的 CI 估计）
- `load_obd` 通过 `OBD_MAP` 加载 `results/exp_024_arxiv/pairwise_auc.json` 作为 baseline
- 输出到 `results/exp_deberta_arxiv/`

**预计耗时：** wiki 版本 5 个实验跑完的时间参考，单个 arXiv 实验（13200 samples × 5 folds × 3 epochs + 10000 bootstrap）预计 30-60 分钟。

---
