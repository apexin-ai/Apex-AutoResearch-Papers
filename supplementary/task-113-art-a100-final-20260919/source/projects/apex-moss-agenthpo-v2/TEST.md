# TEST.md — 测试指南

## 运行全部单元测试(无 API 调用)

```bash
.venv/bin/python -m pytest tests/ -q
```

## 用例说明

### Moss V2 Experiment 1 回归

```bash
.venv/bin/python -m pytest -q \
  tests/test_experiment_one_cli.py \
  tests/test_dual_harness.py \
  tests/test_experiment_one.py \
  tests/test_dual_runtime.py \
  tests/test_experiment_one_production.py
```

V1 是默认入口，测试会保证历史 manifest/hash 仍可加载；V2 只能通过
`--harness-version v2` 显式选择，并验证 schema/hash 绑定。V2 的静态公开工具
必须经过 `ToolRegistry` 并留下 receipt，evaluator 工具必须拒绝。cross-test
Solver 或 evaluator 失败只写 `error.evidence.json` 和 `status=invalid` receipt，
`official_score` 必须为 `null`，且重放不能再次调用。

### `tests/test_eval.py`

| 用例 | 验证什么 |
|---|---|
| `test_oracle_passes` | 正确修复 solution.py 的 harness 得满分 |
| `test_cheater_caught_and_scored_zero` | 改写 test_solution.py 的作弊 harness 被哈希校验抓住,记 0 分并标记 tampered |
| `test_do_nothing_fails_honestly` | 不作为的 harness 正常得 0 分、不误报篡改 |
| `test_model_lock_rejected` | 未声明 `MODEL = "claude-haiku-4-5"` 的 harness 被拒评(SystemExit) |
| `test_guarded_dispatch_rejects_paths_outside_work_dir` | 工具路径越过 work_dir 时只返回错误并累计合同违规 |
| `test_hidden_suite_is_final_judge_and_output_is_redacted` | 可见测试通过不等于得分；隐藏套件是终验且只落计数 |
| `test_hidden_directory_is_not_exposed_to_harness` | Harness 越界探测拿不到隐藏内容 |
| `test_visible_test_side_effects_stay_in_scoring_directory` | 可见 pytest 的相对路径写入留在临时目录，不污染评测器 cwd |
| `test_candidate_runtime_and_teardown_errors_are_capability_failures` | 候选导致的 test/setup/teardown error 按能力失败计分，不误标环境错误 |
| `test_pytest_infrastructure_exit_codes_remain_invalid` | timeout/interrupted/internal/usage/no-tests 退出码仍使格子基础设施无效 |
| `test_benchmarks_are_valid` | 全部 benchmark task 结构完整；普通题修复前可见测试失败，隐藏题修复前隐藏终验失败 |

### `tests/test_builder.py`

| 用例 | 验证什么 |
|---|---|
| `test_nested_markdown_fence_does_not_truncate_source` | Harness 内部提示词含代码围栏时，提取外层完整 Python 源码 |
| `test_keyword_dispatch_call_is_rejected` | 拒绝用 `**kwargs` 调用只接受单个 input dict 的工具 |
| `test_string_method_on_run_tests_dict_is_rejected` | 拒绝把 `run_tests` 返回 dict 当字符串处理 |
| `test_wrong_run_tests_input_key_is_rejected` | 拒绝 `run_tests` 缺少必需的 `test_path` 参数键 |
| `test_prompt_cannot_name_extra_python_file` | 拒绝在 Harness 提示词中诱导写第三个 Python 文件 |
| `test_existing_harnesses_satisfy_sandbox_contract` | 四份现存 Harness 均通过新静态沙箱，无误伤 |
| `test_sandbox_contract_rejects_unsafe_source` | 拒绝额外 import、危险 builtin 与越权 os 属性 |
| `test_builder_repairs_invalid_candidate_without_benchmark_feedback` | Builder 仅依据合同错误修复候选，不接触 benchmark 反馈 |
| `test_proposer_repairs_invalid_candidate_from_contract_error_only` | Proposer 最多两次仅依据合同错误修复，不引入新 benchmark 信息 |
| `test_explicit_candidate_repair_uses_only_candidate_and_contract_error` | 已隔离候选仅凭自身代码和合同错误修复，并保留生成原文 |
| `test_v005_returns_tool_result_when_response_has_tool_use` | 网关状态标记异常时仍按实际动作返回结果，避免流程状态失配 |

### `tests/test_config.py`

| 用例 | 验证什么 |
|---|---|
| `test_local_env_overrides_inherited_gateway` | `.env.local` 的实验网关覆盖会话继承的其他 Anthropic 网关 |

### `tests/test_formal_runner.py`

验证正式队列按 lane 冻结顺序调用既有评测器、每 lane 最多一个活动格、全局最多三格，
记录有效格台账，并在基础设施/共享额度故障时隔离对应格和熔断后续启动；测试只使用
fake evaluator，不消耗 API。

### `tests/test_bigcodebench_import.py`

验证 BigCodeBench-Hard canary 的固定选题顺序、stub 不泄露 canonical solution、V0/V1/V2
AST 拆分、fixture/helper 保留、CLI 调用、rows 服务的固定 Parquet 回退、正式池 SHA 分族/
缩容规则，以及固定 seed 的 AST 变异顺序和“可见过、隐藏挂”接受合同。测试使用内存样例，
不访问网络。

### `tests/test_q2_paired.py` / `tests/test_q2_paired_benchmarks.py`

验证同一底层任务的 V0/V1 版本只改变可见测试，solution/隐藏终验与旧复用格逐字一致；
分析器使用 Harness 增益的 paired difference-in-differences、固定 seed 分层 bootstrap，
而不是跨题池 raw 通过率。测试全部离线，不消耗 API。

### `tests/test_q1_external*.py` / `tests/test_q1_lineage_runner.py` / `tests/test_q1_confirmation*.py`

验证新增依赖白名单不会因传递包漂移、外部任务从未进入旧 pool、4/12 固定哈希选题和文件
指纹；两条独立谱系从逐字相同 v001 起步并通过离线 Harness smoke；正式格按决策价值排序，
24M B1 总预算会重建 quick/canary/无效消耗且正式 canary 记入台账；分析器在优先四格完成
时可合法关闭结论，否则明确报告矩阵未完成。全部测试离线。

