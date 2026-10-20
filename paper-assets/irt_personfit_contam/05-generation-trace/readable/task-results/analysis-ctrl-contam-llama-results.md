# analysis ctrl contam llama results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ctrl-contam-llama-results_20260520T210404_result.json`
- **Structured JSON:** [`bd9f8e0d688eba4c3f69.json`](../../sessions/bd/bd9f8e0d688eba4c3f69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有完整的情况了。以下是结构化报告：

---

## Llama Ctrl-Contam 实验状态报告（2026-05-21 05:07 UTC+8）

### 1. 训练状态：三个条件全部仍在训练中

| 条件 | GPU | 当前步数 | 总步数 | 进度 | 预计完成 |
|------|-----|---------|-------|------|---------|
| **clean** | cuda:0 (RTX PRO 6000, 97%) | 527 | 939 | 56% | ~05:15 |
| **contam_15** | cuda:1 (79%) | ~198+ | 1335 | ~15% | ~05:28 |
| **contam_50** | cuda:2 (94%) | ~180+ | 2256 | ~8% | ~05:50 |

- 3块 GPU 均在活跃训练（GPU util 79-97%）
- GPU 3 空闲
- 训练配置：QLoRA r=16/alpha=32, 3 epochs, batch=4, grad_accum=4, lr=2e-4, bf16

### 2. Clean 训练 Loss 曲线（唯一有 loss 数据的条件）

| epoch | loss | mean_token_acc | 备注 |
|-------|------|---------------|------|
| 0.032 | 2.097 | 0.537 | 起始 |
| 0.256 | 1.657 | 0.595 | warmup 阶段 |
| 0.512 | 1.490 | 0.622 | 收敛中 |
| 0.736 | 1.461 | 0.614 | |
| 0.992 | 1.450 | 0.614 | epoch 1 结束，已保存 checkpoint-313 |

Loss 正常下降并收敛，无异常。

### 3. Checkpoints

- `clean/checkpoint-313/` — epoch 1 checkpoint 已保存（adapter_model.safetensors 27MB）
- `contam_15/` — **空**，第一个 epoch checkpoint 在 step 445
- `contam_50/` — **空**，第一个 epoch checkpoint 在 step 752

### 4. Eval 状态

**尚无任何 eval 结果。** `results/` 目录为空。

`train.py` 不包含自动 eval。训练完成后需要手动运行 `eval_lz.py`：
```bash
python eval_lz.py --condition clean --gpu 0
python eval_lz.py --condition contam_15 --gpu 1
python eval_lz.py --condition contam_50 --gpu 2
```
输出指标：theta_mle, lz_star (overall/seen/unseen), accuracy (overall/seen/unseen)

### 5. Qwen Pilot 参考数据（已完成，用于后续对比）

| 条件 | accuracy | theta_mle | lz_star | lz_fixed | d_free | d_fixed |
|------|----------|-----------|---------|----------|--------|---------|
| **clean (n=3 mean)** | 0.679 | -0.097 | **7.345** (±1.214) | 7.343 | — | — |
| **contam_15** | 0.731 | 0.197 | **3.005** | 10.022 | -3.576 | 2.950 |
| **contam_50** | 0.764 | 0.370 | **5.448** | 15.708 | -1.563 | 9.212 |

Qwen pilot 关键发现：
- lz_star_seen：contam_15=0.446, contam_50=3.648
- lz_star_unseen：contam_15=3.132, contam_50=4.554
- memorization_fraction：contam_15=38.4%, contam_50=29.3%

### 6. 异常/问题

- **contam_15 和 contam_50 的 tee 日志未正常写入 loss 数据**——训练在 tmux 终端里跑，progress bar 输出到终端，loss metrics 可能因缓冲没有被 flush 到日志文件
- 之前在 `/root/runs/` 下有一组失败的 nohup 启动记录（GPU 都设成了 0），日志只跑了 ~50 步就停了——当前运行的是重新启动的正确版本（各自分配到 GPU 0/1/2）
- 训练本身没有报错，GPU 温度和功耗正常

### 7. 后续行动

1. 等待训练完成（clean ~05:15, contam_15 ~05:28, contam_50 ~05:50）
2. 训练完成后运行 `eval_lz.py` 计算 lz* 指标
3. 与 Qwen pilot 对比分析

---
