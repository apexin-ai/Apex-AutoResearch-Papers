# Plan A 技术预研：N-gram Entropy + PI Controller for Collapse-Aware Mixing

> 日期：2026-05-14 | 状态：预研草案

## 1. N-gram Entropy 计算模块设计

### 1.1 计算时机

**信号源选择：generated text（非 holdout）。**

MVP v7 数据明确表明 holdout 上的指标（spectral eff_rank、PPL）对 collapse 不敏感——G2 模型已完全崩塌（unique_tokens=1），holdout eff_rank 反而从 676.96 升至 683.44（+0.96%），PPL 仅从 13.27 涨到 13.59（+2.4%）。而 generated text 的 n-gram entropy 在 G1 step 152 即检测到崩塌（unigram entropy -43.5%），是目前最早、最灵敏的信号。

因此控制信号计算在每个 checkpoint boundary 的 **generated text** 上进行。流程：

1. 训练 `save_steps` 步（当前配置 = 76 步 ≈ 5M tokens）
2. 保存 checkpoint
3. 用当前 checkpoint 模型生成 sample tokens（`metrics_gen_tokens`=500K）
4. 在 generated tokens 上计算 n-gram entropy → 作为 PI 控制器输入
5. 控制器输出新的 mixing ratio w → 更新下一个 training segment 的数据配比

**频率：每 checkpoint 一次（每 5M tokens ≈ 76 optimizer steps）。** v7 每代有 4 个 checkpoint，collapse 在 G1 第 2 个 checkpoint（step 152）即被检测到，说明 5M token 间隔足够早。更频繁的评估（如每 2.5M tokens）会增加 overhead，性价比不高。

### 1.2 N 的选择

v7 数据对比：

| 指标 | G0 | G1 (final) | G2 (final) | G0→G1 变化 | 灵敏度 |
|------|-----|-----------|-----------|-----------|--------|
| unigram_entropy | 6.93 | 0.96 | 0.00 | -86.1% | 高 |
| trigram_entropy | 11.41 | 1.28 | 0.00 | -88.8% | 高 |
| unigram_unique | 23586 | 6878 | 1 | -70.8% | 高 |
| vocab_coverage | 0.469 | 0.137 | 2e-5 | -70.8% | 高 |

**Unigram 和 trigram entropy 灵敏度相当，** 但 unigram entropy 有以下优势：

1. **计算成本最低：** O(N) 单次遍历，无需 n-gram 组合
2. **噪声最低：** trigram 分布更稀疏，小样本下方差更大
3. **检测时间相同：** 两者在 G1 step 152 同时检测到（因为 collapse 是全面性的——当 mode collapse 到少数 token 时，所有 n-gram 阶的 entropy 同步下降）
4. **可解释性强：** 直接反映 token 分布集中度

**建议使用 unigram entropy 作为主控制信号。** Trigram entropy 作为辅助监控指标记录，但不输入控制器（避免多输入增加调参复杂度）。

### 1.3 计算成本

**Overhead 极低。** N-gram entropy 计算在 CPU 上完成，不需要 GPU：

- 500K tokens 的 unigram entropy：单次 Counter + entropy 计算，< 0.1 秒
- 瓶颈在于 **生成 500K tokens**（需要 GPU）：以 Pythia-1B 在 RTX PRO 6000 上约 1000 tokens/sec 估算，需 ~8 分钟
- 对比训练时间（76 步 × ~2 sec/step ≈ 2.5 分钟），生成 overhead 约 3.2x 训练时间

**优化选项：减少 sample tokens。** 对 unigram entropy 而言，50K-100K tokens 已经足够稳定（unigram 分布收敛快）。将 `metrics_gen_tokens` 从 500K 降至 100K 可将生成时间压缩到 ~1.7 分钟，overhead 降至 0.7x。

**建议：PI 控制用 100K tokens（快速反馈），完整评估用 500K tokens（高精度记录）。**

## 2. PI Controller 架构

### 2.1 系统建模

