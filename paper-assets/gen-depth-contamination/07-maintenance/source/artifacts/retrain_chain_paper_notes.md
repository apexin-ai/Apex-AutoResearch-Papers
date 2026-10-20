# Retrain-Chain K*=7 Paper Notes

> 素材文档，供 Paper Agent 写作使用。非论文正文。

---

## A. 完整 AUC 数值 + CI（Qwen2.5-1.5B LoRA, 7 generations）

| Pair | AUC | 95% CI | Per-fold AUC | JSD |
|------|-----|--------|-------------|-----|
| 0v1 | 0.9837 | [0.9821, 0.9854] | .9832, .9821, .9837, .9823, .9873 | 0.2301 |
| 1v2 | 0.8971 | [0.8949, 0.8993] | .8923, .8988, .8986, .8991, .8967 | 0.1039 |
| 2v3 | 0.8098 | [0.8052, 0.8144] | .8086, .8074, .8180, .8024, .8128 | 0.0750 |
| 3v4 | 0.7600 | [0.7528, 0.7672] | .7534, .7617, .7753, .7566, .7531 | 0.0654 |
| 4v5 | 0.7459 | [0.7379, 0.7538] | .7429, .7562, .7521, .7300, .7482 | 0.0605 |
| 5v6 | 0.7017 | [0.6958, 0.7076] | .7006, .7077, .7104, .6915, .6984 | 0.0350 |
| 6v7 | 0.6410 | [0.6376, 0.6445] | .6419, .6349, .6464, .6390, .6430 | 0.0177 |

**K\*=7** at θ=0.60。6v7 CI lower bound = 0.6376，margin = +3.76pp above θ。

### Pythia-1.4B LoRA retrain-chain（depth 0-4, K\*≥4）

| Pair | AUC | 95% CI |
|------|-----|--------|
| 0v1 | 0.9842 | [0.9823, 0.9860] |
| 1v2 | 0.9471 | [0.9432, 0.9509] |
| 2v3 | 0.8888 | [0.8832, 0.8943] |
| 3v4 | 0.7994 | [0.7920, 0.8067] |

4 generations tested, all above θ. Pythia depth extension 正在跑，预期 K\* 与 Qwen 同量级。

---

## B. Retrain-Chain vs Prompt-Chain 对比

### 同 depth pair 的 AUC 差异（Qwen2.5-1.5B, C4）

| Pair | Retrain AUC | Prompt AUC (best cont.) | Δ | 倍率 |
|------|-------------|------------------------|---|------|
| 0v1 | 0.9837 | 0.9971 | -0.0134 | ~1.0x |
| 1v2 | 0.8971 | 0.6112 | +0.2859 | 1.47x |
| 2v3 | 0.8098 | 0.5609 | +0.2489 | 1.44x |
| 3v4 | 0.7600 | 0.5409 | +0.2191 | 1.41x |
| 4v5 | 0.7459 | 0.5141 | +0.2318 | 1.45x |

- Prompt-chain: K\*=2（1v2=0.6112, 2v3=0.5609 < θ）
- Retrain-chain: K\*=7（所有 7 对 > θ）
- **K\* 差距 = 5 generations**（retrain 7 vs prompt 2）
- 0v1 pair 反向：prompt > retrain，因为 prompt-chain depth-0 是 human text 而 depth-1 是纯 LLM output（最大信号），retrain-chain depth-0 同样是 human text 但 depth-1 是 LoRA-finetuned model output（仍保留大量原模型特征）

### JSD 对比

| Metric | Prompt-chain (C4 Qwen-cont) | Retrain-chain |
|--------|------------------------------|---------------|
| 0v1 JSD | ~0.29 | 0.2301 |
| 1v2 JSD | ~0.01 | 0.1039 |
| Cliff ratio (0v1/1v2) | ~29x | 2.2x |
| λ (exponential decay) | ~2.9 | 0.285 |
| K\* | 2 | 7 |

**核心差异**：Prompt-chain 有 sharp cliff（0v1→1v2 JSD 下降 ~29x），retrain-chain 无 cliff（比率仅 2.2x），衰减缓慢且持续。

### Pythia 也复现了 retrain >> prompt 的差距

| Pair | Retrain AUC | Prompt AUC (cont.) | Δ |
|------|-------------|---------------------|---|
| 0v1 | 0.9842 | 0.9932 | -0.0090 |
| 1v2 | 0.9471 | 0.6539 | +0.2932 |
| 2v3 | 0.8888 | 0.5514 | +0.3374 |
| 3v4 | 0.7994 | 0.5152 | +0.2842 |

Pythia retrain 1v2=0.9471 vs prompt 1v2=0.6539，差距更大（+29.3pp vs Qwen +28.6pp）。

---

## C. 关键 Narrative Points

### C1. 为什么 retrain K\* >> prompt K\*？

