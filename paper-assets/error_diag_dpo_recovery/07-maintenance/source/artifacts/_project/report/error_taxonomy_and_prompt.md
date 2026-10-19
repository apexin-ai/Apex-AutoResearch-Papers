# ETADN Error Taxonomy for ALFWorld

## 1. 三分类 Taxonomy 定义

### 1.1 Action Error（动作执行错误）

**定义**: Agent 在单步动作选择上犯错——目标对象、目标容器或动作动词本身不正确，但其整体策略和步骤规划是合理的。纠正只需替换该步动作的参数或动作类型。

**ALFWorld 典型表现**:
1. **拿错物品**: 任务要求 "put a pencil on desk"，agent 执行 `take pen 1 from drawer 1`（pencil vs pen 混淆）
2. **去错容器实例**: 需要去 `countertop 2` 但去了 `countertop 1`（同类容器的实例选择错误，agent 知道要去 countertop 但选错了编号）
3. **动作动词错误**: 需要 `open fridge 1` 才能取出物品，但直接执行 `take apple 1 from fridge 1`（忘记先 open）
4. **对象不存在**: 执行 `take mug 3 from shelf 1` 但该位置只有 mug 1 和 mug 2
5. **use 错误对象**: 在 examine 任务中，`use desklamp 1` 时手里拿着错误的物品

**与其他类的区分标准**:
- Action error 的特征是 **策略正确、执行偏差**：agent 知道该做什么（如"去拿杯子"），但具体操作的参数选错了
- 与 Verification error 的区别：action error 不涉及状态检查的缺失，而是动作本身就选错了
- 与 Planning error 的区别：如果 agent 选择了完全错误的步骤序列（如在 clean 任务中尝试 heat），那是 planning error；但如果策略正确只是拿错物品，就是 action error

---

### 1.2 Verification Error（验证确认错误）

**定义**: Agent 未验证关键前置条件或动作结果，导致在错误状态上继续执行。错误的根因不是动作选择本身，而是缺少必要的状态检查步骤——如果 agent 在关键节点进行了验证，本可以及时发现并纠正问题。

**ALFWorld 典型表现**:
1. **未确认持有状态**: `take mug 1 from countertop 1` 实际失败了（环境返回 "Nothing happens"），但 agent 没有识别失败信号，继续执行 `go to sinkbasin 1` 准备清洗——此时手中并没有 mug
2. **未确认清洗/加热/冷却结果**: 执行 `clean mug 1 with sinkbasin 1` 后未检查是否成功，直接进入 put 阶段
3. **未检查容器内容物**: 去了正确的 receptacle，但没有 `examine` 或 `open` 就尝试 take，结果物品不在该位置；如果先检查就能提前换目标
4. **重复动作不自知**: 执行 `go to shelf 1` 返回 "Nothing happens"（因为已经在 shelf 1），agent 再次执行同一动作而非分析原因
5. **忽略环境反馈**: 环境返回 "You need to open the cabinet first" 之类的提示，agent 未解读此反馈继续执行不可能成功的动作

**与其他类的区分标准**:
- Verification error 的特征是 **信息可得但未获取/未利用**：环境已经给出了足够的反馈信号，agent 未能正确解读或未主动查询
- 与 Action error 的区别：action error 是"做错了"，verification error 是"不知道自己做错了"或"不检查就往下走"
- 与 Planning error 的区别：verification error 的计划本身可能是对的，只是缺少验证步骤导致错误级联；planning error 则是策略/步骤顺序本身有问题

---

### 1.3 Planning Error（规划策略错误）

**定义**: Agent 对任务的整体策略或步骤序列存在根本性错误——要么遗漏了关键子目标，要么子目标的顺序/组合不正确，要么对任务目标本身的理解有偏差。纠正需要修改多个步骤或重新规划整个序列。

