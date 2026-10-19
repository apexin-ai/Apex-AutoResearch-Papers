# B-self：可执行 Builder 脚手架实现方案

## 目标

Builder 与 Task Harness 的架构变化都只修改内容寻址 artifact，不修改 Python 控制器源码。
Python 只保留固定 schema、compiler、runtime、archive、evaluator、budget、gate 和 sandbox 权限。

## 表示

现有 `BuilderArtifact` 已包含两层外部脚手架：

- `meta_policy`：决定 Builder 看哪些公开诊断/记忆、采用哪类 mutation、搜索阶段、提案槽位和失败恢复；
- `task_harness_policy`：决定下层 Task Harness 的 role graph、memory、tools、parent、workflow、scheduler、recovery 和 execution mode。

不引入模型生成的 Python，也不新增仓库写权限。Builder child 仍是完整 typed artifact，绑定 parent hash。

## 固定编译流程

新增 `BuilderScaffoldCompiler`，将 `BuilderArtifact + BuilderPublicState` 编译成
`CompiledBuilderScaffold`：

1. 按 `diagnostic_focus` 选择公开诊断字段；
2. 按 `memory_views` 选择公开 memory bucket；
3. 根据公开失败、score trend、`search_mode`、`exploration_rate` 和稳定哈希选择 mutation family；
4. 将 mutation family 机械映射为下层 rule/parent/workflow/recovery 变化；
5. 将 `proposal_budget` 展开为显式 proposal slot；
6. 将 `failure_recovery` 编译成 preserve/repair/reset action；
7. 输出完整 `HarnessDecision` 和内容哈希。

同一 artifact、task、round 和公开状态必须得到逐字相同的 compiled scaffold。

## Runtime 接线

`HarnessRuntime.run_round()` 增加可选 `builder_artifact` 与 `builder_public_state`：

- 没有 BuilderArtifact 时保持 v1 行为；
- 有 BuilderArtifact 时先编译 scaffold，再把精确 compiled projection 交给 planner；
- planner 返回的 HarnessDecision 必须落在 compiled scaffold 允许的 role/memory/tool/workflow 边界内；
- 下层 runtime 仍由 `TrustedOperatorRegistry` 执行；
- evaluator、hidden data、预算和 gate 永不进入 Builder artifact。

## 自进化链路

题后 Builder 只读取公开 score/feedback/state，产生完整 child proposal。Controller 严格校验后：

1. 保存 child artifact；
2. 保存 parent/proposal/child transition；
3. 原子推进 head；
4. 下一题重新编译 child，因此架构变化由 Python runtime 机械生效，而不是只写进 prompt。

## 本轮范围

- 实现 compiler、compiled receipt、下层 decision 机械派生和 runtime 可选接线；
- 增加 deterministic、allowlist、proposal slot、failure recovery 和 runtime enforcement 测试；
- 保持正式 provider/evaluator 未授权，不启动 benchmark；
- operation journal 与跨题 campaign 的 production 接线留到后续独立冻结。

