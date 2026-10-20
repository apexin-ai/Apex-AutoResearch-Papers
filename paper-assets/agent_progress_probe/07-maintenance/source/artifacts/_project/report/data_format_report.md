# SWE-agent Trajectories 数据格式报告

## 1. 数据集概况

| 属性 | 值 |
|------|-----|
| HuggingFace ID | `nebius/SWE-agent-trajectories` |
| Splits | `train` (仅一个) |
| 总记录数 | 80,036 条轨迹 |
| 唯一 instance_id | 3,591 个（同一问题有多个 agent 尝试） |
| Resolved (target=True) | 13,389 (16.7%) |
| Unresolved (target=False) | 66,647 (83.3%) |
| 模型分布 | llama-70b: 74,792 / llama-8b: 4,053 / llama-405b: 1,191 |
| 子集文件 | `artifacts/data/swe_agent_trajectories_1000.jsonl` (68.4 MB, 1000条) |

## 2. 顶层字段

每条记录包含 **7 个字段**：

| 字段 | 类型 | 说明 |
|------|------|------|
| `instance_id` | `str` | SWE-bench 问题 ID，格式 `{repo_owner}__{repo}-{issue_number}`，如 `AnalogJ__lexicon-336` |
| `model_name` | `str` | 使用的模型，`swe-agent-llama-70b` / `swe-agent-llama-8b` / `swe-agent-llama-405b` |
| `target` | `bool` | **最终是否解决了问题**。`True` = resolved，`False` = unresolved |
| `trajectory` | `list[dict]` | 交互轨迹序列，每个元素是一个 step（见下文） |
| `exit_status` | `str` | 退出状态：`submitted` (74%) / `submitted (exit_context)` (24%) / `exit_context` (2%) |
| `generated_patch` | `str` 或 `None` | agent 生成的最终 diff patch（unified diff 格式），7% 为空 |
| `eval_logs` | `str` 或 `None` | SWE-bench 评估日志（含 patch apply + 测试运行结果），7% 为空 |

## 3. 轨迹序列结构 (`trajectory`)

### 3.1 Step 字段

每个 step 是一个 dict，包含 **5 个固定字段**：

| 字段 | 类型 | 说明 |
|------|------|------|
| `role` | `str` | `system` / `user` / `ai` |
| `text` | `str` 或 `None` | step 的文本内容（action 或 observation） |
| `mask` | `bool` | `True` 表示该 step 是 AI 生成的（`ai` role 始终为 True） |
| `cutoff_date` | `str` 或 `None` | 仅 system step 有值（如 `01.01.2023`），其余为 None |
| `system_prompt` | `str` 或 `None` | 仅 system step 有值（SWE-agent 的系统提示词，~4873 chars），其余为 None |

### 3.2 轨迹模式

一条轨迹的 role 序列始终为：

```
system → user → ai → user → ai → user → ai → ... → ai
```

- **Step 0** (`system`): 系统提示词，`text` 为空/None，实际内容在 `system_prompt` 字段
- **Step 1** (`user`): Issue 描述 + 指令，格式为 "We're currently solving the following issue... ISSUE: ... INSTRUCTIONS: ..."
- **Step 2+** (`ai` / `user` 交替): agent action 和环境 observation 交替出现

### 3.3 轨迹长度统计（1000 条子集）

| 指标 | 值 |
|------|-----|
| 最短 | 3 steps |
| 最长 | 699 steps |
| 中位数 | 35 steps |
| 平均值 | 55.3 steps |
| Step 文本平均长度 | ~1,102 chars |
| Step 文本最大长度 | ~16,000 chars |

### 3.4 AI Step (Action) 格式

AI step 的 `text` 包含两部分：
1. **思考/推理文本**（自然语言）
2. **命令**（包裹在 ``` 代码块中）

示例：
```
To start solving this issue, we need to reproduce the error first.

\```
lexicon memset create example.com TXT --name _acme-challenge.example.com --content BLAH --ttl 300
\```
```

常见命令类型：
- `open <path>` / `goto <line>` / `scroll_down` / `scroll_up` — 文件导航
- `edit <start>:<end>\n<content>\nend_of_edit` — 编辑文件
- `search_dir <term>` / `search_file <term>` — 搜索
- `find_file <name>` — 查找文件
- `submit` — 提交最终修改
- 标准 bash 命令（`ls`, `cat`, `python`, `pytest` 等）

**100% 的 AI step 都包含代码块**（命令是通过代码块传递的）。

### 3.5 User Step (Observation) 格式

User step 的 `text` 是环境返回的 observation，常见格式：

- **文件内容显示**: `[File: /path/to/file.py (N lines total)]` 后跟带行号的代码
- **命令输出**: 标准 stdout/stderr 输出
- **错误信息**: Python traceback, 编译错误等
- **状态行**: `(Open file: /path) (Current directory: /repo) bash-$`

34% 的 observation 包含 `[File:` 文件显示，25% 包含错误信息，100% 以 `bash-$` 结尾。

## 4. 标签信息

### 4.1 Resolved/Unresolved 标签

