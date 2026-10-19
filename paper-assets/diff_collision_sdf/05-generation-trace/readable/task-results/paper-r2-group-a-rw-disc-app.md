# paper r2 group a rw disc app

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r2-group-a-rw-disc-app_20260528T065004_result.json`
- **Structured JSON:** [`bc1279f68bbccf3fbac7.json`](../../sessions/bc/bc1279f68bbccf3fbac7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。汇总：

### P0 #1: SafeVLA 分类事实性错误
- **related_work.tex L12**: "Constraint-based planning" → "Constrained optimization"；SafeVLA 描述改为 CMDP + Lagrangian optimization 范式；结尾句从 "bypass" 改为区分 constrained optimization vs runtime filtering 两种不同机制
- **discussion.tex L6**: "constraint-based and runtime filtering approaches bypass..." → 分别描述 SafeVLA（CMDP 约束违规概率）和 runtime filtering（跳过训练）

### P1 #3: "redundant" 5 处分层处理
1. **related_work.tex L12**: → "redundant at the tested scale" ✓
2. **discussion.tex L20**: → "redundant at the tested scale" ✓
3. **discussion.tex L11**: "SDF redundancy finding" → "finding that EE-only SDF shows no significant benefit" ✓
4. **appendix.tex L229**: → "absence of EE-only SDF benefit" ✓
5. **appendix.tex L235**: → "absence of SDF benefit" ✓

### P1 #4: Discussion 首句 scope
- **discussion.tex L3**: → "CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable" ✓

### P1 #10a/b: 补充引用
- **related_work.tex L15**: 评估段落加入 HazardArena（语义安全 twin scenarios）和 VLA-Risk（物理鲁棒性 benchmark）
- **references.bib**: 新增 `chen2026hazardarena` 和 `vlariskanon2026` 条目

### P2 #8: "20×" 替换
- **discussion.tex L6**: "20$\times$ the lowest tested weight" → "spanning an order of magnitude above the lowest tested weight" ✓
- **appendix.tex L181**: 无 "20×" 倍数声明（该行 "20" 是排列组合数 $\binom{6}{3}=20$），无需修改

---
