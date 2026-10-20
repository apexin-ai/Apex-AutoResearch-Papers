# writing r16 paper text fixes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r16_paper_text_fixes_20260521T033136_result.json`
- **Structured JSON:** [`46fe4748351229336897.json`](../../sessions/46/46fe4748351229336897.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改总结

### 已修改的文件和变更

| 文件 | 变更 | Action |
|---|---|---|
| `abstract.tex` | "enabling dependency" → "empirical enabling dependency" | M1 |
| `section1_introduction_draft.tex` | "enabling dependency" → "empirical enabling dependency"; 加 Mistral 排除原因 "due to atypical entity typing interaction" | M1, M3 |
| `section3_method_draft.tex` | Corollary 内 "enabling dependency" → "empirical enabling dependency"(2处); DFA 示例改为 DocRED (7 entity types, >10^17 states)，补充 O(|E|^|entities|) 复杂度说明 | M1, W6 |
| `section4_composition_draft.tex` | WikiEvents κ̄=0.029 后加 "(27 entity types, 56 event types, mean 21 valid type pairs per event type out of 27²=729 possible)"; "enabling dependency" → "empirical enabling dependency" | W1, M1 |
| `section5_docred_draft.tex` | Zero-shot diagnostic 段末加 residual DR fallback 解释（1.4--5.7% fallback rate, causal tracing 证实）; "enabling dependency" → "empirical enabling dependency" | W2, M1 |
| `section5_scierc_draft.tex` | "enabling dependency" → "empirical enabling dependency" | M1 |
| `section5_runtime.tex` | 70B CF 分析扩展：CF 5.15--7.01% 与 8B ZS (2.57--9.90%) 对比，归因 zero-shot 不确定性而非模型规模，INT4 可能加剧，FT 是关键缓解手段 | W4 |
| `appendix_related_work.tex` | "enabling dependency" → "empirical enabling dependency" | M1 |
| `appendix_discussion.tex` | "enabling dependency" → "empirical enabling dependency" | M1 |

### 各 Action Item 状态

| Item | 状态 | 说明 |
|---|---|---|
| MF2 | done | 已有 92--100%，无需修改 |
| MF3 | done | 已有 0--21.1% ZS, ≤1.3% FT，无需修改 |
| W1 | done | §4 加入 WikiEvents 约束密度数据 |
| W2 | done | §5 DocRED 加入 ZS residual DR fallback 归因 |
| W3 | done | 已有 "initial evidence for applicability" 和 "preliminary" |
| W4 | done | 70B 段落加入 CF 跨规模对比分析 |
| W5 | done | 已有 "formalize a well-known intuition" |
| W6 | done | §3 DFA 状态数改引 DocRED，补充复杂度公式 |
| M1 | done | 全文 9 处 "enabling dependency" 加 "empirical" |
| M3 | done | §1 加 Mistral 排除原因 |

### 一致性确认

- Abstract / §1 / §5 DR 范围一致：92--100% FT, 45--99% ZS
- CF 范围一致：≤1.3% FT, 0--21.1% ZS
- DR ≤ 0.09%、R-F1 ±0.6pp 全文统一
- "empirical enabling dependency" 术语统一

---
