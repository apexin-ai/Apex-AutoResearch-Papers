# Plan 015: Dynamic vs Static Embedding Mining

## 背景与动机

2/3 dream reviewers 提出 static vs dynamic mining confound：当前 StructFuse 使用 pretrained encoder（Qwen2.5-Coder-3B）一次性计算所有 candidate embeddings，基于这些固定 embeddings 挖掘 hard negatives，整个训练过程使用相同的负样本排序。Reviewer 的 concern 是：随着训练推进，模型表示空间发生变化，pretrained embeddings 挖掘的 negatives 可能变得"stale"——不再是当前模型认为最难区分的 negatives。

**代码现状确认**：虽然 `train.py:323-332` 每 epoch 调用 `mine_batch()`，但 `EmbeddingDistanceMiner` 使用的 embeddings 是从 `--embeddings-file` 一次性加载的，训练过程中从未更新。因此当前实际是 **static mining**——每 epoch 的 mining 产生相同结果（除了 fallback padding 的随机性）。

## 文献综述

### 1. ANCE (Xiong et al., ICLR 2021)
**"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"**

核心方法：异步更新 ANN index。训练过程中维护一个 parallel Inferencer，每 m 个 batch 用当前 checkpoint 重新编码全部 corpus，重建 ANN index，从中采样 global hard negatives。

关键发现：
- In-batch/random negatives导致 gradient variance 大、收敛慢
- 全局 hard negatives 显著改善收敛和最终性能
- 异步更新引入的 staleness（index 落后当前模型几百步）是可接受的
- MSMARCO 和 NQ 上显著超过 DPR

与本实验的关系：ANCE 的 asynchronous refresh 是 dynamic mining 的经典范式。我们的场景（~11K samples）远小于 ANCE 的 corpus（~8.8M passages），re-encode 开销可忽略。

### 2. DPR (Karpukhin et al., EMNLP 2020)
**"Dense Passage Retrieval for Open-Domain Question Answering"**

使用 BM25 hard negatives（static）+ in-batch negatives。负样本在训练前确定，不随训练更新。DPR 展示了 static hard negatives 即可显著优于 random negatives，但后续工作（ANCE、RocketQA）表明 dynamic mining 可进一步提升。

### 3. ANCE-Tele (Sun et al., EMNLP 2022)
**"Reduce Catastrophic Forgetting of Dense Retrieval Training with Teleportation Negatives"**

发现 ANCE 的 iterative mining 导致 **catastrophic forgetting**：模型在新一轮 hard negatives 上学习时，会遗忘之前学到的区分能力。提出 teleportation negatives：累积过去迭代的 momentum negatives + 用 lookahead 近似未来的 negatives，平滑学习过程。

关键启示：dynamic mining 并非总是更优——过于频繁的 re-mining 可能引起训练不稳定。对于我们的小数据集（~11K），这一风险更需关注。

### 4. RocketQA (Qu et al., NAACL 2021)
**"An Optimized Training Approach to Dense Passage Retrieval"**

三大贡献：cross-batch negatives、denoised hard negatives（用 cross-encoder 过滤 false negatives）、data augmentation。其 denoised hard negatives 是 mining 后经 cross-encoder 过滤，而非训练中动态更新，本质上仍是 static pipeline。

### 5. SimANS (Zhou et al., EMNLP 2022 Industry)
**"Simple Ambiguous Negatives Sampling for Dense Text Retrieval"**

发现 too-hard negatives 可能是 false negatives（标注稀疏导致），提出采样"ambiguous negatives"（排名位于 positive 附近但不太硬的）。启示：dynamic mining 使 negatives 越来越难时，false negative 风险增加。

### 6. CoCoHaNeRe (ACM TOSEM 2024)
**"Effective Hard Negative Mining for Contrastive Learning-Based Code Search"**

代码搜索领域最相关的工作。使用 embedding distance 挖掘 hard negatives，发现 memory bank 中的 stale embeddings 会降低训练效果。

### 总结：文献共识

| 维度 | 共识 |
|------|------|
| Static vs Dynamic | Dynamic 通常优于 static，但边际收益随数据规模减小而降低 |
| Re-mine 频率 | ANCE 每数千 steps；过于频繁可能导致 catastrophic forgetting (ANCE-Tele) |
| 小数据集 | 文献主要在大规模 corpus（百万级）上验证，~11K 规模的收益未有定论 |
| Staleness 容忍度 | 异步更新的数百步延迟可接受 (ANCE)；但 epoch 级更新的 staleness 更大 |

## 实验设计

### Variants