### `tests/test_three_tier_qualification.py`

验证三层资格协议的离线门禁：training 严格 `+1/16` 与 validation `ε=1/20` selector、
Fraction/重复方差 formal gate、NFKC 实例特判 linter、16/20/34 快照的文件 hash/互斥性、
training-only proposer payload，以及 global registry 前不得 unseal、started test job
永不重跑的状态机。使用临时 fixture，不调用 API。

### `tests/test_optimization_lab.py`

验证 KernelBench 实验的反馈分段、错误候选不得获得速度分、环境故障隔离、GPU/API 硬帽、
追加式幂等账本、固定 commit/题目哈希预检、官方输出解析和实时 HTML 看板。已淘汰任务的
异常分数必须显示为“不计分”，不能进入历史最佳或最近成绩。测试使用 fake adapter 和临时
Git 仓库，不连接 A100、不调用模型 API。

### `tests/test_optimization_campaign.py` / `tests/test_optimization_generation.py`

验证 P1 每题三种冻结基线具有相同预算上限，P2 每题三条谱系从逐字相同 seed 起步但历史
目录完全隔离；八轮、连续三轮无正确/无进步停止，环境错误不消耗轮次，最佳候选和恢复状态
不丢失。另验证模型输出只能包含一个完整 `ModelNew` Python 候选、短反馈会移除私有路径，
候选/原始响应追加归档且同 ID 不得覆盖不同内容。Campaign 在 P0 干净环境、固定模型、lane
上限和 API/GPU 两个费用硬帽缺任一项时都保持不可执行。若持久化目录已有 campaign 计划，
实时看板在未开跑时必须把六个 P1 lane 和六条 P2 谱系标为待运行，说明 blocker 与零消耗；
开跑后只统计 P1 Kernel 候选，逐 lane 展示完成数、最近结果、最好成绩与实际模型/GPU 消耗，
并明确 P1 Harness 固定不迭代。任何状态都不得暴露 artifact、私有评分日志等绝对路径；P0
干净环境确认写入账本后，看板必须把 P0 标为已完成、把 P1 标为等待授权，不能继续显示 P0
进行中。全部测试不调用模型或 GPU。

### `tests/test_optimization_controller.py`

使用 fake generator 和 fake adapter 走通一个 P1 lane 的端到端控制路径：冻结 Harness 组装、
单一 `ModelNew` 提取、候选及模型原文不可覆盖归档、评分短反馈、模型/API/GPU 预算和追加式
账本。重点回归 `execution_ready=false` 时 generator/adapter 调用数必须为零、API 硬帽必须在
生成前拦截，以及同一 candidate ID 在当前进程或恢复后的新控制器中都不得重复调用模型或
评分器。无效模型输出只进入隔离归档和拒绝事件，不进入评分。测试全离线，不连接 Docker、
GPU 或真实模型 API；P2 继续由 `LineageTracker` 的现有停止/恢复测试覆盖。

### `tests/test_optimization_container.py`

验证 P0 容器基镜像固定到明确摘要，包含 Python 3.10 和现场编译所需工具，但不把服务器级
NVIDIA Toolkit 安装进项目镜像；同时验证容器 smoke 必须只看见一张 GPU，并实际经过
`torch.compile`。测试本身不连接 Docker 或 GPU，正式 smoke 与正反例复现证据写入实验账本。

### `tests/test_codex_generator.py`

验证 ChatGPT 登录的 `codex exec` 生成器固定使用临时会话、只读沙箱、显式模型和 JSON Schema，
只把提示词送入无项目文件的隔离目录；子进程环境必须移除 OpenAI、TokenRouter 等 API 密钥，
JSONL usage 和审计日志必须保留。CLI 非零退出或限流时失败关闭，不自动切换供应商。

### `tests/test_p1_campaign_runner.py`

验证 P1 runner 只执行两题六组冻结基线：每题零样本 1 轮、同预算通用流程 8 轮、人工朴素
流程 2 轮，共 22 个候选；后续轮次只能看到本 lane 的短反馈和上一候选。验证断点重跑不重复
调用模型/GPU、lane 预算会从账本恢复、P1 完成后看板显示 P2 等待授权，且没有 P2 执行入口。
若评分器规则拒绝曾被旧解析器误记为环境故障，必须追加纠正事件而不是改写旧账本；恢复时复用
原候选和纠正后的反馈，不多调用一次模型或 GPU，并按纠正值恢复预算。

### `tests/test_harness_evolution.py` / `tests/test_p2_campaign_runner.py`

验证 P2 只有在 P1 完成事件存在时才能启动；两题各三条谱系从逐字相同 v001 起步，Harness
版本带父指针且不可覆盖，优化器提示只包含当前谱系的短反馈。离线端到端测试让六条谱系在
连续三轮无提升后停止，核对每条 4 个 Harness/Kernel 版本、候选与 Harness 两类模型调用共同
恢复预算、断点重跑零调用、看板显示当前 Harness 版本与最好成绩，且全程没有 P3 入口。
生成 Harness 若包含绝对私有路径会在进入做题模型前被拒绝；Harness 调用开始后若在归档前
中断，恢复时必须计入既有调用、冻结当前谱系并继续其余谱系，不能重复调用或越过 lane 硬帽。

### `tests/test_harness_builder_runtime.py` / `tests/test_harness_builder_runner.py`

验证 Builder prompt 可见有界当前候选及决策前公开工具结果；`multi_step` Harness 会按
`analyze → generate → verify_contract` 等编译 stage 实际调用模型，最终候选来自 `generate`
stage，且各 stage 输出可传给后继 stage。runner 测试还核对每个 stage 的独立 journal operation、
round receipt 中的响应哈希/provider/usage，以及 stage 中断时的 no-retry 恢复语义。

### `tests/test_p2b_plan.py` / `tests/test_p2b_policy.py`

验证 P2b 冻结两题各四条不同路线、每题一个 P1 与三个 P2 起点的代码哈希、8 Kernel/15 调用
lane 硬帽和 120 调用/14,400 GPU 秒全局硬帽。结构化 Harness 必须显式选择代码起点、工具、
任务内 Skill、记忆视图、工作流和 Kernel 结构范围；每轮必须保留 score/score-trend，分数没有
2% 可信提升时不得只改写措辞或局部参数。第六轮强制重启、结构探索轮、绝对私有路径拒绝、
未知候选和不可用工具拒绝都由离线合同测试覆盖。

