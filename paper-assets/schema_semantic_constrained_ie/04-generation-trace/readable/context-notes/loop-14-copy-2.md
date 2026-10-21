# reviewer / loop_14.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`b632e54b32a655a75a02.json`](../../sessions/b6/b632e54b32a655a75a02.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T16:40:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- WikiEvents 数据在 westd-16980，代码也在 westd-16980。westd-21461 用途未确认，不要假设两台服务器配置相同
- `ontology_constraints_wikievents.json` 使用 `event_constraints` 格式（非 `argument_constraints`），`_build_spec()` 有自动转换（line 137-142），不要手动改 JSON 格式
- 论文 bootstrap delta 使用 `+0.02pp`（Llama-DocRED composability），不是 registry 的 `+0.51pp`（后者未考虑 parse failure）
- Qwen-DocRED composability 是 **significant negative**（-0.37pp, p=0.014），framing 已从 "orthogonal" 改为 "near-lossless"，不可 claim "zero-cost composability"

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，代码根目录 `/root/schema_semantic_constrained_ie`
- 模型：`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
- WikiEvents 数据：`/root/schema_semantic_constrained_ie/data/wikievents/`（ontology + event_role_KAIROS.json，train/dev/test.jsonl 可能仍在下载中未确认）
- WikiEvents ontology：`data/wikievents/ontology_constraints_wikievents.json`（event types 已 flatten 为短名，碰撞率从 96.1%→3.9%）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`
- 活跃进程：截至 handoff 时未查，可能有诊断 worker 在跑

### 3. 📊 当前状态
**刚完成审查**：WikiEvents Phase 1-3 全链路（schema compilation → semantic layer → violation checker → eval → dry run → flatten → bugfix → re-dryrun）

**核心发现**：Semantic layer (Layer 2) 在 EE 上持续触发 XGrammar assertion error → fallback 到 grammar-only。First-token collision bugfix + `any_allowed_valid` guard 已部署但未解决根因。Grammar-only 结果：EV 38.5%→0%，Trigger F1 +13.3pp，但 RoV 55.5% 未改善。

**Registry**：70 个实验，最近的都是 DONE。`r4_prompt_detailed` 和 `r4_prompt_minimal` 仍 PREPARING（prompt sensitivity 实验，非关键路径）。

**等待中**：Agent 正在跑 assertion error 诊断 Worker（我建议了 debug logging 方案）。下一个审查点是诊断结果或 semantic layer 修复后的 re-dryrun。

### 4. 📋 待办
- assertion 诊断 Worker 完成 → 审查根因分析是否合理，verify fix approach
- semantic layer 修复 + re-dryrun → 检查 RoV 是否 ↓50%+；如果是 → Claim 5 full strength；如果不是 → 建议 Director 调整 claim 措辞为 grammar-only generalization
- WikiEvents 全量实验（3 models × 2 modes）启动 → 审查 GPU 使用（L1 红线 #4）+ 检查 experiment spec completeness
- 论文 §5.4 Event Extraction section 写作提交 → 按 §5.2 模板做 chapter review，重点检查 claim 强度是否与实际 violation reduction 匹配
- 任何 ROADMAP 更新涉及 deadline 风险 → 用 `ai-time-discipline` skill 评估 GPU-hours

### 5. 🎯 战略上下文
**项目核心**：OntoCoDec = grammar + semantic 两层 constrained decoding for IE。RE 主实验（SciERC + DocRED）已完成且结果强（94% DR reduction）。WikiEvents EE 是 D040 扩展，目标 conference main。

**决策链**：D040（conference main 升级 + WikiEvents）→ ACE05 排除（LDC 付费）→ WikiEvents 选定 → Phase 1-3 完成 → semantic layer assertion error 未解

**最容易判断错的事**：
1. **不要以为 bugfix 已经解决 assertion error** — collision-safe fix + `any_allowed_valid` guard 已部署但 assertion 仍触发。根因是 PositionDetector 在错误时机返回 semantic position，不是 token collision
2. **AC 从 0%→12.2% 不是退化** — 是 grammar 修正 event types 后暴露的 latent violations（unconstrained 的 invalid event types 跳过了 AC 检查）
3. **`_apply_first_token_mask` 和 `_apply_type_mask` 都已有 collision-safe + guard** — 不要重复修这个 bug
4. **论文 DDL May 25** — 距今 8 天。RE 主实验数据已齐，WikiEvents 是增量。如果 semantic layer 1 天修不好，grammar-only 结果仍可写入论文（降级 claim 但不致命）


---
