# analysis degeneracy definition audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_degeneracy_definition_audit_20260517T075532_result.json`
- **Structured JSON:** [`c2c84394130974307c6d.json`](../../sessions/c2/c2c84394130974307c6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手，可以写最终报告了。

---

## Degeneracy Definition Audit — 最终报告

### 1. Paper 定义 (discussion.tex)

> "Constant F1": all N samples receive identical instance-level F1.

使用 `entity_strict_match` 匹配 `(start, end, type)` 计算 F1。对 **ALL 实例**（含 gold-empty）计算。gold-empty 实例因为所有 sample 的 F1 恒为 0.0，属于 trivially degenerate。

### 2. 各脚本定义差异

| 脚本 | 定义 | 过滤 | 数据量 |
|------|------|------|--------|
| **论文 Table** | Constant F1 | **不过滤** gold-empty | 全量 |
| `analyze_exp023_rank8_full.py` | Constant F1 (round 6位) | **不过滤** | 全量 |
| `analyze_fewnerd_results.py` | KeySet `(text, type)` 全同 | **过滤** gold-empty | 全量 |
| `analyze_per_type_lp.py` | KeySet `(text, type)` 全同 | **过滤** gold-empty | 全量 |
| `analyze_lp_compression.py` (W2) | KeySet `(text, type, start, end)` 全同 | **不过滤** | **max 5000** (Few-NERD) |

### 3. 差异根因

**三个独立因素叠加**:

**(a) 定义差异 (最主要)**:
- Constant F1 最宽松：不同 entity set 可以产生相同 F1 → 更高 degeneracy
- KeySet(text,type) 中等：要求所有 sample 的实体集合完全相同
- KeySet(text,type,start,end) 最严格：还要求位置完全一致

逻辑关系：KeySet identical ⊂ Constant F1。所以 KeySet degeneracy ≤ Constant F1 degeneracy。

**(b) Gold-empty 过滤**:
- 不过滤：gold-empty 实例全部算 degenerate（F1 恒 =0），推高比率
- 过滤后：denominator 变小，但 degenerate 实例也全部移除，降低比率
- Few-NERD 有 13.5% gold-empty（5083/37648），影响显著

**(c) 数据子集**: Few-NERD W2 只取前 5000/37648。

### 4. 统一重算结果 (使用官方 `per_instance_f1`)

```
                                 Constant F1    Constant F1    KeySet(t,T)    KeySet(t,T,s,e)
Dataset                          (all data)     (gold-filt)    (gold-filt)    (all data)
─────────────────────────────────────────────────────────────────────────────────────────
SciERC full-rank (exp_012, N=8)    21.1%          17.8%          11.3%          11.6%
SciERC rank=8   (exp_023, N=8)     10.9%           7.2%           2.6%           3.3%
Few-NERD N=8 first-5k (exp_021)    25.1%          13.7%          10.0%          19.0%
Few-NERD N=8 ALL-37k  (exp_021)    25.4%          13.8%          10.1%          19.3%
Few-NERD N=16         (exp_027)    19.1%           7.1%           4.5%          13.2%
CoNLL N=16            (exp_002)    58.0%          47.4%          45.5%          49.4%
```

### 5. 各来源数值追溯

| 被报告的值 | 实际对应 | 列 |
|-----------|---------|-----|
| 论文 SciERC 21% | Constant F1, all data | ✅ 21.1% |
| 论文 CoNLL 58% | Constant F1, all data | ✅ 58.0% |
| 论文文本 Few-NERD 10% | **KeySet(t,T), gold-filtered** | 10.1% ← **不是 Constant F1** |
| Registry SciERC rank=8 7.2% | Constant F1, **gold-filtered** | 7.2% ← **过滤了 gold-empty** |
| W2 SciERC full-rank 11.6% | KeySet(t,T,s,e), all data | 11.6% |
| W2 SciERC rank=8 3.3% | KeySet(t,T,s,e), all data | 3.3% |
| W2 Few-NERD 19% | KeySet(t,T,s,e), all data, first-5k | 19.0% |

### 6. 论文中哪些数字正确？

- **SciERC 21%, CoNLL 58%**: 正确，Constant F1 on all data。
- **Few-NERD "10%"**: **定义不一致**。论文 Table 用 "Constant F1"，但文本中 Few-NERD 的 10% 来自 `analyze_fewnerd_results.py` 的 KeySet(text,type) + gold-filtered。如果统一用论文 Table 的定义 (Constant F1, all data)，Few-NERD N=8 应为 **25.4%**，gold-filtered 也有 **13.8%**。
- **SciERC rank=8 "7.2%"**: 用了 Constant F1 但 **过滤了 gold-empty**。不过滤应为 10.9%。

### 7. W2 worker 数值对其结论的影响

W2 的 LP compression 分析关注的是 logprob range 和 within-instance ρ(LP, F1)，degeneracy 只是附带报告的诊断指标。W2 使用最严格的 KeySet 定义（含位置），所以：
- SciERC 11.6% vs 论文 21%：低估了 degeneracy，但 W2 的 LP correlation 分析仅在 non-degenerate 实例上进行，实际过滤集更大（论文定义下的 degenerate 更多），W2 的 ρ 值可能略偏高（因为混入了一些 "F1 constant 但 key_set 不同" 的实例）
- Few-NERD 19% vs 论文定义 25.4%：同理
- W2 的核心结论（LP range 窄、within-instance ρ 低）不受 degeneracy 定义影响，因为这些是连续值分析

**建议**：论文应统一使用 Constant F1 (all data) 作为所有数据集的 degeneracy 定义，或者在文本中明确 Few-NERD 的 10% 用的是不同定义。

---
