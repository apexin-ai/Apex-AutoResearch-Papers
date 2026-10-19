# apex-moss — 项目指南

> **重要：Claude 必须自主维护本文件。** 架构或约定变化时更新，保持简洁。

## 架构速览

- 通用模型 transport 统一采用流式消费且不设置客户端时长上限：Responses API 强制
  `stream=True` 并拒绝非流式配置，OpenAI-compatible Chat 按 SSE 增量组装正文并要求 `[DONE]`，
  内建 OpenAI client、HTTP stream 与 `codex exec` 均不设置请求/进程 timeout；evaluator、SSH 和
  本地隔离操作的安全超时不受影响。
- v2 B-self 不再把 policy 仅作为 prompt 提示：`BuilderScaffoldCompiler` 将内容寻址
  `BuilderArtifact(meta_policy + task_harness_policy)` 与题目公开状态确定性编译为
  `CompiledBuilderScaffold`，机械决定诊断/记忆投影、search phase、mutation family、proposal slots、
  recovery action 及下层 `HarnessDecision`。`HarnessRuntime` 可直接执行该脚手架，不需要修改 Python
  控制器或调用 planner 解释 policy；child head 会被下一任务进程加载并重新编译。evaluator、budget、
  journal、gate、sandbox 和 task split 仍属于不可变 Controller 边界。

Harness 条件化验证实验(历史 Task-conditioned pilot:
`docs/plans/2026-07-27-task-conditioned-harness-builder-pilot.md`;隐藏终验轮:
`docs/plans/2026-07-27-hidden-final-verification-round.md`;已实现离线阶段、暂停执行的三层资格方案:
`docs/plans/2026-07-28-three-tier-benchmark-qualification.md`;当前执行方向:
`docs/plans/2026-07-31-instance-conditioned-ai-for-ai-benchmark-plan.md`):

- **当前开发主线为双层可执行 Harness**：下层 `TaskHarnessArtifact` 是由 interface、memory、
  capabilities/skills、router 以及 model/tool/skill/emit 节点组成的 schema-2 内容寻址程序，
  `TaskHarnessRuntime` 按路由执行多角色 Solver 调用并产生候选和公开 trace；上层固定 `BuilderHarness` 执行
  inspect→propose→validate→probe→commit/rollback，并只读取 evaluator 的 typed public projection。
  新增的 portfolio 控制面保留显式 champion、不可覆盖候选/Gate/promotion archive；Builder 可从同一
  champion 或历史分支生成多个小 mutation，只有绑定外部 evaluator contract、通过 Gate 且有可信提升的
  最优候选可晋升，其他 Pareto 候选继续保留。`ChampionArchivePolicy` 机械执行 60% champion、30%
  结构差异 Pareto、10% early-stable restart；同类 Gate 失败三次轮换 mutation family，自最近可信提升或
  restart 起六次停滞强制 restart。workspace 已增加 claim-bound 通用 operation result；首个接线路线为
  SimpleTES 四项 scaling-law 的八 Harness 首轮：论文 commit/SLDBench revision/`gpt-oss-120b`
  Hugging Face revision `b5c939de8f754692c1647ca79fbf85e8c1e70f8a`
  配置内容寻址冻结，Builder/Solver/evaluator 均逐操作 fail-closed，候选只在禁网 bubblewrap worker
  中看到 train label 与 test feature，test label 留在 controller。当前 reference/negative canary 与执行器
  已就绪；H100 本地 `vllm 0.10.1.1` 已对固定 revision 的 15/15 权重分片逐 SHA-256 验证并通过
  chat canary，不经过 NewAPI。正式首轮已封存八个新 Harness：最好均值仅 -0.184101，未超过冻结
  released-best 均值 0.817516；主要失败为错误使用未安装的 `sympy`、输出广播 shape 和参数预算。
  后继 clean round 改从 pinned SimpleTES commit 内公开的四项 released-best 程序起步，并逐字注入
  NumPy/SciPy-only、标量/多输出 shape ABI 和参数上限，首轮证据不改写；旧
  `evolve_once` 入口保持兼容。
  第二轮 `round-002` 已用同一 H100 本地 vLLM、离线 pinned SLDBench cache 和新合同封存 8/8
  Harness；最佳均值 `0.8731852745`（parallel `0.9999697066`、domain_mix `0.9710317465`、
  lr_bsz `0.9476659372`、u_shape `0.5740737076`，全部有效），超过冻结前次最高均值 `0.8175160871`。
  晋升冠军为 `018a7b4e36f0fa5ccf28d25122f07584d9d09f0426f25c9821ca80d7c7a146c6`；round receipt、候选、
  solver/evaluator operation result 和 gate evidence 均内容寻址封存，未重发任何 started operation。
  新增的 SimpleTES task-lineage 入口按单 task 严格执行 H0→H7：每轮先生成并评分一个 solver，
  再由同 task 的 Builder 历史驱动下一版 Harness；每条 lineage 8 次 solver/evaluator、最多 7 次 Builder，
  不再把一批八候选误标为八轮自进化。旧 portfolio 入口保留用于历史回放。
  `DualHarnessRuntime` 以 stage claim、不可覆盖结果和 round receipt 串起 Solver→evaluator→Builder，
  同一 `run_id` 可重放，started-without-result 则 fail closed。EdgeBench/ALE-Bench 实验一统一由
  `scripts/run_moss_experiment_one.py` 进入，KernelBench 双层实验由
  `scripts/run_kernelbench_dual_experiment.py` 进入；旧根目录 pilot、P1/P2/P2b、三臂和 factorial
  模块均作为历史合同或回归基线保留，不是当前生产入口。实验一 production probe 不再把
  下层 Harness 写死为一次模型调用；任意多步 model/tool/emit 结构均可通过，只要至少包含一次
  model call、最终唯一 emit 且工具全部来自公开白名单。EdgeBench/ALE-Bench 的公开输出 Contract
  Skill 由 Python 不可删除地追加到真正供给最终 emit 的模型节点，中间分析节点不受最终交卷格式
  限制；进化、H0 与 cross-test 共用同一绑定函数，contract identity 进入 Solver request/audit 证据
  。实验一 Builder 默认从当前 Ht 生成 Ht+1；如果当前单题的公开证据支持从历史 Harness 分支，
  也可以选择公开 `available_harnesses` 中的精确 hash。proposal 的 `source_sha256` 与
  `base_sha256` 必须逐字复制同一个获准 hash，并且只能以该 Harness 的公开 spec 为修改基础；
  Builder prompt 同时明确节点字段白名单，禁止模型发明运行时不支持的 `output_key`。
  V2 刷新入口与 V1 并存：CLI 默认加载冻结 V1，只有显式传入
  `--harness-version v2` 才加载 schema-2 manifest。V2 的静态工具节点和 Agent
  动态工具调用统一经过固定 `ToolRegistry`；evaluator 不在下层工具白名单内。
  cross-test 遇到 Solver/API/格式/Harness/evaluator 异常时保留原始错误审计，不生成
  分数、不把异常记为 0，也不自动 retry。
