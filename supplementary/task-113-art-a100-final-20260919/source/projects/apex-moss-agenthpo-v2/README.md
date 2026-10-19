# apex-moss

## Dual executable Harness runtime

The incremental dual-Harness path lives beside the original configuration runtime:

- `TaskHarnessArtifact` is a versioned, content-addressed JSON program. Its ordered nodes execute real model calls, allowlisted tools, and one final emit operation.
- `BuilderHarnessSpec` is a hashed upper Harness with explicit `inspect -> propose -> validate -> probe -> commit_or_rollback` steps.
- `HarnessWorkspace` stores immutable lower-Harness versions plus hash-verified public execution traces and round receipts.
- `DualHarnessRuntime` runs the lower Harness, calls an evaluator, exposes only its typed `PublicEvaluation`, and lets the upper Builder Harness produce the next version. Reusing a completed `run_id` replays the receipt without new model or evaluator calls.

Experiment-1 production execution additionally binds a fresh public-only
`ExperimentOneToolPack` under each round/cross-test cell.  The lower Task
Harness may use the fixed Agent protocol (`tool`, `workflow`, or final
`emit`) and the bounded tool registry; the official evaluator is never
registered in that loop and remains an external Python step.  Every Agent
model turn receives a node-local, deterministic scope such as
`solve.agent.0000`, while cross-test cells write their own solver audit ledger.
The final benchmark candidate is the string inside `emit.candidate`; the
intermediate Agent action JSON is not itself the benchmark submission.

### V1/V2 Experiment-1 entry points

The historical V1 manifests remain the default and are replay-compatible. The
new schema-2 Task Harness is additive and must be selected explicitly:

```bash
python scripts/run_moss_experiment_one.py preflight \
  --suite edgebench --harness-version v2 --root <artifact-root>
```

In V2, static public `tool_call` nodes and Solver-selected Agent actions both
go through the fixed `ToolRegistry`, which applies the allowlist, workspace
boundary, call budget, replay checks, and append-only tool receipts. Evaluator
tools are forbidden in the lower Harness; official scoring remains a separate
Python evaluator step. In cross-test, API/Solver/format/Harness/evaluator
errors are terminal audit evidence: Moss preserves the original exception,
writes no official score, and never retries or converts the error to zero.

Run the no-network fixture:

```bash
python scripts/run_dual_harness_fixture.py
```

The default model configuration uses `gpt-5.6-sol` for both layers. The models can be separated with `MOSS_BUILDER_MODEL` and `MOSS_SOLVER_MODEL`; `create_dual_harness_runtime(...)` selects each transport independently through `MOSS_BUILDER_TRANSPORT` and `MOSS_SOLVER_TRANSPORT` (`codex_cli` or `openai_responses`). Tool execution is fixed to `controller_json` in this first version: models produce typed text/JSON, while Moss Python executes allowlisted tools. Native model tool calling is therefore not an architectural dependency. Required API and server resources are listed in `docs/plans/2026-08-24-dual-harness-resources.md`.

Evaluators must keep private evidence outside the public projection:

```python
EvaluationResult(
    public=PublicEvaluation(score=0.5, feedback="format_error"),
    private={"hidden_test_log": private_log},
)
```

Only `public` enters the trace and Builder prompt.

Each round also requires an `execution_contract_sha256` covering the frozen transports/generation settings, tool registry, evaluator public projection, and probe contract. Moss writes a durable stage claim before every external Solver, evaluator, or Builder call. If a process dies before that call's result is saved, retrying the same `run_id` raises `IncompleteRoundError` instead of silently paying for the call twice. A later round is blocked until the pending round is recovered or, if it made no Harness commit, explicitly closed with `workspace.abandon_round(...)` after operator audit.

**历史 Task-Conditioned Harness pilot**：最初用两个 benchmark family 检验
Harness 条件化与 Builder 生成的研究主张。历史方案见
`docs/plans/2026-07-27-task-conditioned-harness-builder-pilot.md`；当前术语与下一步资格实验
见下文。

2026-07-27 pilot 已完成，结果见 [`RESULTS.md`](RESULTS.md)：通用基准四格均为
100%，出现天花板效应，Q1/Q2 无法有效区分；builder0 两族 train/val 也均为 100%，按冻结的
“至少一族提升 10 点”判定线仍为无信号。后续 5 道 BigCodeBench-Hard canary 也为 100%，
说明完整测试可见且允许迭代时，单纯增加函数题复杂度仍不够。第二轮采用
[`Hidden Final Verification`](docs/plans/2026-07-27-hidden-final-verification-round.md)：
同题只暴露少量测试，完整官方套件仅由评分器终验。V1 起始档 canary 得到 4/5（80%），
已按预注册规则冻结。隐藏正式终验随后完成：tdd 进化在 train 提升 20.8 点、val 下降
3.3 点（泛化/应试灰区），spec 进化未生效；Q3 Builder 两族 val 均低于 v001。旧 Q2 的
raw 主场差受题池难度混淆，因此追加
[`同题配对确认实验`](docs/plans/2026-07-27-q2-paired-feedback-confirmation.md)。配对交互
最终为 −6.7 点（95% CI −15.0 到 +1.7），方向反证当前 v005 的反馈形态专长。
随后独立 Q1 确认得到 R0/R2 两条合格训练谱系，但全新 external 的聚合增益仅 +1.39 点
（95% CI −4.17 到 +8.33），按冻结线为不明确：训练专化可以复制，稳定迁移仍未证实。
以上 `train`/`val` 是历史目录名；旧协议中的 `val` 承担当轮终验角色，并不等于新三层
协议中供 selector 使用的 validation benchmark。

当前研究方向改为先验证“面向 benchmark 具体任务的 Harness 能否靠即时分数稳定爬升”。
[`实验计划一`](docs/plans/2026-07-31-instance-conditioned-ai-for-ai-benchmark-plan.md)
已完成 P0：`optimization_lab/` 提供追加式实验账本、预算门禁、KernelBench 适配器、
A100 SSH 执行和每 5 秒刷新的 HTML 看板。固定任务为 LayerNorm 与预登记备选题
Matmul + Sigmoid + Sum。P1 在每道题上冻结三种 Harness，通过编译、正确性、速度三段反馈
反复修改 Kernel 候选；P2 才会让 Harness 本身形成独立版本谱系。原 Matmul + Subtract + Multiply + ReLU 题因全零负例也能通过官方五次
正确性检查，在任何模型调用前淘汰，异常分数永久保留但不计入结论。P0 正反例、三次重复
计时和全新隔离容器复现均已通过。容器不依赖服务器缺失的 NVIDIA Container Toolkit：只把
GPU4 设备和必要的只读驱动库映射进去，禁网、只读根文件系统，容器内只能看到一张 A100；
冻结环境为 Python 3.10、Torch 2.13.0+cu130、Triton 3.7.1。
面向管理层的阶段汇报见
[`KernelBench 专用 Harness 实验｜CTO 汇报`](docs/reports/2026-07-31-kernelbench-experiment-briefing.html)。
不依赖 Docker 的后续准备也已落地：P1 三种基线、P2 两题各三条独立谱系、共同 seed、
八轮/连续三轮停止规则、双费用硬帽占位、候选代码提取、私有路径脱敏和追加式候选归档。
P1 的端到端控制器先用 fake generator 与 fake adapter 走通“冻结 Harness 组装提示词→
单一 `ModelNew` 提取→原始响应和代码不可覆盖归档→评分短反馈→预算和账本”的完整路径；
草案状态不会触发 generator，同一 candidate ID 重放也不会重复消耗模型或评分资源。
真实 P1 已在 `gpt-5.6-sol`、A100 GPU4 和已批准硬帽下完成：六条路线共 22 个 Kernel 候选，
22 个评分均有效、17 个正确；LayerNorm 的 8 轮通用流程最好为 19.86×，Matmul + Sigmoid + Sum
最好为 1.006×。GPU 计时累计约 723 秒，22 次模型调用均走已登录的 Codex/ChatGPT，账本记录
API 费用为 0。P2 已在单独授权后完成：两题各三条隔离谱系从逐字相同的 v001 起步，
共得到 47 个有效评分、45 个正确候选，GPU 计时约 1661 秒。LayerNorm 三条路线最好为
19.82×、19.68×、5.70×，接近但未超过 P1 的 19.86×；Matmul + Sigmoid + Sum 三条路线
均超过 P1 的 1.006×，最好为 1.85×、4.10×、3.45×。最后一条路线的第八轮 Harness 调用
被会话中断，系统保留已消费调用并安全冻结在 7 个有效轮次，没有越过 15 次 lane 硬帽。
P3 未启动，须另行授权。

