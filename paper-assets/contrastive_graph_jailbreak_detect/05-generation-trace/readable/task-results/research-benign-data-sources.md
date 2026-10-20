# research benign data sources

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_benign-data-sources_20260517T055130_result.json`
- **Structured JSON:** [`f94bd4b2d88ade737f5b.json`](../../sessions/f9/f94bd4b2d88ade737f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报结果：

---

## 1. Benign Traces 各 Repo 结论

| Repo | 结论 |
|------|------|
| **ToolBench** | **有**, 126K benign traces, 完整 tool_name+params+result, Apache-2.0 |
| **SHADE-Arena** | **有**, 但公开量少 (5/17 task pairs), 需申请完整版 |
| **AgentBench** | **无预录 traces**, 仅 task definitions, 需自行运行生成 |
| **Agent-SafetyBench** | **无**, 仅环境/工具定义, 无执行 traces |
| **STAC** | **无 benign**, 483 条全部是攻击 traces |

## 2. 推荐 Benign 数据获取方案

**首选: ToolBench** — 126K 条 benign API call traces, 格式 `Action(tool_name) + Action_Input(params) + Observation(result)` 几乎直接映射到目标格式，Apache-2.0 可自由使用。

**备选 (同分布合成)**: 用 STAC 的 4 个 SHADE-Arena 环境定义给 agent 正常任务，录制 benign traces，确保与攻击数据同分布。

## 3. STAC Failure Mode 分布

10 类 failure mode 分布均匀 (42-55/类)，总计 483 样本。80.7% 来自 SHADE-Arena 4 大环境 (spam_filter_updating 103, travel 99, workspace 98, banking 90)。

## 4. STAC Tool Chain 统计

- **256 个 unique tools**
- 链长: min=1, max=11, mean=2.62, median=3.0
- **84.7% 攻击链为 2-3 步** — 图规模小，需侧重节点属性编码而非拓扑复杂度
- Top tools: search_files_by_filename(117), send_email(99), get_file_by_id(42)

---
