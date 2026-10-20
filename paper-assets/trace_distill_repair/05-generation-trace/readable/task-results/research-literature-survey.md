# research literature survey

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_survey_20260514T134901_result.json`
- **Structured JSON:** [`0f1ca4545cc5ccf84b18.json`](../../sessions/0f/0f1ca4545cc5ccf84b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `register_artifact` 工具可用。文件已写入完毕。

产出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/literature_map.yaml`

共收录 **15 篇论文**，按四个维度分布：

| 维度 | 数量 | 代表论文 |
|------|------|----------|
| Direct Competitors | 5 | Wang2025 (EMNLP目标论文), TraceFixer, TraceRepair, DynaFix, Haque2025 |
| Method Components | 5 | LDB, TraceCoder, Avatar, MiniPLM, KD for Code |
| Evaluation | 2 | BugsInPy, SWE-bench |
| Background | 3 | APR Survey, RepairAgent |

关键发现对 DTD 立项的支撑：
- **Haque2025** 和 **Wang2025** 都证实原始 trace 直接拼入 prompt 效果有限，且 trace 复杂度越高效果越差——这正是 DTD 结构化过滤要解决的问题
- **LDB** 的 basic block 分段验证思路验证了结构化分段的可行性，但依赖大 LLM 在线推理
- **DynaFix/TraceRepair** 代表最新竞争者，均用全量 trace + 大模型推理，DTD 用蒸馏小模型做预过滤是差异化路线

---