### `tests/test_p2b_profiling.py` / `tests/test_ssh_profiler.py`

验证轻量结构签名、Profiler 摘要隐私边界、`nsys` JSON 解析、Triton 编译缓存、`cuobjdump`
寄存器/共享内存解析和 A100 静态理论 Occupancy。缺失的 achieved occupancy、DRAM/L2、warp
stall 或 spill 不能同时出现伪造数值；理论 Occupancy 必须明确区别于硬件实测。单测使用假
cache 和 fake profiler，不连接 A100；真实端到端 profiler 预检属于显式集成测试。

### `tests/test_p2b_runner.py`

用 fake model、adapter 和 profiler 完整运行 8 lane × 8 轮，核对 64 个 Kernel 调用、56 次
Harness 更新、每轮即时分数趋势、至少四轮结构探索、满足条件时的第六轮强制重启、独立历史、
追加式 ProfileSummary 和 HTML 看板。断点恢复必须新增零模型/零 GPU/零 profiler 调用，且事件
中不得出现 P3 入口；看板必须按 Harness 版本绘出冻结起点、每轮精确 speedup 和正确性失败断点。
正确性失败、没有 ProfileSummary 的轮次必须正常渲染；评分完成后才中断的未封存轮次也必须从
`candidate_evaluated` 事实恢复成橙色分数点。该仿真全部离线，但因覆盖完整 120 调用状态机会比
普通单测更慢。

### `tests/test_harness_builder_*.py` / `tests/test_hb_*_adapter.py`

验证 HB-GEN-1 的三 benchmark × 八 instance 冻结流、A/B0/B*/B-online 信息边界与逐题
test-then-learn 状态机；系统级 Harness decision 必须真实改变父代、记忆、可信工具、workflow、
scheduler 或 recovery，只换 directive 措辞不能冒充进化。Experience Bank/checkpoint 内容寻址且
只有四臂封存后才能更新；规则须经跨 instance/benchmark 复制才晋升。操作账本使用 SHA-256 链和
独立 head 锚点，模型能力只由 trusted controller 一次持有，started 中断按完整预留计费，逐 cell
额度不可借用。KernelBenchX、CompilerGym 与 SWE-Perf adapter 分别验证私有 supervisor 结果通道、
固定 action allowlist/fresh replay、source/index 哈希绑定的 ordinary semantic validator 集合、
digest-pinned correctness→performance Docker 边界；candidate
stdout 永不参与裁决。KernelBenchX 单卡隔离还必须验证宿主物理 GPU 设备节点保留原编号、worker
内 `CUDA_VISIBLE_DEVICES` 和官方 pipeline 参数均重编号为逻辑 `0`，且不得额外挂载
`/dev/nvidia0`；Triton 编译器必须用只读 `/usr` 下的版本化绝对路径，不能依赖未挂载的
`/etc/alternatives`；Python headers 必须来自 regular-file-only、大小受限、完整树哈希绑定的只读
snapshot，任何 header 变更都在创建 worker 前失败；`python3.10/Python.h` 与
`x86_64-linux-gnu/python3.10/pyconfig.h` 均为强制文件。冻结 KernelBenchX 集合必须包含
`Fusion/fused_relu_max_pool2d_conv2d.py` 且排除 evaluator schema 不可精确绑定的
`Activation/gelu_bf16.py`，两套 task hash 表必须逐字一致。检索测试还验证同题经验排除、
descriptor 匹配、支持级别即时派生，以及 B0/B*
模板只有实际 Experience Records 可以不同。全部测试使用 fake transport/environment/executor，
不连接模型、Docker 或 GPU。