- 统一术语:`Task`=上游通用能力范围/目标分布;`Benchmark`=从 Task 抽取的有限测量集合;
  `Benchmark instance`=其中一道题。Task-conditioned 针对上游规律,
  benchmark-/instance-conditioned 分别是有限题库/具体题目的潜在过拟合
- **当前新方向**有意把具体任务专化当作目标，而非先当作过拟合失败：实验计划一首发
  KernelBench 固定 commit 的 LayerNorm 与 Matmul+Sigmoid+Sum 两题，每题独立
  Harness/谱系；P1 通过“编译→正确性→速度”即时反馈调 Kernel 候选，P2 才调 Harness
  工作流。`optimization_lab/` 已实现
  追加式账本、反馈卡、预算门禁、SSH A100 适配器和含逐轮分数曲线的实时 HTML 看板，
  不改旧 `eval.py`/
  sealed-test 合同。P0 使用 `a100jump` GPU4(A100 80GB)；原 Matmul+Subtract+Multiply+ReLU
  因全零负例通过 5/5 正确性检查而在模型调用前淘汰。当前正反例和三次计时稳定性已过，
  P0 也已在全新锁文件环境的隔离容器中复现：只映射 GPU4 设备节点及只读宿主驱动库，
  禁网、只读根文件系统、容器内仅见一张 A100，错误候选均为 0/5、参考候选均为 5/5。
  因而不再依赖主机缺失的 NVIDIA Container Toolkit/runtime/CDI。P0 门禁已通过
- P1 已真实完成、P2 已获授权并完成执行器实现:`campaign.py` 冻结每题三种 P1 基线、每题
  三条逐字相同 seed/历史隔离的 P2 谱系与 lane 预算占位；`optimizer.py` 机械执行八轮、
  连续三轮停止/历史最好/恢复规则；`generation.py` 只给模型脱敏短反馈，强制单一完整
  `ModelNew` 代码块并追加归档原始响应；`controller.py` 已用 fake generator/adapter 走通
  单个 P1 lane 的生成→归档→评分→短反馈→预算/账本闭环，草案状态和重复 candidate ID 均
  不会消费调用。`codex_generator.py` 通过 ChatGPT 登录的 `codex exec` 在隔离、只读、临时会话
  中生成结构化候选，剥离 API/TokenRouter 密钥并记录 JSONL usage；`p1_runner.py` 只执行冻结的
  六组 P1 基线（1/8/2 轮），按 lane 恢复预算和短反馈。`harness_evolution.py` 为每条 P2 谱系
  保存不可覆盖、带父版本的 Harness 档案并生成隔离提案；`p2_runner.py` 从共同 v001 起步，
  每轮用新版 Harness 生成 Kernel，复用 `LineageTracker` 的八轮/连续三轮停止规则，恢复时将
  Harness 与 Kernel 模型调用共同计入 lane 硬帽，且没有 P3 入口。真实 P1 固定
  `gpt-5.6-sol`、每 lane 15 次模型调用/
  3600 GPU 秒及 API/GPU 各 100 美元硬帽；六个固定 Harness lane 已完成 1/8/2 轮，共 22 个
  Kernel 候选、22 个有效评分、17 个正确，GPU 计时约 723 秒，API 账本费用为 0。LayerNorm
  同预算通用流程最好 19.86×，Matmul+Sigmoid+Sum 最好 1.006×。首次静态规则拒绝曾被误分为
  环境错误，现以追加纠正事件覆盖，不改旧事实、不重跑候选。P2 已真实完成六条谱系，共 47 个
  有效评分、45 个正确候选、约 1661 GPU 秒；LayerNorm 三条最好为 19.82×/19.68×/5.70×，
  未超过 P1 的 19.86×，Matmul+Sigmoid+Sum 三条最好为 1.85×/4.10×/3.45×，均超过 P1
  的 1.006×。五条跑满八轮；最后一条第八轮 Harness 调用被会话中断，恢复器保留已消费调用并
  在七个有效轮次安全冻结，不突破 15 次 lane 硬帽。看板、Harness/Kernel 配对和原始响应均已
  归档；P3 无事件且必须另行授权
- P2b 已获授权，冻结方案为
  `docs/plans/2026-08-02-kernelbench-p2b-profiler-guided-harness-exploration.md`：两题各四条不同
  路线（分析强解/架构重建/反向假设/前沿重组），每条 v001–v008 一版 Harness 对应一个
  Kernel；结构化 Harness 真正控制代码起点、任务内 Skill、工具、记忆视图、工作流和 Kernel
  结构范围。每轮都看当前/上一轮/历史最好/冻结起点分数；小于 2% 为噪声区，无可信提升必须
  换搜索维度，第六轮满足条件时强制重启，不使用 P2 三轮早停。`p2b_plan.py`/`p2b_policy.py`/
  `p2b_runner.py` 使用独立计划、追加账本、八 lane 恢复预算和无 P3 入口；`ssh_profiler.py`
  已在 GPU4 对冻结正确 LayerNorm 候选完成 Tier A 端到端预检，自动得到 3 Kernel/30 launch、
  最大 48 registers/thread、32B shared 和 62.5% 静态理论 Occupancy。`nsys`、Triton cache 与
  `cuobjdump` 可用；`ncu`/管理员硬件计数器不可用，achieved occupancy、DRAM/L2、stall 必须
  明示缺失。正式产物根固定为
  `/home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2b-profiler`；正式 P2b 已写入
  phase completed，八条路线均已停止，但只有 writer/ledger 双锁、稳定哈希、terminal lane 和
  逐 lane 保守预算重放全部通过后才可成为下游 source snapshot。看板保留每版 Harness 的精确
  分数、错误断点及评分后中断但未封存的尝试。上限 64 Kernel、120 模型调用、14,400 GPU 秒，
  P3 仍需另行授权
