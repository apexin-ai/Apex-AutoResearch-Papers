# analysis boolq confidence margin

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_boolq-confidence-margin_20260520T144742_result.json`
- **Structured JSON:** [`33e5376bd68415a3ca50.json`](../../sessions/33/33e5376bd68415a3ca50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总表：

### Control 1: hurt vs stayed-right (within pure-correct)

| Arch | n(hurt) | n(SR) | hurt_mean | SR_mean | Cohen's d | p | hypothesis |
|------|---------|-------|-----------|---------|-----------|---|------------|
| GDN | 441 | 1471 | 3.003 | 2.979 | 0.041 | 0.461 | supported (n.s.) |
| RetNet | 648 | 1351 | 3.084 | 3.080 | 0.006 | 0.956 | supported (n.s.) |
| HGRN2 | 488 | 1388 | 2.988 | 3.061 | −0.098 | 0.154 | **not supported** |

### Control 2: helped vs stayed-wrong (within pure-wrong)

| Arch | n(helped) | n(SW) | helped_mean | SW_mean | Cohen's d | p | hypothesis |
|------|-----------|-------|-------------|---------|-----------|---|------------|
| GDN | 605 | 753 | 3.505 | 3.732 | −0.357 | **1.68e-10** | **supported** |
| RetNet | 550 | 721 | 3.592 | 3.696 | −0.158 | 0.054 | supported (marginal) |
| HGRN2 | 691 | 703 | 3.554 | 3.779 | −0.312 | **5.61e-09** | **supported** |

**要点**：
- **C1 全部不显著** — BoolQ 中 pure-correct 样本被 hurt 与否与 pure confidence 无关
- **C2 GDN/HGRN2 高度显著**（小到中等效应量 d≈0.31–0.36），helped 样本的 pure confidence 更低，符合"低信心样本更易被 hybrid 修正"的假设
- RetNet C2 borderline (p=0.054)，方向一致但效应量较小 (d=−0.16)

---
