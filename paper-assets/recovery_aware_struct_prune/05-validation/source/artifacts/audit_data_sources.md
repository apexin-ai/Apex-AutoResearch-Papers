# 数据源审计目录

采集自：westd-32935（主服务器，161 个 JSON）+ westb-23072（补充，100 个 JSON）
日期：2026-05-25
项目：recovery_aware_struct_prune

---

## 1. Results JSON 文件清单（按论文用途分类）

### 1.1 主表 GSM8K (n=1319, greedy) — 7B & 1.5B

| 文件路径 (server:dir/file) | experiment_id | accuracy | n_correct/n_total |
|---|---|---|---|
| westd:autodl/results/eval_grpo_unpruned_v2_step100.json | grpo_unpruned_v2 | 0.8127 | 1072/1319 |
| westd:autodl/results/eval_grpo_unpruned_v2_step90.json | grpo_unpruned_v2 step90 | 0.8059 | - |
| westd:autodl/results/eval_unstructured_20_n1319.json (westb) | unstructured_20 | 0.8787 | - |
| westd:autodl/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json | cka_only_15_v2 | 0.7309 | - |
| westd:autodl/results/eval_gsm8k_grpo_cka_only_15_seed123_n1319.json | s123 | 0.7309 | - |
| westd:autodl/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json | s456 | 0.7210 | - |
| westd:autodl/results/eval_gsm8k_sft_cka_only_15_n1319.json | sft_cka15 | 0.7218 | - |
| westd:autodl/results/eval_gsm8k_grpo_cka_only_20_seed456_n1319.json | cka20_s456 | 0.6459 | - |
| westd:autodl/results/eval_gsm8k_grpo_cka_only_20_extended_300.json | cka20_ext300 | 0.6437 | 849/1319 |
| westd:autodl/results/eval_sft_cka_only_20_n1319.json (= eval_gsm8k_sft_cka_only_20_n1319) | sft_cka_only_20 | 0.6391 | 843/1319 |
| westd:autodl/results/eval_gsm8k_grpo_standard_15_v2_n1319.json | std15_v2 | 0.6611 | - |
| westd:autodl/results/eval_gsm8k_grpo_standard_15_seed123_n1319.json | std15_s123 | 0.6513 | - |
| westd:autodl/results/eval_gsm8k_grpo_standard_15_seed456_n1319.json | std15_s456 | 0.6543 | - |
| westd:autodl/results/eval_gsm8k_sft_standard_15_n1319.json | sft_std15 | 0.6649 | - |
| westd:autodl/results/eval_gsm8k_sft_rasp_20_n1319.json | sft_rasp_20 | 0.6149 | 812/1319 |
| westd:autodl/results/eval_gsm8k_grpo_rasp_20_fair.json | rasp_20_fair | 0.6088 | 803/1319 |
| westd:autodl/results/eval_gsm8k_grpo_standard_20_fair_v2.json | std20_fair_v2 | 0.5944 | 784/1319 |
| westd:autodl/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json | std20_s123 | 0.5989 | - |
| westd:autodl/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json | std20_s456 | 0.6020 | - |
| westd:autodl/results/eval_gsm8k_grpo_standard_20_extended_300.json | std20_ext300 | 0.5929 | - |
| westd:autodl/results/eval_gsm8k_sft_standard_20_n1319.json | sft_std20 | 0.5921 | - |
| westd:autodl/results/eval_grpo_standard_25_n1319.json | grpo_std25 | 0.5110 | 674/1319 |
| westd:autodl/results/eval_sft_standard_20_full_westd.json | sft_std20_full | 0.5929 | - |
| westd:autodl/results/eval_sft_rasp_20_full_westd.json | sft_rasp_20_full | 0.6149 | - |
| westd:autodl/results/eval_gsm8k_grpo_random_20_seed123.json | random_20 s123 | 0.5125 | - |
| westd:autodl/results/eval_gsm8k_grpo_random_20_seed123_v2.json | random_20 s123 v2 | 0.5072 | - |
| westb:autodl/results/eval_gsm8k_grpo_random_20_seed456.json | random_20 s456 | 0.5087 | - |
| westd:autodl/results/gsm8k_grpo_shortgpt_20.json | grpo_shortgpt_20 | 0.4337 | 572/1319 |
| westd:autodl/results/gsm8k_sft_shortgpt_20.json | sft_shortgpt_20 | 0.4473 (partial 999/1319) | - |
| westb:autodl/results/eval_gsm8k_dense_unpruned_n1319.json | dense_unpruned | 0.9083 | - |
| **1.5B family (westb)** | | | |
| westb:autodl/results/eval_gsm8k_sft_cka_only_20_1p5b.json | sft_cka_only_20_1p5b | 0.3563 | 470/1319 |
| westb:autodl/results/eval_gsm8k_sft_standard_20_1p5b.json | sft_std_20_1p5b | 0.2290 | 302/1319 |
| westb:autodl/results/eval_gsm8k_sft_rasp_20_1p5b.json | sft_rasp_20_1p5b | 0.2691 | 355/1319 |
| westb:autodl/results/eval_gsm8k_grpo_cka_only_20_1p5b.json | grpo_cka_only_20_1p5b | 0.3548 | 468/1319 |
| westb:autodl/results/eval_gsm8k_grpo_standard_20_1p5b.json | grpo_std_20_1p5b | 0.2229 | 294/1319 |
| westb:autodl/results/eval_gsm8k_grpo_rasp_20_1p5b.json | grpo_rasp_20_1p5b | 0.2616 | 345/1319 |