```
                    ┌─────────────┐
  r (setpoint) ──→ ⊕ ──→ │ PI Controller│ ──→ w(k) ──→ ┌──────────────┐
                  - ↑    └─────────────┘            │ Data Mixer   │
                    │                                 │ (real/synth)  │
                    │                                 └──────┬───────┘
                    │                                        ↓
                    │                               ┌──────────────┐
                    │                               │   Trainer    │
                    │                               │ (1 segment)  │
                    │                               └──────┬───────┘
                    │                                        ↓
                    │                               ┌──────────────┐
                    │                               │  Generator   │
                    └────────────── y(k) ◀───────── │  + Entropy   │
                                                    │   Compute    │
                                                    └──────────────┘
```

| 概念 | 实例 |
|------|------|
| 被控对象 (Plant) | Iterative training pipeline：一个 segment（76 步训练 + 500K token 生成） |
| 控制变量 u(k) | w(k) = real data ratio，w ∈ [0.1, 0.9] |
| 被控变量 y(k) | unigram entropy of generated text (从 checkpoint 模型生成) |
| 设定点 r | G0 baseline unigram entropy（6.93）或带 margin 的目标值 |
| 扰动 | 模型参数每步更新导致的 distribution shift |
| 采样周期 T_s | 1 segment = 76 optimizer steps ≈ 5M tokens |

**关键非线性特性：**
- Plant 响应强非线性：w=0 时 entropy 指数衰减；w=1 时 entropy 基本不变
- 存在时延：当前 segment 的 mixing ratio 变化需要等到下一个 checkpoint 才能在 generated text 中反映
- 不可逆性：严重 collapse 后即使 w→1 也可能无法完全恢复 entropy

### 2.2 控制律

**标准离散 PI（位置式）：**

```
e(k) = r - y(k)                          # 误差：entropy 低于 setpoint 时 e > 0
u(k) = u_bias + Kp * e(k) + Ki * Σ e(j)  # PI 输出
w(k) = clamp(u(k), w_min, w_max)          # 执行器饱和约束
```

**误差方向解释：**
- e > 0：entropy 下降（collapse 趋势）→ u 增大 → 增加 real data 比例 → 抵抗 collapse
- e < 0：entropy 高于 setpoint（不太可能发生，除非 real data 本身变化）→ u 减小 → 可使用更多 synthetic data
- e ≈ 0：系统在 setpoint 附近 → u ≈ u_bias

### 2.3 参数设计

#### Setpoint 策略

**方案 A（保守）：r = G0 baseline × 0.9 = 6.24**

留 10% margin，允许一定程度的 diversity 自然衰减（real data 本身在不同 epoch 也有小幅 entropy 波动），避免控制器过于敏感。

**方案 B（aggressive）：r = G0 baseline = 6.93**

以 G0 的 entropy 为硬约束，任何下降都触发干预。可能导致控制器持续输出高 w（因为少量 synthetic data 就会略微降低 entropy）。

**建议先用方案 A（r = 6.24），** 如效果不明显再调低至 5.5。

#### Kp, Ki 估计

**系统增益分析（基于 v7 数据）：**

v7 中，G1 在 w=0（纯 synthetic）条件下训练。Entropy 轨迹（插值估计）：
- Step 0: y = 6.93（G0 final model 的生成 entropy）
- Step 76（ckpt 1）: y ≈ 5.4（估计，基于 step 152 时 -43.5%）
- Step 152（ckpt 2）: y ≈ 3.92（实测 -43.5%）
- Step 305（final）: y = 0.96

单个 evaluation interval（76 步）的 entropy 变化量：
- 初始阶段：Δy ≈ -1.5（从 6.93 到 ~5.4）
- 中间阶段：Δy ≈ -1.5（从 ~5.4 到 ~3.92）
- 后期：加速衰减

这是 w=0 的情况。假设 w=1 时 Δy ≈ 0（real data 训练不改变 entropy），则：

