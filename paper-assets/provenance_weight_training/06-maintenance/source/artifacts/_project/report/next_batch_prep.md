# 下一批实验预准备报告

生成时间: 2026-05-15 ~15:00 UTC

## 1. nmin4_seed42（优先级最高，cuda:1）

### 假设
n_min=4 (=batch_size) 强制 b*→0，退化为 uniform-equivalent PPL (~17.69)

### 代码验证：n_min=4 边界行为

`weighting/alpha_eff.py` 中 `find_optimal_b` 逻辑：
1. ESS(0) = n = batch_size = 4 = n_min → 满足约束
2. 对任何 b>0，ESS(b) < 4（只要 q_scores 非全等）→ 不满足约束
3. grid search 在第一个 b>0 就 break，返回 best_feasible_b = 0.0

**结论：n_min=4 在所有非退化 batch 上 b*=0，等价于 uniform weighting。** 代码无 bug，边界行为正确。

唯一例外：若某 batch 的 q_scores 全部相同（实际概率极低），ESS 恒等于 n，但此时 alpha_eff 也不随 b 变化。

### 训练命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16"
```

> **注意：** 服务器上 `run_nmin4_seed42.sh` 包含 `--eval_data_path data/human/eval_holdout.jsonl --eval_steps 500`（inline eval），但 registry planned_command 和当前 tau sweep 实验都不含 inline eval。建议**不加 inline eval**，训练后用 post-hoc eval，与其他实验保持一致且避免 eval overhead (~40min/round)。

### Registry 状态
已存在 `nmin4_seed42`，status=PREPARING。提交时更新 spec 即可。

---

## 2. ess_only_seed123（Claim 1 最大缺口，cuda:0 或空闲 GPU）

### 假设
ESS-only baseline (max-intervention), seed=123 复现。参考 ess_only_seed42: PPL=17.73, b_star_mean=3.51

### 训练命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed123 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16"
```

> `--tau 0.8` 对 ess_only 方法无实际作用（find_ess_only_b 不使用 tau），保留仅为命令一致性。n_min 未指定，默认 max(2, 4//2) = 2，与 ess_only_seed42 一致。

### Registry 状态
尚未创建，需要新建 registry entry。

---

## 3. 参数对比表

| 参数 | nmin4_seed42 | ess_only_seed123 | 参考: nmin1_seed42 | 参考: ess_only_seed42 |
|------|-------------|------------------|--------------------|-----------------------|
| weighting_method | adaptive | ess_only | adaptive | ess_only |
| n_min | **4** | 2 (default) | **1** | 2 (default) |
| tau | 0.8 | 0.8 (unused) | 0.8 | 0.8 (unused) |
| seed | 42 | **123** | 42 | 42 |
| output_dir | nmin4_seed42 | ess_only_seed123 | nmin1_seed42 | ess_only_seed42 |
| batch_size | 4 | 4 | 4 | 4 |
| grad_accum | 4 | 4 | 4 | 4 |
| tokens | 200M | 200M | 200M | 200M |
| lr | 5e-5 | 5e-5 | 5e-5 | 5e-5 |
| bf16 | ✓ | ✓ | ✓ | ✓ |
| inline eval | ✗ | ✗ | ✗ | ✗ |

---

## 4. 文件存在性验证

| 文件 | 状态 | 大小 |
|------|------|------|
| training/pretrain_weighted.py | ✓ 存在 | — |
| data/scored_data.jsonl | ✓ 存在 | 975MB |
| data/human/eval_holdout.jsonl | ✓ 存在 | 238MB |
| models/Qwen/Qwen3-0.6B/config.json | ✓ 存在 | 726B |
| output/models/nmin4_seed42 | ✗ 不存在（干净） | — |
| output/models/ess_only_seed123 | ✗ 不存在（干净） | — |
| run_nmin4_seed42.sh | ✓ 存在（含 inline eval） | — |

---

## 5. 预估运行时间

参考 nmin1_seed42 (4h50m) 和 ess_only_seed42 (3h37m)。nmin4 由于 b*=0（无 weight 计算开销），预计 ~3.5-4h。ess_only_seed123 预计 ~3.5-4h。

## 6. 需要主 Agent 决策的事项

1. **nmin4 inline eval**：服务器上的 run_nmin4_seed42.sh 含 inline eval 参数，但其他同期实验（tau sweep、nmin1）都不含。建议统一不加 inline eval，post-hoc eval。如果想加，需注意 eval overhead。
2. **GPU 分配**：nmin4 计划用 cuda:1（tau_05 当前占用），ess_only_seed123 需分配空闲 GPU。4 个 tau sweep 完成后有 cuda:0/1/2/3 全部可用。
3. **ess_only_seed123 的 registry entry** 需要新建。
