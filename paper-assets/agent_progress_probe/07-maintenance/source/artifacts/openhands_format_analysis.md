# OpenHands 轨迹格式分析与 Pipeline 复用性评估

**数据集**: `nebius/SWE-rebench-openhands-trajectories`
**规模**: 67,074 条轨迹, 2.08 GB parquet
**模型**: Qwen3-Coder-480B-A35B-Instruct / OpenHands v0.54.0
**解决率**: 47.9% (32,161/67,074)

---

## 1. 数据格式描述

### 顶层字段

| 字段 | 类型 | 示例 |
|------|------|------|
| `trajectory_id` | str | `"chatcmpl-27dd0152..."` |
| `instance_id` | str | `"PlasmaFAIR__sdf-xarray-24"` |
| `repo` | str | `"PlasmaFAIR/sdf-xarray"` |
| `trajectory` | list[dict] | 185 steps（平均 64.3, max 100） |
| `tools` | list[dict] | 5 个工具定义 |
| `model_patch` | str | unified diff |
| `exit_status` | str | `"submit"` 或错误信息 |
| `resolved` | int | 0 或 1 |
| `gen_tests_correct` | float/null | agent 生成测试的正确数 |
| `pred_passes_gen_tests` | float/null | 通过的 agent 生成测试数 |

### Step 结构

每个 step 固定 5 个 key：`content`, `name`, `role`, `tool_call_id`, `tool_calls`

**4 种 role：**

| Role | 含义 | content | tool_calls | name/tool_call_id |
|------|------|---------|------------|-------------------|
| `system` | 系统 prompt | OpenHands agent 指令 (11k chars) | None | None |
| `user` | Issue 描述 | `<uploaded_files>...<issue_description>...` | None | None |
| `assistant` | Agent 动作 | 推理文本 + 引导语 | list[{function, id, type}] | None |
| `tool` | 工具响应 | 执行结果文本 | None | 工具名 / call_id |

**tool_calls 结构（assistant step）：**
```json
{
  "function": {
    "name": "execute_bash" | "str_replace_editor" | "think" | "finish" | "task_tracker",
    "arguments": "{\"command\": \"ls -la\"}"  // JSON string
  },
  "id": "chatcmpl-tool-...",
  "type": "function"
}
```

**可用工具：**
- `execute_bash` — 执行 bash 命令
- `str_replace_editor` — 文件查看/编辑（view / str_replace / create / insert）
- `think` — 内部推理（不改变环境）
- `finish` — 标记完成
- `task_tracker` — 任务跟踪

### 典型交互序列
```
Step 0: system  → 系统 prompt
Step 1: user    → Issue + 上传文件路径
Step 2: assistant (tool_calls: think) → 分析问题
Step 3: tool    → "Your thought has been logged."
Step 4: assistant (tool_calls: str_replace_editor view) → 浏览文件
Step 5: tool    → 文件内容
Step 6: assistant (tool_calls: execute_bash) → 运行命令
Step 7: tool    → 命令输出
...
Step N: assistant (tool_calls: finish) → 提交
```

---

## 2. 与 SWE-agent 格式差异对比