**机制解释**：
1. **Prompt-chain** 仅传递 text（上一代 output 作为下一代 input），信息丧失纯粹来自 text-intrinsic degradation（autoregressive generation 的信息压缩）。经过 1-2 代，文本统计分布快速收敛到模型的 stationary distribution，后续代际几乎不可区分。
2. **Retrain-chain** 传递 model weights（在上一代 output 上 fine-tune 出新模型，再用新模型生成）。每一代 LoRA fine-tune 引入**累积的 model-adaptation artifacts**：
   - Vocabulary narrowing（词表使用逐代收窄）
   - Repetition bias amplification（重复倾向逐代增强）
   - Mode collapse（模型行为逐代趋向更窄的分布）
   - 这些 artifacts 叠加在 text-intrinsic degradation 之上，提供**额外的 depth-distinguishing signal**

**类比**：Prompt-chain 像复印文件（每次复印都有信息损失，但损失很快饱和）；retrain-chain 像让不同人根据上一份复印件重新手写一遍（每次手写都引入个人风格累积漂移）。

### C2. 与 model collapse 文献的关系

- Shumailov et al. (2024) "The Curse of Recursion"：描述 iterative retraining on self-generated data 导致 model collapse（分布坍缩、tail loss）。我们的 retrain-chain 正是这一设置的受控版本。
- Alemohammad et al. (2024) "Self-Consuming Generative Models Go MAD"：理论分析 iterative training 的分布退化。
- **关键定位**：model collapse 文献关注**模型质量退化**（performance degradation），我们关注**可检测性**（discriminability between adjacent generations）。两者互补：
  - Model collapse = "what happens to the model"
  - 我们的 K\* = "what happens to the text, and how long can we tell"
- **Retrain K\*=7 的含义**：即使在 model collapse 进行到第 7 代，我们仍然能区分相邻代际的文本。这意味着 model collapse 的累积效应（vocabulary narrowing 等）恰好是**可检测的 fingerprint**，它们让代际差异持续可观测远超 text-intrinsic saturation point。

### C3. 两种 K\* 的 operational 含义

| | Prompt-chain K\* | Retrain-chain K\* |
|---|---|---|
| 测量对象 | Text-intrinsic information loss | Model-adaptation artifacts + text loss |
| 适用场景 | Data curation（不知道数据来源） | Model archaeology（知道训练 pipeline） |
| 实操边界 | K\*=2: 只需 binary filter (gen-0 vs gen-≥1) | K\*=7: 可做更细粒度的 depth estimation |
| Generalizability | High（不依赖训练 pipeline 信息） | Low（artifacts 是 setup-specific） |

**论文定位**：Prompt-chain K\*=2 是 **operational boundary for data curation**（保守的、可泛化的）；retrain-chain K\*=7 是 **upper bound achievable via model archaeology**（乐观的、需要 pipeline 信息的）。

### C4. AUC 衰减形态对比

- **Prompt-chain**：Step function。0v1 极高（~0.99），1v2 骤降到 ~0.61-0.70（刚好过 θ），2v3 直接到 ~0.55（chance level）。之后 flat。
- **Retrain-chain**：Smooth concave decay。从 0.98 平滑下降到 0.64，无 cliff。三阶段：
  1. Rapid (depth 1-3): ~0.087/step
  2. Plateau (depth 3-5): ~0.014-0.050/step  
  3. Resumed decline (depth 5-7): ~0.053-0.061/step
- **Extrapolation**：Linear fit → 7v8 AUC ≈ 0.57 < θ；Logarithmic → 7v8 ≈ 0.60-0.62 borderline. K\* ceiling ≈ 7-8.

---

## D. Gap 分析：当前论文已写 vs 缺失

### 已入稿内容

| 位置 | 内容 | 数据完整度 |
|------|------|-----------|
| `appendix_extended.tex` §Extended Limitations | Retrain-chain K\*=7 (Qwen) + K\*≥4 (Pythia) 的完整 AUC/CI 表 (Table 24) | ✅ 完整 |
| `appendix_extended.tex` §Extended Limitations | CI methodology note（为什么 retrain-chain 用 fold-based CI 而非 bootstrap） | ✅ 完整 |
| `appendix_extended.tex` §JSD Decay Analysis | Retrain-chain JSD λ=0.285, cliff ratio 1.31x，与 prompt-chain 对比 | ✅ 完整 |
| `appendix_extended.tex` Fig retrain_decay | AUC decay 图（7 pairs + θ line + extrapolation） | ✅ 完整 |
| `main.tex` Limitations paragraph | 一句话提及 "retrain-chain yields K\*=7...confirmed ≥4 for Pythia" | ✅ 但极简 |
| `paper_framing.md` Q6 defense | Retrain-chain 作为 "prompt-chain ≠ real-world" concern 的 defense | ✅ 完整 framing |

### 缺失/不足内容

