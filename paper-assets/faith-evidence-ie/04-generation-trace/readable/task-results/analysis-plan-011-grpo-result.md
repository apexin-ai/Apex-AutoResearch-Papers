# analysis plan 011 grpo result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_011_grpo_result_20260515T143225_result.json`
- **Structured JSON:** [`b5edd6bf2964242ac33d.json`](../../sessions/b5/b5edd6bf2964242ac33d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_011 GRPO G=8 bf16 训练摘要

### 训练状态
- **正常完成**：100/100 steps, EXIT_CODE=0
- 训练时长：554s（~9.2 min）
- Checkpoints：10 个（每 10 步一个，checkpoint-10 到 checkpoint-100）
- LoRA config：r=64, alpha=128, dropout=0.05, bf16 全精度（无量化）
- 无 W&B 日志

### Metrics Trajectory（每 5 步记录，仅展示有 reward 的步）

| Step | f1_reward | ced_reward | reward | format | frac_zero_std | KL |
|------|-----------|------------|--------|--------|---------------|------|
| 5    | 1.516     | 0.321      | 2.137  | 0.300  | 0.0           | 0.006 |
| 10   | 0.930     | 0.423      | 1.651  | 0.298  | 0.0           | 0.052 |
| 20   | **0.564** | 0.157      | 0.852  | **0.131** | 0.0        | 0.011 |
| 25   | 1.349     | 0.202      | 1.850  | 0.300  | 0.0           | 0.006 |
| 35   | 1.353     | 0.557      | 2.209  | 0.300  | 0.0           | 0.010 |
| 45   | 0.814     | 0.468      | 1.582  | 0.300  | 0.0           | 0.024 |
| 50   | 0.451     | 0.291      | 1.042  | 0.300  | 0.0           | 0.023 |
| 60   | 1.597     | 0.735      | 2.631  | 0.300  | 0.0           | 0.011 |
| 65   | 0.743     | 0.434      | 1.476  | 0.300  | 0.0           | 0.018 |
| 75   | **0.157** | 0.673      | 1.096  | **0.266** | 0.0        | 0.012 |
| 85   | **1.850** | 0.708      | **2.858** | 0.300 | 0.0         | 0.011 |
| 90   | 0.834     | 0.417      | 1.550  | 0.300  | 0.0           | 0.011 |
| 100  | 1.002     | 0.494      | 1.795  | 0.300  | 0.0           | 0.022 |

### 关键发现

**1. 无 mode collapse**
- frac_reward_zero_std = 0.0 贯穿全程，模型始终生成多样化输出
- 对比 QLoRA：QLoRA 后半程 frac_zero_std = 0.0-0.2

**2. 训练 metrics 极度不稳定**
- f1_reward 在 0.157 ~ 1.850 之间剧烈振荡（范围跨 12x）
- G=8 每 step 只有 8 个 completions，方差极大，无法看出稳定趋势
- 两次 format_reward 降到 0.131/0.266（步 20 和 75），说明偶尔生成格式不正确的输出

**3. KL divergence 极低**
- 始终在 0.005-0.052 范围，大部分 ~0.01
- 策略几乎未偏离 reference model

### 与 QLoRA GRPO (kl001_r4) 对比

| 指标 | QLoRA GRPO (best@90) | bf16 GRPO (final@100) |
|------|---------------------|----------------------|
| reward | 1.370 | 1.795 |
| f1_reward | 0.720 | 1.002 |
| ced_reward | 0.353 | 0.494 |
| frac_zero_std | 0.0-0.2 (后半程) | 0.0 (全程) |
| eval rel_f1 | max 0.217 ❌ | **未评估** |

bf16 训练 metrics 表面上更好：reward 更高，无 mode collapse 信号。但 **QLoRA 的训练 metrics 同样不差，问题出在 eval 上（catastrophic forgetting）**。

### 科学结论

**训练层面**：bf16 消除了量化引入的额外噪声，训练比 QLoRA 更稳定（无 frac_zero_std 升高）。

**但关键问题未解答**：是否存在 catastrophic forgetting 需要 eval 验证。QLoRA 训练时 reward 也在正常范围，但 eval 时 rel_f1 仅 0.217。bf16 可能有两种结果：

1. **eval 也出现 forgetting** → GRPO 在结构化 IE 上的失败是算法层面的（非量化问题），**强化 Claim 3**
2. **eval 正常** → 量化是 QLoRA GRPO 失败的主因，**需要修正 Claim 3**

**下一步**：需要在 bf16 checkpoint 上跑 eval（rel_f1/rel_p/rel_r on dev set）才能得出最终结论。

---
