# 多 Benchmark 宽 Harness 与元机制实验合同（2026-08-12）

> 状态：实验因子、资格切分和恢复合同已冻结并开始实现；所有候选 Benchmark 当前仍为
> `BLOCKED_*`、执行授权为 `NOT_GRANTED`、正式 entitlement 为零。本文不授权模型、GPU、Docker
> 或正式 evaluator 调用，也不导入 `v1r8/v1r9` 的轨迹或 Experience。

## 1. 实验目的

主实验回答两个问题：

1. 不依赖跨题经验时，题内 Harness 重编译是否能在至少两个机制不同的 Benchmark 上重复优于固定
   Harness 和 task-local Skill/Reflection；
2. 强制每轮把全部七个 Harness 架构轴都改掉，是否比按反馈只改必要轴更好，还是会产生破坏性搜索。

B-online 小试另回答：同一批 sealed source 轨迹若分别编码为 Memory、Meta-policy 或 Harness
Archive，哪一种表示能改善未见题 cold start 或题内适应。主实验和 online 小试的基础设施可并行准备，
但不得共享 outcome、调参或把两套样本合并成一个显著性结论。这里的“并行”目前只授权准备；正式
online 必须等待 qualification/主门禁通过和单独非零 entitlement。

## 2. Benchmark 资格与冻结切分

唯一静态入口为
`optimization_lab/harness_builder/data/benchmark_qualification_v1.json`，验证器为
`qualification.py`。旧正式结果只作报告引用，初始 Bank 固定为空。

- AgentHPOBench 固定 commit `6d8d900...`，切分为 `Q7/D11/T12`。Q7 按官方
  `configs/scoring_reference.tsv` 的七类各取一个 hash 最小任务；类别文件 SHA256
  `c17ad42d...01308` 进入 selector digest。
- GDPevo 固定 commit `0999c0d...`，以完整 task group 为 cluster，机械切为
  `Q6/D6/T6/Tfinal6`，不能把同一 group 的题拆到不同边界。
- BIRD-Interact 固定 repo/dataset revision，但 private bundle 缺失，当前为零执行单元。

任何正式启动要求至少两个机制异质 Benchmark 同时满足：来源重放、reference/negative/leakage
canary、evaluator 隔离、headroom、普通 compute scaling、非格式 Harness sensitivity 与 transfer
topology 全部 PASS；每个 cell 的 CPU/GPU 硬帽只能由 canary p99×1.2 冻结，不能预估铸造。

## 3. 主实验四臂

每个 task/seed 只生成并评分一次共同 v001 trunk，释放 v001 feedback 后才 fork；各臂 solver 都能看
Benchmark 原生 feedback。

| Arm | 可变对象 | 跨题状态 | 作用 |
|---|---|---|---|
| `A-fixed-feedback` | Harness 七轴冻结；solution/action 可用原生反馈 | 无 | 强固定 Harness 对照 |
| `S-reflection-skill` | task-local 文本 SOP/Skill 可更新，七轴哈希冻结 | 题后清空 | Penguin/GDPevo 风格强对照 |
| `B-targeted` | 每轮重建全部对象，但只要求至少一个可执行轴实质变化 | 无 | 常规 Moss 题内适应 |
| `B-frozen-wide` | v002 起七轴全部实质变化，且全部 active Python runtime component 重新实例化/配置 | 无 | 用户要求的宽架构压力臂 |

七轴固定为 `role_graph / memory_views / tools / parent_strategy / workflow /
scheduler_mode / recovery_mode`。role、memory、tool 仅重排不算变化；workflow 顺序变化算控制流变化；
rule/directive 文本变化不算架构变化。可信 Registry、operator 实现、evaluator、scorer、预算与 task
contract 在四臂间冻结。

这里的“重新实例化”有明确边界：每轮由可信 factory 新建七类 typed Python 行为对象，且 parent、memory、
tool、workflow、scheduler、recovery 与 role 指令确实通过这些对象执行；它不是 OS/package 重装，也不
下载新依赖。底层 allowlisted 工具实现仍由 Registry 冻结，任意代码、evaluator、scorer 和预算均不可变。

