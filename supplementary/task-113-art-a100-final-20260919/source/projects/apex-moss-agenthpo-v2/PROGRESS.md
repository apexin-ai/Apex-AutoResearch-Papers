# PROGRESS

## 2026-09-06 — v2 Builder 诊断可见性与多步 Harness 修复

- 问题：Builder 旧 projection 只给分数、短反馈和结构摘要，缺少当前候选正文与 task-bound 诊断，
  难以针对实例选择 mutation；下层 Harness 也把 workflow 当作一次 solution call，多节点结构
  无法真正执行或审计。
- 解决：Builder projection 现在提供有界当前候选（hash/长度/截断标记），controller 在 proposal
  前确定性运行公开 allowlist 工具并注入 `pre_decision_tool_outputs`。新增兼容的
  `execution_mode`：默认 `single_solution` 保持旧预算，显式 `multi_step` 按编译 workflow
  stage 分别调用模型，stage 间传递有界输出，最终候选取 `generate` stage；每个 stage 使用独立
  journal operation，round receipt 记录响应 SHA、provider 与 usage，started-without-artifact
  仍永久 abandoned、禁止重发原 operation。
- 验证：全仓离线 pytest `527 passed in 316.25s`，定向 Builder runtime/runner/evolution 测试
  全部通过，`git diff --check` 通过；未运行真实模型、evaluator 或 GPU。
- 实现提交：`0ca6a05`

## 2026-08-29 — Moss V2 main refresh

- 从 `origin/main` 重新核验后，远端主线仍为 `c52a2bd`；V2 改动在隔离分支基于该提交继续完成，未覆盖主 checkout 的用户未提交文件。
- 新增 EdgeBench/ALE-Bench schema-2 manifest，并在 CLI 增加显式 `--harness-version v1|v2`；默认仍为 V1，历史 manifest/hash 与回放语义不变。
- schema-2 静态公开工具统一经过固定 `ToolRegistry`，生成稳定 operation id 和 append-only receipt；evaluator 工具在 Task Harness 内 fail closed。
- cross-test Solver/evaluator 异常写入 `error.evidence.json`，receipt 为 `invalid` 且 `official_score=null`，不自动 retry、不把异常转成 0。
- 新增 V2 manifest、工具审计和失败保留回归测试；使用仓库已有 `.venv` 验证，重点回归当前为 `60 passed, 1 skipped`（后续将再跑完整套件）。

## 2026-07-27 — Pilot Builder 恢复与生成物门禁

- 问题：通用 v001 在四格基准上开局 100%，进化无法产生新版，实验出现天花板效应。
  Builder 首次生成物又因内部 Markdown 围栏被非贪婪正则截断；恢复候选随后两次违反工具合同
  （把 `run_tests` dict 当字符串、使用错误参数键），导致正式跑分把基础设施错误表现成 0 分。
- 解决：保留冻结题库、模型、计分与判定线；将无效结果隔离，增加外层代码块提取、AST/合同、
  工具参数与返回类型校验，以及仅依据合同错误的零样本修复。最终 Builder 132/132 次正式
  task-run 通过，0 error、0 tamper；完整结论写入 `RESULTS.md`。
- 避免：所有生成代码必须使用 `skills/validate-generated-artifacts/`，按“提取 → 编译 →
  静态合同 → 离线 smoke → 单题 canary → 正式运行”门禁推进；出现 import/contract error、
  0 steps/tokens 或异常短耗时时，不得解释为能力分数。执行中若需要脱离现有 plan 设计新路线，
  先暂停并通知用户进入方案模式。
- 实现提交：`b492a71`

## 2026-07-27 — BigCodeBench-Hard 难度 canary

- 问题：原 HumanEval/MBPP/QuixBugs 题库满分，无法区分 Harness；需要先小批量校准更难题。
- 解决：固定导入 5 道依赖轻量的 BigCodeBench-Hard v0.1.4 任务，导入时强制验证 stub
  失败、官方 oracle 通过，再按门禁先跑 1 题、后跑 4 题。保持原
  `claude-haiku-4-5` + TokenRouter 路线，单遍共使用 111,266 executor tokens。
- 结果：v001 仍为 5/5（100%），0 error、0 tamper，未达到 50–80% 目标，不能扩大为正式
  实验。完整测试可见且允许迭代重试，显著降低了 BigCodeBench 原本的一次生成难度。
- 避免：正式扩题前必须先做 3–5 题同协议 canary；下一轮优先设计“公开规格/少量可见测试
  + 隐藏终验”或真实仓库级任务，而不是继续堆测试完全可见的单函数题。进入方案模式前先
  输出可直接交接给更强模型的完整 Prompt。
- 实现提交：`6daf0f1`

## 2026-07-27 — Hidden Final Verification V1 校准

- 问题：同一批 BigCodeBench-Hard 在完整测试可见时仍为 5/5，无法区分 Harness；同时生成
  代码与评分器同进程，隐藏套件必须在不改冻结工具的前提下与 Harness 隔离。
- 解决：增加 work_dir 路径护栏、静态 Harness 沙箱、全新目录隐藏终验、只落计数的结果结构
  和基础设施失败分类；V1 每题只暴露第一个行为测试。导入器固定官方 v0.1.4 commit 与
  Parquet SHA，rows 服务 500 时仍可重建同一数据。P0 红测还发现现存 builder0 使用纯
  `os.path.join`，因此在冻结前将它收窄为唯一额外 os 例外并加入回归。
- 结果：先跑 1 题再跑 4 题，v001 为 4/5（80%），83,959 executor tokens；0 harness/env
  error、0 tamper、0 contract violation。起始 V1 已落入预注册 3–4/5 带，故冻结 V1，
  不运行 V0/V2；失败的 274 为可见全过、隐藏 4/6 的有效 capability failure。
- 避免：隐藏协议必须在首次模型调用前同时冻结任务 manifest、文件哈希、信息边界和移动规则；
  结果中不得保存隐藏测试文本。外部 rows 服务不可用时只允许切换到内容寻址的同版本官方
  文件，不得换题或改测试。
- 实现与冻结提交：`ca584f0`

## 2026-07-27 — 隐藏终验正式池冻结

- 问题：标准库候选只有 22 题；按预注册安装 numpy/pandas 后也只有 43 题进入质量门禁，
  且 5 题官方 oracle 在冻结环境失败。bugfix AST 变异最终也只有 12/19 题满足“可见过、
  隐藏挂”，少于正式族所需 18。结构回归测试首次直接在 benchmark 目录跑 stub，`-x`
  提前退出还留下 3 个测试临时文件，险些污染冻结题目。
- 解决：按预注册最低规模把两族缩为 train8/val10/reserve1；B 族整体回退为 V0
  `specgen_hidden`。所有选择由 `sha256(task_id)`、固定依赖/seed/算子顺序机械完成，
  manifests 记录环境版本、剔除原因和文件哈希。结构测试改在全新临时目录运行，误产物在
  冻结提交 amend 前删除。
- 结果：`tddgen_hidden` 与 `specgen_hidden` 各 18 道正式题，彼此及 canary task_id
  全不相交；36 道隐藏 stub 全部失败、108 个题目文件哈希复算一致、36 个仓库测试全绿。
  两份新 v001 与原通用 v001 逐字一致。Q2 后续只能解释为信息形态差异。
- 避免：任何会执行第三方测试的校验都必须在临时副本中运行；冻结前除白名单任务文件外
  扫描额外产物。正式池不足或变异不足只走预注册缩容/回退，不临时增加依赖、算子或换题。
- 实现与冻结提交：`c4525ec`

## 2026-07-27 — Hidden Final Q1/Q2/Q3 正式终验

- 问题：旧 pilot 因四格 100% 无法识别专化；新隐藏终验还先后遇到消息配对错误、单次隐藏
  判分环境错误、调度切换中断和预算预留门禁，任何错误格都不能当作能力分或跨尝试拼接。
- 解决：冻结新题池与信息边界后，使用三 lane 受控并行；每 lane 保持队列顺序，每格 3 遍
  一次跑完。无效格整体移入 `results/invalid/` 后从头重跑；用户批准有效正式预算从 13.5M
  提至 16.5M，1.5 倍开跑预留不变。补回归使 runner 退出时明确写入 complete/paused。
- 结果：Q1 的 tdd train 提升 20.8 点而 val 下降 3.3 点，证明强训练专化但泛化/应试仍在
  灰区；spec 进化未生效。Q2 按冻结 raw 主场差过线，但经 v001 难度归一后仅 −6.7/+3.3
  点，只能作为探索性信息形态信号。Q3 两个 Builder 可执行，但 val 分别下降 16.7/3.3 点，
  未达到零样本生成成功线。10 个有效新格共 10,794,315 executor tokens。
- 避免：跨题族 raw 分差不能独立识别 Harness 专长；后续应使用同一底层任务的反馈形态配对
  版本，并以相对共同基准的交互效应为主指标。灰区结果应增加独立任务与独立进化谱系，而不
  是只在同一题上增加重复。
- 实现提交：`2d6e8fe`（受控并行）、`39d33b6`（预算修订）、`6e290e4`（终态落盘）

## 2026-07-27 — Q2 同题配对消混淆确认

- 问题：旧 Q2 的 tdd/spec val 基准相差 40 点，raw 主场差把题池难度误当成 Harness
  专长；首次配对正式格又发现 pytest runtime/teardown errors 被摘要关键字误标为环境错误。
- 解决：对旧 20 道 val 全集生成只改变可见测试的 V0/V1 配对视图，用 v005 相对 v001 的
  paired difference-in-differences 和固定 seed task bootstrap 作主指标。评分分类改用 pytest
  returncode：1 为 capability，-1/2/3/4/5 与 collection/internal 为 infrastructure；两个
  旧格整体隔离后从头重跑。
- 结果：tdd/spec block 交互分别 −10.0/−3.3 点；综合 −6.7 点，95% CI
  [−15.0,+1.7]，按冻结线为方向反证。四个有效新格 3,946,778 executor tokens；旧 Q2 的
  +33.3 点 raw 主场优势不能归因于反馈形态专长。
- 避免：跨题池比较必须先做共同基准归一或同题随机/配对；pytest 的 test/setup/teardown
  exception 是候选行为，不得仅凭输出含 `errors` 判基础设施失效。
- 实现提交：`bf3cdb8`（配对协议与产物）、`415ab5d`（错误分类修复）

## 2026-07-28 — Q1 独立谱系与 external 确认

- 问题：旧 R0 只有一条成功谱系且旧 val 变化在灰区；R1 quick 又出现版本间任务交换、
  单遍 75% 和约 10× token 膨胀，无法判断训练提升能否复制或迁移。原六格并行顺序还可能
  在预算不足时先消耗低价值 R1 external，且 formal canary 未计入 24M 总账。
- 解决：按批准的修订 A/B1 把正式格改为 R2-train→v001/R0/R2-external→R1 两格；
  重建 quick/canary/无效消耗，正式 canary 单列入账，预算暂停后允许在主数据齐全时机械
  产出 `decision_complete`。每个生成版本继续经过原始响应、静态合同、严格离线 smoke 和
  单题 canary；77 项全套离线测试通过。
- 结果：R0/R1/R2 formal train 为 95.8/83.3/91.7%，R0/R2 满足 2/3 训练前提；
  external v001/R0/R2 为 41.7/44.4/41.7%，合格谱系平均增益 +1.39 点，95% CI
  [−4.17,+8.33]，冻结结论 `inconclusive`。R1 external 因 B1 预留门未启动且不影响主判。
  总消耗 23,180,336/24M，恢复阶段所有正式 run 均无 tamper/contract/infra。
- 避免：单遍 quick 只能驱动搜索，不能代替 formal qualification；总预算必须覆盖 canary
  与无效尝试；价值排序应先保证能改变判定的格。Harness 搜索后续必须同时约束回归与成本，
  否则会用数倍 tokens 在任务间交换得失。跨轮通用规则已写入
  `skills/validate-generated-artifacts/SKILL.md`：全调用记账、内容哈希缓存失效、
  canary 角色、暂停指针和 decision/matrix completeness。
- 实现提交：`514382a`（价值排序/B1 总账/部分分析）、`3a349ab`（准确预算暂停指针）

## 2026-07-28 — 三层 Benchmark 迁移资格协议

- 问题：旧进化循环只按 training benchmark 选版本，独立谱系虽能复制训练提升，却未在
  external test 上识别出稳定迁移；原下一阶段又把 selector 修复、Builder seed 和
  task-conditioned specialization 同时改变，失败时无法定位 optimizer 还是初始化。
- 解决：正式统一 Task → Benchmark → Benchmark instance 术语，机械冻结互斥的
  training16 / validation20 / sealed-test34；只运行两条逐字相同 v001 lineage。
  Proposer 只见本 lineage training trace，selector 只接收 validation 聚合分数；
  final/formal gate 全冻结后才 exact-once 解封 test。协议同时冻结整数/Fraction 判定、
  回归锁、三套状态机、WAL 恢复、100M 原子调用预留与 Builder go/no-go。
- 避免：已消费 test 只能降级为后续 training/validation，不能再次称 sealed；
  validation selection signal 不能冒充无偏迁移证据；单个 fresh test benchmark 上的
  提升只能称 benchmark-sample transfer，更强 Task-level 结论需要独立 benchmark/来源
  复制。并发产生的旧 v2 四谱系方向稿必须标为历史，仓库只保留一个待执行真源。
- 方案提交：`b80444a`

## 2026-07-28 — 三层资格实验 P0/P2 离线启动

- 问题：当前协议要求在任何模型调用前，先证明 16/20/34 三池快照、selector 精确边界、
  Proposer 可见性和 test-once 状态机都可离线审计；旧 runner 的全局 archive/path 语义不能
  直接承担这些新信息边界。
- 解决：新增独立 `scripts/three_tier_runner.py`，仅开放 `--prepare`。它以原 importer 的
  V1 stub/oracle/flaky 门禁重建 34 个 reserve，再把已消费 Q1 16、Q2 20 与 fresh reserve
  34 复制到 worktree 外的持久化快照；同时写内容哈希 manifest、实例 token 禁表、整数/
  Fraction gate 和 sealed-test 不可重跑状态机。新增 7 个离线回归，现有全套测试保持通过。
- 避免：准备阶段不接触 TokenRouter、Harness 或 sealed test 评分；若 manifest 缺少原始
  basename、存在 symlink/额外文件/池重叠，必须在落盘前失败。任何执行模型调用仍须完成 P1、
  P3 路由/账本预检并获得明确 100M 硬授权。
- 实现提交：`3c3c511`

## 2026-07-28 — 快照审计返回值修复

- 问题：`verify_protocol_snapshot()` 正确校验磁盘 digest，但在返回对象前从内存 dict
  移除了 `manifest_digest`，使调用方无法把已验证的 digest 写入后续 registry。
- 解决：对 digest 计算使用独立副本，返回完整 manifest；补回归断言并用已生成的
  16/20/34 快照复验 digest、17/17 test block 与 seed hash。
- 避免：审计函数不得为了校验而损失调用方需要冻结的证据字段。
- 修复提交：`805cc2c`

## 2026-07-31 — 具体调优任务 Harness 实验计划

- 问题：旧路线已经证明有限 training benchmark 上的 Harness 专化可以复制，但新
  benchmark 上的稳定迁移仍不明确；隐藏 pass/fail 反馈也不利于快速判断哪种 Harness
  结构有效。
