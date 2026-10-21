# Citation Audit Round 4: Literature Survey + Bib Completion

Generated: 2026-05-17

---

## 新增引用清单

### zhou2024alignment
- **Title:** How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States
- **Authors:** Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, Yongbin Li
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2406.05644
- **BibTeX:**
```bibtex
@inproceedings{zhou2024alignment,
  title={How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States},
  author={Zhou, Zhenhong and Yu, Haiyang and Zhang, Xinghua and Xu, Rongwu and Huang, Fei and Li, Yongbin},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  pages={2461--2488},
  year={2024},
  url={https://arxiv.org/abs/2406.05644}
}
```
- **与本文关系:** 使用 weak classifiers 探测中间层 hidden states 以解释 safety alignment 机制，发现 LLM 在 early layers 即可区分恶意/正常输入。与本文 temporal probing 方法论直接相关，但它们研究标准 LLM 而非 reasoning models 的 CoT traces。
- **建议引用位置:** Related Work (hidden state probing for safety) + Introduction (motivation: prior work shows safety is encoded in intermediate layers)

---

### zhao2025harmfulness
- **Title:** LLMs Encode Harmfulness and Refusal Separately
- **Authors:** Jiachen Zhao, Jing Huang, Zhengxuan Wu, David Bau, Weiyan Shi
- **Venue:** NeurIPS 2025
- **arXiv:** 2507.11878
- **BibTeX:**
```bibtex
@inproceedings{zhao2025harmfulness,
  title={{LLMs} Encode Harmfulness and Refusal Separately},
  author={Zhao, Jiachen and Huang, Jing and Wu, Zhengxuan and Bau, David and Shi, Weiyan},
  booktitle={Advances in Neural Information Processing Systems 38 (NeurIPS)},
  year={2025},
  url={https://arxiv.org/abs/2507.11878}
}
```
- **与本文关系:** 证明 harmfulness 和 refusal 在表征空间中是独立编码的，且分布在不同 token positions。为本文"safety commitment 可在 hidden states 被检测"提供理论支撑，也解释了为什么 text-level probes 可能不如 hidden state probes（text 只捕获 refusal 信号，不一定捕获 harmfulness 编码）。
- **建议引用位置:** Related Work (representation of safety) + Discussion (interpreting HS advantage over text probes)

---

### hcot2025
- **Title:** H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking
- **Authors:** Martin Kuo, Jianyi Zhang, Aolin Ding, Qinsi Wang, Louis DiValentin, Yujia Bao, Wei Wei, Hai Li, Yiran Chen
- **Venue:** arXiv preprint, February 2025
- **arXiv:** 2502.12893
- **BibTeX:**
```bibtex
@article{hcot2025,
  title={H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models},
  author={Kuo, Martin and Zhang, Jianyi and Ding, Aolin and Wang, Qinsi and DiValentin, Louis and Bao, Yujia and Wei, Wei and Li, Hai and Chen, Yiran},
  journal={arXiv preprint arXiv:2502.12893},
  year={2025},
  url={https://arxiv.org/abs/2502.12893}
}
```
- **与本文关系:** 展示 reasoning models 的 CoT safety reasoning 可被 hijack，motivates 为什么需要 hidden-state level 的 safety monitoring 而非仅依赖 text-level CoT safety reasoning。直接支撑本文的 threat model。
- **建议引用位置:** Introduction (motivation: CoT safety reasoning is vulnerable) + Related Work (attacks on reasoning model safety)

---

