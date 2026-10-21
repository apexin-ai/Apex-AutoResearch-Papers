# LIBERO-Goal Instruction-Conditioned Probe 可行性评估

> 日期: 2026-05-15 (updated) | 项目: vla-ssd

---

## 1. Grant et al. 2026 关键发现

**"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"**
arXiv:2603.19233 | ICLR 2026 Workshop MM Intelligence | Case Western Reserve University

### 1.1 实验规模

- 6 个 VLA 模型 (80M–7B): π0.5, OpenVLA-OFT, X-VLA (~1B, 24 layers, Florence-2), SmolVLA, GR00T N1.5, ACT
- 方法: activation injection + 424 SAEs (TopK k=64) + linear probes
- 总 rollout: 394K+ episodes，跨 4 个 LIBERO suites + SimplerEnv

### 1.2 LIBERO-Goal vs LIBERO-Object：语言敏感性的关键对比

**LIBERO-Goal (shared scene, language-critical):**

| Model | Correct Prompt | Null Prompt | Wrong Object |
|-------|---------------|-------------|--------------|
| π0.5 | 83.3% | 80% | 76.7% |
| OFT | 100% | 10% | 10% |
| X-VLA | 94% | 10% | 4-10% |
| GR00T | 97% | 0% | 0% |

**LIBERO-Object (distinct scenes, vision-sufficient):**

| Model | Correct Prompt | Null Prompt | Wrong Object |
|-------|---------------|-------------|--------------|
| π0.5 | 77.4% | 77% | 74.2% |
| OFT | 100% | 100% | 100% |
| X-VLA | 100% | 60% | 60-90% |

**核心结论**: 语言敏感性取决于 task structure（scene 是否 ambiguous），而非模型架构。OFT/X-VLA/GR00T 在 LIBERO-Goal 上 collapse 到 0-10%；π0.5 衰减较小（可能因其 dual-pathway 架构保留了更多视觉 prior）。

### 1.3 线性 Probe 的 Paradox（对我们至关重要）

**π0.5 Layer 17: 99.3% prompt classification accuracy，但行为几乎不受 prompt 影响。**

这意味着：模型在中间层 **密集编码了语言信息**，但没有将其路由到 motor pathway。"Prompts are encoded but not used"——视觉主导 action generation，语言信息在 LIBERO-Object 等 vision-sufficient 场景中被 bypass。

**GR00T N1.5**: 100% task identification + 96.4% success prediction（32 层均一致）。

**与我们的关系**: Grant 的 probe 在 fine-tuned models 的 **rollout episodes** 上做 task ID。我们在 **offline demo features** 上做 instruction identity，且对比 **trained vs untrained**——这是他们没有做的。

### 1.4 SAE 分析

