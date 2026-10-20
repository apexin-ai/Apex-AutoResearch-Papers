# MVP RASP Pipeline V2 — 实验结果分析

**日期**: 2026-05-14
**模型**: DeepSeek-R1-Distill-Qwen-7B @ 35% sparsity
**服务器**: westb-23072
**日志**: `~/runs/recovery_aware_struct_prune/mvp_rasp_pipeline_v2.log` (82074 行)

## 1. 执行概况

Pipeline 脚本: `src/run_mvp_resume_from_3_5.sh`，从 Step 3.5 恢复执行。

| 阶段 | 状态 | 说明 |
|------|------|------|
| Step 0: Baseline eval | ⏭ 跳过 | V2 从 3.5 恢复，baseline 数据不在此次运行中 |
| Step 1+2: CKA + Importance | ⏭ 跳过 | 使用之前运行的产物 |
| Step 3: Pruning | ⏭ 跳过 | 使用之前运行的产物 |
| Step 3.5: Post-prune eval | ✅ 完成 | 两模型均 0.15% accuracy |
| Step 4: GRPO recovery | ❌ 失败 | 两进程在 step ~177/5604 被 SIGTERM (exit 143) |
| Step 5: Post-recovery eval | ❌ 未执行 | Step 4 失败后 set -e 退出 |
| Step 6: Correlation analysis | ❌ 未执行 | Step 4 失败后 set -e 退出 |

**关键遗漏**: 尽管计划采用 SFT warmup → GRPO 两阶段恢复，V2 pipeline 脚本中 **没有 SFT warmup 步骤**，直接对 0.15% accuracy 的退化模型做 GRPO。

## 2. Post-prune Evaluation (Step 3.5)

| 模型 | Accuracy | Correct/Total |
|------|----------|---------------|
| pruned_standard_35 | 0.15% | 2/1319 |
| pruned_rasp_35 | 0.15% | 2/1319 |

两个模型输出完全退化——生成的是重复 token（"by by by..."、"II II II..."、空格等），无法产生有意义的数学推理。RASP 和 Standard 剪枝后 accuracy 相同，均接近随机水平。

## 3. GRPO Recovery Training (Step 4)

### 配置
- 学习率: 1e-6
- Epochs: 3 (总步数 5604)
- Batch size: 2 × 8 (gradient accumulation) = 有效 batch 16
- num_generations: 4
- max_completion_length: 2048
- temperature: 0.7
- bf16: True
- report_to: "none" (无 W&B 记录)
- save_steps: 200

### GRPO RASP 模型 (GPU 0) 关键指标

| Step | Loss | Grad Norm | Reward | Entropy | frac_reward_zero_std |
|------|------|-----------|--------|---------|---------------------|
| 10 | 0 | 0 | 0.00625 | 0.3418 | 0.975 |
| 20 | 0 | 0 | 0 | — | — |
| 170 | -3.725e-10 | 4.188 | 0.00625 | 0.3497 | 0.975 |

- 偶尔出现 reward=0.00625（= 1/160，即 160 个 completion 中偶然猜对 1 个）
- 绝大部分 step loss=0, grad_norm=0（无学习信号）
- Step 170 出现极微小的 loss 和非零 grad_norm，但 reward 仍极低

### GRPO Standard 模型 (GPU 1) 关键指标

| Step | Loss | Grad Norm | Reward | Entropy | frac_reward_zero_std |
|------|------|-----------|--------|---------|---------------------|
| 10 | 0 | 0 | 0 | 0.0489 | 1.0 |
| 160 | 0 | 0 | 0 | 0.06127 | 1.0 |
| 170 | 0 | 0 | 0 | 0.06429 | 1.0 |

- 全程 reward=0, loss=0, grad_norm=0
- entropy 极低（0.04-0.06），模型已完全 collapse 到退化分布
- 相比之下 RASP 模型 entropy 更高（0.34），输出分布略更多样

