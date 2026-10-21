# paper table2 llama fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table2_llama_fix_20260520T111247_result.json`
- **Structured JSON:** [`4921f36f21a1b4332e6c.json`](../../sessions/49/4921f36f21a1b4332e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Table 2 验证通过，与 eval 结果完全一致：

| | E-F1 | R-F1 | DR% | CF% |
|---|------|------|-----|-----|
| Qwen unc | 82.15 | 40.86 | 0.76 | 0.09 |
| Qwen con | 81.43 | 40.56 | 0.01 | 0.27 |
| Llama unc | 83.93 | 43.72 | 0.49 | 0.08 |
| Llama con | 83.94 | 43.78 | 0.21 | 0.21 |

## 修改汇总

### Table 2 (section5_scierc_draft.tex:139-140)
| 位置 | 旧值 | 新值 |
|------|------|------|
| Llama unc CF | `---` | `0.08` |
| Llama con DR | `0.20` | `0.21` |
| Llama con CF | `0.26` | `0.21` |
| Llama con R-F1 | `44.23` | `43.78` |
| Llama con ΔDR | `59%` | `57%` |

### 正文连带修改 (section5_scierc_draft.tex)
- L105: DR `0.20→0.21`, ΔDR `59%→57%`, R-F1变化 `+0.51pp→+0.06pp`
- L106: `59%→57%`
- L107, L109, L144: `DR≤0.20%→DR≤0.21%`

### Appendix 连带修改 (appendix_discussion.tex)
- L259: Llama DocRED unc CF `---→0.08`
- L262: DR `0.20→0.21`, CF `0.26→0.21`, R-F1 `44.23→43.78`
- L275: `DR≤0.20%→DR≤0.21%`
- L329: post-hoc表 R-F1_cd `44.23→43.78`

### 其他文件连带修改
- section5_docred_draft.tex L71: `0.01--0.20%→0.01--0.21%`
- section4_composition_draft.tex L31, L40: `0.20%→0.21%`
- main.tex L81: `DR≤0.20%→DR≤0.21%`
- section7_conclusion_compressed.tex L4: `DR≤0.20%→DR≤0.21%`

### 未修改（非 Llama DocRED con 数据）
- appendix_beam_search.tex L135 `R-F1=44.23` — Qwen SciERC beam 结果
- appendix_beam_search.tex L161 `CF=0.26` — d065 4096-context 独立实验
- appendix_tcr.tex L63 `0.21/0.20` — TCR 独立指标

编译通过，31 pages，0 errors。

---
