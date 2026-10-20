# analysis plan002 b01 s42 h7 audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-b01-s42-h7-audit_20260514T150601_result.json`
- **Structured JSON:** [`63fb8f3bf901239c3ef1.json`](../../sessions/63/63fb8f3bf901239c3ef1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。完整报告如下：

---

## plan002-b01-s42 H7 逐样本审查结果

**81 proved / 100 total**

### 分类统计

| 类别 | Count | Rate | Mean ISR | Median ISR |
|------|-------|------|----------|------------|
| **H7** (单 premise = conclusion) | 13 | 16.0% | 0.6603 | 0.7500 |
| **H1** (多 premise 含 conclusion) | 42 | 51.9% | 0.2245 | 0.1667 |
| **Genuine** (无 conclusion 重复) | 26 | 32.1% | 0.6014 | 0.5500 |

**Combined conclusion duplication: 55/81 = 67.9%**

### 典型 H7 样本（单 premise = conclusion, ISR 膨胀）

1. **folio_556** (ISR=0.75): Premise `∀x (AssessesSAT(x) → MathSkills(x))` = Conclusion — 直接自证
2. **folio_160** (ISR=0.75): Premise `∀x (IsBatteryTower(x) → ∀y (...))` = Conclusion
3. **folio_304** (ISR=0.33): Premise `∀x (¬Braz(x) ∨ ¬PlaysForNautico(x))` = Conclusion

### 典型 H1 样本（多 premise 含 conclusion, ISR 被压低）

1. **folio_66** (ISR=0.14): 6 premises 中 `W(c) ∧ H(c)` 直接等于 conclusion，其余 5 个 unnecessary
2. **folio_1378** (ISR=0.10): 9 premises 中 `IsPRCNational(Mei)` = conclusion，ISR 极低
3. **folio_1119** (ISR=0.60): 2 premises 中包含 conclusion 的量化公式

### 典型 Genuine 样本（真正推理）

1. **folio_765** (ISR=0.33): 5 premises → `¬(Lawyer(Mary) ∨ TippedEmployee(Mary)) ∧ Advocate(Mary)` — conclusion 是新合取式，非任一 premise 的复制
2. **folio_592** (ISR=0.60): 2 premises → 合取式 conclusion
3. **folio_71** (ISR=0.50): 5 premises → `¬(Easy(2Sum) ∨ Hard(2Sum))` — 需要实质推理得出矛盾

### 对论文的影响

**Critical for Claim 2.** plan002-b01-s42 是 ISR β=0.1 "genuine structural guidance" 的核心证据，但：
- 67.9% proved 样本有 conclusion duplication（H7+H1）
- H7 膨胀 ISR（mean 0.66），H1 压低 ISR（mean 0.22），两种 artifact 方向相反
- Genuine 子集仅 26 样本，其 mean ISR = 0.60 反而高于整体 0.42
- 论文 reported ISR 是三类样本的混合平均，信号被 artifact 主导

---
