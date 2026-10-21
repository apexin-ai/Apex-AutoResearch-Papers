# research citation verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verify_20260515T172008_result.json`
- **Structured JSON:** [`4dc74b85edb1081cd3a6.json`](../../sessions/4d/4dc74b85edb1081cd3a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。27 篇论文全部验证，结果写入 `artifacts/citation_audit.md`。

**3 个严重问题必须修正：**

1. **AgentPRM** — arXiv ID 完全搞错。当前 `2502.10325` 是 Choudhury 的另一篇论文，真正的 AgentPRM 是 `2511.08325`（Xi et al.）。作者 "Chatterjee et al." 在两篇论文中都不存在。
2. **Huang2024** — 作者写 "Huang et al."，但第一作者是 Ryo Kamoi，五位作者中无人姓 Huang。
3. **DAPO** — 标题错误。写的是 "Decoupled Clip and Dynamic Sampling Policy Optimization"（技术描述），实际论文标题是 "An Open-Source LLM Reinforcement Learning System at Scale"。

**2 个中等问题：**
- **CFGM** 标注为 "arXiv 2026"，实际已发表于 EMNLP 2025
- **WebAgent-R1** citation key "pei2025" 错误，第一作者是 Wei 不是 Pei

**额外发现：** 10 篇论文缺失 arXiv ID 已全部找到（含 ReflAct 2505.15182、GiGPO 2505.10978 等）。Thinkless 确认真实存在（arXiv 2505.13379, NeurIPS 2025），但未收录在 literature_map 中。

---