**过程增益 K_p（process）≈ 1.5 / 1.0 = 1.5 entropy_units / w_unit / interval**

即 w 每增加 1 单位（从 0 → 1），每个 interval 可挽救约 1.5 点 entropy。

**PI 参数初始估计（IMC-like tuning）：**

目标闭环时间常数 = 2-3 个 interval（允许 2-3 次测量后达到稳态）：

```
Kp = 1 / (K_process × τ_cl) = 1 / (1.5 × 2.5) ≈ 0.27
Ki = Kp / (τ_cl × N_i) = 0.27 / (2.5 × 3) ≈ 0.036
```

其中 N_i = 3 是积分去耦因子（防止积分过快）。

**但考虑到系统强非线性和不确定性，取保守值：**

| 参数 | 初始值 | 合理范围 | 依据 |
|------|--------|---------|------|
| Kp | 0.15 | [0.05, 0.5] | ~1/(2×K_process)，保守取值 |
| Ki | 0.02 | [0.005, 0.05] | Kp/7.5，慢积分防振荡 |
| r | 6.24 | [5.5, 6.93] | G0 baseline × 0.9 |
| u_bias | 0.5 | [0.3, 0.7] | 默认 50/50 混合 |
| w_min | 0.1 | [0.0, 0.2] | 保留最低 10% real data |
| w_max | 0.9 | [0.8, 1.0] | 避免 100% real（失去 synthetic 的 data augmentation 价值） |

#### Anti-windup 策略

**Conditional integration（条件积分）：**

```python
e = r - y
u_raw = u_bias + Kp * e + integral
u = clamp(u_raw, w_min, w_max)

# 仅在未饱和时积分
if u_raw == u:  # 未被 clamp
    integral += Ki * e
```

**原因：** 当 w 已经被推到极限（如 w=0.9），继续积累误差会导致一旦 entropy 恢复，w 需要很长时间才能回落（integral windup）。条件积分完全避免这个问题。

### 2.4 与文献对比

#### PI/PID 在 ML 训练中的应用

PI/PID 控制器在 ML 训练中的应用主要集中在优化器设计，不涉及数据配比控制：

| 工作 | 应用场景 | 与我们的差异 |
|------|---------|-------------|
| An et al., CVPR 2018 [1] | 证明 SGD-Momentum = PI 控制器，加入 D 项加速训练 | 控制对象是 gradient update，非 data mixing |
| Nature Comms 2024 [2] | PID 加速 DNN 优化器收敛 | 同上 |
| Incremental PID LR Scheduler [3] | PID 控制 learning rate | 控制 LR 而非数据配比 |
| LARS/LAMB [4] | 自适应 learning rate 调整 | 反馈控制思想类似，但无 data mixing |

**结论：没有工作将 PI/PID 控制器用于 data mixing ratio 的动态调节。** 我们的方案在控制论框架下是全新的。

#### 与 Aioli (ICLR 2025) 的架构对比

| 维度 | Aioli | 我们的 Plan A |
|------|-------|--------------|
| **控制信号** | Loss 在不同 domain 上的相对表现 | N-gram entropy（collapse 特异性信号） |
| **优化目标** | 最小化 worst-case domain loss | 维持生成多样性（entropy setpoint tracking） |
| **控制器类型** | Online convex optimization (gradient-based) | PI 控制器（无需梯度，model-free） |
| **粒度** | Multi-domain mixing (code/text/math) | Binary mixing (real/synthetic) |
| **Collapse awareness** | 无 | 有（entropy 直接测量 mode collapse） |
| **延迟** | 每步更新 | 每 segment（76 步）更新 |
| **计算开销** | 需要额外前向传播计算 domain loss | 仅需 CPU 上算 entropy |

## 3. 实验设计草案

### 3.1 Baselines

