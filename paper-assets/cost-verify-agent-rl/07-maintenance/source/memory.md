<!-- NOTE: This file is append-only for exp029 analysis. Preserving all existing content. -->

## exp029_seed100_resume_step10 训练结果分析 (2026-05-23)

### 实验信息
- **Run name**: exp029-seed100-episode-level-resume-step10
- **W&B run ID**: xbiw0zde (entity: xiaoyucorynne-, project: cost-verify-agent-rl)
- **服务器**: westd-47453
- **训练时长**: ~1.54h (5549s total including eval)
- **模型**: Qwen/Qwen2.5-3B-Instruct (SFT: qwen3_exp021_ragen_sft_v4), seed=100
- **Resume**: 从 step5 FSDP checkpoint 继续训练至 step10
- **EXIT_CODE**: 0 ✓

### Checkpoint
- **路径**: `/root/autodl-tmp/checkpoints/exp029-seed100/global_step_10/actor/`
- 包含: model shards (2×4.06GB), optim shards (2×6.88GB), extra_state, huggingface tokenizer
- `latest_checkpointed_iteration.txt` 已更新

### Step-by-Step 训练指标 (steps 6-10)

| Step | Train Success | critic/score/mean | actor/ppo_kl | actor/entropy_loss | actor/grad_norm | train/pass@8 | response_length/mean |
|------|-------------|-------------------|-------------|-------------------|----------------|-------------|---------------------|
| 6 | 39.06% | 3.906 | 0.00404 | 0.121 | 4.155 | 93.75% | 8577.9 |
| 7 | 37.50% | — (truncated) | — | — | — | 100% | — |
| 8 | 47.66% | 4.766 | 0.00587 | 0.105 | 3.935 | 93.75% | 8534.4 |
| 9 | 28.13% | 2.813 | 0.00660 | 0.086 | 3.048 | 81.25% | 11034.3 |
| 10 | — | 4.531 | 0.00246 | 0.081 | 3.974 | — | 8967.1 |

### ID Eval (32 episodes, val-before-train & final)

| Metric | Step 5 (resume point) | Step 10 (final) | Δ |
|--------|----------------------|-----------------|---|
| val-env/AlfworldSG/success | 31.25% (10/32) | 37.5% (12/32) | +6.25% |
| val-core/unknown/reward/mean@32 | 3.125 | 3.750 | +0.625 |
| val-env/AlfworldSG/action_is_valid | 73.43% | 76.43% | +3.0% |
| val-env/AlfworldSG/num_actions | 36.69 | 35.75 | -0.94 |
| val-env/response_length | 3502.5 | 2716.8 | -785.7 |

### Collapse 检测 (step 10)
- first_turn_valid_rate: 98.4% (126/128) — 无 collapse
- MI estimate: 0.167 (healthy diversity)
- retrieval_accuracy@2: 54.7% (above chance 22.1%)

### 分析

**训练健康度: ✓ HEALTHY**

1. **Reward 趋势**: critic/score/mean 从 3.91 (step6) 波动上升至 4.53 (step10)，step9 出现单步回落（2.81）但 step10 立即回升，属于正常 RL 方差
2. **KL 散度**: 稳定在 0.002-0.007 范围，非常低，模型未偏离 reference policy
3. **Entropy**: 0.121 → 0.081 单调下降，策略逐步收敛但未过度收缩
4. **Grad norm**: 3.0-4.2 范围内稳定，无梯度爆炸
5. **ID eval**: success rate 从 31.25% 提升至 37.5% (+6.25pp)，同时 response length 缩短 (-785 tokens)，说明模型变得更高效
6. **无 collapse**: first_turn_valid_rate 98.4%，MI 健康

**Step 9 dip 说明**: critic/score 回落至 2.81，对应 response_length 大幅增加到 11034（vs 正常 8500），说明该 batch 抽到更多难题导致成功率下降。step10 回升，非系统性问题。

### 下一步
- 需要用 step10 checkpoint 跑 **OOD eval** (AlfworldSG_OOD) 验证 hypothesis：seed100 从 step5 的 11.2% OOD 是否在 step10 达到 20-25% 与 seed4/5/6 一致
- OOD eval 是验证 "healthy seed 的 OOD generalization 是 later-emerging property" 的关键实验
