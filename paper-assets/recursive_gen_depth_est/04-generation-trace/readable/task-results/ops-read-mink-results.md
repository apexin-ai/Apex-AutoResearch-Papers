# ops read mink results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read_mink_results_20260518T183528_result.json`
- **Structured JSON:** [`f89e2ce64fcb38521eb6.json`](../../sessions/f8/f89e2ce64fcb38521eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**Min-K% Prob baseline 正在运行中**（PID 994671，启动于 02:14 UTC，已跑 ~22 分钟）。

**进度**：
- 已完成 2/9 cells 的 logprob 计算：
  - `pythia_nucleus` — 3 个 K 值的 score 已保存（K=10/20/30）
  - `pythia_temp09` — 3 个 K 值的 score 已保存
- 当前正在处理第 3 个 cell：`pythia_topk50`
- 剩余 6 个 cells：`olmo_nucleus`, `olmo_temp09`, `olmo_topk50`, `gpt2xl_nucleus`, `gpt2xl_temp09`, `gpt2xl_topk50`

**产出**：
- 6 个 `.npy` score 文件（每个 ~156KB，含 20000 条 passage 的 Min-K% score）
- 无 `mink_prob_results.json`（分类评估尚未运行，应在所有 cells logprob 计算完成后执行）
- 无 error/traceback

**预估**：每个 cell ~8 分钟（417 batches × ~1.13 it/s），9 cells 总计 ~72 分钟。已跑 22 分钟完成 2 个，预计还需 ~50 分钟完成全部 logprob + 后续 5-fold CV 分类评估。

**其他新 .json 文件**（比 table2_rerun_5foldcv.json 更新）：
- `results/qwen25_14b_scale/summary.json`
- `results/reviewer_metrics/pipeline_conditional_decomp.json`
- `results/wild_data_calibration/threshold_calibration_results.json`

---
