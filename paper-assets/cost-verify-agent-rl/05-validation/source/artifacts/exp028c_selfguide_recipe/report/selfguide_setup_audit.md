# Self-Guide vs exp028c Setup 审计

## 摘要

exp028c 与 Self-Guide 论文在**五个关键维度**存在根本差异，其中任何一个都可能独立解释 val success 不动的现象。按重要性排序：**(1)** RAGEN step_independent 训练模式将 50 步的 episode 切成独立样本（history_length=2），彻底破坏长程信用分配，而 Self-Guide 使用 verl-agent 的 episode-level 训练；**(2)** 我们的 prompt 存在 system prompt 与 turn-level format prompt 的矛盾（system 说不用 tag，turn 说用 `<answer>` tag），且叠加了 Turn/State/Reward 结构开销；**(3)** Self-Guide 的核心创新——step-level 自引导 reward（±0.1）完全缺失，我们只有 episode 末尾的 sparse reward；**(4)** val 仅评 16 个 episode（6.25% 分辨率），远低于 Self-Guide 评的 ~140 个；**(5)** Qwen3-1.7B 的 `/think`、`/no_think` 特殊 token 可能干扰 RL 训练。

---

## 1. 环境交互方式

### Self-Guide (verl-agent)
- **Action 格式**: JSON 单行 `{"think": "optional short reasoning", "action": "next action"}`
- **System prompt**: 简洁，指导 JSON 格式输出
- **Admissible actions**: 每步注入可选动作列表
- **Turn 结构**: 标准 user/assistant 轮次，无额外 Turn/State/Reward 包装
- **每步开销**: 极低，JSON 格式紧凑

### exp028c (RAGEN)
- **System prompt**: `"You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment..."` — 包含完整的 Self-Guidance Assessment 指令（[Assessment: positive/neutral/negative]）
- **AlfworldSG env_instruction** 说：`"After the closing </think> tag, output EXACTLY ONE admissible action command directly. Do NOT wrap the action in any tags."`
- **但 RAGEN _build_format_prompt** 在每个 turn 的 user message 里注入：`"Always output: <think> [Your thoughts] </think> <answer> [your answer] </answer>"`
- **Turn 结构**：每步包含 `Turn N:\nState:\n{observation}\n{admissible actions}\nYou have X actions left. Always output: <think>...</think><answer>...</answer>...`
- **Reward 反馈**：每步之间有 `Reward: X` 的 user message（RAGEN 框架特性）

### 差异和影响
| 维度 | Self-Guide | exp028c | 影响 |
|------|-----------|---------|------|
| Action 格式 | JSON `{"think":"...","action":"..."}` | `<think>...</think><answer>...</answer>` | RAGEN 格式更长，且存在矛盾 |
| System prompt 一致性 | 一致 | **矛盾**：system 说不用 tag，turn prompt 说用 `<answer>` tag | 模型收到矛盾指令，可能导致格式混乱 |
| 每步 token 开销 | ~20 tokens overhead | ~100+ tokens overhead (Turn/State/actions_left/format_prompt) | 实际推理空间被压缩 |
| Reward 反馈 | 无显式反馈 | 每步间有 `Reward: X` message | 增加 prompt 长度 |

**关键 bug**：AlfworldSG 的 env_instruction 示例 `<think>...</think>go to desk 1`（bare action）与 RAGEN 的 format prompt `<think>...</think><answer>...</answer>` 矛盾。ctx_manager 的正则解析依赖 `<answer>` tag，所以如果模型遵从 system prompt 输出 bare action，解析会失败。

---

## 2. 训练数据分布

### Self-Guide
- **训练数据**: ALFWorld train split（~3553 games），每步随机采样
- **Rollouts/step**: 论文未明确指出，但 DAPO 兼容性测试用 group_size=8
- **Eval**: 在 eval_in_distribution（valid_seen，~140 games）上评估，可能是全集
- **训练步数**: 100 steps

### exp028c
- **训练数据**: 同 ALFWorld train split（~3553 games）
- **env_groups=16, group_size=8 → 128 rollouts/step**
- **但 step_independent 模式**将每个 episode 的每一步展开为独立训练样本。假设平均 episode 长 ~20 步，则 128 episodes × 20 steps = **~2560 训练样本/step**
- **Val**: env_groups=16, group_size=1 → **仅 16 episodes**
- **训练步数**: 100 steps