### 终止
- 两进程均在 step ~177/5604 (3%) 被 SIGTERM 终止
- `GRPO STANDARD FAILED with exit code 143`
- Pipeline EXIT_CODE=0（脚本捕获了错误但最终返回 0）
- 无 checkpoint 保存（save_steps=200，未到达）
- recovered 目录只有 completions parquet 文件（step 10-170 的日志）

## 4. 未执行的步骤

### SFT Warmup
- `src/train_sft_warmup.py` 和 `src/run_sft_warmup.sh` 存在于代码库中
- 但 `run_mvp_resume_from_3_5.sh` **未包含 SFT warmup 步骤**
- 这是本次实验失败的直接原因：0.15% accuracy 的模型无法生成正确答案 → reward 恒为 0 → GRPO 无梯度信号

### Correlation Analysis
- `src/correlation_analysis.py` 存在
- 因 Step 4 失败，未执行
- 无 Spearman ρ(F(h), recoverability) 数据

### Post-recovery Evaluation
- 因无 recovered model checkpoint，未执行

## 5. 产出文件清单

| 文件 | 大小 | 说明 |
|------|------|------|
| `results/cka_scores.pt` | 122KB | CKA 功能重叠分数（Step 1 产物） |
| `results/importance_scores.pt` | 17KB | 重要性分数（Step 2 产物） |
| `results/eval_pruned_rasp_35.json` | 1.3MB | RASP 剪枝后 eval (0.15%) |
| `results/eval_pruned_standard_35.json` | 1.3MB | Standard 剪枝后 eval (0.15%) |
| `models/pruned_rasp_35/` | — | RASP 剪枝模型 checkpoint |
| `models/pruned_standard_35/` | — | Standard 剪枝模型 checkpoint |
| `models/recovered_rasp_35/completions/` | 17 parquet files | GRPO completions log (step 10-170) |
| `models/recovered_standard_35/completions/` | 17 parquet files | GRPO completions log (step 10-170) |
| `results/analysis/` | 空 | Correlation analysis 未执行 |

## 6. 核心结论

### 判定: **FAILED** — 实验未完成，核心假设未得到验证

**原因**:
1. **Pipeline 设计缺陷**: V2 脚本遗漏了 SFT warmup 步骤，直接对完全退化的模型 (0.15%) 做 GRPO
2. **GRPO 对退化模型无效**: 两模型均 loss=0, grad_norm=0，验证了之前的已知问题——35% sparsity 下模型输出完全退化，GRPO 无法从零开始恢复
3. **GRPO 被提前终止**: 即使继续运行完 5604 步，在 reward≈0 的条件下也不可能恢复
4. **Spearman ρ 未计算**: 核心指标 ρ(F(h), recoverability) 无数据，MVP 目标 ≥ 0.4 无法判定

### 初步观察（非结论性）

尽管实验未完成，GRPO 过程中有一个值得注意的差异：
- **RASP 模型**: entropy ≈ 0.34，偶有 reward > 0（0.00625），step 170 出现微弱梯度
- **Standard 模型**: entropy ≈ 0.05，全程 reward = 0，完全无梯度

这**可能**暗示 RASP 剪枝保留了更多功能多样性，但在无 SFT warmup 的条件下差异不足以产生有效学习。需要完整 SFT → GRPO 流程才能得出有意义的结论。

## 7. 下一步建议

1. 修复 pipeline：在 Step 4 前加入 SFT warmup（`train_sft_warmup.py`），恢复基本推理能力到 >5% accuracy
2. SFT warmup 后重新跑 GRPO
3. 完成 Step 5 (post-recovery eval) 和 Step 6 (correlation analysis)
4. 考虑接入 W&B（当前 report_to="none"）以便追踪训练曲线

## 8. 路径索引

- **日志**: `/root/runs/recovery_aware_struct_prune/mvp_rasp_pipeline_v2.log`
- **代码**: `/root/recovery_aware_struct_prune/src/`
- **模型**: `/root/recovery_aware_struct_prune/models/`
- **结果**: `/root/recovery_aware_struct_prune/results/`
- **Pipeline 脚本**: `/root/recovery_aware_struct_prune/src/run_mvp_resume_from_3_5.sh`
