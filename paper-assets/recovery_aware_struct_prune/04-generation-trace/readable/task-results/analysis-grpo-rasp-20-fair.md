# analysis grpo rasp 20 fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_rasp_20_fair_20260518T010430_result.json`
- **Structured JSON:** [`6aec14781d6e42bb193b.json`](../../sessions/6a/6aec14781d6e42bb193b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，以下是汇总报告。

---

## grpo_rasp_20_fair 实验分析报告

### 1. 训练状态
- **状态**: 正常完成，EXIT_CODE=0
- **步数**: 100/100 (1h02m27s)
- **W&B run**: `s5zf5akl` (W&B summary metrics 为空，但日志有完整数据)
- **Checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair/` (含 checkpoint-80/90/100 + 最终模型 12.3GB)

### 2. 核心指标趋势

| Step | reward | frac_zero_std | comp_length |
|------|--------|---------------|-------------|
| 10   | 0.017  | 85%           | 993.5       |
| 20   | 0.021  | 85%           | 998.7       |
| 30   | 0.023  | 80%           | 965.9       |
| 40   | 0.021  | 85%           | 958.4       |
| **50** | **0.061** | 72.5%     | 973.5       |
| 60   | 0.053  | 75%           | 978.9       |
| 70   | 0.056  | 67.5%         | 930.2       |
| 80   | 0.030  | 77.5%         | 981.2       |
| 90   | 0.015  | 90%           | 990.9       |
| 100  | **0.010** | 85%         | 963.0       |

**趋势**: 微弱上升到 step 50 (peak 0.061) 后坍塌回 0.01。全程 reward 始终在 0.01-0.06 区间，远低于有效学习阈值。

### 3. 病理特征
- **frac_reward_zero_std 67-90%**: 绝大多数 batch 所有 generation 的 reward 完全相同（全错或全对），GRPO 无法计算有效 advantage，无梯度信号
- **completion_length ~930-999/1024**: 模型持续生成接近最大长度的输出，未能学会在 `\boxed{}` 处终止。clipped_ratio 92-96%
- **reward 最终 < 起始**: step 100 (0.01) 低于 step 10 (0.017)，训练实质为负增长

### 4. 三方法公平对比（均为 20% 剪枝，v5 config）

| Method | Final Reward | Peak Reward | Trend |
|--------|-------------|-------------|-------|
| **CKA-only** | 0.30+ | 0.30+ | 持续上升 |
| **Random** | 0.15-0.20 | ~0.20 | 缓慢上升 |
| **RASP (fair)** | **0.01** | **0.06** | 停滞→坍塌 |

### 5. 结论

**Negative result confirmed**: RASP fair retrain 复现了旧版的 reward stagnation，排除了 D058 confound（config 差异）。

Recovery capacity gradient 在公平条件下得到验证：
- CKA-guided pruning (保留对齐关键层) >> Random >> RASP (仅按权重冗余剪枝)
- RASP 剪掉的层虽然在权重统计意义上"冗余"，但包含 GRPO 恢复所必需的表征结构
- 这支持论文核心 claim：结构化剪枝的恢复能力取决于保留的 representation alignment，而非简单的参数量

**建议**: 将此结果作为 Table 1 / Figure 2 的关键证据，展示 recovery capacity gradient (CKA > Random >> RASP) 在公平条件下的稳健性。

---