- P2c 追加式自适应分配仅完成方案、尚未实现或授权执行，见
  `docs/plans/2026-08-02-kernelbench-p2c-adaptive-resource-allocation.md`。它不改 P2b 合同，待 P2b
  完成冻结后按 Task 独立快照；先给格式/基础设施中断路线一次恢复名额，再用绝对前沿、2% 可信
  斜率、正确率和粗结构新颖度做两轮一段的 top-k 竞赛。拟议新硬帽为 32 Kernel、80 模型调用、
  7,200 GPU 秒及 API/GPU 各 100 美元；两题各自硬帽不可借用，P3 仍无自动入口。用户已暂停
  该 POC 的实现，它不是当前实现方向
- **当前用户确认的执行覆盖层**：正式矩阵改为 YAHPO Gym/LCBench、CompilerGym cBench、
  SWE-bench Verified 各 8 题，三臂为 `A/B-frozen/B-online`，不导入 KernelBench 或 P1/P2/P2b 历史。
  三套环境并行准备，正式任务按冻结的平衡交错流串行执行：八个 task block 各含三个 suite 的同位置题，
  block 内 suite 首发顺序循环轮转；每 suite 前六题在三臂封存后立刻只用 B-online 自身轨迹做
  test-then-learn，经验只影响混合流中的下一题，后两题只评分不学习。每题/arm 固定八次尝试，均值和
  最高分只取有效数值轮；不足 4/8 标记 `insufficient_validity` 并排除性能统计。每 suite 前六题至少
  5/6 道同时满足 B-frozen 与 B-online 的 4/8，才允许输出跨题均值、OLS 斜率和 T6−T1。原始分数不跨
  suite 混合，只用通过门禁后的相对 B-online 优势作跨 benchmark 摘要。
  `three_arm.py`/`three_arm_prepare.py`/`three_arm_runtime.py`/`three_arm_providers.py` 已实现新 schema、
  逐 arm-cell 恢复、空 checkpoint、staging/source/gate binding 与 production composition；
  `three_arm_report.py` 只在 24×3×8 全封存后生成曲线。三套 suite 的八题真实 canary 均已 8/8 通过；
  SWE-bench 固定官方 commit、Parquet SHA、八题与镜像 digest；v1r8 的 official/model patch 共用严格
  compatibility layer，只可确定性补齐普通文件缺失的非语义 Git `index` 行，路径/hunk/语义不修复。
  Rule Registry v3 新增强制 v001 的 `contract_compatibility`：Builder 必须先读取 task-bound artifact
  capability card 并编译 `verify_contract` 工作流；合同失败原因码反馈后续 Harness。正式 v1r1 staging 已冻结，首题 A 臂
  8/8 与 B-frozen v001 已封存；B-frozen v002 的 planner 只改 rule/directive、没有 operational change，暴露
  原 runner 会把生成合同拒绝误升级为全局基础设施阻断。恢复语义现将格式/compile/无 operational change
  的 planner 输出封存为 `planner_contract_rejected` 零分轮次，保留已消费 call、跳过该轮 solution/evaluator，
  并从最近有效 Harness 继续；一次性 A 臂 v001 无效时后续只能 sham-reject，不能重新初始化。后继 v1r2
  在新 runtime 下成功启动，但 LCBench 前两轮虽生成合法 16-query 内容，却都省略顶层 `schema_version`/
  `instance_id` 而被 codec 拒绝；该 segment 已保留并停止。LCBench/CompilerGym task card 现逐字注入完整
  三字段顶层模板、task binding、字段范围/allowlist，严格 codec 不放宽，待新 clean revision segment 复跑。
  v1r3 随后完成 LCBench 首题三臂及 CompilerGym `dijkstra` 的 B-frozen，共封存 1/24 instances、4/72
  arms、35/576 rounds；用户会话生命周期于 B-online v004 planner started 后显式停止 systemd，且该调用
  没有 bound result。该 segment 保留为已消费证据，不原地重发。runner 现将 planner/solution/evaluator 的
  started-without-artifact 或 terminal-failed operation 封存为 schema v3 零分轮次，预算保持扣除、原
  operation ID 永不重试，后继轮从最近有效 Harness 继续；source revision 变化时必须新建 clean segment。
  v1r4 在首题 24 轮、三臂封存后的 B-online distillation 暴露另一生成合同缺口：模型返回了自造的
  `suite/instance_id/observation/evidence_event_ids` 简版，而非冻结的 14 字段 Experience Record，三次
  formal attempt 均在严格 parser 处失败。该 segment 与 completed distillation operation 保留为消费证据；
  distillation prompt 现逐字注入完整 14 字段模板、当前 source/checkpoint/provenance binding 与禁止别名
  约束，parser、预算和 test-then-learn 边界不放宽，后继 revision 必须用 clean segment。
  v1r5 在旧平衡交错协议下封存 38/576 rounds、4/72 arms、1/24 instances 后，其 user-session
  systemd manager 显式停止；`dijkstra/B-online/evaluator:v007` started 且无 bound artifact，必须永久
  计费并保留。用户随后曾冻结 suite-blocked 顺序与新八轮均值统计，因此 v1r5 未原地恢复；v1r6
  绑定 schema v3、`stream_policy=suite_blocked` 和新的五报告生成器，从空 Experience Bank 建立。
  v1r6 随后在 suite-blocked schema 下推进到 42/576 rounds、5/72 arms、1/24 instances；用户重新选择
  平衡交错流后，system service 被显式禁用，最新 `yahpo-lcbench:168331/A/sham_planner_call:v003`
  started-without-artifact 永久计费且不重发。v1r6 保留为消费证据；v1r7 绑定 schema v4 平衡交错流，
  但第三题 SWE-bench 三臂均 0 有效，暴露正式 codec 未共享 canary 的 index compatibility 与 B-online
  跨题 memory 静态排除错误。后继 v1r8 必须绑定 schema v5、Rule Registry v3、动态内容寻址 memory
  grant、4/8 与 5/6 有效性门禁，并从 clean segment 验证 `sphinx-doc__sphinx-8459` 至少达到单臂 4/8
  后再继续正式 task 流。
  v1r8 最终安全停止在 6/24 sealed instances；其前缀通过内容寻址 source manifest/snapshot 只读引用，
  `scikit-learn-14983` 的 planner/solution 与 started sham-planner 保留全部扣费证据但不进入学习或成绩。
  后继 v1r9 使用 schema v6，逻辑流仍为 24 题但只授权 index 6–23；A/B-frozen 从空经验开始，只有
  B-online 导入前六题 checkpoint/Bank。未开始的六个 SWE 位置改为六仓库、F2P>=6 且占计分测试至少
  1% 的哈希排序集合：pytest-7205、matplotlib-25775、xarray-4356、sympy-21930、astropy-13977、
  pylint-4604；requests-2317 的 gold canary 因冻结禁网合同下依赖外部 httpbin 而被明确排除，不进入
  正式成绩或学习。资格继承必须绑定 v1r8 8轮证据、候选/codec/adapter/validator 语义等价、新六题 6/6
  gold canary 和 locked-image acquisition 的三项 fail-closed 红测，且为 0 model/0 evaluator、不得复用
  正式分数。每次 reserve 前重验旧 source、资格 receipt、clean revision/source hashes、三套 canary、
  Rule Registry、精确 task/arm 顺序和 suite-specific cell cap；SWE worker 不允许 mutable fallback/pull，
  formal 远端执行根必须与 canary 相同。远端部署 receipt 还绑定完整 Moss tracked-tree manifest、worker
  SHA、远端 Python 二进制身份和干净 SWE-bench commit，并在每次 reserve 前用只读 SSH probe 复核。
  完成后用 references-only composition 组合 v1r8 6题与 v1r9 18题，
  报告按 instance 输出三臂八轮均值、最高分和合规轮数，不做 benchmark 内 task 平均；旧 source
  staging 只需与 snapshot 的原始字节 SHA 精确一致，receipt 仍强制 canonical JSON 与逐层哈希。
  正式 composition 现已封存 24 instance/72 arm/576 round；v1r9 system service 于
  2026-08-06 07:27:49 UTC 以 0/SUCCESS 自然退出。LCBench/CompilerGym 前六题 paired gate 均为
  6/6，SWE-bench 为 4/6、未通过 5/6；B-frozen 对题内分数/有效率有明确改善，B-online 的每 suite
  两题 sealed holdout 一正一负或不可判定，尚无稳定跨题正迁移证据。最终报告：
  `docs/reports/2026-08-06-harness-builder-cross-benchmark-final-report.md`
  SWE-bench trust grade 为 `official_standard_candidate_visible_test_process`，不外推为对抗式可信评分。
  positions 7–8 只禁止题后写入跨题 Experience Bank，仍允许当前题八轮 evaluator feedback；因此只称
  `cross-instance-transfer holdout under allowed within-instance adaptation`。Self-Evolving AI 相关工作、
  同名 MOSS 冲突与 contribution 边界见
  `docs/reports/2026-08-07-self-evolving-ai-systems-literature-review.md`