- 解决：调研可连续评分的 AI-for-AI/性能优化 benchmark，首发选择仍活跃的
  KernelBench 固定 LayerNorm 与 Matmul 融合任务，每题独立 Harness，通过编译、正确性、
  速度三段反馈进化；Atrex-Bench 后置确认，已归档的 CompilerGym 仅作 CPU 备用。
  RE-Bench 因官方明确请求避免过拟合，未经书面许可不运行。
- 避免：允许具体任务专化不等于允许修改评分器或偷看答案；新实现应另建
  `optimization_lab/`，不得放宽旧 `eval.py` 与 sealed-test 协议。没有 GPU 的本机不能
  冒充运行前提，必须先做云 GPU 评分稳定性门禁并单独批准 API/GPU 硬帽。
- 方案提交：`19da44f`

## 2026-07-31 — KernelBench P0 与 A100 评分闭环

- 问题：本机没有 GPU；历史 A100 服务器系统盘接近满、账号没有 sudo/Docker 权限且各卡有
  常驻进程。原定 Matmul+Subtract+Multiply+ReLU 题的全零负例又通过 5/5 正确性检查并
  得到约 215×，不能作为有效优化目标。
- 解决：通过 `a100jump` 固定使用 GPU4，不干预其他进程；把 pinned KernelBench、uv、
  Python 开发头文件和所有缓存放到 `/data3/chenzhuofan/moss-kernelbench-pilot`。新增独立
  `optimization_lab/`，统一编译/正确性/速度反馈、追加式账本、预算门禁、SSH 评分和实时
  HTML 看板。按预登记规则在任何模型调用前把退化题替换为 Matmul+Sigmoid+Sum，旧异常
  分数保留但标为不计分；同一候选 ID 重跑不重复消费 GPU，ID 不能越出私有日志目录。
- 结果：两道有效任务的错误候选均被拒绝；正确参考候选各重复三次，LayerNorm 为
  0.994/0.970/0.971×，Matmul+Sigmoid+Sum 均为 1.000×，单次反馈约 24–53 秒；全套 97 项
  离线测试通过。账号仍无 Docker 权限，因此 P0 的全新容器复现未完成，未启动模型调用。
- 避免：性能题开跑模型前必须先用“可编译但故意错误”的负例验证评分器，异常快值不能只靠
  速度阈值判断；远端输出延迟时先核对追加式账本再声明中断，并用追加更正而非覆盖历史。
- 实现提交：`012be4e`

## 2026-07-31 — P1/P2 无调用 Campaign 合同

- 问题：P0 的干净容器仍待管理员资源，但 P1/P2 的结构、信息边界和停止规则若等开跑才写，
  容易在看到分数后临场改口径；同时模型、lane 上限和美元硬帽尚未获批，不能提前调用 API。
- 解决：新增 `campaign.py` 冻结每题三种 P1 基线与三条 P2 独立谱系，三谱系 seed 逐字相同、
  历史目录隔离、最多八轮；`optimizer.py` 机械处理连续三轮无正确/无速度进步、环境无效不计
  轮次、历史最好和恢复快照。`generation.py` 强制模型响应只有一个完整 `ModelNew` 代码块，
  只暴露脱敏短反馈，并不可覆盖地保存候选和原始响应。预算增加 API/GPU 独立美元硬帽；P0
  干净环境只认账本证据，不提供命令行绕过开关。
- 结果：真实 `campaign_plan.json` 已在持久化目录生成，P1 六个 baseline lane、P2 六条谱系
  均冻结，但因 P0、模型及四类上限未齐全保持 `execution_ready=false`，模型/GPU 新消耗均为
  0；全项目 117 项离线测试通过，CTO HTML 同步了当前状态。
- 避免：离线准备和正式实验必须分开命名；“计划可序列化”不等于“允许执行”。费用硬帽不能
  只用调用次数替代，环境确认也不能靠人工 CLI 布尔值伪造。
- 实现提交：`dee1706`

## 2026-07-31 — Docker GPU 复现二级门禁与双层机制说明

- 问题：管理员加入 Docker 组后，账号已能访问 29.4.3 daemon，但 `--gpus device=4` 仍报
  `no known GPU vendor found`；只确认 Docker 权限会把“能开普通容器”误当成“能开 GPU
  容器”。CTO 汇报还需要明确专用 Harness 与 Builder 的两种更新时钟。
- 解决：只读核验 daemon runtime 只有 `runc`，主机不存在 NVIDIA Container Toolkit、
  runtime、`nvidia-ctk` 或 CDI 定义；账本分别记录 Docker daemon ready 与 GPU runtime
  blocked。CTO HTML 新增任务内每轮 Harness 所见信息/可改结构/冻结边界，以及 Builder 在
  多任务 P3/P4 后、仅于任务批次之间更新的机制。
- 避免：GPU 容器门禁必须同时验证 daemon 权限、NVIDIA runtime/CDI 和指定 GPU smoke；
  Builder 不得被描述为单题每次得分后更新，也不能把尚未执行的机制写成已取得成绩。
- 文档提交：`eb935b9`

## 2026-07-31 — 实时看板展示冻结 Campaign

- 问题：P1/P2 矩阵已经写入 `campaign_plan.json`，但实时看板只展示 P0 评分事件；外部人员
  看不到正式实验为何尚未获准、十二条路线准备到了哪里，也容易把“计划中的 lane”误解为
  已经跑出的成绩。账本说明还可能带有内部评分日志的绝对路径。
- 解决：看板在同一持久化目录发现 campaign 计划时，只读取开跑状态、待补条件、两组路线
  和总消耗，以中文展示六个 P1 对照组、六条 P2 独立谱系，并逐条标记“待运行，不是成绩”；
  同时对资源说明和最近事件中的内部评测目录、Unix 绝对路径做公开页脱敏。
- 避免：管理看板必须区分“结构已冻结”和“实验已执行”；计划文件中的 artifact、seed、
  history 等路径即使方便调试，也不能原样复制到面向外部人员的 HTML。
- 实现提交：`43df9fa`

## 2026-07-31 — P1 离线端到端控制器

- 问题：P1/P2 虽已冻结矩阵、候选合同和预算占位，但尚无一条能证明执行门禁实际包住
  generator、归档、评分和账本的端到端路径；若直接接真实 API，草案误执行、恢复后重复计费
  或无效输出进入评分都可能到付费阶段才暴露。
- 解决：新增 `CampaignController`，用 fake generator/adapter 离线走通单个 P1 lane；它先检查
  `execution_ready` 和冻结 Harness 哈希，再预留模型/API 硬帽，强制提取唯一 `ModelNew`，
  不可覆盖地归档模型原文、代码与元数据，最后复用评分 runner 生成短反馈并把完整预算写入
  追加式账本。无效输出单独归档；同一 candidate ID 在当前进程和恢复后的新控制器中均直接
  复用既有反馈，不重复调用 generator 或 adapter。P2 继续只复用已测的 `LineageTracker`。
- 结果：新增 5 个控制器端到端回归；合并前全项目 122 项通过，合并最新看板后相关 39 项
  继续通过。没有连接 Docker、GPU 或真实模型 API，也没有改变 CTO HTML 或旧评分协议。
- 避免：昂贵执行链不能只测试各模块；必须用无网络替身证明门禁在最外层、资源在调用前预留、
  原始响应可审计且 candidate identity 可重放。真实 generator 接入前仍须获得 P0 和双硬帽。
- 实现提交：`2fa43c0`

## 2026-07-31 — KernelBench P0 隔离容器门禁通过

- 问题：Docker 组权限已生效，但服务器没有 NVIDIA Container Toolkit/runtime/CDI，标准
  `--gpus device=4` 路径不可用；不能因此沿用宿主虚拟环境并把它称为干净复现。
- 解决：构建固定 Ubuntu 摘要的最小 Python 3.10 镜像，从 KernelBench `uv.lock` 离线创建
  全新环境；容器禁网、只读根文件系统、删除全部额外 capability，只映射 GPU4 四个设备节点
  和三类只读宿主驱动库。容器内只见一张 A100，Torch 2.13.0+cu130、Triton 3.7.1 的
  `torch.compile` smoke 成功。两道固定题再次得到错误候选 0/5、参考候选 5/5，P0 追加式
  账本门禁改为 ready；P1 仍因固定模型、lane 调用/GPU 上限和 API/GPU 美元硬帽未确认而锁定。
- 避免：标准 NVIDIA runtime 缺失不等于 GPU 容器一定不可用，但任何旁路都必须证明设备
  cgroup 只开放目标 GPU、版本来自冻结锁文件、网络与写权限受限，并重新跑正式正反例，不能
  用通用 CUDA smoke 代替 benchmark 复现。
- 实现提交：`dbf21c5`
- P0 结论、看板状态与管理汇报提交：`ba90ca4`

## 2026-07-31 — Codex 套餐优先的 P1 执行器

- 问题：用户希望优先使用当前 ChatGPT/Codex 套餐，但原控制器只有 fake generator 和单候选
  路径；直接从主仓库调用 Codex 会暴露无关文件，也无法按 lane 恢复调用/GPU 硬帽，P1 完成
  后还可能被误显示为正在运行或自动跨入 P2。
- 解决：新增 `CodexExecGenerator`，用已登录 ChatGPT 的 `codex exec` 启动临时、只读、无项目
  文件的结构化调用，剥离 API/TokenRouter 密钥并保存 JSONL usage；控制器支持上一候选和本 lane
  短反馈，按账本恢复 lane 预算。新增无 P2 入口的 P1 runner，冻结执行每题 1/8/2 轮的三种
  基线，完成后看板明确显示“P1 已完成，P2 待授权”。
- 避免：套餐调用仍是正式模型调用，必须显式固定模型、记录次数与 token usage；限流或认证失败
  时失败关闭，不能在同一实验路线自动切换 TokenRouter。长任务的预算必须从追加式账本恢复，
  不能依赖单进程内存计数。
- 实现提交：`9a4770d`
- 验证：全项目 `131 passed`。

## 2026-07-31 — KernelBench P1 六组真实对照完成

- 问题：第一次真实 LayerNorm 候选使用了非 Triton 扩展，官方静态规则正确拒绝，但解析器先按
  “非零退出且无 compiled 标记”把它误记为环境故障；直接删账或重跑会破坏调用次数和审计链。
- 解决：先补失败回归，再把静态规则拒绝置于通用非零退出分类之前；新增
  `candidate_evaluation_corrected` 追加事件，控制器恢复、lane GPU 预算和看板都优先采用纠正事实，
  旧评分和旧停止事件完整保留。真实候选没有重跑，也没有多消费一次模型调用。
- 结果：在 `gpt-5.6-sol`、A100 GPU4、每 lane 15 次调用/3600 GPU 秒和 API/GPU 各 100 美元
  硬帽下，P1 两题六条固定 Harness 路线全部完成，共 22 个 Kernel 候选、22 个有效评分、17 个
  正确，GPU 计时约 723 秒，账本 API 费用为 0。LayerNorm 的 8 轮通用流程最好 19.86×；
  Matmul+Sigmoid+Sum 的最好结果 1.006×。P2 事件数为 0，阶段停在“P2 待授权”。
- 避免：报告和 UI 必须把“Kernel 候选”与“Harness 版本”分开；P1 的每轮反馈只改下一版 Kernel，
  不能把 P1 成绩写成 Harness 已自迭代。追加式实验账本出现分类 bug 时，只能追加可追溯纠正事件，
  不能覆盖旧事实。看板消耗必须从事实账本计算，不能继续展示计划文件中的初始零值。
- 实现提交：`3fa561b`（解析与追加纠正）、`19e2a08`（实时 lane 看板）、`1fa61f6`（P1 结果汇报）。
- 验证：修复后全项目 `132 passed`；P1 完成审计确认 22 次 generation start、22 次归档、六条 lane
  计划数为 1/8/2、P1 完成事件存在且无任何 P2 执行事件。

## 2026-07-31 — KernelBench P2 六条专用 Harness 谱系完成

- 问题：P2 需要把 Harness 改版与 Kernel 候选严格分开计账，同时保证三条谱系历史隔离、共同
  v001、每 lane 15 次模型调用/3600 GPU 秒硬帽和无 P3 自动入口。最后一条谱系准备第八轮时，
  对话会话中断发生在 `generation_started` 之后、Harness 归档之前；盲目重发会突破冻结调用语义。
- 解决：实现不可覆盖、带父指针的 Harness 档案和 P2 runner；每轮先让优化器只读本谱系短反馈
  生成下一版 Harness，再生成并评分 Kernel，保留历史最好配对。恢复器对已开始但未归档的 Harness
  调用保守计费，追加 `p2_lineage_recovery_stopped` 并冻结该谱系，不重复发起模型调用。
- 结果：六条谱系均完成并停在 P3 门前，共 47 个有效评分、45 个正确候选、约 1661 GPU 秒。
  LayerNorm 三条最好为 19.82×/19.68×/5.70×，未超过 P1 的 19.86×；Matmul+Sigmoid+Sum
  三条最好为 1.85×/4.10×/3.45×，均超过 P1 的 1.006×。五条跑满八轮，最后一条安全冻结
  在七个有效轮次；所有 lane 均未越过硬帽，账本无 P3 事件。
- 避免：长时间实验不能把进程存活等同于事实完成；恢复时必须以追加式账本和不可覆盖产物为准。
  已发起但无产物的调用不能悄悄重放，也不能删掉开始事件来伪装未消费。
- 实现与恢复提交：`1507dc4`、`7cc3421`。
- 验证：P2 定向测试 `4 passed`；最终全项目测试见本次交付提交记录。

## 2026-08-02 — KernelBench P2b 大范围 Harness 搜索执行器

- 问题：P2 的 Harness 优化器主要看到编译、正确性和最终速度，容易把后续轮次收缩为
  `num_warps`/`num_stages` 等局部微调；同时服务器没有 `ncu`，硬件计数器又是管理员专用，
  不能把理论 Occupancy 或猜测的带宽冒充实测证据。
- 解决：新增完全独立的 P2b 计划、策略、执行器和看板。两题各四条不同路线，结构化 Harness
  真正选择代码起点、任务内 Skill、工具、记忆视图、工作流和 Kernel 主结构；每版 Harness
  只生成一个 Kernel，每轮固定查看当前/上一轮/历史最好/冻结起点分数，无 2% 可信提升必须
  换搜索维度，并保留第六轮强制重启和至少四轮结构探索。Tier A profiler 使用 `nsys`、干净
  Triton cache 与 `cuobjdump`，只给模型公开脱敏摘要；缺失的硬件计数器显式记为空。
- 结果：离线 8×8 闭环精确覆盖 64 个 Kernel、56 次 Harness 更新和 120 次模型调用状态，恢复
  后零新增调用；GPU4 对冻结正确 LayerNorm 候选的端到端 profiler 预检得到 3 Kernel、30
  launch、48 registers/thread、32B shared 和 62.5% 静态理论 Occupancy，原始 trace 私有归档。
  正式 P2b 产物根和 8 个历史起点已冻结，但本提交时真实模型/评分轮次仍为零。
- 避免：Profiler 能力必须分层，理论值和实测值使用不同字段；分数不涨时不仅改提示词，还要
  机械检查工具、Skill、记忆、起点、假设或主结构是否变化。P2b 账本、硬帽和 P3 门禁不得复用
  或改写旧 P1/P2 事实。
- 实现提交：`a57f73a`。
- 验证：P2b 定向测试 `14 passed`；全项目 `153 passed`。

## 2026-08-02 — P2b 错误候选看板恢复