**ALFWorld 典型表现**:
1. **遗漏关键子任务**: Clean & Place 任务中，agent 直接 take → put，完全跳过了 clean 步骤
2. **子任务顺序错误**: Heat & Place 中先去放置位置再去加热，导致需要二次搬运（或者根本没意识到要先加热）
3. **错误搜索策略**: 需要找 mug，但 agent 从不太可能的位置开始搜索（如先搜 bathtub），浪费大量步数后 max_steps 超限
4. **任务目标误解**: 任务要求 "put a clean mug in cabinet"，agent 理解成只需 put（不 clean）或 put 到了错误类型的容器
5. **Pick Two 策略缺失**: puttwo 任务需要找并放置两个同类物品，但 agent 只规划了一个物品的流程，完成第一个后不知所措

**与其他类的区分标准**:
- Planning error 的特征是 **方向性错误**：即使每一步执行完美、验证充分，仍然无法完成任务，因为步骤序列本身就是错的
- 与 Action error 的区别：planning error 涉及多步的策略问题，不是单步参数选错；改一步解决不了问题
- 与 Verification error 的区别：planning error 即使加上验证步骤也不能自愈，因为计划本身走不通

---

## 2. Failure Pattern → Error Type 映射表

| Failure Pattern | 主要映射 | 条件映射 | 判定规则 |
|----------------|---------|---------|---------|
| `wrong_object` | **Action** | — | Agent 的搜索策略和目标容器都正确，仅物品选择错误（如 pencil vs pen）。这是典型的单步参数错误。 |
| `wrong_receptacle` | **Action** / **Planning** | 取决于错误性质 | **Action**: agent 知道要去某类容器但选错了实例编号（`shelf 1` vs `shelf 2`）——单步修正即可。**Planning**: agent 去了完全错误类型的容器（任务要求放 `desk` 但去了 `shelf`），说明对目标位置的理解有误，属于策略层错误。**判定方法**: 检查错误容器与目标容器是否同类（同类 → Action，异类 → Planning）。 |
| `missing_step` | **Planning** | — | 遗漏 clean/heat/cool 等关键子任务，属于对任务分解的根本性遗漏。agent 不是做错了一步，而是根本没有规划该步骤。这是典型的策略层错误，纠正需要插入整个子任务序列（go to sink → clean → go to target）。 |
| `repeated_action` | **Verification** | **Planning** (退化情况) | **Verification**（主要）: agent 重复执行同一动作，未检查环境反馈（"Nothing happens"）或未识别失败信号，缺乏状态验证导致无效循环。**Planning**（退化）: 如果 agent 在正确识别失败后仍无法生成替代方案而持续重试，则退化为 planning error——agent 没有 fallback 策略。**判定方法**: 检查重复动作间是否有 thought 变化。有 thought 变化但仍重复 → Planning（知道失败但无替代方案）；无 thought 变化或直接重复 → Verification（未识别失败）。 |
| `max_steps_exceeded` | **Planning** | **Action** (少数情况) | **Planning**（主要）: 搜索策略低效（遍历大量不相关位置）或子任务分解导致步骤冗余，40 步预算耗尽。属于规划效率问题。**Action**（少数）: 如果 agent 策略正确但因 1-2 个 action error 导致需要额外步骤修正从而超限，则根因是 action error。**判定方法**: 分析轨迹是否在正确方向上推进。如果 agent 一直在有效搜索只是位置太多 → Planning（搜索策略问题）；如果 agent 离完成只差 1-2 步 → Action（临门一脚的执行错误累积）。 |
| `parse_error` | **Action** | — | Agent 输出格式不符合 `Thought: ...\nAction: ...` 规范，或生成了不存在的动作名称。这是执行层面的错误——agent 无法正确生成可被环境解析的动作字符串。映射为 action error 因为这是单步输出格式问题，与策略和验证无关。 |

### 条件映射的自动判定算法

对于 `wrong_receptacle` 和 `repeated_action` 等条件映射，分类 prompt 需要执行以下判定：

```
wrong_receptacle:
  IF target_receptacle.type == actual_receptacle.type:
    → Action Error (实例选错)
  ELSE:
    → Planning Error (容器类型错)

repeated_action:
  IF agent_thought_changes_between_repeats:
    → Planning Error (知道失败但无替代方案)
  ELSE:
    → Verification Error (未识别失败)

max_steps_exceeded:
  IF steps_remaining_when_on_track <= 3:
    → Action Error (执行偏差累积)
  ELSE:
    → Planning Error (策略效率问题)
```