- **下一步实验已完成静态合同及零调用/compile-only 基础设施，尚未授权正式执行**，见
  `docs/plans/2026-08-11-benchmark-qualification-and-b-online-validation.md`。新方案把“方法是否胜过普通
  compute scaling/领域强基线”和“B-online 是否跨题迁移”拆成两个门：当前首批只保留机制明显不同的
  AgentHPOBench 与 GDPevo；BIRD-Interact、Atrex 和 OSWorld 作为未授权 reserve。
  冻结 selector 为 AgentHPOBench `Q7/D11/T12`、GDPevo `Q6/D6/T6/Tfinal6`，后者始终按完整
  task group 隔离。
  每个候选先过 reference/negative/leakage、headroom、`N=1/2/4` 普通 scaling、非格式 Harness
  sensitivity 与 transfer-topology 门禁；正式因子改为 Experience `E0/E1` × 题内 Harness 更新 `H0/H1`，
  solver 的 benchmark-native feedback 在四格保持一致。8–12 个 held-out 只作 exploratory go/no-go，
  要声称显著需 fresh 24+ tasks、3 seeds 与 cluster-aware paired inference；旧 v1r8/v1r9 不导入、不续跑。
  后继 `docs/plans/2026-08-12-wide-harness-and-meta-mechanism-execution-contract.md` 冻结
  `A-fixed-feedback / S-reflection-skill / B-targeted / B-frozen-wide`，并将 B-online 拆成隔离的 `OM`
  内容寻址 memory、`OP` typed meta-policy 与 `OA` typed Harness archive。`B-frozen-wide` 的 accepted
  v002+ 必须七轴全变、完整 lineage fingerprint 不复用；七类 trusted Python runtime component 每次
  compile 都重新实例化并实际驱动 parent/memory/tool/workflow/scheduler/recovery/role 行为，solution 前
  只能通过 `store_trusted_version` 用实际 `CompiledHarness` 重建并逐字核对后写内容寻址 v2 receipt
  （含 task/context binding）；generic store 显式为 fixture-only。wide campaign replay 会绑定 provider 并逐轮 trusted
  recompile。arm-independent v001 typed trunk/archive 已补 full compiled-Harness semantic projection 与
  typed task/source/seed binding schema；专用 exact-plan
  zero-call controller 已接线，在共同 v001 的每次 bind/recovery 重验四臂 variant、policy、contract 与 fork
  receipt，且不暴露 provider callback。source authority 从两个 pinned Git object database 机械重建 42 个
  solver-visible task artifact 与 126 个 task/context-bound key；GDPevo 只向 solver 投影公开 input，私有
  evaluator/gold 仅进入 controller-side binding。exact plan 只接受经 authority 重放的 canonical bundle 并
  绑定其 SHA；barrier 构造及每次 v001 bind/recovery 都重读 pinned source、重建 bundle 后逐键核对，裸 key/
  self-rehashed bundle 不能进入 formal barrier。typed outcome/stage-interruption archive 将 `ENVIRONMENT_INVALID` 限为可换环境
  重试的 attempt，并保存中断时真实完成前缀。strict zero-call formal plan 从 checked-in manifest 展开
  126 个 task×seed cell，绑定 arm policy、完整 arm variant digest、精确轮数与 Latin position balance；
  任意计划仍保持 `NOT_GRANTED` 与零 entitlement。AgentHPO strict intervention/space/request receipt 已离线实现，拒绝
  alias、clamp、fallback 与 no-op；11 个 scalar task 已从 pinned commit/tree 的 manifest/backend/runner AST
  机械派生精确离散空间（包括 JSON `null`），free-form room-selector 仍需专用 codec 或 fresh split。
  source-bound 零调用 v001 orchestrator 会重读 pinned source、exact plan、Rule Registry/operator source，
  四次重编译并逐字核对 complete compile evidence；artifact capability 通过 allowlisted `task_semantics` 精确
  进入 solver prompt。exact ITT artifact 已把 typed invalid receipt 绑定到 Benchmark native floor，公开 report
  row 仅含 raw score；exact coverage 已列出 126 个共享 v001 加两个 Benchmark 各 720 个 post-v001 槽，
  并机械展开 4,338 个潜在外部 stage（1,206 update/1,566 solution/1,566 evaluator，满路径
  2,772 model/1,566 evaluator）；A post-v001 无 update，逐 cell 离散上限已冻结，CPU/GPU 秒保持 real-canary
  pending，schedule 无 reserve/execute callback。semantic-only stage verifier 已在单一 v1 snapshot 上一次
  replay 4,338 项 synthetic exact-set（1,566 failed roots + 2,772 immediate-parent skips），并拒绝 extra/
  nonterminal/无 artifact completion/跨级或 caller 重造证据；持久化 artifact 必须用 pinned source 与当前
  ledger/head 全量重派生并逐字比对，standalone DTO 不构成 provenance。但它固定 `NOT_READY/NOT_GRANTED`，不属于
  hardened formal evidence。版本化 journal v2/pending-WAL 仅有
  `docs/plans/2026-08-13-factorial-hardened-journal-v2.md` 未授权草案。能证明 request 无遗漏的唯一 hardened
  transport ledger、typed local-gate disposition 与全部 reserved attempt 的 evaluator/optimizer/report
  一对一 dispatch 仍缺失。
  post-v001 的零调用 authority 已在 pinned AgentHPO/GDPevo source 上重放 exact
  slot/context：B-targeted trusted compile 至少一轴变化，B-frozen-wide 的 accepted v002+ 七轴配置全变、
  active component nonce/config 与历史不复用，已有 intent 的 rejected round 后继续最近 accepted parent。
  S 的零调用 authority 只允许同 task/seed bounded Skill，冻结 v001 Harness trusted recompile 后才附加到
  solution prompt。二者尚未绑定正式 provider/operation journal/evaluator。
  B-online 零调用计划固定 732 attempts/84 updates/1,548 logical calls，并明确其 T_fresh
  identity 与主实验重合，只能禁止主实验结果/trace/state 输入后做同题机制比较，不能称独立 fresh
  confirmation；exact 16 lanes 和 source/update slot 已重放，OM/OP/OA 的 typed M/P/A transition、final
  checkpoint→held-out Builder prior、O0 零注入和同-context trusted compile 已有零调用验证。source/
  operation digest 尚未由真实 journal 认证，完整 planner request/result、online task authority、updater
  failure cursor 与 stage gate 仍未绑定。零调用 static Q0 evidence 已重放 AgentHPO Q7 31 个 source 文件、
  七个 original space 和 21/21 evaluator 前 strict-codec negative，并从 GDPevo Git ODB 核对 commit/root/
  task-groups 与 Q6 group/env/test trees；它不读 private gold，未独立复算的 file-manifest 聚合显式保持
  `UNVERIFIED`，且不属于 reference/environment/isolation canary。当前开发机无 GPU/OCI/Conda 且根盘
  余量约 1.7 GiB；历史 A100 alias 当前不可达，可达 jump 也只有 2 CPU/约 1.6 GiB RAM，不能承载正式 Q0。
  正式 provider/Skill/score dispatch、真实 evaluator canary、环境/
  资源预算 authority 与非零 entitlement 仍 `NOT_READY/NOT_GRANTED`；B-online 只能并行准备，不得在
  qualification 门通过前正式执行，也不得
  启动模型或 evaluator 调用。AgentHPO/GDPevo 是全新实验，旧 24 题结果、Harness、Skill 与 Experience
  均不导入、不改写
