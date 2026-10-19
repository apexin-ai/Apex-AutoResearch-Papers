# research r7 arxiv verification 4papers

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r7_arxiv_verification_4papers_20260518T053434_result.json`
- **Structured JSON:** [`c3e7c25aabf8448821c0.json`](../../sessions/c3/c3e7c25aabf8448821c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| # | arXiv ID | 存在 | 真实标题 | 真实作者 | 与声称匹配 | 相关性 |
|---|----------|------|----------|----------|-----------|--------|
| 1 | 2503.11926 | ✓ | Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation | Baker, Huizinga, Gao, Dou, Guan, Madry, Zaremba, Pachocki, Farhi | **MISMATCH**: 标题缺少后半部分 "and the Risks of Promoting Obfuscation" | **高** — CoT monitoring 检测 reasoning model 的 misbehavior，与本项目 probing hidden states for safety detection 直接相关 |
| 2 | 2510.06594 | ✓ | Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection? | Kadali, Papalexakis | 匹配 | **高** — 研究 LLM 内部层对 jailbreak 的响应模式，与本项目 probing internal representations 方法高度一致 |
| 3 | 2510.06036 | ✓ | Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning? | Yin, Leong, Yang, Huang, Li, Wang, Yoon 等 | **MISMATCH**: 声称标题 "Refusal Falls Off a Cliff"，真实标题含副标题 "How Safety Alignment Fails in Reasoning?" | **高** — mechanistic interpretability 分析 reasoning model 的 safety failure（refusal cliff），与本项目 contrastive trace analysis 直接相关 |
| 4 | 2509.21344 | ✓ | Linear probes rely on textual evidence: Results from leakage mitigation studies in language models | Boxo, Neelappa, Raval | **MISMATCH**: 声称标题缺少副标题 | **极高** — 直接研究 linear probe 检测 harmful behavior 的局限性（依赖文本证据而非深层模式），是本项目方法的核心 baseline/对比工作 |

**MISMATCH 汇总**：
- **#1**: 声称标题 "Monitoring Reasoning Models for Misbehavior"，实际为 "Monitoring Reasoning Models for Misbehavior **and the Risks of Promoting Obfuscation**"
- **#3**: 声称标题 "Refusal Falls Off a Cliff"，实际为 "Refusal Falls off a Cliff: **How Safety Alignment Fails in Reasoning?**"
- **#4**: 声称标题 "Linear probes rely on textual evidence"，实际为 "Linear probes rely on textual evidence: **Results from leakage mitigation studies in language models**"

三处 mismatch 均为省略了副标题，主标题部分正确。4 篇论文全部存在，与项目相关性均为高或极高。

---