### 1.2 主表 MATH-500 (n=500, 7B)

| 文件 | exp_id | accuracy |
|---|---|---|
| westd:autodl/results/math500_dense_unpruned.json | dense_unpruned | 0.736 |
| westd:autodl/results/math500_grpo_unpruned.json | grpo_unpruned | 0.690 |
| westd:autodl/results/eval_math500_grpo_cka_only_20_2048_v2.json | cka_20_v2 | 0.274 |
| westd:autodl/results/math500_grpo_cka_only_20_2048.json | grpo_cka_20 | 0.292 |
| westd:autodl/results/math500_sft_cka_only_20_v4.json | sft_cka_20 | 0.290 |
| westd:autodl/results/eval_math500_sft_cka_only_20.json | sft_cka_20 (alt) | 0.268 |
| westd:autodl/results/eval_math500_sft_cka_only_25_fixed.json | sft_cka_25 | 0.188 |
| westd:autodl/results/eval_math500_grpo_cka_only_25_fixed.json | grpo_cka_25 | 0.176 |
| westd:autodl/results/eval_math500_grpo_standard_20_fair_fixed.json | grpo_std_20_fixed | 0.270 |
| westd:autodl/results/eval_math500_sft_standard_20_fixed_v4.json | sft_std_20_fixed | 0.256 |
| westd:autodl/results/math500_sft_standard_20_2048_v2.json | sft_std_20 | 0.258 |
| westd:autodl/results/eval_math500_sft_standard_25_fixed_v2.json | sft_std_25 | 0.154 |
| westd:autodl/results/math500_grpo_standard_20_fair_v2.json | grpo_std_20_fair | 0.264 |
| westd:autodl/results/eval_math500_grpo_random_20_v2.json | grpo_random_20 | 0.134 |
| westd:autodl/results/eval_math500_sft_random_20_v3.json | sft_random_20 | 0.144 |
| westd:autodl/results/eval_math500_sft_rasp_20.json | sft_rasp_20 | 0.242 |
| westd:autodl/results/math500_sft_rasp_20_2048.json | sft_rasp_20_2048 | 0.226 |
| westd:autodl/results/math500_grpo_rasp_20_fair.json | grpo_rasp_20_fair | 0.240 |
| **Alpha ablation MATH-500** | | |
| westd:autodl/results/eval_math500_sft_rasp_alpha0p5_20_fixed.json | sft α=0.5 | 0.268 |
| westd:autodl/results/eval_math500_sft_rasp_alpha1p0_20_fixed.json | sft α=1.0 | 0.216 |
| westd:autodl/results/eval_math500_sft_rasp_alpha2p0_20_fixed.json | sft α=2.0 | 0.256 |
| westd:autodl/results/eval_math500_sft_rasp_alpha4p0_20_fixed.json | sft α=4.0 | 0.278 |
| westd:autodl/results/eval_math500_grpo_rasp_alpha1p0_20_fixed.json | grpo α=1.0 | 0.230 |
| westd:autodl/results/eval_math500_grpo_rasp_alpha2p0_20_fixed.json | grpo α=2.0 | 0.274 |
| westd:autodl/results/eval_math500_grpo_rasp_alpha4p0_20_fixed.json | grpo α=4.0 | 0.272 |
| westd:autodl/results/eval_math500_grpo_rasp_alpha3p0_20.json | grpo α=3.0 | 0.228 |
| westd:autodl/results/eval_math500_sft_rasp_alpha3p0_20.json | sft α=3.0 | 0.232 |
| **MATH-500 1.5B (westb)** | | |
| westb:autodl/results/eval_math500_sft_cka_only_20_1p5b.json | 1p5b_cka | 0.106 |
| westb:autodl/results/eval_math500_sft_rasp_20_1p5b.json | 1p5b_rasp | 0.062 |
| westb:autodl/results/eval_math500_sft_standard_20_1p5b.json | 1p5b_std | 0.054 |

