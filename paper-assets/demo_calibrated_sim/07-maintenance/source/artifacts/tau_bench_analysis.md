# τ-Bench Retail 环境调研笔记

## 1. 整体架构

τ-Bench 模拟三方交互循环：**User (LLM simulated)** ↔ **Agent (被评估)** ↔ **Tools (环境 API)**

```
┌─────────────┐     respond      ┌──────────┐    tool_call     ┌──────────┐
│ User Sim    │ ◄──────────────► │  Agent   │ ◄─────────────► │  Env/DB  │
│ (LLM+prompt)│   observation    │ (被测模型)│   observation    │  (mock)  │
└─────────────┘                  └──────────┘                  └──────────┘
```

核心文件结构：
- `tau_bench/envs/base.py` — Env 基类，包含 reset/step/calculate_reward
- `tau_bench/envs/user.py` — User simulator（多种策略：llm/react/verify/reflection）
- `tau_bench/envs/retail/` — Retail domain（env、tools、tasks、wiki、rules、data）
- `tau_bench/agents/` — Agent 实现（tool_calling、react、few_shot）
- `tau_bench/run.py` — 主运行逻辑，多线程并发执行
- `tau_bench/types.py` — 所有数据类型定义

## 2. Retail 任务列表

**任务数量**：test=115, train=500, dev=20

任务类型覆盖（从 instruction 模式归纳）：
| 类别 | 说明 | 典型 actions |
|------|------|-------------|
| Exchange | 已送达订单换货（不同选项） | find_user → get_order → get_product → exchange_delivered_order_items |
| Return | 已送达订单退货 | find_user → get_order → return_delivered_order_items |
| Cancel | 取消待处理订单 | find_user → get_order → cancel_pending_order |
| Modify Items | 修改待处理订单商品选项 | find_user → get_order → get_product → modify_pending_order_items |
| Modify Address | 修改待处理订单地址 | find_user → get_order → modify_pending_order_address |
| Modify Payment | 修改待处理订单支付方式 | find_user → get_order → modify_pending_order_payment |
| Info Query | 查询产品/订单/用户信息 | find_user → list_all_product_types / get_product_details |
| Composite | 多个任务组合（查询+退货，换货+地址修改等） | 上述组合 |

每个 Task 包含：
- `user_id`: 用户标识
- `instruction`: 用户角色扮演指令（含身份、目标、偏好、性格）
- `actions`: ground-truth 动作序列（用于评估）
- `outputs`: 可选的期望文本输出（如数字答案）

## 3. 对话格式

### Agent 消息格式（OpenAI tool calling 标准）

```python
# System message = wiki.md（零售客服策略文档）
{"role": "system", "content": "<wiki.md 内容>"}

# User message（来自 user simulator）
{"role": "user", "content": "Hello! I'd like to exchange..."}

# Agent response（纯文本回复）
{"role": "assistant", "content": "I can help you with that..."}

# Agent response（工具调用）
{"role": "assistant", "content": null, "tool_calls": [{
    "id": "call_xxx",
    "type": "function", 
    "function": {"name": "get_order_details", "arguments": "{\"order_id\": \"#W2378156\"}"}
}]}

# Tool result
{"role": "tool", "tool_call_id": "call_xxx", "name": "get_order_details", "content": "{...json...}"}
```

**关键约束**：Agent 每次只能做一个动作——要么回复用户，要么调用工具，不能同时。

### 对话终止条件
- User simulator 发送 `###STOP###`（任务完成）
- Agent 调用 `transfer_to_human_agents`（放弃/转人工）
- 达到 `max_num_steps=30`

## 4. User Simulator 实现

### 核心实现：`LLMUserSimulationEnv`（文件：`tau_bench/envs/user.py`）

**System prompt 模板**：
```
You are a user interacting with an agent.

Instruction: <task.instruction 的完整内容>

Rules:
- Just generate one line at a time to simulate the user's message.
- Do not give away all the instruction at once. Only provide the information that is necessary for the current step.
- Do not hallucinate information that is not provided in the instruction.
- If the instruction goal is satisfied, generate '###STOP###' as a standalone message.
- Do not repeat the exact instruction in the conversation. Instead, use your own words.
- Try to make the conversation as natural as possible, and stick to the personalities in the instruction.
```

