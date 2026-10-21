# research related work gap check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_gap_check_20260524T011417_result.json`
- **Structured JSON:** [`63aeeb8df18d7d2743d1.json`](../../sessions/63/63aeeb8df18d7d2743d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成，整理结果。

## 搜索结果汇总
- 搜索了 8 组主要关键词 + 8 组跟进关键词
- 发现 **10 篇**潜在相关论文（排除已引用的）

---

## 需要关注的论文

### Paper 1: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **作者**: Grover, Gopalkrishnan, Ai, Christensen, Su, Li
- **时间**: Sep 2025, [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- **核心结论**: VLM→VLA fine-tuning 降解 pretrained representations，提出 dual-encoder（一个 frozen、一个 trainable）+ string-based action tokenizer + co-training 策略缓解
- **与我们的关系**: **直接互补** — 他们文档化了我们发现的同一现象（fine-tuning 导致 representation degradation），但从工程方案角度解决，我们从 mechanistic 角度刻画（R² exit collapse）
- **引用建议**: **建议引用** — Related Work 中作为"representation degradation during VLM→VLA fine-tuning"的工程方案对照

### Paper 2: "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling"
- **作者**: 未完全确认
- **时间**: Nov 2025, [arXiv 2511.19878](https://arxiv.org/abs/2511.19878)
- **核心结论**: 首个 VLA robust fine-tuning 框架；visual encoders 保持接近 pretrained priors，action-oriented language layers 更自由适配。跨 MiniVLA / OpenVLA-OFT / CALVIN / LIBERO 提升 up to +30%
- **与我们的关系**: **互补** — 他们发现 visual encoder 需要保持稳定、language layers 可以更大幅适配，与我们发现的 exit layer action collapse 一致（deeper language layers 变化最大）
- **引用建议**: **建议引用** — 支撑我们 exit collapse 发现的实用验证

### Paper 3: "Head Pursuit: Probing Attention Specialization in Multimodal Transformers"
- **作者**: Lorenzo Basile et al.
- **时间**: Oct 2025, NeurIPS 2025 spotlight, [arXiv 2510.21518](https://arxiv.org/abs/2510.21518)
- **核心结论**: 用 SOMP 发现 VLM 中 attention heads 对语义/视觉概念的 specialization；editing 1% heads 可 suppress/enhance 目标概念
- **与我们的关系**: **方法论相关** — 他们研究 VLM attention head specialization，我们研究 VLA 中 instruction-dominant attention heads。他们的发现（头部 specialization 是普遍现象）支撑我们的 L1 attention 分析
- **引用建议**: **建议引用** — Related Work 中作为 attention specialization 的一般性方法论参考

### Paper 4: "Look Before Acting: Enhancing Vision Foundation Representations for VLA Models" (DeepVision-VLA)
- **作者**: 未完全确认
- **时间**: Mar 2026, [arXiv 2603.15618](https://arxiv.org/abs/2603.15618)
- **核心结论**: 发现 VLA 中 visual token sensitivity 在 deeper layers 逐渐降低；提出 VL-MoT 架构注入多层级 visual features 到深层，提升 9.0%/7.5%
- **与我们的关系**: **互补** — 他们独立观察到类似现象（deeper layers visual info loss），我们的 R² exit collapse 提供了 mechanistic 解释（action fine-tuning 重写了 exit layer representations）
- **引用建议**: **建议引用** — 独立验证了 deep-layer representation 变化的现象

### Paper 5: "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting" (VLM2VLA)
- **作者**: 未完全确认
- **时间**: Sep 2025, [arXiv 2509.22195](https://arxiv.org/abs/2509.22195)
- **核心结论**: 将 robot actions 重表示为自然语言描述，使 fine-tuning 数据与 VLM pretrained representation space 对齐，仅用 LoRA 即可避免 catastrophic forgetting
- **与我们的关系**: **互补** — 他们的方案本质上是减少 VLM→VLA transition 对表征空间的冲击，与我们发现的 exit collapse 机制一致
- **引用建议**: **建议引用**

### Paper 6: "Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning"
- **作者**: Liu, Huihan; Kim, Changyeon; Liu, Bo; Liu, Minghuan; Zhu, Yuke
- **时间**: Mar 2026, [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- **核心结论**: Pretrained VLAs 在 continual learning 中极少遗忘；simple experience replay 几乎 zero forgetting；知识保留能力使技能快速恢复
- **与我们的关系**: **直接相关** — 他们的 "VLA→VLA resistant to forgetting" 与我们的 "VLA→VLA transition 无显著 collapse" 发现高度一致，从 continual learning 角度提供了互证
- **引用建议**: **建议引用** — 强烈互证我们的 VLA→VLA no-collapse 发现

### Paper 7: "Representational de-collapse: Interactions between SFT and ICL in Language Models"
- **作者**: 未完全确认
- **时间**: Mar 2026, ICLR 2026, [OpenReview](https://openreview.net/forum?id=iZ9eKf1ZCK)
- **核心结论**: SFT 沿 task labels 折叠 representations；ICL 可逆转此折叠恢复丰富表征
- **与我们的关系**: **概念相关** — "representational collapse from SFT" 的理论框架与我们的 "exit collapse from action fine-tuning" 概念相近，但在 NLP 而非 VLA 领域
- **引用建议**: **可以引用** — 作为 representation collapse 的 NLP 理论基础

### Paper 8: "Emergent World Representations in OpenVLA"
- **作者**: Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis
- **时间**: Sep 2025, [arXiv 2509.24559](https://arxiv.org/abs/2509.24559)
- **核心结论**: OpenVLA 内部编码了 emergent world model；linear probes 在 middle layers 发现 state transition 预测能力
- **与我们的关系**: **高度相关** — 同样对 OpenVLA 做 layer-wise probing 分析，发现 middle layers 信息最丰富
- **引用建议**: **需要确认** — 第一作者是 Marco Molinari，你们已引用的 "Molinari et al. 2025 — symbolic representations" 可能就是这篇。如果不是同一篇，则**必须引用**

### Paper 9: "From Intention to Execution: Probing the Generalization Boundaries of VLA Models"
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **时间**: Jun 2025, [arXiv 2506.09930](https://arxiv.org/abs/2506.09930)
- **核心结论**: VLM backbone 赋予 VLA robust perceptual understanding 和 high-level planning ("good intentions")，但不能可靠转化为精确运动执行；fine-tuning 侵蚀 VLM 推理能力
- **与我们的关系**: 第一作者 Irving Fang 与你们已引用的 "Fang et al. 2025 — reasoning erosion" 可能是同一篇。如果不是，则**建议引用**
- **引用建议**: **需要确认是否已引用**

### Paper 10: "Controlling Vision-Language-Action Policies through Sparse Latent Directions"
- **作者**: 未完全确认
- **时间**: Sep 2025, NeurIPS 2025 Mech Interp Workshop, [OpenReview](https://openreview.net/forum?id=wtf3ww1EOL)
- **核心结论**: 在 SAE latent space 中 steer VLA 的 language backbone 实现 fine-grained action control
- **与我们的关系**: 可能与已引用的 Haon et al. 2025 是同一工作的 workshop 版本
- **引用建议**: **需要确认** — 如果是 Haon et al. 的 companion paper 则无需额外引用

---

## 结论

**无重大遗漏，但有几篇值得补充引用。**

核心发现：
1. **没有发现直接竞争论文** — 没有其他团队做过跨架构的 VLM→VLA exit collapse 机制分析，我们的工作在这个方向上是首创
2. **有 6 篇建议引用的互补论文**（Paper 1-6），它们从工程/训练/continual learning 角度验证了与我们发现一致的现象（representation degradation, forgetting resistance, attention specialization）
3. **有 2 篇需要确认是否已引用**（Paper 8 Molinari, Paper 9 Fang）— 请核实 bib 文件中 Molinari et al. 2025 和 Fang et al. 2025 对应的具体论文
4. Paper 6 (Liu et al. 2026 continual learning) 对我们 "VLA→VLA no collapse" 发现提供了最强独立互证

Sources:
- [Enhancing Generalization in VLA Models](https://arxiv.org/abs/2509.11417)
- [MAPS: Module-Wise Proximity Scheduling](https://arxiv.org/abs/2511.19878)
- [Head Pursuit: Attention Specialization](https://arxiv.org/abs/2510.21518)
- [Look Before Acting: DeepVision-VLA](https://arxiv.org/abs/2603.15618)
- [Actions as Language: VLM2VLA](https://arxiv.org/abs/2509.22195)
- [Pretrained VLAs Resistant to Forgetting](https://arxiv.org/abs/2603.03818)
- [Representational de-collapse (ICLR 2026)](https://openreview.net/forum?id=iZ9eKf1ZCK)
- [Emergent World Representations in OpenVLA](https://arxiv.org/abs/2509.24559)
- [From Intention to Execution](https://arxiv.org/abs/2506.09930)
- [Controlling VLA through Sparse Latent Directions](https://openreview.net/forum?id=wtf3ww1EOL)
- [Not All Features Are Created Equal](https://arxiv.org/abs/2603.19233)
- [Mechanistic Interpretability for Steering VLAs](https://arxiv.org/abs/2509.00328)
- [Sparse Autoencoders in VLA Models](https://arxiv.org/abs/2603.19183)
- [DySL-VLA](https://arxiv.org/abs/2602.22896)
- [NoTVLA](https://arxiv.org/abs/2510.03895)
- [VLA-GSE](https://arxiv.org/abs/2605.06175)

---
