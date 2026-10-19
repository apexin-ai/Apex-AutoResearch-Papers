# Moss 通用 Builder 与 Agent Task Harness V2 设计

日期：2026-08-28  
状态：用户已确认，进入实现

## 1. 目标

Moss 的核心结构边界固定为：

- 上层 `Builder Harness` 跨题目保持固定，泛化的是“如何根据现场证据指导下层进化”。
- 下层 `Task Harness` 在单个 instance 内持续变化，目标是越来越适合当前 instance。
- `Solver` 是被 Task Harness 调用的模型，不等同于 Task Harness。
- Python Runtime 负责受控执行、权限、审计、恢复和官方 evaluator 调用，不替 Builder 决定架构。

主版本默认只启用当前 instance 的单题 Memory。跨题 Memory 默认关闭，只能在明确标记的 B-online 实验中开启。

## 2. 当前实现缺口

### 2.1 正式 Builder 看不到历史 Harness 完整结构

通用 `HarnessWorkspace.inspect()` 已能列出历史 Harness，但正式 Experiment 1 使用的
`experiment_one_builder_view()` 目前只暴露当前 Harness，以及历史运行的 Harness hash、分数、反馈和节点元数据。
这导致 Builder 无法可靠比较“哪种结构变化带来了哪种分数变化”。

### 2.2 下层仍是顺序节点图，不是完整工具型 Agent Harness

当前 V2 已支持 `model_call`、固定 `tool_call`、`skill_call` 和 `emit`，但 Solver 不能在运行时根据题目状态自主选择直接作答、调用工具、进入多阶段工作流，或者根据公开检查继续修复。本次在现有 `TaskHarnessArtifact` 内扩展 `model_call` 的动态 tool 策略，不建立第二套 Agent/Solver artifact。

### 2.3 多模型节点的审计编号冲突

正式运行中，同一轮的多个 Solver 模型节点复用了相同的 audited operation id。第一个模型节点完成后，第二个节点会因 operation id 已存在而失败。V1 和 V2 都必须修复。

## 3. 不变的实验语义

### 3.1 Builder 泛化，Task Harness 专门化

同一个 Builder Harness 面对不同 instance 时读取统一现场信息，并可以提出完全不同的 Task Harness 改法。Builder 本身不在单题八轮中修改结构或提示。Builder 使用同一套通用流程：

```text
inspect → diagnose/propose → validate → probe → commit/rollback
```

### 3.2 B-Frozen

B-Frozen 的每个新 instance 使用同一个固定 Builder 模型、Builder Harness 和初始 Builder 指令，创建新的 Task Harness 谱系和空的单题 Memory，只读取该 instance 自己谱系的历史。它不读取先前 instance 的提炼经验、Harness、分数、反馈或轨迹。

B-Frozen 验证固定 Builder 是否具有现场适应能力。

### 3.3 B-online

B-online 在 B-Frozen 的单题 Memory 之外，额外读取经过清洗的跨题经验。跨题经验只能保存通用改造规律，不能包含具体候选答案、其他 instance 的完整 Task Harness、隐藏测试、私有 evaluator 信息，或者可以还原其他 instance 的数据。

B-online 验证前面题目的进化经验能否帮助后续题目更快、更稳定地完成专门化。

## 4. Builder 可见的单题 Memory

正式 Builder 视图新增 `available_harnesses`，每一项只来自当前 instance 的当前实验线路，并包含实际执行过、被提案、被拒绝或被 rollback 的 Harness。它不能只沿当前 Harness 的 parent 链回溯，否则从旧版本分支后会丢失已经执行过的历史 Harness。

每一项包含：

- Harness 完整公开 spec；
- Harness sha256、schema version、版本号和 parent sha256；
- 是否为当前 Harness；
- 使用该 Harness 的公开运行结果：run id、公开分数、公开反馈和公开状态；
- Builder 提案的 source/base/candidate/next Harness hash；
- 提案结果：commit、reject 或 rollback；
- 下一轮是否实际采用该 Harness；
- 不含输入输出正文的公开节点执行摘要。

Builder 仍然看不到：