---

## 3. Zero-shot LLM 分类 Prompt 模板

```
You are an expert at analyzing agent failure trajectories in ALFWorld, a text-based household environment. Your task is to classify the root cause of a failed trajectory into exactly one of three error types.

## Error Type Definitions

### Action Error
Single-step execution mistakes where the agent's overall strategy is sound but a specific action parameter is wrong.
- Picking up the wrong object (e.g., pen instead of pencil)
- Going to the wrong instance of the correct receptacle type (shelf 1 instead of shelf 2)
- Using an invalid action verb or format (parse errors)
- The hallmark: fixing ONE step would have led to success

### Verification Error
The agent fails to check preconditions or action outcomes, causing error cascading from undetected failures.
- Proceeding after a failed "take" action without noticing "Nothing happens"
- Not confirming whether clean/heat/cool succeeded before moving on
- Repeating the same failed action without reading environment feedback
- The hallmark: the agent HAD the information (or could have obtained it) but did not use it

### Planning Error
Fundamental flaws in the task strategy or step sequence that cannot be fixed by correcting a single action.
- Skipping a required subtask entirely (e.g., forgetting to clean in a Clean & Place task)
- Searching for objects in highly unlikely locations, wasting steps
- Misunderstanding the task goal (e.g., ignoring the "clean" requirement)
- Having no fallback strategy when the primary approach fails
- The hallmark: even with perfect single-step execution and verification, the plan would not succeed

## Classification Rules

1. **Root cause principle**: When multiple error types are present, classify by the EARLIEST error that caused the failure cascade. Later errors are often consequences of the root cause.

2. **Conditional mappings**:
   - `wrong_receptacle`: If the agent went to the wrong TYPE of receptacle → Planning. If wrong INSTANCE of the correct type → Action.
   - `repeated_action`: If the agent shows no awareness of failure (no thought change) → Verification. If aware but has no alternative → Planning.
   - `max_steps_exceeded`: If the agent was on track and within 3 steps of completion → Action. If the search strategy was fundamentally inefficient → Planning.

3. **Tie-breaking**: Planning > Verification > Action. If genuinely ambiguous, the deeper structural error takes precedence.

## Task Context

ALFWorld has 6 task types:
- Pick & Place: take object → put in receptacle
- Clean & Place: take object → clean at sinkbasin → put in receptacle
- Heat & Place: take object → heat at microwave → put in receptacle
- Cool & Place: take object → cool at fridge → put in receptacle
- Examine in Light: take object → use desklamp
- Pick Two & Place: repeat pick-and-place for two objects of the same type

## Your Analysis Process

Analyze the following failed trajectory step by step:

1. **Identify the task type** from the initial observation (which of the 6 types?)
2. **Identify the required steps** for this task type (what should the agent have done?)
3. **Find the failure point** — the first step where things went wrong
4. **Determine why** — was it a wrong parameter (Action), missing check (Verification), or wrong strategy (Planning)?
5. **Check for root cause** — trace backward from the failure: is the identified error the root cause, or a symptom of an earlier error?

## Trajectory to Classify

{trajectory}

## Output Format

Respond with ONLY a JSON object, no other text:

```json
{
  "error_type": "action|verification|planning",
  "failure_step": <step number where the root cause error first occurs>,
  "failure_pattern": "wrong_object|wrong_receptacle|missing_step|repeated_action|max_steps_exceeded|parse_error",
  "reasoning": "<2-3 sentences: what the agent should have done vs what it did, and why this constitutes the classified error type>"
}
```
```

### Prompt 使用说明

**输入格式**: `{trajectory}` 占位符替换为完整的多轮交互记录，格式如下：

```
Task: put a clean mug in cabinet.

Step 1:
Observation: You are in the middle of a room. Looking quickly around you, you see a countertop 1, a cabinet 1, ...
Thought: I need to find a mug, clean it, and put it in the cabinet.
Action: go to countertop 1

Step 2:
Observation: On the countertop 1, you see a mug 1, a knife 2, ...
Thought: I see a mug. Let me take it.
Action: take mug 1 from countertop 1

...
[FAILED after step N]
```