### 1.3 主表 HumanEval (n=164, pass@1)

| 文件 | pass@1 | n_correct |
|---|---|---|
| westd:autodl/results/eval_humaneval_unpruned_2048.json | 0.4512 | 74/164 |
| westd:autodl/results/eval_humaneval_unpruned.json | 0.0183 | 3/164 (短 max_new_tokens) |
| westd:autodl/results/humaneval_grpo_cka_only_20_1p5b_2048.json | 0.2012 | 33/164 |
| westd:autodl/results/humaneval_sft_cka_only_20_2048_v2.json | 0.2012 | 33/164 |
| westd:autodl/results/humaneval_sft_standard_20_2048_v3.json | 0.1341 | 22/164 |
| westd:autodl/results/humaneval_grpo_standard_20_fair_2048_v3.json | 0.1098 | 18/164 |
| westd:autodl/results/humaneval_sft_rasp_20_2048_v2.json | 0.1037 | 17/164 |
| westd:autodl/results/humaneval_grpo_rasp_20_fair_2048.json | 0.1098 | 18/164 |
| westd:autodl/results/humaneval_grpo_cka_only_20_2048.json | 0.2012 | 33/164 |
| westd:autodl/results/humaneval_sft_cka_only_20_1p5b_2048.json | 0.0061 | 1/164 |
| westb:autodl/results/humaneval_sft_standard_20_1p5b_2048.json | 0.0061 | 1/164 |
| westd:autodl/results/eval_humaneval_sft_standard_25.json | 0.0183 | - |

### 1.4 主表 MBPP (n=374, pass@1)

| 文件 | pass@1 | n_correct |
|---|---|---|
| westd:autodl/results/eval_mbpp_dense_unpruned.json | 0.5348 | - |
| westd:autodl/results/mbpp_sft_cka_only_20.json | 0.1283 | 48/374 |
| westd:autodl/results/eval_mbpp_grpo_rasp_20.json | 0.1310 | - |
| westd:autodl/results/eval_mbpp_grpo_standard_20.json | 0.1310 | - |
| westd:autodl/results/eval_mbpp_sft_rasp_20.json | 0.1176 | - |
| westd:autodl/results/eval_mbpp_sft_standard_20.json | 0.1203 | - |
| westd:autodl/results/mbpp_grpo_shortgpt_20.json | 0.1444 | 54/374 |
| westd:autodl/results/mbpp_sft_shortgpt_20.json | 0.1043 | 39/374 |
| westb:autodl/results/eval_mbpp_sft_standard_20_1p5b.json | 0.0080 | - |
| westb:autodl/results/eval_mbpp_sft_cka_only_20_1p5b.json | 0.0 | - |

### 1.5 Alpha ablation GSM8K (n=100 for n1.0, others varied)

| 文件 | α | accuracy |
|---|---|---|
| westd:root/results/alpha_ablation/eval_prune_alpha_0.0.json | 0.0 | 0.30 |
| westd:root/results/alpha_ablation/eval_prune_alpha_0.5.json | 0.5 | 0.25 |
| westd:root/results/alpha_ablation/eval_prune_alpha_1.0.json | 1.0 | 0.27 |
| westd:root/results/alpha_ablation/eval_prune_alpha_2.0.json | 2.0 | 0.29 |
| westd:root/results/alpha_ablation/eval_prune_alpha_4.0.json | 4.0 | 0.40 |
| westd:autodl/results/eval_gsm8k_grpo_alpha4_20_v3.json | 4.0 (grpo full) | 0.6277 |
| westd:autodl/results/eval_gsm8k_sft_alpha4_20_v5.json | 4.0 (sft full) | 0.6194 |
| westd:autodl/results/eval_gsm8k_grpo_rasp_alpha3p0_20.json | 3.0 (grpo) | 0.6346 |
| westd:root/results/eval_sft_alpha_0.0_n100.json | 0.0 | 0.64 |
| westd:root/results/eval_sft_alpha_1.0_n100.json | 1.0 | 0.57 |
| westd:root/results/eval_sft_alpha_2.0_n100.json | 2.0 | 0.62 |
| westd:root/results/eval_alpha_4.0_greedy.json | 4.0 | 0.62 |

### 1.6 Floor ablation GSM8K

