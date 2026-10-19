# research openthinker 7b deepdive

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openthinker_7b_deepdive_20260517T060328_result.json`
- **Structured JSON:** [`988a6ff9bf9ca6ed91b0.json`](../../sessions/98/988a6ff9bf9ca6ed91b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。核心结论：

**GO — OpenThinker-7B 数据完全可用于 Path A 实验。**

关键发现：
- 数据集 `ishitakakkar-10/HarmThoughts` 中 `ot-7b` 有 333 条 traces（270 条 self-jailbreak），step-level 标签体系与 R1-8B 完全一致
- CP 可直接通过首个 `DKE` 标注推导，97.3% traces 有效
- 模型 15.2 GB BF16，服务器有 2×97GB VRAM，无瓶颈
- Full pipeline 端到端估算 30-50 分钟
- 作为非 R1-蒸馏的 reasoning model（STILL 训练），对 generalizability 有独立验证价值

---
