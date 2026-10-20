# research uda baseline eval

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_uda_baseline_eval_20260522T004400_result.json`
- **Structured JSON:** [`a8e6438a9e6f45a85c3b.json`](../../sessions/a8/a8e6438a9e6f45a85c3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是 UDA baseline 可行性报告。

---

## UDA 可行性报告

### 1. 论文信息

- **全称**: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge
- **作者**: Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang (ZhipuAI/PKU), Guangsheng Bao (Westlake), Jie Tang (Tsinghua)
- **Venue**: AAAI 2026
- **arXiv**: [2508.09724](https://arxiv.org/abs/2508.09724)
- **核心方法**: 通过可学习的 MLP 动态调整 Elo rating 的 K-factor 和 soft labels，以最小化多 judge 间 Elo 轨迹的 dispersion，达成无监督去偏

### 2. 代码可用性：确认无公开代码

- Anonymous repo (`anonymous.4open.science/r/62AB93CD-23B4`) 返回 **403**，仍不可访问
- AAAI proceedings 页面无代码链接
- 两位关键作者 GitHub（[baoguangsheng](https://github.com/baoguangsheng)、[wangcunxiang](https://github.com/wangcunxiang)）均无 UDA 相关 repo
- PapersWithCode 无收录
- **结论：需要重实现**

### 3. 方法核心描述

**输入**：
- 多 judge 的 pairwise 判断 r_ij^(k) ∈ {0,1}（judge k 对 model i vs j 的 win/loss）
- 每个 response 的 embedding（e_i, e_j）+ judge 自身生成的 response embedding（e_k）

**特征构造**（Algorithm 1）：
- 6D+9 维特征向量 φ_ij^(k)：element-wise differences/products of embeddings（6个D维向量）+ 9个标量（cosine sim、KL-div、norm diff）

**模型**：
- 3-layer MLP: ℝ^(6D+9) → ℝ^3，输出 (K_ij, s_i, s_j)
  - K_ij: 自适应 K-factor（替代固定 K=32）
  - s_i, s_j: soft labels（替代硬 binary 标签）

**Elo 更新**（Algorithm 2）：
```
p̂_ij = σ(R_i - R_j)
R_i ← R_i + K_ij × (s_i - p̂_ij)
R_j ← R_j + K_ij × (s_j - (1 - p̂_ij))
```

**损失函数**：
```
L(θ) = α∑_b ||R^(b) - G||² + σ||R̄ - G||² + β∑_b(1 - ρ_p(R^(b), G))
```
- 第一项：每个 judge 的分数向 consensus anchor G 对齐
- 第二项：集体均值与 G 对齐
- 第三项：Pearson correlation 与 G 一致

**输出**：每个 model 在每个 judge 下的 debiased Elo score

**训练规模**：500 ArenaHard prompts × 10 judges = 450k pairwise judgments，单卡 4090 训练 8h

### 4. 重实现复杂度估算

| 模块 | 行数 | 复杂度 | 说明 |
|------|------|--------|------|
| Feature construction | ~60 | 中 | 6D+9维特征，需 embedding 模型 |
| MLP model | ~30 | 低 | 标准 3-layer MLP |
| Adaptive Elo update | ~40 | 低 | Algorithm 2 直接实现 |
| Consensus loss + training loop | ~100 | 中 | 三项 loss + differentiable Elo |
| Data loader + embedding | ~60 | 中 | 需适配 G-MFRM 数据格式 |
| Evaluation (correlation, std reduction) | ~40 | 低 | 标准指标 |
| **合计** | **~330 行** | — | **预估 2-3 天** |

### 5. 关键难点

1. **Embedding 来源不明**：论文未明确说用什么 embedding 模型。需要选一个（如 sentence-transformers），或论文 appendix 有说明但 HTML 版未完整展示
2. **Judge 自身 response embedding**：UDA 要求 judge 对同一 prompt 也生成 response 并取 embedding——这在 G-MFRM 数据收集时需额外生成
3. **Differentiable Elo**：整个 Elo 更新链需可微（通过 MLP 反传），实现时需注意梯度传播
4. **Consensus anchor G**：论文描述为"mean Elo across judges"，但具体初始化和更新策略需确认

### 6. 与 G-MFRM Pipeline 的接口对接

**兼容性**：
- G-MFRM 的 exp-001 数据收集（多 judge pairwise judgments on ArenaHard）可直接复用为 UDA 的输入
- 需额外：为每个 judge 生成对应 prompt 的 response（用于 e_k 特征）
- 输出：UDA 产出 debiased Elo scores，可与 G-MFRM 的 debiased ability estimates 在 rank correlation / agreement with human 指标上直接对比

**对接方案**：
```python
# 输入接口
def uda_debias(
    pairwise_judgments: dict[str, list[tuple[str, str, int]]],  # judge_id -> [(model_i, model_j, win)]
    response_embeddings: dict[str, np.ndarray],  # model_id -> embedding matrix
    judge_response_embeddings: dict[str, np.ndarray],  # judge_id -> embedding matrix
) -> dict[str, dict[str, float]]:  # judge_id -> {model_id: debiased_elo}
```

### 7. 建议

重实现可行，核心算法描述清晰（两个 Algorithm 伪代码），3-layer MLP + Elo update 本身不复杂。主要工作量在：
1. 确认 embedding 选择（~0.5天）
2. 核心实现 + 调试（~1.5天）
3. 与 G-MFRM 数据格式适配（~0.5天）

**总估计：2-3 天**，与之前调研结论一致。建议在 exp-001 数据收集完成后开始实现，因为 UDA 需要相同的 pairwise judgment 数据。

Sources:
- [arXiv 2508.09724](https://arxiv.org/abs/2508.09724)
- [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40788)
- [Guangsheng Bao GitHub](https://github.com/baoguangsheng)
- [Cunxiang Wang GitHub](https://github.com/wangcunxiang)

---
