---
round: 40
review_mode: continue
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-22T01:57:25.380877+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 40 (Continue Review)

**论文**: Depth Fingerprinting: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 via ARR May 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性; R2: 新颖性+完整性）
**模式**: 修订评估（基于 Round 39 意见）
**交叉验证**: 完成，1 轮收敛

---

## Summary

修订版实质性回应了 Round 39 的两个最 critical 问题：(1) DDR 现有形式化定义 DDR_f = |ρ(depth, f)| + k-means validation + 理论动机；(2) 三个不同族 reference model 消融（F1 spread <0.013）convincingly 排除了 Pythia proximity confound。页面溢出问题仍存在（~8-10 行），QLoRA 指标引用有新的混淆问题。

---

## Round 39 Issues 修复状态

### 已解决 (Round 40 确认)

| Issue | 状态 | 修复内容 |
|-------|------|---------|
| R32-N1 DDR 形式化 | ✅ RESOLVED | DDR_f=\|ρ(depth,f)\| + k-means(sil=0.660) + mixing motivation |
| R39-N1 Reference model confound | ✅ RESOLVED | 3 ref models (Pythia/OLMo/Qwen), F1 spread 0.013, partition invariant |
| R32-W4 Cross-domain/instruct 主文数字 | ✅ RESOLVED | Discussion: binary F1=0.74-0.75, 3-class=0.62-0.65; instruct -3.7-19.9pp |
| R32-W6 gen-0 shared-seed caveat | ✅ RESOLVED | Section 4.1 explicit bias note + independent-seed F1=0.68 |
| R39-W2 Concurrent work 区分 | ✅ RESOLVED | Section 2.2 inline differentiation + Table 45 cross-ref |
| R32-N3 TOST power | ✅ RESOLVED* | Caveat in main text + Table 29 bootstrap (B=1000) |

*R1 标 "partially" 因 caveat 指向 depth levels 而非 seeds，但 bootstrap 实质性缓解。

### 仍需修复 (camera-ready 级别)

| Issue | 状态 | 所需修改 |
|-------|------|---------|
| R39-N2 页面溢出 | 🟡 ~8-10 行溢出 | Figure 3 移附录或压缩 Discussion |
| R34-W3 + R40-W1 QLoRA 指标混淆 | 🟡 minor | "F1=0.905" → "binary F1=0.905; 3-class=0.805" |
| R40-W2 "mixing property" 无引用 | 🟡 minor | 标为 conjecture 或加 Markov chain citation |
| R34-V1 缺 method overview figure | 🟡 推荐 | p.2-3 加 pipeline 概览图 (非必须) |

---

## Strengths (修订后新增)

1. **Cross-reference-model 消融** (Round 40 新增): 三个不同族 reference model 的一致性验证（F1 spread 0.013）是本轮最有说服力的实验补充，彻底消除了 Pythia family proximity confound。
2. **DDR 形式化定义**: DDR_f = |ρ(depth, f)| 配合 k-means + permutation test 双重验证，使概念从 post-hoc 描述升级为可操作的定量框架。
3. **原有优势保持**: 8-gen LOGO 严谨性、22 页附录覆盖度、transparent reporting of negative results。

---

## Weaknesses (修订后残余)

### 结构性限制（不可修改，影响 Excitement）
1. **Base-model-only scope**: Instruction-tuned 模型下 DDR 失效（silhouette 0.372 vs 0.660）。实际 LLM 文本主要来自 instruction-tuned 模型。
2. **3-class depth resolution**: gen-2+ 合并，5-class F1=0.50。
3. **Downstream utility 阴性**: depth-aware curation ≈ random（TOST equivalence）。

### 可修改问题（camera-ready）
4. **页面溢出 ~0.15 页**: Discussion + Conclusion 溢出到 p.9。两位 Reviewer 共识：不构成 reject 理由，但 camera-ready 必须修复。
5. **QLoRA F1 指标混淆**: Discussion 中 "F1=0.905" 紧跟 "5-class F1=0.50"，未标注 binary/3-class，误导性 juxtaposition。

---

## Reviewer Consensus (Round 40)