- **字段**: `target` (bool)
- **True** = 问题成功解决（通过 SWE-bench 评估验证）
- **False** = 未解决
- **分布**: 16.7% resolved / 83.3% unresolved

### 4.2 Exit Status

| 状态 | 含义 | 占比 |
|------|------|------|
| `submitted` | agent 正常提交 patch | ~74% |
| `submitted (exit_context)` | agent 超出上下文窗口后被强制提交 | ~24% |
| `exit_context` | agent 超出上下文但未提交 | ~2% |

## 5. 中间产物

### 5.1 生成的 Patch (`generated_patch`)

- 标准 unified diff 格式（`diff --git a/... b/...`）
- 可以直接用 `git apply` 应用
- 平均长度 ~1,392 chars，最大 ~16,126 chars
- 7% 为空（agent 未成功生成 patch）

### 5.2 评估日志 (`eval_logs`)

包含 SWE-bench 的完整评估流程，结构化为几个阶段：

```
1. Apply prediction patch:  "git apply -v /swebench_matterhorn/prediction_patch.patch"
2. Apply test patch:        "git apply -v /swebench_matterhorn/test_patch.patch"
3. ___ENVIRONMENT_SET_UP_PATCH_APPLIED___
4. Run tests:               "pytest --no-header -rA --tb=no ..."
5. ___TESTS_SECTION___
   ... pytest 输出（PASSED/FAILED 列表）...
   ___TESTS_SECTION_END
```

**测试结果解析方法**：
- 定位 `___TESTS_SECTION___` 和 `___TESTS_SECTION_END` 之间的文本
- 每行 `PASSED tests/...` 或 `FAILED tests/...` 表示单个测试结果
- 最终汇总行如 `5 failed in 0.54s` 或 `20 passed in 1.2s`

### 5.3 轨迹内的测试运行

agent 在轨迹中间也可能运行 `pytest`，输出出现在 `user` step 的 observation 中。格式与标准 pytest 输出一致，但**不带 `___TESTS_SECTION___` 标记**。

### 5.4 文件修改（在轨迹中）

agent 使用 `edit` 命令修改文件，下一个 observation 会显示修改后的文件内容。可以通过追踪所有 `edit` 命令来重建文件修改历史。最终的完整 diff 在 `generated_patch` 字段中。

### 5.5 没有的信号

- **无 linter 输出**：除非 agent 主动运行 linter
- **无结构化 code quality 指标**
- **无中间 checkpoint/状态快照**

## 6. 对 Labeling Function 实现的影响

### 6.1 `file_diff_delta` — 代码变更信号

**主数据源**: `generated_patch` 字段
- 直接可用的 unified diff 格式
- 可解析出：修改的文件列表、添加/删除行数、涉及的函数/类

**辅助数据源**: 轨迹中的 `edit` 命令
- 可以在每个 step 级别追踪代码变更的增量
- 需要解析 AI step 中的 `edit <start>:<end>` 命令格式

### 6.2 `test_pass_rate_transition` — 测试结果转变

**主数据源**: `eval_logs` 字段
- 解析 `___TESTS_SECTION___` ... `___TESTS_SECTION_END` 区间
- 提取 PASSED/FAILED 计数
- 这是**最终**测试结果（agent 提交后的评估）

**辅助数据源**: 轨迹内的 pytest 输出
- agent 可能在轨迹中间运行测试（出现在 `user` step 中）
- 可以追踪测试通过率随时间的变化（transition）
- 需要用正则匹配 pytest 输出格式：`N passed`, `N failed`, `PASSED`, `FAILED`

**注意**: 不是所有轨迹都有中间测试运行，取决于 agent 的行为策略。

### 6.3 `outcome_backpropagation` — 结果回传

**数据源**: `target` 字段（bool）
- 直接获取，无需解析
- `True` = resolved，可以作为正样本
- `False` = unresolved，负样本

**增强信号**:
- `exit_status` 可区分 "正常提交但失败" vs "超时/上下文溢出"
- `eval_logs` 中的测试结果可提供更细粒度的"接近成功"信号（如 5 个测试通过了 4 个）

## 7. 数据质量观察

1. **同一 instance 多次尝试**: 80,036 条轨迹对应 3,591 个唯一问题，平均每个问题 ~22 次尝试。建议按 `instance_id` 分组分析。
2. **模型不均衡**: 93.5% 是 llama-70b 的轨迹，8b 和 405b 样本较少。
3. **空值处理**: `generated_patch` 和 `eval_logs` 各有 ~7% 为空，需要在处理时跳过。
4. **text 字段 None**: system step 的 `text` 为 None（内容在 `system_prompt` 中），以及少数异常 step 的 `text` 可能为 None。
5. **轨迹长度差异极大**: 3 到 699 步，长轨迹可能对应 context overflow 的情况。
6. **子集前 1000 条是按 instance_id 排序的**，前 11 条都是同一个 issue (AnalogJ__lexicon-336)，数据分布并非随机。后续分析建议 shuffle 或按 instance_id 采样。
