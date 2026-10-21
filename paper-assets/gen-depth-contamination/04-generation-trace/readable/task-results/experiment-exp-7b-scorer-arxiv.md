# experiment exp 7b scorer arxiv

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_7b_scorer_arxiv_20260520T122956_result.json`
- **Structured JSON:** [`0145569d6a5ca6378306.json`](../../sessions/01/0145569d6a5ca6378306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并运行中：

- **PID**: 320673
- **GPU**: cuda:1 (RTX 4090D, 3595 MiB 已占用)
- **状态**: Phase 1 进行中，1.5B scorer 已加载 (1.5B params)，正在提取 `pythia_arxiv` depth 0 的 surprisal 特征（~6 it/s，batch_size=8）
- **数据源**: Pythia-1.4B arXiv (exp_025_pythia_arxiv) + OLMo-1B arXiv (exp_arXiv_olmo)，各 6 depths × 2200 samples
- **日志**: `/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_arxiv.log`
- **Registry**: `exp_7b_scorer_arxiv` → RUNNING, parent=exp_024_arxiv_domain

Pipeline 流程：Phase 1 (1.5B scorer, 2 generators) → Phase 2 (7B scorer, 2 generators, batch_size=4) → Phase 3 (summary + K* 对比)。预计 Phase 2 显存会升到 ~14GB，在 24GB 卡上可行。

---