P2b 是在 P2 之后单独冻结的新搜索阶段，方案见
[`Profiler 引导的大范围 Harness 探索`](docs/plans/2026-08-02-kernelbench-p2b-profiler-guided-harness-exploration.md)。
每题不再复制三条相同 seed，而是运行“分析强解、架构重建、反向假设、前沿重组”四条不同
路线。每条路线把输入起点、任务内 Skill、分析工具、记忆视图、工作流和 Kernel 结构范围写成
结构化 Harness；v001 为路线 seed，v002–v008 在每个 Kernel 跑分后更新。每一版 Harness 只生成
一个 Kernel，以便把方法变化与分数变化对应起来。分数不足 2% 的变化视为噪声区；没有可信
提升时必须换工具、Skill、记忆、代码起点、瓶颈假设或主结构，第六轮仍未超过冻结起点则强制
重启。P2b 不使用 P2 的连续三轮早停，每题四条路线各最多 8 个 Kernel/15 次模型调用；两题
总上限为 64 个 Kernel、120 次模型调用和 14,400 GPU 秒。

P2b 的 Tier A profiler 使用 `nsys` 时间线、干净 Triton 编译缓存和 `cuobjdump` 资源摘要，
可以公开 Kernel/launch 数、寄存器、共享内存和静态理论 Occupancy。服务器当前未安装 `ncu`，
且硬件计数器为管理员专用，因此 achieved occupancy、DRAM/L2 与 warp stall 必须显式记为
`unavailable`，不能用理论值冒充实测。Profiler 只在候选已通过正确性后运行；原始 trace 保存在
私有目录，给 Harness 的只有脱敏摘要。P2b 使用独立计划、账本、看板和恢复预算，没有 P3
入口，也不在单任务循环中修改通用 Builder。P2b 已写入 phase completed 事实，但在 writer/
ledger 双锁、稳定哈希、terminal lane 和逐 lane 保守预算重放通过前，不视为下游可消费快照。

P2b 后的自适应追加阶段目前只有未授权的
[`P2c 资源分配方案`](docs/plans/2026-08-02-kernelbench-p2c-adaptive-resource-allocation.md)，尚无执行
入口。它计划在 P2b 完成冻结后按 Task 独立做分段 top-k 竞赛，并把格式或基础设施中断与性能
淘汰分开；P2b 的 64 Kernel/120 调用合同不会因此改变。该 POC 的实现现已暂停。

上一轮正式执行矩阵为三臂、三个 benchmark：YAHPO Gym/LCBench、CompilerGym cBench、
SWE-bench Verified 各 8 题。`A` 是 v001 后冻结 Harness 的 task-conditioned 对照，`B-frozen` 在题内
持续进化但没有跨题记忆，`B-online` 与它从逐字相同的空状态开始，并在每道在线题三臂都评分封存后
立即吸收自己的公开轨迹，经验只影响下一道未见题。每个 benchmark 前 6 题执行 test-then-learn，
最后 2 题不再写入 Experience Bank，用于检查前六题的经验在后续题上是否有增量；这两题仍允许各臂
读取当前题 evaluator feedback 并完成八轮题内适应，因此是跨题学习 sealed，而不是完全不反馈的
evaluator-blind holdout。三个环境可并行
准备；正式 24 题按冻结的平衡交错流串行运行。每个 task block 各取三个 benchmark 的同位置题，suite
首发顺序按 block 循环轮转，避免某个 benchmark 固定处于更早或更晚的服务时段；B-online 在每道 online
题三臂封存后更新，checkpoint 沿混合流前传。报告按 instance 输出三臂有效轮均值、best 与合规轮数，
并把任务 7–8 单列为 sealed holdout，不生成 benchmark 内 task 原始分数均值。每题每臂均为
v001–v008。旧 KernelBench meta-train、
P1/P2/P2b 轨迹和四臂 `A/B0/B*/B-online` 不进入本轮初始 Experience Bank。
v1r8 的合同修复、同题准入与有效性门禁见
[`Harness 合同兼容与有效性方案`](docs/plans/2026-08-04-harness-contract-compatibility-validity-v1r8.md)。

正式结果现由 schema-v6 `v1r9` successor continuation 接续：v1r8 已封存的前 6 个 instance 只按
内容哈希引用，旧账本中意外启动的 `scikit-learn-14983` 三个 operation 保留为已计费但明确不进入
学习或性能统计；新 segment 只拥有全局 stream index `[6,24)` 的 18 题、54 arm、432 round
entitlement。B-online 独占导入前缀 checkpoint/Bank，A 与 B-frozen 仍从空经验开始。未执行的六个
SWE 位置替换为六仓库、`F2P>=6` 且 `F2P/(F2P+P2P)>=1%` 的哈希排序集合：`pytest-7205`、
`matplotlib-25775`、`xarray-4356`、`sympy-21930`、`astropy-13977`、`pylint-4604`。原候选
`requests-2317` 在冻结禁网合同下依赖外部 httpbin，gold canary 未通过，因此明确排除且不进入正式成绩
或学习。镜像只允许本地已物化的 locked digest，缺失时 fail closed，禁止 mutable-tag fallback 或网络 pull。每次新 operation reserve 前
都会重验旧 source、资格继承、干净代码 revision、逐 cell 配额与三套 canary。SWE 远端部署另由
内容寻址 receipt 绑定完整 Git tracked tree、worker、Python、SWE-bench checkout 和执行路径，并在
每次 reserve 前通过只读 SSH probe 复核，不能只凭 revision 形状的目录名放行。最终报告以 24 个
instance 各自的三臂八轮均值、最高分和合规轮数为单位，不生成 benchmark 内 task 平均。
references-only composition 对旧 staging plan 使用 continuation snapshot 中的精确原始字节 SHA，
不要求历史 JSON 重新序列化；instance/arm receipt 仍必须是 canonical JSON 并逐层通过内容哈希校验。
正式 v1r8+v1r9 composition 已完成 24 instance/72 arm/576 round：LCBench 与 CompilerGym 的前六题
paired validity gate 均为 6/6，SWE-bench 为 4/6、未通过 5/6 门禁；题内 B-frozen 明显改善分数或
有效生成率，但 B-online 相对 B-frozen 的两题/suite held-out 结果方向混合。完整结果见
[`正式实验报告`](docs/reports/2026-08-06-harness-builder-cross-benchmark-final-report.md)。
Self-Evolving AI 的对象/尺度 taxonomy、直接近邻、Moss 命名冲突与 contribution 审计见
[`Self-Evolving AI Systems 文献综述`](docs/reports/2026-08-07-self-evolving-ai-systems-literature-review.md)。