| 维度 | SWE-agent | OpenHands | 影响 |
|------|-----------|-----------|------|
| **Step 文本字段** | `text` | `content` | 字段重命名 |
| **Action role** | `"ai"` | `"assistant"` | 角色名映射 |
| **Observation role** | `"user"` (index>0) | `"tool"` | 角色名映射 |
| **动作格式** | text 中嵌入 \`\`\`command\`\`\` | 结构化 `tool_calls` (function calling API) | **核心差异** |
| **命令提取** | 正则匹配三反引号 | 解析 `tool_calls[].function.arguments` JSON | 需重写提取逻辑 |
| **文件编辑** | `edit <start>:<end>` 命令 | `str_replace_editor` tool call (view/str_replace/create/insert) | **需重写** |
| **文件显示标记** | `[File: <name> (N lines)]` | tool response 直接返回文件内容 | 需适配匹配规则 |
| **结果字段** | `target` (bool) | `resolved` (int 0/1) | 简单映射 |
| **Patch 字段** | `generated_patch` | `model_patch` | 字段重命名 |
| **退出状态** | `"submitted"` / `"exit_context"` | `"submit"` / 错误信息 | 值映射 |
| **模型名** | `model_name` 字段 | 无（数据集级固定为 Qwen3-Coder） | 不影响 pipeline |
| **Step mask** | `mask` (bool) | 无 | 不影响（未使用） |
| **额外字段** | `eval_logs` | `tools`, `repo`, `gen_tests_correct` | 可忽略或利用 |
| **Step 关联** | 无（靠顺序推断 action→observation） | `tool_call_id` 显式关联 | 更可靠的配对 |

---

## 3. Pipeline 组件复用性评估

### data_loader.py — 需适配 (中等工作量)

| 子组件 | 状态 | 说明 |
|--------|------|------|
| `Step` dataclass | **需改写** | 字段不同：`text→content`, 新增 `tool_calls/name/tool_call_id`，去掉 `mask/cutoff_date/system_prompt` |
| `Step.is_action` | **需改** | `role == "assistant"` (原 `"ai"`) |
| `Step.is_observation` | **需改** | `role == "tool"` (原 `"user" and index>0`) |
| `Step.command` | **需重写** | 从 `tool_calls[0].function.arguments` 解析，不再是三反引号提取 |
| `Step.has_file_display` | **需重写** | OpenHands 无 `[File: ...]` 标记，改为检测 `str_replace_editor` tool response |
| `Step.has_error` | **可复用** | `"Traceback"` / `"Error"` 检测仍适用于 tool response content |
| `Step.has_test_output` | **可复用** | PASSED/FAILED 模式在 bash 输出中仍然适用 |
| `Trajectory` dataclass | **需改写** | `target→resolved`, `generated_patch→model_patch`, `model_name` 不存在 |
| `parse_trajectory()` | **需重写** | 解析逻辑完全不同 |
| `load_trajectories()` | **可复用** | JSONL 加载逻辑通用 |

**建议**：写一个 `OpenHandsAdapter` 将 OpenHands 格式转为统一的 `Trajectory`/`Step` 接口，而非修改原始 dataclass。

### window_extractor.py — 可直接复用 (少量适配)

| 子组件 | 状态 | 说明 |
|--------|------|------|
| 滑动窗口逻辑 | **可复用** | 与数据格式无关，只依赖 Step 列表 |
| action-observation 配对 | **可复用** | OpenHands 也是严格的 assistant→tool 交替 |
| `trajectory_id` 构造 | **需改** | OpenHands 已有 `trajectory_id` 字段，不需要拼接 |
| 窗口 dict 构建 | **可复用** | 字段名兼容 |

### generate_embeddings.py — 可直接复用

| 子组件 | 状态 | 说明 |
|--------|------|------|
| Embedding 模型加载 | **完全复用** | 与数据格式无关 |
| 文本提取 | **需微调** | `step["text"]` → `step["content"]`；assistant step 需要拼接 content + tool_calls arguments |
| Tensor 构建 | **完全复用** | shape/pooling/normalization 通用 |
| 输出格式 | **完全复用** | .pt 格式不变 |

### Labeling Functions — 需中等程度适配

| LF | 状态 | 说明 |
|----|------|------|
| `lf_file_diff_delta` | **需重写核心逻辑** | SWE-agent 检测 `edit <start>:<end>` 命令 + `[File: ...]` 标记；OpenHands 需检测 `str_replace_editor` tool call 中的 `str_replace`/`create`/`insert` command，从 `arguments` JSON 提取文件名和编辑内容 |
| `lf_command_repetition` | **需适配提取** | 命令从 `tool_calls[].function.arguments` 提取而非三反引号；相似度计算 (`SequenceMatcher`) 可完全复用 |
| `lf_outcome_backpropagation` | **几乎可复用** | 仅需映射 `target→resolved`（int→bool）和 `exit_status` 值（`"exit_context"` → 检测非 `"submit"` 状态） |

---

## 4. 建议适配方案

### 方案：Adapter 模式 (推荐)

新建 `openhands_adapter.py`，实现格式转换层，使下游 pipeline 无需修改：

```
OpenHands JSONL → openhands_adapter.py → 统一 Trajectory/Step 接口
                                              ↓
                              window_extractor → LFs → embeddings → train_probe
```

**核心转换逻辑：**

1. **Step 转换**:
   - `role`: `"assistant"` → `"ai"`, `"tool"` → `"user"`
   - `content` → `text`
   - assistant step: 拼接 `content + "\n```\n" + extract_command(tool_calls) + "\n```\n"` 模拟 SWE-agent 的 text 格式
   - tool step: 直接使用 `content` 作为 `text`

2. **命令提取** (`extract_command`):
   - `execute_bash`: 从 `arguments.command` 提取
   - `str_replace_editor view`: → `open {path}`
   - `str_replace_editor str_replace`: → `edit` (拼接 old_str/new_str)
   - `str_replace_editor create`: → `create {path}`
   - `think` / `finish`: 跳过或特殊处理

3. **Trajectory 转换**:
   - `resolved` (int) → `target` (bool)
   - `model_patch` → `generated_patch`
   - `exit_status`: `"submit"` → `"submitted"`, 其他 → `"exit_context"`

4. **LF 适配**:
   - `file_diff_delta`: 在 adapter 层将 `str_replace` 动作转为类似 `edit` 的格式，或直接在 LF 中增加 OpenHands 分支
   - `command_repetition`: adapter 层已将命令提取到 text 中，可复用
   - `outcome_backpropagation`: adapter 层已映射字段，无需改动

### 工作量估算

| 组件 | 工作量 | 说明 |
|------|--------|------|
| `openhands_adapter.py` | ~200 行 | Step/Trajectory 格式转换 + 命令提取 |
| `data_loader.py` 改动 | ~20 行 | 添加 format 参数选择 adapter |
| `labeling_functions.py` 改动 | ~50 行 | `file_diff_delta` 增加 str_replace_editor 检测分支 |
| 其余组件 | 0 行 | 无需修改 |
| **总计** | **~270 行** | 1-2 天工作量 |

### 关键风险

1. **OpenHands 一个 assistant step 可能包含多个 tool_calls**（SWE-agent 每步一个命令），窗口切分逻辑需验证
2. **`think` 和 `task_tracker` 工具**不改变环境但占 step，需决定是否过滤
3. **解决率差异大**（OpenHands 47.9% vs SWE-agent 16.7%），label 分布会显著不同，可能需要调整 LF 阈值或重新标定 probe