| Variant | ID | 描述 | 实现方式 |
|---------|----|----|---------|
| **Static-Pretrained** | `static_pt` | Pretrained embeddings 一次性挖掘，整个训练不变 | 当前默认行为（`--embeddings-file` 固定） |
| **Dynamic-Per-Epoch** | `dynamic_ep` | 每 epoch 开始前用当前 checkpoint 重新编码所有 candidates，重建 nearest-neighbor index，重新挖掘 | 修改 train.py：epoch 边界插入 re-encode + rebuild |
| **Dynamic-Per-500-Steps** | `dynamic_500` | 每 500 steps 重新挖掘（更高频，接近 ANCE 风格） | 可选，仅在 dynamic_ep 显著优于 static_pt 时执行 |

### 超参数（与 M2 一致，控制变量）

| 参数 | 值 |
|------|-----|
| model | Qwen2.5-Coder-3B |
| hard_negative_strategy | `dataflow_aware` |
| batch_size | 8 |
| learning_rate | 2e-5 |
| num_epochs | 2 (D026 过拟合缩减) |
| max_seq_length | 2048 |
| num_negatives | 7 |
| temperature | 0.07 (learnable) |
| pos_weight_alpha | 1.0 |
| proj_dim | 256 |
| LoRA | r=16, alpha=32 |
| warmup_ratio | 0.1 |
| eval_steps | 500 |
| seeds | 42 (单 seed 即可，目的是对比 static vs dynamic，不需多 seed CI) |

### Dynamic Mining 实现细节

每次 re-mine 的流程：
1. `model.eval()` + `torch.no_grad()`
2. 遍历所有 unique candidates，用当前 checkpoint 前向传播，提取 projection head 输出（256-d）
3. L2 normalize → 构建 cosine similarity matrix
4. 用更新后的 embeddings 重建 `EmbeddingDistanceMiner`
5. 调用 `mine_batch()` 生成新 negatives
6. `train_ds.refresh_negatives(mined)`
7. `model.train()` 继续训练

### 评估指标

| 指标 | 说明 | 关键性 |
|------|------|--------|
| val_loss | 验证集 InfoNCE loss | 主要 — 收敛速度对比 |
| R@1 | 验证集 Recall@1 | 主要 — 最终检索质量 |
| R@5, R@10 | 验证集 Recall@5/10 | 辅助 |
| Training wall time | 含 re-mine 的总训练时间 | 次要 — 开销对比 |
| Loss stability | Loss 曲线的方差（smoothed） | 辅助 — 检测 catastrophic forgetting |

### 控制变量

- 相同 seed (42)
- 相同训练/验证数据拆分
- 相同 dataflow graph
- 相同初始 embeddings（epoch 0 的挖掘使用相同 pretrained embeddings）
- 唯一差异：epoch 1+ 是否用当前 checkpoint 重新编码

## GPU 开销估算

### 当前训练开销（Static baseline）

- ~11K samples / batch_size 8 = ~1,375 steps/epoch
- 2 epochs = ~2,750 total steps
- 基于 M2 Qwen 运行数据（step 1550/4242 at ~12h?），估算 step rate ≈ 2.1 steps/min
- **单 run 训练时间 ≈ 22h**（2 epochs on single RTX PRO 6000）

注：上述是保守估计。实际可能因 early stopping 和 2048 seq length 的 padding 效率而更快。

### 每次 Re-mine 开销

**Step 1: Re-encode all candidates**
- Unique candidates ≈ ~11K files（query + positive 有重叠，去重后 ~8-10K unique）
- Inference batch size = 64（no gradients, 96GB VRAM 充裕）
- Batches = 10,000 / 64 ≈ 157
- Qwen2.5-Coder-3B forward（2048 tokens, inference only）≈ 1.5s/batch on RTX PRO 6000
- **Re-encode time ≈ 157 × 1.5s ≈ 4 min**

**Step 2: Nearest-neighbor search**
- 10K vectors × 256-d，brute-force cosine similarity
- NumPy matrix multiply: 10K × 10K × 256 → **< 1 sec**

**Step 3: DataFlowAwareMiner.mine_batch()**
- 11K queries × top-50 similar → dataflow filter → **< 30 sec**

**单次 re-mine 总计 ≈ 5 min**

### Dynamic-Per-Epoch 总额外开销

- 2 epochs：epoch 0 用 pretrained embeddings（与 static 相同），epoch 1 需 re-mine 1 次
- **额外开销：~5 min（1 次 re-mine）**
- 占总训练时间比例：5 min / ~22h ≈ **0.4%**

### Dynamic-Per-500-Steps 总额外开销（可选）

- 2750 total steps / 500 = 5 次 re-mine（除去 step 0）
- **额外开销：~25 min**
- 占总训练时间比例：25 min / ~22h ≈ **1.9%**

### 实验总 GPU 时间

