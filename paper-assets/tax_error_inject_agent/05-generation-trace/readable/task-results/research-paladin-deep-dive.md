# research paladin deep dive

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paladin-deep-dive_20260514T215004_result.json`
- **Structured JSON:** [`a00ad74b1e4e5106941d.json`](../../sessions/a0/a00ad74b1e4e5106941d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心结论:

**PALADIN 数字验证**: paper_framing.md 中所有数字准确 (32.76% → 89.68% RR, 7 failure types, 50K+ trajectories, 80/20 ratio)。

**需要更新 paper_framing 的 3 个发现**:

1. **PALADIN 不是纯 SFT** — 包含 inference-time retrieval (55+ exemplars)，去掉后 RR 降 ~30pp。这是重要的未讨论 confound，应加入对比维度表
2. **PALADIN 也没做多 seed 验证** — 只有 bootstrap 统计检验。我们的多 seed 设计反而是方法论优势
3. **EEF (arXiv 2504.13145)** 是关键对比论文 — 同样利用失败 trajectory 但方向相反(提取好 signal vs 注入坏 signal)，在 WebShop 上成功，强化了 "injection 方向本身可能错误" 的论点

**ALFWorld SOTA 上下文**: CoEx 93.28%, AgentPRM 91.0%, Reflexion+GPT-4 ~97%(multi-trial)。我们的 65.3% vanilla 在 SFT-only 8B 模型范畴合理。

**除 PALADIN 外无其他 taxonomy-guided error injection 工作** — 我们是第一个跨域迁移尝试，也是第一个报告失败的。

产出:
- `paladin_comparison.md` — 完整调研报告 (已注册 artifact)
- `literature_map.yaml` — 结构化文献地图 (已注册 artifact)
- `memory.md` — 已更新关键文献洞察

---
