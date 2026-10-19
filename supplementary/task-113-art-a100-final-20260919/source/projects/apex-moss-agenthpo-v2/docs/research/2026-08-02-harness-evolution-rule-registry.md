# Harness 进化规则一手来源审计

本报告只吸收可归因的控制规则，不把某个项目在单一任务上的数值、候选代码或品牌结论复制为 Moss 的经验。固定检查日期为 2026-08-02。

## 结论

真正直接改变 Agent/Harness 的公开实现较少：DGM 会改 coding agent 源码，ADAS 生成完整 agent workflow，AFlow 搜索 workflow graph 与 prompt。OpenEvolve、AIDE 等主要进化的是任务解或实验代码，只能借用搜索调度原语，不能作为“HarnessBuilder 已被证明有效”的证据。

Rule Registry 与 TrustedOperatorRegistry 必须分开：前者描述触发条件和 typed effect，后者冻结真正执行 effect 的代码。任务专属数值进入有 scope 的 Experience Record，不进入通用规则正文。

## 已固定的一手来源

| 来源 | 固定版本 | 实际变异对象 | 可借规则 | 采用边界 |
|---|---|---|---|---|
| Apex-Tune v9 | [`17223eec`](https://github.com/apexin-ai/Apex-Tune/tree/17223eec6f7c29490888a278c86122e9f9f070ad) | solution 与搜索控制面；Harness meta-loop 主要仍是 roadmap | discipline、dream、law inversion、recombination；stagnation rebalance；leader follow-up；QD archive | 不复制 NanoChat 阈值、候选、分数或“verified”结论；documented-but-unwired 行为不算实现证据 |
| DGM | [`a565fd2d`](https://github.com/jennyzzt/dgm/tree/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2) | coding agent 自身源码、工具与 workflow | 父代质量与已育子代数平衡；父子 outcome 记忆；开放档案 | 外层 archive maintenance 与 parent selection 仍固定，不能声称 search policy 全自改 |
| ADAS | [`2702bee8`](https://github.com/ShengranHu/ADAS/tree/2702bee8fefda42255efc5be9f60e3bd3db96ae4) | 完整 agent workflow forward | workflow graph 作为 genotype；archive 中完整 agent 作为父代 | 只注册声明式 graph/template 组件，不允许模型生成任意可执行 plugin |
| AFlow | [`3f457218`](https://github.com/FoundationAgents/AFlow/tree/3f457218fc716093fe53f6df8a5d5e6379d66346) | workflow graph 与 prompt | workflow-graph mutation；搜索树/验证反馈 | MCTS 参数不跨任务照搬；必须在固定 validation 上选择、fresh test 上评价 |
| AIDE | [`5d66a217`](https://github.com/WecoAI/aideml/tree/5d66a21771e98623dc9fc8716bdbe388d63464c0) | 任务 solution/实验代码 | draft/debug/greedy improve 三态搜索 | 属于 solution evolution 原语；计分从候选 stdout 抽取，不能迁移 evaluator 合同 |
| OpenEvolve | [`411fb59c`](https://github.com/codelion/openevolve/tree/411fb59c886c18704caaffb611e17cf9e7d824d2) | 任务 program/solution | MAP-Elites、island migration、top candidates、staged evaluation | 结构新颖度只能辅助分配，不能越过正确性和可信评分 |

## 进入 v1 Rule Registry 的规则

### Apex 来源

- `discipline`：证据支持单一瓶颈时，沿 incumbent 做一个可证伪的有限改动。
- `dream`：局部家族饱和时从冻结 root 重建设计。
- `law_inversion`：连续失败共享同一假设时，显式反转该假设。
- `recombination`：重组两个冻结、互补的父版本，child 从零评分。
- `successor_followup`：新 leader 出现后，给其相邻机制一个预算内 follow-up。
- `stagnation_rebalance`：冻结 epoch 后才重配探索/利用比例。

### 其他实现来源

- `failure_directed_mutation`：吸收 DGM 的失败类型路由，但只传 typed taxonomy；format/compile/correctness/performance 失败分别处理，不能把所有失败都当作“换性能方向”。
- `parent_fertility_balance`：父代选择同时考虑质量与已育子代数，避免单一 leader 无限繁殖。
- `workflow_graph_mutation`：角色拓扑、步骤依赖和模板一起成为 typed genotype，但只能引用可信组件。
- `archive_reflection`：吸收 ADAS 的全档案反思，再对当前父子关系做局部、可证伪更新；反思调用同样计费。
- `archive_diversity`：保留机械结构 niche 的 elite/bridge，而不只保留最快候选。
- `progressive_evaluation`：先便宜合同/正确性 gate，再运行昂贵性能评测。
- `cross_instance_distillation`：当前 instance 首次见面轨迹封存后，才产生下一代经验。

## 不注册或降级的项目

- AlphaEvolve、普通 AIDE/AIRA、AI Scientist 的主要贡献是 solution/idea evolution，不登记成“直接 Harness 自进化证据”。
- 只有论文主张、缺少可核对实现的 Meta-Harness、Self-Harness、STOP、AIDE² 等先进入 research backlog，不进入 v1 trusted rule。
- DGM 的 full-eval、ADAS retry、部分 model-merge 或 prior 权重若在固定代码中未真正消费，标为 `documented_unwired`，不能进入 runtime。
- 任意模型自报的 novelty、机制标签或适用范围只作 annotation；调度只信机械 descriptor 和可信 outcome。

## Shadow Registry：后续晋级候选

以下规则已有源码证据，但当前 v1 runtime 尚未逐项实现，所以只在轨迹中 shadow-log，不能让模型选择一个实际无语义的标签。只有离线重放一致、预算闭合且跨多个封存 instance 显示正向证据后，才可进入下一版 TrustedOperatorRegistry。

| 候选规则 | 一手实现 | 准备加入的机械语义 | 当前不直接启用的原因 |
|---|---|---|---|
| top-S mixed-softmax parent | AFlow `3f45721` | top-S 中加入固定均匀探索质量，再按 validation softmax 选父 | 需先冻结尺度、温度和 RNG；否则同一分数在不同 benchmark 上含义不同 |
| parent-edge outcome memory | AFlow `3f45721` | 存 father、canonical typed diff、before/after、success；按 diff hash 去重 | 原仓库把成功与失败都格式化为禁止项，必须重写 memory projector |
| one-component bounded mutation | AFlow `3f45721` | 每次仅改一个 genotype field group，并限制结构距离 | 原实现靠 Prompt 限制五行，不是机械边界 |
| score/child-count parent balance | DGM `a565fd2` | 质量权重除以 `1+有效子代数`，固定 RNG | 原仓库 `best` 分支和 argparse 有 bug，需只实现经测试的公式 |
| archive-reflect-twice | ADAS `2702bee` | 全档案反思一次、父局部反思一次，再提交 typed proposal | 多两次模型调用，必须先做 call-matched 价值验证 |
| cascade promotion | OpenEvolve `411fb59` / DGM `a565fd2` | static→correctness→performance 分级晋级，后级失败保留前级事实 | 当前 evaluator 已有固定 gate；要先证明新增 rung 不引入异尺度平均与预算偏置 |
| island MAP-Elites | OpenEvolve `411fb59` | 外置机械 descriptor 映射 cell；同 cell 只留高 fitness；周期迁移按 genotype hash 去重 | 24 题首轮规模过小，直接启用会把大种群成本混入 Builder 泛化结论 |
| Pareto parent mix | AlphaEvolve Google Cloud client `b51ab7a` | Moss 自行实现 non-dominance、方向统一和确定性 tie-break | 官方仅公开 schema，服务端父选择实现不可核验 |

AlphaEvolve engine 与 Sakana Evolutionary Model Merge 的搜索实现并未公开；相关 README 或结果表不作为“已核对算法”。AFlow 的精确冻结停止、ADAS 的 `n -= 1` retry/错误 percentile、DGM private-test diagnosis，以及任何从候选 stdout 读分的实现明确拒绝迁移。

## Experience Record 的长期积累

每条经验必须记录 instance descriptor、Builder 版本、初始 Harness 结构、rule trigger、typed action、结果增量、正确性、资源、反例、scope 和 ledger event IDs。晋级顺序为：单 instance 观察 → 同 benchmark 重复 → 跨 benchmark 重复 → trusted default prior。未达到跨 benchmark 支持的规则可以检索，但不能成为所有新任务的默认先验。
