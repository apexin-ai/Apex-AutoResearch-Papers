# research narrative b draft

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_narrative-b-draft_20260516T075150_result.json`
- **Structured JSON:** [`d82486f6f43475e0fdae.json`](../../sessions/d8/d82486f6f43475e0fdae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用工具列表中，文件已写入 artifacts 目录但无法通过 MCP 注册。

产出已保存到 `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/narrative_b_draft.md`。

核心内容：

1. **Core claim 改写** — 从 "significantly improves" 转向 "structured magnitude-sensitive correction behavior + safe augmentation"，不依赖 p<0.05

2. **Evidence 分三层**：
   - **Tier 1 (mechanistic)**: inverted-U magnitude curve（非噪声的系统性行为）+ obs_only >> perdof（隔离出 obs features 为关键因素）
   - **Tier 2 (cross-seed)**: obs_only 在所有 seed 上 >= VLA-only（never hurts）
   - **Tier 3 (honest scope)**: spatial null result

3. **与当前论文的 diff**：Method 不变；Results 仅 reframe 措辞；magnitude curve 从 supporting evidence 升级为 main figure；需新增 ~40 行 analysis（why inverted-U, why obs > perdof）

4. **切换成本**：~135 行改动，~7 小时工作量。关键路径是新 analysis subsections 的论证质量。

---
