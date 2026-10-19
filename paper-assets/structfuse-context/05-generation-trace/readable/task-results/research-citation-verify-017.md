# research citation verify 017

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verify_017_20260514T170911_result.json`
- **Structured JSON:** [`d49b4100313ad5daefe0.json`](../../sessions/d4/d49b4100313ad5daefe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RANGER
- **真实性**：✅ 确认存在
- **正确 arXiv ID**：2509.25257（与标注一致）
- **正确作者**：Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta → "Shah et al., 2025" ✅
- **正确标题**：*RANGER -- Repository-Level Agent for Graph-Enhanced Retrieval* ✅
- **描述准确性**：
  - "Knowledge graph + MCTS traversal" — ✅ 准确，论文使用代码知识图谱 + MCTS 引导的图探索
  - "MCTS-guided graph exploration" — ✅ 准确
  - "dual-stage (Cypher + MCTS)" — ✅ 准确，entity 查询走 Cypher lookup，NL 查询走 MCTS 探索
  - "heavy inference cost" — ⚠️ 编辑性判断。论文实际说的是 cross-encoder 评分成本高，MCTS 是为了让它 tractable。可保留但建议措辞改为 "higher inference cost due to cross-encoder scoring"
- **需要修正**：arXiv ID 序号虽高但确认真实存在（2025年9月 arXiv 月投稿量已超 25000）。无需修正核心信息。

---

## ARISE
- **真实性**：✅ 确认存在
- **正确 arXiv ID**：2605.03117（与标注一致）
- **正确作者**：Shahd Seddik, Fatemeh Fard → "Seddik & Fard, 2026" ✅
- **正确标题**：*ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair*
  - ⚠️ Discussion 中标题缺少 "A"、"Representation and Toolset"，建议补全
- **描述准确性**：
  - "Multi-granularity program graph (statement nodes + def-use edges)" — ✅ 准确
  - "intra-procedural def-use edges + data-flow slicing tool" — ✅ 准确，论文明确提到 three-tier tool API 将 data-flow slicing 作为 first-class queryable primitive
  - "SWE-bench Lite (300 issues)" — ✅ 准确（300 real GitHub issues, 11 Python repos）
  - "+17.0 Function Recall@1" — ✅ 准确（相比 SWE-agent baseline）
- **需要修正**：标题应补全为完整形式

---

**结论**：两篇引用均为真实论文，核心描述准确。修正项仅为：
1. RANGER "heavy inference cost" 措辞可更精确
2. ARISE 标题需补全

Sources:
- [RANGER - arXiv](https://arxiv.org/abs/2509.25257)
- [ARISE - arXiv](https://arxiv.org/abs/2605.03117)

---