| 文件 | floor_ratio | accuracy |
|---|---|---|
| westd:autodl/results/eval_gsm8k_floor_0.3.json | 0.3 | 0.6505 |
| westd:autodl/results/eval_gsm8k_floor_0.5.json | 0.5 | 0.6171 |
| westd:autodl/results/eval_gsm8k_floor_0.6.json | 0.6 | 0.6202 |
| (默认 0.4) = eval_gsm8k_grpo_cka_only_20_extended_300 | 0.4 | 0.6437 |

### 1.7 Qwen2.5-Math-7B 跨模型验证

| 文件 | accuracy |
|---|---|
| westd:autodl/results/eval_grpo_rasp_20_qwen_math.json | 0.725 |
| westd:autodl/results/eval_grpo_standard_20_qwen_math.json | 0.705 |
| westd:autodl/results/eval_sft_standard_qwen_math.json | 0.71 |
| westd:autodl/results/eval_sft_rasp_qwen_math.json | 0.725 |
| westd:autodl/results/eval_sft_rasp_rlvr_20_qwen_math.json | 0.730 |
| westd:autodl/results/eval_grpo_rasp_rlvr_20_qwen_math.json | 0.710 |
| westd:autodl/results/eval_grpo_rasp_25_qwen_math.json | 0.625 |
| westd:autodl/results/eval_grpo_standard_25_qwen_math.json | 0.635 |
| westd:autodl/results/eval_sft_qwen_math_rasp_25.json | 0.64 |
| westd:autodl/results/eval_sft_qwen_math_standard_25.json | 0.63 |

### 1.8 Pass@k = 8 GSM8K

| 文件 | pass@8 |
|---|---|
| westd:autodl/results/eval_pass_k8_unpruned_qwen_math.json | 0.965 |
| westd:autodl/results/eval_pass_k8_rasp_20_grpo_qwen_math.json | 0.915 |
| westd:autodl/results/eval_pass_k8_rasp_20_sft_qwen_math.json | 0.935 |
| westd:autodl/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json | 0.910 |
| westd:autodl/results/eval_pass_k8_rasp_20_grpo_deepseek.json | 0.890 |
| westd:autodl/results/eval_pass_k8_standard_20_grpo_deepseek.json | 0.855 |

### 1.9 CKA heatmap 数据

| 文件 | 用途 |
|---|---|
| westd:autodl/results/cka_15pct/cka_heatmap_cka_only_15.json | 28×28 matrix, n=50, dense vs sft_cka_only_15 |
| westd:autodl/results/cka_15pct/cka_heatmap_standard_15.json | 28×28 matrix, n=50, dense vs sft_standard_15 |
| westb:autodl/results/cka_heatmap_cka_only.json | 主图 (20%) |
| westb:autodl/results/cka_heatmap_standard.json | 主图 (20%) |
| westb:autodl/results/cka_heatmap_rasp.json | 主图 (20%) |
| westb:autodl/results/cka_heatmap_random.json | 主图 (20%) |
| westb:root/results/cka_heatmap.json | 旧版本 |
| westb:autodl/results/cka_reliability_ablation.json | n_samples=1024, n_layers=28, valid_groups=28, GQA结构数据 |

### 1.10 推理基准 (inference benchmark)

| 文件 | 内容 |
|---|---|
| westb:autodl/results/inference_benchmark.json | dense vs rasp_20 vs standard_20 |
| westb:autodl/results/inference_benchmark_cka_only.json | (含异常 dense baseline) |
| westb:autodl/results/inference_benchmark_cka_only_clean.json | dense=75.73 tok/s, cka_only=75.79, standard=51.86 |

详见 §3.

### 1.11 统计检验文件

| 文件 | 内容 |
|---|---|
| westd:autodl/results/bootstrap_ci_accuracy_v2.json | bootstrap CI + McNemar, 16 methods × 1319 samples, B=10000 |
| westd:autodl/results/bootstrap_ci_analysis_combined.json | 主统计表（McNemar p-values） |
| westd:autodl/results/bootstrap_ci_analysis_v3.json | 简化版 |
| westd:autodl/results/bootstrap_ci_results.json | 旧版 |
| westb:autodl/results/bootstrap_ci_westb_v3.json | 7B + 1.5B 全部 CI |
| westd:autodl/results/tost_binary_westd.json | TOST per-method outcomes, 8 methods × 1319 |
| westd:autodl/results/tost_keyed_westd.json | TOST keyed by question hash |
| westb:autodl/results/tost_binary_westb.json | TOST 同上 westb 备份 |
| westb:autodl/results/tost_keyed_westb.json | TOST 同上 |
| westb:autodl/results/binary_outcomes_westb.json | per-sample binary outcomes |
| westb:autodl/results/gradient_flow_v3/statistical_tests.json | Wilcoxon CKA-only_vs_Standard per-layer p<1e-33 |
| westb:autodl/results/gradient_flow_v3/gradient_flow_stats.json | 梯度统计 (mean/std/min/max per layer) |
| westb:autodl/results/gradient_flow_v3/raw_gradient_norms.json | 原始 gradient norms |
| westb:autodl/results/gradient_flow/gradient_flow_stats.json | v1 旧版 |
| westb:autodl/results/rci_diversity_correlation.json | CKA diversity scores（见 §3） |

