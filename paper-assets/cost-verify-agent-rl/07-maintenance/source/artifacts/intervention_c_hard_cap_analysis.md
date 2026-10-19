# Intervention C: Generation Hard Cap Analysis

**exp_id**: intervention-c-hard-cap  
**server**: westd-47453  
**seed**: 999 (same as Seed 7 crash seed)  
**config**: response_length=512, max_turn=20, kl_loss_coef=0.01, total_steps=7  
**hypothesis**: step 7 时 resp_len < 2000 且 success > 30% → hard cap 有效  

## Conclusion: **NEGATIVE** (partial success — cap works but training still degrades)

Hard cap 成功阻止了 response inflation（核心指标 resp_len 受控），但模型仍在 step 5-7 出现 success rate 崩溃，表明 response inflation 是症状而非根因。

---

## Per-Step Training Metrics

| Step | train_success | train_resp_len | total_resp_len | critic_score | kl_loss | num_actions | pass@8 |
|------|:----------:|:-----------:|:------------:|:----------:|:------:|:----------:|:-----:|
| 1 | 28.1% | 815.6 | 4736.6 | 2.81 | 0.00032 | 16.54 | 62.5% |
| 2 | 33.6% | 791.0 | 4344.6 | 3.36 | 0.00045 | 15.15 | 100% |
| 3 | **47.7%** | 670.4 | 4087.5 | 4.77 | 0.00188 | 13.54 | 87.5% |
| 4 | **54.7%** | 604.1 | 3754.0 | **5.47** | 0.00331 | 12.24 | 100% |
| 5 | 32.8% | 774.6 | 6191.5 | 3.28 | 0.00470 | 16.03 | 75.0% |
| 6 | 38.3% | 745.0 | 4662.2 | 3.83 | 0.00399 | 14.95 | 93.8% |
| 7 | **15.6%** | 870.3 | 7170.4 | 1.56 | **0.02044** | 18.14 | 50.0% |

## Validation Metrics

| Step | val_success | val_resp_len | val_reward@32 | val_num_actions |
|------|:----------:|:----------:|:------------:|:--------------:|
| 0 (init) | 6.25% | 974.8 | 0.625 | 19.50 |
| 5 (mid) | 9.38% | 911.6 | 0.938 | 18.72 |
| 7 (final) | 9.38% | 927.4 | 0.938 | 19.16 |

## Comparison with Seed 7 Baseline (exp029_seed7, no intervention)

| Metric | Seed 7 (no cap) @ step 7 | Intervention C (hard cap) @ step 7 | Delta |
|--------|:-----:|:-----:|:-----:|
| total_resp_len | **11569** (exploded from 1784) | **7170** | -38% |
| resp_len explosion ratio | 6.5x (1784→11569) | 1.5x (4737→7170) | Controlled |
| train_success | ~0% (collapsed) | 15.6% (degraded) | Slightly better |
| Failure mode | Response inflation → OOM-like collapse | KL spike → success degradation | Different |

## Key Observations

### 1. Hard cap 物理约束有效
- per-turn response length (total/num_actions) 在所有步骤保持 286-395 tokens，远低于 512 上限
- total_resp_len 最高 7170 vs baseline 的 11569，未出现爆炸性增长
- 没有 OOM、没有 abort、clip_ratio 始终很低

### 2. 但出现了新的崩溃模式
- Step 1-4: 健康学习，success 单调上升 28%→55%，resp_len 下降
- Step 5-7: success 骤降 33%→16%，同时 kl_loss 从 0.005 飙升到 0.020（4x spike）
- 这是 KL-driven collapse，不是 response inflation collapse
- entropy 从 0.094 降至 0.076，策略变得更确定但错误

### 3. Val metrics 几乎没有改善
- val_success 从 6.25% 只提升到 9.38%（在 32-episode 评估下可能不显著）
- 训练集 overfitting 明显：train peak 55% vs val 9.4%

### 4. Step 7 的特殊性
- num_actions 升至 18.14（接近 max_turn=20），说明模型在用尽所有可用 turn 但仍无法完成任务
- action_is_valid 降至 73%（vs peak 时的 84%），模型开始产生更多无效动作

## Per-turn response length verification

| Step | total_resp_len | num_actions | per_turn_avg | vs 512 cap |
|------|:------------:|:----------:|:-----------:|:---------:|
| 1 | 4736.6 | 16.54 | 286.4 | OK |
| 4 | 3754.0 | 12.24 | 306.7 | OK |
| 7 | 7170.4 | 18.14 | 395.3 | OK |

Hard cap is physically enforced and working correctly.

## Implications for Paper Framing

1. **Generation caps are necessary but not sufficient**: 物理限制 response length 可以防止 token explosion（最严重的崩溃形式），但不能防止策略退化

2. **Response inflation is a symptom, not the root cause**: 当 response inflation 被物理阻止时，instability 通过 KL divergence spike 和 success degradation 以另一种形式表现

3. **The instability is in optimization dynamics**: KL loss 在 step 7 飙升 4x 表明模型偏离 reference policy 的趋势本身就是不稳定的，无论 response length 是否被约束

4. **Three interventions, three failures — but each reveals mechanism**:
   - Intervention A (len_penalty): reward shaping 不够强
   - Intervention B (high_kl): KL 系数太高压制学习
   - Intervention C (hard_cap): 证明 length explosion 不是根因

5. **论文可以 frame 为**: "We systematically investigated the root cause of training instability through controlled ablations. While generation caps successfully prevent the most visible symptom (response inflation), the underlying optimization instability persists, suggesting the need for fundamental algorithmic solutions (e.g., adaptive KL, reward normalization, or curriculum-based training)."

---

*Analysis generated: 2026-05-21*  
*Log: ~/runs/cost-verify-agent-rl/intervention-c-hard-cap.log*  
*Exit code: 0 (completed successfully)*
