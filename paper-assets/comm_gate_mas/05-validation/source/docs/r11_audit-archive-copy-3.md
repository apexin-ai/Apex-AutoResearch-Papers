# R11 审稿意见全面对照审计

> 审计日期: 2026-04-26
> R11 评分: Borderline Accept 5.5/10
> 决策: D142 (2026-04-25 16:37 UTC), D143 (2026-04-25 17:17 UTC)
> D143 结论: 7 条全部写作修正，0 条需要新实验

---

## Writing Issues (W1-W7)

### W1: TOST reframe — ±3pp non-inf 为 primary claim ✅

**审稿意见**: TOST ±1pp p=0.048 borderline 且无先验依据，应以 ±3pp non-inferiority (p<0.001) 为 primary claim。

**论文现状**:
- Abstract: "non-inferiority at δ = -3 pp (p < 0.001) and TOST equivalence at ±1 pp" — non-inf 在前
- Introduction C2: "non-inferiority at δ = -3 pp (p < 0.001) and **supplementary** TOST equivalence at ±1 pp" — 明确标记 supplementary
- Results §5.2: 先报 non-inf，再报 TOST
- Conclusion: "non-inferiority at δ = -3 pp (p < 0.001) and TOST equivalence at ±1 pp"

**判定**: 充分回应。±3pp non-inf 已全面升级为 primary claim，±1pp TOST 降为 supplementary。

---

### W2: Cascade dissolution 降级为 proposed explanation ✅

**审稿意见**: Cascade dissolution 被过度 claim 为确定性机制，应降级为假说。

**论文现状**:
- Abstract: "We **propose** that self-reinforcing ack cascades create structural redundancy that dissolves under aggregate removal...distinct from human backchannel dynamics and neural network weight pruning, **requiring causal verification**."
- Discussion: "We **attribute** the dissociation to LLM-specific cascade dynamics"
- Conclusion: "This mechanism...and **requires causal verification**."

**判定**: 充分回应。语言已从断言式改为提议式，并明确标注需要因果验证。

---

### W3: 页数 ≤ 9 pages ✅

**审稿意见**: 页数可能超 9 页导致 desk reject。

**论文现状**: ROADMAP 多次确认编译后 9 页。Director 直接编辑压缩 Discussion (7→3段)、Table 2→inline、删 Related Work neural pruning 段落。

**判定**: 充分回应。9 页零余量。

---

### W4: MiniLM metric — 区分 impact metric vs pruning metric ✅

**审稿意见**: §3.2 中 MiniLM embedding similarity 被误读为 pruning safety 的依据，需明确区分。

**论文现状** (methodology.tex §3.2):
> "Cosine similarity measures perturbation sensitivity---behavioral disruption from message removal. **This is distinct from pruning safety, which is independently evaluated via task accuracy and McNemar's exact test** (§5, Table 1). The impact gradient (§5.1) characterizes perturbation patterns; **it does not serve as the basis for pruning safety claims**."

**判定**: 充分回应。明确两句话区分 perturbation sensitivity 和 pruning safety。

---

### W5: Annotation bias direction ✅

**审稿意见**: Annotation bias 的方向（inflation vs deflation）需要明确说明。

**论文现状** (methodology.tex §3.1):
> "Annotators were not blinded to the research hypothesis; non-blinding could **inflate** ack classifications (confirmation bias), but this makes the pruning test **more conservative**---suppressing more messages while maintaining accuracy."

**判定**: 充分回应。明确了 bias 方向（inflate）及其对 pruning 实验的影响（保守化）。

---

### W6: FG cascading confounding 确认 ✅

**审稿意见**: FG pruning 的 online 结果被 cascading suppression 混淆，需明确承认。

**论文现状** (results.tex §5.2):
> "Online FG is **confounded by cascading suppression** (~90% removal)."

**判定**: 充分回应。一句明确承认 confounding。

---

### W7: Greedy decoding scope in Conclusion ⚠️

**审稿意见**: Conclusion 中需要明确 "under greedy decoding" 限定。

**论文现状** (conclusion.tex):
> "Acknowledgment pruning reduces inference calls by 36--56% with non-inferiority at δ = -3 pp (p < 0.001) and TOST equivalence at ±1 pp"

Conclusion 全文未出现 "greedy" 一词。Abstract 和 Introduction scope 段落有 "under greedy decoding" 限定，但 conclusion 作为独立阅读单元缺失此 qualifier。

**判定**: 部分回应。Conclusion 缺少 greedy decoding 限定符。

**建议**: 在 conclusion.tex 第 1 行 "reduces inference calls by 36--56%" 前加 "under greedy decoding, " 变为: "under greedy decoding, acknowledgment pruning reduces inference calls by 36--56%..."

---

## Method/Data Issues (m1-m8)

### m1: Contribution 3 → "Empirical deployment guidelines" ✅