### 1.12 Pruned 模型保留 group 数据（结构验证）

| 文件 | 内容 |
|---|---|
| westb:autodl/results/group_selection_comparison.json | 7B, original_intermediate_size=18944, group_size=676, groups_per_layer=28, num_layers=28, total_groups=784, rasp/cka/std/random 各方法每层保留数 |
| westb:autodl/results/cka_per_layer.json | 旧版 |

---

## 2. Registry 成功实验指标（250 个有 metrics 的成功实验）

> 由 `read_registry(filters={"conclusion":"success"})` 拉取，共 277 个，250 个含 metrics。完整保存在 `/tmp/registry_with_metrics.json`（本地）。

### 2.1 关键事实

- 注册的 GSM8K-GRPO 成功实验：32 个，覆盖 7B/1.5B、cka_only/standard/rasp/random/shortgpt/unstructured、α=0/0.5/1.0/2.0/3.0/4.0、sparsity 15%/20%/25%、3 个 seeds (42/123/456)
- 注册的 GSM8K-SFT 成功实验：19 个
- 注册的 MATH500 成功实验：49 个（GRPO 20 + SFT 26 + 其他 3）
- 注册的 HumanEval 成功实验：21 个
- 注册的 MBPP 成功实验：11 个

### 2.2 单位不一致警告（Reviewer 雷区）

部分 registry metrics 字段使用百分比形式 (如 `accuracy: 73.09`)，与同名实验的小数形式 (`0.7309`) 共存。例：
- `eval_gsm8k_grpo_cka_only_15_seed123.metrics.accuracy = 73.09`（百分比） vs JSON 文件 `0.7309`
- `eval_grpo_standard_20_fair_v2.metrics.accuracy = 59.44`（百分比） vs JSON 文件 `0.5944`
- `eval_grpo_unpruned_v2_step100.metrics.accuracy = 81.27`（百分比） vs JSON 文件 `0.8127`
- `eval_postprune_rasp_25.metrics.accuracy = 21`（百分比） vs JSON 文件 `0.21`
- `eval_humaneval_sft_cka_only_20_2048_v2.metrics.pass_at_1 = 20.12`（%） vs JSON 0.2012

**含义**：写论文取数字必须从 JSON 文件取，不能直接信 registry metrics 字段。

### 2.3 Math500 字段命名不一致

- 大多数 fixed 版本用 `accuracy / n_correct / n_total / stderr / truncation_rate / avg_response_length`
- 个别用 `correct / total / natural_eos / truncated`（如 `eval_math500_grpo_rasp_alpha0p5_20_fixed`、`eval_math500_sft_rasp_alpha4p0_20_fixed`）
- 个别用 `num_correct / num_total`（如 `eval_math500_sft_cka_only_20_fixed_v2`）
- `eval_math500_grpo_standard_20_fixed` 用 `math500_acc / math500_correct / math500_total / math500_stderr`

---

## 3. 图表数据源（论文 Figure / Table 用）

### 3.1 Inference benchmark（论文 §Inference Efficiency / Fig）

文件：`westb:autodl/results/inference_benchmark.json`（**实际可信版本**）
```
dense (DeepSeek-R1-Distill-Qwen-7B):  76.25 tok/s, 6.682s/prompt, 16.22 GB peak
rasp_20    (sft_rasp_20):              52.07 tok/s, 4.156s/prompt, 11.60 GB peak, 28.5% mem ↓
standard_20 (sft_standard_20):         49.78 tok/s, 6.167s/prompt, 11.61 GB peak, 28.4% mem ↓
```

文件：`westb:autodl/results/inference_benchmark_cka_only_clean.json`
```
dense:        75.73 tok/s, 6.729s, 16.22 GB
rasp_20 (= DeepSeek dense, 模型路径错配): 75.79 tok/s, 16.23 GB  ← 数据可疑
standard_20 (= sft_cka_only_20): 51.86 tok/s, 4.078s, 11.60 GB
```