**全部技术问题达成共识：**
- [AGREE] DDR 形式化定义 RESOLVED
- [AGREE] Reference model 消融 convincingly RESOLVED
- [AGREE] QLoRA 指标混淆是 valid concern (minor severity)
- [AGREE] 页面溢出是 camera-ready fix
- [AGREE] "mixing property" 需引用或标 conjecture

## Reviewer Divergence (Round 40)

**核心分歧：Soundness vs. Excitement 权重**

| 维度 | R1 | R2 | 分歧 |
|------|----|----|------|
| Soundness | 4.0 | 4.0 | **一致** |
| Excitement | 3.0 | 2.5 | R1: scoped novelty 足以 merit Conference; R2: structural cap |
| Overall | **4.0** | **3.0** | 1.0 分差 |

**R1 立场**: DDR 是首次形式化的 depth classification task，在 base-model scope 内做了 exemplary 的 empirical work。Scoped contributions 可以是 Conference-level（ACL/EMNLP 每年接收大量 narrowly-scoped 工作）。

**R2 立场**: Conference-level 需要 actionable value（推动 benchmark/改善 pipeline/扩展到主流场景）。本文在三个维度均未达到：3-class 太粗、downstream 阴性、instruct 失效。

**两位 Reviewer 均认为这是 legitimate disagreement，适合 AC/SAC 裁定。**

---

## Visual Layout Check（非评分项）

视觉审查完成（0 critical, 4 warning, 8 info）：

**Warnings:**
1. Pages 1-2 纯文本（Title/Abstract/Intro/RW），审稿人前 2 分钟无视觉锚点
2. 全文无 method overview figure（3 个 figure 均为实验结果可视化），审稿人在 Method 段 (p.3-4) 全靠文字理解方法
3. 附录 Figure 编号顺序错乱（Figure 9/10 在 Figure 8 之前，LaTeX float 漂移）
4. 最后一页底部 ~1/3 空白

**Info (正面):**
- 全文无 margin overflow、无 LaTeX 渲染错误、无 [?] 未解析引用
- 表格均使用 booktabs 风格，最优结果加粗，格式质量高
- 主文 display items 密度合理（6个/8页 = 0.75/页）
- Figure 1 strip plot 质量良好，颜色区分度高

---

## Questions (需作者澄清)

1. "mixing property of finite vocabularies" 的理论依据是什么？是否有 Markov chain 文献支持？
2. QLoRA Discussion 段中的 "F1=0.905" 是 binary 还是 3-class LOGO？请在 camera-ready 中明确标注。

---

## Missing References

Round 40 无新增缺失引用。Round 39 建议的 arXiv:2511.17602 的 relevance 仍待验证。

---

## Overall Assessment

**评分: 3.5 — Borderline Conference**

**置信度: 4/5**

**评分依据**:

| 因素 | 权重 | 评估 |
|------|------|------|
| Soundness | 高 | 4.0 — DDR 形式化 + cross-ref 消融使方法论达到 Conference 标准 |
| Excitement/Impact | 高 | 2.5-3.0 — base-model scope + 3-class resolution + 无正向 downstream 限制实际影响力 |
| Presentation | 中 | 3.5 — 页面溢出 + QLoRA 指标混淆需 camera-ready 修复 |
| Reproducibility | 低 | 4.0 — 代码/数据承诺公开，实验描述充分 |

**3.5 的裁定逻辑**：
- R1 (4.0) 和 R2 (3.0) 的分歧是 legitimate 的 Soundness-vs-Excitement 权重差异
- 论文在其声明的 scope 内做得 rigorous 且 novel（DDR 首次形式化 + cross-ref validation + comprehensive ablations）
- 但 structural limitations（base-model-only, 3-class, no downstream utility）确实限制了对 community 的即时 actionable impact
- 3.5 = Borderline Conference 反映了这种 tension：technically sufficient for Conference with caveats, but would benefit from AC consideration of scope vs. rigor trade-off

**Camera-ready 硬性要求（若接收）**：
1. 🔴 正文收回 8 页（Figure 3 移附录）
2. 🟡 QLoRA F1 指标标注修正
3. 🟡 "mixing property" 标为 conjecture 或加引用

**修改优先级（若 resubmit）**：
1. 扩展到 instruction-tuned 模型（打破最大结构性限制）
2. 探索 depth signal 在 corpus auditing/contamination detection 中的正向应用
3. 5+ class fine-grained classification 的方法改进
