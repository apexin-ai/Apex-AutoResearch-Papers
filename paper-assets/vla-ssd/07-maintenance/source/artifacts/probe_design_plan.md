# MVP Probe 技术方案 — VLA-SSD Phase 3

> 版本: v1.0 | 日期: 2026-05-15 | 状态: 待 Director 审查

## 1. Overview

**目标**: 验证 OpenVLA 7B 的隐状态是否编码了 task-progress 信息，且信号来自 task-semantic content 而非 positional shortcut。

**两组 Probe**:
1. **Temporal Distance Probe** — 给定同一轨迹中两个 timestep 的隐状态，预测归一化时间距离
2. **Sub-task Predicate Probe** — 给定单个 timestep 的隐状态，预测 BDDL sub-task predicates 的完成状态

**四组控制实验**:
- Control A: Timestep Fraction Oracle（位置信息上界）
- Control B: Cross-Trajectory Shuffle（负控制）
- Control C: Untrained Model Baseline（分离训练贡献 vs 架构偏差）
- Control D: DINO-V2 Feature Baseline（VLA vs 纯视觉特征）

**关键架构事实** (影响实验设计):

| 属性 | 值 |
|------|-----|
| LLM backbone | LLaMA 2 7B, 32 transformer layers + embedding layer = 33 hidden states (layer 0–32) |
| Hidden dim | 4096 |
| Position encoding | RoPE (Rotary Position Embedding) |
| Vision encoder | DINOv2 ViT-L/14 + SigLIP ViT-So400M/14, channel-wise fuse → MLP projector |
| Image tokens | 256 per observation (224×224 input, patch size 14, 16×16 grid) |
| Action tokens | 7 (one per DoF, each discretized into 256 bins, autoregressive) |
| Text tokens | ~10–30 (task instruction, fixed per task) |
| Sequence per timestep | ~256 + ~20 + 7 ≈ 283 tokens |

---

## 2. Temporal Distance Probe

### 2.1 关于 RoPE 的关键澄清

**OpenVLA 对每个 trajectory timestep 做独立的 forward pass**（输入当前 observation + language instruction → 输出 action tokens）。RoPE 编码的是 **sequence 内的 token position**（第几个 image patch、第几个 text token），**不是 trajectory timestep**。

由于每个 timestep 的 sequence 结构完全相同（256 image + ~20 text + 7 action），同一 token slot 在不同 timestep 的 RoPE rotation 完全一致。**因此 RoPE 不是 trajectory-level temporal distance probing 的直接混淆因素**。

如果 temporal distance probe 有效，信号必然来自 **content**（visual observation 和 language processing 产生的语义表示），而非 positional shortcut。

### 2.2 输入表示

**推荐方案: 绝对差值 |h_l(t_j) − h_l(t_i)|**

| 方案 | 维度 | 优点 | 缺点 |
|------|------|------|------|
| A: h(t_j) − h(t_i) | 4096 | 保留方向信息 | 非对称，需要 ordered pairs |
| **C: \|h(t_j) − h(t_i)\|** | **4096** | **对称（匹配对称目标）、维度紧凑** | **丢失方向** |
| B: [h(t_i); h(t_j)] | 8192 | 最大表达力 | 维度翻倍，非对称，probe 复杂度高 |

选择 C 的理由:
- 目标 |t_j − t_i|/T 是对称的，输入也应对称
- 维度 4096 = 单隐状态大小，线性 probe 参数仅 4097
- 对于"信息是否存在"的 probing 实验，限制 probe 复杂度是好事
- 绝对值保留了差异的幅度信息

**Ablation**: 方案 B（concatenation）作为 upper-bound 对比——如果 B >> C，说明方向信息重要。

### 2.3 Token 维度聚合

每个 timestep 的 forward pass 产生 hidden states shape = (seq_len ≈ 283, 4096)，需聚合为单个 4096-dim 向量。

**主方案: Last pre-action token**
- 取 sequence 中 action tokens 之前的最后一个 token（即最后一个 text token 或 separator token）
- 理由: autoregressive model 在此位置汇聚了全部 image + text context，是 action prediction 的"决策点"
- 实现: `h = hidden_states[layer][0, -(num_action_tokens+1), :]`

