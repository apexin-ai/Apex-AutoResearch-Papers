# verify multi nli d061

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_multi-nli-d061_20260522T213004_result.json`
- **Structured JSON:** [`993aeaf7d0d9020a1c1b.json`](../../sessions/99/993aeaf7d0d9020a1c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the verification report.

## Multi-NLI D061 验证结果

### 数据源确认
`r11_3verifier_canonical.json` 使用 **alphabetical tiebreaking (D061)**，脚本中所有 `sc_answer_alpha()` 和 `combo_answer_alpha()` 函数均通过 `sorted(tied)[0]` 实现。

SC baseline (D061): **39.33%** (236/600)

---

### tab:multi-nli (appendix L892–908)

**Caption 问题**: 写的 `SC = 39.17%`，应为 **39.33%** ❌

| Verifier | w | 论文 Δ | D061 combo | D061 Δ | 匹配？ |
|----------|---|--------|-----------|--------|--------|
| DeBERTa | 1 | +1.17 | 40.17% (241) | **+0.83** | ❌ |
| DeBERTa | 3 | +7.00 | 46.00% (276) | **+6.67** | ❌ |
| DeBERTa | 5 | +11.17 | 50.33% (302) | **+11.00** | ❌ |
| RoBERTa | 1 | −0.17 | 39.17% (235) | −0.17 | ✅ |
| RoBERTa | 3 | +4.17 | 43.50% (261) | +4.17 | ✅ |
| RoBERTa | 5 | +4.33 | 43.67% (262) | +4.33 | ✅ |
| BART | 1 | 0.00 | 39.33% (236) | 0.00 | ✅ |
| BART | 3 | +5.17 | 44.50% (267) | +5.17 | ✅ |
| BART | 5 | +6.33 | 45.67% (274) | +6.33 | ✅ |

**RoBERTa 和 BART combo 值均正确**，与 D061 完全一致。仅 DeBERTa 三行需更新（之前 DRC 审计已发现）。所有 p 值也匹配。

---

### 额外发现：表间不一致

**tab:cil_empirical (L226)** DeBERTa Δ 已更新为 **+6.67**（D061 正确值），但 **tab:multi-nli (L899)** 同一 w=3 仍写 **+7.00**。两表之间存在矛盾。

**tab:nli-combo-full (L965–968)** 也未更新——Mistral-7B DeBERTa 行：
- SC baseline: 39.17% → 应为 39.33%
- w=1 combo: 40.33% → 应为 40.17%, Δ: +1.17 → +0.83
- w=3 combo: 46.17% → 应为 46.00%, Δ: +7.00 → +6.67
- w=5 combo: 50.33% ✅, Δ: +11.17 → +11.00

---

### 需修改汇总

1. **tab:multi-nli caption**: SC 39.17% → 39.33%
2. **tab:multi-nli DeBERTa 三行 Δ**: +1.17→+0.83, +7.00→+6.67, +11.17→+11.00
3. **tab:nli-combo-full**: SC baseline、DeBERTa combo 绝对值和 Δ 同步更新
4. RoBERTa 和 BART — **无需修改**

---