- 问题：正式 P2b 的 LayerNorm `architecture_reset` v006 编译成功但正确性失败，轮次按合同记录
  `profile: null`；看板把该字段无条件当作字典调用 `.get()`，导致评分事实已落盘后 runner 仍因
  `AttributeError` 退出。
- 解决：先用真实事件形态补回归测试，再让看板只在 ProfileSummary 为字典时读取分析级别；错误
  候选显示占位符并保留其反馈，恢复器可跳过已完成 v006、从同一 lane 的 v007 继续。
- 避免：派生看板不能成为实验执行器的单点故障；所有按合同可空的评分字段都必须用显式类型门禁
  渲染，且回归测试要覆盖“有效评分但没有 profiler”的正确性失败路径。
- 实现提交：`d8a1019`。
- 验证：`tests/test_p2b_runner.py` 4 项通过，其中新增空 ProfileSummary 回归用例。

## 2026-08-02 — P2b Harness 逐轮分数曲线

- 问题：追加账本保存了每轮评分，但原看板只显示 lane 最好分和最近变化，无法直接证明 Harness
  v001–v008 的分数轨迹；评分完成后才发生 Profiler/进程中断的候选没有 `p2b_round_completed`，
  还会从普通轮次视图中消失。
- 解决：看板从 `p2b_candidate_generated`、`candidate_evaluated` 和 `p2b_round_completed` 联合重建
  每条 lane 的完整评分证据，内嵌 SVG 折线和逐点精确表格。冻结起点用虚线，正确性失败用红叉且
  折线断开，已评分但未封存的尝试用橙点；每点绑定 Harness 版本、Kernel ID、speedup 和相对起点。
- 避免：研究看板不能只显示 best-so-far，也不能把“轮次未封存”等同于“分数不存在”；任何曲线
  必须可回溯到追加事实，失败点不能在绘图时被过滤成一条虚假的连续上升线。
- 实现提交：`831d960`。
- 验证：`tests/test_p2b_runner.py` 4 项通过；真实账本只读预览确认中断候选 `19.273084×`、错误断点
  和后续恢复分数均出现在曲线及明细表中。

## 2026-08-02 — SHE-1 系统级 Harness 自进化方案

- 问题：P2/P2b 把大部分 Harness 变化压缩成 Prompt/JSON policy，controller、角色拓扑、记忆、
  搜索算子、scheduler 和 recovery 仍固定；同时 P1 的八轮只用 8 次 Kernel 调用，P2 的八轮通常
  另用 7 次 Harness 调用，旧最终最好分不能作为等总成本因果比较。安全审查还发现旧 adapter
  解析候选可控的合并 stdout，并复用可写 cache，不足以承载更强的对抗性系统搜索。
- 解决：设计独立 `SHE-1`，把完整可执行 Bundle 作为 genotype，同时把 scorer、预算、ledger、
  canonical 和 champion authority 永久外置。正式矩阵使用 Prompt×System 的互斥 2×2 四臂、
  固定 call/Token/GPU AUC、多 seed replay 和同期 6-call attribution control；Bundle 全文件哈希、
  分层预算、失败保守结算、无正确 seed fail-closed 及 trusted result side channel 均成为硬合同。
- 避免：系统搜索空间扩大时必须同步扩大信任边界审计；candidate stdout、共享 cache 或旧签名结果
  不能成为正式事实。不同 horizon 的 AUC 不得直接做确认性归因，2% 只能称预注册 operational
  margin，不能冒充统计置信区间。设计、实现和正式运行必须分别授权。
- 方案提交：`43902ef`。
- 验证：P1/P2 账本仍为 548 行、SHA-256
  `2b1048012857c50a487830da5c380a04c7d19954996dc7538b70ef7686c120c0`；定向回归 `21 passed`；
  未修改代码、未调用付费模型、未连接 GPU 或启动 SHE-1。

## 2026-08-02 — SHE-1 声明式 IR 与快照门禁修订

- 问题：首版方案允许模型生成 sandbox Python Harness plugin，造成多重语义源和额外逃逸面；旧
  `specialist_v001.md` 又写死 P2 八轮，不能逐字作为 SHE-1 的 16/8-call 静态基线。P2b 虽已
  写入 phase completed，但 PID、单个 lane completion 和旧 global GPU 检查都不足以证明可供
  下游消费，后者还漏掉 unmatched profile reservation。
- 解决：把 v1 收紧为单一 `harness_ir.json` + 冻结 TrustedOperatorRegistry/SkillRegistry 的
  声明式系统搜索，Reviewer 决策后才确定性 canonicalize/compile/seal；新增统一
  ExperimentContract/SeedManifest 和一等 proposal/review/evaluation/allocation 制品。`C0` 使用
  新冻结、跨题同字节且通过 `CurrentCellHorizon` 参数化的 specialist `P0`，只做 16/8 个 Kernel
  call。P2b source verifier 固定按 runner→ledger 双锁、精确事件链与候选 hash 关联、逐 lane
  reservation 重放、Task subtotal 和 global cap 复算后才允许封存快照。
- 避免：声明式 genotype 只能有一个语义源；registry 固定实现而非可变 Skill 文本。不能把
  phase-completed、陈旧 PID、dashboard 或旧近似预算函数当作冻结证明，也不能用事后截断
  `C0` 冒充 fixed-Kernel sham-planner 实验。
- 方案修订提交：`fd1912a`。
- 验证：三轮独立只读复核均无阻断；全项目 `154 passed`；P1/P2 账本仍为 548 行且 SHA-256 为
  `2b1048012857c50a487830da5c380a04c7d19954996dc7538b70ef7686c120c0`。未修改实现代码、旧
  P1/P2/P2b 账本或 runner，未调用模型/GPU，也未启动 SHE-1。

## 2026-08-02 — SHE-1 对抗性合同定稿

- 问题：系统级搜索仍可能借候选 stdout、跨尝试 cache、状态化 correctness/timing 或含糊的
  capability/账本锚点权限伪造正式事实；champion、reproduction owner、失败分母和成本 gate 也需
  单义 reducer 才能复算。
- 解决：冻结 correctness-bound `CandidateInvocationABI-v1`、12 个预算内 canary、prospective
  canonical/champion 规则、Kernel opportunity 分母和分离 reducer；Broker 成为唯一 grant
  issuer/holder/consumer/dispatcher，CheckpointAuthority 必须独立逐条重放 canonical ledger 后
  才能签名锚点。
- 避免：controller 不持有可调用 service 的 grant，签名服务也不能只签 EventWriter 声称的 head；
  每个正式副作用和冠军 token 都必须由独立权限域根据冻结事实机械产生。
- 方案提交：`a802aa8`。
- 验证：定向回归 `39 passed`；额外全量检查按用户要求及时收敛，在中止前 `48 passed` 且无失败；
  三路独立只读复核均判定无 Gate A 阻断。P1/P2 账本仍为 548 行且 SHA-256 为
  `2b1048012857c50a487830da5c380a04c7d19954996dc7538b70ef7686c120c0`；未修改实现代码、调用模型或 GPU。

## 2026-08-02 — HB-GEN-1 跨 Benchmark 泛化与持续学习执行层

- 问题：已有 P1/P2/P2b 只能说明固定 KernelBench instance 上的专化，不能区分一次性
  task-conditioned Harness、通用 Builder、跨题经验与持续学习；旧评分路径也不足以安全承载
  跨 Kernel、LLVM action sequence 和真实仓库 patch 的统一系统级搜索。
- 解决：实现 3 benchmark × 8 unseen instance 的 `A/B0/B*/B-online` 首次见面流。每个 instance
  必须先封存四臂，经验才可进入下一题；Builder checkpoint 可改变后续题的角色图、记忆、工具、
  workflow、父代、scheduler/recovery 和进化规则，trusted operator/scorer/budget 在本轮冻结。
  新增内容寻址 Experience Bank、严格 Harness decision compiler、一次性模型 capability、哈希链
  ledger/独立 head 重放、逐 cell 预算和 KernelBenchX/CompilerGym/SWE-Perf 三种 evaluator 边界。
- 避免：正式 test 不能同时作为当前题的训练反馈；同题更新后复跑只算 diagnostic。开源搜索规则
  必须区分 Harness 证据和 solution-only 调度原语，未实现的规则只能 shadow-log。CompilerGym
  aggregate validation 会混入 reference 也失败的 sanitizer，且 `rijndael`/`sha` 缺少可信语义门，
  因此只运行 source/index 哈希绑定的 ordinary validator allowlist，并在正式计分前换成
  `stringsearch2`/`blowfish`。
- 实现提交：`2127a46`。
- 验证：HB-GEN-1 定向测试 `152 passed`；全项目 `306 passed`；compileall、diff check 与敏感值
  精确扫描通过。尚未越过 runtime/meta-train/evaluator canary，正式搜索分数仍为零。

## 2026-08-02 — KernelBenchX 单 GPU namespace 逻辑编号修复

- 问题：首个 reference canary 在强制 bubblewrap 内报告没有 CUDA GPU。隔离层只挂载物理
  `/dev/nvidia4`，却仍把宿主 ordinal `4` 传给 `CUDA_VISIBLE_DEVICES` 和官方 pipeline；单设备
  namespace 会把这张卡重编号为逻辑 GPU0，因此设置 `4` 反而隐藏了唯一设备。
- 解决：宿主侧仍只选择并挂载物理 GPU4，worker 环境和官方 pipeline 参数固定使用逻辑 `0`；
  新增红测同时锁住 `/dev/nvidia4` 存在、`/dev/nvidia0` 不得挂载和两处逻辑编号。旧 canary 失败
  与预算预留保留，修复后必须以新代码快照和新 staging root 重跑，不能覆盖或退款。
- 避免：设备节点的宿主编号与隔离 namespace 的逻辑编号必须分字段处理；任何新 GPU 隔离实现都
  先跑“只挂一张非零 ordinal GPU、容器内必须是 device 0”的真实 runtime canary。
- 实现提交：`1443722`。
- 验证：KernelBenchX 定向回归 `34 passed`；全项目 `307 passed`。

## 2026-08-02 — KernelBenchX 隔离工具链路径修复

- 问题：r2 reference canary 的 call/execution 均 100% 通过，但 performance 阶段没有 timing row。
  私有日志显示 Triton 找不到 C compiler：隔离层只读挂载 `/usr`，而 `/usr/bin/gcc` 是指向未挂载
  `/etc/alternatives` 的软链。
- 解决：不扩大 `/etc` 暴露面，worker 明确设置 `CC=/usr/bin/x86_64-linux-gnu-gcc-12` 和对应
  `CXX` 版本化绝对路径；新增红测拒绝 `/etc/alternatives` 挂载依赖。旧 r2 失败仍按完整 seat
  记账，后续只允许在新 revision/staging root 重跑。
- 避免：安全沙箱中的 PATH 可见不等于工具实际可执行；runtime canary 必须在同一 namespace 中
  完成真实编译和链接，而不只运行 `which gcc`。
- 实现提交：`539a4ad`。
- 验证：精确 bubblewrap C 编译/链接探针通过；KernelBenchX 定向回归 `35 passed`；全项目
  `308 passed`。

## 2026-08-02 — KernelBenchX Python headers 内容绑定

- 问题：r3 reference canary 已能完成 call/execution，但 Triton 的 performance helper 编译
  `cuda_utils.c` 时找不到 `Python.h`；宿主 `/usr/include/python3.10` 只有无关的四个文件。
- 解决：从既有 Python 3.10 dev artifact 复制 163 个 regular headers 到独立只读 runtime root，
  以真正 NUL 域分隔的路径、类型和逐文件内容计算完整树 SHA-256 `26aefabf...ac71cd`。worker 仅把该 snapshot
  ro-bind 到 `/opt/hb-python-include` 并设置 `CPATH`；启动前重新计算全树哈希，symlink、special
  file、超限大小或任意内容漂移都 fail closed。
- 避免：GPU 可见和 C compiler 可运行仍不足以证明 Triton runtime 完整；正式 reference 前应在
  同一 namespace 运行会触发 `cuda_utils` 编译的 `triton.testing.do_bench` 微型探针。
- 实现提交：`728cf7b`。
- 验证：KernelBenchX 定向回归 `36 passed`；全项目 `309 passed`。

- 后续校正：首次用 shell 独立计算 manifest 时错误地把 `\0` 当成两个可见字符，预检因此在任何
  evaluator transaction 前拒绝了 r4。生产常量已改为代码独立重放得到的 `26aefabf...ac71cd`，
  并新增固定 test vector `3f2a3ad6...32e472` 锁定真正 NUL 分隔语义；不改 header 内容。校正提交：
  `8e2c6ec`；全项目 `310 passed`。

## 2026-08-02 — KernelBenchX multiarch Python header 闭环

- 问题：在正式 reference 前执行的 `triton.testing.do_bench` 微探针已找到 `Python.h`，但该头
  文件进一步包含 `x86_64-linux-gnu/python3.10/pyconfig.h`；v1 快照只复制了单一子目录。
- 解决：v2 冻结整个 include tree，共 164 个 regular files，树 SHA-256 为
  `0487df20...fcaa67`。`CPATH` 同时包含 `python3.10` 子目录和 include 根；启动前除全树哈希外，
  机械要求 `Python.h` 与 multiarch `pyconfig.h` 都是 regular file。
- 避免：语言开发头文件往往有 multiarch 二级依赖；runtime snapshot 应从完整 include root 构建，
  并用会真实加载扩展的微探针验证，不能只检查第一层 include。
- 实现提交：`05c6ba9`。
- 验证：KernelBenchX 定向回归 `38 passed`；全项目 `311 passed`。

## 2026-08-02 — KernelBenchX 正式出分前的任务替换

- 问题：r4 的第七个 reference `Activation/gelu_bf16.py` 已通过 call、correctness 与 timing，
  但当前官方 perf serializer 写出 `[4096]`，冻结 A100 golden 写成 `[[4096]]`；可信 parser 无法
  精确绑定同一 input，故按 `environment_invalid` 封存。正式搜索分数仍为零。
- 解决：不放宽 parser、不覆盖或退款失败 seat。固定 KernelBenchX 与 TritonBench 两个 commit，
  从失败题 selection digest 后对全池顺序扫描，机械排除 perf/golden schema 不一致项和
  TritonBench 同 basename 项，首个合格替换为
  `Fusion/fused_relu_max_pool2d_conv2d.py`。扫描链、source/perf/golden SHA 和替换理由写入独立
  audit artifact，并纳入 staging plan 的 source hash。
- 避免：held-out task digest 只能排序已经选中的题，不能冒充全池资格规则；任何 canary 前换题
  都要同时冻结全池、排除条件、外部重名审计 commit 和被跳过的前驱，且不得读取替代题性能。
- 实现提交：`1c7e2b6`。
- 验证：KernelBenchX/prepare/stream/learning 定向回归 `40 passed`；全项目 `312 passed`；三个
  source digest、TritonBench commit、JSON 和 compileall 均独立复核。新任务尚需在新 staging
  revision 通过 8 reference + 3 adversarial canary，正式 24 题搜索仍为零。

## 2026-08-02 — HB-GEN-1 KernelBench meta-train 恢复门禁

- 问题：正式 24 题需要先冻结 B* 的 KernelBench Experience Bank，但原仓库只有 pending manifest，
  没有六题真实执行、八源蒸馏、预算重放或 B* heldout 排除的可执行门禁；直接复用旧 KernelBench
  adapter 又会让候选 stdout 和共享 cache 进入控制面。