`tests/test_hb_three_arm_campaign.py` 另行锁定当前三臂协议：`A/B-frozen/B-online` 从空经验开始，
每题三臂封存后只有 B-online 自身轨迹可进入一次蒸馏，下一道题才可检索；最后两题仍执行八轮题内
反馈，只是不再做题后跨题蒸馏，因此它们不是 evaluator-blind holdout。
测试同时覆盖 arm-cell 中断恢复、整题 immutable replay 和零新增模型/评测调用。`test_hb_three_arm_prepare.py`
核对 8 个三-suite task block 的轮转式平衡交错流、每 suite 的 6+2 online/holdout 边界、schema v5
`stream_policy=balanced_interleaved` 和不可借用预算，并反向拒绝 suite-blocked 排列；`test_hb_three_arm_report.py` 要求 72 条 arm 曲线与 576 个
round 点齐全后才生成五份报告，并锁定八次尝试、有效轮均值/最高分、单臂 `4/8` 与学习题配对 `5/6`
门禁；不足者必须标记 `insufficient_validity` 且不得进入性能均值或趋势。逐 benchmark
`B-online − B-frozen`、顺序斜率、T6−T1 变化均只使用通过门禁的配对题，跨 benchmark 不混合原始量纲。LCBench、CompilerGym 与 SWE-bench Verified
生产 adapter/canary 分别绑定固定数据、Python/LLVM runtime、官方源码/镜像 digest 和私有评分结果。
`tests/test_harness_builder_learning.py` 还锁定 distillation prompt 必须逐字包含冻结 Experience Record
的全部 14 个字段、bare `records` 模板与禁止 compact alias 的约束；formal/three-arm fake transport 只从
显式 `Sealed public trajectory` 边界读取输入，避免模板 JSON 与轨迹 JSON 被错误拼接。严格 parser 仍须
拒绝缺字段、别名字段、重复 key、未绑定 provenance 或错误 source instance。
`tests/test_harness_builder_runner.py` 还必须证明 planner 只改 rule/directive 而没有 operational change 时，
该轮封存为 `planner_contract_rejected`、不调用 solution/evaluator、恢复时零新增调用，后续轮仍从最近有效
Harness 继续；还必须分别覆盖 planner、solution、evaluator 的 started-without-artifact 与 terminal-failed
恢复：已消费 reservation 保持扣除，原 operation ID 不重发，schema v3 零分轮次绑定原 journal event，
后续轮继续执行。`tests/test_harness_builder_runtime.py` 锁定一次性 A 臂 v001 无效后不得在 v002 偷偷重初始化。
`tests/test_harness_builder_wide_adaptation.py`、`test_harness_builder_compile_receipts.py` 与
`test_harness_builder_wide_multibenchmark.py` 进一步锁定 `B-frozen-wide`：v002 起七个架构轴全部变化，
role/memory/tool 的纯重排不算变化，七类行为由当轮新建的 typed runtime component 实际执行；完整
accepted lineage 不能截短或复用旧 fingerprint，compile receipt 必须在 solution 前绑定 parent、catalog、
component config、七轴稳定 configuration hash 和解析后行为；任一稳定配置未变都拒绝父子封存，同名
tool callable 也不能替换 Registry 实现。production seal 必须经 `store_trusted_version` 携带实际
`CompiledHarness`，在任何落盘前重建并逐字核对 receipt；fully-rehashed memory/tool/axis-effect 伪造必须
零落盘失败，generic archive 写入只能显式标成 `fixture_only`。AgentHPOBench/GDPevo fake cell 均跑满八轮，并验证相同输入重编译
确定、跨 benchmark receipt 不可复用。`test_hb_three_arm_campaign.py` 还验证 wide arm 和完整 instance
恢复会重新绑定 task provider 并逐轮 trusted recompile，同时保持模型、evaluator 和 ledger 零新增；旧
`conditional_any_v1` 继续允许 provider-free immutable replay。
`tests/test_harness_builder_{qualification,agenthpo_qualification,gdpevo_qualification}.py` 验证冻结来源、
互斥切分、严格候选/结果边界与零 entitlement；`test_harness_builder_factorial_contract.py` 锁定
AgentHPOBench/GDPevo、共同 v001 后四臂 fork、七轴 wide 改动、逻辑预算以及正式执行
`NOT_READY/NOT_GRANTED`。`test_harness_builder_factorial_trunk.py` 验证每个
task×seed 只封存一个 arm-independent v001，四臂 compile 的 typed 语义等价、共同
solution/evaluation 引用、完整 compiled-Harness semantic projection、typed task/source/seed rebind、
内容寻址恢复及“篡改 embedded receipt 后连同其外层 receipt 重哈希”攻击；整套 semantic projection
被替换并重哈希时，trunk 类型自身仍不足以证明 provenance；新 formal-dispatch 路径会另行执行
source-bound trusted compiler replay，
非法 terminal 组合与跨 task/seed 重绑均 fail closed。`test_harness_builder_factorial_policies.py` 分别锁定
A 的 Harness 冻结、S 的 task-local typed Skill、B-targeted 至少一轴实质改变，以及 B-frozen-wide
七轴全变、fresh typed runtime component 与不可复用 lineage fingerprint。

