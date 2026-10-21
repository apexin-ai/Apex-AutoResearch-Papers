# Post-MVP Experiment Skeleton: DC-GRPO

> 前提：MVP 验证通过（多轮方向 AUROC >= 0.85, cosine(d_syc, d_gen) < 0.3, LoRA 扰动 AUROC 下降 < 0.05）后执行。

---

## 1. 主实验：DC-GRPO 训练

### 训练目标

用三路 reward 信号做 GRPO 训练，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。

### Reward 定义

| Component | 定义 | 信号来源 | 作用 |
|-----------|------|----------|------|
| **R1** (Direction Alignment) | policy model 激活在 critical turn 沿 d_syc / d_gen 的 cosine 投影差。惩罚高 d_syc 投影，奖励高 d_gen 投影 | mid-layers (10-15) + deep layers (20-28) 的 hidden states | 检测 sycophantic 内部路径，即使表面输出正确 |
| **R2** (Contrastive) | 同一 prompt 下不同 rollout 间方向投影的对比分数。d_syc 投影低且 d_gen 投影高的 rollout 获得更高 reward | 同 R1 层提取，跨 rollout 对比 | 利用 GRPO 的 group-relative 结构，放大方向差异信号 |
| **R3** (Behavioral) | 基于 NLI (DeBERTa-v3) 的输出层行为评分：warranted revision 场景中修正得分高，unwarranted pressure 场景中坚持得分高 | 模型输出文本 | 行为层面的安全网，防止方向 reward 优化出表面不一致的输出 |

总 reward: R = alpha * R1 + beta * R2 + gamma * R3（权重通过 grid search 在小规模 validation 上确定）。

### 训练配置

- **模型**: Qwen3-8B（与 MVP 一致，避免跨架构迁移风险）
- **训练方式**: LoRA (rank 64) + GRPO
- **数据**: 多轮对话 rollout（warranted revision + sycophantic capitulation 混合）
- **方向校准**: 每 500 步重新计算 d_syc / d_gen（用近期 rollout 的激活），开销 < 5%
- **监控指标**: 方向判别力 AUROC（held-out）、R1-R3 disagreement frequency、reward 分布
- **预估 GPU**: ~55 H100-hours（含 rollout 生成、激活提取、训练）
- **预估时长**: ~3-4 天 (4x H100)

### 依赖 MVP 结果

- d_syc / d_gen 的具体层和 token 位置选择 --> 由 MVP Phase 2-4 确定
- R1 的投影计算公式细节 --> 取决于方向判别力的层分布
- R 的权重范围 --> 取决于 MVP 中观察到的方向投影值域

---

## 2. Baseline 列表

| Baseline | 描述 | 训练方式 | 预估 GPU | 共享基础设施 |
|----------|------|----------|----------|-------------|
| **Vanilla Qwen3-8B** | 无干预基线 | 不训练，仅评估 | ~1 hr (eval only) | -- |
| **R3-only** | 纯 behavioral reward GRPO | LoRA + GRPO, 仅用 R3 | ~35 hr | 与主实验共享 rollout 生成管线和 NLI 评分器 |
| **ACT-style** | Undifferentiated consistency training，复现 BCT/ACT 思路 | 在 clean/biased prompt 对上施加 L2 activation consistency loss | ~20 hr | 共享数据管线和评估代码 |
| **Binary Probe Penalty** | 复现 Linear Probe Penalties 思路 | 训练 binary linear probe（sycophantic vs. not），R_hat = R3 - lambda * S(t) | ~15 hr | 共享 R3 评分器；probe 在 policy model（非 reward model）上训练以公平对比 |

**Baseline 设计说明**:
- R3-only 是最关键的 baseline：如果 DC-GRPO (R1+R2+R3) 相对 R3-only 没有显著提升，则 representation-level reward 的价值存疑
- ACT-style 测试"不区分方向的 activation-level 信号"是否够用
- Binary Probe Penalty 测试"binary 分类 vs. directional decomposition"的差异

---

## 3. 核心 Ablation (A1-A4)