- 以下原 `HB-GEN-1` 四臂设计只保留为历史实现背景，不再控制当前正式执行：
  `docs/plans/2026-08-02-harness-builder-cross-benchmark-generalization.md`。KernelBench 8 题只作
  meta-train；正式首次见面流固定为 KernelBenchX、CompilerGym cBench、SWE-Perf 各 8 题。
  `A/B0/B*/B-online` 四臂将一次性 task-conditioned Harness、无跨题经验 Builder、离线跨题经验
  Builder 与严格 test-then-learn Builder 分开；当前 instance 四臂封存前禁止更新，封存经验只影响
  下一道未见题；B-online checkpoint 可据此改变下一题的角色图、memory/tool/workflow、父代与调度，
  但本轮 trusted operator/scorer/budget 保持冻结，跨 benchmark 复制有效的机制只在轮后提升经验
  支持或进入下一版 Registry 提案。
  `optimization_lab/harness_builder/` 已实现系统级 decision compiler、真实父代/
  memory/tool/workflow/scheduler/recovery 语义、Rule Registry、内容寻址 Experience Bank、一次性
  模型能力、哈希链操作账本、逐 cell 不可借预算、三种 solution 合同及三个 evaluator adapter
  边界。Rule Registry 已升级为 provenance-bound v2：固定 source commit/path/SHA、迁移说明和三轴
  置信度；只有 discipline/dream/law_inversion/recombination/correctness_recovery 五条绑定 trusted
  operator，八条未接线方法仅作为 planner advisory，cross_instance_distillation 仍为外层 post-seal
  动作。planner/solution 均收到可信 rule effect，编译产物保存 RuleDecisionTrace；只换 rule 标签不计
  operational change，task 数值阈值保持在冻结合同/profile 外置。模型签名固定为
  `gpt-5.6-sol`/`high`/登录态 `codex exec 0.144.6`，另预留两次 runtime canary。
  总 entitlement 为 1,666 model calls、1,138 evaluator transaction、246,600 GPU 独占秒和
  1,416,000 CPU evaluator 秒，低于冻结硬帽。CompilerGym 移除无可信语义 gate 的 rijndael/sha，
  改用 stringsearch2/blowfish，并只执行 source/index 哈希绑定的 ordinary validator allowlist。
  旧 model runtime canary 与 CompilerGym evaluator canary 已通过，但前者绑定旧 code revision，
  只能作为已消费 segment 保留。`model_route_canary.py` 与显式 `--execute` CLI 会把 clean full
  revision、staging/source/prompt hash 和精确 model/provider/client/reasoning 绑定到新 segment；
  旧 journal/head/summary 经独立重放后只扣费、不复用，因此两次专用 entitlement 中当前仅余一次。
  completed 只重放，started 无 artifact 永久 abandoned。KernelBenchX reference canary
  抓到单设备 namespace 内错误复用宿主 GPU4 ordinal，以及 Triton 编译器和 Python headers 未
  完整进入 sandbox 的问题；worker 现把物理 GPU4 映射为逻辑 GPU0，显式使用只读版本化
  `gcc-12/g++-12`，并通过 `CPATH` 挂载同时含 `Python.h` 和 multiarch `pyconfig.h`、完整树哈希
  绑定的 Python 3.10 header snapshot。旧失败不退款
  并要求新代码快照复跑。随后 `gelu_bf16` reference 虽完成 call/correctness/timing，但官方 perf
  shape 与 golden schema 不可精确绑定；正式分数仍为零，故按冻结全池哈希后继规则，排除
  TritonBench `603e28a...` 同名和 schema 不一致项后改用首个合格的
  `Fusion/fused_relu_max_pool2d_conv2d.py`，保留失败 seat 且在新 revision 重跑全部 canary。
  新 revision 的首个 `conv2d_w8a8` reference 又在 call/compile 阶段失败，公开 artifact 不含足以
  判定底层异常的私有 stderr；离线审计同时发现 canary 绕过 solution codec，把含 dataset 分隔符/
  tests 的整份 task source 当候选。现已增加 task-SHA 绑定的实现段抽取，并让 reference preflight
  只消费离线 prepare CLI 生成、不可覆盖且内容寻址的 candidate manifest，复用正式 codec、在 GPU
  前拒绝整份 task 文件或手工 candidate 路径；尚未重跑，KernelBenchX 仍阻断。
  KernelBench meta-train 已新增独立恢复式 runner：六个新任务都用
  无跨题经验的冻结 B0 跑八轮，全部封存后才允许把两条历史轨迹与六条新轨迹做八次蒸馏；B* 与
  B-online 绑定逐字相同的内容寻址 checkpoint，formal heldout ID 在 Experience Record 全文和运行时
  memory 两层均 fail closed。历史两题由 `historical_import.py`/离线 prepare CLI 按冻结
  P1→P2→P2b ledger 原序生成每题一个 all-lanes aggregate，纳入所有 terminal 成败及中断 artifact，
  双锁双读复核 548/402 events、四个 plan/ledger SHA 和候选/Harness/policy parent hash；任何漂移只写
  blocked prepare。当前公开 trajectory hash 为 `f1417f0...6b2d`/`f6a6900...fc00`，不含候选源码、
  raw response、私有路径或 evaluator log。evaluator 完成事实绑定 canonical controller-result artifact；恢复时
  completed 只重放，started+artifact 补记 terminal，started 无 artifact 永久 abandoned，不会重发
  或退款。fake 端到端已覆盖 104 calls/48 eval 及零新增调用恢复。formal prequential runner 也已
  离线实现：严格按 staging stream/arm_order 执行四臂 v001-v008，四臂封存后恰好一次 B-online
  distillation；A/B0/B* 经验边界固定，在线 checkpoint 只前流到下一题。同题重跑只验证 immutable
  arm/trajectory/instance receipt，模型/evaluator/学习均为零；CLI 默认 preflight，只有显式
  `--execute`、ready staging 与 staging-bound suite provider factory 同时成立才能进入 runner，且无
  自动 P3/扩预算。`formal_providers.py`/离线 preflight CLI 已实现正式 composition：逐 suite 重放
  canary ledger 与独立 head anchor，并把 staging/manifest/task/source/evaluator hash 绑定到 provider；
  单 suite 通过只允许离线检查，三-suite factory 必须全部通过。CompilerGym 的旧 12-seat canary
  只对精确 36-event segment 做 adapter-byte、codec/backend AST 和当前 verifier 重放的内容寻址 rebind，
  不声称全局代码等价；SWE-Perf capability verdict 仍机械阻断 factory。KernelBench meta 已新增固定六题
  source SHA、每 attempt 独立 scratch/cache、nonce/task/candidate/protocol/scorer 绑定私有 JSON且
  完全忽略 stdout 的 adapter/backend，并复用单物理 GPU→逻辑 GPU0、禁网、只读 source/system、
  内容哈希 Python header 的 bubblewrap namespace；subprocess fake supervisor E2E 已通过。pinned
  KernelBench meta 已新增 `CandidateInvocationABI-v1` 离线核心：codec 与 supervisor 双重执行内容哈希
  绑定的 Restricted Torch/Triton AST policy，禁止文件/进程/网络、反射、持久化、CUDA control 与
  module monkeypatch；可信 protocol loop 在 import 前捕获 timer/synchronize/comparator，对 5 次
  correctness 和 100 次 timing 的每个新鲜输入/output 都逐次核验，并在 process/GPU quiescence 前
  拒绝结果。policy SHA 已绑定私有 evidence。真实 Torch/CUDA production worker 已接入并通过
  CPU/fake 合同测试：每 attempt 独立只读/禁网/scratch/cache namespace，supervisor 私有 HMAC input
  seed，匿名 fd3 在 runtime import 前 CLOEXEC，pre/post health 与 reference-state seal 均 fail closed。
  但 capability report 仍固定 `execution_ready=false`，blocker 为 `kernelbench_meta_canary_pending`；
  canary/formal 必须各有 worker 不可见的内容寻址授权 receipt，后者还绑定通过后的 canary evidence。
  adapter 构造时强制绑定外部签发、controller 只持有/消费的 mode-0600 receipt 的 path/SHA，只向 trusted supervisor
  传路径；缺失、漂移、非内容寻址或落入 repo/attempt worker state 均 fail closed，candidate argv/env
  不可见。staging 没有独立 entitlement，冻结的 10 个 canary seat×600 GPU 独占秒尚未写入正式预算或消费。
  `kernelbench_meta_canary.py` 已实现零 GPU 的六正四攻候选固化、external receipt、独占执行锁、逐席
  reserve/start、永久 abandoned 恢复语义与独立 ledger/head/协议计数重放；通过后也只写 canary evidence，
  不自动铸造 formal authority。两项静态攻击明确在 policy 层终止，其余八项才可进入 GPU。
  受限 policy 还按六题绑定 task-specific Torch/Functional/Tensor/TL capability，且 `self.*()` 只能调用已
  声明 helper 或 `__init__` 创建的明确 `nn.Module`。SWE-Perf 的 upstream digest 只作为基础镜像；
  新离线 wrapper context 生成器会
  加入 root `evaluate-stage`、逐题 manifest/labels/content hash、10 CPU/32 GiB/512 PID 固定 envelope、
  exact apply、receipt 与真实 quiescence；攻击红测证明任意 candidate Python 与 pytest JSON reporter
  同处 uid-65534 进程，可伪造 outcome/call-duration/退出码，root-only 文件、FD/HMAC 或外置 monitor
  不能从冻结语义下的可信观测还原这些信号。production supervisor 现于 spawn 前固定 fail closed；
  纯离线 source-lock preparer 只投影七个公开 Parquet 字段、核对 frozen 八题，并把内容寻址
  `in_process_candidate_outcome_unattestable` capability verdict 写入 blocked report。继续 SWE-Perf 必须
  另行批准 task-specific out-of-process oracle；本地 RepoDigest/source lock/build/canary 亦未完成。
  KernelBench meta canary entitlement、SWE-Perf 产物门禁及其余 evaluator canary 继续阻断，
  未启动正式 24 题搜索；
  旧 SHE-1 文档只作历史设计依据