`test_harness_builder_factorial_score.py` 锁定 AgentHPOBench/GDPevo 的原始分数范围、只供优化内部使用的
正值 affine utility、报告只输出 raw score，并拒绝越界、NaN、伪造 transform/contract 或无证据的有效分。
`test_harness_builder_factorial_itt.py` 进一步把两套 Benchmark 的 native floor 固化为逐 attempt ITT
策略：typed invalid score receipt 必须记入 floor，可信优化入口每次重验 checked-in factorial manifest，
公开 report row 只能携带 native raw score，不能泄露内部 utility。reservation/evaluator/optimizer/report
的一对一 dispatch 尚未实现，因此测试不声称覆盖了所有 reserved attempt。
`test_harness_builder_factorial_precheck.py` 将任意多 Benchmark 零调用状态机明确限定为
`FIXTURE_ONLY`；另外验证严格 formal zero-call 计划必须从 checked-in
`wide_meta_factorial_v1.json` 机械展开 126 个精确 task×seed cell，锁定 AgentHPOBench 6 轮、
GDPevo 3 轮、完整 arm-policy/arm-variant digest，并对每个 benchmark×seed 审计四臂 Latin
position balance。专用 exact-plan controller 已接入共同 v001 barrier/recovery，并在每次 bind/replay
重验四臂 variant、policy、contract 与 fork receipt；fixture controller 必须拒绝 exact formal plan，
两种计划都必须拒绝任何非零 entitlement 或 `GRANTED` authority。该 controller 没有 provider callback，
仍不能被解释为 evaluator 或正式 runner 已就绪。后续 v002–v008 状态机仍只用 fixture controller 测试。
`test_harness_builder_factorial_task_authority.py` 从两个 pinned Git object database 机械重建 42 个
solver-visible task artifact 与 126 个 task/context-bound key；调用方不能自供 task hash。GDPevo task card
只包含公开 prompt/payload，gold/evaluator 仅进入 controller-private source binding；AgentHPO 离散与
nullable 离散空间可精确派生，free-form room-selector 则明确 fail closed。该 source audit 仍只授予零调用
矩阵。plan 只接受经 pinned-source authority 重放的 canonical bundle 并绑定其 SHA；barrier 构造和 v001
恢复时再重建 bundle、逐键比对，伪造裸 key 或 self-rehashed bundle 均失败。v001 compile-only context
dispatch 已接线；post-v001 compile-only context authority 已接线，production provider dispatch 尚未接线。
`test_harness_builder_factorial_formal_dispatch.py` 从当前 pinned source、exact plan、Rule Registry 与 operator
source 重编译共同 v001 四次，锁定四臂语义相同、arm receipt 独立且 execution entitlement 恒为零；直接
构造的不安全 decision、self-rehashed result、source/Registry 漂移均须在可信消费边界失败。
`test_harness_builder_runtime.py` 同时要求 source-bound artifact capability 经 allowlisted `task_semantics`
精确进入 solver prompt，并证明无关 `public_observations` 不会随之泄露。
`test_harness_builder_factorial_coverage.py` 机械展开并精确核对 1,566 个评分槽，接受 AgentHPO 合法负分与
GDPevo 合法零分，将 typed invalid 映射到 native floor，并明确把无 operation-ledger 绑定的 score 标为
unbound；零调用 exact-set seal 不能冒充执行覆盖。`test_harness_builder_factorial_canary_readiness.py` 固定
AgentHPO 14 个 baseline/21 个 evaluator 前负例断言与 GDPevo 180 个未来 evaluator canary 槽，且不读取
private gold。`test_harness_builder_factorial_operation_schedule.py` 从相同 pinned source、formal plan 与 exact
matrix 机械展开 4,338 个潜在外部阶段，严格核对 1,206 update、1,566 solution、1,566 evaluator、满路径
2,772 model/1,566 evaluator 上限及逐 cell 不可借离散帽；A post-v001 不得出现 update，重排、漏项、增项、
operation rebind 或整体 self-rehash 都不能通过可信 source replay。该 schedule 的 CPU/GPU 帽仍为 canary
pending，且没有 journal/governor/provider callback，所以不声称任何 operation 已 reserve 或执行。
`test_harness_builder_factorial_stage_disposition.py` 使用单次 v1 semantic journal replay 将 exact schedule
映射为 terminal operation 或 immediate-parent skip：小链覆盖 completed→failed→skip、failed→skip→skip、
started/reserved、completed-without-artifact、跨级/跨 attempt、extra operation 与 physical retry suffix
失败关闭；全量 fixture 一次重放 4,698 events，精确封存 1,566 failed roots + 2,772 skips；mixed exact-set
另覆盖 3 completed + 1,565 failed + 2,770 skips。deep-freeze 攻击、child reserve/start 时序、持久化 artifact
对 pinned source 与当前 ledger/head 的 fresh full replay、32 MiB 输入上限，以及缺项/重复/caller 重建
receipt/seal 均失败关闭。测试明确断言 `formal_execution_ready=false`、全零 entitlement，不能替代
descriptor-relative journal v2、pending-WAL、typed gate 或正式 provider/evaluator dispatch。
`test_harness_builder_factorial_static_q0_evidence.py` 实际重放 AgentHPO Q7 的 31 个 source 文件、七个
original space 与 21 个 strict-codec negative，并从 GDpevo Git ODB 核对 pinned commit/root/task-groups 和
Q6 group/env/test trees；测试确保 evaluator/model debit 为零、不读取 private gold、未独立复算的 file
manifest 显式保持 `UNVERIFIED`，伪 disposition、source drift 与 self-rehash 都失败。它不是 reference、
environment 或 isolation canary。`test_harness_builder_factorial_online_plan.py` 锁定 `O0/OM/OP/OA` 的 732 attempts、84 updates、
1,548 logical calls、隔离 state roots、主实验结果禁入与“非独立 fresh confirmation”边界。
`test_harness_builder_factorial_post_v001_authority.py` 在 AgentHPOBench/GDPevo 的 pinned source 上重放
post-v001 exact slot：B-targeted 至少一轴变化，B-frozen-wide 七轴配置全部变化、active component
nonce/config 不复用且 fingerprint 不重复；已形成 intent 的 rejected physical round 保留 ITT floor，并让
下一轮继续最近 accepted parent。`test_harness_builder_factorial_skill_dispatch.py` 证明 S 的 Harness 决策、
七轴与 compile fingerprint 冻结，只允许 bounded Skill 在同 task/seed 内更新并于可信 compile 后进入
solution prompt。两者仍使用未绑定真实 journal 的 operation/source-terminal fixture SHA，不证明正式
provider/evaluator coverage。
`test_harness_builder_factorial_online_lineage.py` 锁定 exact 16 条 benchmark×seed×mechanism lane，逐步
解析 OM/OP/OA 的 proposal、parent/child memory/policy/archive/checkpoint 并调用 trusted transition
validator，拒绝跨机制、未来 source 与 forged state/CompiledHarness；held-out context 必须携带重新派生的
Builder prior，O0 必须为零注入，四机制还需共享同一 source-terminal cohort。严格 bytes replay 与可信
重编译已覆盖，但 source/operation digest、完整 planner request/result、online task authority、updater
failure cursor 和 stage gate 仍必须保持 NOT_READY。
`test_harness_builder_factorial_outcomes.py` 锁定 v001 environment/solution/candidate/evaluation/interruption
的 typed stage receipts 与 content-addressed archive：环境无效仅能作为绑定旧 attempt 且更换环境 SHA 的
重试原因，其他失败为 terminal；中断保留已完成前缀但不得伪造后续 artifact。
`test_harness_builder_agenthpo_intervention.py` 锁定 AgentHPO discrete codec 不接受 alias、未知 key、
nearest/clamp、类型替换、no-op、重复 key 或 permissive JSON；一个 decision operation 必须绑定恰好一个
已提交的 provider-request receipt，失败 request 仍计费，提交多个 retry 会被拒绝。pinned derivation
还绑定 commit/tree、space manifest/backend 与逐 task runner blob，从 runner AST 和 manifest 双向核对
11 个 scalar task 的原始离散空间、baseline/current config，并精确保留 JSON `null`；唯一 free-form
task 必须使用另一个 codec 或 fresh split。该单测不能证明调用方
没有省略真实 request；这一点仍需唯一 trusted transport ledger，当前因此不授予执行权限。

`test_harness_builder_{meta_evolution,meta_prior,online_meta}.py` 锁定
`OM/OP/OA` 独立 checkpoint/ledger、test-then-learn 顺序、resolved typed 父子对象更新和 Builder-only
prior，禁止伪造不可解析的 state digest、跨机制读取、执行任意自修改代码或把 prior 注入 solution prompt。
`tests/test_optimization_lab.py` 还覆盖新 wide 事实账本的 canonical hash chain/head 篡改检测；compile
receipt、runner 与 formal 测试覆盖 symlink target/parent、非目录父路径及 no-replace 封存。
`tests/test_hb_three_arm_providers.py` 锁定 LCBench 与 CompilerGym task card 必须包含完整顶层 JSON 模板、
当前 task binding 和“不得只返回 payload 数组包装对象”的明确约束，防止模型生成可用内容却遗漏身份字段。
SWE-bench 官方 gold 与正式模型 patch 共用兼容层，可确定性补入 validator 要求的非语义 `index`
metadata；回归必须证明移除新增行后逐字恢复输入、修改/新增普通文件均可正规化，且路径、hunk 或
语义异常仍由同一严格 validator 拒绝。gold canary 的终态判定必须读取
SWE-bench 专属的 `valid_scored/resolved/status/score` 字段，不得假设其他 adapter 才有的 `correct` 字段。
同一测试文件还锁定 Docker 网络合同：必须使用 `network_mode="none"` 禁用外网，禁止使用会破坏本机
名称解析的 `network_disabled=True`；`localhost` 只映射到 `127.0.0.1`，且 worker 必须在复制/应用候选前
完成 loopback socket bind。预检失败必须返回环境错误，不能生成候选分数。

