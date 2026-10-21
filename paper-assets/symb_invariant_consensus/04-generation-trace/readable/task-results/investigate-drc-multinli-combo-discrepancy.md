# investigate drc multinli combo discrepancy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_drc-multinli-combo-discrepancy_20260522T220755_result.json`
- **Structured JSON:** [`bf888678b1b02d21946e.json`](../../sessions/bf/bf888678b1b02d21946e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整报告。

---

## 调查报告：DRC 表与 multi-NLI 表精度不一致

### 数据源

| 来源 | SC baseline | DeBERTa w=3 combo | delta |
|------|------------|-------------------|-------|
| **r11_3verifier_canonical.json**（权威） | 39.33% (236/600) | 46.00% (276/600) | +6.67pp |
| **主表** (experiments.tex L31) | 39.33% | — | — |
| **DRC 表** (appendix.tex L875-877) | 39.17% | 46.00% (Full combo) | — |
| **multi-NLI 表** (appendix.tex L899) | 39.17% | 46.17%（隐含） | +7.00pp |
| **full NLI combo 表** (appendix.tex L967) | 39.17% | 46.17%（显式） | +7.00pp |

### 根因

**ID_FIX 修复前后的数据差异。**

`r11_3verifier_final_v2.py` / `r11_3verifier_canonical.py` 包含一个 ID 修复：

```python
ID_FIX = {
    "ProofWriter_AttNeg-OWA-D5-1176_Q4": "ProofWriter_AttNeg-OWA-D5-1176_Q8",
    "ProofWriter_AttNoneg-OWA-D5-1284_Q4": "ProofWriter_AttNoneg-OWA-D5-1284_Q8",
}
```

这修正了 SC votes 文件中两个问题 ID 的错配。脚本明确断言 `assert sc_n == 236`。

**appendix 的三个表（DRC、multi-NLI、full NLI combo）使用了 ID_FIX 之前的旧数据（SC=235=39.17%，DeBERTa w3 combo=277=46.17%）。**

主表 (experiments.tex) 已经使用了修正后的 SC=39.33%。

### 矛盾细节

**Multi-NLI 表内部自相矛盾**：
- Caption 声称 SC=39.17%，但 RoBERTa/BART 的 delta 值和 canonical JSON（SC=39.33%）完全一致
- 只有 DeBERTa 的 delta 不一致（来自旧计算）
- 说明表格是混合了新旧两个数据源

**DRC 表 vs multi-NLI 表**：
- DRC Full combo = 46.00%（276 correct，与 canonical JSON 一致）
- multi-NLI DeBERTa w3 隐含 combo = 46.17%（277 correct，旧数据）
- 差 1 题，因为 DRC 表的 Full combo 恰好用了正确值

### 需要修改的位置

全部改为 canonical JSON 的权威值 (SC=39.33%, DeBERTa w3 combo=276=46.00%):

1. **appendix.tex L875**: SC `39.17%` → `39.33%`
2. **appendix.tex L892** (multi-NLI caption): SC `39.17%` → `39.33%`
3. **appendix.tex L898-900** (DeBERTa deltas): `+1.17` → `+0.83`, `+7.00` → `+6.67`, `+11.17` → `+11.00`
4. **appendix.tex L965**: SC `39.17%` → `39.33%`, gap `+15.83` → `+15.67`
5. **appendix.tex L966**: combo `40.33` → `40.17`, delta `+1.17` → `+0.83`, p_raw 需验证
6. **appendix.tex L967**: combo `46.17` → `46.00`, delta `+7.00` → `+6.67`, p_raw `5.0×10⁻⁶` → `1.13×10⁻⁵`
7. **appendix.tex L968**: delta `+11.17` → `+11.00`, p_raw `6.2×10⁻⁷` → 需验证（canonical=6.18×10⁻⁷，可能只是四舍五入）
8. **appendix.tex L948**: prose 中 SC `39.17%` → `39.33%`
9. **appendix.tex L1001**: fine-tuned table SC `39.17%` → `39.33%`（delta 也需验证）
10. **solutions.tex L9**: SC `39.17%` → `39.33%`
11. **solutions.tex L12**: SC `39.17%` → `39.33%`
12. **solutions.tex L23**: SC `39.17%` → `39.33%`, gap `+15.83` → `+15.67`, delta `+7.00` → `+6.67`
13. **figures/gen_capability_gap_scatter.py**: 散点图数据中所有基于 39.17 的计算

### 建议

1. **立即修复**：将上述 SC=39.17% 全部改为 39.33%，DeBERTa delta 改为 canonical JSON 值
2. **DRC τ=0.7 行**（L876: 45.33%）：可能不受影响（DRC routing 使用 raw vote agreement，与 tiebreaking 无关），但建议用 canonical 数据重新验证
3. **Fine-tuned NLI 表**（L1001-1004）：SC 改为 39.33%，delta 需要确认是否也受 ID_FIX 影响
4. **Recovery 计算**：DRC Recovery = (45.33−39.33)/(46.00−39.33) = 6.00/6.67 = 89.96% ≈ 90.0%，不变

---
