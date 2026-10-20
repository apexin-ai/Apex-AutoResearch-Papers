# ops gpu check and script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_script_20260515T052241_result.json`
- **Structured JSON:** [`46b131524bd82cc9d4fb.json`](../../sessions/46/46b131524bd82cc9d4fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. GPU 状态

| GPU | Utilization | Memory Used | Memory Total |
|-----|------------|-------------|--------------|
| 0 | 94% | 14,391 MiB | 97,887 MiB (~96GB) |
| 1 | 43% | 14,391 MiB | 97,887 MiB (~96GB) |

两张卡都在使用中，显存各占 ~14.4GB / 96GB。

### 2. 训练进程

3 个 `iterative_train.py` 进程在跑：

| 任务 | GPU | 参数 | 状态 |
|------|-----|------|------|
| `plan_006_s42` | GPU 0 | `--synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000` (wikitext103 全集) | 运行中，CPU 188% |
| `alpha_sweep_a050_s42` | GPU 1 | `--synthetic_ratio 0.50 --num_generations 10 --steps_per_gen 5000` (wikitext103_5k) | 运行中，CPU 208% |
| `alpha_sweep_a000_s42` | GPU 0 (tmux) | `--synthetic_ratio 0.0 --num_generations 10 --steps_per_gen 5000` (wikitext103_5k) | tmux session 存在，可能已完成或排队 |

另外 `analyze_alpha_sweep.py` 也正在 GPU 上执行（PID 87799, CPU 217%）。

### 3. gen_dose_response.py

**分析脚本，不是训练脚本。** 它从 `results/alpha_sweep/` 和 `results/mvp/` 目录读取各 generation 的 metrics（token_entropy, ece, perplexity, distinct_1/2/3），汇总成 CSV 用于绘制 dose-response 曲线（不同 synthetic_ratio α 值对指标的影响）。无命令行参数，直接运行即可。

---