下一步暂不继续旧三臂 runner，而是先执行
[`Benchmark 资格预评测与 B-online 因果验证方案`](docs/plans/2026-08-11-benchmark-qualification-and-b-online-validation.md)：
第一批只用机制不同的 AgentHPOBench 与 GDPevo；前者检查 Moss 是否超过普通采样、固定反馈 Agent
与 Random/TPE/BOHB，后者检查跨题机制能否改善 held-out。BIRD-Interact、Atrex 和 OSWorld 当前只作
未授权 reserve。所有候选必须先通过零模型可信性、headroom、普通 compute scaling、非格式 Harness
sensitivity 和跨题 motif 门禁。旧 24 题及其 Harness/Skill/Experience 只保留为历史证据，均不导入
新实验。冻结切分为 AgentHPOBench `Q7/D11/T12`，以及按完整 task group 隔离的 GDPevo
`Q6/D6/T6/Tfinal6`。新的
[`宽 Harness 与元机制执行合同`](docs/plans/2026-08-12-wide-harness-and-meta-mechanism-execution-contract.md)
冻结共同 v001 后才 fork 的四臂：`A-fixed-feedback`、`S-reflection-skill`、`B-targeted`、
`B-frozen-wide`。`B-frozen-wide` 从 v002 起要求 role、memory、tool、parent、workflow、scheduler、
recovery 七轴全部实质变化；可信编译器每轮重新实例化并安装七类 typed Python 运行组件，以新配置实际
驱动行为，并在 solution 前通过 `store_trusted_version` 以实际 `CompiledHarness` 重建并逐字核对完整
compile receipt，随后才封存逐轴稳定 configuration hash 与完整谱系。generic archive 写入必须显式标为
`fixture_only`，不能成为正式证据。
这不是操作系统或 Python 包重装，也不允许修改 Registry、evaluator、scorer 或预算。当前静态
source-lock、typed 共享 v001 artifact/archive、task/source/seed binding schema、typed outcome/
stage-interruption archive，以及 checked-in manifest 的精确 126-cell task×seed/arm-policy/arm-variant/
Latin-order 零调用 audit plan 均已实现；任意 fixture 计划被明确标成 `FIXTURE_ONLY`。新增的零调用
v001 orchestrator 会重读 pinned source、Rule Registry 与 operator source，重新编译四臂并逐字核对
完整 semantic/compile evidence；solver 也会经内置 `task_semantics` 收到精确 source-bound artifact
capability card，而不会收到其他任意 observation。
exact-plan barrier 现已独立接线并在每次 v001 bind/recovery 重验四臂 variant/contract，仍不含任何执行
callback，authority/entitlement 恒为零。source authority 从两个固定 Git object database 机械生成 42 个
solver-visible task artifacts 与 126 个 task/context-bound keys；plan 只能接受该 authority 的 canonical
bundle，并绑定 bundle SHA，barrier 构造及恢复时重新读取 pinned source、重建完整 bundle 后逐键核对，
不再接受裸 key 的自洽哈希。GDPevo 仅投影公开 input，完整 group tree 只进入 controller-private digest。
post-v001 的零调用 context authority 已能从 exact source/plan/matrix 重放 B-targeted/Wide intent，用
trusted Registry 重新编译并核对 receipt；Wide 的 accepted v002+ 强制七轴配置全部变化、所有 active
component nonce/config 不复用，拒绝轮后继续最近 accepted parent。正式 provider/operation-journal
dispatch 仍未接线。
原始 benchmark score 只在 strict public ITT row 公开；invalid typed score receipt 映射到各 Benchmark
native floor，内部正值 affine utility 不能混入报告。精确主实验计分集合现已机械展开为 1,566 个槽
（126 个共享 v001 + 两个 Benchmark 各 720 个 post-v001）；进一步从同一 pinned source/plan/matrix
展开了 4,338 个潜在外部阶段：1,206 个 update、1,566 个 solution 与 1,566 个 evaluator，满路径上限为
2,772 次模型调用和 1,566 次 evaluator transaction。A 的 post-v001 槽没有伪 update；CPU/GPU 秒仍明确
等待真实 canary，整个 schedule 保持零 entitlement 且没有 reserve/execute callback。它只是证明潜在阶段
没有漏列，不是 operation journal，也不证明失败短路后的实际 stage disposition 或任何槽已经执行。
正式 operation ledger/evaluator/optimizer/report 尚未一对一接线，因此不能声称这些槽已执行或覆盖。
零调用 semantic stage verifier 现可从 pinned source 重新派生该 schedule，并对同一 v1 journal snapshot
只重放一次，逐项核对 terminal `completed/failed` 与合法的 immediate-parent failure cascade；4,338 项
synthetic exact-set 已覆盖 1,566 个 failed root 与 2,772 个 skip。它会拒绝 schedule 外 operation、
reserved/started、failed parent 后的 child、无 artifact completion、跨 attempt/跨级 skip 和 caller 重造
receipt/seal；持久化 semantic artifact 必须结合 pinned source 与当前 ledger/head 全量重派生并逐字比对，
单独的 DTO/type/hash 都不构成 provenance。但旧 v1 reader 尚无 descriptor-relative storage、WAL、resource grant、physical retry 或
typed local-gate binding，所以该 seal 固定为 semantic fixture 的 `NOT_READY/NOT_GRANTED`，不是正式执行
证据。新 journal v2/WAL 仅有合同草案：
`docs/plans/2026-08-13-factorial-hardened-journal-v2.md`，尚未获授权实现。
S-reflection-skill 的零调用 authority 已能从同一
task/seed 的 typed public feedback 生成 bounded task-local Skill，并用冻结 v001 Harness 可信重编译后才
附加到 solution prompt；它不跨题保存状态。正式 provider、planner/Skill operation journal、solution/
evaluator dispatch、真实 canary 和非零 entitlement 仍为 `NOT_READY/NOT_GRANTED`，因此没有启动
模型调用、真实评测或产生新成绩。

AgentHPOBench 另新增零调用 strict intervention boundary：未知 key、别名、越界/nearest clamp、类型替换、
无 operational change 与 permissive JSON 都在 evaluator 前拒绝；离线 derivation 从固定 commit/tree 的
space manifest、backend 与逐 task runner 交叉推导 scalar allowlist/current config，并显式拒绝特殊的
`agent_lightning_room_selector` free-form prompt action。一个 logical decision 必须逐个登记底层 provider
request，replay 会拒绝提交多个 request。它尚未接入能证明“无遗漏”的唯一可信 transport ledger，
所以还不能宣称已排除隐藏 retry，也不能消除 GPU、数据、checkpoint/model 与 isolation canary 的环境阻断。
静态 Q0 evidence 现会重哈希 pinned Q7 的 31 个 source/control 文件、机械派生七个 original discrete
space，并实际执行 7×3 个 unknown-key/out-of-range/no-op codec negative，21/21 均在 evaluator 前拒绝且
transaction debit 为零；GDPevo 只从 Git object database 重放 commit/root/task-groups 与 Q6 的
group/env/test trees，不读取 private gold。GDPevo 四类 file manifest 尚无独立冻结算法，因而在 evidence
中保持 `UNVERIFIED`。该 artifact 明确不是 reference、environment 或 isolation canary，也不授予执行权限。