| ID | 策略 | 描述 | 复杂度 |
|----|------|------|--------|
| B0 | Pure Synthetic | w=0，G1+ 完全用 synthetic data（= v7 原实验） | 最简 |
| B1-30 | Fixed w=0.3 | 30% real + 70% synthetic，固定比例 | 简 |
| B1-50 | Fixed w=0.5 | 50/50 混合 | 简 |
| B1-70 | Fixed w=0.7 | 70% real + 30% synthetic | 简 |
| B2 | Threshold | unigram_entropy < r×0.8 时 w→0.9，否则 w=0.3（bang-bang 控制） | 中 |
| **PI** | **PI Controller** | **Kp=0.15, Ki=0.02, r=6.24, u_bias=0.5** | **中** |

**注意：**
- B0 数据已有（v7 实验，可直接复用，无需重新训练）
- B3 Oracle（用真实分布作为 target）概念上有意义但实际上等价于 w=1.0（每代都用 real data 训练），会退化为 "没有 synthetic data" 的 trivial 解。不作为 baseline，改用 B1-70 代替。

### 3.2 评估指标

**Primary（决定成败）：**
- **Holdout PPL trajectory**：各策略下 PPL 随 generation 的变化。越低越好。
- **Entropy preservation**：各策略下 unigram entropy 随 generation 的变化。越接近 G0 baseline 越好。

**Secondary（辅助分析）：**
- **Collapse delay**：entropy 首次下降超过 20% 时的 generation index。越晚越好。
- **Real data efficiency**：达到 B1-70 同等 PPL 所需的 real data 总量。越少越好（PI 的价值在于用更少 real data 达到同等效果）。
- **Controller behavior**：w(k) 轨迹、error 轨迹、integral 项变化（仅 PI 方案）。

**Reporting：**
- 每个 checkpoint 记录：generation, step, unigram_entropy, trigram_entropy, vocab_coverage, holdout_ppl, w(k), controller_state
- 最终汇总：每条策略的 entropy curve + PPL curve + w trajectory

### 3.3 最小可行实验

直接复用 v7 配置：

| 参数 | 值 | 依据 |
|------|-----|------|
| Model | Pythia-1B | 同 v7 |
| Data | wikitext-103-raw-v1 | 同 v7 |
| tokens_per_generation | 20M | 同 v7，已验证 collapse 发生 |
| num_generations | 5 | 比 v7 多 2 代，观察 PI 的长期稳定性 |
| checkpoint_interval | 5M tokens（76 步） | 同 v7，已验证检测灵敏度足够 |
| seeds | 3 (42, 0, 7) | v7 用 seed=42，seed=0 正在验证中 |
| batch_size × grad_accum | 8 × 4 = 32 | 同 v7 |
| lr | 2e-6 | 同 v7 |
| dtype | bfloat16 | 同 v7 |

**GPU 需求估算（基于 v7）：**

v7 运行了 3 代 ≈ 15 小时（含 eval、generation、和中间故障时间）。纯净运行时间估算：

| 阶段 | 时间/代 | 占比 |
|------|---------|------|
| Training（76 步/ckpt × 4 ckpts） | ~10 min | 5% |
| Generation for metrics（100K tokens × 4 ckpts） | ~7 min | 3% |
| Evaluation（spectral rank + PPL，4 ckpts） | ~40 min | 18% |
| Synthetic data generation（20M tokens for next gen） | ~5.5 h | 74% |
| **合计** | **~6.5 h** | 100% |

**生成是绝对瓶颈（占 74%）。**

5 代的单次运行（4 次 synth gen + 5 次 train+eval）：
- 训练+评估：5 × 50 min ≈ 4.2 h
- Synthetic gen：4 × 5.5h ≈ 22 h
- **单次运行 ≈ 26 h**

### 3.4 实验矩阵

采用两阶段策略降低 GPU 成本：

**Phase 1: 筛选（1 seed, seed=42）**

