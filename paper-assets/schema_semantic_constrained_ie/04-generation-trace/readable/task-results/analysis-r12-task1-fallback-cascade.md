# analysis r12 task1 fallback cascade

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_task1_fallback_cascade_20260520T174540_result.json`
- **Structured JSON:** [`ea0440bedd441c72d6a4.json`](../../sessions/ea/ea0440bedd441c72d6a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Layer 1 — S1 诱导的 fallback 极小**
- Qwen: 仅 3 个 entity 因 S1 fallback 到 Generic（unc 中 type 为 "Feature-of"，一个不合法的类型名），涉及 2 个 relation 被弱化
- Llama: 仅 1 个 entity（unc 中 Material → con 中 Generic），0 个 relation 弱化
- S1 在 SciERC 的 6 种 entity type 上覆盖几乎完美

**Layer 2 — Generic wildcard 级联效应（真正的发现）**

| | Qwen | Llama |
|---|---|---|
| Generic entity 占比 | 10.2% (con) vs 10.1% (unc) | 14.6% vs 14.4% |
| 涉及 Generic 的 relation | 235 (13.6%) | 237 (18.0%) |
| DR 被 Generic 弱化的 relation | 109 (6.3%) | 123 (9.4%) |
| 弱化占涉及的比例 | 46.4% | 51.9% |

**Per-relation 分析**：Hyponym-of 和 Compare 100% 弱化（DR 表窄）；Used-for 0% 弱化（DR 表最宽，35 对 valid pairs）。Generic 平均参与每种 relation 38% 的 valid pairs。

输出文件在 westd-16980 上：
- JSON：`/root/autodl-tmp/schema_outputs/r12_fallback_cascade_analysis.json`
- LaTeX：`/root/autodl-tmp/schema_outputs/r12_fallback_cascade_text.txt`
- 脚本：`/root/schema_semantic_constrained_ie/r12_fallback_cascade_v2.py`

---