- 6 个模型上 82+ manipulation concepts（motion primitives, object categories, spatial relationships）
- 频率加权 contrastive selection (Cohen's d)
- 43-82 distinct concepts per model
- Causal ablation: 28-92% zero-effect rates（很多 feature 对行为无影响）

### 1.5 Counterfactual 条件设计（6 种）

Baseline (correct), null prompt (empty), negation ("Don't pick up X"), motor command ("Move slowly"), object swap, temporal switches.

---

## 2. 相关工作与 Novelty Gap 分析

### 2.1 Swann, McGranahan, **Buurmeijer**, Kennedy, Schwager (2026)

**"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models"**
arXiv:2603.19183 | Stanford University

- 模型: π0.5 (primary) + OpenVLA
- 数据: LIBERO (4 suites, 1693 episodes, 40 tasks) + DROID (2000 episodes, 1545 tasks)
- **发现**: VLA 存在大量 episode-level memorization；larger/diverse datasets (DROID) 产生更多 generalizable features
- **Feature 类型**: general (grasping, transport, alignment) vs memorized (episode-specific sequences)
- 79% features interpretable, steering experiments 验证因果影响
- **与我们的关系**: 他们关注 sensorimotor features，**没有分析 language-related features**，没有 trained vs untrained 对比

### 2.2 LIBERO-CF (2026)

**"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs"**
arXiv:2602.17659

- 首个 VLA counterfactual benchmark（CF-Spatial, CF-Object, CF-Long, CF-OOD）
- **Modality ablation**: VLA 维持 94-97% vision-only success，language-only collapse 到 ~0%
- π0.5 best model 也只有 30.8% grounding / 13.2% task success on counterfactual instructions
- **Bayesian 解释**: VLAs collapse 到 P(a|o) 而非正确加权 P(a|l,o)。Language 是 secondary conditioning signal
- Object removal 实验: 移除 training-task objects → counterfactual performance +25.4%
- **与我们的关系**: 他们测 behavioral 层面的 counterfactual failure（intervention），我们测 representational 层面的 instruction encoding（probing）。互补。

### 2.3 INT-ACT (2026)

**"From Intention to Execution: Probing the Generalization Boundaries of VLA Models"**
arXiv:2506.09930

- 提出 "intention-action gap"：VLA 在 OOD shifts 下维持高 semantic intent，但 motor success 大幅下降
- **与我们的关系**: 他们 probe "intention" 的 generalization，我们 probe instruction identity 的 **training-dependent encoding**

### 2.4 Novelty Gap 总结

| 论文 | 做了什么 | **没有做什么**（我们的空间） |
|------|---------|---------------------------|
| Grant 2026 | Behavioral language sensitivity (causal, 6 models) | Trained vs untrained; layer×timestep granularity |
| Swann/Buurmeijer 2026 | SAE feature interpretability + steering | No language features; no training effect comparison |
| LIBERO-CF 2026 | Counterfactual behavioral benchmark | No representation analysis |
| INT-ACT 2026 | Intention probing under OOD | No shared-scene instruction discrimination |

**我们的独特贡献**:
1. **Trained vs untrained VLA** — 唯一一篇对比 VLA 训练前后的 instruction encoding
2. **Layer × timestep granularity** — 33 层 × early/mid/late timesteps 的细粒度分析
3. **Vision-unsolvable probing target** — early timestep + shared scene = 纯 vision baseline 无法区分
4. **Offline demo probing** — 无需 rollout 环境，可复现性强

---

## 3. LIBERO-Goal 数据集规格

### 3.1 Suite 设计

LIBERO-Goal 是 LIBERO benchmark 的 4 个主要 suite 之一（Spatial / Object / Goal / 100）。**核心特征：10 个 task 共享同一 kitchen scene（相同物体、相同空间布局），仅 goal 不同。** 视觉 ambiguous，必须依赖 instruction 区分 task。

### 3.2 完整 Task 列表（10 tasks）

| # | Task Name | Language Instruction | HDF5 Size |
|---|-----------|---------------------|-----------|
| 1 | open_the_middle_drawer_of_the_cabinet | Open the middle drawer of the cabinet | 702 MB |
| 2 | open_the_top_drawer_and_put_the_bowl_inside | Open the top drawer and put the bowl inside | 1.02 GB |
| 3 | push_the_plate_to_the_front_of_the_stove | Push the plate to the front of the stove | 763 MB |
| 4 | put_the_bowl_on_the_plate | Put the bowl on the plate | 468 MB |
| 5 | put_the_bowl_on_the_stove | Put the bowl on the stove | 509 MB |
| 6 | put_the_bowl_on_top_of_the_cabinet | Put the bowl on top of the cabinet | 510 MB |
| 7 | put_the_cream_cheese_in_the_bowl | Put the cream cheese in the bowl | 536 MB |
| 8 | put_the_wine_bottle_on_the_rack | Put the wine bottle on the rack | 879 MB |
| 9 | put_the_wine_bottle_on_top_of_the_cabinet | Put the wine bottle on top of the cabinet | 540 MB |
| 10 | turn_on_the_stove | Turn on the stove | 448 MB |

**总计: 6.37 GB, 10 tasks × 50 demos = 500 trajectories**

### 3.3 Task 特征分析（对 probing 的影响）

- Tasks 4-6 (bowl → plate/stove/cabinet) 共享 object (bowl) 但 target location 不同 → **同 object 不同 goal 的 subset**
- Tasks 8-9 (wine bottle → rack/cabinet) 类似
- Task 1 vs 10 (drawer vs stove) → **完全不同的操作对象和动作**
- 这种 hierarchical structure 可支持 sub-group 分析（within-object vs cross-object instruction discrimination）

### 3.4 HDF5 格式（与现有 LIBERO-10 完全兼容）

```
data/demo_{i}/obs/agentview_rgb     (T, 128, 128, 3) uint8
data/demo_{i}/obs/eye_in_hand_rgb   (T, 128, 128, 3) uint8
data/demo_{i}/actions               (T, 7) float64 [3D pos delta + 3D rot delta + gripper]
```

- 每 task 50 demos，每 demo 220-290 timesteps，max 300 steps
- 20 Hz control frequency, Franka Panda arm
- **`extract_features.py` 可直接使用，无需修改数据加载代码**

### 3.5 下载

```bash
# HuggingFace (推荐)
huggingface-cli download yifengzhu-hf/LIBERO-datasets --include "libero_goal/*" --local-dir ./data/

# 或 LIBERO 官方脚本
python benchmark_scripts/download_libero_datasets.py --datasets libero_goal --use-huggingface
```

AutoDL 注意: `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + SSL certs.

---

## 4. Instruction-Conditioned Probe 方案

### 4.1 核心思想

> 同一 visual scene + 不同 instruction → hidden states 是否编码了 instruction identity？

直接回应 MVP 失败的根因：temporal distance 是 vision-solvable，所以需要 **vision-unsolvable** 的 probing target。LIBERO-Goal trajectory 开头视觉几乎相同（共享 scene），只有 instruction 不同——天然的 vision-unsolvable 信号。

### 4.2 Probe 架构

```
Input:  h_t ∈ R^4096  (layer l, timestep t 的 hidden state)
Probe:  Linear(4096, 10) + softmax  →  10-way classification
Target: instruction identity (哪个 task)
Loss:   CrossEntropy
```

每层单独训练一个 linear probe，沿用 last_preaction token 位置。

### 4.3 对比条件（4 models）

| Condition | Has instruction tokens? | Has trained LLM? | Has vision? | 预期 early-step accuracy |
|-----------|------------------------|-------------------|-------------|------------------------|
| Trained VLA | Yes | Yes | Yes | **高 (70-90%)** |
| Untrained VLA | Yes | No (random LLM) | Yes (SigLIP preserved) | **中 (30-50%)** — token embeddings 提供 partial signal |
| DINO-V2 | No | No | Yes | **低 (~10% = chance)** — 强 control |
| SigLIP only | No | No | Yes | **低 (~10%)** — 另一个 vision control |

### 4.4 关键实验

**Exp A: Full-Trajectory Instruction Identity Probe**
- 所有 timestep 的 hidden states
- 预期: 随着 trajectory 推进，视觉分歧增大，vision-only 也能区分

**Exp B: Early-Timestep Probe（核心实验）**
- 只用前 K 步 (K=5, 10, 20)
- 理由: trajectory 开头视觉场景几乎相同，行为尚未分化
- **关键指标**: Δ_acc(trained VLA − DINO) @ K=5

**Exp C: Layer-wise Analysis**
- 33 层的 instruction identity accuracy profile
- 预期: early layers (vision-dominated) 低，middle/late layers (LLM-processed) 高
- 与 Grant 的 99.3% finding 对照：trained 在哪些层 encode instruction？untrained 呢？

**Exp D: Sub-group Analysis**
- Within-object pairs (bowl→plate vs bowl→stove vs bowl→cabinet): harder, requires fine-grained goal distinction
- Cross-object pairs (bowl tasks vs wine bottle tasks): easier, object identity helps
- 如果 trained VLA 在 within-object 也高 accuracy → 更强的 claim

### 4.5 Train/Test Split

- 每 task 50 demos: 40 train / 10 test (stratified)
- K=10: 10 classes × 40 × 10 = 4000 train, 1000 test
- Linear probe 足够

### 4.6 Confound 控制

| Confound | 风险 | 控制 |
|----------|------|------|
| t=0 视觉微小差异 | 低 | 检查 DINO t=0 accuracy；如果 >20% → probe premise 有问题 |
| Instruction tokens 直接泄露 | 高（但不是 bug） | Untrained 对比：也有 instruction tokens 但缺 grounded encoding |
| Trajectory 长度分布差异 | 中 | 固定 K，不用 relative position |
| OpenVLA 未在 LIBERO-Goal 上 fine-tune | 中 | 不需要 task success — 只需 hidden states 编码 instruction；通用 prompt format 足够 |

---

## 5. 时间/资源估算

### 5.1 数据下载 + 验证

| 步骤 | 耗时 |
|------|------|
| LIBERO-Goal HDF5 (6.37 GB) | ~30 min |
| 验证 HDF5 兼容 + t=0 visual check | ~10 min |

### 5.2 特征提取 (GPU time, 2×RTX PRO 6000)

| 模型 | 方案 A (全 33 层) | 方案 B (8 关键层) |
|------|------------------|------------------|
| Trained OpenVLA | ~3h | ~1h |
| Untrained OpenVLA | ~3h | ~1h |
| DINO-V2 | ~15 min | ~15 min |
| SigLIP | ~15 min | ~15 min |
| **总计** | **~6.5h** | **~2.5h** |

### 5.3 存储

| 数据 | 方案 A | 方案 B |
|------|--------|--------|
| 原始 HDF5 | 6.37 GB | 6.37 GB |
| Trained features | ~53 GB | ~13 GB |
| Untrained features | ~53 GB | ~13 GB |
| DINO + SigLIP | ~1 GB | ~1 GB |
| **总计** | **~113 GB** | **~34 GB** |

当前 `/root/autodl-tmp/` 已有 ~107 GB LIBERO-10 features。方案 B 需额外 34 GB，可行。方案 A 需清理旧数据。

### 5.4 Probe 训练 + 分析

- Linear probe 训练: 每层 < 1 min
- 33 layers × 4 models × 3-4 K values ≈ ~2h
- 分析、绘图、写报告: ~1h

### 5.5 总工时

| 阶段 | 方案 A | 方案 B (推荐) |
|------|--------|--------------|
| 数据下载 + 验证 | 0.5h | 0.5h |
| 特征提取 | 6.5h | 2.5h |
| Probe 训练 + 分析 | 3h | 3h |
| **端到端** | **~10h** | **~6h** |

---

## 6. 风险分析

### 6.1 实验可能 FAIL 的场景

| 风险 | 概率 | 后果 | 缓解 |
|------|------|------|------|
| **LIBERO-Goal t=0 视觉其实不同** — 初始 arm pose 或 scene layout 因 task 而异 | 中 | Probe premise 不成立，DINO 也能高 accuracy → 实验无价值 | **下载后立即验证** t=0 DINO cosine similarity；如果 10 个 task 的 t=0 两两 sim > 0.95 → OK；否则 abort |
| **Untrained VLA 也高 accuracy** — random LLM 的 token embeddings 足以区分 instruction | 中-高 | "VLA training contributes instruction grounding" claim 不成立 | 这种情况下 pivot 到 "where in the network does instruction info reside"，仍有 layer-wise 贡献 |
| **Trained VLA accuracy 也低 (~10-20%)** — OpenVLA 未在 LIBERO-Goal 上 fine-tune，instruction 未被 grounded | 低-中 | Negative result → instruction encoding 确实 weak | 报告为 negative result；与 Grant 的 behavioral finding (94%→10%) 对比分析 |
| **存储空间不足** | 中 | 无法存全部 features | 用方案 B (8 层) 或清理 LIBERO-10 旧 features |
| **OpenVLA prompt format 不匹配** | 低 | 模型收到格式异常的 instruction → hidden states 不正常 | 测试前用 1 个 demo 验证 forward pass 输出合理 |

### 6.2 "这条路也 FAIL" 的最坏情况

如果 trained VLA accuracy ≈ untrained ≈ DINO（都能或都不能区分），说明：
- LIBERO-Goal 的 "shared scene" 其实在 pixel level 已经可区分
- 或 OpenVLA 的 instruction processing 根本不工作（因为没有在 LIBERO-Goal 上 fine-tune）

此时 instruction probe 作为 **informative negative** 仍有价值：证明 VLA 训练的 instruction grounding 在 out-of-distribution scenes 上失效，与 LIBERO-CF 的 findings 一致。

---

## 7. Go/No-Go 建议

### Decision Matrix

| 因素 | 评分 | 说明 |
|------|------|------|
| 数据可用性 | ✅ | HuggingFace 直接下载，HDF5 兼容 |
| Pipeline 兼容性 | ✅ | extract_features.py 无需修改 |
| 工时可控 | ✅ | 方案 B ~6h 端到端 |
| Novelty 空间 | ✅ | Trained vs untrained + layer×timestep granularity 无人做过 |
| 独立 story 强度 | ⚠️ | Grant et al. 已覆盖核心 behavioral insight |
| 组合 story 强度 | ✅ | 与 temporal distance + action probe 构成 "when does VLA training matter" 的完整 story |
| CoRL deadline 风险 | ⚠️ | 还剩 14 天 (abstract 5/26, paper 5/29) |
| 存储空间 | ✅ | 方案 B 仅需 ~34 GB |

### 建议: **Conditional GO**

**必须先过的 gate**:
1. 下载 LIBERO-Goal 后，用 DINO 检查 10 个 task 的 t=0 pairwise cosine similarity ≥ 0.95 → 确认视觉 ambiguity
2. Action prediction probe 结果出来后，确认 "VLA training matters for action" story 成立

**执行顺序**:
1. 下载 + t=0 visual check (0.5h)
2. 方案 B 特征提取：8 关键层 (2.5h)
3. Probe 训练 + 分析 (3h)
4. 如果结果好 → 补全 33 层做 full layer-wise analysis

**论文定位（最终 story）**:
- Sec 4.1: Temporal distance probe → vision-solvable → Δρ 小 (informative negative)
- Sec 4.2: Instruction identity probe → vision-unsolvable → Δ_acc 大 (VLA training matters)
- Sec 4.3: Action prediction probe → policy knowledge → Δ large (VLA training matters)
- Sec 5: Unified "when does VLA training matter?" analysis

---

## 附录 A: OpenVLA Prompt 构造

```python
LIBERO_GOAL_PROMPTS = {
    "open_the_middle_drawer_of_the_cabinet":
        "In: LIBERO-Goal Kitchen Scene\nOpen the middle drawer of the cabinet.",
    "open_the_top_drawer_and_put_the_bowl_inside":
        "In: LIBERO-Goal Kitchen Scene\nOpen the top drawer and put the bowl inside.",
    "push_the_plate_to_the_front_of_the_stove":
        "In: LIBERO-Goal Kitchen Scene\nPush the plate to the front of the stove.",
    "put_the_bowl_on_the_plate":
        "In: LIBERO-Goal Kitchen Scene\nPut the bowl on the plate.",
    "put_the_bowl_on_the_stove":
        "In: LIBERO-Goal Kitchen Scene\nPut the bowl on the stove.",
    "put_the_bowl_on_top_of_the_cabinet":
        "In: LIBERO-Goal Kitchen Scene\nPut the bowl on top of the cabinet.",
    "put_the_cream_cheese_in_the_bowl":
        "In: LIBERO-Goal Kitchen Scene\nPut the cream cheese in the bowl.",
    "put_the_wine_bottle_on_the_rack":
        "In: LIBERO-Goal Kitchen Scene\nPut the wine bottle on the rack.",
    "put_the_wine_bottle_on_top_of_the_cabinet":
        "In: LIBERO-Goal Kitchen Scene\nPut the wine bottle on top of the cabinet.",
    "turn_on_the_stove":
        "In: LIBERO-Goal Kitchen Scene\nTurn on the stove.",
}
```

## 附录 B: Grant et al. 方法学详细

**六种 Counterfactual 条件**: correct prompt, null (empty string), negation ("Don't pick up X"), motor command ("Move slowly"), object swap, temporal switch.

**Activation Injection**: 替换模型内部 activation 为另一 task 的 activation → 测试 vision vs language pathway 的因果贡献。Visual pathway injection: cosine sim 0.999 with source task behavior.

**SAE Training**: 424 SAEs across 6 architectures, TopK sparsity (k=64), frequency-weighted contrastive selection → 82+ manipulation concepts.

**Linear Probes on Rollouts**: GR00T 100% task ID across 32 layers; π0.5 99.3% prompt classification at L17 despite behavioral invariance to prompts → **"encoded but not used"** paradox.
