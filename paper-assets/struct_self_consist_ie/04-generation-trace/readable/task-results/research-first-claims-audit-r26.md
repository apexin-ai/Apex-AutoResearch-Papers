# research first claims audit r26

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_first-claims-audit-r26_20260520T151205_result.json`
- **Structured JSON:** [`a9b1e5caa4087d789f9c.json`](../../sessions/a9/a9b1e5caa4087d789f9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。结果：

**8 matches total** (5 true positives, 3 false positives)

**需要修改的活跃文件（2个）：**

| 文件 | 行 | 匹配 | 风险 | 建议 |
|------|-----|------|------|------|
| `abstract.tex:6` | "the first systematic characterization" | HIGH | 加 "to our knowledge," |
| `introduction.tex:9` | "the first systematic empirical characterization" | HIGH | 加 "to our knowledge," 或改为 "a systematic..." |

**旧文件（不参与编译，仅记录）：** `conclusion.tex:3`, `introduction.tex:42`, `related_work.tex:24` 共 3 处 HIGH/MEDIUM，但按 C001 约束不需修改。

**零匹配模式：** pioneering, unprecedented, first comprehensive, first study, first work, first framework, novel（仅 "novel entities" 假阳性）。

报告已写入 `artifacts/r26_response/first_claims_audit.txt` 并注册。

---
