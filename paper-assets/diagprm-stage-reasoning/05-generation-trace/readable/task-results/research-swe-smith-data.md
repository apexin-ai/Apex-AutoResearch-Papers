# research swe smith data

**diagprm stage reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_swe-smith-data_20260511T145404_result.json`
- **Structured JSON:** [`925bef10d530d0cd2cfa.json`](../../sessions/92/925bef10d530d0cd2cfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，跳过注册。报告已写入：

**`artifacts/swe-smith-trajectory-research.md`**

核心结论：

1. **SWE-smith 轨迹完全可用** — `SWE-bench/SWE-smith-trajectories` (HuggingFace, MIT)，76k 条轨迹，包含 `resolved` 标签
2. **包含自然语言推理** — SWE-agent 的 Thought-Action-Observation 范式，assistant content 中有诊断分析、推理策略等自然语言文本，不是纯工具调用序列
3. **三种格式 split**：`tool`（function call）、`xml`（XML 标签）、`ticks`（反引号），推荐用 `tool` split
4. **字段**：`messages`（JSON string，role/content 对话格式）、`instance_id`、`resolved`（bool）、`model`、`traj_id`、`patch`
5. **备选**：`nebius/SWE-agent-trajectories`（80k 条，CC-BY-4.0，unresolved 比例更高）

加载命令：
```python
from datasets import load_dataset
ds = load_dataset("SWE-bench/SWE-smith-trajectories", "tool")
```

待实际加载确认的事项：messages 是否需要 `json.loads()` 解析、thought 和 action 在 content 中的分隔方式、tool split 的 function call 具体结构。

---