B-online 不再只测试 Experience Bank：`OM` 是内容寻址 mechanism memory，`OP` 是 typed
meta-policy，`OA` 是 typed Harness recipe/archive。它们借鉴 HyperAgents 的 archive 与 stepping-stone
风格，但各自 checkpoint/ledger 隔离，只能组合 trusted Registry 对象，不能保存或执行任意自修改代码。
零调用计划已精确展开 732 个 attempt、84 个 learned-state update 和 1,548 个逻辑模型调用。exact
benchmark×seed×mechanism lane 与 update slot 已绑定；OM/OP/OA 的 parent/child M/P/A 对象会逐步经
typed transition 重放，最终 checkpoint 必须重新派生下一题 Builder prior，O0 则证明 prior 与旧 memory
通道均为空；held-out compile 还会用同一 context 可信重编译。source terminal/operation digest 仍未由
唯一 journal 认证，完整 planner request/result、pinned online task authority、updater failure cursor 与
正式 stage gate 仍未绑定。online held-out
与主实验部分复用预声明 task identity，因此这里只能做独立状态、禁止导入主实验结果/trace 的同题机制
比较，不能称为 fresh confirmation。

旧 24 题三臂实验仍按其冻结的八轮、`4/8` 与 `5/6` 报告门禁解释；这些规则不进入本次新实验。
新合同固定两个 Benchmark、3 seeds，AgentHPOBench 每臂 6 轮、GDPevo 每臂 3 轮；正式统计边界须在
获得非零执行授权前另行冻结，且不同 Benchmark 的原始分数不得混加。

HarnessBuilder 的可执行搜索空间包含角色图、
记忆视图、可信工具、父代选择、discipline/dream/law-inversion/recombination 等规则、workflow、
scheduler、recovery 与最终 directive，不是 Prompt-only 优化。

Builder 的公开决策视图现在还包含当前候选的有界正文、哈希和长度，并在 proposal 前由 controller
确定性运行公开 allowlist 的 task/score/structure/profile/compiler/diff 工具；工具结果以
`pre_decision_tool_outputs` 进入 prompt，隐藏 evaluator 信息仍被隔离。Harness 默认保持
`single_solution`（一次 solution-call）；只有显式选择 `multi_step` 时，编译 workflow 的每个
stage 才会各自调用模型并写入独立 journal operation。每个 stage 的响应哈希、provider 和 usage
都会进入 round receipt，恢复仍禁止重发已有 operation。

`optimization_lab/harness_builder/` 已实现冻结任务流、Rule Registry、系统级 decision compiler、
内容寻址 Experience Bank/B-online checkpoint、one-shot 模型能力、哈希链操作账本、不可借用的
逐 cell 预算、三种 solution 合同，以及三个 benchmark 的可信 adapter 边界。每道题必须先封存
四臂，随后经验才能进入下一道未见题；同题复跑只能算 training diagnostic。
历史通用 Registry 保留 provenance-bound v2；当前三臂 v1r8 使用独立的 provenance-bound v3：每条方法绑定固定源码 commit/path/SHA、迁移说明和
实现/经验/迁移置信度。只有 `discipline`、`dream`、`law_inversion`、`recombination`、
`correctness_recovery` 以及新增的 `contract_compatibility` 绑定可信 operator。每个 task 的 v001
强制使用 `contract_compatibility`：先把 codec capability card 编译进角色、工具与 `verify_contract`
工作流，再允许正确性或性能搜索；后续合同失败也按精确阶段回到该规则。controller 会把可信 rule effect 注入
solution plan，并把 Registry SHA、operator 与 source refs 写入 `RuleDecisionTrace`；只换 rule 标签
或 directive 措辞不算系统级进化。通用 Registry 不含 benchmark-specific 数值阈值。

早期模型 runtime canary 已通过，但它绑定旧代码 revision，只保留为已消费的旧 segment，不能为当前 staging 解锁；
新的恢复式 runner 会独立重放旧 journal/head/summary 并从两次专用额度中扣除该次调用，当前
revision 只能再显式消费一次。CompilerGym evaluator canary 已通过；KernelBenchX reference canary 先后抓到物理 GPU4 在
单设备 namespace 内未重编号，以及 Triton 编译所需的 compiler/Python headers 未完整进入 sandbox
的问题。worker 现固定使用逻辑 GPU0、只读系统 `gcc-12/g++-12`，并挂载包含 multiarch
`pyconfig.h`、完整内容哈希绑定的 Python 3.10 header snapshot；旧失败照常入账并待新代码快照复跑。
随后第七个 reference `gelu_bf16` 的 call/correctness/timing 均成功，但官方 perf 的 input shape
与 golden schema 不同，可信 parser 按合同拒绝。正式分数仍为零，因此按冻结的全池哈希扫描规则
机械排除 schema 不一致题和固定 TritonBench commit 的同名题，最终换成首个合格的
`Fusion/fused_relu_max_pool2d_conv2d.py`；旧 seat 不退款，新题须在新 staging revision 从头
通过 reference 与三项对抗 canary，扫描证据作为 prepare source hash 冻结。
最新一次 `conv2d_w8a8` reference 仍在 call/compile 阶段失败；公开结果没有保存可证明根因的
私有 worker stderr，因此不把它猜成某个 CUDA 修复。离线审计另确认 canary 曾直接把含 146 个
`#` 分隔符和内嵌测试的 dataset task 文件当候选，绕过正式 solution codec。现在 reference
只能在完整 task SHA 匹配后机械抽取实现段，并重新通过同一 codec；preflight 会在 GPU 前拒绝
整份 task 文件。`scripts/prepare_hb_kernelbenchx_reference_canaries.py` 只读 pinned checkout，
生成不可覆盖的 content-addressed candidate/manifest；preflight 运行入口只消费该 manifest，
不再接受手工 reference 路径。该修复尚未重跑 canary，KernelBenchX 正式分数仍为零。
SWE-Perf 的八个 upstream digest 只作为基础镜像，不能直接充当正式 evaluator image。
[`SWE-Perf wrapper runbook`](docs/runbooks/hb-gen1-sweperf-wrapper.md) 与
`optimization_lab/harness_builder/sweperf_wrapper/` 提供不调用 Docker/网络的 context 生成器和
root `evaluate-stage` supervisor：每题 manifest、labels 与源码内容哈希绑定；资源固定为
10 CPU/32 GiB/512 PID；patch 只走 exact `git apply`；candidate stdout 不参与裁决；correctness
receipt 和真实 quiescence 是 performance 前置条件。攻击红测进一步证明任意 candidate Python 与
pytest JSON reporter 同进程，能伪造 outcome、call duration 和退出码；root-only 文件、FD/HMAC 或
外置进程 monitor 不能从可信观测还原冻结评分信号。production supervisor 现在会在 worker spawn
前以 `in_process_candidate_outcome_unattestable` fail closed，并把完整 capability verdict 纳入内容
哈希。实际基础镜像 digest、task-specific out-of-process oracle（需另行批准）、私有 task
command/test manifest、wrapper 构建与 canary 仍是阻断项。
`scripts/prepare_hb_sweperf_source_lock.py` 只读 pinned evaluator/dataset checkout 和 Parquet 的
七个公开列，机械核对冻结八题顺序、task hash、公开 test/functions 与 realistic problem hash。
它不会读取 gold patch/test patch/head commit，也不会调用 Docker、网络、模型或 evaluator；在
本地 RepoDigest 与候选不可伪造的结果通道尚未证明前，只写包含 capability verdict 的内容寻址
`blocked` prepare report，
绝不生成可运行的 `WrapperSourceLock`。
`optimization_lab/harness_builder/three_arm*.py`、`scripts/{prepare,run}_hb_three_arm.py` 与
`scripts/{prepare,run}_hb_three_arm_v1r9.py` 已实现
新三臂 staging、逐 arm-cell 恢复、每题封存后立即蒸馏、正式 provider composition 和最终 CSV/HTML
评分曲线。LCBench 八题与 CompilerGym 八题的无模型真实 canary 已通过；SWE-bench Verified 使用
官方源码、固定 Parquet SHA 与 digest-locked Docker 镜像，八个 gold-patch canary 也已全部通过。
正式 runner 会把格式错误、未通过 trusted compile 或在强制变化轮只改 rule/directive 措辞的 planner
输出封存为 `planner_contract_rejected` 无效轮次：已消费 planner call 不退款，不发起该轮 solution/evaluator，
下一轮从最近有效 Harness 继续。若进程在 planner/solution/evaluator started 后中断且没有 bound result，
runner 同样将该操作以 schema v3 `*_operation_abandoned` 零分轮次封存；terminal-failed 操作封存为
`*_operation_failed`。两者均保留已消费预算、禁止重发原 operation ID，并从最近有效 Harness 继续。
跨题蒸馏同样保持严格输出合同：prompt 会逐字给出冻结 Experience Record 的 14 个字段、当前
`source_instance_id`/builder checkpoint、合法 provenance event 与禁止别名列表。模型若返回
`suite/instance_id/observation/evidence_event_ids` 等自造简版，parser 仍会拒绝，不能自动补字段或改写
已完成 operation；含该结果的旧 segment 作为消费证据保留，修复后只能启用新 revision 的 clean segment。
`skills/diagnose-goal-blockers/` 是所有持久目标停滞的首个诊断入口，先核对 goal/Monitor、产物、服务
journal、operation ledger 和 revision binding，再决定等待、恢复或启用 clean segment。两个 JSON suite
的 task card 还逐字给出不可省略的顶层模板：LCBench
必须返回 `schema_version/instance_id/queries`，CompilerGym 必须返回
`schema_version/benchmark_uri/actions`；只返回 `queries` 或 `actions` 的对象继续由严格 codec 拒绝。
SWE-bench official/model patch 若仅省略普通文件的 Git `index` 行，canary 与正式 codec 现在共用同一
内容寻址兼容层确定性补入非语义 metadata，并保存 normalization trace；路径、file mode、hunk、上下文、
增删行和测试语义均不修复，仍由同一严格 validator fail closed。离线容器使用 Docker
`network_mode="none"` 禁用外网，同时显式保留 `localhost` 映射并在候选应用前做 loopback bind 预检，
避免 pytest 本机套接字依赖被误算成候选失败；不得改用会同时破坏名称解析的 SDK `network_disabled=True`。
SWE-bench 采用官方标准 threat model，明确标记为
`official_standard_candidate_visible_test_process`，不声称能抵抗候选在同一测试进程内主动伪造结果。
旧 SHE-1 与原四臂 HB-GEN-1 文档保留为历史设计依据，不再是当前实验矩阵。

