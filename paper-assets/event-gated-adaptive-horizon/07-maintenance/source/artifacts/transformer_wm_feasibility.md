# Transformer World Model dt-Conditioning 可行性报告

> 目标：评估在 transformer WM 上复现 CIVO 实验的工程可行性
> 日期：2026-05-29（STORM section 追加于 2026-05-29）

---

## 1. IRIS 架构概览

| 组件 | 实现 | 关键特征 |
|------|------|----------|
| **Tokenizer** | VQ-VAE (taming-transformers) | 64×64 RGB → discrete tokens (e.g. 16×16=256 tokens/frame), vocab_size 可配 |
| **World Model** | GPT-style autoregressive transformer (minGPT) | block-causal attention, KV-cache; 输入序列 = [obs_tokens, action_token] × T |
| **Actor-Critic** | CNN(4层) + LSTM(1024→512) + linear heads | 在 reconstructed images 上操作，不在 latent space |
| **Imagination** | WorldModelEnv.step() 自回归采样 | 逐 token 采样 obs，Categorical 采样 reward/done |
| **环境** | **仅 Atari**（discrete actions, 64×64 image obs） | NoFrameskip wrappers, reward clipping |

### 序列结构

每个 "block" = `[obs_token_1, ..., obs_token_K, action_token]`，共 K+1 tokens/step。Embedder 用 block_mask 将 obs tokens 和 action token 分别送入不同的 embedding table。Transformer 在完整序列上做 block-causal attention。

### 与 DreamerV3 RSSM 的关键差异

| 维度 | DreamerV3 (RSSM) | IRIS (Transformer) |
|------|------------------|---------------------|
| 状态表示 | 连续 latent (stoch + deter) | 离散 image tokens |
| 动作空间 | 连续（DMC）/ 离散 | 仅离散（Atari） |
| Observation | 支持 proprioceptive vector | 仅 image (VQ-VAE) |
| Imagination | 单步 RSSM prior，parallel rollout | 自回归 token-by-token，sequential |
| dt-embedding | 可直接加到 latent state | 需要新增 token type 或 additive signal |

---

## 2. dt-Conditioning 注入点分析

### 方案 A：dt 作为额外 token（推荐）

在每个 block 的 action token 后追加一个 dt token：`[obs_1, ..., obs_K, action, dt]`

**需修改的文件：**

