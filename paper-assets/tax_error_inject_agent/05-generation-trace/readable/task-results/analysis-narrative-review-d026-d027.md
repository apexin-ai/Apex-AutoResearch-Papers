# analysis narrative review d026 d027

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_narrative-review-d026-d027_20260515T153818_result.json`
- **Structured JSON:** [`9a31f72119f5c4d24ee1.json`](../../sessions/9a/9a31f72119f5c4d24ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

# 叙事审查报告：D026/D027 新发现对 Paper Narrative 的影响

## 1. D026: TaxEI loop_repetition 2.2× (Qualitative Failure Analysis)

### (a) 对 Core Claims 的影响

| Claim | 影响 | 说明 |
|-------|------|------|
| **C1**: TaxEI 高方差、无改善 | ✓ 支持 | loop_repetition 提供了 *为什么* 性能下降的机制解释——模型陷入重复循环而非探索新策略 |
| **C2**: Taxonomy 标签特别损害多步协调任务 | ✓ 支持 | P1=15, P2=14 最高，恰好是多步协调类 operator，与 pick_cool/pick_two 退化一致 |
| **C3**: 注入增加训练不稳定性 | ✓ 支持 | fixation 模式解释了为什么某些 seed 崩溃——模型在某些随机初始化下更易陷入重复循环 |
| **C4**: 注入不改善 recovery | ✓ 支持 | loop_repetition 说明模型学到的不是 recovery 策略而是 fixation——直接解释 recovery 失败 |
| **C5**: Detection 完全无效 | — 无关 | |
| **C6**: 任务结构边界条件 | ✓ 支持 | fixation 是 embodied planning 特有的失败模式（tool-use 中 retry 是局部操作，不会产生 loop_repetition） |
| **C7**: Recovery-paired 实验 | — 待定 | 但预测：如果 fixation 是根本问题，recovery-paired 也救不了 |
| **C8**: 跨环境泛化 | — 待定 | |

**关键数据对比**: TaxEI 49 vs Random 6 (8.2×) 是最强的 TaxEI-specific 负面信号。Random 几乎不产生 loop_repetition，说明这不是注入本身的问题，而是 **taxonomy 标签特有的**。这直接强化 C2（taxonomy penalty）。

### (b) 是否需要调整 paper framing?

**需要局部增强，不需要结构调整。** 现有 framing 的 "taxonomy labels amplify variance" 是统计层面的描述，D026 提供了行为层面的 mechanistic 解释。建议：

- **Claim 6 的 structural analysis 中新增一行**：在 tool-use vs embodied planning 对比表中增加 "Failure mode" 维度——tool-use 失败是 discrete error（可 retry），embodied planning 失败是 loop fixation（需全局 re-plan）
- **Claim 2 的 evidence 补充**：当前只有统计数据（pick_cool -19pp），D026 提供了 *机制*：taxonomy 标签让模型在多步任务上学到 fixation pattern，因为这些任务的 error 注入涉及 step reordering (P1) 和 sub-goal deletion (P2)

### (c) 8 页长文整合方案

- **Section**: Results → 新增 "§4.4 Qualitative Failure Analysis" 子节，紧接 dose-response 和 per-task analysis 之后
- **篇幅**: ~半页文字 + 1 个 figure（bar chart: loop_repetition counts by method × operator，4 组 × 3 条）
- **呼应关系**:
  - 回指 §4.2 per-task analysis 的 pick_cool/pick_two 退化 → "我们进一步分析 *如何* 失败"
  - 前引 §5 Discussion 的 structural analysis → "fixation 是 embodied planning 特有的"
  - 与 D027 training dynamics 形成互补：D027 说 "模型学到了注入内容"，D026 说 "学到的内容具体是 fixation pattern"

---

## 2. D027: 训练 loss 跨 seed 极稳定，eval 高方差

### (a) 对 Core Claims 的影响

| Claim | 影响 | 说明 |
|-------|------|------|
| **C1**: TaxEI 高方差、无改善 | △ 修改 | 需要精确化：**eval 方差不是训练不稳定导致的**。训练极稳定 (SD=0.0004) 但 eval 高方差 (SD=8.6pp)，说明方差来源是 representation/generalization 层面 |
| **C2**: Taxonomy 标签损害多步任务 | — 无关 | training dynamics 不区分 task type |
| **C3**: 注入增加训练不稳定性 | ✗ **反对当前措辞** | 现有 Claim 3 说 "training instability"——D027 证明 **训练本身完全稳定**。不稳定发生在 eval（generalization），不是 training。措辞需从 "training instability" 改为 "generalization instability" 或 "evaluation instability" |
| **C4**: 注入不改善 recovery | — 无关 | |
| **C5**: Detection 完全无效 | — 无关 | |
| **C6**: 任务结构边界条件 | ✓ 支持 | 加深了 structural 解释——在 embodied planning 中，模型可以在训练分布上 converge 但无法泛化到 clean eval，因为注入的 error pattern 与 clean task 的 action distribution 存在不可调和的冲突 |
| **C7/C8** | — 待定 | |

**关键洞察**: 50% injection final loss 最低 (0.26) 但 eval 最差 (51.1%)。这是 **memorization-generalization dissociation** 的直接证据。模型并非 "学不会注入内容"——恰恰相反，它学得 *太好* 了，以至于损害了 clean task 泛化。

### (b) 是否需要调整 paper framing?

**需要调整 Claim 3 措辞和 §3/§5 的解释框架。**

具体调整：

1. **Claim 3 改写**: 
   - 旧: "Error injection increases **training instability** disproportionately"
   - 新: "Error injection produces **stable training but unstable generalization** — a memorization-generalization dissociation that increases cross-seed evaluation variance"
   
2. **Training-evaluation paradox 升级为独立发现**:
   - 当前 paper_framing 中 training-eval paradox 在 §3 末尾简短提及
   - D027 提供了精确数据（SD=0.0004 vs SD=8.6pp），足以成为独立的 subsection
   - 与文献链 (Arpit 2017 memorization + Zhou 2023 LIMA superficial alignment) 已在 memory.md 中建立

3. **Story arc 调整**: 现有 arc 是 "注入加噪声 → 训练不稳定 → 性能下降"。D027 修正为 "注入被有效学习 → 训练 loss 下降 → 但学到的内容与 clean task 冲突 → eval 退化"。这是更强的论点——不是 "方法不 work"，而是 "方法 work 得太好但方向错了"。

### (c) 8 页长文整合方案

- **Section**: Results → "§4.5 Training Dynamics Analysis"，在 Qualitative Failure Analysis (§4.4) 之后
- **篇幅**: ~半页文字 + 1 个 figure（双 y 轴图：training loss curves 3 seeds 叠加 + eval SR scatter plot，展示 loss 收敛 but eval 分散）
- **呼应关系**:
  - 回指 §4.1 main results 的方差梯度 → "我们追溯方差来源"
  - 与 D026 loop_repetition 形成因果链：训练稳定地学到了 fixation pattern (D027) → 这些 pattern 在 eval 表现为 loop_repetition (D026)
  - 前引 §5 Discussion：连接到 Arpit 2017 memorization dynamics 和 LIMA superficial alignment hypothesis
  - 为 forward pass per-sample loss（待完成实验）提供预测和动机

---

## 3. Forward Pass Per-Sample Loss（待完成）

### (a) 预期影响（基于 hypothesis，非实际数据）

| Claim | 预期影响 | 条件 |
|-------|----------|------|
| **C1** | ✓ 支持（若确认 injected loss < clean loss） | 证明模型对注入样本记忆更深 |
| **C3** | ✓ 支持 | 为 memorization-generalization dissociation 提供 sample-level 证据 |
| **C6** | ✓ 支持 | clean vs injected loss gap 越大，说明 distribution conflict 越严重 |

**不做进一步推断。** 等实际数据再更新。

### (c) 整合方案（预留位）

- **Section**: 与 D027 合并为 §4.5 Training Dynamics Analysis 的 subsection
- **篇幅**: ~1/4 页 + 1 个小图（histogram: per-sample loss distribution, clean vs injected）
- **如果结果不符合预期**: 同样有价值——说明 memorization 不是 sample-selective 的，而是 distributional shift

---

## Overall Assessment

### 核心判断

三个发现 **强化而非颠覆** 现有 narrative，但需要一个重要的措辞修正：

**必须修改**: Claim 3 "training instability" → "generalization instability"。D027 明确证伪了 "训练不稳定" 的说法。这不是小修——它改变了 failure mechanism 的解释：从 "注入是噪声，破坏训练" 变为 "注入被有效学习，但学到了错误的东西"。后者是更深刻、更有贡献的论点。

### Story Arc 升级

现有 arc: motivation → method → no benefit + high variance → structural analysis → contributions

建议升级为因果链式叙事:

1. **Motivation**: error injection should work (PALADIN)
2. **Method**: TaxEI for embodied planning
3. **Main Results**: no benefit, variance gradient (§4.1-4.3, 现有)
4. **Why it fails — behavioral level**: TaxEI 产生 loop fixation, 集中在多步任务 (§4.4, D026)
5. **Why it fails — representation level**: 训练稳定地 memorize 了 injection pattern, 但 generalization 崩溃 (§4.5, D027)
6. **Structural analysis**: 这些 failure mode 是 embodied planning 特有的 (§5, 现有 + 加强)

D026 和 D027 填补了 §4.1-4.3 (统计描述) 和 §5 (结构分析) 之间的 **mechanistic gap**，使论文从 "描述了一个 negative result" 升级为 "解释了 *为什么* 是 negative result"。

### 篇幅预算

| Section | 现有内容 | 新增 | 总计 |
|---------|---------|------|------|
| §1 Intro | ~1p | 无 | ~1p |
| §2 Method | ~1.5p | 无 | ~1.5p |
| §3 Related Work | ~0.5p | 扩展到 ~0.75p (dream review 要求) | ~0.75p |
| §4 Results | ~2p | +§4.4 failure analysis (~0.5p) + §4.5 training dynamics (~0.5p) | ~3p |
| §5 Discussion | ~1p | Claim 3 措辞修正, 加 fixation 解释 | ~1p |
| §6 Conclusion | ~0.5p | 无 | ~0.5p |
| References | ~0.75p | | ~0.75p |
| **Total** | ~7.25p | +~1p | **~8.5p** |

略超 8 页，需压缩约半页。建议将 dose-response 的 per-seed 详细数据移至 appendix，为 §4.4/§4.5 腾出空间。

### 优先级

1. **立即**: 修改 Claim 3 措辞（training → generalization instability）
2. **写作时**: D026 的 loop_repetition figure 设计和 §4.4 起草
3. **待数据**: forward pass per-sample loss 实验完成后更新 §4.5

---