### safedream2026
- **Title:** SafeDream: Safety World Model for Proactive Early Jailbreak Detection
- **Authors:** Bo Yan, Weikai Lin, Yada Zhu, Song Wang
- **Venue:** arXiv preprint, April 2026
- **arXiv:** 2604.16824
- **BibTeX:**
```bibtex
@article{safedream2026,
  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},
  author={Yan, Bo and Lin, Weikai and Zhu, Yada and Wang, Song},
  journal={arXiv preprint arXiv:2604.16824},
  year={2026},
  url={https://arxiv.org/abs/2604.16824}
}
```
- **与本文关系:** 使用 hidden states 构建 safety world model 做 proactive detection（多轮对话中提前检测 jailbreak）。与本文共享"用 hidden states 做早期 safety detection"的思路，但它关注 multi-turn 场景，本文关注 single-turn reasoning CoT traces。
- **建议引用位置:** Related Work (proactive safety detection via hidden states) + Experiments (concurrent work comparison in discussion)

---

### hu2026refusal_dynamics
- **Title:** Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection
- **Authors:** Xulin Hu, Che Wang, Wei Yang Bryan Lim, Jianbo Gao, Zhong Chen
- **Venue:** arXiv preprint, May 2026
- **arXiv:** 2605.02958
- **BibTeX:**
```bibtex
@article{hu2026refusal_dynamics,
  title={Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection},
  author={Hu, Xulin and Wang, Che and Lim, Wei Yang Bryan and Gao, Jianbo and Chen, Zhong},
  journal={arXiv preprint arXiv:2605.02958},
  year={2026},
  url={https://arxiv.org/abs/2605.02958}
}
```
- **与本文关系:** 标题相似（"Tracing the Dynamics of Refusal"），都研究 refusal 的动态过程。但方法和对象不同（见下方 Novelty Threat 评估）。
- **建议引用位置:** Related Work (concurrent work) + Discussion (differentiation)

---

### ahrend2026safer_traces
- **Title:** Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in LLMs
- **Authors:** Patrick Ahrend, Tobias Eder, Xiyang Yang, Zhiyi Pan, Georg Groh
- **Venue:** arXiv preprint, March 2026
- **arXiv:** 2603.05618
- **BibTeX:**
```bibtex
@article{ahrend2026safer_traces,
  title={Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in {LLMs}},
  author={Ahrend, Patrick and Eder, Tobias and Yang, Xiyang and Pan, Zhiyi and Groh, Georg},
  journal={arXiv preprint arXiv:2603.05618},
  year={2026},
  url={https://arxiv.org/abs/2603.05618}
}
```
- **与本文关系:** 研究 CoT reasoning traces 的安全问题（PII leakage），属于"reasoning trace safety"大领域。与本文关注的 safety commitment detection 不同，但共同说明 reasoning traces 的安全分析是活跃方向。
- **建议引用位置:** Related Work (safety of reasoning traces, broader context)

---

## Orphan 引用整合

### arditi2024refusal
- **建议引用位置:** Related Work (representation engineering for safety) + Experiments (baseline discussion)
- **建议引用句:** "Arditi et al. (2024) demonstrate that refusal in standard LLMs is mediated by a single linear direction in representation space, motivating our investigation of whether analogous structure exists in reasoning model CoT traces."

### chen2025unfaithful
- **建议引用位置:** Introduction (motivation) + Discussion (implications)
- **建议引用句:** "Recent work reveals that reasoning models do not always faithfully verbalize their internal computations (Chen et al., 2025), raising the question of whether text-level safety signals in CoT traces reliably reflect the model's internal safety state."

### wang2025lrmsafety
- **建议引用位置:** Introduction (background, 1st paragraph)
- **建议引用句:** "The safety challenges unique to large reasoning models have been systematically surveyed by Wang et al. (2025), highlighting the gap between standard alignment approaches and the emergent risks of extended chain-of-thought generation."

### alain2017understanding
- **建议引用位置:** Related Work (probing methodology)
- **建议引用句:** "Following the linear probing framework introduced by Alain and Bengio (2017), we train logistic regression classifiers on intermediate hidden states to detect safety-relevant signals."

### conneau2018probing
- **建议引用位置:** Related Work (probing methodology, same paragraph as alain2017)
- **建议引用句:** "Our probing methodology builds on the sentence-level probing paradigm of Conneau et al. (2018), adapted to track temporal dynamics across reasoning steps."