**调用建议**:
- 使用 temperature=0 保证分类一致性
- 对同一轨迹可多次采样（temperature=0.3, n=3）取多数投票提高鲁棒性
- Prompt 长度约 800 tokens，加上轨迹通常总计 2000-4000 tokens，适合 Qwen3-8B 的上下文窗口

---

## 4. 纠正跨度假设与 γ_e 建议

### 4.1 Correction Horizon 定义

**Correction Horizon**（纠正跨度）= 纠正该错误所需的**最少步数**，即从错误发生点出发，采取最优纠正策略到达正确状态所需的最少动作数。注意这不是两条轨迹的 edit distance，而是纠正的最小代价。

示例：
- **Action error**: 纠正只需 1 步（换正确物品）→ horizon ≈ 1
- **Verification error**: 需要插入检查步 + 可能的补救步 → horizon ≈ 2-4
- **Planning error**: 需要从分叉点重新规划整个后续序列 → horizon ≈ 5-15+

### 4.2 γ_e 的物理含义：DMPO 时间折扣因子

γ_e **不是** DPO 的 β 参数。γ_e 是 DMPO（Discounted Markov Preference Optimization）长度归一化公式中的**时间折扣因子**，出现在信用分配权重函数中：

```
φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
```

其中 t 是当前时间步，T 是轨迹总长度。φ(t,T) 决定了每个时间步在偏好 loss 中分配到多少信用（credit）。

**γ 的作用**：
- **γ 接近 1**（如 0.97）：信用分布趋于均匀，意味着纠正需要影响更多步骤（长跨度）。适合需要重新规划整个序列的 planning error
- **γ 远离 1**（如 0.85）：信用集中在纠正步附近的早期步骤（短跨度）。适合只需局部修正的 action error

**核心论点**：纠正跨度越长的错误类型，需要越均匀的信用分布（γ 越接近 1），以确保梯度信号覆盖到所有需要修正的步骤。因此 γ_e 应与 correction horizon 正相关。

#### Action Error → 短纠正跨度 → γ ≈ 0.85

- **纠正方式**: 替换 1 个动作的参数（对象名称、容器编号等）
- **Correction horizon**: ≈ 1 步
- **信用分配需求**: 信用只需集中在错误步附近，不需要传播到远处。较小的 γ 使 φ(t,T) 在纠正步处权重最大，远离纠正步的步骤权重快速衰减，避免在不需要改变的步骤上产生不必要的梯度

#### Verification Error → 中等纠正跨度 → γ ≈ 0.92

- **纠正方式**: 在关键节点插入验证动作（examine/check），并基于验证结果调整后续动作
- **Correction horizon**: ≈ 2-4 步（插入验证 + 条件分支 + 补救）
- **信用分配需求**: 信用需要跨越验证检查序列——从"应该插入验证的位置"到"基于验证结果的补救动作"。中等 γ 使信用在这个窗口内有效传播

#### Planning Error → 长纠正跨度 → γ ≈ 0.97

- **纠正方式**: 重新规划步骤序列，可能涉及添加/删除/重排多个子任务
- **Correction horizon**: ≈ 5-15+ 步（从分叉点到任务完成的整个后续序列）
- **信用分配需求**: 信用必须均匀分布在整个重规划轨迹上，因为每一步的改变都对最终成功有贡献。接近 1 的 γ 使 φ(t,T) 近似均匀，确保长距离的策略重构获得充分的梯度信号

### 4.3 γ_e 建议值

| Error Type | γ_e 范围 | 推荐初始值 | 理由 |
|-----------|---------|-----------|------|
| Action | 0.80 – 0.88 | **0.85** | 短跨度纠正，信用集中在错误步附近。γ=0.85 时 φ 在 5 步外衰减到 ~44%，有效限制了信用传播范围。 |
| Verification | 0.88 – 0.95 | **0.92** | 中等跨度，信用需跨越验证-补救序列（2-4 步）。γ=0.92 时 φ 在 10 步外衰减到 ~43%，覆盖典型验证跨度。 |
| Planning | 0.95 – 0.99 | **0.97** | 长跨度，信用需覆盖整个重规划序列。γ=0.97 时 φ 在 20 步外仍保持 ~54%，确保长距离策略重构获得梯度。 |