- 解决：新增六个互相隔离的 B0 meta-train cell，每题固定八轮 planner+solution 与八个评分机会；
  两条历史和六条新轨迹全部内容寻址封存后，才按源各做一次严格 distillation，并给 B*/B-online
  冻结同一 checkpoint。所有调用/评分走 hash-chained OperationJournal、独立 head anchor 与逐 cell
  entitlement；Experience Record 全文和运行时 memory 都机械拒绝 formal heldout ID。
- 避免：训练轨迹也会污染后续 Builder，不能因其不是正式 test 就降低 evaluator 信任边界；旧
  stdout/shared-cache scorer 未替换前，真实 meta-train CLI 必须 fail closed，不能用“只是训练”
  作为静默放宽理由。
- 实现提交：`654449d`、`ba1901c`。
- 验证：meta-train fake 端到端 `5 passed`，精确覆盖 104 calls/48 evaluator transaction；全项目
  `316 passed`。未调用付费模型或 GPU。

## 2026-08-02 — HB-GEN-1 evaluator 中断恢复单义化

- 问题：cell runner 在 evaluator 已完成但 round 尚未封存时会再次调用 terminal operation；若
  evaluator started 后中断且没有结果，恢复器又会用同一 transaction 重跑，既可能重复副作用，
  也会让中断样本被静默替换。
- 解决：在 terminal event 前原子保存 canonical `controller-result.json`，逐字段绑定 operation、
  cell、instance、version、candidate SHA、usage 与 evidence，再由 journal 绑定 result SHA。恢复只
  允许两条机械路径：completed 读取已绑定 artifact；started+artifact 补写 terminal。started 且
  无 artifact 永久报 abandoned，不重试、不退款。
- 避免：不能把“同一个 operation ID”误当成“同一次副作用”；任何可复用评测结果都必须先有
  controller-owned、内容寻址且能独立校验的事实 artifact。
- 实现提交：`da50d85`。
- 验证：三个 evaluator/round-seal 中断回归 `3 passed`；全项目 `320 passed`；未调用模型、GPU
  或外部 evaluator。

## 2026-08-02 — SWE-Perf 离线 wrapper 信任边界

- 问题：审计得到的八个 SWE-Perf digest 只是上游依赖/仓库基础镜像，不包含 HB-GEN-1 约定的
  root supervisor、私有结果通道或内容绑定 labels；直接交给现有 adapter 会把“环境镜像”误当
  “可信 evaluator 镜像”。
- 解决：新增严格八题 source lock 和不调用 Docker/网络的 build-context 生成器；wrapper 叠加
  `/opt/hb-sweperf/bin/evaluate-stage`，并绑定 task manifest、supervisor bundle、upstream ref、
  instance/task hash 与 10 CPU/32 GiB/512 PID envelope。运行时只允许 exact `git apply`，丢弃
  candidate stdout，correctness receipt 绑定 request/patch/state/evidence，任何残留 worker 即使成功
  kill 也使 stage fail closed。
- 避免：基础镜像 digest、wrapper RepoDigest 与 task manifest digest 必须分字段冻结；只有 source
  lock、离线构建 receipt、逐 label inspect 和 reference/对抗 canary 全部闭合，才能解除 SWE-Perf
  family blocker。缺失镜像不得自动 pull，执行失败不得用 mutable tag 或 fuzzy patch 恢复。
- 实现提交：`caf746e`。
- 验证：新增 wrapper/既有 SWE-Perf 定向测试 `61 passed`；rebase 最新 `origin/main` 后全项目
  `334 passed`。没有拉取或构建镜像，没有运行 Docker/evaluator，也没有调用模型、GPU 或付费服务。

## 2026-08-02 — SWE-Perf source-lock 公开投影与阻断证明

- 问题：冻结八题的 Parquet 同时含公开任务描述与 gold patch/test patch/head commit；直接加载整行
  会污染 heldout 边界。与此同时，基础镜像尚无本地 RepoDigest 证明，现有 wrapper 又让候选 worker
  写测试 JSON 后由 root supervisor 读取，不能据此铸造可信 source lock。
- 解决：新增纯离线 preparer，只向 Arrow 请求七个公开列，复核 detached evaluator/dataset commit、
  Parquet SHA、PilotManifest task hash 与八题原始顺序，并从公开 `test_functions` key 机械派生
  allowed paths。产物是内容寻址、幂等的 `blocked` report；代码路径中不存在 runnable lock 输出。
- 避免：数据集文件整体已被哈希固定，不代表可以把整行读入内存；source identity、gold-column
  projection、镜像 RepoDigest 和结果通道 provenance 必须作为四个独立门禁。
- 实现提交：`de9b378`。
- 验证：source-lock 红测 `5 passed`，SWE-Perf 全组定向 `62 passed`；真实 pinned checkout 离线得到
  8 个 public task binding，仅保留 `local_repo_digest_unverified` 与
  `worker_authored_report_untrusted` 两个 blocker。未调用 Docker、网络、模型、evaluator 或 GPU。

## 2026-08-02 — SWE-Perf 同进程结果伪造红测与硬关闭

- 问题：进一步红测证明 uid-65534 的同一 pytest 进程既执行任意 candidate Python，又写 test
  outcome、pytest call duration 和退出码；候选可直接伪造全 passed 与任意短 duration。root 在退出后
  读取 0600 JSON、绑定 nonce/HMAC 或监控外层进程，都无法证明断言真实执行，也无法独立得到冻结的
  per-test call-duration 信号。
- 解决：新增 canonical、内容寻址的 result-channel capability verdict，明确区分 worker 可控信号与
  root 可观测信号，并把 blocker 收紧为 `in_process_candidate_outcome_unattestable`。production
  supervisor 现在在任何 worker spawn 前固定 fail closed；离线 source-lock report 内嵌同一 verdict，
  wrapper bundle 也绑定 gate 源码 hash。
- 避免：文件 ownership、私有 FD、HMAC、退出码和外层 wall clock 都不是同地址空间 Python 的
  correctness attestation。继续 SWE-Perf 必须另行批准 task-specific out-of-process oracle 或等价新
  scorer；不得把通用 RPC 假定为复杂 Python object/test 语义的等价替代。
- 实现提交：`1fa5f2f`。
- 验证：伪造路径先红后绿；SWE-Perf 定向 `64 passed`，rebase 最新 main 后全项目 `427 passed`，compileall 与
  `git diff --check` 通过。未运行 Docker、网络、模型、正式 evaluator 或 GPU。

## 2026-08-02 — HB-GEN-1 KernelBench meta evaluator 信任边界

- 问题：旧 KernelBench adapter 从候选可写的合并 stdout 正则提取 correctness/timing，并跨候选复用
  cache；更根本的是 pinned `run_and_check.py` 会在掌握 correctness 与 CUDA timer 的同一进程内
  `exec/import ModelNew`。只把 stdout 包成 JSON 仍允许候选 monkeypatch scorer，不能成为可信事实。
- 解决：新增固定六题 commit/source SHA 的严格 adapter/backend；每 attempt 使用独立 candidate、
  scratch/cache 和 mode-0600 私有结果，结果逐字绑定一次性 nonce、task、candidate、protocol 与 scorer
  SHA，并要求 5/5 correctness 和 100/100 correctness-bound timing。candidate stdout/stderr 完全不参与
  状态判定，环境故障只接受 out-of-band health 字段。bubblewrap namespace 复用单物理 GPU→逻辑 0、
  禁网、非 root、只读源码/系统和内容哈希 Python header 边界；`MetaTrainTask` 已接入该 backend。
- 避免：namespace 与结果 Schema 不是 CandidateInvocationABI 本身。当前官方 scorer 仍不满足进程/权限
  分离，所以生产 supervisor 在加载 candidate/GPU 前固定以 78 fail closed；staging 又没有独立
  `canary:kernelbench-meta` entitlement，禁止借六个正式 meta-train cell 的 seat。
- 实现提交：`805166e`。
- 验证：安全边界与任务绑定定向测试 `13 passed`，另有 subprocess fake-supervisor 私有通道 E2E；CLI 只读报告
  ABI、canary entitlement 与两份历史轨迹三个 blocker，started model/evaluator 均为 0。未调用模型、
  GPU 或外部 evaluator；全项目 `333 passed`。

## 2026-08-02 — HB-GEN-1 历史 all-lanes 轨迹导入

- 问题：两道历史 KernelBench meta-train 源只有 P1/P2/P2b 追加账本与分散 artifact；
  手工整理会引入 winner selection、漏掉失败/中断轮，或泄露 candidate/raw/private 内容。
- 解决：新增纯离线 importer，按 P1→P2→P2b ledger 原序为每题生成一个 all-lanes
  aggregate。它在 writer/ledger 锁内双读四个冻结源 SHA，验证候选、Harness/policy parent、
  profile 与全部 terminal provenance；任一证明不成立时只写 content-addressed blocked prepare。
- 避免：历史经验也必须有机械 selection policy 和公开字段白名单；不能用“已完成实验”
  代替源 hash、锁、artifact parent 与失败事实的重放证明。
- 实现提交：`8954835`。
- 验证：rebase `origin/main@938d558` 后定向 `22 passed`、全项目 `351 passed`；真实冻结源
  离线 prepare 得到 LayerNorm `f1417f0...6b2d` 与 Matmul `f6a6900...fc00`，新模型、
  evaluator、GPU 和网络调用均为 0。

## 2026-08-02 — HB-GEN-1 模型路由 canary 版本化恢复

- 问题：旧 runtime canary 虽已通过，但绑定过时 code revision，summary 又没有 staging/source/prompt
  的完整 RunSignature；直接复用会把旧路由事实冒充当前代码事实，而忽略旧调用又会重置两次专用
  entitlement。
- 解决：新增内容寻址 model-route segment，绑定 clean full revision、staging/source/prompt hash、
  `gpt-5.6-sol/high/codex-cli-0.144.6/codex_chatgpt` 和精确 `HarnessDecision`。旧 canary 的独立
  journal/head/summary 只生成 `reusable=false` 收据并扣除一次调用；新 segment 共享恢复账本，
  completed 只重放，started 无 artifact 永久 abandoned。CLI 默认只 preflight，必须显式
  `--execute` 才能进入 transport。
- 避免：模型 route smoke 也必须按 RunSignature 切段；代码、prompt 或 staging 任一变化都不能
  复用旧通过事实，但历史失败/通过调用仍须占原硬帽。
- 实现提交：`84b2dda`。
- 验证：fake 定向回归 `38 passed`、全项目 `417 passed`；未运行 Codex、未读取密钥、未调用
  evaluator/GPU，正式搜索分数仍为零。

## 2026-08-02 — HB-GEN-1 CandidateInvocationABI-v1 离线核心

- 问题：nonce-bound 私有 JSON 只修复结果通道，不能限制 arbitrary Python candidate，也不能防止
  “前 5 次 correctness 正确、随后 100 次 timing 返回错误快路径”。pinned 官方 scorer 的同进程
  `exec/import ModelNew` 仍不能直接用于 meta-train。
- 解决：新增 canonical Restricted Torch/Triton policy，由 solution codec 与生产 supervisor 对同一
  candidate bytes 独立验证；绑定 policy SHA 到 protocol/argv/private evidence。可信 invocation loop
  在 import 前捕获 timer/synchronize/comparison primitives，固定 compile→5→100，给全部 invocation
  新鲜 input commitment，并对每个 measured output 和 input mutation 逐次核验；candidate teardown、
  process group 与 GPU context 未静默时结果 fail closed。对抗测试覆盖 stdout/control-line 伪造、
  result/path/FD、反射、后台 child、Torch save/load、global/module monkeypatch 和 stateful timing cheat。
- 避免：AST policy 不是 GPU 隔离或真实性能证据。当前只有 fake runtime 协议验证，真实 Torch/CUDA
  worker 尚未接入且尚未 canary，故 `KERNELBENCH_META_PRODUCTION_READY` 继续为 `False`，blocker 是
  `kernelbench_meta_runtime_and_canary_pending`；capability report 必须分别写明 trusted loop 已实现、
  production runtime 未实现，不得借正式 meta seat 或回退 legacy stdout/shared-cache scorer。
- 实现提交：`3d0c79d`。
- 验证：Candidate ABI/Policy 单测 `51 passed`，与 meta adapter/supervisor/meta-train/isolation 及新历史
  importer 的整组定向回归通过；rebase `origin/main@465e0c5` 后全项目 `403 passed`。没有调用模型、
  GPU、网络或远端 evaluator。拟议 real canary 预算为 10 transaction、
  每个最多 600 GPU 独占秒（总计 6,000 秒）；这只是 production runtime 完成后的 canary 建议，尚未
  修改正式 plan 或消费。

## 2026-08-02 — KernelBenchX reference canary 候选合同

- 问题：`conv2d_w8a8` canary 把 SHA 等于冻结 task source 的整份 dataset 文件直接当成 reference
  candidate；该文件含 146 个 `#` 分隔符和内嵌 tests，正式 `KernelBenchXSolutionCodec` 明确拒绝，
  因而 canary 没有覆盖真实 solution ABI。公开 `compile_failed` artifact 又不含足以判定底层异常的
  私有 worker stderr，不能从状态名猜测 CUDA/Python 根因。
- 解决：新增完整 task SHA 绑定的 reference-canary 生成器，只机械抽取分隔符前实现段，再走同一
  solution codec；纯离线 prepare CLI 把 candidate 与 manifest 分别内容寻址、不可覆盖。preflight
  入口只接受 manifest，复核 candidate hash/codec/task binding，并在创建 GPU worker 前拒绝整份
  task、手工 candidate、symlink、非 UTF-8 或超限输入。stdout/private-result 信任边界没有改变。
- 避免：task specification、oracle implementation 与 formal candidate 必须是三个不同 identity；
  reference canary 也不能绕过 model candidate ABI。缺少私有运行证据时保留 blocker，不能用一次
  离线合同修复宣称已修好 GPU 失败。
- 实现提交：`0112a00`、`fa483e9`。
- 验证：先得到 2 条预期红测，再转为定向 `13 passed`、全项目 `419 passed`；真实 pinned checkout
  纯离线生成 `conv2d_w8a8` 实现段 `20c60c5...a2d1` 和 manifest `46fc461...f83c4`。未调用 GPU、
  SSH、远端、模型或网络，未修改预算，也未重跑 canary。

## 2026-08-02 — HB-GEN-1 formal prequential 控制面

- 问题：已有 cell runner、PrequentialState 和 ContinualUpdater，但缺少把冻结 24 题 stream、每题
  arm_order、四臂封存与 test-then-learn 串成一个可恢复正式状态机的控制层；直接手工编排会让
  B-online 在当前题提前学习、让 B* 漂移，或在中断后重复模型/评分副作用。
- 解决：新增 staging-bound provider protocol 与 formal runner。每臂生成 immutable 八轮 receipt，
  四臂齐全后才封存公开 trajectory 并恰好蒸馏一次；Experience Bank/Builder checkpoint 逐代绑定
  parent SHA，在线更新只进入下一 stream item。整题 receipt 使同 instance 再跑严格 replay-only；
  started+canonical model artifact 可补 terminal，started 无 artifact 永久 abandoned。`B*` cell 名中的
  `*` 只允许在 cell authority ID，实际 operation ID 使用内容哈希前缀，避免放宽操作路径字符集。
- 避免：first-encounter 成绩、training diagnostic 与在线学习必须是三个不同 reducer；外层恢复不能
  仅依赖“文件存在”，必须逐层复核 staging、round event、artifact SHA、bank/checkpoint parent 和
  operation terminal。独立 suite provider 必须绑定 staging SHA，formal CLI 不应猜测或自动构造
  尚未通过 canary 的 evaluator。