- Solver 候选答案正文；
- 原始模型输出、节点输入输出正文或模型内部思维过程；
- 隐藏答案、隐藏测试和 evaluator 私有字段；
- 其他 A/B/C 线路或其他 instance 的 workspace；
- Builder 审计账本中的密钥、原始请求和私有响应。

所有数据在进入 Builder 前由 Python 构造新的 JSON 副本；Builder 不能通过引用修改 workspace 数据。

## 5. Agent Task Harness V2

### 5.1 兼容方式

- 保留现有 `workflow-only-v1`，旧 artifact、receipt 和实验结果继续可回放。
- 新 artifact 使用明确的 V2 schema 和内容寻址 hash。
- V1 不在读取时被静默改写为 V2。
- 新实验 manifest 明确声明所用 Harness schema，旧冻结 manifest 不修改。

### 5.2 V2 定义的能力

V2 Task Harness 至少定义：

- Agent 的角色与任务指导；
- 执行模式：`direct`、`agent_loop`、`workflow` 或 `auto`；
- 工具 allowlist/denylist；
- 可选工作流及其选择规则；
- 模型调用、工具调用、时间和输出大小预算；
- 停止条件和失败恢复规则；
- 当前 instance 内的 session memory 策略；
- benchmark 输出合同绑定；
- schema version、artifact version、parent hash 和内容 hash。

V2 继续使用以下已有执行单元：

- `model_call`：一次固定模型调用，或在节点明确开启时运行受限的动态 tool 循环；
- `tool_call`：Harness 强制执行的固定工具调用；
- `skill_call`：加载或执行一个允许的 benchmark/contract Skill；
- `emit`：提交最终候选。

工作流不是新的节点类型，而是由 router 和 Workflow Registry 对现有节点的执行顺序进行受控组织。这样 Builder 改动的仍然是同一份 Task Harness 结构。

### 5.3 Solver 与 Builder 的决定边界

Builder 可以改变 Task Harness 提供的工具、默认执行模式、可选工作流、阶段和信息流、角色、指导、预算、停止条件和恢复规则。

Solver 可以在当前 Task Harness 允许的范围内决定直接作答还是调用工具、调用哪个已允许工具、选择哪个已允许工作流，以及根据工具结果继续、修复或停止。Solver 不能自行扩大工具权限、预算、网络范围或 evaluator 权限。

## 6. 工具插件层

工具通过统一 Registry 注册，每个工具声明稳定名称、版本、输入输出 schema、权限、超时、输出大小、调用次数上限、是否修改 workspace，以及可审计的执行 receipt。

首批通用工具目标为：`list_files`、`read_file`、`search_text`、`write_file`、`apply_patch`、`run_command`、`compile` 和 `run_public_tests`。每个 benchmark 只启用适用的子集，并可增加 benchmark 专用只读或受控工具。工具不能提交或评分候选；唯一权威候选来自 Task Harness 的最终 `emit`。如果 workflow 同时暂存候选文件，Runtime 必须验证文件 hash 与 `emit` 内容 hash 一致，否则 fail closed。

以下能力永不进入 Solver 工具箱：官方或私有 evaluator、隐藏测试和答案、其他谱系 workspace、Builder 内部账本、无限制宿主机文件系统和无限制网络。

公开测试可以在 Agent Loop 内调用。官方评分 evaluator 必须在最终候选产生后，由外部 controller 每轮调用一次。controller artifact root、Solver 可见 scratch root 和 evaluator private root 必须物理分离，Solver 工具只绑定 scratch root。

## 7. 工作流插件

V2 首批提供三个有边界的通用工作流：

1. `direct_solve`：适合不需要工具的短任务。
2. `inspect_plan_execute`：先检查公开上下文，再计划和执行。
3. `implement_test_repair_verify`：实现、运行公开测试、修复并最终验证。

工作流不是写死给所有题使用。`auto` 模式用一次受审计、计入模型预算的 Solver 路由动作，从 Builder 允许的工作流集合中选择；Python 只校验选择是否合法并执行。Builder 可以在下一轮改变集合或默认选择。

## 8. 审计、operation id 与恢复

每次模型或工具调用使用唯一且可重放的 operation id，至少绑定：

