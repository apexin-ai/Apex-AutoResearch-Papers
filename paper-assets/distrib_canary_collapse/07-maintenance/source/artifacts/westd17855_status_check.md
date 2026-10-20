# westd-17855 实验状态检查 (2026-05-19 13:12 UTC+8)

## GPU 状态

| GPU | 型号 | 显存占用 | GPU-Util | 进程 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 Black | 71019/97887 MiB | 93% | PID 29033 (scale_69b_a100_s42, pythia-6.9b) |
| 1 | RTX PRO 6000 Black | 34801/97887 MiB | 80% | PID 74460 (qwen35_08b_wiki_a100_s42_v2) |
| 2 | RTX PRO 6000 Black | 0 MiB | 0% | - |
| 3 | RTX PRO 6000 Black | 0 MiB | 0% | - |
| 4 | RTX PRO 6000 Black | 0 MiB | 0% | - |
| 5 | RTX PRO 6000 Black | 0 MiB | 0% | - |

## 各实验状态

| exp_id | 状态 | PID | Exit Code | 完成标志 | Gen 数 | 输出目录 |
|--------|------|-----|-----------|---------|--------|---------|
| interv_pred_a075_s42_fp32_v4 | **已完成** | - | 0 | all_metrics.json (12:39) | 11/11 (gen_0-10) | `results/intervention/interv_pred_fp32_v4_d080/` |
| alpha_sweep_a060_s42_fp32_v3 | **已完成** | - | 0 | all_metrics.json (12:34) | 11/11 (gen_0-10) | `results/alpha_sweep/a060_s42_fp32_v3_d080/` |
| alpha_sweep_a005_s42_v3 | **已完成** | - | 0 | all_metrics.json (12:38) | 11/11 (gen_0-10) | `results/alpha_sweep/a005_s42_fp32_v3_d080/` |
| qwen35_08b_wiki_a100_s42_v2 | **运行中** | 74460 | - | - | gen_0-4 完成, gen_5 训练中 (1183/5000, 23%) | `results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/` |
| smollm3_3b_wiki_a100_s42_v3 | **未找到** | - | - | - | - | 无任何痕迹 |

## 已完成实验关键指标摘要

### interv_pred_a075_s42_fp32_v4 (intervention, alpha=0.75)
- Intervention 在 gen 1 触发，gen 2 起 effective_alpha=0.0
- 最终 (gen 10): ppl=20.81, entropy=3.05, eff_rank=44.8, mauve=0.031
- 干预后 ppl 稳定在 ~20.7-21.0，无进一步退化

### alpha_sweep_a060_s42_fp32_v3 (alpha=0.60, no intervention)
- 未触发 intervention，全程 alpha=0.60
- 最终 (gen 10): ppl=45.41, entropy=2.48, eff_rank=69.3, mauve=0.023
- 明显的 collapse 趋势: ppl 从 26.9 (gen0) 持续升至 45.4 (gen10)，distinct_3 从 0.83 降至 0.54

### alpha_sweep_a005_s42_v3 (alpha=0.05, no intervention)
- 未触发 intervention，全程 alpha=0.05
- 最终 (gen 10): ppl=20.81, entropy=3.04, eff_rank=45.3, mauve=0.023
- 基本稳定: ppl 从 26.9 (gen0) 降至 ~20.8 (gen1 起)，之后保持

## 需要注意的问题

1. **smollm3_3b_wiki_a100_s42_v3 完全缺失**: 服务器上没有任何该实验的痕迹（无进程、无 tmux session、无 exit file、无输出目录、无 log 文件）。可能从未成功提交到此服务器，需要检查 registry 记录和提交历史。

2. **qwen35_08b 预计完成时间**: 已运行约 4h43m 完成 ~52% (5.23/10 gen)。按当前速率 (~1.85 it/s)，预计还需 ~4-5 小时（约 17:30-18:00 本地时间完成）。

3. **额外运行中的实验**: GPU 0 上有 `scale_69b_a100_s42`（pythia-6.9b, seed 42, 5000 steps/gen）从 02:03 起运行，不在本次检查列表中，但占用 71GB 显存和 93% GPU。

4. **GPU 2-5 空闲**: 4 张卡完全空闲，可以用于重新提交 smollm3 或其他实验。