- 实现提交：`17c6414`。
- 验证：formal fake 端到端覆盖四臂顺序、跨题前向经验、B* 冻结、同题零调用重放、崩溃恢复与
  精确模型/evaluator 预算；rebase `origin/main@0cee479` 后全项目 `425 passed`。未调用模型、GPU、
  Docker、SSH、网络或真实 evaluator。

## 2026-08-02 — HB-GEN-1 KernelBench meta production runtime

- 问题：离线 CandidateInvocationABI 已能证明 5+100 correctness-bound 调用顺序，但正式 supervisor
  没有真实 Torch/CUDA worker、候选不可访问的结果通道和可执行的单 GPU 隔离链，不能进入 GPU canary。
- 解决：新增逐题绑定 Restricted Torch/Triton 的 production worker；在 candidate 前捕获 trusted
  primitives，以 supervisor 私有 HMAC nonce 生成一致权重和每次新鲜输入，逐次封存 output/input 与
  reference state。pre/candidate/post 三个 bubblewrap phase 均禁网、只读 root、独立 scratch/cache、
  单 GPU；结果仅走 canonical fd3 且 runtime import 前 CLOEXEC，outer evidence 绑定 scorer/protocol/
  task/candidate/schedule/input-schedule。malformed evidence 只成为 candidate failure，stdout 永不裁决。
- 避免：实现 production runtime 不等于获得执行权。capability 继续固定 `execution_ready=false` 和
  `kernelbench_meta_canary_pending`；canary/formal 都需 worker 不可见的内容寻址授权 receipt，正式
  receipt 还需绑定通过后的 10-seat/6,000 GPU 秒 canary evidence。没有修改正式预算，也没有调用
  GPU、模型、网络或远程 evaluator。
- 实现提交：`4809b17`。
- 验证：最终实现快照全项目 `431 passed`；随后 rebase `origin/main@04a3834`，production runtime、
  adapter/isolation/supervisor 与上游 KernelBenchX reference 交叉定向 `79 passed`。首次全测的既有
  并发配额测试出现一次时序抖动（其余 412 passed），该项单独复跑通过，后续完整重跑全绿。

## 2026-08-02 — KernelBench meta authorization receipt adapter binding

- 问题：production supervisor 已要求 canary/formal 外置授权 receipt，但 outer adapter 不接受或传递
  receipt；因此任何正常 `prepare_attempt` 都必然在 GPU 前被拒绝，未来只能改代码再 canary，破坏冻结
  revision 的授权闭环。
- 解决：`KernelBenchMetaAdapter` 构造时强制绑定 controller-owned mode-0600 内容寻址 receipt；
  `MetaSupervisorCommand` 保存 canonical path/SHA，并只向 trusted supervisor 追加
  `--authorization-receipt`。每次 prepare 重新核验内容，receipt 与 repository/attempt worker state
  必须分离，path/SHA 不进入 candidate argv 或 environment。真实 supervisor contract 的 canary/formal
  两种 receipt 均完成无 worker、无 GPU 的重建验证。
- 避免：授权能力必须在将要 canary 的同一代码 revision 内已有完整消费路径；不能依赖 canary 后翻常量
  或再补 argv。缺失、symlink、错误权限、非内容寻址、漂移或 worker-visible receipt 一律 fail closed。
- 实现提交：`09f32ca`。
- 验证：adapter/supervisor 定向 `22 passed`；production runtime、KernelBenchX reference 与 formal runner
  交叉定向 `89 passed`。未调用 GPU、模型、网络或远程 evaluator，正式预算未改变。

## 2026-08-02 — HB-GEN-1 formal suite-provider composition

- 问题：formal runner 已要求 staging-bound provider factory，但没有 production composition authority；
  手工注入 adapter 会绕过 suite canary、task/source binding 或 SWE-Perf 的可信结果通道 blocker。
- 解决：新增 fail-closed 组合器与纯离线 preflight。每个 suite gate 独立复核 canary result、operation
  ledger、外置 trusted-head anchor、terminal artifact/resource projection 和 staging/manifest/task hash；
  单个通过的 KernelBenchX/CompilerGym provider 只能用于离线 binding 检查，三-suite factory 必须全部
  通过。CompilerGym 已消费的旧 canary 只对精确 36-event segment 做 component rebind：adapter bytes、
  codec/backend canonical AST 与旧/新 cell-ID 交集都必须不变，且由当前 verifier 独立重放；证据不可覆盖、
  内容寻址。SWE-Perf 只有完整匹配当前 capability verdict 才识别为已知 blocker，绝不生成 fake provider。
- 避免：旧 canary 事实不能按文件名或相邻 summary 复用；必须同时绑定独立 anchor 与 exact terminal
  projection。suite 局部 ready 也不等于 campaign authority，blocked preflight 不能进入正式 runner。
- 实现提交：`a454fc1`、`84c3332`。
- 验证：provider 定向回归 `8 passed`、跨 formal/三 evaluator 合同 `61 passed`、全项目
  `452 passed`。未调用模型、evaluator、Docker、SSH、网络或 GPU；正式 24 题搜索仍为零，
  SWE-Perf 与其余 suite gate 继续阻断 factory。

## 2026-08-02 — KernelBench meta 十席 canary 控制器

- 问题：production runtime 已能接收外置 authorization receipt，但六个正例没有统一的正式 codec
  构造路径，四个攻击例混淆了 GPU 前静态拒绝与动态 evaluator 失败；也没有逐席预算、永久 abandoned
  恢复和独立 ledger/head 复算，因而不能安全消费拟议 canary 额度。
- 解决：新增内容寻址十席 plan。六个完整 task SHA 只提取 Model、规范化为 ModelNew，并重新通过逐题
  restricted policy/正式 codec；补入只对对应题开放的 cumsum/SDPA/HardSwish/GELU-GAP tensor 能力。
  执行顺序先静态拒绝与早失败、后大输入正例。controller 在副作用前 reserve/start，结果对象和私有
  evidence 只以 hash 绑定；started 无 artifact 永不重发。独立 verifier 不信 controller projector，重放
  append-only journal 与外置 anchor、逐项核对十个 terminal artifact，只铸造 canary evidence，不自动
  铸造 formal authority。
- 避免：静态 `print/open` 红测不能冒充“已动态执行攻击”；正式正例不能复制含 input generator 的整份
  task；canary 通过也不等于获得正式运行授权。当前 staging 没有 `canary:kernelbench-meta` entitlement，
  因此新 CLI 默认只读 preflight，未调用 GPU、模型、网络或远程 evaluator。
- 实现提交：`3972dce`。
- 验证：新增 policy/adapter/controller 定向测试 `76 passed`；完整回归在合并前另行记录。

## 2026-08-02 — KernelBench meta canary authority/replay closure

- 问题：controller 仍可自行生成授权 receipt，preflight 会回显其路径；并发 controller 也可能在同一
  reserve/start 窗口重复触发 evaluator。结果投影没有保留精确 correctness/timing 计数，GPU 实际用量
  若被截断还会掩盖 reservation 超额，独立重放因而不能单义证明攻击在预期调用点被抓住。
- 解决：receipt 改为外部 authority 提供，controller 仅验证、持有和消费，且必须与 evaluator capability
  的 SHA 完全一致；preflight 只公开是否存在。整个 execute 由非阻塞独占锁包围。结果对象保留并机械
  核对 0/0/0、5/1/0、5/100/100 三类协议计数；单席 GPU 超过 600 秒立即 fail closed，不再截断。
  authorization 精确绑定零起始 ledger head、staging plan 与 canary plan，独立 verifier 再重放 ledger
  和外置 head anchor。
- 避免：执行授权不能由消费授权的 controller 自签；replay 不能只核对最终 status，必须核对攻击停止点、
  真实资源用量和唯一执行者。
- 实现提交：`ee9f747`。
- 验证：authority/adapter/supervisor/policy 定向回归 `88 passed`，全项目 `470 passed`；未调用 GPU、
  模型、网络或远程 evaluator。

## 2026-08-03 — HarnessBuilder provenance-bound Rule Registry v2

- 问题：原 Rule Registry 只是规则名称与自然语言卡片；planner 只收到 rule ID，未接线的规则也能进入
  Builder allowlist，且只换 rule 标签会被误计为系统级 Harness 变化。这会把“来源中描述过的方法”
  错当成“controller 已能执行的方法”，无法可靠归因。
- 解决：新增 provenance-bound v2，逐条绑定固定仓库/commit/path/line/SHA、迁移说明与三轴置信度；
  五条真实 operator 规则可执行，八条未接线规则只能作 advisory，distillation 保持外层 post-seal。
  planner 获得解析后的规则卡，solution 获得可信 rule effect，每次编译保存 `RuleDecisionTrace`；未知或
  advisory rule fail closed，rule 标签从 operational fingerprint 中移除。四个 Builder 变体和 prepare
  输入统一绑定 v2 SHA，旧 staging 不能为新 revision 提供执行授权。
- 避免：新增外部搜索方法时，必须先区分源码事实、Moss 安全迁移和 trusted operator 接线状态；没有
  operator 与回归测试的规则不得进入 executable allowlist，task-specific 数值继续由冻结合同/profile
  外置。
- 实现提交：`5a2a5ff`。
- 验证：规则注册表定向 `11 passed`，HB-GEN-1 相关回归 `43 passed`，全项目 `481 passed`；
  `git diff --check` 与 Registry/variant SHA 绑定检查通过。未调用模型、GPU、网络或远程 evaluator。

## 2026-08-03 — 三臂 24 题实时泛化矩阵

- 问题：旧 `A/B0/B*/B-online` 四臂依赖 KernelBench 历史与仍阻断的 KernelBenchX/SWE-Perf，且不符合
  用户确认的“空状态起步、每题评分后立即学习、最后两题只验证”协议。
- 解决：新增独立 schema v2 的 `A/B-frozen/B-online` controller，冻结 LCBench、CompilerGym cBench、
  SWE-bench Verified 各 6 online + 2 holdout；三臂按题封存后只蒸馏 B-online 自身公开轨迹，逐 arm-cell
  恢复且同题复跑零学习。补齐三套 production codec/backend/provider、真实 canary、clean-revision/source
  binding、内容寻址预算与 72 arm/576 round 全封存后才生成的 CSV/HTML 曲线。SWE-bench 明示采用官方
  standard threat model，并为远程 terminal result 增加不重跑 evaluator 的严格绑定恢复。
- 避免：跨题经验只能由当前 online arm 的 sealed public events 产生；holdout 不得 distill；旧四臂资产和
  KernelBench 轨迹不得暗中进入空 Experience Bank。镜像 digest、数据 SHA、suite canary 与代码 revision
  必须在 staging 时共同冻结。
- 实现提交：`dc956ca`；SWE-bench 最小官方 harness import、log-parser helper 与远程 terminal replay
  修复：`fe9ff48`、`5d65c10`；digest 校验后的本地镜像 tag fallback：`5a9a8b5`。
- 验证：LCBench 8/8 与 CompilerGym 8/8 真实无模型 canary 通过；三臂/HB 定向 `340 passed`，全项目
  `494 passed`，最新 SWE-bench adapter/replay 回归 `3 passed`，`git diff --check` 与 compileall 通过。

## 2026-08-03 — SWE-bench Verified gold canary diff 归一化

- 问题：冻结的八条官方 gold patch 都省略 Git `index` 行，直接送入与正式候选共用的严格 diff validator
  会在远端 evaluator 前被拒绝，导致 canary 无法验证已经锁定的镜像与官方评分链。
- 解决：仅在数据集 SHA、八题选择和镜像锁均通过后的 canary 专用入口，给普通文件修改段确定性补入
  非语义 `index` metadata；所有原始 header/hunk 保持逐字不变，并把官方 patch SHA、归一化规则和归一化后
  candidate SHA 一并写入证据。模型候选与远端 worker 继续使用原严格 validator，没有新增宽松分支。
- 避免：可信 reference/gold 输入与模型候选共享 codec 时，先核对两者的纯 metadata 形态；若只需正规化，
  必须证明移除新增 metadata 后逐字恢复上游输入，且不得修改正式候选接受集合。
- 实现提交：`a235dc4`。
- 验证：新增红测后定向回归 `12 passed`；冻结八题实际 Parquet patch 全部完成静态归一化，移除新增
  `index` 行后逐字等于官方 patch；`git diff --check` 通过。

## 2026-08-03 — SWE-bench canary 终态字段纠正

- 问题：首个 normalized gold patch 已由远端 evaluator 判为 `valid/resolved/score=1.0`，但 canary 汇总器
  误读其他 adapter 才有的 `correct` 属性，导致成功的 terminal result 在汇总阶段抛出 `AttributeError`。
- 解决：新增 SWE-bench 专属终态判定，机械要求 `status=valid`、`valid_scored=true`、`resolved=true`、
  `score=1.0` 且 FAIL_TO_PASS/PASS_TO_PASS 计数全通过；已封存的私有结果按绑定 replay，不重跑 evaluator。
- 避免：跨 suite 的 evaluator dataclass 不得按相似语义猜测字段；canary acceptance 必须对具体 result schema
  写红测，并覆盖成功结果及每个拒绝维度。
- 实现提交：`098db55`。
- 验证：先复现 import/contract 红测，修复后 SWE-bench adapter/canary 定向 `5 passed`；首题私有结果显示
  `valid_scored=true`、`resolved=true`、`score=1.0`、F2P `1/1`、P2P `17/17`。

## 2026-08-03 — SWE-bench 离线容器 loopback 修复

- 问题：前四题 gold canary 均为 1.0，第五题 Matplotlib 在 pytest 收集前由 `pytest-rerunfailures`
  初始化本机套接字失败；Docker `network_disabled` 环境未解析 `localhost`，官方 grader 随后把 265 个
  未执行的目标测试误列为失败。
- 解决：保持容器外网禁用，只显式加入 `localhost -> 127.0.0.1`，并在复制/应用候选前用 testbed Python
  执行 loopback bind 预检；失败走现有 `environment_invalid` 终态，不产生候选分数。
- 避免：禁网 evaluator 仍可能依赖 loopback；正式评分前必须分别验证“无外网”和“本机 IPC 可用”，且
  环境预检必须发生在候选代码进入容器之前。
- 实现提交：`428ecd7`。
- 验证：新增红测先因缺失网络合同 helper 在收集阶段失败，修复后定向 `6 passed`；同一锁定 Matplotlib
  镜像在 `--network none --add-host localhost:127.0.0.1` 下实际完成 267 项收集，官方两项 F2P 与全部
  263 项 P2P 均通过（另有 1 个非计分测试失败、1 个非计分测试跳过）。

## 2026-08-03 — Docker SDK 禁网语义纠正

- 问题：v3 首题 Sphinx 在候选应用前的 loopback 预检失败。对照证明 Docker SDK
  `network_disabled=True` 即使记录了 `localhost:127.0.0.1`，testbed Python 仍返回名称解析错误；而 CLI
  `--network none` 与 SDK `network_mode="none"` 都能在无外网 namespace 中成功解析并 bind loopback。
- 解决：网络创建参数改为 `network_mode="none"` 加固定 `localhost` 映射，候选前预检与资源限制不变；
  v3 的 `environment_invalid` 终态保留，后继使用新的内容寻址运行快照和 canary segment。
- 避免：Docker CLI 与 SDK 名称相似的禁网选项不得按字面视为等价；生产前必须用与 worker 相同的 SDK
  create/exec 路径做真实 socket 预检，而不是只用 CLI 对照。
