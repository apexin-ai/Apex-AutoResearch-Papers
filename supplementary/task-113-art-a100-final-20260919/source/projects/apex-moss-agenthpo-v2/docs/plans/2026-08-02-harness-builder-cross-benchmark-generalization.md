# HB-GEN-1：HarnessBuilder 跨 Benchmark 泛化与持续学习实验

状态：执行中；当前处于合同冻结、规则库整理和 evaluator reference canary 阶段。真实模型搜索只能在对应 evaluator 的 reference 与对抗 canary 全部通过后启动。

## 1. 要回答的问题

本实验不再把“某个 Harness Prompt 能否刷高分”作为核心问题。要验证的是一个上游 HarnessBuilder：

1. 它能否根据新 instance 的结构选择合适的第一版 Harness；
2. 它能否根据本题逐轮反馈选择合适的 Harness 进化方向；
3. 从其他 instance 学到的经验，能否迁移到未见 benchmark；
4. 在严格 `test-then-learn` 下持续吸收新题经验后，它是否越来越好。

HarnessBuilder 的输出空间是系统级 Harness，不只是一段 Prompt。可变部分包括 context builder、角色图、Skill、记忆视图、父代选择、discipline/dream/law-inversion/recombination 等提议算子、工具与 profiler、workflow、scheduler、recovery/restart 和最终 solution directive。Evaluator、任务合同、预算、账本和最终裁决永远在 Builder 外部。

## 2. 为什么正式测试不再包含 KernelBench

P1/P2/P2b 的历史轨迹来自 KernelBench 的两道题：

- `level1/40_LayerNorm.py`；
- `level2/56_Matmul_Sigmoid_Sum.py`。

其他 KernelBench instance 虽未见过，但继续用 KernelBench 做正式测试只能证明同 benchmark 内迁移。HB-GEN-1 因此把 KernelBench 降为 meta-train 来源，正式 24 题来自三个未进入经验库的 benchmark。

## 3. Meta-train：8 个 KernelBench instance

固定 commit：`423217d9fda91e0c2d67e4a43bf62f96f6d104f1`。

已有完整轨迹的两题：

1. `level1/40_LayerNorm.py`
2. `level2/56_Matmul_Sigmoid_Sum.py`

新增六题：

3. `level1/21_Sigmoid.py`
4. `level1/92_cumsum_exclusive.py`
5. `level1/97_ScaledDotProductAttention.py`
6. `level2/45_Gemm_Sigmoid_LogSumExp.py`
7. `level2/57_Conv2d_ReLU_HardSwish.py`
8. `level2/67_Conv2d_GELU_GlobalAvgPool.py`

六道新题用冻结的通用 Builder 运行 v001–v008，产生训练轨迹。`cross_instance_distillation` 只读取公开、已封存的 Harness 决策、任务机械描述符、正确性、分数、成本和失败类型；不复制候选代码、私有 evaluator 日志或未封存测试结果。其输出形成 `moss-kernelbench-meta-train-v1`，随后冻结为 B* 与 B-online 的共同初始 Experience Bank。

两道历史题的导入规则冻结为
`hb-gen1-kernelbench-historical-all-lanes-v1`：每题只生成一个 **ALL-LANES aggregate**，绝不按
winner、最好分或最终 incumbent 选轨迹。先按原追加顺序收集 P1 全部 terminal lane attempt，随后
收集 P2 全部 terminal round 和已消费但缺失 Harness artifact 的终止尝试，再拼接 P2b 全部已评分
attempt/round、已评分但 profiler artifact 中断的尝试及全部无效 policy artifact；两源内部顺序
始终等于各自 ledger 顺序。每个 summary 只含 phase/lane/version/event ID、公开 Harness/policy
结构与 hash、正确性、speedup、reason-coded failure、资源成本及公开 structure/profile 摘要；禁止
candidate source、raw response、私有路径、私有 evaluator/log 或隐式思维链。所有实际读取并贡献
字段的生成、决策、评分、纠正、profile 和终止失败事件都进入 provenance，不能挑选成功事件。

