# paper fix t ablation values

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_t_ablation_values_20260517T133229_result.json`
- **Structured JSON:** [`d31bd12b2486c8ba1984.json`](../../sessions/d3/d31bd12b2486c8ba1984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。以下是所有变更清单：

| 文件 | 行号 | 旧值 | 新值 | 上下文 |
|------|------|------|------|--------|
| `appendix.tex` | 998 | `0.022` | `0.015` | T ablation 表 T=0.5 LP range |
| `appendix.tex` | 999 | `0.043` | `0.031` | T ablation 表 T=0.8 LP range |
| `appendix.tex` | 1000 | `17.6` → `0.060` | `17.8` → `0.042` | T ablation 表 T=1.0 Degen% + LP range |
| `appendix.tex` | 1001 | `0.075` | `0.058` | T ablation 表 T=1.2 LP range |
| `appendix.tex` | 984 | `from 0.022 to 0.075` | `from 0.015 to 0.058` | 正文描述 LP range 范围 |

**未修改的同值出现**（确认为非 T ablation 上下文）：
- `appendix.tex:76` — FK NER ρ drops by 0.022（ρ 差值）
- `appendix.tex:288` — VC Δρ=0.022（统计检验）
- `appendix.tex:387,617` — ρ=0.297±0.022（多 seed 标准差）
- `discussion.tex:108,121` — 引用 tab:t_degeneracy 但未引用 LP range 数值

---