### 4.4 γ_e 值的理论约束

1. **单调性约束**: γ_action < γ_verification < γ_planning（这也是 P1 验证的核心假设）
2. **下界**: γ_e ≥ 0.80，低于此值信用衰减过快，即使是短跨度纠正也可能丢失相邻步的梯度信号
3. **上界**: γ_e ≤ 0.99，γ→1 时 φ(t,T) 退化为均匀分布，失去按错误类型区分信用分配的能力
4. **P1 MVP gate**: correction_horizon(action) < correction_horizon(verification) < correction_horizon(planning)，p < 0.05

### 4.5 超参搜索策略

建议分两阶段：

**阶段 1: 验证跨度假设（不训练）**
- 用 LLM 分类器对 ETO 收集的失败轨迹进行分类
- 对每类错误，计算 correction horizon = 纠正该错误所需的最少步数
- 验证 P1 假设：correction_horizon(action) < correction_horizon(verification) < correction_horizon(planning)，p < 0.05

**阶段 2: γ_e 网格搜索**
- 搜索空间 γ ∈ [0.80, 0.99]
- 固定 γ_action = 0.85（锚点）
- 搜索 γ_verification ∈ {0.88, 0.92, 0.95}
- 搜索 γ_planning ∈ {0.95, 0.97, 0.99}
- 评估指标：ALFWorld test set 成功率 + 各任务类型成功率分解
- 共 9 个组合，每个约需 1 轮 DMPO 训练（~2-3 小时 on 2×RTX 4090D）

### 4.6 与 ETO 迭代的交互

ETADN 中 γ_e 可能需要随迭代调整：

- **iter1**: 使用建议初始值（action=0.85, verification=0.92, planning=0.97）
- **iter2+**: 各 γ_e 可向 1.0 方向微调（如 +0.02），但保持单调性且不超过 0.99
- 直觉：后续迭代中 agent 已学会避免简单错误，剩余错误更集中在难纠正的类型，需要更均匀的信用分布

---

## 附录 A: ALFWorld 任务类型与典型错误分布预估

| 任务类型 | 典型 Action Error | 典型 Verification Error | 典型 Planning Error |
|----------|------------------|------------------------|-------------------|
| Pick & Place | 拿错物品/去错实例 | 未确认 take 成功 | 搜索策略低效 |
| Clean & Place | 拿错物品 | 未确认 clean 成功 | **跳过 clean 步骤** |
| Heat & Place | 拿错物品 | 未确认 heat 成功 | **跳过 heat 步骤** |
| Cool & Place | 拿错物品 | 未确认 cool 成功 | **跳过 cool 步骤** |
| Examine in Light | 拿错物品 | 未确认手持物品 | use 错误灯具 |
| Pick Two & Place | 拿错物品 | 未确认第一个已放好 | **只规划了一个物品** |

**预估分布**（基于 ETO 论文中 ALFWorld ~50% 成功率的 SFT 模型）:
- Action Error: ~40%（最常见，尤其在简单任务中）
- Verification Error: ~25%（中等频率，尤其在多步任务中）
- Planning Error: ~35%（missing_step 在 clean/heat/cool 任务中频发）

实际分布需从 ETO exploration 数据统计验证。

---

## 附录 B: 分类质量评估计划

在将 LLM 分类器用于 DPO 训练数据标注前，需要评估分类质量：

1. **人工标注**: 从每个任务类型随机抽取 10 条失败轨迹（共 60 条），由 LLM 多模型/多 temperature 交叉验证（如 Qwen3-14B + GPT-4o，temperature 0.0/0.3/0.7 各 3 次），计算一致性
2. **LLM vs 人工**: 同一 60 条数据用 Prompt 模板分类，计算与人工标注的 agreement
3. **目标**: Cohen's κ ≥ 0.6（substantial agreement），LLM-人工 agreement ≥ 70%
4. **迭代优化**: 如果分类质量不达标，分析 confusion matrix 调整 prompt 中的定义和判定规则