- 历史三层 optimizer 资格实验不混入 Builder:两条逐字相同 v001 lineage;
  `scripts/three_tier_runner.py` 已实现 P0/P2 离线快照、精确 selector/formal gate、
  实例特判 linter 与 test-once 状态机；Proposer 只见 training16,selector 只见
  validation20 聚合,test34 全程密封并一次解封。该路线尚未发起模型调用，随研究方向
  切换暂停；除非用户另行恢复，不进入 P3，也不消费 fresh test
- `benchmarks/<family>/<train|val>/<instance>/`:题库,统一 `solution.py` + `test_solution.py`;族=bugfix/tddgen
- `benchmarks/tddgen_hard/canary/`:5 道 BigCodeBench-Hard 非正式难度校准题；导入脚本先验证 stub 失败/oracle 通过，正式扩题前目标 v001=50–80%
- `benchmarks/tddgen_hidden/canary/`:同 5 题的 V1 隐藏终验校准；v001=4/5 后已冻结 V1，只暴露 1 个行为测试，`_hidden/test_hidden.py` 仅评分器可见
- `benchmarks/tddgen_hidden/{train,val}`:V1 正式构造族(8/10)；`benchmarks/specgen_hidden/{train,val}`:预注册回退的 V0 纯规格族(8/10)
- `benchmarks/q2_paired/`:原 20 道 val 的 V0/V1 同题配对视图；只允许 `test_solution.py` 不同，用 v001/v005 的 paired difference-in-differences 消除题池难度混淆
- `benchmarks/q1_external/`:固定新增 matplotlib/scipy/sklearn/seaborn 后，从未进旧 pool 的 V1 任务按 SHA 机械冻结为 canary4/val12；外部分数不得反馈进化
- `eval.py` + `_eval_one.py`:**唯一计分入口**。防作弊(恢复+哈希、路径护栏、测试 cwd 限定、生成 Harness 静态沙箱)、隐藏终验只落计数、模型锁、正式 3 遍/快速 1 遍、子进程硬超时
- `loop.py`(单族进化,只见 train)→ `proposer.py`(sonnet 诊断失败出新版)→ `archive.jsonl`(谱系台账)；生成原文保存在 `results/generator_raw/`
- `builder.py` + `harness_source.py`:读 `family_cards/<family>.md` 零样本生成 harness，并在落盘前校验完整代码块、语法、冻结合同、工具调用及不得命名第三个 `.py` 文件
- 当前 `optimization_lab/harness_builder` Builder projection 会提供有界的当前候选正文（含 hash/长度/截断标记），并在决策前确定性执行公开 allowlist 工具，将结果写入 `pre_decision_tool_outputs`；隐藏 evaluator 状态仍不进入投影。默认 `execution_mode=single_solution` 保持一次 solution-call 预算；显式 `multi_step` 才按编译 workflow 每个 stage 调用模型，每个 stage 使用独立 journal operation，receipt 记录 response SHA、provider 与 usage，恢复时继续遵守 no-retry/started-without-artifact 语义。
- `skills/validate-generated-artifacts/`:生成代码/恢复实验的合同与审计门禁；统一记 valid/invalid/canary/中断成本、按内容哈希失效缓存、区分 decision/matrix complete；可复用失败须先补红测再沉淀 Skill
- `skills/diagnose-goal-blockers/`:持久目标出现暂停、Monitor 失败、服务停止、产物无增长或长期 started
  operation 时的首个诊断入口；先核对控制面/产物/进程/账本/revision，再按冻结恢复合同采取动作