冻结源合同在
`optimization_lab/harness_builder/data/historical_trajectory_sources_v1.json`：P1/P2 ledger 为 548
events、SHA-256 `2b1048012857c50a487830da5c380a04c7d19954996dc7538b70ef7686c120c0`，
campaign plan SHA-256 为
`cbade2206737952dc981709c56c3159871cce3a507ce2e0a45e045046b37d452`；P2b ledger 为 402
events、SHA-256 `da5d862309d31a1135ca5df16603b66d76a62bf3f54fd2edea443f96767472f6`，
plan SHA-256 为 `a83580b2c226e5631b1bd3bfb9fb66ff672f27d8e064e4ca0f877cab35b8773c`，且
ledger 尾必须是 completed `p2b-phase:completed`。导入器非阻塞取得 pilot `.ledger.lock`，再按
`.p2b-runner.lock → .ledger.lock` 取得 P2b 双锁，在锁内前后两次读取并核对四个 SHA；候选、Harness、
policy 的内容 hash、metadata 和 parent/version 绑定任一不可证明时，只写 content-addressed blocked
prepare，不生成轨迹。冻结事实下 LayerNorm 为 P1/P2/P2b `11/24/22` 个 summary，Matmul+Sigmoid+Sum
为 `11/24/26`；trajectory 对象按 canonical JSON 内容寻址，source binding 以 source ID 稳定键
绑定 source/trajectory SHA。

Apex-Tune 与其他开源系统提取出的 discipline、dream、law inversion、recombination、archive diversity、progressive evaluation 等规则属于 A/B0/B*/B-online 共用的动作词表，不算作 B* 独享经验。这样 `B*−B0` 只归因于跨-instance轨迹，而不是更多工具或不同 Prompt。

## 4. 三个正式测试 benchmark，各 8 题

### 4.1 KernelBenchX：量化与混合精度