**警告**：`inference_benchmark_cka_only.json` 的 dense baseline 异常慢（35.4 tok/s）；`_clean` 版本 rasp_20 用了 dense 模型路径，命名混乱。论文应只引 `inference_benchmark.json`（westb 主版本）。

### 3.2 CKA Reliability（论文 Tab/Fig）

文件：`westb:autodl/results/cka_reliability_ablation.json`
- num_samples=1024, n_layers=28, n_heads_original=28, n_kv_heads=4, heads_per_kv=7
- total_gqa_groups=112, valid_gqa_groups=28
- per-layer-group CKA scores, 大多数 group1/2/3 为 null（仅 group0 有值 → 文档说明 GQA 共享 KV 后只有 1 个有效 group/layer）

### 3.3 RCI Diversity Correlation（论文 §RCI formalization）

文件：`westb:autodl/results/rci_diversity_correlation.json`
- 定义：diversity_score = 1 - mean(diag(CKA(dense_layer_i, pruned_layer_i)))
- 数据（n_layers=28, matrix=28×28）：

| Method | mean_diag_CKA | std | diversity_score |
|---|---|---|---|
| cka_only | 0.6202 | 0.1601 | **0.3798** |
| standard | 0.9039 | 0.0431 | 0.0961 |
| random   | 0.9233 | 0.0730 | 0.0767 |
| rasp     | 0.8822 | 0.0604 | 0.1178 |

含 28 维 cka_diagonal_values 数组。

### 3.4 Bootstrap CI + McNemar（Table 1 主统计）

文件：`westd:autodl/results/bootstrap_ci_analysis_combined.json`
- date: 2026-05-20, dataset: GSM8K test, n_samples=1319, n_bootstrap=10000, ci=0.95, seed=42
- McNemar: continuity-corrected χ² (Edwards), df=1, threshold=0.05

关键 CI：
- Dense_GRPO_Unpruned_7B: 81.27% [79.15, 83.32]
- CKA-only_SFT_7B@20%: 63.91% [61.33, 66.49]
- CKA-only_GRPO_7B@20%_s42: 64.37% [61.71, 66.94]
- Standard_SFT_7B@20%: 59.29% [56.63, 61.94]
- Standard_GRPO_7B@20%: 59.44% [56.79, 62.09]
- RASP_GRPO_7B@20%: 60.88% [58.23, 63.46]
- Standard_GRPO_7B@25%: 51.10% [48.45, 53.75]
- ShortGPT_SFT_7B@20%: 44.73% (partial 999/1319)
- ShortGPT_GRPO_7B@20%: 43.37% [40.71, 46.02]
- Unstructured_20%: 87.87%
- 1.5B family 6 个 (22%-36% 范围)

McNemar 关键比较（p-values）：
- CKA-only vs Standard GRPO 7B@20%: p=0.00086 ★
- CKA-only vs RASP GRPO 7B@20%:    p=0.0200  ★
- CKA-only vs ShortGPT GRPO 7B@20%: p=0.0     ★
- CKA-only vs Standard SFT 7B@20%: p=0.00223 ★
- RASP vs Standard GRPO 7B@20%:    p=0.349   (n.s.)
- Dense vs CKA-only GRPO 7B@20%:   p=0.0     ★
- CKA-only vs Standard 1.5B@20% (SFT, GRPO): both p=0.0 ★

### 3.5 Gradient Flow（论文 §Recovery dynamics）

文件：`westb:autodl/results/gradient_flow_v3/`
- `gradient_flow_stats.json`: 每层 attn/mlp 的 mean/std/min/max
- `statistical_tests.json`: Wilcoxon CKA-only_vs_Standard 全部 p < 1e-33（28 层 × 2 模块）
- `raw_gradient_norms.json`: 原始数据

### 3.6 Per-layer Group Selection（论文 Fig: 保留率分布）

文件：`westb:autodl/results/group_selection_comparison.json`
- 7B, intermediate=18944, group_size=676, 28 groups/layer, 28 layers, 784 total
- RASP @20%: keeps 584 / prunes 200。**前 7 层各 prune 16 (强 prune)，layer 7-27 大多 prune 0-4**（即 RASP 偏向前几层）
- 各 method 完整每层数据可绘 "保留 group/intermediate_size by layer" 图

### 3.7 CKA matrix raw（28×28 数据）

- `westd:autodl/results/cka_15pct/cka_heatmap_*.json`：sparsity=15% 版本
- `westb:autodl/results/cka_heatmap_*.json`：sparsity=20% 主版本

