# paper citation audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation_audit_20260519T192756_result.json`
- **Structured JSON:** [`f40a04e569c3f432b7a8.json`](../../sessions/f4/f40a04e569c3f432b7a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification complete. Here's the full audit report.

---

## 引用审计结果

### 重点审计条目（Round 8-9 新增）

| bib key | title | author | year | venue | issues |
|---------|-------|--------|------|-------|--------|
| `yang2024sweagent` | ✅ | ✅ | ✅ 2024 | ✅ NeurIPS 2024 | 无 |
| `wang2025openhands` | ✅ | ✅ | ✅ 2025 | ✅ ICLR 2025 | 无 |
| `jiang2023llmlingua` | ✅ | ✅ | ✅ 2023 | ✅ EMNLP 2023 | 无 |
| `li2023selectivecontext` | ✅ | ✅ | ✅ 2023 | ✅ EMNLP 2023 | 无 |
| `barr2015oracle` | ✅ | ✅ | ✅ 2015 | ✅ IEEE TSE 41(5) | 无 |
| `he2021loganalysis` | ✅ | ✅ | ✅ 2021 | ✅ ACM CSUR 54(6) | 无 |
| `papadakis2019mutation` | ✅ | ✅ | ✅ 2019 | ✅ Advances in Computers 112 | 无 |

### 发现问题的条目

| bib key | 问题类型 | 详情 |
|---------|----------|------|
| **`mukherjee2025llmfl`** | **严重：arXiv URL 错误 + 论文可能不存在** | arXiv 2312.02986 实际是一篇物理论文（lattice QCD），与 FL 无关。搜索无法找到标题为 "Can Large Language Models Localize Faults like Developers?" 的论文。Soneya Binta Hossain 在 ICSE 2025 发表的是 TOGLL（test oracle generation），不是这篇。此外 key 用 "mukherjee" 但作者列表中无此人。**建议删除或替换为真实论文。** |
| **`widyasari2024llm4fl`** | **可疑：标题无法验证 + key/year 不匹配** | 搜索无法找到标题为 "LLM4FL: An LLM-based Fault Localization Integrated Debugging Framework for Automated Program Repair" 的 Widyasari 论文。已有的 "LLM4FL" 论文是不同作者的不同工作。Widyasari 在 dblp 上无 ICSE 2025 记录。Key 用 2024 但 year=2025。**建议核实或删除。** |
| `qwen2025coder` | key/year 不匹配 | key 含 "2025" 但 year={2024}。arXiv 提交于 2024 年 9 月，year=2024 正确。建议 key 改为 `qwen2024coder`。 |
| `ferrando2025execute` | key 命名问题 | key 含 "ferrando" 但作者列表中无此人，第一作者是 Jordi Armengol-Estapé。建议 key 改为 `armengol2025execute`。 |
| `roziere2024code` | year 可商榷 | Code Llama arXiv 提交于 2023 年 8 月（2308.12950），bib 写 year=2024。部分数据库标注为 2024，但原始发表是 2023。 |

### 其他条目验证（均通过）

| bib key | 状态 | 备注 |
|---------|------|------|
| `chen2025tracepile` | ✅ | NeurIPS 2025 |
| `ding2024traced` | ✅ | ICSE 2024 |
| `chen2021evaluating` | ✅ | Codex/HumanEval |
| `austin2021program` | ✅ | |
| `gu2024cruxeval` | ✅ | ICML 2024 |
| `hu2022lora` | ✅ | ICLR 2022 |
| `deepseek2024coder` | ✅ | |
| `wang2025dcsh` | ✅ | EMNLP 2025 Findings |
| `ni2024next` | ✅ | ICML 2024 |
| `eguchi2025etcot` | ✅ | ICML 2025 Workshop PRAL |
| `xu2025cruxevalx` | ✅ | ACL 2025 |
| `appt2024` | ✅ | IEEE TSE 50(3) |
| `zhou2024llm4patch` | ✅ | IEEE TSE 50(11) |
| `spiess2025calibration` | ✅ | ICSE 2025 |
| `foster2025mutation` | ✅ | FSE 2025 Industry |
| `widyasari2024fusefl` | ✅ | SANER 2024 |
| `huang2026tracecoder` | ✅ | ICSE 2026 |
| `wang2025inspectcoder` | ✅ | arXiv 2510.18327 |
| `haque2025traces` | ✅ | KnowledgeNLP@ACL 2025 |
| `yang2024generalization` | ✅ | NAACL 2024 |
| `tian2024debugbench` | ✅ | ACL 2024 Findings |
| `abreu2007accuracy` | ✅ | |
| `jones2002visualization` | ✅ | ICSE 2002 |
| `wong2014dstar` | ✅ | JSS 2014 |
| `kang2024autofl` | ✅ | ICSE 2024 |
| `qin2024agentfl` | ✅ | ASE 2024 |
| `dinella2022toga` | ✅ | ICSE 2022 |
| `steenhoek2024deepdfa` | ✅ | ICSE 2024 |
| `jimenez2024swebench` | ✅ | ICLR 2024 |
| `kadavath2022language` | ✅ | |
| `kamei2013large` | ✅ | IEEE TSE 2013 |
| `bouzenia2025repairagent` | ✅ | ICSE 2025 |
| `chen2024selfdebug` | ✅ | ICLR 2024 |
| `liu2023codeexecution` | ✅ | ACL 2023 Findings |
| `tian2020patchcorrectness` | ✅ | ASE 2020 |
| `watson2020atlas` | ✅ | ICSE 2020 |
| `yu2022assertion` | ✅ | ICSE 2022 |
| `nashid2023assertion` | ✅ | ASE 2023 |
| `yadavally2024slicing` | ✅ | OOPSLA 2024 |
| `xia2024agentless` | ✅ | |
| `guo2017calibration` | ✅ | ICML 2017 |
| `geng2024calibration` | ✅ | NAACL 2024 |
| `hoang2019deepjit` | ✅ | MSR 2019 |
| `hoang2020cc2vec` | ✅ | ICSE 2020 |
| `pornprasit2021jitline` | ✅ | MSR 2021 |
| `bengio2009curriculum` | ✅ | ICML 2009 |
| `sachdeva2024dataefficient` | ✅ | |
| `swayamdipta2020cartography` | ✅ | EMNLP 2020 |
| `xie2023doremi` | ✅ | NeurIPS 2023 |

### 重复条目检查
未发现重复条目。

### 总结

- **2 个严重问题**：`mukherjee2025llmfl`（arXiv URL 指向错误论文，标题/作者无法验证）和 `widyasari2024llm4fl`（标题无法验证，可能是幻觉引用）
- **3 个轻度问题**：`qwen2025coder`（key/year 不匹配）、`ferrando2025execute`（key 命名错误）、`roziere2024code`（year 可商榷）
- 其余 ~46 个条目全部通过验证

---