KernelBench meta-train 的恢复式控制层已经实现：六个新 task 各自在完全空的跨题记忆下用同一
`B0` Builder 跑 v001–v008，得到 96 次模型调用与 48 个评分机会；只有两条历史轨迹和六条新轨迹
都已公开封存，才会使用另外 8 次调用生成 Experience Records，并冻结一个由 `B*`/`B-online`
逐字共同绑定的 checkpoint。操作都走哈希链 journal、独立 head anchor 与不可借 cell entitlement。
evaluator 结果先写入绑定 operation/cell/instance/version/candidate SHA 的 canonical controller
artifact，再由 journal 的 terminal event 绑定其 SHA；已完成结果只重放，started 且无 artifact
的尝试永久视为 abandoned，既不重发也不退款。`excluded_task_ids` 也在运行时检查整个经验记录，
不能只靠 JSON 配置声明隔离。

两条历史轨迹不再手工挑选或整理。离线 importer 在 pilot ledger lock 与 P2b
runner→ledger 双锁内复核冻结的 548/402 events、两个 plan 和全部候选/Harness/policy
artifact/parent hash，然后按 `P1 → P2 → P2b` 原追加顺序为每题生成一个 all-lanes aggregate。
它保留编译/正确性失败、P2 缺失 Harness artifact、P2b 缺失 profile artifact 和无效 policy
artifact，只输出公开决策、分数、成本、结构/profile 摘要与 provenance event ID；不复制候选代码、
raw response、私有路径或 evaluator log。任一证明失败只产生 content-addressed blocked prepare。

```bash
PYTHONPATH=. .venv/bin/python scripts/prepare_harness_builder_historical.py \
  --pilot-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot \
  --p2b-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2b-profiler \
  --output-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-historical-v1
```

冻结源当前机械得到 LayerNorm `11/24/22` 和 Matmul+Sigmoid+Sum `11/24/26` 个 P1/P2/P2b
summary；trajectory SHA-256 分别为
`f1417f07068436616f5a5d740ea60de564060eaa27f909207783afe70de16b2d` 与
`f6a6900327c65293dc6f7504d818235ae56baec9ace334043bb227320096fc00`。

只读 preflight 入口如下；它不会调用模型或 GPU。新的 KernelBench meta adapter 已经固定六题
source SHA、每 attempt 独立 scratch/cache、nonce/task/candidate/protocol/scorer 绑定的私有 JSON，
并让 candidate stdout 完全退出裁决；worker namespace 复用单物理 GPU→逻辑 GPU0、禁网、只读
源码/系统和内容哈希 Python header 的 bubblewrap 边界。`MetaTrainTask` 也已绑定这个 backend，fake
supervisor 子进程端到端通过：

```bash
PYTHONPATH=. .venv/bin/python scripts/run_harness_builder_meta_train.py \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1 \
  --historical-trajectory /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-historical-v1/trajectories/objects/f1417f07068436616f5a5d740ea60de564060eaa27f909207783afe70de16b2d.json \
  --historical-trajectory /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-historical-v1/trajectories/objects/f6a6900327c65293dc6f7504d818235ae56baec9ace334043bb227320096fc00.json
```

`CandidateInvocationABI-v1` 的离线核心现在已经实现：同一确定性 policy 在 solution codec 与生产
supervisor 内各验证一次，只接受受限 Torch/Triton `ModelNew`；文件/进程/网络、反射、pickle、
`torch.save/load/from_file`、CUDA 控制、module monkeypatch 和顶层副作用都 fail closed。可信 protocol
loop 在 candidate import 前捕获 timer/synchronize/comparator，对 5 个 correctness 和全部 100 个
measured invocation 使用新 input commitment，并逐次核验 output 与 input 未被改写；结果只有在
candidate teardown 与 process/GPU quiescence 后才可产生。policy SHA 也进入 protocol、supervisor
argv 与 nonce/task/candidate/scorer 绑定的私有 evidence。

真实 Torch/CUDA production worker 现已接入，但只完成 CPU/fake 验证，尚未获准在 GPU4 上运行。
worker 在 candidate 加载前捕获 timer/synchronize/comparator/reference，使用 supervisor 私有 HMAC
seed 为 reference 与 candidate 构造一致权重及每次新鲜输入；5 次 correctness 与 100 次 timing
全部逐次比对并绑定 schedule commitment。candidate 只能经受限、逐题绑定的 Torch/Triton policy
进入每 attempt 独立的禁网、只读 root、独立 scratch/cache、单 GPU bubblewrap namespace；结果只走
匿名 inherited fd3，且在 Torch 编译器或 candidate 可启动子进程前置为 CLOEXEC。pre/post health、
reference-state seal、timeout 与 process/GPU quiescence 均 fail closed，stdout 永不参与裁决。