- 代码与数据 commit：`fd4192293bf9a8c645327a9d46aa1e807f1f9cf2`
- 官方项目：[KernelBenchX](https://github.com/BonnieW05/KernelBenchX/tree/fd4192293bf9a8c645327a9d46aa1e807f1f9cf2)
- 评测：call → execution correctness → performance

固定八题：

1. `Quantization/conv2d_w8a8.py`
2. `Quantization/layernorm_w8a8.py`
3. `Quantization/bmm_w8a8.py`
4. `Quantization/attention_w8a8.py`
5. `Quantization/matmul_w8a8.py`
6. `Quantization/linear_w4a16.py`
7. `Fusion/fused_relu_max_pool2d_conv2d.py`
8. `MatrixMultiply/matmul_fp16.py`

最初预注册的第 7 题是 `Activation/gelu_bf16.py`。正式搜索尚未产生任何分数时，reference
canary 发现该题当前官方 performance 输出把单 tensor shape 写成 `[4096]`，而冻结 golden
写成 `[[4096]]`；call、correctness 和 timing 本身均成功，但无法按精确 input binding 形成可信
speedup。失败 attempt 和 seat 永久保留，不放宽 parser。替换规则在查看任何替代题 runtime 前
冻结为：固定 KernelBenchX commit 和用于重名排除的 TritonBench commit
`603e28a5050e8c268f6883a69709d477a272d49a`，对全体 KernelBenchX task 按
`SHA256("hb-gen1-v2|kernelbenchx|" + task_id)` 排序，从失败 digest 后严格向后扫描；排除
TritonBench 同 basename 以及当前 perf serializer 无法与 A100 golden 每行精确绑定的任务，且不
读取替代题 runtime/speedup。依次排除 `fused_gelu_min`（schema 不同）及四个 TritonBench 重名题
后，首个合格项是 `Fusion/fused_relu_max_pool2d_conv2d.py`（selection digest
`619f5a9d...b17f3ca`）。完整扫描证据冻结在
`optimization_lab/harness_builder/data/kernelbenchx_replacement_v1.json`；新题必须在新
staging/code revision 中通过完整 reference 与对抗 canary 后才能进入正式流。

KernelBenchX 建立在 TritonBench 基础上；两个仓库当前有 120 个同名 task basename，因此 TritonBench 不再作为独立 benchmark。上述八题在固定 TritonBench checkout 中均无同名任务，避免把同一任务重复计算成跨 benchmark 证据。

### 4.2 CompilerGym cBench：LLVM pass 序列优化

- release commit：`64bdd6cd39967d3d2fe5e6c72deb15e830b838bb`（v0.2.5）
- 官方项目：[CompilerGym](https://github.com/facebookresearch/CompilerGym/tree/64bdd6cd39967d3d2fe5e6c72deb15e830b838bb)
- 目标：正确性验证通过后，最小化 LLVM IR instruction count

固定八题：`qsort`、`bitcount`、`bzip2`、`crc32`、`dijkstra`、`stringsearch2`、`blowfish`、`susan`。`rijndael` 在固定的 CompilerGym v0.2.5 中没有语义 validator，故按预注册 SHA-256 选择规则由具有 baseline-valid ordinary validator 的 `stringsearch2` 替换；`sha` 的 v0.2.5 validator 忽略了 `validate_sha_output()` 的返回值，不能形成可信 correctness gate，因此在任何正式分数产生前由 20/20 ordinary validators 通过的 `blowfish` 替换。两次替换、bitcode SHA、selection digest 与原因全部进入冻结 manifest，不允许在看到分数后换题。

候选不是 Kernel 源码，而是有界 LLVM pass/action 方案。HarnessBuilder 仍控制角色、记忆、父代、搜索规则、工具、调度与恢复；benchmark adapter 负责把最终方案翻译为 CompilerGym action sequence。

### 4.3 SWE-Perf：真实仓库性能补丁

- evaluator commit：`9e8fed285ed640b51baaf66b13773706dc95aa45`
- dataset commit：`6298f128c550e92ac25af17653cf092224046516`
- dataset parquet SHA-256：`7c682ebdc080078ad936b6ddcb2b802227e5c91b933bd812077bce7ad6d70253`
- 官方项目：[SWE-Perf](https://github.com/SWE-Perf/SWE-Perf/tree/9e8fed285ed640b51baaf66b13773706dc95aa45)
- 官方数据：[SWE-Perf dataset](https://huggingface.co/datasets/SWE-Perf/SWE-Perf/tree/6298f128c550e92ac25af17653cf092224046516)

为避免 54 个 xarray instance 支配样本，先取至少含 3 个实例的八个 repository，再按 `SHA256("hb-gen1-v2|swe-perf|" + instance_id)` 每仓库选最小值：

1. `astropy__astropy-13817`
2. `matplotlib__matplotlib-24250`
3. `mwaskom__seaborn-2313`
4. `pydata__xarray-9407`
5. `pylint-dev__pylint-7747`
6. `scikit-learn__scikit-learn-12625`
7. `sphinx-doc__sphinx-12615`
8. `sympy__sympy-25205`

模型只看到 realistic problem statement、允许的 repository files 与本题公开反馈；human patch、head commit 内容和私有 evaluator 原始日志不进入 Builder 或 solution generator。

上游每题 image digest 只固定依赖环境和 base repository，不等同可信 evaluator image。正式 canary
前必须以 `--pull=false --network=none` 的离线 context 为每题叠加 root-owned
`/opt/hb-sweperf/bin/evaluate-stage`，并把 task manifest、supervisor bundle、上游 ref、资源 envelope
与最终 wrapper RepoDigest 全部绑定。wrapper 固定 10 CPU/32 GiB/512 PID；candidate patch 只走
`git apply --check` 后的 exact apply；stdout 不裁决；correctness receipt 和 worker/context quiescence
未满足时不得计时。执行细节见 `docs/runbooks/hb-gen1-sweperf-wrapper.md`。

离线攻击红测进一步证明：当前上游 pytest 命令让任意 candidate Python 与 JSON reporter 位于同一个
uid-65534 进程，candidate 因而可以直接伪造 per-test outcome、pytest call duration 与退出码。
root-owned 结果文件、nonce/HMAC、私有 FD 或外部进程 monitor 都无法从外层 wall clock/quiescence
推出这两个冻结评分信号；改用外层 wall clock 又会改变 scoring 语义。生产 supervisor 已在启动
worker 前固定 fail closed，source-lock report 以内容寻址 capability verdict 记录
`in_process_candidate_outcome_unattestable`。因此 SWE-Perf 当前不能进入 canary 或正式搜索；继续
使用它必须另行批准 task-specific out-of-process oracle（或等价新 scorer），不得把现有 worker JSON
包装成可信事实。

## 5. 四个实验臂

| 臂 | 初始 Harness | instance 内自进化 | 跨 instance 经验 | 24 题期间更新 |
|---|---|---|---|---|
| A | task-conditioned | Harness 冻结，Kernel/solution 继续迭代 | 无 | 否 |
| B0 | 通用 Builder 决定 | 是 | 无 | 否 |
| B* | 训练后的 Builder 决定 | 是 | KernelBench meta-train v1 | 否 |
| B-online | 与 B* 逐字相同起点 | 是 | KernelBench meta-train v1 | 每道首次测试封存后更新 |

每题每臂均为 v001–v008：每轮一次 Harness/planner call、一个正式 solution attempt。A 的 v002–v008 planner call 运行冻结 sham planner，以匹配模型调用、token 上限、Kernel/patch/action opportunity 和上下文长度。四臂使用相同模型、reasoning 配置、工具 capability 和 evaluator。

## 6. Test-then-learn 状态机

对当前 instance：

1. 绑定当前 B-online checkpoint hash；
2. 在 A/B0/B*/B-online 四臂完成八轮并封存；
3. 首次见面分数进入泛化报告；
4. 运行 `cross_instance_distillation`，只读取本题已公开、已封存的四臂轨迹；
5. 产出带父版本的新 Experience Bank 和 Builder checkpoint；
6. 下一道未见 instance 才可读取该 checkpoint。

同一道题的更新后复跑只能标为 training diagnostic，不能改写首次见面分数。

Builder 采用两种时间尺度更新：在同一轮 24 题的在线阶段，只更新内容寻址的 Experience Bank 与 Builder checkpoint；新 checkpoint 可在下一题选择不同的初始 role graph、memory/tool/workflow、parent strategy、scheduler/recovery 和进化规则，但 TrustedOperatorRegistry、schema、scorer 与预算保持冻结。这样 B-online 确实会改变后续 Harness 架构，又不会在半途改实验规则。24 题全部结束后，只能提升规则的经验支持级别，或在确有新执行语义时提出下一版 Rule Registry/new trusted operator；本轮题库随即降级为训练/回归集，任何新版本都必须在另一批 fresh instance 上重新测泛化。

当前冻结输入升级为 provenance-bound Rule Registry v2。它逐条绑定来源仓库、固定 commit、路径、行区间、文件 SHA、迁移说明及三轴置信度，并把“来源中有这个想法”和“本轮 controller 能执行这个动作”分开：`discipline`、`dream`、`law_inversion`、`recombination`、`correctness_recovery` 五条绑定受信任 operator，可被 Harness decision 选择；`successor_followup`、`stagnation_rebalance`、`archive_diversity`、`progressive_evaluation`、`failure_directed_mutation`、`parent_fertility_balance`、`workflow_graph_mutation`、`archive_reflection` 八条只作为 planner 的 advisory cards，不能直接执行；`cross_instance_distillation` 仍是四臂封存后的外层动作。所有 task-specific 数值阈值仍必须来自独立的冻结合同/profile，不能硬编码进通用 Registry。

24 题排成 8 个 block，每个 block 含三个 benchmark 各一道。各 suite 内按 selection digest 排序；suite 顺序按三阶轮换，arm 顺序按四阶 Latin rotation，所有顺序在 prepare artifact 中冻结。B-online 因此不能先学完整个 benchmark 再测另一个。

进入下一题前，Experience Retriever 按当前题的机械 descriptor 与历史记录 descriptor 的
重合度做有界、确定性检索，并同时携带初始 Harness 结构、进化规则触发条件、收益、反例和
派生支持级别。同题记录机械排除；原始单题记录不改写，支持级别由其他已封存 instance 的数量
和 benchmark 数即时复算。这样经验既能进入 Builder 的实际上下文，又不会被单题观察直接升级
为通用默认规则。

## 7. HarnessBuilder 的真实可执行搜索空间

每个 Harness decision 必须产出严格 JSON，并至少绑定：

- `role_graph`：分析、批评、生成、验证等角色拓扑；
- `memory_views`：current、best、failure、structural-diverse、cross-instance records；
- `tools`：task semantics、score、diff、static structure、公开 profiler 或 compiler observation；
- `parent_strategy`：reference、incumbent、stable-best、restart、recombine；
- `rule_id`：只能从当前 Builder allowlist 的五条可执行规则中选择；其可信 action/guardrails 由 controller 注入，advisory/external rule fail closed；
- `workflow`：步骤与输入输出依赖；
- `scheduler_mode` 与 `recovery_mode`；
- solution directive。

`rule_id` 标签和 solution directive 均不单独计入 operational fingerprint；换标签或改措辞而不改变角色图、记忆、工具、父代、workflow、scheduler 或 recovery，不能冒充系统级 Harness 进化。每次编译保存 `RuleDecisionTrace`，绑定 Registry SHA、operator、source refs 与 write paths；声明了但 runtime 没有实现的字段 fail closed。

## 8. 指标

每个 instance 的可信 reference/baseline 归一为 1.0，错误 candidate 不更新 incumbent。主要记录：

- `initial_score`：v001 的正确性门控分数；
- `final_best`：v008 后历史最好；
- `evolution_gain = final_best / max(initial_score, reference)`；
- v001–v008 running-best log AUC；
- 首次超过对照 2% 的轮次、模型 calls、evaluator 秒和 GPU 独占秒；
- all-attempt correct yield；
- 各 rule 的触发条件、成功/失败、成本和适用范围。

核心 contrasts：

1. `B*−B0`：离线跨-instance经验的泛化价值；
2. `B-online−B*`：test-then-learn 的持续学习价值；
3. `B*−A` 与 `B-online−A`：Builder 相对一次性 task-conditioned Harness 的价值；
4. v001 contrast 与 v002–v008 conditional gain 分开报告，分别对应初始化和进化方向。

操作性通过线，不表述为总体统计显著性：

- `B*−B0` 的 24 题中位 AUC 差至少 0.005；
- 至少两个 benchmark 的中位 final ratio `B*/B0 ≥ 1.02`；
- 剩余 benchmark 不得低于 0.98；
- all-attempt correct yield 不得劣化超过 10 个百分点；
- 每题每臂的最终 winner 用三个全新 process 复测，discovery score 不进入复测中位数。

B-online 另报告随 stream position 的 forward-transfer 曲线。若只在已经学过的 instance 上变好、对下一道未见 instance 没有改善，则持续学习结论失败。

## 9. 资源上限

| 部分 | 模型调用 | solution attempts | evaluator transactions |
|---|---:|---:|---:|
| 六道新增 KernelBench meta-train + distillation | ≤104 | 48 | 48 |
| 24 题 × 4 臂 × 8 轮 discovery | 1,536 | 768 | 768 |
| 每道后的 B-online distillation | 24 | 0 | 0 |
| 固定模型/推理档位/传输方式 runtime canary | ≤2 | 0 | 0 |
| evaluator canary：24 个 reference + 每个 evaluator family 一组对抗样本 | 0 | 0 | 34 |
| 24 题 × 4 臂 × 3 fresh retest | 0 | 0 | 288 |
| 合计/硬帽 | ≤1,666 / **1,700** | **816** | 1,138 / **1,140** |

其他硬帽：

- 模型固定为 `gpt-5.6-sol`、`high` reasoning，通过已登录 ChatGPT 的隔离
  `codex exec 0.144.6` 调用；四项均写入 run signature，禁止静默降档、换模型、换客户端或换 provider；
- GPU 独占秒：250,000；
- CPU evaluator 秒：1,450,000；
- GPU4 严格串行；SWE-Perf container 可并行，但每 instance/arm 内串行；
- 使用现有登录态模型；禁止自动切 TokenRouter 或其他付费 provider；
- 任一局部额度不能向另一 benchmark 借用；started 即预留并计费。

每个正式 instance/arm cell 固定 16 次模型调用与 11 个 evaluator seat（8 次 discovery + 3 次 fresh retest）。KernelBenchX cell 固定 6,600 GPU 独占秒，CompilerGym cell 固定 3,300 CPU evaluator 秒，SWE-Perf cell 固定 39,600 CPU evaluator 秒。六个新 meta-train cell 各为 16 calls、8 eval、4,800 GPU 秒；其余 distillation/canary entitlement 在 staging plan 逐 cell 固定且不可转移。全部 cell entitlement 机械求和为 1,666 calls、1,138 eval、246,600 GPU 秒与 1,416,000 CPU 秒，均低于全局硬帽。

## 10. 执行门禁

### Gate 0：合同冻结

- manifest、provenance-bound Rule Registry v2、Builder variant v2、Experience Bank schema 和顺序计划全部 canonical hash；
- 旧 P1/P2/P2b 目录只读且 SHA 不变；
- B* 初始经验不能含三个测试 benchmark 的轨迹。

### Gate 1：Evaluator canary

每个选中 instance 的 reference 必须通过；错误/no-op/伪 stdout 候选必须失败。KernelBenchX 的 reference 不能直接使用含 dataset 分隔符和内嵌 tests 的 task 文件；必须先绑定完整 task SHA，只机械抽取实现段，并让该段重新通过正式 solution codec。抽取结果及 manifest 必须分别内容寻址且不可覆盖，preflight 只接受 manifest 并复核 candidate hash/codec/task binding，不接受手工 candidate 路径。每 attempt 使用独立 scratch/cache；candidate stdout 不参与可信状态解析。CompilerGym 必须重放 action sequence，并按固定 source SHA、callback 注册长度与索引逐个执行所有 ordinary semantic validators；禁止调用会混入失效 sanitizer 的聚合 `env.validate()`。SWE-Perf 必须先由另行批准的 trusted oracle 解除 `in_process_candidate_outcome_unattestable`，再在固定 image 中先过正确性后计时；当前 worker-authored JSON/退出码不得进入 canary。任何 benchmark 的 canary 未闭合，只阻断该 benchmark，不用别的题静默替换。

### Gate 2：Meta-train 与 B* 冻结

补齐六道 KernelBench 轨迹，生成 Experience Bank v1 和 B* checkpoint；B* 与 B-online 初始 checkpoint 必须逐字相同。

### Gate 3：24 题 prequential 正式运行

按冻结 block 顺序执行。任一题未完成四臂前，B-online 不得更新。恢复只依赖 append-only ledger 与内容哈希。

### Gate 4：Fresh retest、报告与下一代经验

完成三次独立复测和结果报告后，把 24 题轨迹提升为 Experience Bank v2，生成下一代 Builder；本轮 24 题随即降级为训练/回归集，下一轮必须使用 fresh instance。

## 11. 产物边界

正式根目录：`/home/ubuntu/Projects/Moss/results/optimization_lab/harness-builder-gen1`。

必须保存：合同、source snapshot hashes、Builder/Experience Bank 父图、每轮 Harness decision、`RuleDecisionTrace`、solution artifact、公开反馈、私有 evaluator evidence、模型 usage、预算、恢复事件、首次见面曲线、fresh retest 和最终报告。所有事实追加写；dashboard 是可重建视图。

本实验没有 P3、leaderboard 上传、自动扩 benchmark、自动扩预算或自动换 provider 入口。