**审稿意见**: 原 Contribution 3 表述过宽，应改为更精确的 "Empirical deployment guidelines"。

**论文现状** (introduction.tex):
> "3. **Empirical deployment guidelines** (§5.4, §5.5). Cross-generational failure (Qwen3) and domain mismatch (MATH) define applicability limits, motivating empirical screening (N ≥ 200) before deployment."

**判定**: 充分回应。

---

### m3: SafeSieve + Zhang et al. references ✅

**审稿意见**: 遗漏 SafeSieve 和 Zhang et al. 相关工作。

**论文现状**:
- related_work.tex: "SafeSieve [safesieve_2025] prunes inter-agent edges via dual-mechanism scoring (12--28% token reduction)"
- related_work.tex: "Zhang et al. [zhang_communication_strategies_2025] evaluate communication strategies...finding that acknowledgment and hints play key roles in collaborative performance."

**判定**: 充分回应。两篇均已引用并描述。

---

### m2, m4-m8: 批量修复 ✅

**审稿意见**: ROADMAP 记录为 "m2-m8: 全部批量修复"。

**判定**: 无法逐条验证（缺原始条目文本），ROADMAP 和多个 context 文件确认全部完成。

---

## Priority Fixes (P0-P5)

### P0: 三层 paradox — Introduction gap 重写 ✅

**审稿意见**: Introduction 缺乏 "three-way paradox" 结构化表述。

**论文现状** (introduction.tex §The gap):
> "Three layers of evidence point in contradictory directions: (1) information content suggests acknowledgments are dispensable; (2) individual perturbation reveals they are structurally critical (91% high disruption); (3) aggregate pruning shows they are safely removable (Δ ≈ 0 pp). No prior work has tested this three-way paradox in LLM agents..."

**判定**: 充分回应。三层 paradox 清晰呈现为编号列表。

---

### P1 → W4: MiniLM distinction ✅
见 W4。

### P2: Eq.1 a_orig/a_regen 定义 ✅

**审稿意见**: Eq.1 中变量未定义。

**论文现状** (methodology.tex §3.2):
> "where **a_orig denotes the final solver answer in the original trace** and **a_regen the answer regenerated from position i+1 after removing m_i**; e(·) denotes the sentence embedding from all-MiniLM-L6-v2"

**判定**: 充分回应。

---

### P3 → W5: Annotation bias direction ✅
见 W5。

### P4 → W6: FG confounding ✅
见 W6。

### P5 → m1: Contribution 3 reframe ✅
见 m1。

---

## 汇总

| 编号 | 问题 | 状态 | 说明 |
|------|------|------|------|
| W1 | TOST reframe ±3pp primary | ✅ | Abstract/Intro/Results/Conclusion 全部已改 |
| W2 | Cascade dissolution 降级 | ✅ | "propose" + "requiring causal verification" |
| W3 | 页数 ≤ 9 pages | ✅ | 编译确认 9 页 |
| W4 | MiniLM metric 区分 | ✅ | §3.2 两句明确区分 |
| W5 | Annotation bias direction | ✅ | §3.1 明确 inflate + conservative |
| W6 | FG cascading confounding | ✅ | §5.2 一句确认 |
| W7 | Greedy scope in Conclusion | ⚠️ | Abstract/Intro 有，**Conclusion 缺少** |
| m1 | C3 → Empirical guidelines | ✅ | Introduction C3 已改 |
| m2-m8 | 批量方法/数据修复 | ✅ | ROADMAP 确认，无法逐条验证 |
| m3 | SafeSieve + Zhang refs | ✅ | Related Work 已引用 |
| P0 | 三层 paradox | ✅ | Introduction gap 段落 |
| P1 | = W4 | ✅ | |
| P2 | Eq.1 变量定义 | ✅ | §3.2 定义完整 |
| P3 | = W5 | ✅ | |
| P4 | = W6 | ✅ | |
| P5 | = m1 | ✅ | |

**结论**: 18 项修复中 17 项充分回应，1 项部分回应 (W7)。

---

## 待修复

### W7: Conclusion 加 greedy decoding 限定

**位置**: `artifacts/paper/sections/conclusion.tex` 第 1 行

**当前**:
```
Acknowledgment pruning reduces inference calls by 36--56% with non-inferiority...
```

**建议改为**:
```
Under greedy decoding, acknowledgment pruning reduces inference calls by 36--56% with non-inferiority...
```

---

## 附注: 非 R11 但值得关注

1. **72B placeholders**: `\qwenSevenTwoB*` 宏仍为 XX.X（72B 实验尚未完成），results.tex/discussion.tex/appendix_scaling.tex 有 3 个 TODO 注释。这不是 R11 审稿修复项，但是论文完成前必须填充。
2. **CONTINGENCY-B 注释块**: results.tex 和 discussion.tex 中有注释掉的备选叙事（72B degradation 场景），需要在 72B 结果出来后清理。
