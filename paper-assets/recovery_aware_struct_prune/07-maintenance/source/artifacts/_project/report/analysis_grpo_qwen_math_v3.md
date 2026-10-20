# GRPO v3 Qwen2.5-Math-7B 跨模型验证分析

**日期**: 2026-05-16
**实验**: grpo_rasp_qwen_math_v3, grpo_standard_qwen_math_v3
**服务器**: westd-11672
**W&B**: yyg9ty4u (RASP), 5n2snh48 (Standard)

## 实验配置

| 参数 | 值 |
|------|-----|
| Base model | Qwen2.5-Math-7B |
| Pruning ratio | 20% |
| GRPO steps | 100 |
| beta | 0.04 |
| loss_type | dapo |
| lr | 5e-7 |
| temperature | 0.4 |
| repetition_penalty | 1.15 |
| max_completion_length | 1024 |
| Dataset | GSM8K (7473 samples) |

## 关键指标摘要

### RASP 20% (grpo_rasp_qwen_math_v3)

| Step | reward | frac_zero_std | loss | comp_len | clipped_ratio | terminated_len |
|------|--------|--------------|------|----------|---------------|----------------|
| 10 | 0.049 | 0.650 | 0.000367 | 1015 | 0.988 | 60.5 |
| 20 | 0.083 | 0.625 | 0.00883 | 1020 | 0.994 | 33.7 |
| 30 | 0.059 | 0.550 | 0.000320 | 1019 | 0.994 | 18.0 |
| 80 | 0.056 | 0.700 | 0.000621 | 1024 | 1.000 | 0.0 |
| 90 | 0.048 | 0.575 | 0.01484 | 1003 | 0.975 | 57.0 |
| 100 | 0.061 | 0.675 | -0.00236 | 1006 | 0.975 | 128.1 |

- **Collapse 判定: Permanent** — reward 全程 0.04-0.08，从未突破 0.1
- completion_length 持续在 1003-1024（近 max），clipped_ratio 0.975-1.0
- mean_terminated_length 极低（0-128），绝大多数 generation 未自然终止
- 模型陷入重复生成模式（日志可见 "110 yards is the total distance" 无限循环）
- Final: reward=0.061, frac_zero_std=0.675, loss=-0.00236

### Standard 20% (grpo_standard_qwen_math_v3)

| Step | reward | frac_zero_std | loss | comp_len | clipped_ratio | terminated_len |
|------|--------|--------------|------|----------|---------------|----------------|
| 10 | 0.063 | 0.750 | 0.01531 | 943 | 0.881 | 271.3 |
| 20 | 0.044 | 0.850 | 0.000705 | 952 | 0.888 | 320.9 |
| 30 | 0.031 | 0.900 | -0.00527 | 931 | 0.863 | 327.3 |
| 80 | 0.069 | 0.750 | 0.02252 | 903 | 0.831 | 319.4 |
| 90 | 0.038 | 0.825 | 0.00245 | 922 | 0.856 | 341.7 |
| 100 | 0.044 | 0.850 | -0.01208 | 921 | 0.856 | 241.8 |

- **Collapse 判定: Permanent** — reward 全程 0.03-0.07，无 recovery 迹象
- frac_zero_std 高达 0.75-0.90，比 RASP 更严重
- completion_length 903-952（不如 RASP 极端但仍偏高）
- mean_terminated_length 241-342（比 RASP 好，有更多 generation 能终止）
- Step 30 frac_zero_std 达到 0.90 峰值 → 最严重的多样性坍缩点
- Final: reward=0.044, frac_zero_std=0.850, loss=-0.01208

### Checkpoint 信息

| 实验 | 路径 | 大小 |
|------|------|------|
| RASP | /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math/ | ~12GB |
| Standard | /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math/ | ~12GB |

两个实验的 checkpoint-100 均已保存，模型 safetensors 完整。

## 与 DeepSeek 基准对比

### DeepSeek-R1-Distill-Qwen-7B 基准 (已有结果)

| 方法 | Collapse 类型 | Peak reward | Final frac_zero_std | Recovery? |
|------|-------------|-------------|---------------------|-----------|
| RASP 20% | Permanent | 0.039 | 0.95 | No |
| Standard 20% | Transient | ~0.15 | ~0.4 | Yes (~step 90) |
| Unpruned | None | 0.661 | ~0.1 | N/A |

### Qwen2.5-Math-7B (本次结果)

| 方法 | Collapse 类型 | Peak reward | Final frac_zero_std | Recovery? |
|------|-------------|-------------|---------------------|-----------|
| RASP 20% | Permanent | 0.083 | 0.675 | No |
| Standard 20% | Permanent | 0.069 | 0.850 | No |

### 关键差异

1. **RASP collapse 在两个模型上都复现** — Qwen Math RASP 也出现 permanent collapse，但严重程度不同：
   - DeepSeek: frac_zero_std → 0.95, reward ~ 0.039（极端坍缩）
   - Qwen Math: frac_zero_std ~ 0.65, reward ~ 0.06（中等坍缩）

2. **Standard 模式不一致** — 这是核心发现：
   - DeepSeek Standard: transient dip → recovery（C2 的核心支撑）
   - Qwen Math Standard: **permanent collapse**，frac_zero_std 高达 0.85-0.90
   - Standard 在 Qwen Math 上甚至比 RASP 更严重（frac_zero_std 0.85 vs 0.65）

3. **Generation 行为差异**:
   - RASP: 几乎所有 generation 都 hit max length（clipped_ratio ~1.0），重复生成
   - Standard: clipped_ratio 较低（~0.86），更多 generation 能终止，但答案仍然错误

## Conclusion 判定

### C1: RASP permanent collapse
**Result: SUCCESS (partial)** — RASP 在 Qwen Math 上确实出现 permanent collapse，但严重程度弱于 DeepSeek。collapse 的定性模式（低 reward、高 frac_zero_std、max-length generation）一致。

### C2: Standard transient dip + recovery
**Result: NEGATIVE** — Standard 在 Qwen Math 上未出现 recovery pattern，而是表现为 permanent collapse。这意味着 DeepSeek 上观察到的 Standard recovery 优势不具备跨模型泛化性。

### 综合判定: NEGATIVE (mixed)
跨模型验证部分失败。RASP collapse 可复现，但 Standard recovery 不可复现。

## 对论文 Claims 的影响

### 正面影响
- "RASP pruning leads to GRPO collapse" 的 claim 获得第二个模型的支持（泛化性+1）

### 负面影响 / 需要修正
- **不能** claim "Standard pruning shows transient collapse with recovery" 是通用现象 — 这是 model-specific 的
- 需要弱化 C2 的表述：从 "Standard pruning enables GRPO recovery" → "Standard pruning showed recovery on DeepSeek-R1 but not universally"
- 或者需要探究原因：为什么 Qwen Math Standard 也 collapse？可能与 base model 的数学推理能力底线有关

### 后续建议
1. 运行 Qwen2.5-Math-7B unpruned GRPO baseline — 确认 base model 本身是否就容易 collapse
2. 如果 unpruned 也 collapse → 问题出在 model 而非 pruning method
3. 如果 unpruned 不 collapse → 20% pruning 对 Qwen Math 的伤害比对 DeepSeek 更大，两种方法都无法恢复
4. 考虑降低 pruning ratio（如 10%）在 Qwen Math 上测试

### 模型参数对比
- RASP model: 6,169,214,464 params
- Standard model: 6,147,409,408 params
- 差异仅 ~22M params，不太可能是 collapse 差异的主因
