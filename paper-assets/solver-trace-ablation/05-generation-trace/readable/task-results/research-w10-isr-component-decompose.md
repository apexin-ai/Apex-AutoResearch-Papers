# research w10 isr component decompose

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_w10-isr-component-decompose_20260518T084729_result.json`
- **Structured JSON:** [`ebe68a2b490221d89b77.json`](../../sessions/eb/ebe68a2b490221d89b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data. Here's the complete report.

---

```
=== 代码实际行为 ===
decompose_fol 输入: (premises: list[str], conclusion: str)
decompose_fol 输出: list[FOLComponent]

分解逻辑:
  1. 每个 premise → FOLComponent(type="premise")
  2. Conclusion 进一步分解:
     a. 循环剥离外层量词 → FOLComponent(type="conclusion_quantifier")
        ⚠️ 量词 regex 只匹配 ∀/forall/∃/exists，不匹配 Prover9 的 "all"/"exist"
     b. 尝试 top-level 蕴含分割 →
        - FOLComponent(type="conclusion_antecedent")
        - FOLComponent(type="conclusion_consequent")
     c. 若无蕴含结构 → FOLComponent(type="conclusion_whole")

消融逻辑 (ablation.py):
  - premise: 移除该 premise，re-prove
  - conclusion_quantifier: 从 conclusion 字符串删除量词文本
  - conclusion_antecedent: str.replace(content, "$T", 1)
  - conclusion_consequent: str.replace(content, "$F", 1)  ← 存在 bug
  - conclusion_whole: 用 "$T" 替换整个 conclusion

=== P→P tautology 实测 ===

Case 1: all x (P(x) -> P(x)) [Prover9 原生格式]
  n = 2
  components:
    [0] type=premise, content="all x (P(x) -> P(x))" → necessary=False (tautology, no-premise 仍可证)
    [1] type=conclusion_whole, content="all x (P(x) -> P(x))" → necessary=False (替换为 $T 总能证)
  ISR = 0/2 = 0.0

Case 2: P(x) -> P(x) [无量词]
  n = 3
  components:
    [0] type=premise, content="P(x) -> P(x)" → necessary=False
    [1] type=conclusion_antecedent, content="P(x)" → necessary=True (替换为 $T→P(x)≡P(x), 无法证)
    [2] type=conclusion_consequent, content="P(x)" → necessary=False ← BUG: str.replace 替换了第一次出现(antecedent)而非 consequent
  ISR = 1/3 = 0.333

Case 3: ∀x (P(x) -> P(x)) [Unicode 量词，触发 regex]
  n = 4
  components:
    [0] type=premise → necessary=False
    [1] type=conclusion_quantifier, content="∀x" → necessary=False
    [2] type=conclusion_antecedent, content="P(x)" → necessary=True
    [3] type=conclusion_consequent, content="P(x)" → necessary=False ← 同样的 str.replace bug
  ISR = 1/4 = 0.25

真实 H7 样本 (eval 数据, 100 个 H7):
  - 93 个 ISR=0.5 (原子结论, n=2)
  - 7 个 ISR=1.0 (非重言蕴含结论, ante≠cons, n=3)
  - 0 个 ISR=0.75

=== 论文描述 ===

method.tex L25 当前措辞:
  "What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog."
  → 说 FOL 的 component 是 premises，但代码还分解了 conclusion

ISR=0.75 出现位置 (5 处):
  - experiments.tex:48 "tautological proofs (P→P) receive ISR=0.75"
  - experiments.tex:86 "H7 tautologies receive expected reward 1+0.75β"
  - appendix.tex:153 "tautological proofs (P→P) receive ISR=0.75"
  - appendix.tex:179 "P→P yields ISR=0.75"
  - related_work.tex:22 "P→P receives ISR=0.75 by construction"

论文内部自相矛盾:
  - method.tex:56 说 "H7 tautologies achieve ISR≥0.5 by construction"
  - 其他 4 处说 ISR=0.75

与代码行为的差异:
  1. ISR=0.75 在代码中不可复现。实测 P→P 得到 0.0 / 0.333 / 0.25（取决于格式）
  2. 真实 H7 eval 数据中无任何 ISR=0.75 样本
  3. 论文说 components = "premises in FOL"，代码实际还分解 conclusion

=== 发现的两个代码 Bug ===

Bug 1: 量词 regex 缺失 Prover9 关键字
  文件: src/sta/components.py _strip_outer_quantifier
  Regex: r'^((?:∀|forall|∃|exists)\s*[A-Za-z_]\w*)\s*\(\s*'
  缺少 "all" 和 "exist"（Prover9 关键字）
  影响: Prover9 格式的量化公式永远不产生 conclusion_quantifier 组件

Bug 2: str.replace 在 antecedent=consequent 时替换错误
  文件: src/sta/ablation.py _ablate_conclusion_part
  consequent 消融用 conclusion.replace(content, "$F", 1)
  当 antecedent 和 consequent 文本相同时（如 P→P），替换的是第一个出现位置（即 antecedent），而非 consequent
  影响: P→P 的 consequent 消融结果为 "$F→P" (恒真) 而非 "P→$F" (应为恒假)

=== 建议修正 ===

1. 论文: 将所有 "ISR=0.75" 改为 "ISR≥0.5"（与 method.tex 一致，且有 eval 数据支持）
   或者: 如果希望保留精确值，用 "ISR=0.5 for atomic conclusions, ISR=1.0 for non-tautological implications"

2. 论文 method.tex L25: "premises in FOL" → "premises and conclusion sub-parts in FOL"
   （与代码行为一致）

3. 代码 Bug 1: regex 添加 "all" 和 "exist":
   r'^((?:∀|forall|all|∃|exists|exist)\s*[A-Za-z_]\w*)\s*\(\s*'

4. 代码 Bug 2: 用位置信息替换而非 str.replace
   对 consequent 消融，应该替换最后一次出现或用 offset 定位
```

---
