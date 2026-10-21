# smollm3_3b_wiki_a100_s42_v3 状态检查

**检查时间**: 2026-05-19 13:17 UTC (服务器时间)
**服务器**: westd-19828, GPU cuda:1 (NVIDIA RTX PRO 6000 Black)

## 状态: 正在运行

- **进程**: PID 408261 (bash wrapper) → 408265 (timeout) → 408266 (python, GPU 进程)
- **GPU 使用**: cuda:1, 64408MiB / 97887MiB, GPU-Util 99%
- **tmux session**: `smollm3_3b_wiki_a100_s42_v3` (创建于 08:24:31)
- **启动时间**: 2026-05-19 08:24

## 实验配置

| 参数 | 值 |
|------|-----|
| model | SmolLM3-3B-Base |
| seed | 42 |
| data | wikitext103_5k |
| steps_per_gen | 5000 |
| num_generations | 10 |
| synthetic_ratio | 1.0 |
| precision | fp32 (bf16=false) |
| lr | 5e-05 |
| batch_size | 4 |
| output_dir | results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3 |

## 进度

| Generation | 状态 | 完成时间 |
|-----------|------|---------|
| gen_0 (baseline) | 完成 | ~09:01 |
| gen_1 | 完成 (含 synthetic_data, trainer, checkpoint) | ~10:49 |
| gen_2 | 完成 (含 synthetic_data, trainer, checkpoint) | ~12:36 |
| gen_3 | **训练中** step ~421/5000 @ 1.18 it/s | - |
| gen_4 ~ gen_10 | 待运行 | - |

- **all_metrics.json**: 尚未生成（实验未完成）
- **每 gen 周期**: ~107 min (含 synthetic data 生成 + 训练 + eval)
- **训练速度**: 1.18 it/s (稳定)
- **当前 gen_3 训练 loss**: 0.5811 @ step 400

## 预估完成时间

- gen_3 训练剩余: ~65 min + eval/transition: ~35 min
- gen_4 ~ gen_10: 7 × 107 min ≈ 749 min
- **总剩余: ~14 小时, 预计完成 2026-05-20 ~03:30 UTC**

## 错误/警告

- 大量 `right-padding was detected` 警告 (transformers, 不影响训练)
- 无错误
- 同一 GPU 0 上另有一个 python 进程 (PID 407864, 62670MiB)，互不干扰