每个 cka_matrix 是 28×28 float 列表（dense layer i × pruned layer j 的 CKA 相似度）

---

## 4. 超参配置（来源代码精确路径）

### 4.1 模型 / 数据集

| 参数 | 值 | 来源 |
|---|---|---|
| 主模型 | DeepSeek-R1-Distill-Qwen-7B (28 layers, hidden=3584, intermediate=18944, heads=28, KV heads=4, heads_per_kv=7) | scripts/run_alpha_ablation.sh:23, group_selection_comparison.json |
| 1.5B 模型 | DeepSeek-R1-Distill-Qwen-1.5B (推断，未在脚本中直接写出) | (registry 中 sft_cka_only_20_1p5b 等命名) |
| Qwen2.5-Math 模型 | Qwen2.5-Math-7B-Instruct（猜测） | qwen_math 路径推断 |
| 校准数据 | openai/gsm8k 'main' train split | src/importance_score.py:41, src/cka_overlap.py:55 |
| SFT 训练数据 | openai/gsm8k 'main' train | src/train_sft_warmup.py:46, sft_recovery.py:47 |
| GRPO 训练数据 | openai/gsm8k 'main' train | src/train_grpo_v5.py:164 |
| Eval GSM8K | openai/gsm8k 'main' test (1319) | src/eval_gsm8k.py:474 |
| Eval MATH-500 | HuggingFaceH4/MATH-500 test (500) | src/eval_math500.py:225 |
| Eval HumanEval | openai/openai_humaneval test (164) | src/eval_humaneval.py:176 |
| Eval MBPP | mbpp train (374 problems used as test) | src/eval_mbpp.py:108 |

### 4.2 Pruning (src/prune.py)

| 参数 | 默认 | 来源 |
|---|---|---|
| --sparsity | 0.35 | src/prune.py:165 (脚本默认 0.20 sparsity) |
| --alpha | 1.0 | src/prune.py:166 |
| --floor_ratio | 0.4 | src/prune.py:170 |
| --seed | 42 | src/prune.py:168 |
| --dtype | bfloat16 | src/prune.py:169 |

实际脚本 (scripts/run_alpha_ablation.sh):
- SPARSITY="0.20"
- ALPHAS=(0.0 0.5 1.0 2.0 4.0)

RASP scoring 公式 (src/prune.py:211, 214):
- `attn_scores = importance * (1 - overlap) ^ alpha`
- `mlp_scores  = importance * (1 - overlap) ^ alpha`

RASP-RLVR (反向 CKA, src/prune.py:219, 222):
- `scores = importance * overlap ^ alpha`

### 4.3 Importance scoring (src/importance_score.py)

| 参数 | 默认 |
|---|---|
| --n_samples (校准) | 512 |
| --max_length | 512 |
| --seed | 42 |
| --dtype | bfloat16 |

### 4.4 CKA overlap (src/cka_overlap.py)

| 参数 | 默认 |
|---|---|
| --n_samples | 512 |
| --max_length | 512 |
| --mlp_groups | 28 |
| --seed | 42 |
| --dtype | bfloat16 |

**注**：CKA reliability 实验用 num_samples=1024（cka_reliability_ablation.json:config）

### 4.5 SFT warmup (src/train_sft_warmup.py)

| 参数 | 默认 |
|---|---|
| --num_epochs | 1 |
| --lr | 2e-5 |
| --batch_size | 2 |
| --gradient_accumulation_steps | 8 |
| --max_seq_length | 2048 |
| --logging_steps | 10 |
| --seed | 42 |

### 4.6 SFT recovery (src/sft_recovery.py)

| 参数 | 默认 |
|---|---|
| --num_train_epochs | 2 |
| --learning_rate | 2e-5 |
| --batch_size | 1 |
| --gradient_accumulation_steps | 8 |
| --max_seq_length | 2048 |
| --seed | 42 |

### 4.7 GRPO v5 (src/train_grpo_v5.py)

| 参数 | 默认 |
|---|---|
| --learning_rate | 1e-6 |
| --num_train_epochs | 3 |
| --per_device_train_batch_size | 2 |
| --gradient_accumulation_steps | 8 |
| --max_completion_length | 512（v5 默认；v1 脚本里用 2048/4096）|
| --temperature | 0.4 |
| --repetition_penalty | 1.15 |
| --num_generations | 4 |
| --beta (KL) | 0.01 |
| --loss_type | dapo |
| --format_reward_weight | 0.1 |
| --gradient_checkpointing | true |
| --optim | adamw_8bit |
| --reward_desert_patience | 50 |
| --save_steps | 100 |
| --save_total_limit | 3 |
| --seed | 42 |

