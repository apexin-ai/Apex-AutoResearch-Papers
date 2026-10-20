# paper r8 framing compress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r8-framing-compress_20260515T222051_result.json`
- **Structured JSON:** [`21a13c0ada24040f0d81.json`](../../sessions/21/21a13c0ada24040f0d81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件 LaTeX 语法正确。修改摘要：

| Task | 变更 | 预估节省 |
|------|------|----------|
| **1. 标题** | "Struggle to Select" → "The Correlation-Selection Gap"，去掉 overclaim 的拟人化措辞 | — |
| **2. Abstract** | 9行→6行：砍掉 self-consistency 展开定义、修辞问句、"closing it likely requires" 尾句；合并两层解释为一句 | ~3行 |
| **3. Introduction** | 砍掉 self-consistency 冗余展开（GSM8K 数据、selection mechanism 解释）、prior work 重复内容、contributions 条目中的冗余措辞 | ~8行（≈0.4页） |
| **4. Related work** | 合并 test-time scaling 段（去掉逐条列举改为批引用）、裁掉 3 个边缘引用（josifoski2022genie, wang2023instructuie, jinnai2024mbr）、压缩 MBR 讨论、删 P(True)/ensembles/MC-dropout/conformal 段 | ~7行（≈0.3页） |
| **5. Method** | 砍掉 problem formulation 中"asymmetry is central to…"冗余句、FK 的 independence test 细节、SJ 的 Jaccard 原始引用、evaluation 段改为更紧凑的表述 | ~5行（≈0.2页） |
| **6. Limitations + Conclusion** | Limitations: 合并段落、砍掉 CoNLL structural advantage 细节和 seed confound 细节。Conclusion: 砍掉具体 nats 数值、single-dataset scope 括号注释 | ~6行（≈0.2页） |

合计节省约 29 行文本（≈1.1 页双栏），达到压缩目标。

---