**对话初始化**：
- System prompt 设好后，第一条 user message 是固定的 `"Hi! How can I help you today?"`（agent 的开场白，作为 user 视角的 input）
- User simulator 基于此生成第一条用户消息

**四种策略**：
| 策略 | 说明 |
|------|------|
| `llm` | 直接用 LLM 生成用户消息 |
| `react` | LLM 先生成 Thought，再生成 User Response（Thought 不发给 agent） |
| `verify` | 生成后用另一次 LLM 调用验证质量，不满意则重新生成（最多 3 次） |
| `reflection` | verify 失败后还会反思并生成改进版（最多 2 轮） |

### task.instruction 示例

```
"You are Yusuf Rossi in 19122. You received your order #W2378156 and wish to 
exchange the mechanical keyboard for a similar one but with clicky switches and 
the smart thermostat for one compatible with Google Home instead of Apple HomeKit. 
If there is no keyboard that is clicky, RGB backlight, full size, you'd go for 
no backlight. You are detail-oriented and want to make sure everything is 
addressed in one go."
```

instruction 包含：身份信息 + 具体目标 + 条件分支（fallback 偏好）+ 性格特征。

## 5. Tool Calling 接口

### Retail 可用工具（16个）

| 工具名 | 功能 | 是否修改数据库 |
|--------|------|---------------|
| `calculate` | 计算器 | 否 |
| `cancel_pending_order` | 取消待处理订单 | 是 |
| `exchange_delivered_order_items` | 已送达订单换货 | 是 |
| `find_user_id_by_email` | 通过邮箱查用户 | 否 |
| `find_user_id_by_name_zip` | 通过姓名+邮编查用户 | 否 |
| `get_order_details` | 查订单详情 | 否 |
| `get_product_details` | 查产品详情（含所有变体） | 否 |
| `get_user_details` | 查用户信息 | 否 |
| `list_all_product_types` | 列出所有产品类型 | 否 |
| `modify_pending_order_address` | 修改待处理订单地址 | 是 |
| `modify_pending_order_items` | 修改待处理订单商品 | 是 |
| `modify_pending_order_payment` | 修改待处理订单支付 | 是 |
| `modify_user_address` | 修改用户默认地址 | 是 |
| `return_delivered_order_items` | 已送达订单退货 | 是 |
| `think` | 内部思考（不影响环境） | 否 |
| `transfer_to_human_agents` | 转人工（终止对话） | 否 |

工具参数格式遵循 OpenAI function calling schema：
```python
{
    "type": "function",
    "function": {
        "name": "get_order_details",
        "description": "Get the status and details of an order.",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string", "description": "..."}},
            "required": ["order_id"]
        }
    }
}
```

每个工具实现为 `Tool` 子类，`invoke(data, **kwargs)` 直接操作内存中的 mock 数据库。

## 6. 评估指标

### 评估机制：规则判定（非 reward model）

`Env.calculate_reward()` 在 `base.py:124-164`：

**两阶段判定**：

1. **数据库状态比对 (r_actions)**：
   - 重放 ground-truth actions 到干净数据库，得到 `gt_data_hash`
   - 将 agent 实际产生的数据库状态 `data_hash` 与之比较
   - 不匹配 → reward=0

2. **输出文本检查 (r_outputs)**（可选）：
   - 检查 `task.outputs` 中的每个期望输出是否出现在 agent 的 respond 消息中（不区分大小写子串匹配）
   - 任一缺失 → reward=0

**Pass^k 指标**：
- 同一任务跑 k 次 trial
- Pass^k = 在 k 次 trial 中全部成功的任务比例（组合计数估计）
- 核心指标：Pass^1（单次成功率）

**历史数据（gpt-4o-retail）**：460 条轨迹，115 任务 × 4 trials，成功 278/460（60.4%）

## 7. 对话 Trace 数据结构