### 差异和影响
| 维度 | Self-Guide | exp028c | 影响 |
|------|-----------|---------|------|
| Rollouts/step | 未明确，≥128 | 128 episodes | 量级相当 |
| 训练样本/step | 128 (episode-level) | ~2560 (step-level) | step_independent 数量大但质量低 |
| Val episodes | ~140 (full valid_seen) | **16** | 6.25% 分辨率，单个成功/失败 = ±6.25% |
| Val 分辨率 | ~0.7% (1/140) | **6.25%** (1/16) | val 结果基本无法区分 baseline 和微小改进 |

---

## 3. 模型和 Tokenizer

### Self-Guide
- **Base models**: Qwen3-1.7B, Qwen3-4B, Qwen2.5-7B-Instruct
- **ALFWorld 主结果**: Qwen3-4B 达 96.9%（含 SG+GR）
- **Qwen3-1.7B**: 也有实验，但论文主表展示的是 4B 模型
- **Thinking mode**: 论文使用 JSON 格式，避开了 `<think>` tag 的冲突

### exp028c
- **Model**: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` — Qwen3-1.7B 的 RAGEN SFT checkpoint
- **Thinking mode**: `enable_think: True`，模型被要求用 `<think>...</think>` 格式
- **Qwen3 特殊 token**: Qwen3 系列内置 `/think` 和 `/no_think` 特殊 token。SFT checkpoint 可能已经训练了这些 token 的使用模式，RL 训练时如果 tokenizer 没有正确处理可能导致梯度异常

### 差异和影响
- Self-Guide 主结果用 **Qwen3-4B**（2.3× 参数量），而我们用 **Qwen3-1.7B**。4B 模型的 ALFWorld 能力显著更强
- JSON 格式天然避免了 `<think>` 与 Qwen3 内置 thinking token 的冲突
- 我们的 SFT checkpoint 是在 RAGEN 格式上微调的，格式惯性可能与 AlfworldSG 的 bare-action 指令冲突

---

## 4. GRPO 实现

### Self-Guide (verl-agent)
- **框架**: verl-agent（论文明确声明 "All RL experiments are implemented using the verl-agent framework"）
- **GRPO Loss**: 标准 clipped surrogate：`L = E[min(r(θ)Â, clip(r(θ), 1-ε, 1+ε)Â)]`
- **Advantage**: group-relative normalization：`Â = (R - μ_R) / (σ_R + ε)`
- **KL**: coefficient = 0.01（DAPO 测试）
- **Clip ratio**: (0.2, 0.28)（DAPO 设置）
- **Advantage 粒度**: Episode-level — 整个 trajectory 共享一个 advantage 值

### exp028c (RAGEN)
- **框架**: RAGEN（基于 verl 的自研框架）
- **GRPO Loss**: 相同公式，通过 verl 的 `core_algos.py` 实现
- **Advantage**: 相同 group-relative normalization
- **KL**: `use_kl_loss: True, kl_loss_coef: 0.01, kl_loss_type: low_var_kl`
- **Clip ratio**: `clip_ratio_low: 0.2, clip_ratio_high: 0.28` — 一致
- **loss_agg_mode**: `token-mean`
- **关键差异 — step_independent overlay**:
  1. `assign_step_rewards`: 将 episode reward 分配到每一步
  2. `compute_step_discounted_returns`: gamma=0.95 折扣
  3. `compute_grpo_step_advantage`: 按 uid 分组归一化

### 差异和影响
| 维度 | Self-Guide (verl-agent) | exp028c (RAGEN) | 影响 |
|------|------------------------|-----------------|------|
| Advantage 粒度 | Episode-level | Step-level (gamma=0.95 折扣) | 信用分配机制完全不同 |
| 每步的 advantage | 整个 trajectory 共享 | 每步独立的 discounted return | RAGEN 的步级 advantage 丧失全局视角 |
| 训练单元 | 1 episode = 1 sample | 1 episode → ~20 samples | 梯度被稀释到步级 |
| KL 计算 | 标准 KL | `low_var_kl` variant | 可能更保守 |

**关键问题**：step_independent + gamma=0.95 的折扣 return 意味着，如果一个 50 步的 episode 在最后一步成功（reward=10.0），那么第 1 步的 return = 10.0 × 0.95^49 ≈ 0.77，第 25 步 = 10.0 × 0.95^25 ≈ 2.77，第 49 步 = 10.0 × 0.95 = 9.5。早期步骤几乎得不到梯度信号，但恰恰是早期步骤（选择去哪个房间/找什么物品）决定了 episode 成败。

---

## 5. Reward 设计

### Self-Guide
- **Environment reward**: Binary task success — R_env(τ) = 1 on success, 0 otherwise
- **Self-guidance reward (核心创新)**:
  - 每步生成 assessment: positive/neutral/negative
  - 映射为 scalar: +0.1 / 0 / -0.1
  - **Composite**: `R(τ;u) = R_env(τ) + λ(u) × Σr_t^sg`
  - λ(u) 梯形 schedule: 0 (step 0-40) → 0→1 (40-50) → 1 (50-70) → 1→0 (70-80)
- **效果**: 提供 dense step-level reward，不再完全依赖 sparse episode reward

### exp028c
- **Environment reward**: `config.score * won = 10.0 * won`（成功 10.0，失败 0）
- **valid_action_bonus**: 0（配置为 0）
- **format_penalty**: 0（配置为 0）
- **Self-guidance reward**: **完全缺失**。虽然 AlfworldSG 的 env_instruction 要求模型输出 `[Assessment: positive/neutral/negative]`，但代码中**没有任何解析 assessment 并转化为 reward 的逻辑**
- **实际 reward signal**: 纯 sparse — 仅在 episode 结束且成功时给 10.0

### 差异和影响
| 维度 | Self-Guide | exp028c | 影响 |
|------|-----------|---------|------|
| Reward 密度 | Dense (每步 ±0.1) + sparse (成功 1.0) | **纯 sparse** (成功 10.0) | Self-Guide 的核心创新被完全丢弃 |
| Reward scale | 1.0 (success) | 10.0 (success) | GRPO 归一化后无影响 |
| Self-guidance 利用 | 双重用途：inference guidance + training reward | 仅 inference guidance（且格式矛盾） | 丧失训练时的 dense reward signal |

**这可能是最大的缺失**：Self-Guide 论文的核心贡献就是 step-level self-guidance reward 带来 8% 提升。我们要求模型输出 assessment 但完全不利用它。

---

## 6. Eval 协议

### Self-Guide
- **Eval set**: eval_in_distribution (valid_seen)，~140 games
- **Temperature**: 0.4（validation）
- **Sampling**: do_sample=True, temp=0.4
- **Episodes**: ~140（全集）
- **结果**: GRPO baseline 86.7%, +SG 91.4%, +SG&GR 96.9%（Qwen3-4B）

### exp028c
- **Eval set**: eval_in_distribution (valid_seen)
- **env_groups=16, group_size=1 → 16 episodes**（从 ~140 可用中随机选 16 个）
- **Temperature**: 0.4, do_sample=True
- **分辨率**: 每个成功/失败 = ±6.25%
- **Baseline**: ~6.25%（≈1/16 success）

### 差异和影响
| 维度 | Self-Guide | exp028c | 影响 |
|------|-----------|---------|------|
| Eval episodes | ~140 | **16** | 方差极大，无法检测 <6% 的改进 |
| 分辨率 | ~0.7% | **6.25%** | val 指标几乎是无用的 |
| 统计功效 | 高 | **极低** | 6 步训练后的微小改进完全被噪声淹没 |

---

## 根因分析：为什么 train success 上升但 val 不动？

### 1. [最可能] Step-independent 训练模式破坏长程信用分配
**证据**：train success 波动上升说明模型在学习局部动作模式（选择正确的 admissible action），但 val 不动说明这种局部学习不能泛化到新 game。

**机制**：step_independent 模式下每一步只看 history_length=2 的上下文窗口，模型无法学会"先去厨房拿刀，再去切面包"这样的多步计划。verl-agent 的 episode-level 训练天然支持这种长程依赖。gamma=0.95 + 50 步 = 第 1 步的 return 仅为终末 reward 的 7.7%，几乎无梯度。

### 2. [很可能] Self-guidance reward 完全缺失
**证据**：论文报告 SG+GR 比 GRPO baseline 提升 10.2%。我们的实验是 GRPO baseline 配置（无 SG reward），在 Qwen3-1.7B（更弱的模型）上运行。

**机制**：仅有 sparse reward，大多数 episode 以失败结束（reward=0），GRPO advantage 在组内全零时退化为无梯度。

### 3. [很可能] Val 样本量太小，无法检测改进
**证据**：16 episodes，6.25% 分辨率。即使 train 有真实改进，val 也需要至少 2/16 的成功率变化才可见（12.5%）。

**机制**：Self-Guide 论文 GRPO baseline 在 Qwen3-4B 上已经 86.7%——但那是 4B 模型 + 100 步训练。1.7B 模型 6 步训练后的改进可能在 1-5% 级别，16 个 episode 完全检测不到。

### 4. [可能] Prompt 格式矛盾导致动作解析异常
**证据**：AlfworldSG system prompt 说"不要用 tag 包 action"，但 RAGEN turn prompt 说"用 `<answer>` tag"。

**机制**：模型可能在两种格式间震荡，导致 action parsing 失败率不稳定。train 中 group_size=8 可以掩盖这个问题（只要 8 个 rollout 中有 1 个格式正确就有梯度），但 val 中 group_size=1 无缓冲。

### 5. [次要] 模型规模差距
**证据**：Self-Guide 主结果用 Qwen3-4B（2.3× 参数），我们用 1.7B SFT checkpoint。

**机制**：1.7B 模型的 ALFWorld 零样本能力本就很弱（baseline ~6%），RL 的改进需要更多步数才能显现。

---

## 建议

### P0 — 立即修复（阻断性问题）

1. **扩大 val 评估到 ≥64 episodes**
   - `val.env_groups: 64`（或更大）
   - 当前 16 episodes 无法提供有意义的 val signal
   - 这是最低成本的修复，不改训练逻辑

2. **修复 prompt 格式矛盾**
   - 方案 A：修改 AlfworldSG env_instruction 的示例和描述，明确使用 `<think>...</think><answer>...</answer>` 格式
   - 方案 B：修改 ctx_manager 的 action parser 支持 bare action（`<think>...</think>go to desk 1`）
   - 推荐方案 A，改动最小

### P1 — 关键架构差异

3. **考虑切回 full context window 模式**
   - 将 `context_window_mode` 从 `step_independent` 改为 `full`
   - 这最接近 verl-agent 的 episode-level 训练方式
   - 代价：训练速度变慢（长序列），可能需要调 max_model_len

4. **实现 self-guidance reward**
   - 从模型输出中解析 `[Assessment: positive/neutral/negative]`
   - 映射为 +0.1/0/-0.1 step-level reward
   - 实现 λ(u) 梯形 schedule
   - 这是 Self-Guide 论文的核心贡献，没有它就不是 Self-Guide 复现

### P2 — 改善训练效率

5. **延长训练到 20+ steps 再判断**
   - 6 步训练对于 1.7B 模型 + sparse reward 太少
   - Self-Guide 论文 100 步训练，自引导 reward 在 step 40 才开始生效

6. **考虑用 Qwen3-4B 做对照实验**
   - 论文主结果是 4B，1.7B 可能根本不够

---

## 附录：超参数对照表

| 参数 | Self-Guide 论文 | exp028c | 一致? |
|------|---------------|---------|------|
| 框架 | verl-agent | RAGEN | ❌ |
| Base model | Qwen3-4B (主结果) | Qwen3-1.7B SFT | ❌ |
| Training steps | 100 | 100 | ✅ |
| LR | 1e-6 | 1e-6 | ✅ |
| KL coef | 0.01 | 0.01 | ✅ |
| Clip ratio | (0.2, 0.28) | (0.2, 0.28) | ✅ |
| Group size | 8 | 8 | ✅ |
| Rollout temp | 1.0 | 1.0 | ✅ |
| Val temp | 0.4 | 0.4 | ✅ |
| Max response | 1024 | 1024 | ✅ |
| Max prompt | 4096 | 4096 | ✅ |
| Max episode steps | 50 | 50 | ✅ |
| Context mode | Episode-level (full) | step_independent (h=2) | ❌ |
| Action format | JSON | `<think>...<answer>...` | ❌ |
| Self-guidance reward | ±0.1 step-level | **缺失** | ❌ |
| Val episodes | ~140 | 16 | ❌ |
| Entropy coef | 未明确 | 0.001 | ? |
| Gamma | 未明确 | 0.95 | ? |
| loss_agg | 未明确 | token-mean | ? |
| format_penalty | 未明确 | 0 | ? |
| norm_adv_by_std | 未明确 (标准 GRPO = Yes) | True | ✅ |