`B-frozen-wide` 每个 accepted transition 必须：

- 七位 change map 全为真；
- 七轴稳定 configuration hash 相对最近 accepted parent 全部改变；resolved effect hash 另作审计证据，
  不因 feedback/history 自然变化而冒充配置变化；
- 当前 operational fingerprint 不与本 lineage 任一历史版本重复；
- solution 调用前封存内容寻址 compile receipt；
- receipt 绑定当前/上一 decision、上一 receipt、Registry/catalog、所有 component config、parent、
  memory/tool/workflow/scheduler/prompt 哈希；
- 任一条件失败，该 reserved round 以 ITT floor 封存并计费，不调用 solution/evaluator，不重发。

主比较为 `Wide−A`；机制比较为 `Targeted−Skill`；宽度安全性为 `Wide−Targeted`；`Skill−A`
描述文本适应增量。若 `Wide−Targeted` 显著为负，不把“大改”包装成 contribution，而应结论为
adaptive scope selection 更重要。

## 4. B-online 三种隔离机制

共同 comparator 是无跨题状态的 `O0=B-frozen-wide`，不先上 hybrid：

- `OM`：内容寻址 Experience/Meta-memory，只保存机制、失败类、适用条件与证据计数；
- `OP`：版本化 typed Meta-policy，只调 trusted component 候选、检索/选择/归档策略和公开权重；
- `OA`：Harness population/archive，只保存 typed recipe、fingerprint、公开 aggregate fitness 和 lineage，
  可做 parent selection/recombination。

M/P/A 各有独立 checkpoint、ledger 和状态根，禁止互读；它们都不能写任意代码、Prompt、evaluator、
scorer、预算、private/future 数据。三者共用相同 source task、顺序、可见信息和 updater-call 数；每个
source task 恰好一次 update，正式 T 上先冻结 snapshot 比较 v001 cold start，再按预注册 gate 补完整
native rounds。Hybrid 只有单机制在 fresh pilot 显示 task-wise 互补后才能另立新池。

控制器不能只接受 proposer 声称的 M/P/A SHA：每次 learned update 必须同时解析 parent/child memory、
typed policy、Harness archive 和 Registry，验证只有当前机制允许的对象发生合法 transition，随后才封存
checkpoint、对象、receipt 与哈希链 ledger。wide compile/round/formal artifact 也必须通过无 symlink 的
descriptor-relative 读取与 no-replace 发布；普通用户态 append-only 不等于不可篡改，因此新事实 ledger
另外绑定 canonical event hash chain 与 head anchor。

