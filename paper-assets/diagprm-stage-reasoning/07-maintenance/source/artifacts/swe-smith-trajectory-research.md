# SWE-smith 轨迹数据调研报告

## 结论

**SWE-smith 轨迹数据完全可用。** 包含自然语言推理（thought）、工具调用（action）、执行结果（observation）的完整交互记录，有 resolved/unresolved 标签，数量远超需求。

---

## 1. 主要数据源：SWE-bench/SWE-smith-trajectories

| 属性 | 值 |
|------|-----|
| HuggingFace | `SWE-bench/SWE-smith-trajectories` |
| 总量 | 76,002 条轨迹 |
| 大小 | 4.22 GB (Parquet) |
| License | MIT |
| 生成模型 | Claude 3.7 Sonnet (via SWE-agent) |

### 字段结构

| 字段 | 类型 | 说明 |
|------|------|------|
| `messages` | string (JSON) | 完整对话历史，包含 thought + action + observation |
| `instance_id` | string | 任务标识（repo + issue） |
| `resolved` | bool | 是否成功修复 |
| `model` | string | 生成模型名 |
| `traj_id` | string | 轨迹唯一 ID |
| `patch` | string | 生成的代码 diff |

### 三个 Split（不同 action 格式化方式）

| Split | 数量 | 大小 | 格式说明 |
|-------|------|------|----------|
| `tool` | 24,100 | 3.73 GB | 结构化 function call 格式（类似 OpenAI tool_calls） |
| `xml` | 26,076 | 3.58 GB | XML 标签包裹 action |
| `ticks` | 25,826 | 3.42 GB | 反引号包裹 action |

三种 split 是**同一批轨迹的不同格式化表示**，用于对比哪种格式训练效果更好。

### messages 字段结构

```json
[
  {
    "role": "system",
    "content": "You are a helpful assistant that can interact with a computer to solve tasks...",
    "agent": "main",
    "message_type": "system_prompt"
  },
  {
    "role": "user",
    "content": "<uploaded_files>...</uploaded_files>\nI've uploaded a repository..."
  },
  {
    "role": "assistant",
    "content": "I'll start by exploring the repository structure to understand the codebase..."
  }
]
```

### 自然语言推理内容（关键判断）

**包含。** SWE-agent 的轨迹遵循 Thought-Action-Observation 范式：

- **Thought**（自然语言推理）：agent 分析问题、诊断 bug 原因、推理修复策略的文本。例如 *"We are indeed seeing the same output as the issue. The problem appears to be in the date parsing logic..."*
- **Action**：执行的命令（`find_file`, `open_file`, `edit`, shell 命令等）
- **Observation**：命令输出/环境反馈

在 messages 格式中，assistant 的 content 同时包含 thought 和 action（thought 在前，action 在后），user 的 content 包含 observation。

---

## 2. 备选数据源

### nebius/SWE-agent-trajectories

| 属性 | 值 |
|------|-----|
| HuggingFace | `nebius/SWE-agent-trajectories` |
| 总量 | 80,036 条 |
| Resolved | 13,389 (16.7%) |
| Unresolved | 66,647 (83.3%) |
| 大小 | 1.11 GB |
| License | CC-BY-4.0 |

字段：`instance_id`, `model_name`, `target` (bool), `trajectory` (list), `exit_status`, `generated_patch`, `eval_logs`

trajectory 字段是 message list：
```json
{
  "role": "system|ai|user",
  "content": "...",
  "cutoff_date": "01.01.2023",
  "mask": false
}
```

优点：unresolved 轨迹更多，resolved/unresolved 比例更适合混合采样。

### nebius/SWE-rebench-openhands-trajectories

- OpenHands agent 框架（非 SWE-agent）的轨迹
- 用 Qwen3-Coder-480B 生成
- 多轮 agent 交互，格式不同于 SWE-agent

---

## 3. 推荐方案

**首选 `SWE-bench/SWE-smith-trajectories`**，理由：
1. 明确包含自然语言推理
2. 有 `resolved` 标签，方便混合采样
3. MIT 开源
4. 76k 条远超 100 条需求，可精选高质量子集
5. 三种格式可选，`tool` split 最接近现代 agent 格式

**采样策略建议**：从 `tool` split 中采样 50 条 resolved + 50 条 unresolved。

---

## 4. 获取命令

```python
from datasets import load_dataset

# 加载 tool 格式 split
ds = load_dataset("SWE-bench/SWE-smith-trajectories", "tool")

# 查看第一条
print(ds[0]["messages"])  # JSON string，需 json.loads()
print(ds[0]["resolved"])  # True/False
print(ds[0]["instance_id"])

# 按 resolved 筛选
import json
resolved = [x for x in ds if x["resolved"]]
unresolved = [x for x in ds if not x["resolved"]]

# 采样 100 条
import random
sample = random.sample(resolved, 50) + random.sample(unresolved, 50)
```

```bash
# CLI 下载（不实际执行）
pip install datasets
huggingface-cli download SWE-bench/SWE-smith-trajectories --repo-type dataset
```

---

## 5. 需确认事项

1. **messages 字段是 JSON string 还是已解析的 list** — 从 HF 元数据看是 string（7.95k-664k chars），加载后可能需要 `json.loads()`
2. **thought 和 action 是否在 content 中明确分隔** — SWE-agent 原始 .traj 有独立字段，但转为 messages 格式后可能合并在 assistant content 中，需实际加载验证
3. **tool split 的 function call 格式** — 是否有独立的 `tool_calls` 字段还是内嵌在 content 中，需实际查看