| 缺失点 | 重要性 | 建议处理 |
|--------|--------|---------|
| **正文无 retrain-chain 专门段落** | 🔴 高 | 需要在 Experiments 或 Discussion 加一个段落（而非仅在 appendix 和 limitations 提及） |
| **Retrain vs prompt 的 side-by-side AUC 对比表** | 🔴 高 | 本文档 §B 的对比表应入稿（至少入 appendix） |
| **机制解释不足** | 🟡 中 | 当前论文只说 "cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias)"，缺少对为什么 retrain artifacts 持续更久的 deeper analysis |
| **与 model collapse 文献的 explicit 连接** | 🟡 中 | 需要在 Related Work 或 Discussion 明确 cite Shumailov et al. / Alemohammad et al. 并 position our retrain-chain 结果 |
| **Pythia depth extension 结果** | 🟡 中 | 目前只有 K\*≥4（4 depths tested），depth extension 正在跑。完成后更新 Table 24 和相关段落 |
| **两种 K\* 的 operational 区别的 explicit framing** | 🟡 中 | paper_framing.md 有此 framing 但论文正文未充分展开 |
| **Retrain-chain 的 JSD 衰减形态与 prompt-chain 的 formal 对比图** | 🟡 中 | fig_retrain_decay.png 已有，但缺少 prompt-chain vs retrain-chain overlay 对比 |
| **K\* ceiling extrapolation 的 uncertainty quantification** | 🟢 低 | Linear/log 两种 fit 已在 analysis_report，可选入 appendix |

---

## E. 建议论文段落结构

### 方案 1：Discussion 段落（推荐）

在 Discussion/Analysis section 加一个 paragraph 或 subsection：

**"Retrain-Chain: Upper Bound on Discriminability"**

1. **Setup**（2 句）：Prompt-chain isolates text-intrinsic degradation; retrain-chain adds model-adaptation artifacts. 两者对应不同 real-world scenarios.
2. **Result**（3 句）：Retrain K\*=7 (Qwen, all CI > θ), K\*≥4 (Pythia, ongoing). 比 prompt K\*=2 多 5 generations. AUC 从 0.98 smooth decay 到 0.64，无 cliff structure.
3. **Mechanism**（2 句）：Each retrain step introduces cumulative vocabulary narrowing and repetition bias (consistent with model collapse literature: Shumailov et al. 2024). 这些 artifacts 提供 persistent depth signal absent in prompt-chain.
4. **Operational implication**（2 句）：Prompt-chain K\* is the conservative, generalizable boundary for data curation. Retrain-chain K\* represents the upper bound achievable when the training pipeline is known.

**需要的数据支撑**：
- Table 24 (appendix, 已有) 的 cross-reference
- Fig retrain_decay (appendix, 已有) 的 cross-reference
- Prompt vs retrain AUC 对比（可 inline 或新建 appendix table）

### 方案 2：Experiments subsection（备选）

如果 reviewer 认为 retrain-chain 应是核心 finding 而非 supporting analysis，可提升为 §4.x：

**"§4.x Retrain-Chain Extends K\* to 7 Generations"**

- 正文放 key numbers + AUC decay figure
- Appendix 放完整 per-fold 表 + JSD analysis
- 这个方案占用更多正文空间（~0.5 column），需要权衡

### Claims 与数据支撑映射

| Claim | 必需数据 | 数据来源 | 状态 |
|-------|---------|---------|------|
| Retrain K\*=7 | 7-pair AUC + CI | Table 24 | ✅ |
| Retrain K\* >> Prompt K\* | Side-by-side comparison | §B of this doc | ⚠️ 需入稿 |
| Cross-model consistency | Pythia K\*≥4 (→ full depth) | Table 24 + ongoing exp | ⚠️ Pythia ext pending |
| Smooth decay (no cliff) | JSD λ + cliff ratio | §JSD Decay Analysis | ✅ in appendix |
| K\* ceiling ≈ 7-8 | Extrapolation + JSD convergence | analysis_report | ✅ in appendix |
| Operational distinction (curation vs archaeology) | Qualitative framing | paper_framing.md Q6 | ⚠️ 需正文段落 |
| Model collapse connection | Literature citation + positioning | Shumailov, Alemohammad | ⚠️ 需 Related Work mention |

---

## F. 数据一致性检查

### exp_qwen_retrain_chain (depth 0-4) vs exp_qwen_retrain_depth7 (depth 0-7)

重叠的 depth 0-4 pairs 一致性：

| Pair | Original (final_results.json) | Extended (depth7_results.tex) | Δ |
|------|-------------------------------|-------------------------------|---|
| 0v1 | 0.9838 | 0.9837 | -0.0001 |
| 1v2 | 0.8969 | 0.8971 | +0.0002 |
| 2v3 | 0.8100 | 0.8098 | -0.0002 |
| 3v4 | 0.7624 | 0.7600 | -0.0024 |

最大差异 0.0024（3v4 pair），在 fold variance 内。Pipeline reproducibility confirmed.

### 论文中的数值 vs 原始数据

appendix_extended.tex Table 24 中的数值与 analysis_report.md 完全一致。✅

---

*Last updated: 2026-05-19*
*Source experiments: exp_qwen_retrain_chain, exp_qwen_retrain_depth7*
*Pending: Pythia retrain-chain depth extension results*