`tests/test_harness_builder_rule_registry.py` 验证 provenance-bound Rule Registry v2 历史合同与当前 v3：所有来源
必须绑定 40 位 commit、相对路径、有效行区间和 64 位文件 SHA；v1 的 trigger/action/guardrail 文本
逐条保留；v3 新增可执行 `contract_compatibility`，并要求启用该规则的每个 task 在 v001 先绑定
artifact capability card、reference parent、`task_semantics` 与 `verify_contract`。外层 distillation
不能被 Harness 选择。正式 Registry SHA 会自动加载完整规则卡并写入
`RuleDecisionTrace`；未知/advisory rule、来源漂移和只换 rule 标签冒充 operational change 都应失败。

`tests/test_hb_swebench_contract_qualification.py` 锁定 v1r8 正式流前的同题资格门禁：
`sphinx-doc__sphinx-8459` 必须封存八次尝试，少于 4 个有效测分时 summary 为
`insufficient_validity`、mean/best 为 `null` 且禁止启动正式流；达到 4 个时才可准入。资格分明确禁止
复用为正式三臂分数。
这些测试纯离线，不访问来源仓库、模型或 evaluator。

`tests/test_hb_three_arm_continuation.py`、`tests/test_hb_three_arm_v1r9_integration.py`、
`tests/test_hb_swebench_qualification_transfer.py`、`tests/test_hb_swebench_remote_deployment.py` 与
`tests/test_hb_three_arm_composition.py` 锁定
schema-v6 successor：精确引用 v1r8 前六题与 1244-event source ledger，scikit tail 只计费不导入；
执行窗口只能是 `[6,24)`，phase/model/task 顺序、全局 arm 轮转、suite-specific CPU cap 和 876/432
suffix entitlement 均不可重绑。A/B-frozen 不得看到导入 Bank，只有 B-online 可接续前缀经验。
三套 canary、Rule Registry、干净 revision、SWE selection/task/image lock 与 0-call qualification
transfer 在首次 preflight 和每次 reserve 前都必须保持内容哈希一致。SWE worker 的负向测试还要求
locked image 缺失或 RepoDigest 不符时立即失败，绝不退回 mutable tag 或网络 pull；formal 远端
project/source/python 必须与六题 gold canary 的执行合同逐字一致。内容寻址 remote-deployment receipt
还会重算本地 clean revision 的完整 tracked-tree manifest，并通过只读 SSH probe 核对远端 tracked
文件、worker、Python 二进制身份及 SWE-bench commit；任一漂移在 paid reserve 前失败。组合 manifest 只有 24 个 instance、
72 个 arm、每臂 8 轮全部封存后才能生成，并显式排除 scikit tail 的学习与性能导入。冻结 source
staging plan 可以保留历史 pretty JSON 字节，但必须与 continuation snapshot 的原始 SHA 完全一致；
所有 instance/arm receipt 继续要求 canonical JSON 与逐层 hash binding。

v1r9 的 SWE 后缀选择器还必须机械重放六仓库、`F2P>=6`、F2P 占比至少 `1/100` 的门槛，并排除
冻结禁网环境不兼容的 `psf/requests`；批准集合按固定 domain 哈希排序为 `pytest-7205`、
`matplotlib-25775`、`xarray-4356`、`sympy-21930`、`astropy-13977`、`pylint-4604`。因此全局
stream index 6 必须是 `pytest-7205`，而不是被排除的 `requests-2317`。

```bash
PYTHONPATH=. .venv/bin/pytest -q \
  tests/test_hb_three_arm_continuation.py \
  tests/test_hb_three_arm_v1r9_integration.py \
  tests/test_hb_swebench_qualification_transfer.py \
  tests/test_hb_swebench_remote_deployment.py \
  tests/test_hb_three_arm_composition.py
```

reference canary 还必须绑定完整 dataset task SHA、只抽取分隔符前的实现段并重新通过正式
solution codec；把含内嵌 tests 的整份 task 文件当 candidate 时必须在 GPU 前失败。该回归由
`tests/test_harness_builder_solutions.py`、`tests/test_hb_kernelbenchx_adapter.py` 与
`tests/test_hb_kernelbenchx_reference_canary.py` 覆盖；后者还验证 content-addressed manifest、
幂等 prepare、不可覆盖和 preflight 实际消费 manifest。纯离线运行：

```bash
PYTHONPATH=. .venv/bin/pytest -q \
  tests/test_harness_builder_solutions.py tests/test_hb_kernelbenchx_adapter.py \
  tests/test_hb_kernelbenchx_reference_canary.py
```

`tests/test_harness_builder_meta_train.py` 另跑完整的六题 meta-train fake 闭环：六个互相隔离的
B0 cell 各消耗 16 calls/8 evaluator seats，八条 source trajectory 未全部封存前禁止 distill，
封存后恰好再消耗八次 distillation call，并验证 B* 与 B-online checkpoint 同字节、heldout task
不能进入跨题 memory。第二次运行必须从 round/模型 artifact/operation journal 恢复，新增模型和
evaluator 调用均为零；总计精确为 104 calls、48 evaluator transaction。

`tests/test_harness_builder_formal.py` 使用纯 fake provider/transport/evaluator 验证正式
prequential 控制面：必须逐字遵循 staging stream 与每题 arm_order，四臂各封存 v001-v008 后
恰好一次 test-then-learn；首题 B* 与 B-online checkpoint/bank 相同，随后只有 B-online 看见前题
经验，B*、B0、A 的边界保持冻结。测试同时检查 first-encounter 曲线、arm/trajectory/instance
内容哈希、bank/checkpoint parent chain、调用/评测预算，以及整题重跑零 provider/模型/evaluator
调用。四臂后崩溃恢复只能复用已封存 arm 并补一次 distillation；同题复跑不得再学习或改变正式
成绩。CLI 默认只 preflight，`--execute`、ready staging 与 staging-bound provider factory 三项缺一
都不能进入 runner。