| 文件 | 修改内容 | 行数估计 |
|------|----------|----------|
| `src/models/slicer.py` — Embedder | 新增 dt embedding table + block_mask 第三项 | ~20 行 |
| `src/models/world_model.py` — WorldModel | tokens_per_block +1, 新增 dt_embedding, forward 中拼接 dt token, compute_loss 中构造 dt labels | ~50 行 |
| `src/models/transformer.py` — TransformerConfig | tokens_per_block 更新, attention mask 调整 | ~10 行 |
| `src/envs/world_model_env.py` — WorldModelEnv | step() 中注入 dt token, reset() 中初始化 | ~30 行 |
| `src/models/actor_critic.py` — ActorCritic | imagine() 中传入 dt, policy 可选输出 dt selection | ~40 行 |
| `src/episode.py` — Episode | 新增 dt 字段 | ~15 行 |
| `src/dataset.py` — EpisodesDataset | sample_batch 支持 temporal subsampling (跳帧) | ~40 行 |
| `src/trainer.py` — Trainer | 训练循环传递 dt 参数 | ~20 行 |
| config/*.yaml | 新增 dt 相关超参 | ~15 行 |

**总计：~240 行修改/新增**

### 方案 B：dt 作为 additive embedding

类似 positional embedding，将 dt embedding 加到整个 block 的所有 token embedding 上。实现更简单（~150行），但语义不如方案 A 清晰，且与 CIVO 论文中 DreamerV3 的 dt_embedding 机制更不对应。

---

## 3. 核心阻塞问题：DMC 环境支持

### 问题

CIVO 是 **6-DoF multi-joint locomotion 特异性现象**（Walker Walk / Cheetah Run）。IRIS **仅支持 Atari**（discrete actions, image observations）。要在 IRIS 上复现 CIVO，必须先让 IRIS 支持 DMC proprioceptive 环境。

### DMC 适配工程量

| 工作项 | 难度 | 行数 | 说明 |
|--------|------|------|------|
| DMC env wrapper | 低 | ~100 | gym 接口封装，连续 action → 连续 obs |
| **Tokenizer 改造** | **高** | **~300+** | VQ-VAE 处理 image，不处理 proprioceptive vector。需要：(1) 换成 MLP encoder 或 (2) 直接用连续 embedding 替代 VQ 离散化 |
| Action embedding 改造 | 中 | ~80 | 离散 action embedding → 连续 action projection (nn.Linear) |
| Actor-Critic 改造 | 中 | ~100 | CNN 前端 → MLP 前端；action head 从 Categorical → Gaussian |
| World model loss 改造 | 中 | ~60 | obs logits (cross-entropy over discrete tokens) → regression loss (MSE/Gaussian NLL) |
| **总计** | | **~640+** | 本质上是重写 IRIS 的大部分 I/O pipeline |

### 核心矛盾

将 IRIS 改造为支持 DMC proprioceptive 的版本后，它不再是 "IRIS"——tokenizer 从 VQ-VAE 变成了 MLP，observation 从离散 tokens 变成了连续向量。这削弱了 "在不同架构上验证 CIVO" 的论证力度，因为改造后的系统更接近 "transformer backbone + continuous latent"（类似 TWM/STORM），而非原始 IRIS 的 "VQ-VAE + autoregressive discrete token prediction" 设计。

---

## 4. 替代路径评估

### 路径 1：IRIS + Atari（最低工程量，但科学价值存疑）

在 Atari 游戏上做 dt-conditioning 实验（仅需 ~240 行修改）。

- **优点**：工程量小，直接用 IRIS 原始架构
- **致命问题**：CIVO 是 6-DoF locomotion 特异性现象，Atari（discrete action, low-dim effective control）几乎不可能触发 CIVO → 实验结果大概率是 "dt-conditioning 在 Atari 上无害"，无法证明 CIVO 跨架构泛化

### 路径 2：改造 IRIS 支持 DMC（高工程量）

~880 行修改（240 dt-conditioning + 640 DMC 适配）。

- **优点**：直接对标 DreamerV3 实验，能回答 "transformer WM 是否也有 CIVO"
- **问题**：(1) 工程量大，~15-25 AI worker 小时；(2) 改造后不再是标准 IRIS；(3) 需要先验证改造后的 baseline（dt=1）在 Walker/Cheetah 上能正常训练，这本身需要调参

### 路径 3：使用已有的 continuous-control transformer WM（推荐）

| 候选 | 特点 | DMC 支持 | 开源 |
|------|------|----------|------|
| **TWM** (Robine et al., 2023) | Transformer WM + VQ-VAE for images | 部分（image-based） | ✅ |
| **STORM** (Zhang et al., 2023) | Transformer WM + **discrete categorical** latent | ❌ DMC（开源代码 Atari-only；GIT-STORM 论文有 visual DMC 结果但代码未公开） | ✅ |
| **TD-MPC2** (Hansen et al., 2024) | MPC, 非 imagination actor-critic | ✅ DMC | ✅ (但 MPC，非 imagination) |
| **TAWM** (Nhu et al., ICML 2025) | TD-MPC2 + dt-conditioning（已证明 work） | ✅ DMC | 待确认 |

**STORM 是最接近的候选**：transformer world model + continuous latent + DMC proprioceptive + imagination-based actor-critic（类似 DreamerV3 的 imagination training）。在 STORM 上加 dt-conditioning 的工程量远小于改造 IRIS。

### 路径 4：等 DreamerV4（如果近期发布）

DreamerV4 可能自带 transformer backbone。但发布时间不确定，不可依赖。

---

## 5. 与 DreamerV3 CIVO 实验的对应关系

| DreamerV3 实验 | Transformer WM 对应 | 可行性 |
|---------------|---------------------|--------|
| Baseline (dt=1) | STORM/IRIS baseline | ✅ 直接可用（STORM）/ 需改造（IRIS） |
| Trained dt_emb (dt=2, subsample ON) | 新增 dt embedding + temporal subsampling | ✅ 核心工作 |
| Frozen dt_emb control | 冻结 dt embedding 权重 | ✅ 简单（freeze param） |
| Removed dt_emb (dim=0) | 移除 dt token/embedding | ✅ 简单 |
| NVE 诊断指标 | 同样计算 value/empirical return 比率 | ✅ 指标代码可复用 |
| Wide dual-critic | 需在 transformer WM 上实现 | 中等（取决于 actor-critic 结构） |

**最小可行实验（1 seed, Walker Walk）：**
- Baseline (dt=1)：验证 transformer WM 基线健康
- Trained dt_emb (dt=2)：观察是否触发 CIVO
- Frozen dt_emb control：验证冻结是否阻止

---

## 6. 工程量估算

| 路径 | 工程量 | GPU 时间 | 风险 |
|------|--------|----------|------|
| IRIS + Atari dt-conditioning | 3-5 AI worker hours | ~5-10 GPU-h | 科学价值低（不触发 CIVO） |
| IRIS 改造 DMC + dt-conditioning | 15-25 AI worker hours | ~15-25 GPU-h | 改造后非标准 IRIS；baseline 调参不确定 |
| **STORM + dt-conditioning** | **8-12 AI worker hours** | **~10-20 GPU-h** | 需确认 STORM 代码质量和 DMC 环境覆盖 |
| TAWM 直接对比 | 5-8 AI worker hours | ~10 GPU-h | MPC setting 非 imagination，对比意义不同 |

---

## 7. 风险清单

1. **Tokenizer 兼容性**（IRIS 特有）：VQ-VAE 离散 tokenizer 与 proprioceptive continuous observation 不兼容。改造代价接近重写。
2. **Imagination 速度**：IRIS 逐 token 自回归采样（每步 K 次前向传播），比 RSSM 慢一个数量级。Walker Walk 150K 步训练时间可能从 DreamerV3 的 ~3h 增加到 ~10-15h。
3. **CIVO 触发不确定性**：即使在 DreamerV3 上，CIVO 也是 stochastic onset（Walker 60%, Cheetah 75%）。Transformer WM 的 latent dynamics 精度不同，可能导致：(a) CIVO 不触发（world model 更准确）或 (b) CIVO 更严重（world model 更差）。两种结果都有科学意义但需要解释。
4. **Baseline 健康度**：如果 transformer WM 在 Walker Walk dt=1 baseline 本身就不稳定（类似 Quadruped/Humanoid 在 DreamerV3 上），则无法隔离 CIVO。
5. **代码维护状态**：IRIS 最后更新较早（ICLR 2023 论文），依赖 PyTorch 1.11.0+，可能存在与当前 CUDA/PyTorch 版本的兼容性问题。

---

## 8. 建议

**推荐路径：STORM + dt-conditioning**

1. 先调研 STORM 代码库（同样做一次可行性评估），确认其 DMC 支持和 imagination training 的实现质量
2. 如果 STORM 可用，在 STORM 上实现 dt-conditioning（~8-12 AI worker hours），运行最小实验（Walker Walk, 1 seed, 3 configs: baseline / trained dt_emb / frozen control）
3. 结果写入论文 Discussion 或 Appendix 作为 "cross-architecture evidence"

**不推荐直接改造 IRIS**：工程量大（~20h）、改造后架构偏离原始 IRIS、DMC baseline 需要额外调参。投入产出比不如 STORM 路径。

**IRIS + Atari 作为补充**：如果需要 "纯 IRIS 实验" 作为论证，可以低成本（~5h）在 Atari 上做 dt-conditioning，预期结果为 "discrete action + low-DoF 不触发 CIVO"，这与论文的 DoF 依赖性结论一致，可作为补充证据。

---

## STORM 可行性评估

> 调研日期：2026-05-29
> 源码：https://github.com/weipu-zhang/STORM （Atari-only，已停止维护）
> 论文：https://arxiv.org/abs/2310.09615 （NeurIPS 2023）
> 后继项目：OC-STORM（object-centric，同样 Atari-only）
> 相关：GIT-STORM (https://github.com/Cmeo97/GIT-STORM) — 论文报告了 DMC 结果，但开源代码仅 Atari

### 1. STORM 架构概览

| 组件 | 实现 | 关键特征 |
|------|------|----------|
| **Encoder** | CNN (EncoderBN) | Conv2d stride-2 下采样，64×64 RGB → flat embedding |
| **Latent** | **Discrete categorical** (stoch_dim=32×32=1024) | straight-through estimator，post/prior KL loss |
| **Dynamics** | StochasticTransformerKVCache | 2-layer transformer, 8 heads, hidden=512; causal temporal mask; KV-cache for inference |
| **Decoder** | CNN (DecoderBN) | 重建 image observations |
| **Reward/Termination** | MLP heads | SymLog two-hot reward encoding |
| **Actor-Critic** | MLP (2-layer, 512) | Latent-space input, PPO-style policy loss + slow/fast critic |

#### 与 DreamerV3 关键异同

| 维度 | DreamerV3 (RSSM) | STORM (Transformer) |
|------|------------------|---------------------|
| Dynamics model | GRU-based RSSM (deter + stoch) | Transformer with KV-cache |
| Latent 表示 | **Continuous** deter (512) + discrete stoch (32×32) | **Pure discrete** categorical (32×32=1024) |
| 动作空间 | 连续（DMC）/ 离散 | **仅离散（Atari）** — 开源代码 |
| Observation | image / proprioceptive vector | **仅 image (CNN encoder)** |
| Imagination | 单步 RSSM prior，parallel rollout | 自回归逐步 predict_next()，sequential |
| AC training | 纯 imagination | 纯 imagination ✅ |

**⚠️ 重要纠正**：之前的评估（§4 路径 3 表格）将 STORM 标注为 "continuous latent + ✅ DMC"，这是**错误的**。STORM 使用 **discrete categorical latent**，且开源代码**不支持 DMC**。

### 2. B1 结论：Imagination Training 证据 ✅

**STORM 的 actor-critic 完全基于 imagination 训练，与 DreamerV3 paradigm 一致。**

证据链（代码文件 + 行为）：

1. **`sub_models/world_models.py` — `WorldModel.imagine_data()`**：
   - 从 replay buffer 采样 context (obs, action)
   - 用 `encode_obs()` 编码 context → latent
   - 循环 `imagine_batch_length` 步：
     - `agent.sample(latent)` → action（actor 在 latent space 采样动作）
     - `predict_next(latent, action)` → next_latent, reward_hat, termination_hat
   - 返回完整的 imagined trajectory: (latent_buffer, action_buffer, reward_hat_buffer, termination_hat_buffer)

2. **`train.py` — 训练循环**：
   - `world_model.imagine_data(agent, ...)` 生成 imagined data
   - `agent.update(latent=imagine_latent, reward=imagine_reward, ...)` 直接用 imagined data 训练 AC
   - **没有任何 real-data AC update** — 纯 imagination training

3. **`agents.py` — `ActorCriticAgent.update()`**：
   - `calc_lambda_return()` 计算 GAE lambda returns
   - slow/fast critic (EMA 98%) + symlog two-hot value loss
   - PPO-style policy loss + entropy regularization
   - 输入全部来自 world model 的 imagined data

**结论：B1 前提成立。** STORM 的 closed-loop imagination training 与 DreamerV3 完全一致，CIVO 的 imagination-based value overestimation 机制在此架构中可能成立。

### 3. B2 结论：DMC Baseline 数据

**原始 STORM 论文（NeurIPS 2023）不包含 DMC 实验**，仅在 Atari 100k 上评估（mean HNS 126.7%）。

GIT-STORM 论文 (arXiv 2410.07836) 扩展 STORM 到 visual DMC 并报告了 Table 6：

| 任务 | SAC | DreamerV3 | STORM | GIT-STORM |
|------|-----|-----------|-------|-----------|
| **Walker Walk** | 38.9 | **955.8** | 758.0 | 854.7 |
| Walker Stand | — | — | — | 954.8 |
| Walker Run | — | — | — | — |
| Cheetah Run | — | — | — | — |
| Median (18 tasks) | — | 808.5 | — | 475.1 |

**关键限制：**
- 这些是 **visual DMC**（image obs, 64×64），非 proprioceptive
- 500K interactions (1M frames, frame_skip=2)
- **GIT-STORM 的 DMC 代码未开源** — GitHub repo 仅含 Atari 代码
- STORM 在 Walker Walk 上 758.0，低于 DreamerV3 的 955.8，但不算 catastrophic failure

**B2 评估：**
- Walker Walk 758.0 是"可用但不理想"的 baseline
- 低于 DreamerV3 约 200 分，CIVO 实验需要确保 dt-conditioning 引起的 degradation 足够大以与 inherent performance gap 区分
- 但注意：这是 GIT-STORM 论文中自己复现的 STORM visual DMC 结果，我们自己复现可能有差异

### 4. dt-Conditioning 注入方案

在 STORM transformer 架构中注入 dt embedding 的方案：

**方案 A：dt 作为 additive embedding（推荐）**

将 dt 编码为 learned embedding，加到 transformer 每步的 latent+action embedding 上：

```python
# 在 WorldModel 中新增
self.dt_embedding = nn.Embedding(max_dt, embed_dim)  # embed_dim = 1024

# 在 predict_next() 中
latent_action_emb = self.storm_transformer.forward_with_kv_cache(...)
latent_action_emb = latent_action_emb + self.dt_embedding(dt)  # additive
```

这与 DreamerV3 的 dt_embedding 最为对应（都是 additive signal）。

**方案 B：dt 作为 transformer 额外 token**

在 (latent, action) 序列中追加 dt token。语义更清晰但改动更大（需调整 attention mask 和序列结构）。

**推荐方案 A**，改动最小且与 CIVO 论文中 DreamerV3 的实现方式直接对应。

### 5. 工程量估算

#### 前提：需先将 STORM 适配到 DMC

| 工作项 | 难度 | 行数 | 说明 |
|--------|------|------|------|
| DMC env wrapper | 低 | ~100 | gymnasium DMC wrapper，continuous action space |
| **Continuous action embedding** | **中** | **~60** | discrete action embedding → `nn.Linear(action_dim, embed_dim)` |
| **Encoder 替换**（proprioceptive） | **中** | **~80** | CNN encoder → MLP encoder for vector obs |
| **Decoder 替换**（proprioceptive） | **中** | **~60** | CNN decoder → MLP decoder for vector obs reconstruction |
| Action head 改造 | 中 | ~50 | Categorical → TanhGaussian policy |
| 小计（DMC 适配） | | **~350** | |

#### dt-Conditioning 在 DMC-STORM 上

| 工作项 | 行数 | 说明 |
|--------|------|------|
| dt embedding module | ~30 | `nn.Embedding(max_dt, 1024)` + additive injection |
| Temporal subsampling in replay buffer | ~60 | 支持 dt>1 的 frame skipping |
| imagine_data() 支持 dt | ~40 | imagination 中注入 dt |
| Config + CLI | ~20 | dt 相关超参 |
| NVE 诊断指标 | ~50 | value/empirical return ratio 计算 |
| 小计（dt-conditioning） | **~200** | |

**总计：~550 行修改/新增**

#### 时间估算

| 阶段 | AI worker hours | 说明 |
|------|----------------|------|
| DMC 适配 + baseline 验证 | 6-10h | 包含 debug 和确认 baseline 健康 |
| dt-conditioning 实现 | 3-5h | 在已验证的 DMC-STORM 上加 dt |
| 实验运行（3 configs × 1 seed × Walker Walk） | 3-6h GPU | 取决于 GPU 速度 |
| **总计** | **10-16 AI worker hours + 3-6h GPU** | |

### 6. 最终可行性判断

**可行但工程量高于预期，且存在关键风险。**

#### ✅ 有利因素
1. **B1 成立**：actor-critic 纯 imagination training，CIVO 的 closed-loop 前提满足
2. **架构差异有科学价值**：STORM 的 transformer dynamics + discrete categorical latent vs DreamerV3 的 GRU-RSSM + continuous+discrete hybrid，如果 CIVO 在此架构上复现，是强有力的跨架构证据
3. **代码结构清晰**：imagine_data() / agent.update() 分离干净，注入 dt-conditioning 的改动集中

#### ⚠️ 风险因素
1. **DMC 适配未现成** — 原始 STORM 和 GIT-STORM 开源代码均 Atari-only。需自行适配 DMC（~350 行），且 baseline 需要从头验证
2. **Latent 是 discrete categorical** — 之前假设 STORM 是 continuous latent 是错误的。Discrete categorical latent 下 dt-conditioning 的 value overestimation 机制可能与 DreamerV3 的 continuous latent 不同
3. **Visual vs Proprioceptive** — GIT-STORM 论文的 DMC 结果是 visual（image obs），我们的 CIVO 实验用 proprioceptive。如果做 proprioceptive STORM，没有任何已知 baseline 可参考
4. **性能 gap** — Walker Walk 758.0 (STORM visual) vs 955.8 (DreamerV3)。如果 proprioceptive STORM baseline 更低，CIVO 的额外 degradation 可能难以隔离
5. **项目已停止维护** — 可能存在依赖版本问题

#### 📊 与 IRIS 路径对比

| | IRIS + DMC 改造 | STORM + DMC 适配 |
|---|---|---|
| 工程量 | ~880 行, 15-25h | ~550 行, 10-16h |
| 核心改造 | VQ-VAE → MLP (根本性) | CNN → MLP (相对温和) |
| Latent type | Discrete tokens | Discrete categorical |
| 已知 DMC baseline | 无 | 758.0 (visual, from GIT-STORM paper) |
| Imagination AC | ❌ (CNN+LSTM AC, 在 reconstructed image 上) | ✅ (MLP AC, 在 latent space 上) |
| 代码维护 | 停滞 | 停滞（→ OC-STORM） |

**STORM 仍然是更优选择**（相对于 IRIS），因为 imagination-based latent-space AC 与 DreamerV3 的 paradigm 一致，改造量也更小。

#### 建议

1. **如果决定做 transformer WM CIVO 实验**：选 STORM，先做 DMC proprioceptive 适配 + baseline 验证（Walker Walk dt=1），再加 dt-conditioning
2. **降低风险的策略**：先做 visual DMC（STORM 的 CNN encoder 可直接复用），参考 GIT-STORM 论文的 758.0 baseline，验证 CIVO 后再考虑 proprioceptive
3. **如果工程预算紧张**：考虑放弃 transformer WM 实验线，在 Discussion 中以文字讨论 "STORM/IRIS 架构差异使得 CIVO 复现需要非平凡适配工作" 作为 limitation
