# paper d111 sf3 sf4 consistency fixes

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d111_sf3_sf4_consistency_fixes_20260521T075301_result.json`
- **Structured JSON:** [`7c91cc288f1960b1991d.json`](../../sessions/7c/7c91cc288f1960b1991d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

主文 8 页（bibliography 从第 9 页开始），符合限制。

---

## 汇报

| # | 修改 | 文件 | 行号 | 状态 |
|---|------|------|------|------|
| SF-3 | information density 工作定义 | method.tex | L37-38（新插入） | ✓ |
| SF-3 dup | 删除 experiments.tex 重复定义 | experiments.tex | 原 L123（已删除） | ✓ |
| SF-4 | 标题降级 | experiments.tex | L183 | ✓ |
| 3a | two-tier hierarchy → consistent two-tier pattern | experiments.tex | L68 | ✓ |
| 3b | Regex (best) → Regex ($B_{\text{marker}}$) + footnote | experiments.tex | L88 + L95 | ✓ ⚠️ |
| 3c | 76--82% 添加 §ref 来源 | introduction.tex | L14 | ✓ |

**PDF**: `481aca6ea5b61f56b64c4ebec4613de3`, 21 页（主文 8 页 + refs + appendix），0 warnings，0 undefined references。

**⚠️ 3b 数据一致性问题**：表中 93.61% 对应 B4（exception type regex matching），而非 B5（marker detection，实际 99.33%）。脚注说 "$B_{\text{marker}}$ detects the absence marker"，描述的是 B5 行为，但数据是 B4 的。这会与 §4.4 nomarker 段落（"regex baseline B5 exploits this for 99.33%"）矛盾。建议改为 `Regex ($B_4$)` 并调整脚注为 "B4 matches exception class names; see Appendix for all regex baselines"，或将行数据改为 B5 的 99.33%。

---