**对比方案: Image token mean-pooling**
- `h = hidden_states[layer][0, :256, :].mean(dim=0)`
- 仅捕获视觉信息，排除语言理解的贡献
- 对比两种聚合方式可揭示 temporal signal 是视觉驱动还是多模态

### 2.4 输出与损失

| 项目 | 选择 |
|------|------|
| 任务类型 | Regression |
| 目标值 | \|t_j − t_i\| / T ∈ [0, 1]，T = trajectory length |
| 模型 | Linear probe: ŷ = w^T x + b, w ∈ R^4096, b ∈ R |
| 损失 | MSE |
| 主指标 | Spearman ρ (rank correlation，对单调变换不变) |
| 辅指标 | R², MAE |

不用 classification bins 的理由: regression 直接产出连续预测，与 Spearman ρ 评估自然对齐；bin 边界引入额外超参数且丢失排序精度。

### 2.5 训练配置

| 超参数 | 值 |
|--------|-----|
| Optimizer | Adam |
| Learning rate | 1e-3 (linear probe 标准) |
| Weight decay | 0 |
| Batch size | 256 pairs |
| Epochs | 50 (early stopping, patience=5, monitor val Spearman ρ) |
| Probe 数量 | 33 layers × 2 aggregation methods = 66 probes |

---

## 3. RoPE Position Controls

### 3.1 Control A: Timestep Fraction Oracle

**目的**: 确立纯位置信息能达到的理论上限。

**设计**:
- 输入: 标量 |t_i/T − t_j/T| ∈ [0, 1]
- 目标: |t_j − t_i|/T（与 VLA probe 相同）
- 模型: 线性回归 ŷ = w·x + b

**预期**: ρ ≈ 1.0（输入即目标，线性完美拟合）

**解读**: 这不是要"打败"的 baseline，而是 **ceiling**。VLA probe 的 ρ 相对于 1.0 的差距反映了从高维隐状态提取 temporal distance 的难度。如果 VLA ρ > 0.3，说明 temporal distance 在隐状态中是 linearly accessible 的。

> **注意**: Roadmap 中 PASS 判据 "VLA > timestep-baseline (Δρ > 0.1)" 在当前目标定义下不成立——标量输入 |t_i/T − t_j/T| 恒等于目标，任何高维 probe 都无法超越。建议修改为 **VLA > untrained-model (Δρ > 0.1)**，见 Control C。此修改需 Director 确认。

### 3.2 Control B: Cross-Trajectory Shuffle

**目的**: 负控制——验证 probe 依赖 trajectory-specific content 而非 universal shortcut。

**设计**:
1. Probe 仅在 **within-trajectory pairs** 上训练（与主实验相同）
2. 测试集分两组:
   - **Within-trajectory** (held-out trajectories): 正常评估
   - **Cross-trajectory**: 从不同 trajectory 各取一帧配对

**Cross-trajectory 配对方案**:

| 类型 | 帧来源 | Pseudo-distance 定义 | 预期 ρ |
|------|--------|---------------------|--------|
| Cross-task | 不同 task 的 trajectory | \|t_i/T_A − t_j/T_B\| | ≈ 0 (无意义) |
| Same-task cross-demo | 同 task 不同 demo | \|t_i/T_A − t_j/T_B\| | 可能 > 0 (如果 VLA 编码了 task-level progress) |

**实现**:
```python
# Cross-trajectory pair generation
for task_a, task_b in combinations(tasks, 2):  # cross-task
    traj_a = random.choice(demos[task_a])
    traj_b = random.choice(demos[task_b])
    t_i = random.randint(0, len(traj_a)-1)
    t_j = random.randint(0, len(traj_b)-1)
    h_i = hidden_states[task_a][traj_a][t_i]
    h_j = hidden_states[task_b][traj_b][t_j]
    pseudo_dist = abs(t_i/len(traj_a) - t_j/len(traj_b))
    # Evaluate trained probe on (|h_j - h_i|, pseudo_dist)
```