| Variant | 训练时间 | Re-mine 开销 | 总时间 | GPU 卡 |
|---------|---------|-------------|--------|--------|
| static_pt | ~22h | 0 | ~22h | 1× RTX PRO 6000 |
| dynamic_ep | ~22h | ~5 min | ~22.1h | 1× RTX PRO 6000 |
| dynamic_500 (可选) | ~22h | ~25 min | ~22.4h | 1× RTX PRO 6000 |
| **合计** | | | **~44-67h** | |

注：可与 M2 其他 seed runs 串行（单卡），或等双卡空出后并行（static+dynamic 各占一卡，~22h wall time）。

## 预期结果与论文角色

### 场景分析

**场景 A：Dynamic ≈ Static（R@1 差异 < 1pp）**
- **最可能的场景**。理由：
  1. 数据规模仅 ~11K，embedding space 变化有限
  2. StructFuse 的核心优势来自 dataflow structural signal（disconnected filtering），而非 embedding ranking
  3. 2 epochs 训练，模型只经历 1 次 re-mine 机会，curriculum effect 有限
- **论文处理**：Limitation 段落明确声明："We use static embeddings from the pretrained encoder for negative mining. Dynamic re-mining (ANCE-style) on our ~11K dataset shows <1pp difference (Table X), suggesting that at this scale, the structural signal from data-flow filtering dominates over embedding recency."
- **Reviewer response**：直接回应 concern，提供实验证据

**场景 B：Dynamic > Static（R@1 差异 ≥ 2pp）**
- **较不可能但有价值**。意味着即使在小数据集上，stale embeddings 也会损失性能。
- **论文处理**：可作为 improvement — "Combining data-flow-aware mining with periodic embedding refresh yields +Xpp additional gain"。但增加了方法复杂度，需权衡是否纳入主方法。
- **风险**：如果 dynamic 大幅优于 static，可能需要重跑 M2 full 18 runs，时间不允许（ARR May 25）。应在 Discussion 中 acknowledge。

**场景 C：Dynamic < Static（R@1 下降 ≥ 1pp）**
- **可能**，对应 ANCE-Tele 发现的 catastrophic forgetting。小数据集上更容易发生：re-mined negatives 变化大 → 训练不稳定。
- **论文处理**：强化当前做法的合理性 — "Dynamic re-mining on small-scale datasets introduces instability (cf. ANCE-Tele), validating our design choice of static pretrained embeddings."

### 论文段落位置

- **Limitation 段落**（Section 6 或 Discussion）：承认 static mining 的局限性，引用 ANCE/ANCE-Tele，报告 plan_015 实验结果
- **不需要放在主实验表格中**——这是 ablation/robustness check，非核心 claim

## 风险

| 风险 | 严重性 | 缓解措施 |
|------|--------|---------|
| GPU 时间挤占 M2/plan_014 | 中 | static+dynamic 仅 ~44h；可等 M2 完成后排队 |
| Dynamic 大幅优于 static | 低概率高影响 | 在 Discussion 中 acknowledge，留作 future work |
| 实现 bug 导致 re-encode 不正确 | 中 | 验证：re-encode 后计算与 pretrained embeddings 的 cosine drift，应 > 0 |
| 2 epochs 不足以体现 dynamic 优势 | 中 | 如果 dynamic_ep 无差异，可追加 dynamic_500 作为更频繁的对比 |

## 实现清单（不含代码，仅逻辑）

1. 新增函数 `re_encode_candidates(model, tokenizer, candidate_texts, batch_size=64)` → 返回 `Dict[str, np.ndarray]`
2. 修改 `train()` 训练循环：epoch > 0 时调用 re-encode → 重建 miner → mine_batch → refresh_negatives
3. 新增 CLI flag `--dynamic-mining`（default False，保持向后兼容）
4. W&B logging：记录每次 re-mine 的耗时和 embedding drift（当前 vs pretrained 的平均 cosine distance）
5. 验证脚本：对比 static 和 dynamic 两次 mining 的 negatives overlap ratio

## 参考文献

- Xiong et al. "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval." ICLR 2021. arXiv:2007.00808
- Karpukhin et al. "Dense Passage Retrieval for Open-Domain Question Answering." EMNLP 2020. arXiv:2004.04906
- Sun et al. "Reduce Catastrophic Forgetting of Dense Retrieval Training with Teleportation Negatives." EMNLP 2022. arXiv:2210.17167
- Qu et al. "RocketQA: An Optimized Training Approach to Dense Passage Retrieval." NAACL 2021. arXiv:2010.08191
- Zhou et al. "SimANS: Simple Ambiguous Negatives Sampling for Dense Text Retrieval." EMNLP 2022 Industry. arXiv:2210.11773
- "Effective Hard Negative Mining for Contrastive Learning-Based Code Search." ACM TOSEM 2024. (CoCoHaNeRe)