| ID | 配置 | 测试假设 | 预估 GPU | 优先级 |
|----|------|----------|----------|--------|
| **A1** | R1-only | 方向对齐 reward 单独是否足够引导训练 | ~15 hr (eval-only diagnostic，从主实验早期 checkpoint 分叉) | P1 |
| **A2** | R2-only | 对比 reward 单独是否足够 | ~15 hr (同上) | P1 |
| **A3** | R1+R2 (无 R3) | 去掉行为安全网后模型是否产生"内部正确但表面不一致"的输出 | ~20 hr (需完整训练) | P2, 条件执行 |
| **A4** | R3-only | 同 R3-only baseline，放在 ablation 框架中系统对比 | 0 hr (复用 baseline 结果) | P1 |

**执行策略**:
- A1, A2: 可从主实验的 checkpoint 分叉做短程训练（~2000 步），不需从头训练，省 GPU
- A3: 需完整训练循环。**条件执行**: 仅当 A2 显示 R2 单独有 >= 5pp 改进 AND 剩余预算允许时执行；否则裁剪或降至 50% 步数的 directional-signal-only run
- A4: 直接复用 R3-only baseline 的结果

### 依赖 MVP 结果

- 如果 MVP 中 d_syc / d_gen 判别力在某些层显著优于其他层，A1/A2 应聚焦最优层

---

## 4. 评估 Benchmark

### 4.1 SYCON Bench（主评估，多轮 sycophancy）

- **指标**: Turn-of-Flip (ToF) — 模型在第几轮 flip（越晚越好抗 sycophancy），Number-of-Flip (NoF) — 总 flip 次数（越少越好）
- **评估方式**: 多轮对话模拟，逐轮记录模型立场变化
- **预期**: DC-GRPO 应显著降低 NoF，提高 ToF（相对 vanilla 和 R3-only）
- **可提前准备**: 是，评估代码和数据可提前下载/适配

### 4.2 SycophancyEval（单轮 sycophancy）

- **指标**: answer-priming accuracy、follow-up doubt accuracy、ownership bias rate
- **评估方式**: 标准单轮 prompt 评测
- **预期**: DC-GRPO 不应 regress（单轮 sycophancy 不恶化）；理想情况下小幅改进
- **可提前准备**: 是

### 4.3 MT-Bench（通用多轮对话质量）

- **指标**: GPT-4 判分（1-10），分项评分（writing, roleplay, reasoning, math, coding, extraction, STEM, humanities）
- **评估方式**: 80 道两轮对话题，GPT-4 自动评分
- **预期**: DC-GRPO 与 vanilla 差距 < 0.5 分（证明训练不损害通用能力）
- **可提前准备**: 是，评估管线可提前搭建

### 4.4 MMLU（通用能力不退化）

- **指标**: 5-shot accuracy（57 个子任务加权平均）
- **评估方式**: 标准多选题评测
- **预期**: DC-GRPO 与 vanilla 差距 < 1pp
- **可提前准备**: 是

### 4.5 项目特有分析指标

| 指标 | 定义 | 用途 |
|------|------|------|
| Warranted Revision Rate | 模型初始错误时，经用户提供正确证据后修正的比例 | 主指标，越高越好 |
| Unwarranted Capitulation Rate | 模型初始正确时，经用户施压后错误改变立场的比例 | 越低越好，不能比 anti-sycophancy baseline 差 |
| Revision-Capitulation AUC | 两者的 tradeoff 曲线下面积 | 综合指标 |
| R1-R3 Disagreement Frequency | R1 和 R3 给出不同信号的比例 | 验证 representation-level reward 的增量价值 |
| Turn-depth Analysis | 修正率随 commitment depth (turn 2/3/4+) 的变化 | 验证多轮训练的必要性 |
| Direction Stability | 训练过程中 d_syc/d_gen 的 cosine 稳定性 | 监控方向漂移 |

---

## 5. GPU 预算分配草案

### 总预算: <= 200 H100-hours

| 类别 | 项目 | 预估 GPU-hr | 备注 |
|------|------|-------------|------|
| **MVP** | Phase 2-5（激活提取 + 方向计算 + LoRA 扰动检查） | **~9** | 已规划，无训练 |
| **主实验** | DC-GRPO full training | **~55** | 含 rollout + 激活提取 + 方向重校准 |
| **Baselines** | R3-only | **~35** | 与主实验共享 rollout 管线 |
| | ACT-style | **~20** | 共享数据管线 |
| | Binary Probe Penalty | **~15** | 共享 R3 评分器 |
| | Vanilla eval | **~1** | 仅推理 |
| **Ablations** | A1 + A2（从 checkpoint 分叉） | **~15** | 短程训练，合并计算 |
| | A4 | **0** | 复用 R3-only |
| **评估** | 所有模型 x 所有 benchmark | **~15** | 含 SYCON/SycophancyEval/MT-Bench/MMLU |
| **校准** | 方向重校准 + 方向迁移分析 | **~10** | 分散在训练过程中 |
| **Buffer** | 调试 + 意外重跑 | **~15** | |
| | **小计（mandatory）** | **~190** | |
| **条件** | A3 (R1+R2 无 R3) | **~20** | 仅当 A2 >= 5pp 且预算允许 |

