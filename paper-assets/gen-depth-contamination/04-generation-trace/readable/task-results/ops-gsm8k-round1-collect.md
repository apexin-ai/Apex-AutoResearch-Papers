# ops gsm8k round1 collect

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k_round1_collect_20260520T220544_result.json`
- **Structured JSON:** [`1f8da48943d1dda7ae8b.json`](../../sessions/1f/1f8da48943d1dda7ae8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cuda:1,2,3 Round 1 状态: 完成

三个 seed0 GSM8K 补跑全部完成（05:46-06:01 UTC）。

**GSM8K 结果:**
| Config | GSM8K |
|---|---|
| no_filter_seed0 | 0.5610 |
| binary_ours_seed0 | 0.5861 |
| graduated_seed0 | 0.5572 |

## cuda:0 Serial 状态: 进行中

当前任务: **no_filter_seed1** 重训练（训练阶段，`no_filter_seed1_train/` 目录已创建）
- GPU 利用率 83%, 显存 8116/24564 MiB
- cmdline: `python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 1 --num_seeds 1 --strategy no_filter --skip_base`
- 完成后还需补: **binary_ours_seed1**, **base_model**

## 完整 GSM8K 汇总

| Config | GSM8K | 状态 |
|---|---|---|
| base_model | null | 待补 |
| no_filter_seed0 | **0.5610** | 完成 |
| no_filter_seed1 | null | **cuda:0 训练中** |
| no_filter_seed2 | **0.5671** | 完成 |
| binary_ours_seed0 | **0.5861** | 完成 |
| binary_ours_seed1 | null | 待补 |
| binary_ours_seed2 | **0.5853** | 完成 |
| graduated_seed0 | **0.5572** | 完成 |
| graduated_seed1 | **0.5618** | 完成 |
| graduated_seed2 | **0.5648** | 完成 |

**仍缺 3 个**: base_model, no_filter_seed1, binary_ours_seed1。cuda:0 正在跑 no_filter_seed1（训练+eval 约 45min），之后还需串行跑 binary_ours_seed1。base_model 的 GSM8K 需要单独补。

## 完整 5-benchmark 数据（已完成的文件）

| Config | PIQA | TruthfulQA | WinoGrande | ARC-C | GSM8K |
|---|---|---|---|---|---|
| base_model | 0.7579 | 0.4659 | 0.6456 | 0.5486 | - |
| no_filter_s0 | 0.7519 | 0.4224 | 0.6519 | 0.5128 | 0.5610 |
| no_filter_s1 | 0.7508 | 0.4237 | 0.6456 | 0.5213 | - |
| no_filter_s2 | 0.7497 | 0.4277 | 0.6480 | 0.5239 | 0.5671 |
| binary_ours_s0 | 0.7530 | 0.4359 | 0.6385 | 0.5196 | 0.5861 |
| binary_ours_s1 | 0.7524 | 0.4456 | 0.6425 | 0.5188 | - |
| binary_ours_s2 | 0.7530 | 0.4378 | 0.6409 | 0.5128 | 0.5853 |
| graduated_s0 | 0.7514 | 0.4225 | 0.6488 | 0.5128 | 0.5572 |
| graduated_s1 | 0.7508 | 0.4234 | 0.6440 | 0.5230 | 0.5618 |
| graduated_s2 | 0.7492 | 0.4275 | 0.6456 | 0.5213 | 0.5648 |

---
