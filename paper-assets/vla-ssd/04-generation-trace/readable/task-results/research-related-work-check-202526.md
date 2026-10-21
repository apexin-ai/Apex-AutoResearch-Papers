# research related work check 202526

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_check_202526_20260524T233145_result.json`
- **Structured JSON:** [`b2636e4f1eb4eec936f7.json`](../../sessions/b2/b2636e4f1eb4eec936f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是完整报告。

---

## Related Work 遗漏论文检查报告

### 已确认引用（无需操作）

以下搜索中频繁出现的论文已在 `related_work.tex` 中引用：
- Grant et al. (2603.19233) → `grant2026`
- Swann et al. (2603.19183) → `swann2026`
- Buurmeijer et al. (2603.05487) → `buurmeijer2026`
- Molinari et al. (2509.24559) → `molinari2025`
- Lu et al. (2502.04558) → `lu2025`
- Haon et al. (2509.00328) → `haon2025`
- Fang et al. counterfactual benchmark → `fang2026when`
- Liu et al. (2603.03818) continual learning → `liu2026forgetting`
- Grover et al. → `grover2025preserving`

---

### 必须引用（3 篇）

#### 1. "Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization"
- **arXiv**: [2510.25616](https://arxiv.org/abs/2510.25616)
- **时间**: 2025-10-29
- **作者**: Kachaev et al.
- **与我们的关系**: **直接竞争** — 通过 t-SNE 分析发现 VLA 在 action fine-tuning 时产生 representation collapse（多样化内部特征被压缩到狭窄表征空间），这与我们的 exit collapse (ΔR² > 0.10) 本质上是同一现象的不同观测角度。他们还观察到 domain-specific forgetting。提出轻量级 visual representation alignment 方法缓解。
- **为什么必须引**: 如果 reviewer 看到我们声称发现 exit collapse 但没引这篇，会认为 novelty claim 有问题。需在 VLA paragraph 或 concurrent work 中讨论，区分我们的贡献（跨架构对照、量化 ΔR² metric）和他们的（t-SNE 可视化 + alignment 方法）。

#### 2. "Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations"
- **arXiv**: [2511.22697](https://arxiv.org/abs/2511.22697)
- **时间**: 2025-11-27
- **作者**: Mitra, Luo, Saravanan, Niu, Pai, Thomason, Darrell, Anwar, Ramanan, Herzig
- **与我们的关系**: **互补** — 提出 "Robotic Steering"，利用 mechanistic interpretability 识别 task-specific attention heads 并选择性微调。他们用 attention head 分析 → 指导 fine-tuning，我们用 cross-architecture probing → 理解 routing 机制。
- **为什么必须引**: 这是唯一一篇将 VLA mechanistic interpretability 与 attention head selection 直接关联的工作。我们的 L1 instruction attention 发现与他们的 task-specific head identification 互为佐证。放在 mechanistic analysis paragraph。

#### 3. "Instruction Anchors: Dissecting the Causal Dynamics of Modality Arbitration"
- **arXiv**: [2602.03677](https://arxiv.org/abs/2602.03677)
- **时间**: 2026-02-03
- **作者**: Zhang, Xu, Bai, Chen, Zhang, Xiang, Zhang
- **与我们的关系**: **方法相关 + 互补** — 研究 multimodal LLM 中 instruction token 如何充当 modality arbitration 的结构锚点。发现 shallow attention layers 将多模态信息路由到 instruction tokens 形成 "latent buffer"，deep layers 解决模态竞争。这与我们发现的 "L1 instruction attention 来自预训练 backbone" 高度吻合。
- **为什么必须引**: 他们的 "instruction anchors" 机制是我们 instruction routing 发现在 VLM 领域的直接 counterpart。尽管他们的分析对象是通用 MLLM 而非 VLA，但机制层面的一致性值得讨论。放在 mechanistic analysis paragraph，指出他们在 VLM 中发现的 instruction routing 模式在我们的 VLA 分析中同样成立。

---

### 建议引用（4 篇）

#### 4. "Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies"
- **arXiv**: [2605.17204](https://arxiv.org/abs/2605.17204)
- **时间**: 2026-05-17
- **作者**: Jin, Chatterjee, Kumar, Paleja (Purdue)
- **与我们的关系**: **互补/concurrent** — 提出 event-grounded SAE pipeline，将 SAE 特征分析锚定到行为事件而非文本上下文。在 OpenVLA 和 π₀.₅ 上验证。扩展了 Swann2026 的 SAE 工作线。
- **建议位置**: Concurrent work paragraph，与 swann2026 并列。

#### 5. "CAST: Counterfactual Labels Improve Instruction Following in VLAs"
- **arXiv**: [2508.13446](https://arxiv.org/abs/2508.13446)
- **时间**: 2025-08-19
- **作者**: Glossop, Chen, Bhorkar, Shah, Levine (Berkeley)
- **与我们的关系**: **互补** — 用 VLM 生成 counterfactual labels 来增强 VLA 的 instruction following（成功率提升 27%）。与我们的 counterfactual perturbation 分析和 Fang2026 的 counterfactual benchmark 形成三方互补。
- **建议位置**: Concurrent work paragraph 中讨论 counterfactual 方法时提及。

#### 6. "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting"
- **arXiv**: [2509.22195](https://arxiv.org/abs/2509.22195)
- **时间**: 2025-09-26
- **作者**: Hancock et al.
- **与我们的关系**: **互补** — 指出 VLM→VLA 的 catastrophic forgetting 源于分布 mismatch，提出 VLM2VLA（natural language actions + LoRA）。为我们观察到的 exit collapse 提供了一种实际解决方案。
- **建议位置**: VLA paragraph，与 grover2025preserving 并列讨论 representation-preserving 策略。

#### 7. "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"
- **arXiv**: [2605.06175](https://arxiv.org/abs/2605.06175)
- **时间**: 2026-05-07
- **作者**: Jiang et al. (MSRA + Tsinghua)
- **与我们的关系**: **互补** — 通过 spectral decomposition 分离 generalized/specialized experts，避免 fine-tuning 覆写核心 spatial representations。从方法角度印证我们 exit collapse 发现的重要性。
- **建议位置**: VLA paragraph，作为 representation-preserving 方法的最新进展。

---

### 可选引用（3 篇）

#### 8. "Alignment among Language, Vision and Action Representations"
- **arXiv**: [2601.22948](https://arxiv.org/abs/2601.22948)
- **时间**: 2026-01
- **作者**: Milano & Nolfi
- **关系**: 在 BabyAI 平台上发现跨模态表征趋同，概念相关但实验规模和对象差异较大。

#### 9. "The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety"
- **arXiv**: [2602.15799](https://arxiv.org/abs/2602.15799)
- **时间**: 2026-02
- **关系**: 从几何角度分析 fine-tuning 导致的 alignment collapse，机制分析有概念借鉴意义，但领域是 LLM safety 而非 VLA。

#### 10. "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success"
- **arXiv**: [2502.19645](https://arxiv.org/abs/2502.19645)
- **时间**: 2025-02
- **关系**: 系统研究 VLA fine-tuning 设计选择（action decoding, action representation, learning objective），偏应用性。

---

### 总结

**必须引用的遗漏**有 3 篇，按紧急程度排序：

1. **Kachaev et al. (2510.25616)** — 与 exit collapse 发现直接重叠，不引会被 reviewer 质疑 novelty
2. **Mitra et al. (2511.22697)** — VLA mechanistic interpretability + attention head 分析，与我们的核心方法论最接近
3. **Zhang et al. (2602.03677)** — instruction anchors 机制与我们的 instruction routing 发现高度一致

**建议引用** 4 篇（Jin 2605.17204, Glossop 2508.13446, Hancock 2509.22195, Jiang 2605.06175），可丰富 related work 的覆盖面但不引也不致命。

---
