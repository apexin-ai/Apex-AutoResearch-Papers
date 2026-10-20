# ops collect d093 results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_d093_results_20260520T192405_result.json`
- **Structured JSON:** [`646b2eba93fe22558dce.json`](../../sessions/64/646b2eba93fe22558dce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report.

---

## 实验 1: exp_expanded_downstream_eval

### 完成度矩阵

```
seed0: no_filter ✅  binary_ours ✅  graduated ✅
seed1: no_filter ✅  binary_ours ✅  graduated ⏳ (eval running, ~66% piqa)
seed2: no_filter ⏳  binary_ours ⏳  graduated ⏳ (未开始)
```

`exp_expanded_downstream_eval.py --num_seeds 3` 仍在 GPU 0 上运行，graduated_seed1 eval 进行中，seed2 全部待跑。

### 原始分数（所有 benchmark 使用 acc_norm 或 acc 视具体 benchmark）

| Model | PIQA | TruthfulQA_mc2 | WinoGrande | ARC-C (norm) |
|---|---|---|---|---|
| **Base** | 0.7579 | 0.4659 | 0.6456 | 0.5486 |
| no_filter seed0 | 0.7519 | 0.4224 | 0.6519 | 0.5128 |
| no_filter seed1 | 0.7508 | 0.4237 | 0.6456 | 0.5213 |
| binary_ours seed0 | 0.7530 | 0.4359 | 0.6385 | 0.5196 |
| binary_ours seed1 | 0.7524 | 0.4456 | 0.6425 | 0.5188 |
| graduated seed0 | 0.7514 | 0.4225 | 0.6488 | 0.5128 |

GSM8K 全部为 null（已确认跳过）。

### Mean ± Std 汇总（仅含已完成 seed）

| Benchmark | Base | no_filter (n=2) | binary_ours (n=2) | graduated (n=1) | binary-nf Δ |
|---|---|---|---|---|---|
| PIQA | 0.7579 | 0.7514±0.0008 | 0.7527±0.0004 | 0.7514 | +0.0013 |
| TruthfulQA | 0.4659 | 0.4230±0.0009 | 0.4408±0.0069 | 0.4225 | +0.0178 |
| WinoGrande | 0.6456 | 0.6488±0.0045 | 0.6405±0.0028 | 0.6488 | -0.0083 |
| ARC-C | 0.5486 | 0.5171±0.0060 | 0.5192±0.0006 | 0.5128 | +0.0021 |

注：graduated 仅 1 个 seed，无法算 std。binary-nf Δ = binary_ours mean - no_filter mean。

---

## 实验 2: exp_deberta_filtering_comparison

### 完成度

```
no_filter:        train ✅  eval ✅  (EXIT_CODE=0, 19:25 UTC)
obd_binary:       train ✅  eval ✅  (EXIT_CODE=0, 03:24 UTC)
deberta_binary:   train ✅  eval ✅  (EXIT_CODE=0, 03:24 UTC)
deberta_graduated: ❌ 目录不存在，未提交
```

### 结果

| Benchmark | no_filter | obd_binary | deberta_binary | obd-nf Δ | deb-nf Δ |
|---|---|---|---|---|---|
| MMLU | 0.5895 | 0.5880 | 0.5870 | -0.0015 | -0.0025 |
| HellaSwag (norm) | 0.6591 | 0.6599 | 0.6593 | +0.0008 | +0.0002 |
| ARC-C (norm) | 0.4352 | 0.4522 | 0.4471 | **+0.0170** | +0.0119 |

MMLU 子类别：

| Category | no_filter | obd_binary | deberta_binary |
|---|---|---|---|
| STEM | 0.5230 | 0.5249 | 0.5224 |
| Humanities | 0.5248 | 0.5248 | 0.5233 |
| Social Sciences | 0.6974 | 0.6929 | 0.6922 |
| Other | 0.6482 | 0.6440 | 0.6447 |

---

### 服务器状态

- GPU 0 (19.5G/24.6G, 100%): exp_expanded_downstream_eval 仍在运行
- GPU 1 (10.7G, 92%): sweep_r10_nofilter 在跑
- GPU 2-3 (10.7G each, 65-83%): torch compile_worker 进程活跃（可能是另一个实验）
- deberta_graduated 需要单独提交

---