### EnvRunResult（每条 trace 的顶层结构）

```python
{
    "task_id": 0,           # 任务索引
    "reward": 1.0,          # 0.0 或 1.0
    "trial": 0,             # 第几次 trial
    "info": {
        "task": {
            "user_id": "yusuf_rossi_9620",
            "instruction": "You are Yusuf Rossi in 19122...",
            "actions": [...],       # ground-truth action 序列
            "outputs": []           # 期望文本输出
        },
        "source": "user",           # 最后一个 observation 来源
        "user_cost": 0.0024475,     # user simulator API 费用
        "reward_info": {
            "reward": 1.0,
            "info": {
                "r_actions": 1.0,           # 数据库状态是否正确
                "gt_data_hash": "d43e..."   # ground-truth 数据库哈希
            },
            "actions": [...]        # ground-truth actions（不含 respond）
        }
    },
    "traj": [               # 完整消息列表
        {"role": "system", "content": "# Retail agent policy\n..."},
        {"role": "user", "content": "Hello! I recently received..."},
        {"role": "assistant", "content": "I can help you..."},
        {"role": "assistant", "tool_calls": [...]},
        {"role": "tool", "tool_call_id": "...", "name": "...", "content": "..."},
        ...
    ]
}
```

### traj 消息类型

| role | 含义 | 关键字段 |
|------|------|---------|
| `system` | Agent 的 system prompt（wiki.md） | `content` |
| `user` | User simulator 生成的消息 | `content` |
| `assistant` | Agent 回复或工具调用 | `content`（回复时）/ `tool_calls`（调用时） |
| `tool` | 工具返回结果 | `tool_call_id`, `name`, `content` |

## 8. 对 DemoCalib 项目的启示

### Hook 注入点

1. **User Simulator 替换/包装**：`LLMUserSimulationEnv` 是最关键的注入点。可以：
   - 继承 `LLMUserSimulationEnv`，在 `build_system_prompt()` 中注入行为校准 prompt
   - 在 `generate_next_message()` 前后添加行为指纹提取逻辑
   - 替换整个 user simulator 为 RL-trained 的策略

2. **Agent 包装**：`ToolCallingAgent.solve()` 是完整的 agent 交互循环。可以：
   - 在 `completion()` 调用前后 hook，记录/修改 agent 的 prompt 和输出
   - 在 `env.step()` 前后 hook，拦截 action 和 observation

3. **Env.step() 包装**：可以在 `base.py:Env.step()` 中注入：
   - 中间 reward 信号（不只在对话结束时计算）
   - 行为指纹收集（tool call 模式、错误恢复模式等）

4. **Reward 扩展**：`calculate_reward()` 当前是 binary（0/1）。可以：
   - 添加中间 reward（部分正确的 action 给部分分数）
   - 添加效率 reward（更少步骤完成 → 更高分）
   - 添加 cost-aware reward（考虑 API 调用成本）

### 行为指纹提取要素

从 traj 可以提取的信号：
- **Tool call 序列**：哪些工具、什么顺序、参数是否正确
- **对话轮数**：完成任务需要多少轮
- **错误模式**：是否调用了错误工具、参数错误、遗漏步骤
- **信息泄露**：user simulator 是否过早给出全部信息
- **确认模式**：agent 是否在修改数据库前征求确认
- **回退行为**：找不到信息时 agent 如何处理

### 关键注意事项

- **评估是确定性的**：基于数据库哈希比对，不是 LLM 判断，这使得 RL reward 信号干净可靠
- **User simulator 的随机性是主要方差来源**：同一任务不同 trial 结果可能不同，因为 user simulator 的 LLM 采样不同
- **task.instruction 包含 fallback 逻辑**：部分任务有条件分支（"如果没有 X，就选 Y"），这增加了对话的复杂性
- **train split 是 synthetic 生成的**：500 个 train 任务的 annotator="synthetic"，instruction 格式更简单直接，可用于训练
- **test split 是人工标注的**：115 个 test 任务的 annotator="0"/"1"/...，instruction 更自然复杂
