# experiment exp 7b scorer ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_7b_scorer_ablation_20260520T112713_result.json`
- **Structured JSON:** [`fae13c78b99c521e3d88.json`](../../sessions/fa/fae13c78b99c521e3d88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并在 cuda:0 上运行。

**确认状态：**
- GPU 0: PID 316317, 4664MiB 占用, 51% util（Qwen2.5-1.5B Phase 1 正在提取 Pythia C4 depth 0 的 surprisal features，进度 ~35%）
- 1.5B scorer batch_size=8, 约 8-9 it/s → 每个 depth 625 batches ~75s，6 depths ~7.5min，两个 generator ~15min 完成 Phase 1
- Phase 2 (7B scorer) batch_size=4，约慢 3-4x，估计 ~45min
- Bootstrap CI 10k 次 × 5 pairs × 4 configs ~5min
- **总预估：~65-80min 完成**

**输出目录：**
- Features: `/root/autodl-tmp/gen-depth-contamination/data/exp_7b_scorer_ablation/{pythia_c4,olmo_c4}__{qwen1.5b,qwen7b}/features.csv`
- Results: `/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_ablation/all_results.json + summary.txt`
- Log: `/root/autodl-tmp/gen-depth-contamination/logs/exp_7b_scorer_ablation.log`

---