这不等于 evaluator 已可正式执行：capability report 固定声明
`trusted_invocation_loop_implemented=true`、`production_runtime_implemented=true`，同时
`execution_ready=false`，blocker 为 `kernelbench_meta_canary_pending`。canary 和 formal 两种执行都要求
位于 worker 可见状态之外的内容寻址授权 receipt；canary receipt 必须绑定精确代码 revision、scorer/
protocol/task-set hash、10 个冻结 transaction 与 6,000 GPU 独占秒，formal receipt 还必须绑定通过后的
canary evidence。`KernelBenchMetaAdapter` 构造时必须绑定由外部 authority 签发、controller 只持有和消费的
mode-0600 receipt，记录
其 canonical path/SHA 并只把路径传给 trusted supervisor；缺失、改写、非内容寻址、落入 repo/attempt
worker state 都 fail closed，candidate argv/environment 永远看不到它。staging 仍没有这项独立
entitlement，正式预算未修改、资源未消费，因此当前
`--execute` 仍会在 GPU 或 candidate 加载前拒绝。

十席 KernelBench meta canary 的离线准备与恢复式 controller 也已实现。六个正例先绑定完整 task
SHA，只提取 `Model` 并机械规范化为 `ModelNew`，随后重新通过逐题 restricted policy 与正式
solution codec；四个攻击例区分 GPU 前的 `print/open` 静态拒绝，以及必须由可信调用循环抓住的
wrong/前五次正确后 timing 错误。执行顺序固定为静态拒绝→早失败→较小正例→SDPA→cumsum→
Sigmoid。每席都在副作用前 reserve/start；started 且无 artifact 永久 abandoned。全部结束后由
独立 reducer 重放 operation ledger 与外置 head anchor，再核对十个内容寻址结果、精确协议计数和 GPU
用量；独占 execute lock 防止两个 controller 重复消费同一席位。它只铸造 canary
evidence，不自动铸造 formal authority 或启动下一阶段。当前 staging 仍缺专用 entitlement，因此以下
第一条命令只准备候选，第二条默认只会报告阻断，均不会运行 GPU：

```bash
PYTHONPATH=. .venv/bin/python scripts/prepare_hb_kernelbench_meta_canary.py \
  --repository <pinned-kernelbench-checkout> \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/hb-gen1-kernelbench-meta-canary

PYTHONPATH=. .venv/bin/python scripts/run_hb_kernelbench_meta_canary.py \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1 \
  --repository <pinned-kernelbench-checkout>
```

真实 `--execute` 还必须显式传入 `--authorization-receipt <external-receipt>`；controller 不创建该文件，
preflight 也不回显其路径。缺失 receipt 时保持阻断态。

Experience Retriever 会按新题机械 descriptor 确定性检索有界记录，同时给出当时的初始 Harness、
进化方向、触发证据、收益与反例；同题记录被排除，规则只有在多个 instance、再到多个 benchmark
重复后才提高支持级别。B0 与 B* 的 planner 输入模板逐字相同，唯一实验差异是 B* 实际绑定的这些
跨题记录。

B-online 在 24 题流中只更新内容寻址 Experience Bank/checkpoint，但这些记录会让下一道新题选择
不同的初始角色图、memory/tool/workflow、父代、scheduler/recovery 和进化规则；trusted operator、
评分器与预算在本轮保持冻结。全流结束后，跨 benchmark 复制有效的机制才晋级到 Builder v2，随后
必须换 fresh instance 再测。CompilerGym 的正式八题已移除无 validator 的 `rijndael` 和忽略校验
返回值的 `sha`，换成 baseline-valid 的 `stringsearch2` 与 `blowfish`；生产评分逐个执行冻结的
ordinary validator allowlist，不调用混入失效 sanitizer 的聚合 `env.validate()`。

HB-GEN-1 固定使用 `gpt-5.6-sol`、`high` reasoning 和已登录 ChatGPT 的隔离
`codex exec 0.144.6`。
零模型、零 evaluator 的 staging 准备命令为：

```bash
PYTHONPATH=. .venv/bin/python scripts/prepare_harness_builder_gen1.py \
  --project-root /home/ubuntu/Projects/Moss \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1
```

该命令只生成带代码提交、合同哈希、24 题顺序和逐 cell entitlement 的阻断态计划；在
`model_runtime_canary_pending`、`meta_train_pending` 与 `evaluator_canaries_pending` 清除前
不会启动正式调用。

正式 prequential 控制面已实现，但仍遵守同一阻断态 staging。默认命令只校验 24 题精确顺序、
四臂 entitlement 与 `execution_ready`，不会构造 benchmark adapter、调用模型或评分器：

```bash
PYTHONPATH=. .venv/bin/python scripts/run_harness_builder_formal.py \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1
```

运行时严格按 `stream → arm_order → v001-v008` 执行；当前题 A/B0/B*/B-online 四臂全部封存后，
才允许一次 B-online distillation，得到的 bank/checkpoint 只供下一道未见题使用。A/B0 始终无跨题
经验，B* 始终绑定 meta-train bank；B* 与首题 B-online 起点相同。同一正式 instance 再次运行只会
校验并重放 immutable arm/trajectory/instance receipt，不会再次评分、学习或改写曲线。只有 staging
明确 `execution_ready=true`、命令显式带 `--execute`，并由可信 composition 注入与同一 staging SHA
绑定的 suite provider factory 后，控制器才可进入执行；当前 standalone CLI 不猜测 evaluator，
因此不能绕过尚未通过的 canary，也没有自动 P3/扩预算入口。

正式 suite-provider 组合层位于 `optimization_lab/harness_builder/formal_providers.py`。它离线复核
staging/manifest、每个 canary result、operation ledger、独立 trusted-head anchor 与 task/source/
evaluator hash；报告只暴露 hash 和 reason code。KernelBenchX 或 CompilerGym 只有在各自 gate
通过后才能单独构造 provider 供离线绑定检查，但这不产生正式 campaign authority；三-suite
factory 必须三者全部通过。CompilerGym 已消费的旧 canary 只能按精确 36-event segment 做
component rebind：adapter 必须逐字相同、codec/backend 的 canonical AST 必须相同，当前 verifier
还必须独立重放同一账本与 anchor；该证据不外推为旧新代码整体等价。SWE-Perf 当前 capability
verdict 仍是 `in_process_candidate_outcome_unattestable`，因此正式 factory 继续 fail closed。

纯离线组合预检命令为：

```bash
PYTHONPATH=. .venv/bin/python scripts/preflight_harness_builder_formal_providers.py \
  --project-root /home/ubuntu/Projects/Moss \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1 \
  --manifest /home/ubuntu/Projects/Moss/optimization_lab/harness_builder/data/hb_gen1_candidates.json \
  --kernelbenchx-repository <pinned-kernelbenchx-checkout> \
  --kernelbenchx-supervisor <trusted-supervisor.py> \
  --kernelbenchx-scratch-root <private-scratch-root> \
  --sweperf-source-lock-receipt <content-addressed-source-lock-report>
```

该命令不会调用模型、evaluator、Docker、SSH、网络或 GPU；若需要 rebind，只会在 artifact root
写入不可覆盖、内容寻址的本地兼容性 receipt。blocked 是正常的可审计预检结果，不会被当成可运行。

模型路由 canary 默认只做 preflight；只有显式增加 `--execute` 才可能调用冻结的
`gpt-5.6-sol/high/codex-cli-0.144.6/codex_chatgpt` 路由：

