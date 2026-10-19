# Benchmark 资格预评测与 B-online 因果验证方案（2026-08-11）

> **状态（2026-08-13）：资格切分、四臂 typed 合同、source-bound 共享 v001 可信重编译、精确 1,566
> 评分槽与 4,338 个潜在外部阶段、typed outcome/中断、原始分数边界、canary/online 零调用计划，
> post-v001/Skill compile-only authority、source/codec static Q0 evidence，以及固定
> `formal_execution_ready=false` 的 semantic-only disposition fixture 已经实现；正式
> provider/operation-ledger/evaluator/report 调度、reference/environment/isolation evaluator
> canary、非零 entitlement 和执行授权
> 仍为 `NOT_READY/NOT_GRANTED`。没有调用模型、正式评测器或付费资源，也没有产生新实验分数。**
>
> 本文承接
> [`2026-08-06` 三臂正式报告](../reports/2026-08-06-harness-builder-cross-benchmark-final-report.md)
> 与
> [Self-Evolving AI 文献综述](../reports/2026-08-07-self-evolving-ai-systems-literature-review.md)。
> 它不续跑 `v1r8/v1r9`，不导入旧 Experience Bank，也不修改旧结果。

当前实现范围由后继
[`宽 Harness 与元机制执行合同`](2026-08-12-wide-harness-and-meta-mechanism-execution-contract.md)
进一步收窄：第一批只保留机制不同的 **AgentHPOBench + GDPevo**。BIRD-Interact、Atrex 和 OSWorld
仍是未授权 reserve，不进入当前零调用计划。旧 24 题结果只作历史证据；其 task、score、trajectory、
Harness、Skill 与 Experience 均不导入新实验。

---

## 0. 决策摘要

上轮失败不只是“题太简单”，而是把三个问题混在了一个三臂实验里：

1. Benchmark 是否还有足够 headroom，普通采样、反思或领域优化器是否已经能低成本刷高；
2. Moss 的收益是否来自 **Harness 架构重编译**，而不是更多模型调用、Prompt 反思或 Skill；
3. 在双方都允许题内优化时，跨题 Experience 是否给 B-online 带来独立增量。

下一步把它们拆成两个实验门：