- 实现提交：`8900bfb`。
- 验证：回归红测先显示返回参数仍为 `network_disabled=True`，修复后定向 `6 passed`；远端同一 Sphinx
  锁定镜像经 Docker SDK `network_mode="none"` 创建后显示 `NetworkMode=none`、`NetworkDisabled=false`，
  testbed Python 成功 bind `127.0.0.1`。

## 2026-08-03 — 三臂 planner 合同拒绝恢复

- 问题：SWE-bench canary v4 已 8/8 通过，正式 v1r1 首题 A 臂 8/8 与 B-frozen v001 已封存；随后
  B-frozen v002 planner 只改了 rule/directive 措辞，没有改变 operational fingerprint。runtime 的
  正确拒绝被 runner 升级成全局异常，三个恢复入口只能重复 replay 同一已消费模型结果，流水线阻断。
- 解决：planner 的格式错误、trusted compile 拒绝和强制变化轮无 operational change 现在都封存为
  schema v2 `planner_contract_rejected` 零分轮次，绑定原始响应 SHA；已消费 planner call 不退款，也不发起
  solution/evaluator。后续轮从最近有效 Harness 继续；一次性 A 臂若 v001 无效，v002–v008 只执行并归档
  sham planner 后同样拒绝，不能偷偷重新初始化。提示词同时明确 operational fingerprint 的七类字段。
- 避免：生成产物违反公开 Harness 合同属于实验结果，不是基础设施故障；必须进入分母、保留成本和原始
  响应绑定。恢复逻辑必须区分最近有效 decision 与逐轮 attempt 槽位，且不能用额外模型调用修补无效输出。
- 实现提交：`c953b38`。
- 验证：先用真实故障形态写红测，修复后 Harness runtime/runner/formal/meta-train/three-arm 定向
  `29 passed`；全仓 `500 passed`；`git diff --check` 与 compileall 通过。

## 2026-08-03 — 三臂 JSON suite 顶层合同提示修复

- 问题：v1r2 在新 planner 恢复语义下正常启动，但 LCBench A 臂前两轮都生成了 16 个合法 query 的
  `{"queries":[...]}`，遗漏冻结 codec 必需的 `schema_version` 与 task-bound `instance_id`；两轮因此均为
  `contract_rejected` 且没有 evaluator transaction。CompilerGym task card 同样只说“strict JSON sequence”，
  存在遗漏 `schema_version/benchmark_uri` 的同类风险。
- 解决：保留并停止 v1r2，不覆盖 round、raw response 或已消费调用。LCBench task card 现逐字给出
  `{"schema_version":1,"instance_id":"<task>","queries":[...]}`、七个 query 字段与范围；CompilerGym
  逐字给出 `{"schema_version":1,"benchmark_uri":"<uri>","actions":[...]}` 与完整冻结 pass allowlist。
  codec、scorer、预算和 task binding 均不放宽。
- 避免：模型看到嵌套 reference contract 不等于会保留身份包装字段；每轮都存在 parent 切换，因此 task card
  自身必须完整、自包含地说明顶层 schema、当前 lane identity 和 payload allowlist。用真实失败形态写 provider
  红测，不能靠放宽 codec 自动补字段掩盖生成合同缺口。
- 实现提交：`c8a452e`。
- 验证：新增 provider 红测先 `2 failed`，修复后 provider/LCBench/CompilerGym/campaign 定向
  `32 passed`；全仓 `502 passed`；`git diff --check` 与 compileall 通过。

## 2026-08-04 — 持久目标阻碍诊断与中断轮次封存

- 问题：v1r3 已封存 1/24 instances、4/72 arms、35/576 rounds，但用户会话生命周期显式停止了
  systemd；`dijkstra / B-online / v004` planner 已 started 且没有 bound result。gateway 正确禁止重发，
  但 cell runner 没有把该已消费操作转成 terminal round，导致同一恢复入口永久阻断。
- 解决：新增 `skills/diagnose-goal-blockers/`，以后目标暂停、Monitor 失败、服务停止、产物无增长或长期
  started 时，先核对控制面、产物、进程、operation ledger 与 revision binding。runner 新增 schema v3
  interruption round：planner/solution/evaluator 的 started-without-artifact 记为 `*_operation_abandoned`，
  terminal-failed 记为 `*_operation_failed`；两者绑定原 journal event、保持预算扣除、禁止重发并继续后继轮。
- 避免：目标状态、Monitor、服务和产物是四个独立信号；恢复前必须按 Skill 对账。source-bound 正式 segment
  若需代码修复，保留旧 segment 为消费证据并启用新 clean revision，不能注入新代码或手工伪造 receipt。
- 实现提交：`a373329`。
- 验证：三类中断与 provider failure 红测先 `3 failed`，修复后 runner `9 passed`、三臂/formal/meta-train
  定向 `35 passed`、全仓 `505 passed`；Skill quick validation、`git diff --check` 与 compileall 通过。

## 2026-08-04 — 三臂跨题蒸馏冻结 schema 提示修复

- 问题：v1r4 已封存首题 24 轮与三臂，distillation operation 也已 completed，但模型返回自造的
  `suite/instance_id/builder_checkpoint_sha256/observation/evidence_event_ids` 简版记录；严格
  `ExperienceRecord.from_dict` 因缺少冻结的 14 字段而拒绝，三个 formal attempt 均在同一解析点失败。
- 解决：保留 v1r4 的 completed operation、raw response、24 轮和 3 个 arm 作为消费证据，停止自动重启。
  distillation prompt 现逐字给出 bare `records` JSON、14 个精确字段、当前 source/checkpoint/provenance
  binding 与禁止 compact alias 的约束；parser、预算、scorer 和 test-then-learn 边界均不放宽。
- 避免：要求“strict Experience Records”不足以让模型推断冻结 dataclass；凡模型输出进入 exact-key codec，
  prompt 必须自包含顶层 wrapper、逐字段模板、当前 identity 与别名禁令，并由捕获真实 prompt 的红测锁定。
- 实现提交：`3a8459d`。
- 验证：红测先因 prompt 缺少 `record_id` 失败；修复后 learning/formal/three-arm 定向 `14 passed`，全仓
  `505 passed`，`git diff --check` 与 compileall 通过。

## 2026-08-04 — 三臂 suite-blocked 顺序与固定八轮均值

- 问题：旧平衡交错流适合控制三个 benchmark 的时间漂移并提早观察混合流迁移，但会把跨 benchmark
  切换混入相邻题差异，不能直接回答“同 benchmark 连续 test-then-learn 后，B-online 相对 B-frozen
  是否逐题增长”。旧报告还跨任务聚合逐轮 running-best，没有把一道题的八轮固定分母平均作为主单位。
- 解决：staging 升级为 schema v3，机械要求 `stream_policy=suite_blocked`，正式顺序冻结为
  YAHPO 八题→CompilerGym 八题→SWE-bench 八题；每 suite 仍为前六题学习、后两题 sealed，B-online
  checkpoint 跨 suite 前传。报告将无效/错误/缺失/非数值轮记零后固定除以 8，逐 suite 输出六题
  `B-online-B-frozen` 均值、OLS 顺序斜率、T6−T1 变化及 sealed 对照；原始分数不跨 benchmark 混加。
- 避免：研究问题改变后，不能只改图表文字而保留回答另一问题的执行顺序；stream policy、统计公式、
  零分语义和五份完成产物必须同时进入严格 schema、反向测试与 source-bound clean segment。v1r5 的
  38 rounds/4 arms/1 instance 及无结果 evaluator operation 只作旧协议消费证据，不用新代码原地恢复。
- 实现提交：`b13361a`。
- 验证：旧交错流和缩小无效轮分母的红测先失败；修复后最新定向 `9 passed`，全仓 `506 passed`，
  `git diff --check` 与 py_compile 通过。

## 2026-08-04 — 三臂恢复轮转式平衡交错流

- 问题：v1r6 在 suite-blocked schema 下推进后，用户重新选择先用平衡交错观察结果。该 live segment
  已绑定不可变 staging，不能原地改顺序；同时 CCM Monitor 已失败但 system-level workload 仍健康运行，
  说明监控状态不能替代 supervisor/账本事实。首次诊断还用过宽的 `v*.json` glob 把 solution/metadata
  误计为 round，必须以 `formal/cells/*/rounds/v*.json` 纠正。
- 解决：显式禁用并停止 v1r6 system service，保留真实 42/576 rounds、5/72 arms、1/24 instances 与
  最后 started-without-artifact operation。staging 升级为 schema v4、
  `stream_policy=balanced_interleaved`；八个 task block 各含三套 suite 的同位置题，block 内首发 suite
  循环轮转。固定八轮均值、无效轮计零、6+2 学习边界、预算和五报告口径均不变，v1r7 从空 bank clean start。
- 避免：任何 live stream 变更都必须新 revision/segment；停止前先对账 supervisor、严格 round 路径、
  arm/instance receipt 和最新 operation。数据汇报应同时区分 best score 与固定八轮均值，且旧协议的
  部分数据只能作方向证据，不能并入新协议正式曲线。
- 实现提交：`2639c96`。
- 验证：平衡交错与 schema v4 红测先 `6 failed`，实现后定向 `9 passed`、全仓 `506 passed`，
  `git diff --check` 与 py_compile 通过。

## 2026-08-04 — Harness 初版合同适配与有效性门禁

- 问题：v1r7 的 SWE-bench `sphinx-doc__sphinx-8459` 三臂均为 0 个有效轮。正式 task card 没有说明
  strict codec 要求的 Git `index` metadata；初版 Harness 也没有先从 task artifact contract 推导结构，
  后继轮只看到笼统拒绝。同时 B-online 的 controller 已选出前序经验，但旧静态 formal exclusion 又在
  compile 阶段拒绝它们。把这些无效轮按 0 计入均值还混淆了生成可靠性和性能。
- 解决：Rule Registry v3 新增可信 `contract_compatibility` operator，并在每题 v001 及合同失败后的
  恢复轮强制使用 task-bound capability card。SWE official/model patch 复用同一严格 compatibility layer，
  只允许剥外层 diff fence、补末尾 LF 和确定性非语义 `index` 行；路径、hunk、apply 与测试语义继续
  fail closed。B-online 改由 controller 对 stream/checkpoint/bank/record/source 签发内容寻址 grant。
  schema v5 同时冻结单臂至少 4/8 有效、suite 前六题至少 5/6 成对有效的门禁，均值与 best 仅统计有效轮。
- 避免：任何 exact-key/codec 任务都必须让 v001 Harness 先编译响应边界、逐字模板、安全正规化和禁止变换；
  controller 已授权的动态前序经验不能再与全池静态 exclusion 混用。合同可靠性不足时必须保留失败轨迹并
  标记 `insufficient_validity`，不得用零分或缩分母伪装为可比较性能。
- 实现提交：`275fabc`。
- 验证：v1r7 归档响应离线重放的 codec 接受率为 A `8/8`、B-frozen `4/5`、B-online `3/3`；受影响
  模块组合测试 `71 passed`，全仓 `516 passed`，`git diff --check` 与 compileall 通过。真实同题八轮
  qualification 仍作为正式流前独立门禁，成绩不得复用到正式实验。

## 2026-08-04 — v1r9 successor continuation 与远端执行硬绑定

- 问题：v1r8 已有六题可信前缀及 B-online 经验，但意外启动的 `scikit-learn-14983` 只应保留扣费证据；
  其余 SWE 题的 F2P 覆盖不足。直接复跑或复制旧 ledger 会污染顺序、经验与预算，远端镜像/代码路径、
  Codex CLI 和 staging/artifact root 若只靠名称约定也存在漂移或重复消费风险。
- 解决：新增 schema-v6 references-only continuation，内容寻址导入 v1r8 六题 checkpoint/Bank，执行窗口
  严格限制为全局 index `[6,24)`；A/B-frozen 保持空经验，B-online 才接续前缀。六个未开始 SWE 位置
  改为六仓库且 `F2P>=6` 的冻结集合；worker 只接受本地唯一 locked RepoDigest。资格 transfer 会重算
  evaluator 语义和镜像负向测试；remote-deployment receipt 绑定完整 tracked tree、worker、Python 与
  SWE checkout，并在每次 reserve 前 live reprobe。Codex 绝对路径/SHA、三套 gate、逐 cell cap 及
  `artifact_root == staging.parent` 同样 fail closed。报告只按 instance 输出三臂八轮均值、最高分和合规轮数。
- 避免：跨 revision 续跑必须把“历史引用、当前 entitlement、学习导入和排除尾部”分别做不可变证明；
  所有可能新建第二套账本或切换实际执行二进制/远端树的参数，都必须在首次 preflight 与 paid reserve
  之前交叉绑定，不能依赖 wrapper 命名或人工操作约定。
- 实现提交：`56bc079`。
- 验证：多轮独立审计补出 qualification 伪造、Codex 替换、远端树漂移与 artifact-root 重绑定红测；
  定向回归最高 `94 passed`，最终全仓 `569 passed`，`git diff --check` 与 compileall 通过；六个远端
  Docker RepoDigest 已与冻结 image lock 逐一一致，尚未由这些离线验证消费正式 round。

## 2026-08-04 — v1r9 SWE 禁网不兼容题替换

- 问题：`requests-2317` 的官方 gold patch 能 exact apply，但在冻结 `network_mode=none` 的正式合同中
  仍有 60 余个依赖外部 httpbin/TARPIT 的测试失败；把它继续留在正式池会把环境网络约束误记成模型能力。
- 解决：明确排除 `psf/requests`，在仍保持六仓库和 `F2P>=6` 的前提下把占比门槛降为批准的 `1/100`，
  按原固定 domain 哈希重放得到 `pytest-7205`、`matplotlib-25775`、`xarray-4356`、`sympy-21930`、
  `astropy-13977`、`pylint-4604`。全局 index 6 因此机械变为 `pytest-7205`；失败的 requests canary
  只保留为诊断证据，不进入成绩或学习。
- 避免：选题覆盖门槛通过后仍必须在完全相同的冻结网络、镜像与 worker 合同下跑 gold canary；任何环境
  不兼容题都要显式进入 selector exclusion，不能靠正式运行时 fallback、联网或 sidecar 临时补救。
- 实现提交：`ac7a0b8`。
- 验证：选择器红测先为 `4 failed`，实现后 v1r9/qualification/remote/adapter 定向 `55 passed`，全仓
  `569 passed`，`git diff --check` 与 compileall 通过。

## 2026-08-06 — references-only composition 兼容冻结历史 staging 字节

- 问题：v1r9 正式 campaign 已自然完成，但最终 composition 被 v1r8 的 pretty-printed
  `staging_plan.json` 阻断。该文件是有效 JSON，且 continuation snapshot 已精确绑定其原始字节 SHA；
  composition 额外要求 canonical JSON，错误地把历史序列化格式当成内容漂移。
- 解决：新增普通 JSON object reader，仅对 source staging 使用“有效对象 + snapshot 原始 SHA”合同；
  instance/arm receipt 继续走 canonical reader、逐层 SHA 与 sealed 8-round 校验，旧正式产物不修改。
- 避免：跨 revision composition 应区分不可变内容身份与新版本序列化约定；已由 snapshot 精确绑定的
  历史控制文件不应被事后 canonicalization 要求拒绝，但可执行 receipt 必须维持原严格合同。
- 实现提交：`3d32499`。
- 验证：正式故障形态红测先因 `source staging plan is not canonical` 失败；修复后 composition/report
  定向 `17 passed`，`git diff --check` 通过。

## 2026-08-06 — 三臂正式 campaign 完成与小型 held-out 报告

