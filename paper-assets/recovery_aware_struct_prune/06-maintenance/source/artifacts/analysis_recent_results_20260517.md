# 近期实验分析 (2026-05-17)

## A. grpo_rasp_25 Collapse 分析

### 逐步 Metrics (wandb run bc4ojqie, logging every 10 steps)

| Step | reward | reward_std | frac_zero_std | entropy | grad_norm | kl | loss |
|------|--------|-----------|---------------|---------|-----------|-------|--------|
| 10   | 0.0019 | 0.0075    | 0.925         | 0.0577  | 1.258     | 0.000934 | 0.0130 |
| 20   | 0.0075 | 0.0284    | 0.925         | 0.0513  | 0.032     | 0.000842 | 0.0054 |
| 30   | 0.0206 | 0.0667    | 0.875         | 0.0492  | 0.938     | 0.002224 | -0.0015 |
| 40   | 0.0025 | 0.0084    | 0.925         | 0.0474  | 1.125     | 0.000824 | 0.0133 |
| 50   | 0.0100 | 0.0333    | 0.875         | 0.0523  | 0.820     | 0.000835 | 0.0228 |
| 60   | 0.0025 | 0.0084    | 0.925         | 0.0460  | 0.024     | 0.000684 | 0.0141 |
| 70   | 0.0150 | 0.0584    | 0.850         | 0.0517  | 0.844     | 0.000842 | 0.0139 |
| 80   | 0.0019 | 0.0075    | 0.925         | 0.0389  | 0.052     | 0.000646 | 0.0035 |
| 90   | 0.0106 | 0.0384    | 0.850         | 0.0444  | 1.633     | 0.000704 | 0.0225 |
| 100  | 0.0094 | 0.0315    | 0.875         | 0.0426  | 0.054     | 0.000704 | 0.0128 |

### 与 20% RASP (v9) 对比

| 特征 | RASP 20% (v9) | RASP 25% (bc4ojqie) |
|------|---------------|---------------------|
| Collapse onset | ~step 10 | step 1 (首个日志点已 collapsed) |
| frac_zero_std 峰值 | 0.95 | 0.925 |
| frac_zero_std 范围 | 0.90-0.95 | 0.85-0.925 |
| Reward 范围 | near-zero | 0.002-0.021 (near-zero) |
| 持续性 | Permanent (100 steps) | Permanent (100 steps) |
| Entropy 趋势 | 持续下降 | 0.058→0.043 持续下降 |
| KL | 极低 | 极低 (0.0006-0.0022) |

### 结论

1. **Collapse onset**: 25% RASP 从第一个日志点起即处于 collapsed 状态（frac_zero_std=0.925），不存在非 collapse 阶段。与 20% RASP onset ~step 10 相比，25% 的 collapse 更早或同时。

2. **Collapse 深度**: frac_zero_std 峰值 0.925，略低于 20% 的 0.95。但 reward 始终 near-zero（最高 0.021），表明这一微小差异无实质意义。

3. **Permanent collapse**: 100 步内无任何恢复迹象。entropy 持续下降（0.058→0.043），模型越来越确定性但无法发现 rewarding trajectories。

4. **25% vs 20% 总结**: 两者 collapse 模式本质相同。25% 的 post-prune 损伤更严重（post-prune acc 21% vs 29%），但 GRPO collapse 表现趋同。两种 sparsity 下 SFT 恢复后的模型均无法通过 GRPO 进一步提升，collapse 都是 immediate + permanent。

5. **与 Standard 20% (v8) 对比**: Standard 20% 有 transient dip（~step 60）和 recovery（~step 90），属于完全不同的 collapse 类型。RASP 剪枝导致的 collapse 是 immediate/permanent，而 Standard 剪枝的 collapse 是 delayed/transient。

## B. eval_postprune_cka_only_30 故障调查

### 发现

1. **PID 59403 仍在运行**: `ps aux` 确认进程存活，正在执行 eval_gsm8k.py 评估 pruned_cka_only_30

2. **原始失败原因**: Registry 记录的失败是原始提交（PID 59861），失败原因为 `ValueError: tokenizer.chat_template not set`（剪枝模型目录缺少 tokenizer 文件，已知问题）

3. **Fix worker 已介入**: 自动修复 worker 复制了 tokenizer 文件并重新提交。当前运行的 PID 59403 是修复后的重试，启动于 2026-05-18 06:00

4. **当前进度**: 56/200 samples completed，~95s/sample → 预计总时长 ~5.3h

5. **早期结果不乐观**: 50/200 时 acc=0.0000，eos_rate=4%，avg_len=4024。与 RASP 30% 相同的 collapse 模式（全截断、零准确率）

6. **Registry 状态过时**: 显示 DONE/failed（来自原始失败），但实际重试正在运行中。需更新 registry 或等待完成后 reconcile

### 判断

- 进程真在跑，无需重试
- 但从 50 样本的结果看，CKA-only 30% post-prune accuracy 很可能也是 0%
- 预计 ~3-4 小时后完成（约 2026-05-18 10:00 UTC）

## C. 30% Sparsity 降级模式分析

### 降级曲线（RASP post-prune GSM8K accuracy）

| Sparsity | Accuracy | Truncated Rate | Avg Response Length | EOS Rate |
|----------|----------|----------------|---------------------|----------|
| 20%      | 29%      | -              | -                   | -        |
| 25%      | 21%      | -              | -                   | -        |
| 30%      | **0%**   | **97%**        | **3984/4096**       | **3%**   |

25%→30% 之间存在 **cliff**（断崖式下降）。

### 0% Accuracy 的具体模式

**不是乱码/随机 token**，而是"语法正确但推理崩溃"：

1. **循环逻辑**: 模型反复重述问题条件，开始计算后又回到起点
   - Example: "I need to determine the total age... I need to subtract 10 years from 162... I need to set up a ratio..."（不断重述，无法推进）

2. **输入回声**: 直接将题目中的数字作为答案输出
   - 题目总年龄 162 → 模型预测 162（未做任何运算）

3. **推理链断裂**: 开始多步推理但中途丧失连贯性
   - "First, I need to find... Next, I need to... I then subtract... Finally, I need to divide..."（逻辑步骤之间无数学关联）

4. **极端退化案例**: 部分响应出现大量 bold markdown 标记重复（`**more** **laps** **can** **Beth**`），文本结构本身开始崩解

5. **无法终止**: 97% 样本命中 4096 token 上限仍未得出答案。模型丧失了"完成推理并输出结论"的能力

### 与 Standard 30% 对比（待完成）

eval_postprune_standard_30 目前 RUNNING（PID 47667），完成后可对比。Standard 20% post-prune = 17.5%，若 Standard 30% 也 = 0%，则 cliff 是 sparsity-universal；若 > 0%，则 RASP 在高 sparsity 有额外脆弱性。

### 关键洞察

30% 结构化剪枝（移除 303/784 MLP groups）造成的损伤是**质变而非量变**：模型从"准确率降低但仍能推理"（20-25%）跌至"完全丧失数学推理能力"（30%）。保留的 MLP 容量不足以支撑 chain-of-thought 推理的基本功能。这一 cliff 可能对应某个临界的 MLP capacity threshold。
