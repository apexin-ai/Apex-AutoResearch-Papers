# AgentHPOBench on Moss v2：Vast.ai 执行与 L1 Harness 设计

状态：设计冻结草案；尚未启动正式模型或 evaluator 调用。

基线：`apex-moss` `codex/agenthpo-v2-moss`，来源 `origin/v2`，commit
`b3bdb192de1254c7f1146af148ee3cfa833b5539`。

## 目标与边界

目标是在 AgentHPOBench 官方 1 次 baseline + 5 次 sequential intervention
协议下，测试 Moss v2 的 L1 Harness 和 typed BuilderArtifact 是否能提高最终
第五次结果，并在同一模型、任务版本、evaluator、预算和硬件下与固定对照比较。

L1 只改变公开证据的整理、诊断顺序、候选生成/筛选、探索与利用路由、失败恢复
和终局选择。Builder 不得修改 evaluator、hidden labels、任务划分、预算账本、
gate、sandbox、模型身份或评分公式。不得把任务答案、私有日志、后题反馈或隐藏
标签写入 BuilderArtifact。

## 官方任务闭环

```text
source-locked task card
  -> baseline evaluator
  -> public feedback projection
  -> L1 Builder/Harness decision
  -> strict typed configuration codec
  -> one intervention evaluator transaction
  -> receipt + public history
  -> repeat exactly five times
  -> final-step score and best-so-far diagnostic
```

模型明确返回当前合法配置时，记录为 `explicit_keep`，并执行一次官方干预。
解析失败后的程序补旧配置属于 `fallback`，必须计为失败证据，不能静默修复。
free-form room-selector 任务在专用 codec 完成前不进入正式 scalar 结果。

## L1 适配设计

每个任务的公开状态固定为：

```text
task_card, current_config, current_training_state,
best_observed_config, metric_direction, metric_history,
train_validation_gap, recent_trend, failure_category,
tested_configs, remaining_interventions, execution_mode
```

L1 Harness 只允许以下可变点：

- `diagnostic_focus`
- `memory_views`
- `mutation_families`
- `search_mode`
- `parent_selection`
- `stagnation_window`
- `exploration_rate`
- `proposal_budget`
- `failure_recovery`

每轮只执行一个候选配置。候选可以先生成 4–8 个，但候选生成本身不计作
evaluator 结果；所有真实评估必须占用五个 intervention 槽位。第五轮默认采用
保守的可靠配置或显式 keep，不为了信息价值进行无依据的大范围探索。

## 实验矩阵

第一阶段只比较三臂：

| 臂 | 行为 |
|---|---|
| A-fixed | v2 固定 Builder/Harness，使用官方公开反馈 |
| A+select | 固定流程，增加显式终局选择/keep |
| B-targeted | v2 L1 Builder 根据公开证据动态选择诊断、搜索和恢复流程 |

稳定后再加入 `B-self`：每个源题完成后，由 typed
`BuilderSelfModificationProposal` 生成 child artifact；题后才原子提交，后续
任务加载 child。Builder 更新成本和失败提案都计入模型预算。

开发集使用 D11，T12 只在 artifact、prompt、模型、预算和 adapter 冻结后运行。
Q7 只做资格和环境检查，不能用来反复挑选策略。公开对榜需要完整 30-task
canonical run；D11 的调参和轨迹不应被描述为独立 SOTA 结果。

## 模型与预算

正式对齐公开 limited-budget 结果时，首选 Claude Sonnet 4.6 API；Builder 和
Solver 第一版使用同一模型以便归因。Moss v2 的 `gpt-5.6-sol` 只作为离线和
工程 canary，除非另行冻结对照协议。

正式合同必须记录：模型 ID、provider/base URL、temperature、最大输出 token、
超时、重试策略、请求/响应原文、输入输出 token、客户端版本和时间戳。

开发起点上限：每题最多 20 次物理模型请求、80k 总 token、5 次真实干预；
正式 30-task 运行前重新按官方 API/本地模型协议校准并冻结。Builder 额外调用
不能从 evaluator 预算中隐式扣除，也不能无账本重试。

## Vast.ai 资源方案

Vast.ai 只负责 evaluator 运行资源，模型通过 API 调用。推荐正式起点：

