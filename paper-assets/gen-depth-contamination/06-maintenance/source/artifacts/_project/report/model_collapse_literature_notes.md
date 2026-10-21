# Model Collapse Literature Notes for Retrain-Chain Positioning

> 为论文 Discussion 中 retrain-chain (K*≥7 vs. prompt-chain K*=2) 的发现提供引用支撑。

---

## 1. Shumailov et al. (2024) — 奠基性工作

- **引用**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal. "AI Models Collapse When Trained on Recursively Generated Data." *Nature*, 631, 755–759, 2024.
- **核心发现**: 在 VAE、GMM、LLM 上系统验证了 model collapse 现象：递归训练导致分布尾部消失，模型输出逐代收敛到低方差的点估计。早期代次丢失低频模式（tail trimming），后期代次丢失高频模式（tail narrowing）。
- **与我们的关系**: 直接相关。他们关注的是质量退化（分布收敛），我们关注的是这种退化是否可被检测器区分。我们的 retrain-chain 实验本质上复现了他们的递归训练设定（LoRA fine-tune on own output），但测量的是代际可区分性而非输出质量。K*≥7 说明每代的分布漂移足够大，使检测器在 7 代内仍能区分相邻代次。
- **Bib key**: `shumailov2024collapse` ✅ 已在 references.bib

---

## 2. Alemohammad et al. (2024) — MAD 概念

- **引用**: Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk. "Self-Consuming Generative Models Go MAD." *Proceedings of ICLR*, 2024.
- **核心发现**: 提出 Model Autophagy Disorder (MAD) 概念。在图像生成模型上证明：纯合成数据递归训练导致质量和多样性持续下降；混入真实数据可减缓但不能完全阻止退化。区分了 fully synthetic loop 和 synthetic augmentation 两种场景。
- **与我们的关系**: MAD 框架适用于理解 retrain-chain：每代 LoRA fine-tune 构成 fully synthetic loop。他们的"质量/多样性退化随代数单调递增"与我们的"代际可区分性随代数保持"是同一现象的两面：distributional drift 既导致退化，也产生可检测的代际签名。
- **Bib key**: `alemohammad2024selfconsuming` ✅ 已在 references.bib

---

## 3. Dohmatob et al. (2024) — 理论 scaling law 视角

- **引用**: Elvis Dohmatob, Yunzhen Feng, Pin-Yu Yang, Francois Charton, Julia Kempe. "A Tale of Tails: Model Collapse as a Change of Scaling Laws." *Proceedings of ICML*, 2024.
- **核心发现**: 将 model collapse 形式化为 scaling law 的变化：递归训练使尾部概率以特定速率衰减，collapse 速率取决于数据维度和模型族。提供了 collapse 不可避免性的理论下界。
- **与我们的关系**: 他们的理论预测了每代分布漂移的量级。这解释了为什么 retrain-chain 的 K* 远高于 prompt-chain：retrain-chain 每代引入权重更新（LoRA），产生的分布漂移远大于仅改变输入（prompt-chain）所引起的漂移，因此代际签名更强、可区分的代数更多。
- **Bib key**: `dohmatob2024model` ✅ 已在 references.bib

---

## 4. Gerstgrasser et al. (2024) — Collapse 可避免性

- **引用**: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo. "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data." *Proceedings of COLM*, 2024.
- **核心发现**: 证明如果每代训练都累积保留之前所有真实数据（而非仅用上一代合成数据），model collapse 可以完全避免。关键条件：真实数据占比不能低于某阈值。
- **与我们的关系**: 我们的 retrain-chain 设定是 pure synthetic loop（每代仅用上一代输出），属于他们证明的"必然 collapse"情形。这恰好是我们需要的：持续的分布漂移保证了代际可区分性。如果混入真实数据（如他们建议的），collapse 减缓，代际签名也会减弱，K* 可能降低。
- **Bib key**: `gerstgrasser2024model` ✅ 已在 references.bib

---

## 5. Bertrand et al. (2024) — 迭代再训练的稳定性理论