```bash
PYTHONPATH=. .venv/bin/python scripts/run_harness_builder_model_route_canary.py \
  --artifact-root <new-hb-gen1-artifact-root>
# 获得单独执行授权后才可在同一命令末尾增加 --execute
```

runner 把 staging/source/prompt/code revision 组成内容寻址 segment，复用共享 operation journal、
独立 head anchor 与 `canary:model-route` entitlement。completed 只重放；started 且没有 result artifact
永久 abandoned，不重发；started 且已有完整绑定的 canonical result artifact 则只补写 terminal，
不会重发 provider；旧 revision 的 passed canary 只计费、不复用。

P1 的真实执行入口使用已登录 ChatGPT 的 Codex CLI，而不是把认证信息放进候选工作区。
`CodexExecGenerator` 为每次调用创建临时、只读、无项目文件的会话，要求结构化候选输出并保存
usage JSONL；P1 runner 固定执行每题的零样本 1 轮、同预算通用流程 8 轮、人工朴素流程 2 轮，
GPU 评分仍按顺序使用 GPU4。它没有 P2 入口，P1 完成后必须重新获得授权。实时看板按 lane
显示 Kernel 候选数量、正确数、最好成绩与实际消耗，并明确 P1 的 Harness 固定不迭代。

P2 获得单独授权后使用另一条无 P3 入口的执行器。每道任务的三条谱系从逐字相同的 v001
起步；第 2–8 轮先由隔离的 Harness 优化器生成带父版本的新工作流，再由固定模型生成 Kernel。
Harness、优化器原文、Kernel、短反馈和成本都不可覆盖归档；每 lane 最多 8 次 Kernel 生成和
7 次 Harness 改版，正好受 15 次模型调用硬帽约束。连续三轮无正确结果或无速度提升时提前停止。
如果 Harness 调用已经开始但会话在归档前中断，恢复器不会悄悄重发并突破硬帽，而是记录恢复
停止事件、保留历史最好配对并冻结该谱系。

```bash
.venv/bin/python -m scripts.run_kernelbench_p2 \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot \
  --project-root /home/ubuntu/Projects/Moss
```

准备和执行 P2b（准备命令不调用模型或 GPU）：

```bash
.venv/bin/python scripts/prepare_kernelbench_p2b.py \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2b-profiler

.venv/bin/python -m scripts.run_kernelbench_p2b \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2b-profiler
```

实时页面为
`/home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2b-profiler/dashboard.html`。
看板直接从追加账本重建每条 Harness 路线的 v001–v008 分数曲线和精确明细：冻结起点为虚线、
正确候选为折线点、正确性失败为红叉；若评分已经完成但后续 Profiler/进程中断，该分数仍以橙色
点保留并标记为“轮次未封存”。
运行器持有独占锁；中断后使用同一命令恢复，已开始但无产物的模型/Profiler 尝试不会静默重发。

```bash
.venv/bin/python -m scripts.run_kernelbench_p1 \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot \
  --project-root /home/ubuntu/Projects/Moss
```

此前的
[`三层 Benchmark 迁移资格方案`](docs/plans/2026-07-28-three-tier-benchmark-qualification.md)
已完成离线协议核心与题池快照实现，但从未发起模型调用。它作为 Task-level 迁移路线的
冻结历史保留，随本次方向切换暂停；除非用户另行恢复，不进入 P3，也不消费 fresh test。

## 术语

```text
Task                 上游通用能力范围 / 目标能力分布
  ↓
Benchmark            从 Task 抽取的有限测量集合
  ↓
Benchmark instance   Benchmark 中的一道具体题目
```

Task-conditioned Harness 针对上游 Task 的稳定规律；benchmark-conditioned Harness
只适合一个有限 benchmark；instance-conditioned Harness 记忆或特判具体 instance。
单个 test benchmark 上提升只证明迁移到新的 benchmark sample，不足以单独宣称已经
泛化到整个 Task。

## 已完成 pilot 的三个历史实验问题

- **Q1**：training benchmark 上的可复制改进，能否迁移到未参与进化的 test benchmark sample？
- **Q2**：针对一个 benchmark family 演化的 Harness，换到另一个 family 后是否存在主场优势？
- **Q3**：只凭上游能力与反馈形态说明（不含 benchmark instance），能否零样本生成不差于通用
  seed 的 Harness？

## 目录结构

仓库保留历史实验以便复现，但当前开发主线是双层可执行 Harness。目录按“当前主线”和
“历史实验”区分如下；文件较早的 Git 更新时间只表示该稳定组件近期没有改动。

```
当前双层 Harness 主线
  optimization_lab/harness_builder/
    dual_harness.py              下层 Task Harness 的 typed 程序、执行 trace 与内容寻址工作区
    builder_harness.py           上层 Builder Harness 的 inspect/propose/validate/probe/commit 流程
    dual_runtime.py              Solver→公开评分→Builder 演化的可恢复单轮状态机
    experiment_one*.py           EdgeBench/ALE-Bench 实验合同、审计、生产 controller
    kernelbench_dual_*.py        KernelBench H200 双层 Harness runner 与 CLI
    adapters/{edgebench,alebench}_official.py  官方 evaluator 隔离边界
    manifests/                   冻结任务、模型、轮数、资源与 source binding
  optimization_lab/openai_generator.py       Responses API 的流式生成适配器
  scripts/run_moss_experiment_one.py          Edge/ALE 唯一生产入口（默认只读）
  scripts/run_kernelbench_dual_experiment.py  KernelBench 双层实验入口

历史、仍可复现的实验
  benchmarks/                    早期 bugfix/TDD/hidden/Q1/Q2 题库与冻结测试
  harnesses/ + family_cards/     早期 Harness 谱系与零样本任务卡
  eval.py + _eval_one.py         早期 sealed-test 唯一计分入口
  loop.py + proposer.py          训练集内 Harness 演化
  builder.py + harness_source.py 早期单层 Builder 与静态合同校验
  run_experiment.py              早期 pilot 总编排
  optimization_lab/{campaign,controller,p1_runner,p2_runner,p2b_runner}.py
                                 KernelBench P1/P2/P2b 历史执行器
  scripts/{formal_runner,q1_*,q2_*,three_tier_runner}.py
                                 历史确认实验与三层资格入口
  archive.jsonl                  早期谱系事实台账，不是临时文件

共同基础设施
  docs/plans/ + docs/reports/    冻结实验合同、演进记录与正式报告
  tests/                         离线合同、恢复、隔离和生产边界回归测试
  skills/                        高成本运行前的生成物验证与阻断诊断门禁
```

## 运行

```bash
python3 -m venv .venv
.venv/bin/pip install anthropic pytest pytest-timeout \
  pyarrow==18.1.0 numpy==2.1.3 pandas==2.2.3 \
  matplotlib==3.9.2 scipy==1.14.1 scikit-learn==1.5.2 seaborn==0.13.2
# .env.local 写入 TOKENROUTER_BASE_URL / TOKENROUTER_API_KEY(不入库)
.venv/bin/python scripts/import_quixbugs.py   # 三个导入脚本,重建题库
.venv/bin/python scripts/import_humaneval.py
.venv/bin/python scripts/import_mbpp.py
.venv/bin/python scripts/import_bigcodebench_hard_canary.py  # 下载 5 题并做 stub/oracle 门禁
.venv/bin/python scripts/import_bigcodebench_hidden.py --level V1  # 隐藏终验起始档
.venv/bin/python scripts/import_bigcodebench_hidden.py --formal --level V1  # 冻结正式池
.venv/bin/python scripts/formal_runner.py --parallel  # 隐藏终验 Q1/Q2/Q3 三-lane 受控并行
.venv/bin/python scripts/build_q2_paired.py            # 生成/验证 20 对 V0/V1 任务
.venv/bin/python scripts/q2_paired_runner.py           # Q2 配对 canary + 四格正式确认
.venv/bin/python scripts/build_q1_external.py           # 冻结 4+12 道全新外部题
.venv/bin/python scripts/q1_confirmation_runner.py --gate-only
.venv/bin/python scripts/q1_lineage_runner.py --lineage tddgen_hidden_r02
.venv/bin/python scripts/q1_confirmation_runner.py
.venv/bin/python run_experiment.py            # 全流程;中断后重跑会跳过已完成阶段
```

