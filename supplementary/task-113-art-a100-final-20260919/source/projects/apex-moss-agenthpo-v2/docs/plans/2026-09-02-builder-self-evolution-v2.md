# Moss v2：Builder 自进化实验方案

## 目标

在 `v1` 的 Builder→Task Harness 流程上增加第二个进化层：Builder 不仅修改下层
`TaskHarness`，还可以修改自己生成、诊断、记忆和搜索的策略。实验要测量的是
Builder 产生后续改进的能力，而不是让 Builder 修改评分器。

v2 首个实现采用 typed `BuilderArtifact`，不执行模型生成的 Python 控制器源码。
它把 HyperAgents/DGM-H 的可编辑 meta-agent 思路映射到固定 schema 的策略对象，
为后续受沙箱约束的可执行插件保留升级路径。

## 组件边界

```text
Immutable Controller
  ├── evaluator / hidden labels
  ├── schema and codec minimums
  ├── sandbox and network policy
  ├── operation journal and budget
  └── gate and promotion authority

BuilderArtifact B_t
  ├── task_harness_policy       # 如何生成下层 Harness
  └── meta_policy                # 如何分析、记忆和搜索下一版 Builder

TaskHarness H_t
  └── Solver -> external evaluator -> public projection
```

Builder 只能通过严格的 `BuilderSelfModificationProposal` 修改自身的 typed
`meta_policy`。任何涉及 evaluator、hidden data、budget、gate、sandbox 或
operation journal 的字段都不在 artifact schema 中，不能被提案表达。

## 单轮流程

1. Controller 从 archive 选择一个 Builder parent，并绑定任务快照、seed 和预算。
2. Builder 用当前 `task_harness_policy` 生成下层 Harness，运行固定 Solver/evaluator。
3. Builder 只读取公开分数、reason-coded failure、结构哈希、成本和有限历史摘要。
4. Builder 提交一份完整的 self-modification proposal，修改 `meta_policy` 或
   `task_harness_policy`，并逐字绑定 `base_builder_sha256`。
5. Controller 做 schema、allowlist、预算和 immutable-boundary 检查；失败提案只封存，
   不重试、不消费新的 solution/evaluator 机会。
6. 通过的子代进入不可覆盖 Builder archive；Controller 继续执行外部 gate 和 promotion。

## 可变 meta-policy

v2 允许的自修改字段为：

- `diagnostic_focus`：失败、分数趋势、结构差异、成本等公开视图；
- `memory_views`：current、best、failures、structural-diverse、builder-history；
- `mutation_families`：repair、discipline、restart、recombine、workflow；
- `search_mode`：explore、exploit、explore-then-exploit；
- `parent_selection`：best、lineage-diverse、score-child-balanced；
- `stagnation_window` 和 `exploration_rate`；
- `proposal_budget`：每轮允许的候选数量上限；
- `failure_recovery`：preserve、repair、reset。

这些字段只改变 Builder 的公开上下文和下层 Harness proposal 行为。它们不能
改变 evaluator、评分含义、任务划分或外层 archive/promotion 算法。

## 对照与指标

每个 Builder 在相同 task/seed/模型/预算下运行：

- `fixed-builder`：`v1` Builder，meta-policy 不变；
- `self-evolving-builder`：Builder 可修改 typed meta-policy；
- `self-evolving-no-archive`：只保留最新 Builder，检验 stepping-stone archive；
- `transferred-builder`：从任务族 A 冻结后迁移到任务族 B。

主要指标：

```text
BuilderImp@k(B) =
  B 在 k 次 Harness 机会内产生的最佳有效分数
  - 同一起点 Harness 的有效基线分数
```

同时报告 Harness 正确率、有效率、模型调用、evaluator 交易、CPU/GPU 成本、
Builder 提案拒绝率和跨任务迁移结果。只看最高分不足以晋升 Builder；必须同时
满足可信提升、足够有效率和 immutable-boundary 全部通过。

## 泛化协议

在开发任务族上进化 Builder 后，冻结 Builder artifact、Controller、Registry、
prompt contract 和预算，在未见任务族上重新运行。新任务失败只能产生 typed
`rejected`/`environment_invalid` 证据，不允许原地修改并继续计入同一正式比较。
正式声明跨任务元改进前，至少需要新任务族的独立重复和 paired `BuilderImp@k`。

## 安全与可复现性

- Builder artifact、proposal、parent link、公开输入 projection 和结果全部内容寻址；
- started-without-result 永久计费，不重发；
- evaluator、hidden labels、budget ledger、gate 和 promotion 由 Controller 独占；
- v2 默认 compile-only/fake-provider 验证，不授权正式模型或 evaluator 调用；
- 后续若开放可执行 self-modifier，必须新增受限 ABI、沙箱、静态策略和独立 canary，
  不能把任意仓库写权限直接交给 Builder。

## 成功标准

v2 的第一阶段只在离线/合成 provider 上证明：

1. Builder self-modification proposal 可严格解析、内容寻址和恢复；
2. 不可修改边界无法通过 proposal 绕过；
3. archive 可重放并按 `BuilderImp@k` 计算；
4. fixed-builder 与 self-evolving-builder 的差异可在零新增外部调用下审计。

这份方案本身不授权生产执行；正式实验需要另行冻结 task、provider、entitlement
和 canary receipt。