- 结果：v1r8 六题前缀与 v1r9 十八题后缀已用 references-only manifest 组合为 24 instance、72 arm、
  576 round；v1r9 service 自然 0/SUCCESS 退出，两个 operation journal 均与 trusted head 独立重放一致。
  LCBench/CompilerGym 前六题 paired validity gate 均为 6/6，SWE-bench 为 4/6、未过 5/6 门禁。
- 解释：B-frozen 在 LCBench 八题和 CompilerGym 六个双方合格题上逐题均高于 A，并显著提高 SWE
  有效生成率；B-online 相对 B-frozen 在学习题和每 suite 两题 sealed held-out 上方向混合，当前只能
  证明题内 Harness recompilation 的价值，不能声称稳定跨题正迁移。
- 产物：完整逐题 mean/best/validity、六题 held-out、失败分类、1,139 model calls、496 evaluator
  transaction、token usage 和 provenance 写入
  `docs/reports/2026-08-06-harness-builder-cross-benchmark-final-report.md`；机械 CSV/JSON/HTML 位于
  `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/`。
- 实现提交：`e5ae22d`。
- 验证：composition/report 定向 `17 passed`、全仓 `570 passed`；报告使用 manifest
  `169fcd18...7b2415`，CCM 完成态核验独立确认连续 stream index 0–23、24/72/576 和 v1r9
  3,659-event trusted head。

## 2026-08-07 — Self-Evolving AI 文献综述与 contribution 边界

- 问题：Harness/Agent/Skill 自进化的最新近邻快速增多，原定位容易把 test-time Harness evolution、
  typed compilation、reset/accumulate control 或可信评测宽泛地写成首创；README 还把每 suite 后两题
  误写成“完全不反馈”的 holdout。
- 解决：回到三篇综述、代表论文和 Penguin/GDPevo 固定仓库，按进化对象、时间尺度、反馈、更新算法、
  权限与证据矩阵整理 52 个一手链接；详细对比 Meta-Harness、Living-Harness、Penguin、GDPevo、TTHE、
  Self-Harness、HarnessX、AutoRAS 等，并记录同领域同名 MOSS 的命名冲突。贡献收窄为 task-bound
  closed-world compilation、单-instance controlled decomposition、跨机制复制和 evidence-preserving
  at-most-once recovery；新增少量 fresh held-out 的 2×2 方案，但未把它误写成已执行结果。
- 避免：positions 7–8 只能称 `cross-instance-transfer holdout under allowed within-instance adaptation`；
  whole-arm B-frozen gain 在 Prompt/Skill/component 与 optimizer-compute 对照前不得归因于 Harness 架构；
  不使用 `first`、`causal`、稳定跨题泛化或未消歧的 `MOSS` 名称。
- 实现提交：`79ff1e4`。
- 验证：52 个外部链接全部返回成功状态，Markdown 表格列数与 `git diff --check` 通过；全仓
  `570 passed in 362.36s`。

## 2026-08-11 — Benchmark 资格预评测与 B-online 因果验证方案

- 问题：旧三臂同时承担 Benchmark 难度、题内 Harness 适应和跨题 Experience 三个问题；LCBench、
  CompilerGym 与小规模 SWE-bench 又分别存在便宜传统搜索、已消费和二值 ceiling，无法用同一结果
  识别 B-online 的独立增量。少量 held-out 也不足以支持“统计显著”的 Task-level 表述。
- 解决：把下一轮拆成方法资格门与 online-transfer 门。首选 AgentHPOBench 做方法资格，Atrex 仅作
  硬件条件项；GDPevo 与 BIRD-Interact 做 B-online 迁移，OSWorld 2.0 留作高成本确认。每个候选先过
  evaluator 可信性、headroom、`N=1/2/4` 普通 scaling、非格式 Harness sensitivity 与 transfer topology；
  正式设计改为 Experience `E0/E1` × 题内 Harness 更新 `H0/H1`，四格保留相同 benchmark-native feedback。
- 避免：不能用 Moss 自身的正结果挑正式迁移题，也不能把 `B-frozen` 误解为 Harness 固定。8–10 个
  held-out 只作 go/no-go；确认性结论需每个 Benchmark 至少 24 个 fresh tasks、3 seeds、cluster-aware
  paired inference，并同时报告 ITT、validity 和完整成本前沿。
- 方案提交：`ca328fd`。
- 验证：12 个外部固定版本/论文链接全部返回 200，本地 Markdown 链接与 `git diff --check` 通过；全仓
  `570 passed in 365.96s`。未启动 runner、模型、evaluator 或付费资源。

## 2026-08-12 — 宽 Harness 与多元 B-online 运行时基础设施

- 问题：旧 `B-frozen` 只要求必要时至少一个架构轴变化，无法检验用户提出的“每轮全架构大改”；旧
  B-online 又只把跨题状态表达成 Experience Bank，无法区分 memory、meta-policy 与 Harness archive。
  恢复快路径也只有 round hash，不能证明新 wide Harness 在当前 trusted code 下仍可重编译。
- 解决：新增 `wide_all_fields_recompile_v1`，把 role graph、memory view、tool、parent、workflow、
  scheduler 与 recovery 固定为七轴；v002 起七轴必须全部实质变化，完整 accepted lineage fingerprint
  不得截短或复用。可信 compiler 每次新建七类 typed Python runtime component，并让它们实际执行
  parent/memory/tool/workflow/scheduler/recovery/role 行为；solution 前写入内容寻址 compile receipt，绑定
  parent、decision、catalog、component config 与 resolved effect。wide campaign 的 arm/instance 重放会
  重新绑定 provider、逐轮 trusted recompile，但不新增模型、evaluator 或 ledger 事件。另实现隔离的
  `OM` 内容寻址 memory、`OP` typed meta-policy 与 `OA` typed Harness archive 控制面及 Builder-only prior。
  审计后又把七轴稳定 configuration hash 纳入父子 receipt 门禁，禁止同名 tool callable 注入；M/P/A
  update 必须解析并验证真实 typed 父子对象后才能落账。新 wide 事实账本使用 canonical hash chain/head，
  receipt/index/round/formal 封存路径通过 `O_NOFOLLOW` 和 no-replace 发布拒绝 symlink 或非目录父路径。
- 资格与边界：冻结 AgentHPOBench `Q7/D11/T12` 与 GDPevo `Q6/D6/T6/Tfinal6`，本地固定 checkout 的
  commit/root tree 和 AgentHPO 31 个输入文件均重放通过；两个 Benchmark 的真实 evaluator canary 仍因
  GPU/依赖、容器隔离、磁盘和零 entitlement 阻断。四臂 manifest 明确把 arm-independent v001 trunk、
  `A/Skill/Targeted/Wide` formal orchestrator 与真实 provider 标成 `NOT_READY`，执行权限为
  `NOT_GRANTED`，因此没有产生正式新成绩。这里的组件“重装”只指 trusted Python factory 重实例化和
  配置，不是 OS/package 安装。
- 避免：不把 fake 多 Benchmark 闭环写成真实 Benchmark 效果，不把 HyperAgents 的开放代码 self-edit
  等同于 Moss 的 typed M/P/A，也不复用 `v1r8/v1r9` 经验或成绩来选择新任务。共享 v001 使用独立 trunk
  SHA 引用，不能声称含 arm/cell binding 的 compile receipt 逐字相同。
- 实现提交：`328e5d3`。
- 验证：全仓 `718 passed in 417.52s`；AgentHPO source-lock 重放为 commit
  `6d8d900...`/tree `1acedca...`/31 files，GDPevo 为 commit `0999c0d...`/tree `983742f...`；正式调用为零。

## 2026-08-13 — 四臂因果合同、共享 v001 provisional 控制面与攻击审计

- 问题：A、题内 Reflection/Skill、按需 Harness 变更和七轴全量重构没有共享一次 v001，无法公平归因；
  原始 Benchmark score 也可能被内部正值 utility 混入报告。初版共享 trunk 的自洽哈希仍不足以证明
  embedded compile receipt 与完整 compiled semantics 相同，caller-asserted task key、opaque outcome、
  stage interruption、exact matrix 与 arm-policy digest 也尚未达到正式可信边界。
- 解决：冻结 `A-fixed-feedback / S-reflection-skill / B-targeted / B-frozen-wide`；Targeted 从 v002 起
  必须至少一轴真实变化，Wide 必须七轴全变且 fresh component/lineage 均可审计。新增 task-local Skill、
  AgentHPO/GDPevo raw-score boundary、arm-independent v001 schema/archive、两 Benchmark 的零调用 fixture
  barrier/recovery；compile receipt 升为含 context binding 的 v2，并从 sealed parent 重算 Targeted change
  map。B-online 保持 `OM/OP/OA` 三条隔离表示。攻击审计发现的共享 trunk 缺口没有用“测试全绿”掩盖，
  manifest 已降为 `PROVISIONAL_FORMAL_BINDINGS_NOT_READY`，非零 authority 继续 fail closed。
- 避免：内容寻址只能证明 bytes 自洽，不能替代 typed source、full-semantic recomputation 或 operation
  provenance。正式启动前必须补全 v001 semantic replay、typed task/outcome/stage receipts、exact matrix、
  frozen arm-policy digest、真实 evaluator canary 和 request-level 预算；旧 24 题结果不导入也不改写。
- 实现提交：`7f5db55`。
- 验证：全仓 `794 passed in 474.67s`；后续安全补丁定向 `126 passed`，`git diff --check` 通过。旧 composite
  `summary.json` SHA 仍为 `553e76bd...994e`，计数仍为 24 instances/72 arms/576 rounds；本阶段模型、
  evaluator、GPU 和付费调用均为零。

## 2026-08-12 — Exact matrix、可信编译封存与 formal audit 加固

- 问题：零调用 fixture 只能证明状态机可运行，不能证明新实验的完整 126-cell matrix、四臂 variant 或
  task/context 来源；内容寻址 receipt 还可在重写七轴 change map、编译语义或 v001 fork digest 后整体
  重哈希。AgentHPO qualification 同时保留了已不准确的“strict codec/request accounting 缺失”阻断项。
- 解决：从 checked-in manifest 机械展开 AgentHPOBench 36 与 GDPevo 90 个 task×seed cell，冻结各自
  6/3 轮、四臂 policy/variant digest 与 Latin order balance；新增 typed v001 outcome/interruption archive、
  strict AgentHPO discrete intervention codec、space/request receipt 和 exact-plan v001 fork verifier。Wide
  父链从 sealed decision 重算七轴 change map；production seal 必须用实际 `CompiledHarness` 在任何落盘前
  重建并逐字核对 receipt，generic store 只能显式 `fixture_only`。正式 archive 另绑定全局 contract 与
  per-arm variant digest，store/load 都拒绝 fully-rehashed 错误值。
- 避免：self-consistent hash 不是 provenance。126-cell plan 目前仍只锁 identity/seed/round/order，可信
  task/context artifact authority 与 formal barrier controller 均保持 `NOT_READY`；AgentHPO 仍缺 pinned
  upstream space derivation、唯一 transport ledger、资源和真实 canary。因此 execution authority 继续
  `NOT_GRANTED`、全部 entitlement 为零，未进行模型、GPU 或真实 evaluator 调用。
- 实现提交：`a37918c`。
- 验证：独立攻击复审未发现新的 blocking bypass；全仓 `847 passed in 419.69s`，`git diff --check` 与两个
  canonical manifest 重放通过。factorial contract digest 为
  `fdafbb37d0470d68ee7e36390e8b2c47aac2ba8d066adea02fe52f4bffffd281`，manifest SHA256 为
  `e4cfe9e31d750a197217d47cc7ddd169e726acd517f361e39fbe775a6fc7ad58`。

## 2026-08-12 — Factorial source authority、ITT 边界与可信交接

- 问题：exact 126-cell plan 只校验 identity/seed/round/order，公开工厂仍可接受自洽但伪造的
  task/context hash；typed score receipt 也没有 ITT native-floor 投影。最初把 source authority 做成独立
  组件后，独立攻击审计仍证明 raw keys 能绕过 authority 直接进入 plan，且 DTO parser 名称可能被误当成
  provenance 验证。
- 解决：从 AgentHPOBench/GDPevo pinned Git object database 机械重建 42 个 solver-visible task artifact
  与 126 个 task/seed key；GDPevo 只投影公开 input，private evaluator/gold 仅进入 controller binding。
  authority bundle 使用 strict canonical replay，并要求每个 key 绑定对应 source artifact。公开 plan 构造与
  parser 均强制 exact authority+bundle、重读 pinned source 后比对 bundle SHA 和全部 126 keys；formal
  barrier 构造与每次 v001 bind/recovery 再重放一次。AgentHPO 11 个 scalar task 从 manifest/backend/runner
  AST 双向派生精确离散空间并支持 JSON `null`；free-form task 继续 fail closed。新增 exact ITT artifact，
  typed invalid receipt 映射到 Benchmark native floor，公开报告禁止内部 utility。
- 避免：canonical/self-rehashed DTO 只能证明内部自洽；可信入口必须重新派生 source authority。ITT typed
  projection 也不等于可信正式分数：reservation/evaluator/optimizer/report 一对一 dispatch、transport
  ledger、正式 provider、Skill dispatch、真实 canary 和非零预算仍是 blocker，执行权限保持零。
- 实现提交：`57262f4`。
- 验证：独立两轮攻击复审确认 raw-key、self-rehashed bundle/plan 与错误 authority 的可信入口旁路均已
  闭合；目标回归 `95 passed`，全仓 `880 passed in 438.81s`，compileall 与 `git diff --check` 通过。factorial
  contract digest 为 `afc44a41e2ff18155726d3f5cebfa66c085963215b3a3b1804ba39685667bb2d`，manifest
  SHA256 为 `707545ccce8cde2aa066186b60ce79e8fa1a638c1c8e344e0d55725b9cbd211f`；本阶段模型、
  evaluator、GPU 与付费调用均为零，旧 24-instance 数据未改动。

## 2026-08-13 — Shared-v001 可信重编译、精确覆盖与 online 零调用计划

- 问题：共享 v001 的 typed semantic evidence 仍可能被整体重哈希，artifact capability 虽进入 context
  binding 却没有实际进入 solver prompt；主实验也没有精确枚举全部 scoring slot，B-online 的 M/P/A 只有
  机制概念而没有完整逻辑调度。独立攻击审计进一步证明裸 `HarnessDecision`、自重哈希 compile result 和
  自重哈希 1,566-slot matrix 都可能绕过仅结构校验。
- 解决：新增 source-bound compile-only orchestrator，每次重读 pinned authority、exact plan、Rule Registry
  与 operator source，canonicalize decision 后四次重编译共同 v001，并在消费边界逐字核对 runtime、canonical
  contract、equivalence 与四臂 receipt。source-derived artifact capability 只经 allowlisted `task_semantics`
  深复制进入 prompt。另机械展开 126 个共享 v001 + 两套 Benchmark 各 720 个 post-v001 计分槽；coverage
  verifier 在 seal 前必须从 pinned source/plan/bundle 重建整套矩阵。canary readiness 与 online 计划分别固定
  AgentHPO/GDPevo 的未来零调用 schedule，以及 `O0/OM/OP/OA` 的 732 attempts、84 updates、1,548 logical
  calls；所有对象继续 `NOT_GRANTED`、零 entitlement。