| 实验门 | 首选 Benchmark | 主要问题 | 直接强对照 |
|---|---|---|---|
| **M：方法资格门** | [AgentHPOBench](https://github.com/OpenMOSS/AgentHPOBench/tree/6d8d90071cdb16b06f0db866480ecaae48880fba) | Moss 是否胜过普通 compute scaling、固定反馈 Agent 与传统 HPO | Random/TPE/BOHB、native fixed-feedback agent、CLI Harness |
| **M2：架构压力测试（条件项）** | [Atrex-Bench](https://github.com/alibaba/atrex-bench) | Moss 的结构化 Harness 是否胜过固定 profiler-reflection 和 AKA | vanilla、fixed profiler loop、[Atrex Kernel Agent](https://github.com/alibaba/atrex-kernel-agent) |
| **O：B-online 迁移门** | [GDPevo](https://github.com/Prism-Shadow/GDPevo/tree/0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4) | sealed 前题经验是否改善未见题 cold start，并增强题内 Harness 适应 | Skill-only/self/reflect、固定 memory、相同调用预算 |

首轮执行顺序建议固定为：

1. 对 AgentHPOBench、GDPevo 做零模型 source/合同 precheck；
2. 在资格集上运行低成本强基线，不运行 B-online；
3. 只有通过全部硬门禁的 Benchmark 才进入小型 held-out pilot；
4. Atrex 只有在目标 GPU、DSL、roofline 和 AKA 都能同预算复现后才加入，不用原 KernelBench
   的历史分数替代；
5. OSWorld 2.0 只保留为高成本外部确认项，首轮不直接消费其预算。

当前四臂不是旧三臂或下文早期 2×2 cell 的直接重命名。每个 `task×seed` 只生成、编译和评分一次共同
v001，再 fork 为：`A-fixed-feedback`、`S-reflection-skill`、`B-targeted` 与 `B-frozen-wide`。
A 只让 solution 使用原生反馈；S 只更新当前题内的 typed 文本 Skill；B-targeted 每个 v002+ 至少改变
一个可执行 Harness 轴；B-frozen-wide 每个 accepted v002+ 必须让 role、memory、tool、parent、
workflow、scheduler、recovery 七轴全部实质变化，并由可信 factory 重新实例化七类 typed 运行组件。
这里的“重装”是 Harness 运行对象与配置的重新构建，不是 OS/Python 包重装，也不开放 Registry、
evaluator、scorer 或预算。

B-online 小试也不再只等同于 Experience Bank：`OM` 保存内容寻址机制记忆，`OP` 更新 typed
meta-policy，`OA` 更新 typed Harness recipe/archive。三者借鉴 HyperAgents 的 archive、stepping-stone
和“优化改进过程”思路，但状态彼此隔离，只能引用 trusted Registry 中的对象；不得保存或执行任意代码，
也不得修改模型与评分协议。

评分边界也已类型化：AgentHPOBench 与 GDPevo 的 evaluator 原始分数分别保持各自原生量纲，报告只允许
输出 raw score；为兼容现有正值优化器而做的 affine utility 只在内部使用，不能当成归一化成绩。typed
score artifact 已能离线校验，invalid receipt 的 ITT native floor 也已类型化；但 evaluator/operation ledger
与 1,566 个精确计分槽尚未一对一绑定，不能解释为这些尝试已经执行。

零调用实现已进一步从 exact matrix 展开 4,338 个潜在 side-effect stage：1,206 update、1,566 solution、
1,566 evaluator；满路径上限为 2,772 model calls 与 1,566 evaluator transactions。A post-v001 没有
update。该 artifact 只冻结 logical stage population 与逐 cell 离散上限；合法的 planner/solution contract
reject 会短路后续 stage，最终 journal 必须用 typed disposition 证明 `executed` 或 `skipped-by-parent`，
不能为了凑数制造调用。CPU/GPU 秒仍等待真实 canary，schedule 没有 reserve/execute callback。

零调用 semantic disposition verifier 已进一步实现，但只用于验证上述 DAG 与 exact population：它从 pinned
source 重建 schedule，对单一 v1 journal snapshot 一次 replay，接受 terminal completed/failed，且只允许
failed→immediate child skip 与逐级 cascade。synthetic 4,338-stage fixture 已得到 1,566 failed roots、2,772
skips；caller 自建 receipt/seal、extra journal operation、reserved/started、无 artifact completion、跨级或
失败父后 child 均失败关闭；持久化 artifact 只有经 pinned source 与当前 ledger/head 全量重派生并逐字比对
才可接受，standalone DTO 明确不是 provenance。由于 v1 reader 没有 descriptor-relative storage/WAL/storage grant，physical
retry 与 typed local gate 尚未绑定，该 seal 永久标记 semantic-only `NOT_READY/NOT_GRANTED`，不证明真实
request、Evaluator 或 score/report dispatch。

静态 Q0 evidence 已在零 model/零 evaluator 下重放 AgentHPO Q7 的 31 个 source/control 文件、七个
original space 和 21 个真实 strict-codec negative；21/21 均在 evaluator 前拒绝。GDPevo 目前只从 pinned
Git ODB 重放 commit/root/task-groups 与 Q6 group/env/test trees，未读取 private gold，四类聚合 file
manifest 因缺独立冻结算法继续标记 `UNVERIFIED`。这些事实不是 reference、environment 或 isolation
canary。当前主机只有约 1.7 GiB 根盘余量、无 OCI runtime/GPU/Conda；历史 A100 alias 当前不可达，可达
jump 也只有 2 CPU/约 1.6 GiB RAM。因此真实 Q0 必须等具备 Agent assets/GPU 与 GDpevo container isolation
能力的执行环境，不能用 host-run scorer 冒充通过。

这里有一个必须先说清楚的认识论边界：

> 前置 evaluation 只能证明“这个 Benchmark 尚未被低成本通用方法吃掉，而且确实能测到
> Harness 机制”；它不能预先证明“这个 Benchmark 需要 Moss”。后一句只有 fresh、同预算的正式
> 对照结果才能支持。

---

## 1. 为什么不继续直接用旧三套 Benchmark

旧正式实验已经给出两个可靠信号：

- B-frozen 完整 procedure 在 LCBench、CompilerGym 以及 SWE-bench 的有效性上有收益；
- B-online 相对 B-frozen 的学习题和 held-out 方向混合，没有稳定跨题正迁移。

但旧矩阵不适合继续承担下一轮结论：

- LCBench 是便宜的有限 surrogate table，普通 BO/meta-HPO 才是自然强基线；
- CompilerGym 的 pass-sequence 搜索也有便宜的随机、贪心和经典搜索对照；
- SWE-bench Verified 在通过的题上出现二值 ceiling，旧八题又不足以估计成功概率；
- 三臂缺少“Experience 开、Harness 题内更新关”的纯迁移格；
- 没有匹配 solution-reflect、Skill-only 和 optimizer-side compute，无法把 B-frozen 增益单独归因于
  Harness 架构。

因此，旧 24 题只保留为已完成证据，不再用于选题、调阈值、构建 Experience 或做确认性检验。

---

## 2. 候选审计与当前选择

### 2.1 首选：AgentHPOBench

AgentHPOBench 有 30 个 commit-pinned 的真实 ML 仓库任务，覆盖 7 类研究问题。每题先运行固定
baseline，再允许 5 次顺序 intervention；每一步都返回配置、目标指标、辅助指标和日志。这比 LCBench
的查表反馈更接近真实“看实验结果→诊断→修改下一次实验”。

当前官方结果没有显示低成本饱和：limited protocol 下，Claude Sonnet 4.6 的 final-step MBNS 为
`0.407`，GPT-5.5 为 `0.305`；传统 Random/TPE/BOHB 按 best-so-far 分别达到
`0.325/0.298/0.291`。同模型换 Harness 也会改变结果：Claude native harness 为 `0.407`，Claude
Code CLI 为 `0.332`；GPT-5.5 native harness 为 `0.305`，Codex CLI 为 `0.266`。论文还报告
Qwen3-32B 去掉中间反馈后从 `0.148` 降到 `0.052`。[论文](https://arxiv.org/abs/2607.29626)

这使它成为最重要的资格题：

- 若 Moss 只赢 one-shot，却输给 Random/TPE/BOHB 或固定反馈 Agent，研究价值不足；
- 若 Moss 在相同 accepted interventions、训练预算和 optimizer compute 下仍提高 final、AUC 或
  best-so-far，才能说明 Harness 机制有额外价值；
- 30 题已按 category-stratified hash 冻结为 `Q_qual=7 / D_bank=11 / T_fresh=12`，但 12 个
  held-out 仍只能检测大效应，属于 pilot。

主要风险是环境和调用成本：官方 API agent 的 150 个 accepted decisions 实际产生
`1,231–1,695` 次请求，且任务运行在异构仓库与 H200 上。账本必须同时记录 accepted decision、底层
request、GPU 秒与 wall time，不能用“5 轮”掩盖重试成本。

### 2.2 B-online 首选一：GDPevo

GDPevo 有 24 个 task group、每组 `5 train + 5 held-out test`，共享一个业务环境。这是当前最直接的
Skill-evolution 近邻，也天然提供跨题 Experience 的学习/测试边界。

官方三次运行中，GPT-5.5/Codex 的 `base=49.37%`、`self=55.80%`、
`reflect-3=57.82%`、`fewshot=64.51%`；Claude Code/Opus 4.8 为
`50.63/55.05/59.27/67.07%`。便宜 Skill 已有明显收益，但远未到 90% ceiling；这正适合检验 Moss
是否只是把 Skill 写得更复杂。[官方结果](https://github.com/Prism-Shadow/GDPevo/blob/0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4/README.md#evaluation-results)

正式选择不能按公开 uplift 挑“最容易正迁移”的 group。静态 selector 已将 24 个完整 group 冻结为
`Q6/D6/T6/Tfinal6`：Q 只作 qualification，D 只允许构建 Bank，T 是主实验池，Tfinal 保留给未来确认。
当前 online 小试另从冻结 T 中预声明两个 group，每组只用 5 train 建状态、5 test 做 held-out；这不会
改变静态 selector，而且它与主实验 task identity 重合，只能称隔离状态的同题机制比较，不能称 fresh
confirmation。

- 6 个完整 group 只作 qualification；
- 当前 online 小试固定 2 个 T group，不按 outcome 换组；
- 6 个完整 Tfinal group 保留给可能的 confirmation；
- group 内答案、reference、evaluator 和 test 轨迹不得进入模型 workspace。

### 2.3 Reserve：BIRD-Interact Lite `a-Interact`

BIRD-Interact 的当前公开 Lite 数据 revision
[`f7881a9...`](https://huggingface.co/datasets/birdsql/bird-interact-lite/tree/f7881a9c2b9630cc4fc13b0c39279740b0a2fd87)
含 300 题、18 个数据库，每个数据库 15–17 题。公开文件保留 schema、知识和问题，但 test cases
为空；正式评分材料需按官方流程单独取得并隔离。当前 ADK 在 Lite 上报告 Claude Sonnet 4.5
`a-Interact` 平均 reward `0.328`，远离 ceiling；Full 榜单的强模型 normalized reward 约
`0.23–0.26`，平均模型成本约 `$0.06–$0.60/task`。[官方 ADK 结果](https://github.com/bird-bench/BIRD-Interact/blob/451fe2c3518ee1cf908d8139e2913483bd519381/BIRD-Interact-ADK/README.md#results)

它适合 B-online，因为同一数据库内会重复出现 schema grounding、知识检索、歧义澄清、SQL 调试与
两阶段提交 motif；但必须防止 Bank 直接保存 SQL、literal、表行或 task-specific 答案。正式 pool 应按
数据库分组，先在每个数据库内用 discovery tasks 学习，再在该数据库的未见题评分，并额外留出新数据库
检查是否只是 schema 记忆。

BIRD-Interact 已有 memory grafting 和 interaction-time scaling，因此强对照必须固定 bird-coin/patience，
加入 fixed-memory 与等成本增加 interaction 的 baseline。否则 Moss 的收益可能只是更多轮次。

### 2.4 条件项：Atrex-Bench，而不是继续挑简单 KernelBench 题

Atrex-Bench 有 30 个生产 trace operator、440 个 hot shapes、4 种 DSL，并以
compile→5-seed correctness→performance→roofline/SOL 评分。强模型 correctness 已高，但生产加权
SOL 仍低；论文中 GPT-5.5 correctness 约 `91.1%`，`S_agg=0.107`。这比“能不能写出正确 kernel”
留下更真实的优化空间。[论文](https://arxiv.org/abs/2607.14541)

不过 Atrex 已提供 profile-driven 的 Atrex Kernel Agent（AKA）。Moss 若选它，必须在同模型、同 profiler、
同 GPU/DSL、同生成和评分预算下比较：

```text
vanilla
fixed profiler-reflection
AKA
Moss B-frozen
Moss B-online
```

只赢 vanilla 没有意义。首轮只做目标硬件/DSL 的 reference、错误候选、roofline 与 AKA canary；任何一项
不可复现就降为 reserve，不启动正式搜索。

### 2.5 高成本确认项：OSWorld 2.0

[OSWorld 2.0 `v2026.08.08`](https://github.com/xlang-ai/OSWorld-V2/tree/d578d2d4e0dc82b43e270fdaa7fa89d9708cd154)
固定 108 题，并用 task hash manifest 绑定 gated tasks、assets、网站和 provider image。
每题平均 27.25 个 partial checkpoints，适合观察 memory、tool、workflow、scheduler 和 recovery；论文
`v2026.06.24` 上 GPT-5.5 仅 `13.0%` binary / `49.5%` partial，且 150/300/500 步 binary 基本平台；
Opus 4.8 为 `20.6/54.8`。[论文](https://arxiv.org/abs/2606.29537)

它很有科学价值，但不是低成本首发：论文的 agent-only 成本约 `$25.5–$72.4/task`，不含 Builder、
judge、云主机与代理；当前 release 也必须重新 canary。最小 24-trajectory qualification 仅 agent 成本锚
已约 `$612`，建议等便宜 Benchmark 给出正信号后再授权。

### 2.6 当前不进入首轮

| Benchmark | 当前决策 | 原因 |
|---|---|---|
| LCBench / YAHPO | reject | 有限 table/surrogate；普通 BO/meta-HPO 更自然，旧 B-online 已无稳定信号 |
| CompilerGym cBench | reject | 已消费；便宜经典搜索强，旧 B-online 无稳定信号 |
| SWE-bench Verified / Multilingual | reject | 二值、公开、强 agent 已高分；旧实验还出现 validity/ceiling 问题 |
| Terminal-Bench 2.1 | reject | 当前强系统约 83%，best-of-5 可近 89%；公开且跨题 motif 弱 |
| τ² core | reject | 当前强提交约 80–98%，telecom 接近 ceiling；低成本即可高分 |
| MLE-bench Lite | hold | top 约 80%，test-feedback 可达约 91%；标准 24h×3 seeds 且存在已知数据问题 |
| MLGym | hold | 仅 13 个公开异构任务、框架仍重开发，难以给 B-online 足够独立 cluster |
| KernelBench Level 1/2 | reject | Caesar 10-turn 已能把 correctness 推到 90% 左右；本项目旧题也出现简单负例/ceiling |
| KernelBench Level 3/4 | reserve | 仍有性能 headroom，但必须先胜过 Caesar repeated/refinement，Atrex 的评分更贴生产 |
| SWE-Perf | blocked | 项目已有 out-of-process oracle 信任阻断，不能先跑后补可信性 |

---

## 3. Benchmark Qualification：先淘汰不值得测的题

### 3.1 先冻结互斥数据与 selector

在任何 Moss outcome 出现前，冻结候选列表、版本、selection salt、metadata、拆分与哈希：

- `Q_qual`：只用于资格评测，永不进入 Experience Bank 或正式统计；
- `D_bank`：只用于生成内容寻址的 Experience snapshot；
- `T_fresh`：qualification 期间完全不可见；
- `T_final`：若未来需要确认性结论，再保留独立 group/database/release。

AgentHPOBench 使用 category-stratified hash 做 `7/11/12`；GDPevo 和 BIRD 按整个 task group/database
分割，不能把同一环境中的近邻题拆到 qualification 与 formal 两侧。任何 adapter/evaluator 语义变更都会使
原 qualification 失效，必须新 revision 和 fresh pool。

### 3.2 Q0：零模型可信性门禁

每个候选先运行 reference/gold、已知错误候选和攻击 canary：

- reference 至少 `12/12` 正确且可评分；
- 明显错误候选至少 `6/6` 被拒绝或得到预期低分；
- 确定性 evaluator 重放逐字一致；随机 evaluator 的归一化噪声带 `NB≤0.05`；
- 基础设施失败率 `≤5%`；
- task input、reference、test labels、evaluator 私有状态和候选执行区隔离；
- started-without-result 永久计费，不重发、不退款。

任一失败立即 `REJECT/BLOCKED`，模型调用必须为零。

### 3.3 Q1：当前模型的静态难度和有效性

在 `Q_qual` 上，用同一 contract-compatible、非自进化 Harness 运行：

1. one-shot；
2. frozen Harness 独立采样 `N=2`；
3. frozen Harness 独立采样 `N=4`；
4. 固定 Harness 的 solution-level reflection；
5. 对应 Benchmark 的领域强 baseline。

`best-of-N` 只有在正式部署能用同一反馈选版本时才算 deployment score；否则只能作为 oracle upper
bound。所有方法同时报告 final、AUC、best、validity 和成本，禁止只挑最有利指标。

硬门槛：

- 静态基线可评分率 `≥75%`，否则主要在测 adapter/格式；
- 至少 `5/7` qualification tasks 留下 `max(0.15, 3×NB)` 的 normalized headroom；
- 最强低成本 baseline 的归一化分数应在 `[0.10,0.80]`；
- 若达到 `≥0.90`，或超过一半任务稳定 ceiling，淘汰；
- 若所有方法都接近 floor，且 evaluator 不能给出至少两类 actionable feedback，也淘汰。

### 3.4 Q2：普通 compute scaling 是否已经吃掉空间

定义：

```text
rho_4 = (S_cheap,4 - S_1) / (U - S_1)
```

其中 `U` 是官方 anchor/reference 上界，`S_cheap,4` 是不改变 Harness architecture 的采样、反思或领域
优化器在四次预算内的最好 deployment score。

任一条件成立则淘汰：

- 非 Harness-evolution baseline 用不超过计划 Moss 50% 的成本达到 `S≥0.90`；
- `rho_4≥0.70`，即普通方法已关闭 70% 以上 headroom；
- 预注册的成本曲线预测 `N=8` 已进入 `≥0.90` ceiling；
- 强 baseline 在质量和成本上同时支配 Moss probe。

### 3.5 Q3：必须对架构敏感，而不只是格式敏感

不根据 Moss 正负结果选 Benchmark，而是在 `Q_qual` 上预先做安全、确定的“正确→受控破坏→恢复”测试。
候选至少要在以下两个非格式组件族上产生超过 `3×NB` 的效应，并由恢复版本取回至少 80% 损失：

- context/memory routing；
- tool availability/selection；
- workflow/control flow；
- scheduler/retry/recovery；
- role decomposition。

如果只有 output schema 或 Prompt 模板能改变有效率，该 Benchmark 只能作为 contract-reliability stress
test，不能作为 Harness architecture 主结果。

### 3.6 Q4：B-online 的跨题结构门禁

B-online 主 Benchmark 必须有至少三种 outcome 解封前可由 metadata 标注的 transferable motif；每种
motif 在 `D_bank` 和 `T_fresh` 中都重复出现，held-out 必须重新组合 motif 而不是复制答案。

Experience Record 只允许保存：

- 机制假设、失败类别、适用条件；
- workflow/recovery/tool-selection 经验；
- provenance、支持/反证计数和置信度。

严禁保存具体 SQL、配置值、代码 patch、GPU kernel、数据库行、task ID 特判或 reference-derived 常量。
文本/AST/结构近重复审计在分数解封前完成；超过冻结阈值的 pair fail closed。

### 3.7 Q5：方法候选才运行最小 Moss B-frozen probe

Q0–Q4 全部通过后，AgentHPOBench/Atrex 这类 **方法资格候选** 才能在 `Q_qual` 上运行一次
Moss B-frozen；这里的“frozen”只表示不导入或更新跨题 Experience，仍允许 Builder 根据当前题反馈逐轮
重编译 Harness。该 probe 不进入正式成绩，对照是 Q2 中最强的 matched-cost baseline，
而不是 one-shot。

方法门同时要求：

- solution/accepted-evaluation、optimizer-side model tokens、GPU/CPU 与 wall-time envelope 相同或完整披露；
- Moss 在 primary score 或 validity 上的 paired 增量至少达到
  `max(0.05 normalized points, 3×NB, 0.2 pooled SD)`；
- 质量/成本上不被 Random/TPE/BOHB、fixed reflection、AKA 等领域强 baseline 同时支配；
- operational fingerprint 证明至少一个非格式 Harness 组件实际改变，不能只是 directive 改写。

这个 probe 可以淘汰“不值得为 Moss 扩样”的 Benchmark，但不能作为正式效果；它是一种预先声明的
responsiveness enrichment，所以最终结论必须明确限定在“通过资格筛选的目标分布”。GDPevo/BIRD 的
B-online 资格不依据该 probe 的正负选择，避免专门挑 Moss 已知会赢的迁移题。

### 3.8 100 分 scorecard

所有硬门禁先通过，再计分：

| 维度 | 分值 | 满分条件 |
|---|---:|---|
| evaluator/运行可靠性 | 15 | `NB≤0.02` 且 infra failure `≤2%` |
| headroom | 20 | 强 baseline 在 `[0.25,0.65]`，且 ≥75% tasks 留 0.15 headroom |
| 抗普通 compute scaling | 20 | `rho_4≤0.35` 且预测 `S_8≤0.75` |
| Harness sensitivity | 15 | 三个非格式组件族通过三联测试 |
| transfer topology | 20 | ≥4 motifs 且 held-out 为规则重组 |
| 成本/吞吐 | 10 | qualification 和 formal 都落在预先批准 envelope 内 |

`≥70` 才为 `PASS`，`60–69` 为 reserve，任一硬门禁失败为 reject。若不足两个机制不同的 PASS，停止，
不得因为候选少而放宽阈值。

---

## 4. 原 B-online 2×2 设计（保留作因果背景）

> 本节是 2026-08-11 的早期 decomposition，不控制当前执行。当前主实验采用共享 v001 的四臂，
> Experience 表示则在隔离的 `OM/OP/OA` 小试中比较；除非另立新合同，不把 2×2 cell 与四臂或三个
> online 机制混成同一矩阵。

旧三臂把“当前题反馈”和“用反馈改 Harness”混在一起。新实验把因子写得更精确：

- `E`：是否导入只由 `D_bank` 产生、内容寻址且冻结的跨题 Experience；
- `H`：是否允许 Builder 根据当前题的标准反馈重编译 Harness。

所有格中的 solver 都获得 Benchmark 原生允许的观察、工具输出、日志和 feedback；`H=0` 只是冻结 Harness，
不是故意把固定 baseline 变成盲人。这使 `H=0` 成为真正的 fixed-feedback/reflection 强对照。

| Cell | Experience | Harness 题内更新 | 含义 |
|---|---|---|---|
| `E0H0` | 无 | 关 | 空经验、v001 Harness 冻结；标准反馈只改变 solution/action |
| `E1H0` | 有 | 关 | Experience 初始化 v001 后冻结；纯跨题 cold-start transfer |
| `E0H1` | 无 | 开 | 纯题内 Harness adaptation，即 fresh B-frozen |
| `E1H1` | 有 | 开 | Experience + 题内 Harness adaptation，即 fresh B-online |

每个 task/seed 先只生成两个 v001 trunk（`E0`、`E1`）；二者第一次 solution/action 都必须在当前题新反馈
释放前提交。v001 评分后，各 trunk 再分成 `H0/H1`：

- `H0` 后续继续用逐字相同 v001 Harness，但 solver 可以按 Benchmark 原协议利用反馈；
- `H1` 才允许 Builder 读取同一反馈，输出下一版结构化 HarnessDecision；
- solution model、reasoning、accepted actions/evaluations、task contract、trusted registry 和 evaluator 完全相同；
- 若 optimizer compute 不做 sham matching，treatment 明确定义为完整 procedure，并报告成本前沿，不声称
  只有“反馈信息”不同。

`E1H0` 不等同于 Skill-only：Experience 可以影响 v001 的 role、memory、tool、workflow 与 scheduler
结构。另设只允许文本 SOP/Skill 的 sidecar，才用于回答“结构化 Harness 初始化是否超出 Skill 层”。

主 factorial 中 `D_bank` snapshot 在整个 `T_fresh` 上冻结。真正的 continual accumulation 另作次要
prequential continuation：task `t` 的四格都 sealed 后，才允许把 `t` 的 B-online 轨迹写入只影响
`t+1` 的 Bank。两种 estimand 不混在一个数字里。

---

## 5. 小样本先做什么，何时才谈“显著”

### 5.1 Stage O1：最便宜的 cold-start pilot

先只比较每题的 v001：

```text
tau_cold = mean(Y_v001(E1) - Y_v001(E0))
```

这时当前题尚未释放新的 evaluator outcome，差异只能来自 sealed Experience 对初始 Harness 的影响。
建议：

- GDPevo：2 个新 task groups × 5 test = 10 held-out tasks；
- BIRD-Interact：2 个新数据库 × 4 held-out = 8 held-out tasks；
- 每题 2 条完全隔离 seed lineage；
- 同时跑 Skill-only v001 sidecar，判断 Experience 收益是否只需文本 SOP。

O1 只是 go/no-go。8–10 个 task unit 只能检测很大的 paired effect，不能因为 p-value 偶然小就声称
Task-level 显著迁移。

### 5.2 Stage O2：小型完整 2×2

只有 O1 的方向、validity 和成本都通过预注册门槛，才在同一批任务上把四格补到 `R=3`，作为 exploratory
机制分析：

- primary：每轮 ITT score 的 AUC；
- B-online 增量：`tau_online = mean(Y_AUC(E1H1)-Y_AUC(E0H1))`；
- Harness 主效应：`mean(Y_AUC(E0H1)-Y_AUC(E0H0))`；
- interaction：`(E1H1-E0H1)-(E1H0-E0H0)`；
- 同时报告 final、validity、conditional-on-valid、oracle-best、负迁移比例和成本。

所有 reserved attempt 都进入 ITT；invalid、contract reject、timeout 和 started-without-artifact 按预注册 floor
计分，不再因 `<4/8 valid` 删除整个 task pair。conditional-on-valid 只是次要描述，因为 validity 是
treatment 后变量。

### 5.3 Stage O3：只有新任务才能做 confirmation

若要回答“B-online 效果是否显著”，不能把 O1/O2 的 8–10 题升级措辞。需要新的 confirmation pool：

- 每个 Benchmark 至少 24 个 fresh tasks，3 seeds；
- GDPevo 建议至少 6 个新 group；BIRD 建议至少 6 个新 database cluster；
- task 是主要推断单位，seed nested within task；数据库/task-group 同时作为 cluster；
- task-level paired randomization/permutation test + cluster bootstrap CI；
- 两个 Benchmark 分别检验并做 Holm correction，不平均原始分数。

近似 80% power 下，8/12/24/30 个 task 分别只能检测约 `d_z=1.09/0.89/0.63/0.56`。因此“少量
held-out”与“可靠证明中等效应显著”不可同时满足；本方案先买便宜的决策信息，再决定是否扩样。

强成功标准固定为：

1. 两个机制不同 Benchmark 上 `E1H1-E0H1` 的 Holm-adjusted CI 都大于 0；
2. v001 cold-start、ITT AUC 和 validity 不互相矛盾；
3. B-online 在质量/成本 Pareto 上不被 fixed reflection、Skill-only 或领域强 baseline 支配。

若只有一套为正，只称 benchmark-specific transfer；只有 v001 为正称 cold-start-only；只有后期为正称
interaction-dependent；方向混合则继续报告“无稳定跨题正迁移”。

---

## 6. 成本与报告合同

下一轮不能再用 `api_cost_usd=0` 表示没有成本。即使走登录态或包月服务，也必须按冻结公开价格记
dollar-equivalent，并保留原始物理计量：

- solution calls、accepted decisions、底层 requests 与 tokens；
- Builder/Planner/distillation calls 与 tokens；
- evaluator transactions；
- CPU/GPU seconds、独占资源与 wall time；
- environment reset、失败重试和 started-without-result；
- 实际现金成本与 price-equivalent 分列。

报告至少包含：

- `score@cost` 与完整 cost-quality frontier；
- `delta ITT / delta cost`；
- 达到预注册 threshold 的 time/cost；
- 每 task/seed 的四格数据与失败分类；
- component activation、operational fingerprint 和 Experience provenance；
- qualification 的全部 PASS/RESERVE/REJECT，不能只展示入选者。

任何正式 entitlement 只能在两个真实 canary 测得本项目的 `C_task`、`C_builder`、GPU/CPU 时间后冻结。
本文没有授权额度，也没有启动入口。

---

## 7. 执行阶段与停止条件

### Phase 0：只读准备

- 冻结 upstream commit、dataset revision、license、task manifest 和 selector salt；
- 生成 `Q_qual/D_bank/T_fresh/T_final` manifest；
- 写 reference/negative/leakage canary；当前已冻结零调用 schedule，真实环境执行仍阻断；
- 输出逐候选静态 cost estimate；
- 用 zero-authority precheck 重放两个 Benchmark 的 task×seed 顺序、共同 v001 与四臂 barrier；当前已完成；
- **零模型、零 evaluator 正式调用。**

### Phase 1：Qualification

- 先 Q0，再 Q1/Q2/Q3/Q4；
- 任一硬门禁失败立即停该候选；
- 不运行 B-online，不根据 B-online outcome 选 Benchmark；
- 完整发布 scorecard 后，等待用户再次批准。

### Phase 2：O1 cold-start pilot

- 只在 PASS Benchmark 上构建独立 Experience snapshot；
- v001 E0/E1 同时提交后一次解封；
- 未通过 go gate 不补跑 O2，不换题追正结果。

### Phase 3：O2/O3

- O2 只作 exploratory 2×2；
- O3 必须换 fresh pool，并另行冻结预算、模型和统计方案；
- Atrex 与 OSWorld 都没有自动入口。

全局停止条件：

- 两个以上候选被普通低成本 baseline 饱和；
- evaluator/infra 无法通过可信性门禁；
- Moss 被强 baseline 在质量和成本上同时支配；
- Experience 出现答案、配置、SQL、代码或 task-ID 泄漏；
- insufficient fresh tasks 使预注册推断单位不足。

---

## 8. 当前授权边界

用户已确认并行准备 AgentHPOBench/GDPevo 的多 Benchmark 主实验与 B-online 多机制小试。当前授权仍
只覆盖零调用准备；在以下条件同时满足前，不启动模型或 evaluator：

1. 已有 post-v001/Task-local Skill compile-only authority 进一步绑定正式 provider、planner/Skill operation
   ledger、solution/evaluator/optimizer/report；
2. AgentHPO formal task smoke 与 GDPevo isolation/image/manifest canary 真实通过；
3. 已有 typed learned-state transition→held-out context/compile 进一步绑定 authenticated source terminal、
   完整 planner request/result、pinned online task authority、failure cursor 并经 stage gate 重放；
4. 基于真实 canary 冻结精确模型、硬预算、资源帽和非零 entitlement，再提交用户审阅。

online 预声明 held-out task identity 与主实验部分重合，因此 O1/O2 仅是隔离状态、禁止主实验 result/trace/
state 输入的同题机制比较；若要独立 fresh confirmation，必须另冻未被主实验消费的新 task pool。