三层资格实验在 P3 前只允许准备不可变快照（不会调用 TokenRouter）：

```bash
.venv/bin/python scripts/three_tier_runner.py --prepare \
  --artifact-root /absolute/persistent/artifact-root
```

`artifact-root` 不得位于 `.claude-manager/worktrees/`。该命令重跑 reserve 的 V1
stub/oracle/flaky 门禁，并将 training16、validation20、fresh test34 连同文件哈希和
实例禁表写到持久化目录；它不会解封 test 或运行 Harness。

KernelBench P0 的 A100 远端评分入口：

```bash
.venv/bin/python -m optimization_lab ssh-preflight \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot
.venv/bin/python -m optimization_lab ssh-evaluate \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot \
  --task kernelbench_layernorm \
  --candidate optimization_lab/candidates/p0/layernorm_reference.py \
  --candidate-id p0-layernorm-reference-manual
```

评分事实写入 `ledger.jsonl`，完整日志隔离在 `private_evaluator/`，实时页面为同一 artifact
目录下的 `dashboard.html`。当目录中已有 `campaign_plan.json` 时，看板还会用非技术语言
展示开跑条件、P1 六个固定 Harness 对照、P2 六条独立路线和实际总消耗；已执行的 P1 lane
显示完成数、最近结果和最好分数，尚未执行的 P2 路线明确标为“待运行，不是成绩”。公开页面
只读取计划与账本中的必要字段，并隐藏内部评测路径。
远端默认使用 SSH alias `a100jump` 的 GPU 4；换硬件前必须重新冻结任务合同，不能混合比较
分数。

只准备 P1/P2 campaign 草案，不调用模型或 GPU：

```bash
.venv/bin/python -m optimization_lab prepare-campaign \
  --artifact-root /home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-pilot \
  --project-root /home/ubuntu/Projects/Moss
```

模型、每 lane 调用/GPU 上限和两个美元硬帽均不提供时，命令只冻结矩阵并列出 blocker。
P0 干净环境状态只认同一追加式账本里的自动确认事件，不能用命令行开关自行宣称通过。

单独评测某个 harness:`.venv/bin/python eval.py harnesses/bugfix/v001/harness.py benchmarks/bugfix/val --repeats 3`

## 评测协议(开跑前冻结)

- 干活模型锁死 `claude-haiku-4-5`(eval.py 静态检查,不符拒评);改进/生成模型 `claude-sonnet-4-6`。
- 判分前恢复 solution.py 以外的所有文件并校验哈希,发现篡改记 0 分。
- 含 `_hidden/test_hidden.py` 的题只把根目录文件复制给 Harness；终验在全新目录运行，
  结果只记录通过数/失败数，不保存隐藏测试名、断言或 pytest 输出。
- Harness import/文件访问经过静态沙箱与 work_dir 路径护栏；`tools.py` 的冻结实现不变。
- 生成 Harness 的提示词不得命名 `solution.py` / `test_solution.py` 之外的 Python 文件；
  Proposer/Builder 原始响应保存在 `results/generator_raw/`，合同失败候选隔离审计。
- 评测层调用冻结 `run_tests` 时把 pytest cwd 限定到临时 work/score 目录，第三方测试的
  相对路径副作用不会写入仓库或跨 task-run 污染。
- 正式分数一律 3 遍取平均;进化过程中的快速反馈 1 遍。
- Q1 独立确认按 R2-train→v001/R0/R2-external→R1-train/external 的决策价值顺序；
  24M 总上限同时计入 quick、canary、无效尝试和正式格，预算不足不降重复次数。
- 判定线见方案文档第 7 节,跑完不挪杆。
- Builder 生成物须先通过完整代码块提取、语法/冻结合同、工具参数及返回类型检查；合同失败
  最多零样本修复两次，修复过程不得看到题目或成绩。

## Moss 实验一生产入口

`scripts/run_moss_experiment_one.py` 固定 EdgeBench 与 ALE-Bench 的 A/B/C、S1/S2/S3、8 轮、
上下层 `gpt-5.6-sol`、`high` 和 Responses API。`preflight`、`report` 始终只读；其余命令缺少
`--execute` 时只输出 JSON 计划，不创建目录、不调用模型或官方评分器：

```bash
python scripts/run_moss_experiment_one.py preflight --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official
python scripts/run_moss_experiment_one.py canary --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --position A --execute
python scripts/run_moss_experiment_one.py evolve --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --seed S1 --position A --execute
python scripts/run_moss_experiment_one.py freeze --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --seed S1 --position A --execute
python scripts/run_moss_experiment_one.py cross-test --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --seed S1 --execute
python scripts/run_moss_experiment_one.py resume --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --seed S1 --position A --execute
python scripts/run_moss_experiment_one.py report --suite edgebench --root /home/ubuntu/Projects/moss-exp1-official --seed S1
```

执行前必须 source 含 `LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL=gpt-5.6-sol`、
`LLM_REASONING_EFFORT=high` 的环境，并设置对应 suite 的不可变镜像 digest，例如
`MOSS_EDGEBENCH_IMAGE_DIGEST=sha256:...`。正式目录按
`formal/<suite>/<seed>/lineages|frozen|cross|h0-baselines` 隔离，canary 单独写入
`canary/<suite>`。恢复只读取追加式状态；Builder 只能接收公开分数、短 feedback 与结构摘要，
不能接收隐藏样例、原始 judge 日志或答案正文。固定 8 轮结果属于 Harness 专门化机制证据，
不等同于使用官方完整时间预算的榜单成绩。

Builder 提出的下层 Harness 不限制模型调用次数；`draft → verify → emit` 等多阶段结构可以进入
下一轮。生产门禁只保留通用要求：结构必须通过 `TaskHarnessSpec` 校验、至少包含一次模型调用、
最终只有一个 `emit`，并且所有工具调用都来自当前 benchmark 显式提供的公开白名单。答案仍须
通过对应 benchmark 的 Contract Skill 与严格 codec，结构解禁不会放松提交格式或 evaluator 合同。
实验一会由 Python 将该公开 Contract Skill 不可删除地绑定到真正向 `emit` 提供候选的最后模型节点；
中间分析节点仍按 Builder 设计自由工作。进化轮、H0 和冻结后的交叉测试调用同一绑定函数，contract
哈希同时进入 Solver operation identity 和审计 prompt，Builder 因而可以改角色、步骤和做题方法，
但不能把 EdgeBench 的 JSON bundle 或 ALE-Bench 的 fenced source 交卷规则从下层 Harness 中删掉。

正式池按 `sha256(task_id)` 排序后奇偶分族。依赖和 oracle 质量过滤后剩余 38 题，两族各
19 题，因此按预注册下限缩为 train=8、val=10、reserve=1。bugfix AST 变异只产出 12/19
个合格题，少于所需 18，B 族已按规则回退为 `specgen_hidden`；后续 Q2 只能检验可见反馈
形态差异，不能解释为“构造式 vs 审计式”红利。