| 实验 | Mixing 策略 | Gens | 预计时间 | 说明 |
|------|-----------|------|---------|------|
| B0 | w=0 (pure synth) | 3 | 0 h | **复用 v7 数据** |
| B1-30 | w=0.3 fixed | 5 | 26 h | |
| B1-50 | w=0.5 fixed | 5 | 26 h | |
| B1-70 | w=0.7 fixed | 5 | 26 h | |
| B2 | Threshold (bang-bang) | 5 | 26 h | |
| PI-default | Kp=0.15, Ki=0.02 | 5 | 26 h | |
| **Phase 1 小计** | | | **~130 h (5.4 天)** | |

**Phase 2: 验证（3 seeds，仅前 2-3 名策略）**

| 实验 | Seeds | Gens | 预计时间 |
|------|-------|------|---------|
| Top-1 策略 | 42, 0, 7 | 5 | 78 h (已含 seed=42) → 52 h 新增 |
| Top-2 策略 | 42, 0, 7 | 5 | 52 h 新增 |
| Top-3 策略 | 42, 0, 7 | 5 | 52 h 新增 |
| **Phase 2 小计** | | | **~156 h (6.5 天)** |

**总计：~286 GPU-hours ≈ 12 天** on 1× RTX PRO 6000

**加速选项（若 GPU 预算紧张）：**
1. 减少 gens: 5 → 3（节省 40%，但损失长期稳定性观察）
2. Phase 1 减少 baselines（去掉 B1-30，只留 B1-50, B1-70）
3. vLLM 加速 synthetic generation（可能 2-3x speedup，但需要额外集成工作）

## 4. 代码架构预估

### 4.1 现有代码基础

| 模块 | 功能 | Plan A 可复用度 |
|------|------|----------------|
| `pilot_pipeline.py` | MVP 多代训练 + 评估 | 70%（结构可复用，但需加入控制器） |
| `controlled_pipeline.py` | PI 控制 + 多代训练 | **90%**（已实现 PI 控制循环，只需改信号源） |
| `controller.py` | PI 控制器 | **80%**（需改为 entropy 信号 + 加 anti-windup） |
| `metrics.py` | N-gram entropy、spectral rank、PPL 等 | **100%**（所有需要的指标已实现） |
| `data_utils.py` | 数据加载、mixing、packing | **100%**（MixedDataset + mix_datasets 已实现） |
| `config.py` | 配置管理 | 90%（需加 controller 参数） |
| `generate.py` | Synthetic data 生成 | 100% |
| `train.py` | HF Trainer 封装 | 100% |

**核心发现：`controlled_pipeline.py` 已经实现了完整的 PI 控制循环，** 包括 MixedDataset（支持动态 ratio 更新）、segment-based 训练、checkpoint 后测量 + 控制器步进。主要改动仅需将 `compute_spectral_effective_rank` 替换为 `compute_ngram_entropy`。

### 4.2 需要的改动

**A. 修改 `controller.py`（~1h）**

```
- 将信号语义从 "spectral rank"（下降=bad）改为 "entropy"（下降=bad）
- 添加 anti-windup（conditional integration）
- 添加 u_bias 参数
- 误差方向统一：e = r - y，e > 0 → 增加 real data
```

**B. 修改 `controlled_pipeline.py`（~2h）**

```
- 将 checkpoint 后的 compute_spectral_effective_rank 替换/增加 compute_ngram_entropy
  （调用 generate_sample_tokens → compute_ngram_entropy）
- 将 controller.step(eff_rank) 改为 controller.step(unigram_entropy)
- 添加 holdout PPL 记录（当前已有）
- 增加 r_target 自动设定逻辑（从 G0 baseline 计算）
```

**C. 新增 `baseline_runner.py`（~2h）**

```
- 封装 fixed-ratio 实验（调用 pilot_pipeline.py --fixed-ratio）
- 封装 threshold 策略实验（简单 if-else 控制器）
- 多 seed 批量运行支持
- 统一输出格式
```

**D. 新增 `analyze_plan_a.py`（~2h）**

```
- 加载所有实验的 metrics.jsonl / control_log.jsonl
- 生成对比图：entropy curve、PPL curve、w trajectory
- 统计表：final entropy、final PPL、collapse delay、data efficiency
- 支持多 seed 的 mean ± std 绘制
```