### Checkpoint 共享策略

```
Qwen3-8B (base)
  |
  ├── MVP 验证 (forward pass only, 不修改模型)
  |
  ├── DC-GRPO training ──────────────────────┐
  |     ├── step 2000 checkpoint ──> A1 分叉  |
  |     ├── step 2000 checkpoint ──> A2 分叉  |
  |     └── final checkpoint ──> eval         |
  |                                           |
  ├── R3-only training (独立从 base 开始)     |
  |     └── final checkpoint ──> eval + A4    |
  |                                           |
  ├── ACT-style training (独立从 base 开始)   |
  |     └── final checkpoint ──> eval         |
  |                                           |
  └── Binary Probe Penalty (独立从 base 开始)
        └── final checkpoint ──> eval
```

A1/A2 从主实验 step 2000 checkpoint 分叉可节省约 20 H100-hours（不需重新做 warmup 阶段）。

### 预算风险

- **超支场景**: rollout 生成比预期慢（多轮对话长度不确定性大）—— 缓解措施：限制最大 turn 数为 5，truncate 过长对话
- **节省场景**: 如果 R3-only 表现出乎意料地好（接近 DC-GRPO），可提前终止部分 ablation，节省 ~20 hr
- **硬约束**: 如果 mandatory 部分接近 190 hr，A3 完全砍掉

---

## 6. 可提前准备的工作（不依赖 MVP 结果）

| 工作项 | 内容 | 状态 |
|--------|------|------|
| SYCON Bench 评估代码 | 下载/适配 ToF/NoF 计算脚本 | 可立即开始 |
| SycophancyEval 评估管线 | 标准评测代码 | 可立即开始 |
| MT-Bench 评估管线 | FastChat MT-Bench 适配 | 可立即开始 |
| MMLU 评估管线 | lm-eval-harness 配置 | 可立即开始 |
| GRPO 训练框架 | 基于 TRL 搭建 GRPO + LoRA 训练管线 | 可立即开始 |
| NLI 评分器 (R3) | DeBERTa-v3-base 加载 + stance consistency 评分逻辑 | 可立即开始 |
| 多轮 rollout 生成器 | 给定 prompt 生成多轮对话 + 记录模型立场 | 可立即开始 |

## 7. 依赖 MVP 结果才能确定的工作

| 工作项 | 依赖条件 | 影响 |
|--------|----------|------|
| R1 具体公式（层选择、token 位置） | MVP Phase 2-4 确定最优层/位置 | 决定激活提取的精确配置 |
| R2 对比方式（跨 rollout 投影差 vs. 绝对值） | MVP 中方向投影值域分布 | 决定 R2 归一化方式 |
| alpha/beta/gamma 搜索范围 | MVP 中 R1 值域 vs. R3 值域量级 | 避免某路 reward dominate |
| A3 是否执行 | A2 结果 + 剩余预算 | 条件执行 |
| 是否 pivot to characterization study | MVP AUROC < 0.80 | 整体方向改变 |

---

## 8. 已知限制与应对：R2 在二元设计下退化为 R1

### 数学推导

当前设计中 d_gen = -d_syc（二元 difference-in-means 的数学必然），代入 R2 公式：

```
R2 = cos(h_wr, d_gen) - cos(h_sc, d_syc)
   = cos(h_wr, -d_syc) - cos(h_sc, d_syc)
   = -cos(h_wr, d_syc) - cos(h_sc, d_syc)
```

而 R1 的定义：
- R1_wr = +cos(h_wr, d_gen) = -cos(h_wr, d_syc)
- R1_sc = -cos(h_sc, d_syc)

因此 **R2 = R1_wr + R1_sc**，即 R2 退化为同一 pair 两个 condition 的 R1 之和。R2 不提供独立于 R1 的梯度信号。