### kornblith2019cka
- **建议引用位置:** Discussion (cross-model transfer analysis)
- **建议引用句:** "To quantify representational similarity across model families, we employ Centered Kernel Alignment (CKA; Kornblith et al., 2019)."

### bansal2021stitching
- **建议引用位置:** Discussion (cross-model transfer analysis, same paragraph as CKA)
- **建议引用句:** "The feasibility of cross-model transfer is further supported by model stitching results (Bansal et al., 2021), suggesting that safety-relevant representations may share geometric structure across architectures."

---

## Novelty Threat 评估

### "Tracing the Dynamics of Refusal" (arXiv:2605.02958, Hu et al., May 2026)

**摘要:**
"Representation Engineering typically relies on static refusal vectors derived from terminal representations. We move beyond this paradigm, demonstrating that refusal is a dynamic and sparse process rather than a localized outcome. Using Causal Tracing, we uncover the Refusal Trajectory -- a persistent upstream signature that remains intact even when adversarial attacks (e.g., GCG) suppress terminal signals. Leveraging this, we propose SALO (Sparse Activation Localization Operator), an inference-time detector designed to capture these latent patterns. SALO effectively recovers defense capabilities against forced-decoding attacks, improving detection rates from ~0% to >90% where methods relying on terminal states perform poorly."

**与本文 overlap:**
- 共同主题：refusal 的动态性质，hidden states 包含 safety-relevant 信号
- 共同批评对象：static/terminal representation 方法（如 RepE）不够
- 表面术语重叠："dynamics of refusal"，"trajectory"

**关键差异（本文优势/独特性）:**

| 维度 | Hu et al. (2605.02958) | 本文 |
|------|----------------------|------|
| 对象模型 | 标准 LLM（对抗 GCG 攻击） | Reasoning models (DeepSeek-R1, QwQ 等) |
| "动态"含义 | 单次前向传播中跨层的 refusal 传播 | CoT 生成过程中跨时间步的 safety commitment 演变 |
| 方法 | Causal Tracing + Sparse Activation Localization | Temporal probing (logistic regression on HS per reasoning step) |
| 对比维度 | 无 text probe 对比 | Hidden state probes vs text probes，Holm-Bonferroni 显著性检验 |
| 目标 | 对抗性 jailbreak detection（forced decoding） | Safety commitment timing detection + probe modality comparison |
| 粒度 | Layer-wise（空间） | Step-wise（时间） |
| Key finding | Refusal trajectory persists upstream even under attack | HS probes detect commitment earlier than text probes; layer selection metric introduces systematic bias |

**Novelty threat 程度：低-中等**

两篇论文虽然在高层叙事上有重叠（"refusal is dynamic, not static"），但具体研究对象（标准 LLM vs reasoning models）、方法论（causal tracing vs temporal probing）、分析维度（空间/层 vs 时间/步）、和核心贡献（adversarial robustness vs probe modality comparison）完全不同。

**建议处理:**
1. 在 Related Work 中作为 concurrent work 引用，明确区分："While Hu et al. (2026) trace refusal dynamics across layers within a single forward pass, we trace safety commitment dynamics across reasoning steps during extended CoT generation."
2. 在 Introduction 中可作为进一步 motivation："Recent concurrent work (Hu et al., 2026) confirms that refusal is inherently dynamic even in standard LLMs, further motivating temporal analysis in reasoning models where the generation process itself spans many steps."
3. 无需大幅修改 framing 或 contribution claims。

---

## 引用覆盖度提升预估

- 现有 effective citations: ~15
- 新增 6 篇 + orphan 整合 7 篇 = +13
- 预计整合后 effective citations: ~28
- 仍需在后续 round 补充 evaluation benchmarks、jailbreak attacks、additional probing 方法论等引用以达到 40+ 目标
