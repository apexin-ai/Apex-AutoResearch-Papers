# write relwork expansion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_relwork_expansion_20260514T181500_result.json`
- **Structured JSON:** [`b80ae628482577765571.json`](../../sessions/b8/b80ae628482577765571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出汇总：

**写入文件：**
- `section6_relwork_additions.tex` — 4 个补充段落，标注了精确插入位置
- `relwork_new_entries.bib` — 追加 6 个新 bib 条目（PICARD, RELATE, Ontology-to-Tools, SpERT, PFN, zhou2026snowballing）

**5 项补充内容：**

| # | 引用 | 位置 | 要点 |
|---|------|------|------|
| 1 | PICARD (Scholak et al., EMNLP 2021) | Semantic Constrained Decoding for Code 段 | SQL 增量解析 vs OntoCoDec：fixed schema vs 动态 entity registry（~80 words） |
| 2 | SpERT + PFN (ECAI 2020 / EMNLP 2021) | Structural Constraints 段 | 监督联合模型隐式 enforce type consistency，但限于 fixed schema + supervised |
| 3 | RELATE (Olasunkanmi et al., arXiv 2509.19057) | Post-hoc Ontology Validation 段 | 三阶段 post-extraction ontology 对齐，需额外 SapBERT；OntoCoDec 在解码时 enforce |
| 4 | Ontology-to-Tools (Zhou et al., arXiv 2602.03439) | Post-hoc Ontology Validation 段 | 编译 ontology → tool interfaces（tool-call level），OntoCoDec 在 token level |
| 5 | zhou2026snowballing 审计 | 原文 line 85 | **已验证**：Hongxu Zhou, arXiv:2604.06066, Apr 2026。描述准确，已移除 PENDING AUDIT 注释 |

**注意：** PFN 的实际 venue 是 **EMNLP 2021**，不是任务描述中的 AAAI 2021。bib 条目已按正确 venue 录入。

---