`tests/test_hb_formal_providers.py` 覆盖正式 provider 组合门禁：staging/manifest 与 suite canary
必须逐层绑定，canary operation ledger 必须由当前 verifier 对独立 trusted-head anchor 重放，terminal
artifact 与资源投影必须一致；公开 preflight 只能包含 hash/reason code，不能泄漏 operator path。
CompilerGym 的旧 canary 兼容路径仅接受冻结的 36-event segment，并逐项证明 adapter bytes、codec/
backend canonical AST、cell-ID 交集与当前重放结果；证据内容寻址且重复预检逐字幂等。单个 suite
通过后可离线构造 task binding，但 blocked staging 仍不能铸造三-suite factory。SWE-Perf 的旧
worker-authored receipt 或被篡改的 capability verdict 不能升级，当前
`in_process_candidate_outcome_unattestable` 必须持续阻断 factory。纯离线运行：

```bash
PYTHONPATH=. .venv/bin/pytest -q tests/test_hb_formal_providers.py
```

`tests/test_hb_kernelbench_meta_adapter.py`、
`tests/test_hb_kernelbench_meta_isolation.py` 与
`tests/test_hb_kernelbench_meta_supervisor.py` 锁定训练 scorer 的更强边界：六题 commit/source SHA、
每 attempt 独立 scratch/cache、mode-0600 私有结果、一次性 nonce 与 task/candidate/protocol/scorer
全绑定、5/5 correctness 和 100/100 correctness-bound timing 计数、环境健康与候选失败分离，
candidate stdout 即使伪造完整 score 或环境故障也不参与裁决。namespace 测试复用 KernelBenchX 的
单 GPU 逻辑重编号、禁网、只读源码/系统与完整 header tree，并锁定只读 trusted-runtime bundle、
匿名 fd3 result channel 与每 phase 独立 scratch/cache。supervisor 测试还要求 canary/formal 在缺少
内容寻址授权 receipt 时于加载 GPU/candidate 前拒绝，canary receipt 精确绑定代码 revision、scorer/
protocol/task-set hash、10 个 transaction 与 6,000 GPU 独占秒。subprocess fake supervisor 只用于
验证私有通道 ABI，不代表真实 GPU canary 已通过。

adapter 测试进一步要求 constructor 必须绑定由外部 authority 签发、controller 只持有和消费的
mode-0600、文件名等于内容 SHA 的 receipt；`MetaSupervisorCommand` 保存 path/SHA，并让 canary/formal 两类命令都携带
`--authorization-receipt`。缺失、改名、落入 repository/attempt root 或 prepare 前被改写都拒绝，
receipt path/SHA 不得出现在 `worker_visible_argv` 或 candidate environment；两类命令还会重建真实
`SupervisorRequest` 并通过同一 receipt contract，测试过程不创建 worker 或访问 GPU。

`tests/test_hb_kernelbench_meta_worker.py` 使用无 CUDA fake Torch runtime 验证真实 worker 的控制流：
逐题 policy、权重初始化、5+100 新鲜私有输入、交错 reference/candidate、逐次 output/input seal、
schedule/input commitment、result fd 在 runtime import 前 CLOEXEC，以及异常时不产生 terminal payload。
私有 seed nonce 不得写入 worker evidence；同 nonce 可重放，同 task 下不同 nonce 必须改变输入承诺。

`tests/test_harness_builder_historical_import.py` 验证两条历史 meta-train 轨迹的离线导入：
四个 source SHA/event count 和 all-lanes/no-winner 策略必须精确绑定；P1→P2→P2b 顺序、
全部 terminal 成败/中断事件、Harness/policy parent 和 provenance ID 不得丢失。synthetic 闭环
还检查双锁、候选 hash 篡改时只写 blocked prepare、canonical 内容寻址回读、公开边界，
以及模型/evaluator/GPU/网络新调用为零。

`tests/test_hb_kernel_candidate_policy.py` 与
`tests/test_hb_kernel_candidate_invocation.py` 锁定 `CandidateInvocationABI-v1` 的离线核心。前者要求
codec 和 supervisor 分别执行同一 canonical policy，验证 P1/P2 代表性 Triton 源码的已知 SHA，并
拒绝 fake stdout、私有结果覆写、`os/sys/pathlib/subprocess/threading/socket/ctypes/inspect/pickle`、
动态执行/反射、Torch 文件/Storage/CUDA control 与 module/global monkeypatch。后者用无 GPU fake
runtime 验证 trusted primitives 必须先于 candidate import 捕获，compile→5 correctness→100 measured
的 106 份输入 commitment 均不同，100/100 measured output 都逐次比 reference 且检查 input mutation；
“前五次正确后返回错误快路径”必须在第一次 timing 被抓住，process group/GPU context 未静默时不得
产生 score。这些测试只证明 production runtime 已实现并通过 CPU/fake 合同测试，不代表 GPU4 canary
已通过；`production_runtime_implemented=true` 必须与 `execution_ready=false`、
`kernelbench_meta_canary_pending` 同时保持。
policy 还必须逐题限制 cumsum/attention/logsumexp/GELU 扩展 TL capability；任意
`self.register_forward_hook()` 等未声明方法必须拒绝，只有已声明 helper 或 `__init__` 创建的明确
`nn.Module` 可以作为 `self.*()` callable。

`tests/test_hb_kernelbench_meta_canary.py` 另外冻结十席 GPU canary 的内容与顺序：六个 task SHA
只能产生已知 hash 的 Model-only 正例，两个静态攻击必须在 adapter/GPU 前拒绝，wrong 与
first5-then-wrong 必须进入可信 evaluator。controller 的每席 reserve/start/terminal、结果对象、
外部签发 mode-0600 receipt、started-without-artifact 不重发、独占 execute lock、GPU 超额 fail closed，
以及独立 ledger + external-head 重放都必须通过；verifier 还锁定 wrong 为 0/0/0、first5-then-wrong
为 5/1/0、正例为 5/100/100。独立 verifier 只能写 canary evidence，不能自动产生 formal activation。测试 evaluator
完全是 fake，不连接 GPU。定向运行：

```bash
PYTHONPATH=. .venv/bin/pytest -q \
  tests/test_hb_kernel_candidate_policy.py \
  tests/test_hb_kernelbench_meta_adapter.py \
  tests/test_hb_kernelbench_meta_canary.py \
  tests/test_hb_kernelbench_meta_supervisor.py
```