```text
experiment + benchmark + instance + seed + round
+ Harness hash + node id/agent step + call index + layer
```

要求：

- 同一轮不同模型节点不得复用 operation id；
- 相同 operation id 必须绑定相同请求 hash；
- 已开始但没有持久结果的外部调用继续 fail closed，不自动 retry；
- API、Solver、格式、Harness 门禁和 evaluator 错误不得转换为 0 分；
- round receipt 记录实际使用的 Harness、Builder 提案、commit/reject/rollback 和下一轮实际 Harness；
- replay 不重新发起已经完成的模型、工具或 evaluator 调用。

## 9. Responses 工具调用兼容

实现前先对 `LLM_BASE_URL` 做低成本协议 canary，检查是否完整返回 Responses API 的 function/tool-call 事件。

- 若支持，使用原生 Responses tool calling。
- 若不支持，使用严格的单 JSON tool-action 协议；Python 校验 action schema 后执行工具，并将结果作为下一步输入。
- 两种 transport 对 Task Harness 的语义、权限、预算和审计保持一致，transport 差异写入 receipt。

transport protocol 由 campaign canary 在正式运行前冻结，是 Runtime 配置而不是 Builder 可进化的 Harness 字段；Builder 提案不得切换它。

## 10. Gate 原则

Gate 只保留通用可执行和安全要求：

- schema 合法、引用存在、最终只有一个有效 emit；
- 至少存在一条能产生候选的路径；
- 工具、权限、预算和工作流均来自 manifest 白名单；
- 输出合同不可被 Harness 删除或覆盖；
- 不读取其他谱系和私有 evaluator 数据；
- 结构可被确定性编译和回放。

Gate 不限制合理的模型调用总数为很小的固定值；实际边界由 manifest 的资源预算和服务器限制决定。

## 11. 实现顺序

1. 为当前 V1 修复多模型节点 operation id 冲突，并添加回归测试。
2. 为正式 Builder 视图加入同谱系历史完整 Harness，以及隔离和防泄漏测试。
3. 加入 B-Frozen/B-online 显式 memory mode；默认 `instance_only`。
4. 定义并解析 Agent Task Harness V2，同时保持 V1 回放兼容。
5. 实现 Agent Loop、工具 Registry、权限和预算执行。
6. 实现三个有边界工作流插件。
7. 为 EdgeBench 和 ALE-Bench 配置各自允许的工具包与输出合同。
8. 完善审计、receipt、replay、错误保留和跨谱系隔离测试。
9. 更新 README、TEST、CLAUDE 和实验 manifest 文档。
10. 本地测试后在 AWS 做 smoke test；通过后推送 `apexin-ai/apex-moss` 的 `main`。

## 12. 验收标准

代码完成必须同时满足：

- Builder 能查看当前 instance 同一谱系的 H0...Ht 完整公开结构，并能从历史 Harness 分支提出 Ht+1。
- B-Frozen 新题开始时跨题 Memory 为空，自动化测试证明不能读取其他题数据。
- B-online 只有显式开启后才能读取清洗后的通用经验。
- 至少一个测试证明 Builder 的结构提案被 commit，下一轮实际使用新 Harness，而非只记录提案。
- 多模型节点和 Agent Loop 的每次模型调用拥有不同 operation id，且可重放。
- Solver 能在同一 Task Harness 中分别走 direct、工具调用和有边界 workflow 路径。
- 官方 evaluator 始终位于 Agent Loop 外，每轮最多执行一次正式评分。
- 输出合同、工具权限、预算、谱系隔离和错误不转零均有自动化测试。
- 旧 V1 artifact 和 receipt 的读取与回放测试继续通过。
- EdgeBench 与 ALE-Bench smoke test 产生完整审计证据；遇到正式错误不自动 retry。

## 13. 不在本次范围内

- 单题内进化 Builder Harness 自身结构；
- 训练或微调 Builder 模型权重；
- 默认启用跨题经验共享；
- 让 Solver 访问官方 evaluator、隐藏测试或任意网络；
- 修改已经冻结的旧 Experiment 1 manifest 或覆盖旧实验结果。