- `run_experiment.py`:总编排,按 checkpoint 断点续跑
- `scripts/formal_runner.py`:隐藏终验轮 Q1/Q2/Q3 受控三-lane 队列(每 lane 格间串行、全局最多 3 格)；写正式台账，遇共享额度故障全局熔断
- `scripts/q2_paired_runner.py` + `scripts/analyze_q2_paired.py`:Q2 配对确认的两-lane 四格队列与固定 seed task-paired bootstrap；独立 state/ledger，不覆盖隐藏终验台账
- `scripts/q1_lineage_runner.py` + `scripts/q1_confirmation_runner.py`:R1/R2 从逐字相同 v001 独立进化；正式确认按 R2-train→v001/R0/R2-external→R1 两格排序，24M 总上限计 quick/canary/无效/正式；谱系间禁止共享 trace/提案
- 密钥在 `.env.local`(TOKENROUTER_*,不入库),`config.py` 负责转成 SDK 环境变量;`.venv` 为运行环境
- 隐藏题导入器固定 BigCodeBench-Hard v0.1.4 官方 commit+Parquet SHA；rows 服务故障时用 pinned `pyarrow==18.1.0` 读取同一文件
- 正式池冻结依赖含 `numpy==2.1.3`、`pandas==2.2.3`；AST bugfix 变异仅 12/19 合格，未达 18，故按方案降级 `specgen_hidden`，Q2 只能解释为信息形态差异
- 约定:改评测协议(防作弊规则/重复次数/判定线)前先看方案文档第 5、7 节——判定线开跑后冻结
- 约定:已消费的 test benchmark 后续可降级为 training/validation,但不得再次称 sealed test;
  单一 test 提升只称新 benchmark-sample transfer,Task-level 结论需独立 benchmark/来源复制
