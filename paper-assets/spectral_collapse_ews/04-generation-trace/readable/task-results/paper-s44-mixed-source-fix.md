# paper s44 mixed source fix

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_s44-mixed-source-fix_20260522T063940_result.json`
- **Structured JSON:** [`b89ab897987df3dbea39.json`](../../sessions/b8/b89ab897987df3dbea39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，12 页（含 appendix/references，正文 ≤8 页）。

**验证汇总：**

| 位置 | "4.6" / "2362" 出现 | 状态 |
|------|---------------------|------|
| L142 `$-4.6$` dip | 已标注 `seed~42, representative trajectory` | ✓ |
| L142 `$2362.1$` | 同上句，已覆盖 | ✓ |
| L142 `$2488.1$` 终值 | 已标注 `three-seed mean` | ✓ |
| L158 `$-4.6$` 引用 | 已标注 `seed~42` | ✓ |
| L137 `$2362.7$` (r=0.2 EMA) | 不同数据点，无需改 | — |
| L180 Table 3 `2488.1` | 已是 3-seed mean，无需改 | — |
| L32/L61 `874.6` | 不相关（σ₁ 值） | — |

---