**预期结果**:
- Cross-task ρ ≈ 0: 不同任务的帧之间，probe 无法预测 pseudo-distance → 信号是 task-specific content
- Same-task cross-demo ρ > 0: 如果成立，表明 VLA 编码了 task-level progress pattern（positive evidence）

### 3.3 Control C: Untrained Model Baseline（推荐的核心控制实验）

**目的**: 分离 VLA 训练带来的 task-semantic 信息 vs 架构本身（vision encoder + 随机 LLM）的偏差。

**设计**:
1. 加载 OpenVLA 架构
2. **保留** pretrained vision encoders（DINOv2 + SigLIP）和 projector
3. **随机重新初始化** LLaMA 2 7B backbone 的全部权重
4. 对相同输入提取隐状态
5. 训练相同的 temporal distance + sub-task predicate probes

**理由**:
- 训练和未训练模型共享相同的 vision pipeline → 输入到 LLM 的 visual tokens 相同
- 训练和未训练模型共享相同的 RoPE → 任何 RoPE position bias 在两者中一致
- **差异 = VLA 训练的贡献**

**具体实现**:
```python
from openvla import OpenVLAForActionPrediction

# Trained model
model_trained = OpenVLAForActionPrediction.from_pretrained("openvla/openvla-7b")

# Untrained control
model_untrained = OpenVLAForActionPrediction.from_pretrained("openvla/openvla-7b")
# Reinitialize LLM backbone only
for name, param in model_untrained.named_parameters():
    if "llm" in name or "language_model" in name:
        if param.dim() >= 2:
            torch.nn.init.xavier_normal_(param)
        else:
            torch.nn.init.zeros_(param)
# Keep vision encoder + projector weights intact
```

**PASS 判据（建议替代 Roadmap 原方案）**:
- Δρ(trained − untrained) > 0.1 → VLA 训练贡献了 task-semantic temporal signal
- Δρ ≤ 0.1 → signal 来自 vision encoder 而非 VLA 训练，核心假设受挑战

### 3.4 Control D: DINO-V2 Feature Baseline

**目的**: VLA 隐状态 vs 纯视觉特征的直接对比。

**设计**:
- 对同一 observation images 直接用 DINOv2 ViT-L/14 提取 [CLS] token 或 mean-pooled patch features
- 维度: 1024 (ViT-L/14 hidden dim)
- 训练相同架构的 temporal distance + sub-task predicate probes

**解读**:
- VLA ≥ DINO-V2: VLA representation 至少与纯视觉一样好（可能融合了 language/action 信息）
- VLA < DINO-V2: VLA 的 LLM processing 可能损失了某些视觉 temporal signal（仍可作为 negative finding 发表）

---

## 4. Sub-task Predicate Probe

### 4.1 LIBERO BDDL Predicates

LIBERO 使用 BDDL (Behavioral Domain Definition Language) 定义 task goal 和 sub-task。基于文献和代码库，可用的 predicate 类型:

**状态 predicates (unary)**:
| Predicate | 含义 | 示例 |
|-----------|------|------|
| `open(X)` | 物体 X 处于打开状态 | open(top_drawer) |
| `close(X)` | 物体 X 处于关闭状态 | close(microwave) |
| `turnon(X)` | 设备 X 处于开启状态 | turnon(stove) |
| `turnoff(X)` | 设备 X 处于关闭状态 | turnoff(lamp) |

**空间 predicates (binary)**:
| Predicate | 含义 | 示例 |
|-----------|------|------|
| `on(A, B)` | A 在 B 上方 | on(bowl, shelf) |
| `in(A, B)` | A 在 B 内部 | in(mug, microwave) |

**动作 predicates**:
| Predicate | 含义 | 示例 |
|-----------|------|------|
| `grasped(X)` | 机器人正在抓取 X | grasped(red_mug) |

LIBERO-Long 是 10 个 long-horizon compositional task，每个 task 包含 3–5 个顺序 sub-goals，每个 sub-goal 由 1–2 个 predicate 定义。task 涉及混合的 object manipulation、spatial rearrangement 和 state changes。

### 4.2 Ground Truth 获取

