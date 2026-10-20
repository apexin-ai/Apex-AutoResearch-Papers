# analysis verify gpt2m config

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-gpt2m-config_20260525T215301_result.json`
- **Structured JSON:** [`563893cb23d45f32be9a.json`](../../sessions/56/563893cb23d45f32be9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已确认。汇总如下：

---

## 1. GPT-2-medium 实际配置

| 属性 | 值 |
|------|-----|
| **总参数量** | **354,823,168 (~354.8M)** |
| n_layer | 24 |
| n_head | 16 |
| n_embd | 1024 |
| vocab_size | 50257 |

论文写 "355M" 是合理的四舍五入，实际精确值 354.8M。

## 2. exp_020 (pure_collapse, r=0) 代数

**10 代训练**（gen_0 到 gen_10，共 11 个条目）。gen_0 是基线（预训练模型），gen_1~gen_10 是 10 轮递归训练。

## 3. 其他 GPT-2m 实验代数

| 实验 | condition | 结果文件代数 | checkpoints |
|------|-----------|-------------|-------------|
| pure_collapse_seed42 | r=0.0 | gen_0~gen_10 (**10代**) | gen_0~gen_10 |
| fixed_mix_r025_seed42 | r=0.25 | gen_0~gen_3 (**3代**) | gen_0~gen_3 |
| fixed_mix_r03_seed42 | r=0.30 | gen_0~gen_3 (**3代**) | gen_0~gen_3 |

注意：没有找到 exp_021/022c/023 对应的 adaptive 或 linear_increasing 实验结果，只有以上 3 个 condition。

## 4. 训练脚本默认配置（src/config.py）

| 超参 | 值 |
|------|-----|
| learning_rate | 5e-5 |
| batch_size | 8 |
| gradient_accumulation_steps | 4 (有效 batch=32) |
| warmup_ratio | 0.05 |
| num_epochs_per_gen | 1 |
| num_generations | **默认 10**（脚本 argparse 也是 `--generations` default=10）|
| temperature | 1.0 |
| top_k | 50 |
| num_synthetic_samples | 50,000 |
| max_length | 512 |

---