- Linux Ubuntu 22.04/24.04
- 1×H200（优先；论文实验可见显存约 143 GB）
- 32 vCPU、128 GB RAM、1 TB NVMe
- Conda/micromamba、Docker/OCI 可选
- 固定 NVIDIA/CUDA 驱动、可访问 Hugging Face/数据源和模型 API

小规模 qualification 可先用 1×A100 40/80 GB 或 H100、16 vCPU、64 GB RAM、
300–500 GB NVMe，但不能据此承诺全 30 题成功。任务串行执行、每题独立环境；
记录显存峰值、CPU RSS、磁盘、baseline 时长、每个 intervention 时长和环境失败。

只读报价预检入口为 `scripts/vast_agenthpo_preflight.py`。2026-09-10 公共报价中，
满足至少 80 GB VRAM、64 GB RAM、300 GB 磁盘的可见 H100 候选为 H100 NVL，约
40 effective CPU、315 GB RAM、2.8 TB 磁盘，价格约 1.98–2.07 USD/hour；当前
未发现满足同样筛选条件的公开 H200/A100 候选。报价会变化，正式租用前必须重新执行
预检并把 offer id、价格、硬件和镜像 digest 写入本次 campaign manifest。

需要用户另提供或在本机安全注入 Vast.ai API key。模型 key 与 Vast key 分离：
模型 key 只通过进程环境变量传入，禁止写入 Git、实验 receipt、prompt、Builder
artifact 或聊天记录。当前用户提供的 `https://api.apexin.ai` key 仅用于模型 API，
不作为 Vast.ai 控制面凭据。

## 合规与反作弊证明

每次正式运行必须封存：

1. Moss commit、AgentHPO commit/root tree、任务 runner 和 manifest hash；
2. task card、公开 projection、配置、原始模型响应和 token receipt；
3. baseline + 五次 intervention 的完整顺序；
4. evaluator transaction 与 provider request 一一对应；
5. fallback、格式错误、环境错误和中断，不转换成零分；
6. hidden evaluator 输入只存在 controller-private 区域；
7. BuilderArtifact parent/child hash、加载 receipt 和实际生效 Harness fingerprint；
8. 官方 `validate_results.py` 与 `summarize_multiseed.py` 的输出。

不得使用后题信息、隐藏标签、gold 配置、缓存污染、额外训练步数、额外 evaluator
probe、修改评分器或改变官方任务预算。任何疑似泄漏都使该 cell 失效并停止后续
执行，保留证据，不重跑覆盖。

## 卡顿与架构问题处理

连续两次同一类卡顿或门控失败时，先冻结该 lane，保存最后可靠 receipt 和完整
输入，再用 Stanford AI Agent skill 的长程依赖/回滚模块诊断：依赖是否齐备、节点
是否可逆、是否需要 checkpoint、是否错误地把局部成功合并为全局成功。若问题属于
推理预算或候选选择，再使用验证约束下的预算模块。

每个问题写入 issue ledger，至少包含：复现 task/round、输入与 artifact hash、
失败阶段、原始异常、影响范围、最小修复假设、是否改变核心语义、验证命令和结果。
只允许修改 L1 适配或可信 runtime；不得通过放宽 evaluator、hidden data、预算、
gate 或 sandbox 边界来修复。修复后先跑离线 fixture、negative canary 和单题 smoke，
再恢复正式 lane。

## 放行条件

在以下条件全部满足前，不启动正式 30-task 刷榜：

- v2 offline BuilderArtifact/runtime 全部回归通过；
- AgentHPO source-lock、task card 和 strict codec replay 通过；
- explicit keep、unknown key、越界、重复 key、malformed JSON negative canary 通过；
- Vast 机器完成 baseline 与至少两个 qualification task smoke；
- provider/evaluator journal 能证明 exact-once 或明确计费恢复；
- Q7 完整 1+5 轨迹能通过官方结果校验；
- D11/T12 分割、模型配置和反作弊投影已冻结。

正式 SOTA 目标是同协议 final MBNS 超过公开 0.407，同时 B-targeted/B-self 必须
超过 A+select 才能把增益归因于 Moss，而不是归因于模型或最后一步保留策略。