LIBERO demo HDF5 文件存储 observations (images, proprioception) 和 actions，但**不直接存储 predicate 完成状态**。需要从 simulator 回放获取:

**方案: Simulator Replay + Predicate Query**
```python
import libero.envs
from libero.envs import SubTaskCompletionObservable  # if available

env = make_libero_env(task_bddl_file)
for demo in demos:
    env.reset()
    for t, action in enumerate(demo.actions):
        obs, reward, done, info = env.step(action)
        # Query predicate states from environment
        predicate_states = env.get_goal_predicate_states()
        # predicate_states: dict {predicate_name: bool}
        labels[t] = predicate_states
```

**备选方案**: 如果 LIBERO 环境 API 不直接暴露 predicate states，从 MuJoCo sim state 计算:
- `on(A, B)`: A 的 z 坐标 > B 的 z 坐标 + threshold，且 xy 距离 < threshold
- `in(A, B)`: A 在 B 的 bounding box 内
- `open(X)`: joint angle > threshold
- `grasped(X)`: gripper contact force > 0 且 gripper 在 X 附近

### 4.3 Probe 架构

**Multi-label binary classification**:
- 输入: h_l(t) ∈ R^4096（单 timestep、单 layer 隐状态）
- 模型: σ(W h + b)，W ∈ R^{K×4096}，b ∈ R^K
- K = task 中 predicate 总数（每个 task 不同，典型 6–15 个 predicates）
- 损失: Binary cross-entropy (per predicate)
- 指标: AUC-ROC per predicate, macro-averaged AUC

**训练策略**:
- 每层独立训练一个 probe（共 33 probes per task）
- 跨所有 10 个 LIBERO-Long tasks 训练统一 probe 不可行（predicates 不同），按 task 分别训练
- 最终报告: 每层的 macro-AUC across tasks

**Class imbalance 处理**:
- 大部分 predicates 在 trajectory 早期为 False，后期变为 True
- 使用 AUC-ROC（对 class imbalance 鲁棒）而非 accuracy
- 如果某 predicate 在 >99% timesteps 为同一值，排除该 predicate（参考 Lu et al. 2025）

### 4.4 训练配置

| 超参数 | 值 |
|--------|-----|
| Optimizer | Adam |
| Learning rate | 1e-3 |
| Batch size | 512 timesteps |
| Epochs | 50 (early stopping, patience=5, monitor val macro-AUC) |
| Token aggregation | 与 temporal distance probe 一致（last pre-action token） |

---

## 5. Data Split Strategy

### 5.1 LIBERO-Long 数据规模

| 项目 | 估计值 |
|------|--------|
| Tasks | 10 |
| Demos per task | 50 |
| Total trajectories | 500 |
| Timesteps per demo | ~300–600 (20Hz, long-horizon tasks) |
| Estimated avg | ~400 timesteps |
| Total timesteps | ~200,000 |

> 注: 精确数值需在加载数据后确认。LIBERO demo 最大 episode length 为 600 timesteps。

### 5.2 Train/Val Split

**按 trajectory 划分**（严禁同一 trajectory 的 timestep 跨 train/val）:

| 集合 | Trajectories per task | Total trajectories | 估计 timesteps |
|------|----------------------|-------------------|---------------|
| Train | 40 | 400 | ~160,000 |
| Val | 10 | 100 | ~40,000 |

划分方式: 每个 task 内随机选 10 条 trajectory 作为 val，固定 seed 确保可复现。

### 5.3 Temporal Distance Pair 采样

All-pairs 数量过大: C(400, 2) ≈ 80,000 pairs per trajectory → 40M pairs total。需要采样。

**采样策略: Distance-stratified sampling**
1. 将 normalized distance [0, 1] 等分为 10 个 bin: [0, 0.1), [0.1, 0.2), ..., [0.9, 1.0]
2. 每个 trajectory 每个 bin 采 50 pairs
3. 每 trajectory 共 500 pairs

| 集合 | Pairs per trajectory | Total pairs |
|------|---------------------|-------------|
| Train | 500 | 200,000 |
| Val | 500 | 50,000 |