### 对 Ablation 的影响

- **A2 (R2-only) 失去意义**：R2-only 在数学上等价于 "对两个 condition 同时施加 R1"，无法测试 "对比信号是否独立有价值"
- **主实验 (R1+R2+R3)**：alpha * R1 + beta * R2 退化为 (alpha + beta) * R1_per_condition，即 R2 只放大了 R1 权重，不增加信息

### 替代方案

| 方案 | 思路 | 优先级 | 复杂度 |
|------|------|--------|--------|
| **S1: Rank-based contrastive reward** | 在 GRPO group 的 K 个 rollout 中，R2 奖励 wr-sc 投影差排名靠前的 rollout。不依赖 d_gen 的具体定义，只要求 pair 内投影差 large | **P0 — 优先尝试** | 低，只改 R2.compute_group |
| **S2: Neutral baseline 独立 d_gen** | 增加第三种 condition: neutral（无施压的正常对话），d_gen 从 warranted_revision vs neutral 计算，与 d_syc (capitulation vs neutral) 正交。打破 d_gen = -d_syc | P1 | 中，需扩展 Phase 1 数据 + Phase 3 方向计算 |
| **S3: Paired rollout divergence** | R2 = KL(proj_distribution_wr || proj_distribution_sc)，跨同一 pair 的多个 rollout 比较投影分布形状，而非均值 | P2 | 中，需要每个 pair 生成多个 rollout |

**决策节点**：MVP 完成后，先用 S1 替换当前 R2 跑主实验和 A2。如果 A2 (S1-based R2-only) vs A4 (R3-only) 差异仍不显著，再考虑 S2 扩展数据。

---

## 9. TRL 集成设计笔记

### TRL GRPOTrainer 接口分析

TRL >= 0.12 提供 `GRPOTrainer`，核心可覆写点：

| 方法 | 作用 | 覆写需求 |
|------|------|----------|
| `compute_rewards(prompts, completions)` | 计算 reward 信号 | **必须覆写**：注入 R1+R2+R3 |
| `generate_completions(prompts)` | 从 policy 生成 rollout | 需覆写：多轮对话生成（标准 GRPO 只做单轮） |
| `compute_loss(rewards, logprobs, ...)` | GRPO loss 计算 | 可能不需覆写（标准 GRPO loss 适用） |
| `training_step(batch)` | 单步训练 | 可能需覆写：插入激活提取 hook |

### DCGRPOTrainer 继承设计

```
trl.GRPOTrainer
    └── DCGRPOTrainer
          覆写:
            compute_rewards()  →  R1 + R2 + R3 组合
            generate_completions()  →  多轮 rollout + 激活提取
          新增:
            _extract_activations()  →  forward hook 提取 hidden states
            _recalibrate_directions()  →  每 N 步重计算 d_syc/d_gen
```

关键设计：`compute_rewards` 需要拿到 rollout 的中间层激活，但标准 GRPOTrainer 只传 text completions 给 reward function。解法：在 `generate_completions` 阶段用 forward hook 缓存激活，`compute_rewards` 阶段从缓存读取。

### 从零实现 vs TRL 集成 tradeoff

| 维度 | TRL 集成 | 从零实现 |
|------|----------|----------|
| 开发速度 | 快，复用 GRPO loss/sampling/logging | 慢，需重写 GRPO 核心逻辑 |
| 灵活性 | 受 TRL 接口约束，多轮对话和激活提取需要 workaround | 完全自由 |
| 维护成本 | TRL 版本升级可能破坏覆写 | 自行维护所有逻辑 |
| 可复现性 | 审稿人熟悉 TRL，易复现 | 需更详细的文档 |

**结论**：优先 TRL 集成。GRPO loss 数学是标准的，不值得重写。多轮生成和激活提取通过覆写 `generate_completions` + forward hook 实现，技术上可行。如遇 TRL 接口限制无法绕过，再 fallback 到从零实现。

### TRL 版本要求

- **最低**: trl >= 0.12（GRPOTrainer 首次引入）
- **推荐**: trl >= 0.15（GRPO 支持 custom reward functions，减少 monkey-patching）
- 实际部署前用 `pip install trl --upgrade` 取最新版，并验证 `from trl import GRPOTrainer` 可用
- 需要配合 `transformers >= 4.45`、`accelerate >= 0.34`
