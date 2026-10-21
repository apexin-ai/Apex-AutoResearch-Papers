# paper reframe b1b2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reframe_b1b2_20260522T071201_result.json`
- **Structured JSON:** [`90fad29219c1ee95f016.json`](../../sessions/90/90fad29219c1ee95f016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，页面合规。以下是修改摘要：

### Diff 摘要

**abstract.tex** — +2 sentences (替换最后 1 sentence)
- 新增 benign distribution shift 描述（WildChat FPR 68.1%, 10-shot → 0%）
- 结尾句从 "optimization regularization, not semantic learning" 重写为两轴分解框架总结，含 24.3× speedup

**introduction.tex L20 段** — 两轴框架替换单轴描述
- "shows that classification-based adaptation is the most robust variant" → 分解为 *attack side*（vanilla 0.28–0.31 → DAPT 0.97–1.0）和 *benign side*（WildChat FPR 68.1% → 10-shot 消除）
- 保留 RoBERTa-large 和 variance 观察不变

**introduction.tex Contributions** — 3 点全部重写
- C1: "Systematic decomposition" + old "Architecture/scale" → **Two-axis generalization decomposition**（attack-side + benign-side）
- C2: old C3 mechanistic interpretation → **Condition-dependent effectiveness + constraining negative results**（MLM collapse, 3 negative results）
- C3: 新增 **Practical deployment recipe**（24.3× + 10-shot, no target-domain attack data）

**conclusion.tex Discussion** — 段落标题 + 内容升级
- "Benign distribution as the remaining bottleneck" → **"Two-axis generalization: attack-side vs. benign-side"**
- 新增开头句明确 OOD F1 = attack-side under IID benign，结尾从 "confirming benign mismatch as primary bottleneck" → "the two axes are orthogonal and independently addressable"

**conclusion.tex Conclusion** — 两轴结构同步
- 开头从 "On synthetic multi-turn evaluations" → "Controlled ablation decomposes ... into two orthogonal axes"
- 新增 benign-side 句（10-shot, FPR 68.1%→0%）
- 结尾从 "offering a practical alternative given matched benign distributions" → "two-axis decomposition yields a practical deployment recipe that requires no target-domain attack data"

### 编译验证
- Discussion: page 8
- Conclusion: page 8
- Limitations: page 9

---