- 约定:严格隔离执行与方案设计。沿已确认 plan 为执行模式；一旦要提出新实现路线、架构或非显然取舍，先停写并告知用户进入方案模式，等用户决定是否切更强模型；明确的拼写/合同修复和回归测试仍属执行
- 进入方案模式前必须先给用户一段可直接交接的 Prompt，包含项目目标、上下文、已完成、关键证据、偏离原因、待设计问题、不可变约束和期望输出，然后暂停等待

## Git 信息

- Remote: https://github.com/ApexIntelligence-AI/apex-moss
- 默认分支: main

## 任务生命周期

你收到任务后，按以下 9 步流程自主完成：

1. **领取任务** — 你已被分配任务，阅读本文件和项目代码理解上下文
2. **创建工作区**:
   - `git fetch origin`（如有 remote）
   - `git worktree add -b task-<简短描述> .claude-manager/worktrees/task-<简短描述> origin/main`
   - 进入 worktree 目录工作（后续所有操作在 worktree 中）
   - 如果 worktree 创建失败，直接在当前分支工作
3. **实现功能** — 编写代码，确保可运行
4. **提交代码** — `git add` + `git commit`，commit message 简洁描述改动
5. **Merge + 测试**:
   - `git fetch origin && git merge origin/main`（集成最新代码，如有 remote）
   - 运行测试（如有测试命令）
6. **自动合并到 main**（如有 remote）:
   - `git fetch origin main`
   - `git rebase origin/main`，如果冲突则自行 resolve
   - 如果成功：`git checkout main && git merge <task-branch> && git push origin main`
   - 如果这一步有任何失败，退回到步骤 5 重试
   - （纯本地项目跳过本步）
7. **标记完成** — 更新文档（必须在清理之前，防止进程被杀时状态丢失）
8. **清理** — 回到项目根目录:
   - `git worktree remove .claude-manager/worktrees/<worktree名>`
   - `git branch -D <task-branch>`
   - 如有 remote: `git push origin --delete <task-branch>`
9. **经验沉淀** — 在 PROGRESS.md 记录经验教训（可选）

### 冲突处理

rebase 发生冲突时：
1. 查看冲突文件: `git diff --name-only --diff-filter=U`
2. 逐个解决冲突
3. `git add <resolved-files> && git rebase --continue`
4. 如果无法解决: `git rebase --abort`，退回步骤 5

### 状态判断

- 通过 `git remote -v` 判断是否有 remote
- 有 remote → 必须完成步骤 6（merge + push）
- 无 remote → 跳过步骤 5 的 fetch、步骤 6 和步骤 8 的远程分支删除

## 文件维护规则

> **以下文件都由 Claude Code 自主维护，每次功能变更后必须同步更新。**

- **CLAUDE.md**（本文件）：架构、约定、关键路径变化时更新，只改变化的部分，保持简洁
- **README.md**：面向用户的文档，功能、使用流程变化时同步更新，保持与实际代码一致
- **TEST.md**：测试指南，新增功能时同步添加测试用例和文档
- **PROGRESS.md**：见下方「经验教训沉淀」

## 测试规范

**开发时必须主动使用测试，不是事后补充！**

- **改代码前**：先跑测试，确认基线全绿
- **改代码后**：再跑一遍确认无回归
- **新增功能**：同步新增测试用例，更新 TEST.md
- **修 bug**：先写复现 bug 的测试（红），修复后确认变绿

## 经验教训沉淀

每次遇到问题或完成重要改动后，要在 PROGRESS.md 中记录：
- 遇到了什么问题
- 如何解决的
- 以后如何避免
- **必须附上 git commit ID**

**同样的问题不要犯两次！**

## 注意事项

- 在 worktree 中工作时，不要切换到其他分支
- 完成任务后确保代码可运行、测试通过
- Moss 实验一统一通过 `scripts/run_moss_experiment_one.py` 运行；Edge/ALE 固定 manifests 锁定
  A/B/C、S1/S2/S3、8 轮及上下层 `gpt-5.6-sol`/`high`/Responses。默认只读，任何模型、
  evaluator 或正式写入都必须显式 `--execute`，canary 与 formal root 永久分离。