- **引用**: Quentin Bertrand, Avishek (Joey) Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel. "On the Stability of Iterative Retraining of Generative Models on their Own Data." *Proceedings of ICLR* (Spotlight), 2024.
- **核心发现**: 为 likelihood-based 生成模型的迭代再训练提供稳定性理论框架。证明在初始模型足够接近真实分布、且每轮真实数据比例足够高的条件下，迭代再训练是稳定的（不会 collapse）。反之，纯合成循环不满足稳定性条件。
- **与我们的关系**: 提供了 retrain-chain 行为的理论解释。我们的纯合成 LoRA 循环不满足其稳定性条件，因此每代产生不可逆的分布漂移。这种理论预测的不稳定性正是代际可区分性的来源。
- **Bib key**: ❌ **不在 references.bib，需添加**

---

## 6. Briesch et al. (2023) — LLM 自消费训练实证

- **引用**: Martin Briesch, Dominik Sobania, Franz Rothlauf. "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop." arXiv:2311.16822, 2023.
- **核心发现**: 专门在 LLM 上实证研究自消费训练循环。发现递归训练导致词汇多样性下降、重复率上升、困惑度先降后升。退化速度与模型规模和采样温度相关。
- **与我们的关系**: 最直接的实证对照。他们测量的是质量指标（困惑度、多样性），我们测量的是可区分性（AUC）。两者互补：他们的质量退化曲线对应我们的可区分性保持曲线。可在 Discussion 中对照引用。
- **Bib key**: `briesch2023selfconsuming` ✅ 已在 references.bib

---

## 推荐 Positioning 文字（可直接用于 Discussion）

> The distributional drift underlying model collapse \citep{shumailov2024collapse, alemohammad2024selfconsuming} is typically framed as a failure mode: recursive training on synthetic outputs erodes tail coverage and reduces diversity \citep{dohmatob2024model, briesch2023selfconsuming}. Our retrain-chain results reveal a complementary perspective: the same per-generation drift that degrades output quality also produces generation-specific distributional signatures that remain detectable across at least seven iterations ($K^*\!\geq\!7$). Because each LoRA fine-tuning step modifies model weights, the distributional shift per generation far exceeds that of prompt-chain inference (where weights are frozen), explaining why retrain-chain sustains discriminability well beyond the $K^*\!=\!2$ ceiling observed for prompt-chain. This connects our work to theoretical analyses showing that pure synthetic loops are inherently unstable \citep{bertrand2024stability, gerstgrasser2024model}: the instability that drives collapse simultaneously enables depth-aware contamination detection.

---

## 需添加的 BibTeX 条目

```bibtex
@inproceedings{bertrand2024stability,
  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},
  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},
  booktitle={Proceedings of ICLR},
  year={2024},
  url={https://arxiv.org/abs/2310.00429}
}
```

---

## 已在 bib 中的相关条目汇总

| Bib key | 论文 | 核心角度 |
|---------|------|---------|
| `shumailov2024collapse` | Nature 2024 | 奠基性实证：尾部消失、分布收敛 |
| `alemohammad2024selfconsuming` | ICLR 2024 | MAD 概念：质量+多样性退化 |
| `dohmatob2024model` | ICML 2024 | 理论 scaling law：collapse 速率 |
| `dohmatob2025strong` | ICLR 2025 | Strong collapse 条件 |
| `gerstgrasser2024model` | COLM 2024 | 累积真实数据可避免 collapse |
| `kazdan2025collapse` | ICML 2025 | Collapse vs. thrive 条件分析 |
| `schaeffer2025position` | ICML 2025 | 澄清 collapse 定义误区 |
| `briesch2023selfconsuming` | arXiv 2023 | LLM 自消费循环实证 |
| `guo2024curious` | NAACL Findings 2024 | 语言多样性下降 |
| `shi2025collapse` | NeurIPS 2025 | 泛化→记忆视角 |
| `amin2025escaping` | NeurIPS 2025 | Weak data 逃逸 collapse |
| `drayson2025` | EMNLP 2025 | 检测防止 collapse（与我们最近） |