**Stratification 的理由**: 随机采样会偏向中等距离（组合数最多在 distance ≈ 0.5 附近）。均匀采样所有距离 bin 确保 probe 在全范围内受到训练。

### 5.4 Sub-task Predicate Data

不需要 pair 采样——每个 timestep 独立作为一个样本:
- Train: ~160,000 timesteps
- Val: ~40,000 timesteps

---

## 6. Implementation Notes

### 6.1 计算资源

**服务器**: westd-19183, 2× RTX PRO 6000 (48GB VRAM each)

### 6.2 Feature Extraction（最耗时步骤）

| 步骤 | 内存 | 时间估计 |
|------|------|----------|
| OpenVLA 7B fp16 加载 | ~14GB VRAM | — |
| Forward pass (batch=4, seq≈283) | ~20GB VRAM | ~50ms/sample |
| 200K samples 提取 | — | ~2.5h (单 GPU) |
| Untrained model 提取 | 同上 | ~2.5h (第二 GPU 并行) |
| DINO-V2 特征提取 | ~2GB VRAM | ~30min |

**并行策略**: GPU 0 跑 trained OpenVLA，GPU 1 跑 untrained control，同时完成。DINO-V2 在任一 GPU 上快速完成。

### 6.3 Hidden State 存储

每 timestep 存储 33 layers × 4096 dims × 2 bytes (fp16) = 270KB:

| 模型 | Timesteps | 存储 |
|------|-----------|------|
| Trained OpenVLA | 200K | ~54 GB |
| Untrained OpenVLA | 200K | ~54 GB |
| DINO-V2 | 200K | ~0.4 GB (单层 1024-dim) |

**总存储**: ~110 GB。需确认服务器磁盘空间。

**优化**: 如果磁盘紧张，可分 task 提取和训练，每次只存 1 个 task 的特征 (~11 GB)。

### 6.4 Probe 训练

| 项目 | 估计时间 |
|------|----------|
| 单个 linear probe (200K × 4096 → 1) | < 1 min (GPU) |
| Temporal distance: 33 layers × 2 agg × 3 models (trained/untrained/DINO) | ~3h |
| Sub-task predicate: 33 layers × 10 tasks × 3 models | ~5h |
| 总 probe 训练 | ~8h |

### 6.5 总时间预估

| 阶段 | 时间 |
|------|------|
| 环境搭建 + 数据下载 | 2–4h |
| Feature extraction (all models) | 3–4h (并行) |
| Predicate ground truth 提取 (simulator replay) | 2–3h |
| Probe 训练 + 评估 | 8–10h |
| **Total** | **~16–20h** |

符合 Roadmap 预估的 ~12–16 GPU 小时（加上环境搭建开销）。

### 6.6 Implementation Priority

1. **P0**: Feature extraction pipeline (OpenVLA forward pass + hidden state caching)
2. **P0**: Temporal distance probe + Control A (oracle baseline)
3. **P0**: Control C (untrained model) — 这是核心控制实验
4. **P1**: Sub-task predicate ground truth extraction (simulator replay)
5. **P1**: Sub-task predicate probes
6. **P1**: Control B (cross-trajectory) + Control D (DINO-V2)
7. **P2**: Ablations (concatenation input, image-only pooling)

---

## Appendix: 需 Director 确认的决策点

1. **PASS 判据修改**: 建议将 "VLA > timestep-baseline (Δρ > 0.1)" 改为 "VLA > untrained-model-baseline (Δρ > 0.1)"。原因: timestep fraction oracle 在当前目标定义下 ρ ≈ 1.0，VLA 不可能超越。Untrained model baseline 是更有意义的 RoPE/architecture 控制。

2. **Token aggregation 选择**: 推荐 last pre-action token 作为主方案。如 Director 偏好 mean-pooling 或其他方案，可调整。

3. **存储空间**: 全量 hidden state 需 ~110GB。如服务器磁盘不足，需改为分 task 提取的 streaming 策略。

4. **LIBERO-Long predicate 获取**: 需确认 LIBERO simulator API 是否直接暴露 predicate states。如不支持，需从 sim state 手动计算（增加 ~1 天开发时间）。