`tests/test_harness_builder_runner.py` 另外覆盖 evaluator 与 round seal 之间的三个中断点：terminal
已落账时只读回放 canonical controller result；result 已写但 terminal 未落账时用 artifact SHA
补全 operation；started 且无 result 时判为 abandoned，禁止再次调用 evaluator。三种恢复都必须
保持同一 candidate/operation/cell/instance/version 绑定，并且失败席位不退款。

`tests/test_hb_model_route_canary.py` 使用 fake transport 覆盖 HB-GEN-1 模型路由 canary：固定
`gpt-5.6-sol/high/codex-cli-0.144.6/codex_chatgpt`、staging/source/prompt/full code revision 与精确
`HarnessDecision`；provider/model/结构漂移均 fail closed。completed 结果恢复不新增调用，started
且无 artifact 不重发；额度耗尽会在 transport 前阻断。旧 revision canary 的 journal/head/summary
只作为不可复用的已消费 segment 扣费，并保证新 revision 使用不同的内容寻址目录。CLI 默认
preflight，只有显式 `--execute` 才允许进入模型调用路径；全部测试不会运行 Codex 或读取密钥。
`tests/test_harness_builder_model_gateway.py` 另外验证 provider result 已原子落盘但 terminal 尚未写入
时，恢复器按 operation/cell/kind/prompt/model/output-mode 与 canonical artifact SHA 补账，绝不重发；
started 且无 result 仍永久 abandoned。

### `tests/test_hb_sweperf_wrapper.py`

验证八个上游 SWE-Perf digest 只能进入离线 wrapper build context：任务 source lock 必须逐字覆盖
冻结八题，Dockerfile 直接 `FROM` digest 且没有下载/包管理，manifest、supervisor bundle、资源
envelope 和 labels 都有独立内容 hash。root supervisor 的 correctness receipt 绑定 request/patch/
candidate state/evidence；exact apply 不存在 fuzz fallback；发现任何残留 uid-65534 process 时先清理
再 fail closed；private result 为 atomic 0600 文件且不接受 stdout。专门攻击回归让 fake uid-65534
pytest 进程写出全 passed 与 1µs duration，要求 capability gate 在 subprocess 前拒绝，并校验
`in_process_candidate_outcome_unattestable` verdict 的 canonical content ID。测试使用 fake source
manifest 与 fake process table，不调用 Docker、网络或 evaluator。

### `tests/test_hb_sweperf_source_lock.py`

验证 SWE-Perf source-lock preparer 只向 Arrow 请求 `repo/instance_id/base_commit/version/
efficiency_test/test_functions/problem_statement_realistic` 七列；gold patch、test patch、head commit
与 human patch sentinel 不得进入内存投影或产物。测试同时覆盖 detached commit/Parquet/task hash
不匹配、冻结八题顺序、由公开 `test_functions` key 派生 allowed paths、内容寻址幂等，以及禁止
subprocess/socket 的零 Docker、零网络、零模型、零 evaluator 合同。缺本地 RepoDigest 或仍由
worker 与 pytest reporter 同进程、无法由 root 独立导出 outcome/call-duration 时，只允许产出带
capability verdict 的 `blocked` report，不能生成 runnable source lock。

## 注意

- 单测使用 mock harness / mock Builder 响应,不消耗 API;`run_experiment.py` 的冒烟测试才需要有效 key。
- 新增题库导入脚本后,必须重跑 `test_benchmarks_are_valid` 确认"修复前必挂"。
- 新增 eval 逻辑(防作弊规则、超时等)时在 tests/test_eval.py 同步补用例。
- 新增生成物合同或提取逻辑时,在 tests/test_builder.py 先补复现用例。
- 当前完整 benchmark 结构测试会逐题运行隐藏 stub，全部测试约 1 分钟。
- `ssh-preflight` / `ssh-evaluate` 属于显式远端集成测试，默认单元测试不会运行；执行前确认
  SSH alias、固定 GPU 和 artifact 绝对路径，结果不得写进 worktree。

### Moss 实验一 CLI

```bash
python -m pytest -q tests/test_experiment_one_cli.py
```

该模块纯离线验证两份固定 manifest、A/B/C 与 S1/S2/S3 不可改、上下层模型必须为
`gpt-5.6-sol`/`high`/Responses、8 轮上限、每 suite/instance/seed 路径隔离，以及
`canary/evolve/freeze/cross-test/resume` 缺少 `--execute` 时不构造生产 controller、不写目录。
测试中的 controller 只验证调度边界，不返回或伪造正式实验分数。

### 实验一 Harness 结构门禁

```bash
python -m pytest -q \
  tests/test_experiment_one_production.py::test_frozen_h0_conversion_and_production_probe_enforce_model_and_tool_requirements
```

该回归测试锁定 production probe 的通用边界：单次和多次模型调用都允许，不设置模型调用次数
上限；至少必须有一次模型调用；最终输出仍由 `TaskHarnessSpec` 强制为唯一且位于最后的 `emit`；
未知工具必须拒绝，显式白名单工具才可通过。该测试不调用模型或官方 evaluator。

### 实验一最终答案 Contract Skill 绑定

```bash
python -m pytest -q \
  tests/test_dual_harness.py::test_output_contract_is_bound_only_to_the_model_node_that_feeds_emit \
  tests/test_experiment_one_production.py::test_edge_single_round_executes_solver_evaluator_and_builder_once \
  tests/test_experiment_one_production.py::test_ale_single_round_executes_solver_public_evaluator_and_builder_once \
  tests/test_experiment_one_production.py::test_production_task_runtime_uses_the_same_bound_contract_for_every_phase \
  tests/test_experiment_one.py::test_public_solution_contract_failure_is_recorded_with_its_specific_reason
```

这些测试锁定：公开交卷合同只追加到真正生成最终候选的模型节点，中间分析节点不被要求输出最终
JSON/代码文件；EdgeBench、ALE-Bench 的进化、H0 与交叉测试绑定同一 contract identity；公开格式
错误会在 abandoned receipt 中留下具体且有界的原因，而不是只记录模糊的 `ValueError`。测试使用
fixture 响应，不调用真实模型或 evaluator。
