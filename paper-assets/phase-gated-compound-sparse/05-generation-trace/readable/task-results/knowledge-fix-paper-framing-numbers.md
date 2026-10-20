# knowledge fix paper framing numbers

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_fix_paper_framing_numbers_20260516T015219_result.json`
- **Structured JSON:** [`501652842b714e1a9ba1.json`](../../sessions/50/501652842b714e1a9ba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修正清单

| # | 位置 | 旧值 | 新值 | 原因 |
|---|------|------|------|------|
| 1 | Core Insight: DS dose curve | `0.32→1.15→3.97→9.94` | `0.32→1.13→3.96→9.97` | Registry 0.316→1.128→3.955→9.973，旧值非标准四舍五入(1.15≠round(1.128), 9.94≠round(9.973)) |
| 2 | Core Insight: imp/rand ratio | `3-15×差异` | `2.7-15×差异` | n=500 QW s025 imp/rand=2.7×，低于旧下界3 |
| 3 | Core Insight: QW Cohen's d | `Qwen: 0.28→1.02` | `Qwen: 0.37→1.02` | Registry cohens_d=0.3705；旧值0.28是unpaired d，统一为paired d_z |
| 4 | Narrative Arc: DS short form | `0.32→9.94` | `0.32→9.97` | 同 #1 |
| 5 | Narrative Arc: imp/rand ratio | `(3-15×)` | `(2.7-15×)` | 同 #2 |
| 6 | Framing 硬约束: magnitude | `importance 3-15× larger` | `importance 2.7-15× larger` | 同 #2 |
| 7 | C2 Evidence: DS dose curve | `0.32→1.15→3.97→9.94` | `0.32→1.13→3.96→9.97` | 同 #1 |
| 8 | S3→C Evidence: QW d naming | `d=0.28` | `d_z=0.37` | 同 #3，统一命名为d_z |
| 9 | RC4: QW Cohen's d | `Qwen 0.28→1.02` | `Qwen 0.37→1.02` | 同 #3 |
| 10 | Paper Positioning: DS short form | `0.32→9.94` | `0.32→9.97` | 同 #1 |

**未修改项**：QW accuracy 值（dense 0.46, s015 0.42 等）在 paper_framing.md 中未被引用，无需修改。

---