这只借鉴 HyperAgents 的开放式 archive、stepping-stone 与“改进改进过程”的元认知视角，不复制其任意
Python 代码自修改。HyperAgents 主实验仍在一个大体固定的 outer loop 下搜索可编辑 Agent/meta-Agent
程序；Moss 的 `OM/OP/OA` 分别只允许公共 memory、typed policy 和 typed Harness recipe，不能修改模型、
评分协议或 trusted Registry。其附录中的可编辑 parent selector 也只是初步扩展，并未显著优于随机或
人工 selector，因此本实验不会预设 Archive 一定胜出。第一手来源：
[论文 v1](https://arxiv.org/html/2603.19461v1)、
[官方仓库](https://github.com/facebookresearch/Hyperagents)、
[Meta-Agent 程序](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/meta_agent.py#L6-L18)、
[Archive](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py#L160-L180)、
[Parent selector](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py#L511-L584)。

## 5. 调度、预算和统计

task×seed 与不同 Benchmark 可并行；同一 mutable environment、数据库或 exclusive GPU key 冲突时必须
串行。同一 block 的四臂按冻结 hash Latin rotation 排序；每轮先全部 reserve/generate，经 barrier 后
统一评分并释放各自 feedback。Prequential online 只能在 benchmark×seed 链内按 task 串行，但同题四
机制、不同 seed 和不同 Benchmark 可并行。

主 outcome 是各 Benchmark 单独计算的 post-v001 ITT native-raw AUC。invalid、timeout、contract reject、
started-without-artifact 按预注册 floor 计入，不按 conditional-valid 删除 pair。full AUC、final、best、validity 和完整
cost frontier 为次要指标。每个 Benchmark 单独检验并做 Holm 校正，原始分数不混合；GDPevo 以 group
做 cluster bootstrap/permutation。

正式预算公式先冻结、数值待 canary：

```text
E_main = S * Σ_b N_b * [1 + 4(R_b - 1)]
C_optimizer = S * Σ_b N_b * [1 + 3(R_b - 1)]
C_logical_model = S * Σ_b N_b * [2 + 7(R_b - 1)]
```

逻辑调用、底层 provider request、tokens、accepted decisions、evaluator transaction、CPU/GPU 秒、
wall time、现金成本和 dollar-equivalent 分开记账。逐 cell entitlement 不可借用。

`Wide−Targeted` 的实用界为 `δ=max(0.03 normalized, 2×noise band)`：CI 下界大于 `−δ` 才称
non-inferior；上界小于 `−δ` 为 practical harm。Online 少量 pilot 只作 go/no-go；要声称显著跨题迁移，
仍需每个 Benchmark fresh `24+` tasks、3 seeds 和 cluster-aware paired inference。

## 6. 当前阻断与完成条件

当前正式执行保持停止：AgentHPO 缺可复现目标 GPU/环境，GDPevo 缺隔离 runtime canary，BIRD 缺
private bundle；根分区仅余约 1.8 GiB，也不足以安全物化多个容器环境。不得删除旧结果或环境来暗中
解锁。

当前已实现 arm-independent v001 typed schema/archive、完整 compiled-Harness semantic projection、typed
task/source/seed binding schema、solution/candidate/evaluation/interruption outcome archive，以及从 checked-in
manifest 展开的 exact 126-cell 零调用 audit plan；后者绑定 identity/seed/精确轮数、arm policy、完整 arm
variant digest 与 Latin position balance。专用 exact-plan controller 已接入共同 v001 barrier/recovery，
每次 bind/replay 都重验 variant、policy、contract 与四臂 fork receipt；它没有 provider callback，authority
与 entitlement 恒为零。source authority 从两个 pinned Git object database 机械重建 42 个 solver-visible
task artifact 与 126 个 task/context-bound key，调用方不能自供 task/context hash；GDPevo 只向 solver
投影公开 input，私有 evaluator/gold 仅进入 controller-side source binding。exact plan 只接受经 pinned-
source authority 重放的 canonical bundle 并绑定其 SHA；barrier 构造及每次 v001 bind/recovery 都重新读取
两套 pinned source、重建完整 bundle 后逐键比对，裸 key 或 self-rehashed bundle 不能进入 formal barrier。
零调用 v001 orchestrator 还会重新加载 pinned source、exact plan、Rule Registry 与 operator source，使用
source-bound capability card 四次 trusted compile，并逐字比较 runtime/canonical/equivalence/四臂 receipt；
直接构造的不安全 decision 或整体 self-rehashed evidence 不能成为 provenance。`ENVIRONMENT_INVALID` 只允许作为绑定前次
attempt 且更换环境 SHA 的重试原因，不再永久污染 task×seed。

这些仍不足以成为 formal authority：v001 trusted recompile 已完成，但它没有 provider/evaluator、预算或
执行 callback。现有 production cell 的 version seal 已改成必须携带实际 `CompiledHarness`，在任何落盘前
重建并逐字核对 receipt；generic store 仅能显式用于 fixture，post-v001 的 compile-only authority 已有，
但携带正式 provider/operation journal 的四臂 orchestrator 仍不存在。
AgentHPO 已有严格 discrete intervention codec、typed space provenance binding 与逐 provider-request
receipt；11 个 scalar task 已从 pinned commit/tree 的 manifest、backend 与 runner AST 交叉派生精确
allowlist/current config（包括 JSON `null`），唯一 free-form task 仍需专用 codec 或 fresh split。exact ITT
artifact 已把 typed invalid receipt 机械映射到 Benchmark native floor，并阻止内部 affine utility 进入公开
report；exact matrix 已列出 1,566 个 scoring slot，并从 pinned source replay 机械展开 4,338 个潜在外部
stage（1,206 update、1,566 solution、1,566 evaluator；满路径 2,772 model/1,566 evaluator）。逐 cell 的
离散调用帽已可计算，A post-v001 没有 update；CPU/GPU 秒仍为 real-canary pending，schedule 保持零
entitlement 且不暴露 reserve/execute callback。尚无唯一可信 transport ledger，不能证明调用方没有
省略真实 request，也没有 reservation/evaluator/optimizer/report 的一对一 dispatch 来证明这些 slot 已执行。
合法 contract reject 会短路后续 stage，正式 seal 必须逐 stage 证明 executed 或 typed-parent skip，不能要求
4,338 个 operation 全部出现。
当前新增的 semantic-only disposition verifier 已能在同一 v1 journal snapshot 上验证 terminal operation 与
failed-parent cascade，并对 4,338 项 synthetic exact-set 做一次重放封存；它不会把 completed transport
误作 artifact contract 通过，也不接受 started/reserved 或本地 gate rejection。持久化 artifact 只有经 pinned
source 与当前 ledger/head 全量重派生并逐字比对才可接受；standalone DTO 不构成 provenance。该产物仍显式列出 hardened
journal、WAL、storage/resource grant、physical retry、typed gate 和 provider dispatch blockers，始终
`formal_execution_ready=false`。版本化 journal v2 与 pending-WAL 只形成
`docs/plans/2026-08-13-factorial-hardened-journal-v2.md` 草案，不改变旧 `events.py` 或历史 CompilerGym
36-event canary，也未授权实现/执行。
四臂 post-v001 与 Skill 的 compile-only authority 已实现：前者从 exact source/plan/matrix 重放当前 slot、
用 trusted Registry 重编译 B-targeted/Wide 并核对 accepted/rejected parent lineage，后者冻结 v001 七轴并
只允许同 task/seed bounded Skill 在 compile 后进入 solution prompt；正式 provider/operation journal/score
dispatch 仍不存在。B-online 零调用 plan 已列出 732 个 attempt 与 84 个机制更新，并新增 exact 16-lane
source/update lineage、OM/OP/OA 逐步 resolved typed transition、final checkpoint→held-out Builder prior、
O0 零注入、四机制 source cohort 和 same-context trusted compile 验证。它仍未从唯一 journal 认证 source/
operation digest，也缺完整 planner request/result、pinned online task authority、updater failure cursor 与正式
stage gate；held-out identity 与主实验部分重合，不能称独立 fresh confirmation。静态 factorial manifest 保持
`execution_authority=NOT_GRANTED`、全零 entitlement；现有三/四臂 runner 不能被当作本合同正式执行器。

零调用 static Q0 evidence 另已完成 AgentHPO Q7 31-file source replay、七个 original discrete space 与
21/21 evaluator-before-codec negative，以及 GDPevo pinned commit/root/task-groups/Q6 group-env-test Git tree
replay；它不读取 private gold，并把尚无独立算法的 GDPevo file-manifest 聚合明确标为 `UNVERIFIED`。
它不是 reference/environment/isolation canary。当前本机和可达 jump 都不具备正式 Q0 所需的 GPU/assets 或
OCI isolation；历史 A100 alias 此次探测不可达，因而没有启动真实 evaluator。

下一里程碑完成条件：

1. 宽变异、compile receipt、历史 schema replay、M/P/A 隔离与多 Benchmark fixture 测试全绿；
2. 至少两套 Benchmark 的 source/evaluator/capability receipt 为 READY；
3. 精确模型、seeds、task IDs、硬预算、并发 conflict graph 与统计 manifest 在首个 outcome 前冻结；
4. 用户审阅非零 entitlement 后，才可启动正式模型/evaluator。