- 避免：canonical hash 与 exact count 都不是 provenance；任何可信 consumer 必须重新派生 source、plan、
  Registry/compiler 或 operation journal。Online held-out 与主实验复用部分预声明 task identity，只能称禁止
  导入主实验 result/trace/state 的同题机制比较，不能称 independent fresh confirmation。post-v001 七轴
  Harness chain、Task-local Skill、provider/evaluator、online source receipt→parent/output checkpoint 与真实
  canary 仍是硬门禁，不能因零调用计划完整而启动正式执行。
- 实现提交：`4ba0cea`。
- 验证：全仓 `923 passed in 450.90s`；独立审计后新增全矩阵 self-rehash 红测并通过；`git diff --check`、
  compileall 和 canonical manifest 重放通过。factorial contract digest 为
  `5f3c21dbfe2a448ed95905de244ea75cfe4a2e0f6d0c5a7535d5ad90d4e57ede`，manifest SHA256 为
  `76a3698ec43383cd94bcb793ede2449344bd1f004b3e25da69ea0f1a5ef82c98`；本阶段模型、evaluator、GPU 与
  付费调用均为零，旧 24-instance 数据未改动。

## 2026-08-13 — Post-v001、Task-local Skill 与 typed online state 可信接线

- 问题：精确计划只覆盖共同 v001，无法证明后续 B-targeted/Wide 真正在 pinned task/context 上可信重编译；
  S 的 Skill 也没有与冻结 Harness、当前题 public feedback 和 solution prompt 形成 typed 边界。Online
  `OM/OP/OA` 只有 slot/hash 谱系，任意 state digest、伪造 `CompiledHarness` 或跨题记录仍可能形成表面
  自洽的 held-out prior。
- 解决：新增 post-v001 zero-call authority，从 pinned AgentHPOBench/GDPevo source、exact plan、1,566-slot
  matrix 与 v001 fork 重放当前 physical round；B-targeted accepted transition 至少改变一轴，B-frozen-wide
  强制七轴 configuration 全变、active component nonce/config 不复用、lineage fingerprint 唯一，并用
  trusted Registry 重编译逐字核对 receipt。已有合法 intent 的 rejected round 写 ITT floor，后继从最近
  accepted parent 继续。新增 S authority，只允许同 task/seed 的 bounded Skill，冻结 v001 decision/七轴并
  trusted recompile 后才追加 solution projection。Online 新增 16 条精确 benchmark×seed×mechanism lane，
  每个 OM/OP/OA update 解析 proposal 与 parent/child memory/policy/archive/checkpoint，逐步执行
  `apply_verified`，限制 source allowlist 后重新派生 held-out Builder prior；O0 强制零 prior/legacy memory，
  四机制共享 source cohort，compile consumer 重新生成 binding 并 trusted recompile，不能接受伪造 binding
  或 caller 构造的 `CompiledHarness`。
- 避免：typed dataclass、canonical bytes 和 content hash 都不是 execution provenance。source terminal/
  operation digest 尚未由唯一 journal 认证，完整 planner request/result、pinned online task authority、
  updater failure cursor、正式 provider/evaluator/report dispatch、真实 canary 与非零 entitlement 继续
  `NOT_READY/NOT_GRANTED`。Online 与主实验预声明 identity 重合，只能并行准备和做隔离状态的同题机制
  比较；qualification 门通过前不得正式运行 B-online。AgentHPO selector 已统一为 `Q7/D11/T12`，GDPevo
  为按 group 隔离的 `Q6/D6/T6/Tfinal6`。
- 实现提交：`1643675`。
- 验证：相关范围 `135 passed in 117.88s`；全仓 `958 passed in 558.24s`；compileall 与 staged
  `git diff --check` 通过。正式模型、evaluator、GPU 与付费调用均为零；旧 composite 的 `summary.json`/
  `results.csv` SHA256 仍为 `553e76bd...5994e`/`8818b9e8...3ab6`，24 instances/72 arms/576 rounds 未改动。

## 2026-08-13 — Exact operation schedule 与 static Q0 evidence

- 问题：1,566 个 scoring slot 已枚举，但潜在的 update/solution/evaluator 外部阶段及逐 cell 离散硬帽仍
  没有从 pinned source 机械展开；Q0 readiness 也只是未来计划，不能区分已能本地重放的 source/codec
  事实与尚未执行的 reference/environment/isolation canary。外部能力核验同时确认当前开发机缺
  GPU/OCI/Conda 且根盘余量约 1.7 GiB；历史 A100 alias 当前不可达，可达 jump 仅 2 CPU/约 1.6 GiB
  RAM，不能承载正式 Q0。
- 解决：新增 exact zero-call operation schedule，从 source authority、formal plan 与 1,566-slot matrix 重放
  1,206 update、1,566 solution、1,566 evaluator，共 4,338 个潜在 side-effect stage；满路径为 2,772
  model calls/1,566 evaluator transactions，并机械给出 shared-v001、AgentHPO 5 轮与 GDPevo 2 轮的逐
  cell 不可借离散上限。A post-v001 不生成伪 update，CPU/GPU 秒保持 real-canary pending，模块不暴露
  journal/governor/provider/execute callback。另新增 static Q0 evidence：重哈希 AgentHPO Q7 的 31 个
  source/control 文件、派生七个 original space，并实际执行 21/21 evaluator-before-codec negative；GDPevo
  只从 pinned Git ODB 重放 commit/root/task-groups 与 Q6 group/env/test trees，不运行 whole-worktree
  status、不读取 private gold，缺独立算法的 file-manifest 聚合显式保持 `UNVERIFIED`。persisted static
  evidence 只能经 trusted source replay 消费，不能由 caller 直接构造 typed artifact；Git 审计关闭 optional
  index locks。
- 避免：logical schedule 不是 operation journal，4,338 也是满路径潜在数；planner/solution contract reject
  会合法短路后续阶段，正式 seal 必须用 typed disposition 证明 executed 或 skipped-by-parent，不能为凑数
  制造调用。static Q0 evidence 不是 reference/environment/isolation canary，也不授予 evaluator seat。
  OperationJournal 的 no-follow storage 与 WAL crash recovery、AgentHPO Q7 baseline 的确定性/噪声口径、
  Q7 baseline 与 Q0 `12/12 reference` 的关系仍需在非零执行前冻结。
- 验证：新增 focused `15 passed`；相关 qualification/source/coverage 回归 `99 passed`；全量回归
  `973 passed in 682.99s`。独立攻击审计
  后封闭 nested self-rehash、伪 negative candidate/tree/space 与 GDPevo private worktree 输入旁路，并收紧
  schedule 的 arm/version/cell/attempt/logical-ID/role 关系。正式模型、evaluator、GPU 与付费调用仍为零；
  旧 24-instance 结果未改动。

## 2026-08-13 — Semantic stage disposition 与 hardened journal v2 草案

- 问题：4,338 个 potential stage 只证明“没有漏列”，不能证明同一 journal snapshot 中哪些真实 terminal、
  哪些因父阶段失败而合法短路；现有 v1 `events.py` 又会跟随 symlink，并在 ledger fsync 与 head replace
  之间存在崩溃窗口。直接原地加固会破坏历史 CompilerGym 36-event canary 对整个 `events.py` 的 AST
  compatibility proof。
- 解决：新增完全零授权的 semantic disposition verifier，从 pinned source/plan/matrix 重新派生 exact
  schedule，只对 ledger/head 做一次 v1 semantic replay；terminal completed/failed 必须精确匹配 cell/kind/
  discrete reservation，只有 failed 可使 immediate child skip，grandchild 必须逐级 cascade。它拒绝 schedule
  外 operation、reserved/started、failed/skip parent 后 child、无 artifact completion、跨 attempt/跨级、
  physical retry suffix、caller 重造 receipt/seal 与 mutable replay。4,698-event synthetic journal 形成
  1,566 failed roots + 2,772 skips；另一 mixed exact-set 形成 3 completed + 1,565 failed + 2,770 skips，
  二者都精确覆盖 4,338 项。持久化 artifact 只能通过 pinned source 与当前 ledger/head 全量重派生并逐字
  比对；standalone DTO 明确不构成 provenance。seal 仍内置全部 hardened storage/WAL/grant/retry/
  typed-gate/provider blockers、`formal_execution_ready=false`、`NOT_READY/NOT_GRANTED` 与全零 entitlement。
- 方案：新增 `docs/plans/2026-08-13-factorial-hardened-journal-v2.md` 草案，保持旧 `events.py`/v1 ledger
  字节不变；拟将 no-follow storage、pending-WAL exact redo、schedule/cap/explicit grant、logical→physical
  attempt 与 formal stage evidence 放入独立 v2 模块和新 clean segment。该草案尚未获用户冻结，不代表
  已实现 WAL 或拥有执行授权。
- 避免：`operation_completed` 仅说明 transport terminal，不说明返回 artifact 通过 JSON/schema/compile；
  completed parent 的本地 gate reject 仍需 future typed rejection receipt。started-without-artifact、环境 retry、
  physical IDs、accepted compile head 与 reason-code 闭集也未由本模块决定。正式模型、Evaluator、GPU、CPU
  与付费调用仍为零，B-online 仍仅准备。
- 验证：新增 focused `11 passed`；operation schedule/coverage/disposition 相关 `27 passed`；项目依赖环境
  全量回归 `984 passed in 631.97s`。两个外部 checkout 均在冻结 commit，未发生 skip。正式模型、Evaluator、
  GPU、CPU 与付费调用仍为零，旧 24-instance 结果未改动。

## 2026-08-27 — 双层 Harness 仓库结构清理

- 问题：宿主目录的本地 `main` 落后远端 45 个提交，容易把 8 月 13 日快照误判为当前代码；远端仓库中
  `AGENTS.md` 又在 8 月 24 日被意外从 symlink 提交成只含 `CLAUDE.md` 字样的普通文件。实验一同时保留了
  522 行无入口、无测试、无导出引用的 `_LegacyCrossMatrixRunner`，README 的目录图仍只描述早期 pilot。
- 解决：以 `origin/main` 为审计基线，恢复 `AGENTS.md -> CLAUDE.md`，删除已由现行 `CrossMatrixRunner`
  完整替代的死代码；README 和项目指南将当前双层 Harness、历史可复现实验及共同基础设施明确分区，
  双层实现计划标记为已完成。冻结题库、旧 runner 和 `archive.jsonl` 仍承担协议复现职责，未按更新时间误删。
- 避免：判断“是否本轮有改动”必须先比较本地/远端 revision；GitHub 的文件日期是最后一次内容变更时间，
  不是仓库活跃度。清理研究仓库时必须同时核对 import、CLI、测试、文档和冻结合同引用，只有五者均无引用
  的实现才可按死代码删除。
- 实现提交：`6e920a6`。
- 验证：双层 Harness/实验一 focused `131 passed, 6 skipped`；全仓
  `1195 passed, 85 skipped in 861.04s`；`py_compile`、`git diff --check`、symlink target/content 核对通过。

## 2026-08-27 — 实验一下层 Harness 结构门禁解禁

- 问题：`production_harness_probe` 把下层 Harness 写死为恰好一次 `model_call`。ALE-Bench canary
  中 Builder 合法提出 `draft → verify_and_revise → emit`，但在真正执行前被该内部结构限制回滚；
  Solver 答案本身已通过 Contract Skill、严格 codec 和官方 evaluator，因此不是答案合同故障。
- 解决：删除单模型调用拓扑限制，不新增调用次数上限；production probe 只要求至少一次模型调用
  和公开工具白名单，唯一最终 `emit`、节点类型、节点身份、prompt 大小及整体节点安全界限继续由
  `TaskHarnessSpec` 统一验证。两阶段或更长的线性 Harness 因此可由 Builder 真正提交和执行。
- 避免：通用安全门禁不得夹带特定 Harness 拓扑偏好；答案格式门禁与 Harness 结构门禁必须在
  日志和报告中分开命名，避免把内部回滚误报成 benchmark 或 Contract Skill 拒绝。
- 实现提交：`b7f7a28`。
- 验证：focused production probe 红测先复现两模型 Harness 被拒绝，修改后
  `tests/test_experiment_one_production.py` 为 `14 passed`；AWS Linux 全仓回归为
  `1189 passed, 95 skipped in 321.96s`。首次全仓运行仅因隔离验证环境缺少 `uv` 导致
  KernelBench 环境预检失败；在临时验证目录补齐 `uv 0.12.6` 后，该单测与全仓均通过，未修改共享实验环境。

## 2026-08-28 — 实验一最终答案 Contract Skill 固定绑定

- 问题：实验一 production 入口直接通过 `TaskHarnessRuntime → DualHarnessRuntime` 执行 Builder 生成的
  下层 Harness，绕过了普通 operator 编译路径中的 EdgeBench/ALE-Bench 输出 Contract Skill。Builder
  因而可能在进化 Harness 时删除或写出与公开 parser 冲突的交卷格式要求，导致 Solver API 已成功却在
  本地严格解析阶段终止，无法进入官方 evaluator。
- 解决：Python 依据最终 `emit.input_key` 追溯真正生成候选答案的最后模型节点，只向该节点不可删除地
  追加公开输出 Contract Skill；中间分析节点不受最终 JSON 或 fenced source 格式约束。单题进化、H0
  和冻结 Harness 的 cross-test 统一使用同一 runtime factory，contract hash 进入 Solver request identity、
  prompt audit 与 run receipt。格式失败和已脱敏 API 失败同时记录具体公开原因，不再只写模糊异常类型。
- 避免：固定答案合同只保护 benchmark 的公开交卷边界，不替 Builder 修答案，也不限制 Harness 的角色、
  多模型步骤或工具组合；只有新 `next_harness_sha256` 在下一轮成为实际 `harness_sha256`，才可归因于
  Harness 自进化。同一 Harness 下答案或分数波动仍不得包装为结构改进。
- 实现提交：`7a58d0e`。
- 验证：本次相关回归 `120 passed in 24.84s`；带完整 Git 历史的 AWS Linux 环境全仓
  `1216 passed, 95 skipped in 330.72s`；`compileall` 与 `git diff --check` 通过。首次归档验证中的
  大量哈希失败由 Windows CRLF 传输引起，第二次无 `.git` 归档只剩历史 revision 测试失败，均通过完整
  Git bundle 环境排除；验证过程中未调用模型、benchmark evaluator 或 GPU。

## 2026-08-28 — 实验一 Builder proposal 哈希与节点字段合同修复

- 问题：旧 campaign 的实验一 Builder 公开视图只暴露 `current_sha256`，但 proposal prompt 却要求模型
  从不存在于该视图的 `available_harnesses` 中选择父 Harness。真实响应因此把 `source_sha256` 和
  `base_sha256` 返回为 `null`，并额外发明运行时不支持的 `output_key`，造成 Builder 全部被门禁拒绝。
- 解决：每轮 prompt 直接绑定当前 Ht 的完整 64 位哈希，要求两个 lineage 字段逐字复制；同时列出节点
  字段白名单、状态输出规则以及 raw JSON 边界，不放松 Python 的哈希、schema 或可执行结构校验。
- 避免：Builder 可见信息、自然语言合同与 Python parser 必须引用同一字段集合；若模型返回被拒绝，
  应先捕获脱敏后的响应形状并定位输入合同，不得把同一 H0 下答案变化误称为 Harness 自进化。
- 实现提交：`9baea09`。
- 验证：AWS 上先观察新增测试按预期失败，修复后 Builder/dual runtime/实验一相关回归为
  `108 passed, 6 skipped in 29.83s`。真实 smoke 未被伪装成成功：两次独立调用均因上游 Responses API
  返回 completed 但无 output text 而终止，`provider_attempts=1`，没有 retry，也没有产生 H0→H1 commit。