**关键**：scripts/run_alpha_ablation.sh 里 GRPO 用 max_completion_length=4096, max_samples=2000，与默认不同。

### 4.8 Evaluation

| 参数 | 默认 | 文件 |
|---|---|---|
| GSM8K max_new_tokens | 4096 | eval_gsm8k.py:447 |
| GSM8K temperature | 0.0 (greedy) | eval_gsm8k.py:451 |
| GSM8K pass@k k | 1 | eval_gsm8k.py:457 |
| GSM8K voting_temperature | 0.7 | eval_gsm8k.py:455 |
| GSM8K voting_top_p | 0.95 | eval_gsm8k.py:456 |
| MATH-500 max_new_tokens | 4096 | eval_math500.py:206 |
| HumanEval max_new_tokens | 512 (新版默认；旧 _2048 文件用 2048) | eval_humaneval.py:156 |
| MBPP max_new_tokens | 2048 | eval_mbpp.py:88 |
| HumanEval timeout | 10s | eval_humaneval.py:158 |
| MBPP timeout | 10s | eval_mbpp.py:92 |

---

## 5. 缺失数据 / 风险点

| 缺失/风险 | 说明 |
|---|---|
| ShortGPT_SFT_7B@20% GSM8K | JSON 截断，仅恢复 999/1319 样本（见 bootstrap_ci_analysis_combined.notes）。McNemar 跳过 |
| CKA-only_GRPO_7B@25% | bootstrap CI 文件标注 "file not found on either server" |
| eval_humaneval_unpruned.json | max_new_tokens 太短(默认 512)，导致 pass@1=0.0183 — 主表应只用 `_2048` 版本 (0.4512) |
| MATH-500 baseline 复现版本众多 | `eval_math500_unpruned.json`, `math500_dense_unpruned.json`, `math500_dense_2048.json` 三个值不同 (0.736 / 0.736 / 0.530) — 论文需明确取哪个 |
| inference benchmark 多版本不一致 | inference_benchmark.json (rasp 加速 0.683x) vs inference_benchmark_cka_only_clean.json (rasp 加速 1.001x，但模型路径错配为 dense) — 数据可信度需 reviewer 警告 |
| 1.5B humaneval/mbpp | 部分 pass@1 = 0.0 或 0.006，过低，可能需要重新跑或说明 1.5B 在 code 任务上不可用 |
| Qwen2.5-Math 模型确切路径 | 代码中未硬编码，model_path 由 caller 决定；文档中需补充 |
| eval_gsm8k_floor_0.4 单独文件 | 默认 floor 实验数据 = eval_gsm8k_grpo_cka_only_20_extended_300.json (0.6437)，论文 floor ablation 写法需对齐 |
| Alpha ablation n=100 (root/results/alpha_ablation/) vs full | 一组 n=100 + 一组 full GSM8K (1319) — 论文 alpha ablation 取哪个需注明 |
| eval_grpo_standard_step50_full.json (0.5891) | 单独存在但未在主表，用途不明 |
| group_selection_comparison.json 中 rasp/standard/cka/random 各方法 | 完整数据可绘 §3.6 图（输出截断未取全 28 层；rasp 数据已部分获取） |
| W&B 数据 | wandb dir 是 symlink `/root/recovery_aware_struct_prune/wandb -> /root/autodl-tmp/recovery_aware_struct_prune/wandb`；未拉取具体 run 日志（建议 Worker 后续单独采） |
| 1.5B 模型 huggingface ID | 代码中无硬编码，需通过 `pruned_*_1p5b` 路径找模型 config 才能确认 |

---

## 6. 文件位置速查

- **本地索引（已生成）**：
  - `/tmp/json_index_westd.json` (westd-32935 161 个 JSON 的浅层 metadata)
  - `/tmp/json_index_westb.json` (westb-23072 100 个 JSON)
  - `/tmp/registry_with_metrics.json` (250 个 registry 实验完整 metrics)
- **远端原始 JSON**：
  - westd-32935: `/root/autodl-tmp/recovery_aware_struct_prune/results/` (~120 文件) + `/root/recovery_aware_struct_prune/results/` (~32 文件，含 alpha_ablation/)
  - westb-23072: `/root/autodl-tmp/recovery_aware_struct_prune/results/` (~80 文件) + `/root/recovery_aware_struct_prune/results/` (~18 文件)
- **代码**：westd-32935:/root/recovery_aware_struct_prune/src/

