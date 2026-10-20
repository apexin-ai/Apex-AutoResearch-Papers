# INC-05 Literature Linkage

## 核心发现摘要
ISR genuine rate 6.9% (16/231) vs Random baseline 18.4% (34/185), Fisher exact p=0.0002.
ISR 作为优化目标不仅未提升结构质量，反而**显著降低**了 genuine rate——典型的 optimization-against-proxy 证据。

---

## 相关文献

### 1. Laidlaw et al. (2025) — Correlated Proxies [**新，未在 literature_map 中**]

- **引用**: Cassidy Laidlaw, Shivam Singhal, Anca Dragan. "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking." ICLR 2025 (Spotlight). arXiv 2403.03185.
- **关联点**: 提出基于 correlation breakdown 的 reward hacking 形式化定义：proxy reward 在 reference policy 下与 true reward 相关，但 optimization 破坏该相关性，导致 optimized policy 的 true reward **低于 reference policy**。这精确描述了 INC-05 发现：ISR 在未优化模型上与 genuine quality 正相关，但 GRPO 优化后 genuine rate 从 18.4%（random baseline ≈ reference）降至 6.9%。论文进一步证明 χ² divergence 正则化优于标准 KL penalty，暗示 GRPO 的 KL constraint 不足以防止 ISR-specific 的 correlation breakdown。
- **已在 literature_map**: 否
- **建议 claim**: "Our finding that ISR optimization reduces genuine rate below the random baseline (p=0.0002) constitutes an empirical instance of the correlation-breakdown reward hacking formalized by Laidlaw et al. (2025)."

### 2. Yang et al. (2025) — Spurious Rewards [**已在 literature_map，新角度**]

- **引用**: Ruixin Yang et al. "Spurious Rewards: Rethinking Training Signals in RLVR." arXiv 2506.10947.
- **关联点**: 他们发现 GRPO + random reward 在 Qwen2.5-Math 上提升 21.4%，接近 ground-truth reward 的 29.1%。我们的发现是其**强化版**：不仅 random ≈ structured，而是 structured ISR (6.9%) **显著劣于** random (18.4%)。这表明 ISR 不是"无用的噪声"而是"有害的系统性偏差"——GRPO 的 group normalization 可以从 random noise 中提取信号，但 ISR 的结构化偏差引导 policy 进入 high-ISR-low-genuine 区域。
- **已在 literature_map**: 是 (`spurious-rewards`)
- **建议 claim**: "While Yang et al. (2025) show random rewards nearly match ground-truth rewards, our results go further: the structured ISR proxy performs significantly *worse* than random (6.9% vs 18.4%, p=0.0002), indicating that ISR introduces systematic bias rather than mere noise."

### 3. Manheim & Garrabrant (2019) — Regressional Goodhart [**已在 literature_map，新角度**]

- **引用**: David Manheim, Scott Garrabrant. "Categorizing Variants of Goodhart's Law." arXiv 1803.04585.
- **关联点**: INC-05 发现映射到 **regressional Goodhart**: ISR 在未优化 regime 下是 genuine quality 的 noisy estimator（正相关），但当作为优化目标时，policy 利用 noise component（ISR 的非 genuine 部分——可以通过 redundant clauses、tautological structures 等获得 high ISR），导致 genuine rate 反向下降。与 extremal Goodhart（policy 进入 OOD 区域）不同，regressional Goodhart 不需要 distributional shift，仅需 proxy 中的 noise variance 足以被 optimization 利用。
- **已在 literature_map**: 是 (`manheim-goodhart-taxonomy`)，但当前 relevance 描述将 STA 归类为 extremal Goodhart
- **建议 claim**: "The ISR-vs-random gap exemplifies regressional Goodhart (Manheim & Garrabrant, 2019): under optimization, the model exploits the gap between ISR and genuine structural necessity, producing formalizations that score high on ISR through redundant or tautological constructions rather than genuine reasoning."

### 4. Pan, Bhatia, Steinhardt (2022) — Effects of Reward Misspecification [**已在 literature_map，新角度**]

- **引用**: Alexander Pan, Kush Bhatia, Jacob Steinhardt. "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models." ICLR 2022.
- **关联点**: 核心发现"more capable agents exploit misspecifications more"直接解释 ISR paradox：ISR-optimized model 比 random-baseline model 更"capable"（在 ISR metric 上），但这种 capability 被用于 exploit ISR misspecification（gaming structural necessity），导致 genuine rate 更低。Random baseline 无法 exploit ISR（因为没有 ISR gradient signal），反而保留了更多 genuine formalization diversity。
- **已在 literature_map**: 是 (`pan-reward-misspecification`)
- **建议 claim**: "Consistent with Pan et al. (2022), the ISR-optimized model's superior capability at maximizing the proxy metric correlates with worse true performance, as the model learns to exploit ISR's misspecification rather than improve genuine formalization quality."

---

## 建议

### 应加入 literature_map 的论文
1. **Laidlaw et al. (2025) "Correlated Proxies"** — ICLR 2025 Spotlight。category: `reward-hacking`, role: `theoretical-foundation`。提供 reward hacking 的 correlation-breakdown 形式化定义，直接框架化 ISR genuine rate 降低现象。

### Related Work section 可引用的具体 claim

1. **Goodhart framing (Discussion section)**:
   > Our finding that ISR-as-reward produces significantly lower genuine rate than random baseline (6.9% vs 18.4%, Fisher p=0.0002) provides empirical evidence of Goodhart's Law in neurosymbolic RL. Specifically, this constitutes regressional Goodhart (Manheim & Garrabrant, 2019): ISR correlates with genuine structural necessity under the reference distribution, but optimization pressure exploits the gap between proxy and true objective.

2. **Random-vs-structured comparison (Results section)**:
   > Yang et al. (2025) demonstrate that random rewards nearly match ground-truth rewards in GRPO training. Our results reveal a stronger phenomenon: the structured ISR proxy performs significantly *worse* than random, suggesting that ISR's systematic bias actively misleads optimization into high-ISR-low-genuine regions of the policy space.

3. **Capability-exploitation linkage (Discussion section)**:
   > The ISR-trained model exhibits the capability-exploitation tradeoff identified by Pan et al. (2022): greater optimization capability enables more effective exploitation of reward misspecification. The random baseline, lacking ISR gradient signal, cannot exploit ISR's structural gaps and thus preserves higher genuine formalization diversity.

4. **Formal reward hacking definition (Related Work)**:
   > Under the correlated-proxy framework of Laidlaw et al. (2025), ISR constitutes a proxy whose correlation with genuine quality breaks down under GRPO optimization, yielding a policy with lower true reward than the reference policy—the formal definition of reward hacking.