**E. 测试 & 调试（~2h）**

```
- controller 单元测试（验证 anti-windup、clamp、误差方向）
- 短程集成测试（1 gen, 2 segments, 确认数据流正确）
```

### 4.3 工作量估算

| 模块 | 工作量 | 说明 |
|------|--------|------|
| controller.py 改造 | 1 h | 改信号、加 anti-windup |
| controlled_pipeline.py 改造 | 2 h | 替换信号源、接入 n-gram |
| baseline_runner.py | 2 h | 新模块 |
| analyze_plan_a.py | 2 h | 新模块 |
| 测试 & 调试 | 2 h | 单元 + 集成 |
| **总计** | **~9 Worker-hours** | |

## 5. 风险和开放问题

### 技术风险

| 风险 | 严重度 | 可能性 | 缓解措施 |
|------|--------|--------|---------|
| **Generation bottleneck 导致实验周期过长** | 高 | 高 | Phase 1 先跑 1 seed 筛选；考虑 vLLM 加速 |
| **PI 参数对初始条件敏感** | 中 | 中 | Phase 1 包含参数敏感性检查；必要时加 Kp/Ki sweep |
| **系统非线性导致 fixed-gain PI 失效** | 中 | 中 | 准备 gain scheduling 方案作为 fallback |
| **Collapse 不可逆——PI 纠正太晚** | 中 | 低 | 保守 setpoint（r = 0.9×baseline）+ 高 w_min=0.1 |
| **5 代仍不足以看到 PI 和 fixed ratio 的差异** | 低 | 中 | 如 Phase 1 显示趋势，Phase 2 可扩展到 8-10 代 |

### 需要 Director 决策的问题

1. **GPU 预算**：完整实验矩阵需要 ~12 天 on 1× RTX PRO 6000。是否可以接受？是否有更多 GPU 可调度？
2. **Generation 加速**：是否投入时间集成 vLLM（预计 1-2 Worker-hours 开发 + 潜在 2-3x speedup）？可将实验周期压缩到 ~5 天。
3. **实验优先级**：如果 GPU 预算紧张，建议砍掉哪些 baselines？推荐保留 B0（已有）、B1-50、PI 作为最小集。
4. **论文方向**：Plan A 实验结果若正面，目标会议是 EMNLP 2026（deadline 约 2026-06）还是更后面的 venue？这影响实验规模的取舍。
5. **Seed=0 复现实验**（mvp_seed0_replication_r2）当前状态为 RUNNING。其结果是否是 Plan A 的前置依赖？（如果 collapse 行为不 seed-robust，Plan A 的前提就不成立。）

### 开放的技术问题

- **Entropy 的绝对值 vs 相对值**：不同模型/数据集的 G0 baseline entropy 不同。控制器参数是否需要 normalize？（建议后续实验验证。）
- **Real data 重复使用**：5 代实验中 real data 被重复使用（每代的 real portion 来自同一 train set），是否会导致过拟合？如何区分 "PI 控制器的效果" 和 "real data 多轮训练的效果"？
- **Mixed training 的 gradient dynamics**：Real 和 synthetic data 的 loss landscape 可能不同，简单按比例混合是否最优？还是应该用 alternating batches 或 weighted loss？

---

**参考文献：**

[1] An et al., "A PID Controller Approach for Stochastic Optimization of Deep Networks," CVPR 2018
[2] "Accelerated optimization in deep learning with a proportional-integral-derivative controller," Nature Communications, 2024
[3] "Incremental PID Controller-Based Learning Rate Scheduler for Stochastic Gradient Descent," IEEE TNNLS, 2022
[4] Fan et al., "DoGE: Domain Reweighting with Generalization Estimation," ICML 2024
[5] Bai et al., "Aioli: A Unified Optimization Framework for Language Model Data Mixing," ICLR 2025
[6] Shumailov et al., "AI Models Collapse When Trained on Recursively Generated Data," Nature 2024
