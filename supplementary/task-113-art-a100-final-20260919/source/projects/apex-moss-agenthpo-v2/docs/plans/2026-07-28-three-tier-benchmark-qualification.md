# 三层 Benchmark Harness Evolution 迁移资格实验（2026-07-28）

> **状态：方案已收敛，待用户批准后进入执行模式；尚未实现，未发起任何模型调用。**
>
> 本方案替代
> `2026-07-28-next-round-integrated-plan.md` 原第二阶段中“机制修复 + Builder
> seed 四谱系合并实验”。历史实验、结果和判定不变。Builder seed、Builder
> evolvability、task-conditioned specialization 与 Q2′ 全部后移，只有本资格实验
> 达到 go gate 后才可另立冻结协议启动。
>
> 冻结边界：执行模型、Proposer 模型、TokenRouter 路线、隐藏终验、唯一计分入口、
> 防作弊规则、runtime/tool contract 和正式三遍不变。本文新增的是 benchmark 角色、
> selector、谱系状态机、结果隔离、预算台账和 test-once 门禁。

---

## 0. 决策摘要

本轮只回答一个问题：

> 两条从逐字相同通用 seed 出发的独立 Harness lineage，在 Proposer 只见
> training feedback、selector 只用 validation 聚合分数否决候选的约束下，能否都先
> 提高 training benchmark，再把增益迁移到完全密封的新 test benchmark？

设计固定为：

- 两条独立 lineage：`A1`、`A2`，seed 都是逐字相同的通用 `v001`；
- training benchmark：16 个已消费的 Q1 external benchmark instances；
- validation benchmark：20 个已消费的 Q2/V1 benchmark instances；
- test benchmark：34 个从未发生任何模型调用的 `q1_external` reserve instances；
- 每条 lineage 最多 4 个 mutation rounds、最多 4 次 validation look；
- training 必须严格提高至少 `1/16 = 6.25` 点，validation 只有否决权，
  固定容忍带 `ε = 1/20 = 5` 点；
- 两条 final 和 v001 全部按内容哈希冻结后，才允许一次性解封完整 test matrix；
- Builder go 要求两条 lineage 都满足 training/validation 前置门，test 聚合提升
  `>=0.05`（+5 点）、bootstrap 95% CI 下界 `> 0`，且两条 lineage 各自 test 增益都为正；
- 即使 go，也只能称为“迁移到一个新的 BigCodeBench-Hard benchmark sample”，
  不能直接称为“已泛化到整个 Task”。

这是**整个三层 optimizer 机制包的资格测试**，不是 validation selector 的单因素
因果消融。若需要证明“提升由 selector 导致”，以后还需同 proposal protocol、预算与
随机化规则的单轨对照；若声称“同 proposal stream”，则必须预生成不依赖父代选择的固定
候选流。本轮不为此增加第四层混淆。

---

## 1. 正式术语

### 1.1 三层对象

```text
Task
上游的通用能力范围 / 目标能力分布
例如：根据有限可见反馈，实现满足隐藏规格的程序
        ↓
Benchmark
从 Task 中抽取的有限 benchmark-instance 集合，用于测量这种能力
        ↓
Benchmark instance
Benchmark 中的一道具体题目
```

兼容说明：仓库现有字段 `task_id` 暂不重命名，但正文统一把它解释为
`benchmark-instance identifier`；现有路径中的 `train`、`val` 也不自动决定其在
新实验里的概念角色。

### 1.2 本实验中的 Task

本实验把上游 Task 冻结为：

> 给定带 docstring/specification 的程序 stub 与有限、不完备的可见行为反馈，
> 通过受限的读、写、测试交互实现满足未公开完整规格的程序。

BigCodeBench-Hard V1 是该 Task 的一个可操作 sampling frame，不等于 Task 本身。
固定 Python 环境、`claude-haiku-4-5` executor、工具和步数上限属于本实验的
**protocol context**，不是 Task 定义的一部分。

### 1.3 Harness 条件化层级

- **Task-conditioned Harness**：利用上游 Task 的稳定结构，例如规格审计、边界枚举、
  证据驱动修改和回归检查；不依赖某个固定 benchmark 或具体 instance。
- **Benchmark-conditioned Harness**：只对某个有限 benchmark 的共同口味有效，
  换一批同 Task instances 后增益消失。
- **Instance-conditioned Harness**：记忆、点名或特判具体 benchmark instance，
  包括 ID、路径、唯一函数名、独特常量或实例分支。

test benchmark 上提升只支持“向新的 benchmark sample 迁移”。至少两个独立冻结
benchmark、最好来自不同数据来源且方向一致，才构成较强的 Task-level transfer 证据；
它仍不是对整个 Task 的证明。

### 1.4 分数单位

所有 manifest、DTO、selector、analysis 和 gate 内部统一使用 `[0,1]` 的未舍入 fraction：

- `0.15` = 报告中的 `+15 percentage points`；
- `0.05` = `+5 percentage points`；
- training 单实例 = `1/16 = 0.0625`；
- validation 单实例 = `1/20 = 0.05`；
- test 单实例 = `1/34 ≈ 0.0294`。

只有展示层乘以 100 写“点”。任何 gate 都不得读取 `eval.py` 当前四舍五入后的
`pass_rate_mean`。

### 1.5 Gate 的精确算术

所有阈值和相等边界都用整数 pass count 或 Python `fractions.Fraction` 判定，禁止用
普通 `float` 比较。固定机械形式如下：

```text
training quick:
  candidate_count >= parent_count + 1

validation quick:
  candidate_count >= max(seed_anchor_count, parent_cached_count) - 1

formal training (每个 Harness 共 16*3=48 个判定):
  G_train = Fraction(final_total - seed_total, 48)
  G_train >= Fraction(3, 20)

formal validation (每个 Harness 共 20*3=60 个判定):
  G_val = Fraction(final_total - seed_total, 60)
  G_val >= -Fraction(1, 20)

test (每个 Harness 共 34*3=102 个判定):
  Delta_l = Fraction(final_l_total - seed_total, 102)
  Delta = Fraction(final_A1_total + final_A2_total - 2*seed_total, 204)
  Delta >= Fraction(1, 20)
  Delta_A1 > 0 and Delta_A2 > 0
```

repeat variation 也不以近似平方根决定边界。对每个 Harness 的 3 个 repeat counts
精确计算 pass-rate population variance `var`；因主 gate 已要求 `G_train>0`，
`G_train > pstdev` 机械实现为 `G_train**2 > var`。报告层才把
`sqrt(float(var))` 展示为 standard deviation。

bootstrap quantile、CI 与功效描述必须使用浮点；除此以外，本文所有 `0`、`0.05`、
`0.10`、`0.15` 阈值都先构造对应 `Fraction`。这避免例如 `3/20` 与
`4/20 - 1/20` 因二进制浮点表示被误判。

---

## 2. 研究问题与可证伪假设

### 2.1 RQ1：optimizer 能否稳定产生训练提升？

`A1`、`A2` 的 final 都必须在正式三遍 training benchmark 上相对同轮 v001 提升
`≥ 0.15`（+15 点），且提升大于 v001/final 两者较大的 across-repeat standard deviation。

- 两条都满足：optimizer repeatability 前提成立；
- 任一不满足：资格失败，test 保持密封，优先继续修 optimizer。

### 2.2 RQ2：validation selector 能否满足 Proposer-unseen 的过程容忍门？

两条 final 都必须在正式三遍 validation benchmark 上相对 v001 不低于 `−0.05`
（−5 点）。
validation 对新 Proposer 不可见，但它历史上已被计分、也不是严格 iid stratum；因此这
只是 selector 的 process tolerance gate，不是“未见 benchmark”或无偏泛化结论。

- 两条都满足：允许进入 sealed test；
- 任一低于 `-0.05`（−5 点）：selector/quick noise/回归保护仍不合格，test 保持密封。

### 2.3 RQ3：final 是否迁移到新 test benchmark？

设 `Δ1`、`Δ2` 为两条 lineage 在 34 个 test instances 上相对 v001 的
benchmark-instance-paired gain，`Δ = (Δ1 + Δ2) / 2`。

资格成功必须同时满足：

1. test matrix 完整，frozen finals 与最终 formal/test matrix 为
   0 tamper、0 contract violation、0 infrastructure-invalid；
2. `Δ ≥ 0.05`（+5 点）；
3. 固定 bootstrap 的 95% CI 下界 `> 0`；
4. `Δ1 > 0` 且 `Δ2 > 0`，不能由一条强 lineage 掩盖另一条负迁移。

任一条件不满足即不进入 Builder evolvability。CI 跨 0 属于
`inconclusive/underpowered`，不等于证明无效。

### 2.4 解释边界

本实验没有并行的“无 validation selector”新谱系，因此：

- 可以回答“这个三层机制包是否具备进入后续实验的资格”；
- 不可以单独归因“增益就是 selector 造成的”；
- 旧 R0/R1/R2 只能作历史背景，不能充当同轮因果对照。

---

## 3. Benchmark 构造与冻结

### 3.1 固定数据源与信息合同

全部实例继续来自：

- dataset：`bigcode/bigcodebench-hard` v0.1.4；
- commit：`298d2cc7b96612e15e47313c3603ee124cee0c1f`；
- Parquet SHA-256：
  `73a4270b43feb81abefad7bb1b592937c768ea45c3263bedc1cabd30a9a6ce79`；
- V1：1 个可见行为测试 + 完整隐藏终验；
- 依赖、`MPLBACKEND=Agg`、oracle 双验、flaky 过滤和 side-effect blacklist
  沿 `q1_external` 冻结环境。
- executor：`claude-haiku-4-5`；Proposer：`claude-sonnet-4-6`；路线：
  `.env.local → config.py → TokenRouter`，不得按结果换模型/endpoint。

### 3.2 三个 benchmark

| 角色 | n | 固定来源 | 既往暴露 | 本轮可见性 |
|---|---:|---|---|---|
| training | 16 | `q1_external/canary` 4 + `q1_external/val` 12，全部纳入 | 旧 Q1 已计分 | Proposer 可见本 lineage 的新 training trace |
| validation | 20 | `q2_paired/tdd_val_v1` 10 + `spec_val_v1` 10 | 旧 Q2 已计分 | 仅 scorer-private 聚合分数进入 selector |
| test | 34 | `q1_external/_manifest.json` 的全部 reserve | **从未发生模型调用** | final 全冻结后一次性解封 |

为什么允许旧 test 降级为新 training/validation：

- 已消费数据不能再次声称是 sealed test，但可以成为后续实验的 feedback/selection 数据；
- training 16 个实例全部纳入，不按旧分数挑题；
- validation 20 个实例全部纳入，不复用旧分数，本轮重新跑 v001 baseline；
- 真正无偏的迁移推断只来自 34 个从未运行的 reserve instances。

builder 只创建本轮 content-addressed view/snapshot，不得修改
`benchmarks/q1_external`、`benchmarks/q2_paired` 的历史文件、manifest 或 hashes。

为什么不把 fresh reserve 拆给 validation：

- 若拆成 fresh validation 12 + test 22，validation 单实例权重为 8.33 点，test 功效下降；
- 当前方案的单实例权重为 training 6.25 点、validation 5 点、test 2.94 点；
- validation 本来就会被反复查询，最珍贵的新实例应优先留给一次性 test。

### 3.3 互斥与机械化

实现阶段必须生成一个 tracked protocol manifest，至少包含：

- 三池完整 `task_id` 列表和两两交集为空的证明；
- 34 个 reserve 全量进入 test、无人工替换的证明；
- 每个允许文件的相对路径、SHA-256、大小；
- 无额外文件、无 symlink；hidden 文件只存在 scorer snapshot，永不进入 executor
  workdir；
- dataset、commit、Parquet、依赖、V1 splitter、oracle gate 和 protocol bundle digest；
- seed Harness SHA、模型、repeats、ε、round cap、预算和判定线；
- 每个实例的既往 exposure role：`score_exposed` / `fresh`。

34 个 test instances 在 manifest 中用
`sha256("moss-three-tier-report-block-v1\0" + task_id)` 排序，前 17 个固定为
`report_block_a`、后 17 个固定为 `report_block_b`，只作方向/集中度敏感性报告。
两个 block 来自同一 reserve 和同一数据源，不得称为独立数据来源，也不要求各自单独显著。

### 3.4 同分布声明的诚实边界

training 与 test 来自同一个 `q1_external qualified_order=50` 的机械 sampling frame；
validation 与它们共享同一上游 Task、dataset 和 V1 信息合同，但来自旧 allowed-lib
stratum，且旧结果已被人看过。因此三层属于同一个**声明 Task**，却不是严格 iid 的同一
依赖分层。

这不会污染全新 test，但可能使 selector 的 validation signal 不完全代表目标分布。
若研究目标要求严格 iid 三分割，必须另扩 untouched pool 后重写并重新冻结协议，不能在
本轮看结果后改池。

### 3.5 Canary 不得消耗 formal validation/test

- runtime preflight 只用 synthetic fixture 或已经消费、且不进入本轮三池的旧
  `tddgen_hidden/train` instance；
- 生成候选的真实单题 canary 同样只能用该 consumed canary pool；
- canary 对 controller 只返回“运行有效/无效”；PASS/FAIL、score、trace、instance ID
  永不进入 proposer-visible artifacts、下一轮 prompt、locked set、strict-gain 或
  selector，不能偷偷成为第 17 个 training instance；
- capability PASS/FAIL 都不筛版本；contract/infra 才阻止进入 full training quick，
  任何 tamper 触发全局协议复核并停止；
- test 34 题不做 difficulty canary、不抽样试跑、不换题。

---

## 4. 信息流与代码级隔离

### 4.1 角色权限

| 组件 | 可以看到 | 明确禁止 |
|---|---|---|
| Proposer | 当前 accepted parent、同 lineage 候选的 training-only aggregate/failed traces | validation/test instance、路径、分数、trace、拒绝原因；另一 lineage 的任何产物 |
| Training scorer | training instances 和完整结果 | validation/test 路径 |
| Validation scorer | validation instances、private raw results | 向 selector/Proposer 返回逐实例结果或 trace |
| Selector | typed scalar DTO：candidate/parent hash、train score、regression boolean、validation aggregate、validity | benchmark path、instance ID、per-instance pass、trace、pytest output、cost |
| Test scorer | 冻结 final registry + sealed test | 在完整 matrix 终态前发布任何部分分数 |
| Auditor | private raw、ledger、hash chain | 把 private 数据加入 proposal payload |

validation 对下一代的“父代是否改变”会形成不可避免的 selection-pressure channel。
本文的“不泄漏”定义是：不暴露 validation 的 instance、trace、score 或 rejection
reason；不声称信息论意义上的零比特泄漏。每 lineage 最多 4 次 validation look 用来限制
这种适应。

### 4.2 结果路径

新 runner 不得继续依赖全局 `archive.jsonl` 或“扫描最高 `vNNN`”推断状态。建议布局：

```text
results/three_tier_qualification/<experiment_id>/
  ledger.jsonl                         # 全调用账本，append-only
  state.json                           # 原子状态快照，含 event-chain head
  lineages/A1/proposer_visible/        # 显式白名单的 training-only artifacts
  lineages/A2/proposer_visible/
  private/selector/A1/                 # validation aggregate/private audit
  private/selector/A2/
  private/test/                        # unseal 后的 embargoed jobs
  frozen/v001/
  frozen/A1/
  frozen/A2/
```

`proposer.py` 必须接收显式 training-only artifact allowlist，不得递归扫描 lineage 或
results 根目录。rejected candidate 的 training trace 可以进入下一轮，但 candidate
source 不成为 parent，且 artifact 必须剥离 selector decision、validation score/reason；
这是允许的 training feedback，也构成 §4.1 所述受 look cap 限制的间接 selection channel。
每轮 proposal payload schema 固定为：

- 当前 accepted parent source（唯一待编辑父代）；
- 同 lineage、按 round 排序的 candidate source + training integer pass count +
  training failed traces，不含 accepted/rejected 标签；
- 当前 parent 的 training failures；
- 固定 Task/protocol description 与生成合同。

canary artifact、selector DTO、validation/test、另一 lineage、旧 R0/R1/R2 和人工备注均
不在 schema。contract repair 只得到当前 raw candidate 和通用 contract error；
instance-linter 命中不进入 repair prompt。

目录、symlink、sentinel 测试要证明 validation/test token 无法进入 proposal、repair 或
resume prompt。

`results/` 当前被 gitignore，正式状态不得只存在于将被删除的 worktree。runner 必须要求
显式 `--artifact-root`：`resolve()` 后不得位于 `.claude-manager/worktrees/`，不得经过
symlink，启动时必须通过 write + fsync smoke；tracked protocol/freeze manifests 与最终
机械分析另行提交。

### 4.3 评分输出

现有 `eval.py` 普通 summary 含 `per_task_passes`，逐题 JSON 含 task name、trace 和可见
pytest output，不能直接交给 selector。实现必须增加向后兼容的 exposure mode：

- `training`：完整输出进入显式 proposer-visible 路径；
- `selector_private`：raw 只落 private audit，调用者只得到窄类型 aggregate DTO；
- `sealed_test`：结果缓冲到 embargoed 路径，matrix 完成前 quiet。

评分语义、hidden judge、三遍、模型锁和防作弊不变。

cache identity 不是单纯 content hash。每个 invocation key 至少包含：

```text
experiment_id, cell_id, job_id, repeat_index, lineage_role,
harness_sha, benchmark-tree/manifest sha, evaluator/tool/schema/environment bundle sha,
resolved model identifier, TokenRouter endpoint identifier, exposure_mode, repeats
```

相同 source bytes 的 A1/A2、不同 cell 的 v001、以及同 cell 的 3 repeats 都禁止互相
去重；只有**同一个 invocation ID 的 crash recovery**可以复用带匹配 digest 的原子结果。

protocol bundle 使用排除自身 `bundle_digest` 字段后的 canonical JSON 计算，至少纳入
`eval.py`、`_eval_one.py`、`tools.py`、`harness_source.py`、`proposer.py`、Task/family
description、proposal/repair prompt templates、generation params、Anthropic SDK/依赖锁、
新 runner/selector/linter/analysis schema、resolved model identifiers 和不含密钥的
endpoint/config identifier。hosted model 只冻结 identifier/config，不虚构 model
binary hash。
scorer 为每个 job 建只读 content-addressed snapshot，并在 claim/dispatch 前校验。

---

## 5. 两条 lineage 与 selector

### 5.1 独立性

- canonical seed 固定为
  `harnesses/tddgen_hidden/v001/harness.py` 的 bytes；`A1`、`A2` 从该文件复制，
  bytes 与 SHA 必须完全相同，不能在多个历史 v001 中临时选择；
- 两条使用相同 training/validation、模型、参数、round cap 和 selector；
- 执行顺序预先固定，第二条不得根据第一条结果改 prompt、ε、轮数或停止规则；
- state、raw response、accepted history、trace、proposal 和 private selector ledger
  完全分开；
- A1 开始后，其能力分、training/validation 明细和 candidate source 对人也 embargo
  到 A2 lineage freeze；运行期只发布 budget/infra/terminal 状态，禁止人工据 A1
  表现干预 A2；
- 旧 R0/R1/R2 的 Harness、机制文字、trace 和分数不进入两条新 lineage。

### 5.2 固定 proposal 资源

每条 lineage 最多 4 个 semantic mutation rounds，即最多产生 v002–v005：

- 一个产生了可核验 raw response 的 semantic round，无论 accepted、rejected、
  contract-invalid、instance-invalid、no-op 或 duplicate 都消耗，不补额外 round；
- 每 round **全局**最多 1 个原 proposal + 2 个只依据 contract error 的 repair，
  合计最多 3 次 Sonnet dispatch；必须重构现有嵌套 `propose()` /
  `repair_candidate()` retry，不能让内外层各自再乘 3；
- Sonnet/评分 infrastructure interruption 的调用与预留全部计账；只允许在同 round
  剩余 dispatch slot 内恢复 raw，或对同 candidate hash 按旧规则最多 3 次重试
  pre-test evaluation cell。三次仍无有效结果则 lineage 记 `infra_incomplete`，不是
  “optimizer 不可重复”，也不生成新 candidate 掩盖故障；
- 每 lineage 最多 4 个**有效 validation decision looks**；infra-invalid validation
  attempt 计调用/预算但不产生 selector look，未通过前置门的 candidate 不调用 validation；
- 固定 4 rounds 来自本地证据：R2 首次在 v002 达标，R0/R1 的已观察中间峰值最晚首次
  出现在 v005；它是最低成本资格上限，不声称覆盖所有搜索随机性。

### 5.3 三套显式状态机

```text
CandidateState:
  proposing
    → proposal_failed | contract_invalid | instance_conditioned_invalid
    → contract_valid
      → duplicate_invalid | smoke_invalid | canary_invalid
      → train_done
        → train_rejected | regression_rejected
        → validation_done
          → accepted | validation_rejected | evaluation_infra_incomplete

LineageState:
  initialized → running
    → stopped_round_cap | stopped_confirmed_train_ceiling
    → incomplete_budget | incomplete_infra | incomplete_protocol
  stopped_* → lineage_frozen
  incomplete_* → audit_frozen_only

TestJobState:
  pending → started → completed_valid
                    → completed_infra_invalid | lost
  pending → cancelled

TestMatrixState:
  sealed → unsealed_running → complete_valid | aborted_incomplete
```

只有 CandidateState=`accepted` 的 candidate 能成为 parent；candidate 没有
`stopped/frozen` 状态。只有 `stopped_round_cap` 或
`stopped_confirmed_train_ceiling` 能产生资格 final；budget/infra/protocol fuse 只产生
`audit_frozen_only`，立即 pre-test incomplete/no-go，不得把当前 incumbent 当资格 final。

状态保存 attempt ID、candidate/parent SHA、accepted parent、round、locked set、budget、
所有调用 event ID 和 stop reason。`latest_version()`、目录名排序或相同 content hash
都不具有决策权；A1/A2 即使 source bytes 相同仍是两个不同、不可去重的预注册 lineage。

### 5.4 Instance-conditioned 静态门

首次 proposal 前，builder 必须从 training/validation/test 三池 manifest 的 union
机械生成并冻结
`forbidden_instance_tokens.json` 与 linter SHA：

1. 每个完整 `task_id`，例如 `BigCodeBench/341`；
2. 每个目录 basename，例如 `bigcodebench_341`；
3. 三池 `task_id` 中的数字部分只在固定 tagged pattern 中匹配：
   `\b(task|instance|problem|bigcodebench)\s*[#:/_-]?\s*<id>\b`；
4. 全部匹配先对 candidate source（包括 comments/string literals/内嵌 prompt）做
   Unicode NFKC + lowercase，再按冻结 exact-string/regex boundary 运行；
5. 从三池 stub AST 机械提取 target function symbol；只出现于一个 instance 的唯一
   symbol 纳入 exact-token 禁表，跨多个 instances 共享的通用 symbol 不纳入；
6. matcher、normalization、允许的通用文件名（仅 `solution.py` /
   `test_solution.py`）和空 allowlist 一起 hash 入 protocol manifest。

命中记 `instance_conditioned_invalid`，不允许人工豁免，也不把命中的 token 反馈给
contract repair；candidate 不计能力分但 round、Proposer 成本照常入账。
`task_func` 等跨实例共同符号、一般常量或语义相似规则不作主观 invalid，留给 final
集中度/source audit 作描述，避免看 candidate 后临时决定“唯一 literal”。

另设 source identity 门，同时计算：

```text
source_sha = sha256(exact source bytes)
semantic_sha = sha256(ast.dump(ast.parse(source),
                               annotate_fields=True,
                               include_attributes=False))
```

AST dump 自动忽略注释、空白和位置信息，但保留 prompt string 内容。任一 SHA 等于 parent
或本 lineage 任一历史 accepted/rejected/invalid candidate，即记 `duplicate_invalid`，
round/cost照计但不再运行 canary、training 或 validation，防止只改格式/注释后对同一
Harness 反复抽样碰运气。更深的等价变换无法由此证明，列为残余风险。

### 5.5 Training 严格提升门

seed 先在 training benchmark 正式 3 遍；3 个 repeat 的整数 pass counts 的**数值中位数**
记为 `T_parent_cached_count`（不选择某个同分 repeat vector）。每个 candidate：

1. full training quick 1 遍；
2. 若第一次为 16/16，在 validation 前追加 1 次完整 training ceiling confirmation；
   定义 `candidate_effective_count = min(first_count, confirmation_count)`；否则
   `candidate_effective_count = first_count`；
3. 必须以整数满足
   `candidate_effective_count >= parent_cached_count + 1`；
4. 平分、任务之间等量交换得失或下降都拒绝，不运行 validation；
5. accepted 后 `candidate_effective_count` 成为新 `T_parent_cached_count`。只有
   first/confirmation 都为 16/16 且随后通过 validation，才可早停。

quick 仍是搜索信号，不是正式结论；final 是否真正提高只认三遍 formal gate。

### 5.6 回归保护

- 初始 locked set：v001 在 training baseline 三遍中 3/3 通过的 instances；
- seed 是初始 accepted incumbent，但不计入后述连续计数；未锁 instance 只有在连续
  3 个**不同的新 accepted hashes** 的全部完整 training quick 中都通过才加入 locked
  set；rejected round 中同一 incumbent 原地停留不累计；
- locked set 单调增加，不因后续失败移除；
- candidate 任一完整 training quick（含 ceiling confirmation）若在 locked instance
  失败，按 manifest 顺序对全部失败 locked instances 各做且只做 1 次 training-side
  targeted confirmation；
- 两次连续失败才判 regression、拒绝 candidate，且不运行 validation；
- 任一 locked instance 二次失败即拒绝；targeted confirmation 只判回归，不改写 full
  quick aggregate，属于 training artifact，可进入同 lineage 的 proposer payload；
- Proposer 可看到 training failure，但看不到 candidate 被拒是因为 regression 还是
  validation。

这会保守地拒绝部分随机失败，但资格实验的目标正是证明能力可以累积而不是交换。

### 5.7 Validation 容忍门

v001 在 validation benchmark 正式 3 遍；3 个整数 pass counts 的数值中位数记为
固定 `V_seed_anchor_count`。lineage 初始化时显式设置
`V_parent_cached_count = V_seed_anchor_count`。
通过 training/lock 的 candidate 才运行 validation quick 1 遍。

固定：

```text
epsilon_count = 1
accept iff
  training strict-gain passed
  AND regression gate passed
  AND candidate_count >= V_seed_anchor_count - 1
  AND candidate_count >= V_parent_cached_count - 1
```

等价于
`candidate_count >= max(V_seed_anchor_count, V_parent_cached_count) - 1`。

- validation 只有否决权，不能因为 validation 上升而接受 training 不涨的版本；
- 不使用“历史最高 validation”作 anchor，降低 winner's curse；
- accepted candidate 的 validation quick count 成为新 `V_parent_cached_count`；
- `ε` 不根据 baseline 波动、拒绝率或中途结果调整；
- formal 运行中不得放宽 ε、并回 validation trace、切回单轨或追加 round。

### 5.8 停止与 final

只有两种**有效 lineage 停止**：

1. 4 rounds 用尽；
2. candidate 的 first/ceiling-confirmation 两次完整 training quick 都为 16/16，
   且通过 validation 成为 accepted incumbent。

不因 validation 趋势、test、人工判断或某个中间版本“看起来最好”停止。
budget/infra/protocol fuse 不是有效 stop：lineage 进入 `incomplete_*`，只作 audit freeze，
立即 pre-test incomplete，test 保持密封。

`final = 有效停止时最后一个 accepted incumbent`；若 4 rounds 都完成但从未接受，
final 是 v001。formal 失败只能产生 no-go，禁止回头挑中间版本。

---

## 6. Final 冻结与 test-once

### 6.1 Pre-test gates

P4 的 v001 training/validation baseline 各只运行一次 3 repeats：

- selector anchor 使用 3 个整数 pass counts 的数值中位数；
- formal comparator 复用同一 cell 的未舍入 pass matrix、mean 与 population std
  （现 `statistics.pstdev` 语义）；
- P5 不再运行第二套 v001，也不得在两套 baseline 中择优。

两条 lineage 有效停止并完成 per-lineage freeze 后，再运行：

1. 复用本协议内 P4 已完成且 hash 一致的 v001 baseline，新增
   A1-final、A2-final × training × 3 repeats；
2. 对每条 lineage 定义
   `G_train = raw_final_mean - raw_v001_mean`；必须
   `G_train >= 0.15` 且
   `G_train > max(pstdev(v001_per_repeat), pstdev(final_per_repeat))`；实际判定使用
   §1.5 的 `Fraction` 和 variance 平方比较；
3. 同样复用本协议内 v001 baseline，新增 A1-final、A2-final × validation × 3 repeats；
4. 对每条定义 `G_val = raw_final_mean - raw_v001_mean`，必须
   `G_val >= -0.05`。

只有 2/2 training gate 和 2/2 validation gate 全过才允许解封 test。任一失败：

- 写机械 no-go；
- test 34 题保持零调用，可留给新的冻结协议；
- 不允许基于 formal validation 回到 mutation 或改 selector。

pre-test formal cell 只要尚有 infra invalid，就先按冻结规则以同一 Harness/benchmark
hash 整格隔离重跑，最多 3 次；仍无有效 cell 则结论是 `pretest_incomplete`，不是能力
gate 失败。隔离的 contract/infra attempts 完整报告但不自动否定后续 go；任何 tamper
在任何阶段都触发全局停止复核。

### 6.2 Final registry

冻结分两层：

1. 每条 lineage 有效停止后立即写不可变 `lineage_freeze_entry`（source bytes/SHA、
   state/event head、parent、stop reason）；它不能因 formal 分数改变；
2. 两条 entry、P4/P5 valid formal cells/gates 与 §9.3 固定 preflight/fence
   前置条件全完成后，一次性创建 `global_final_registry`。只有后者可以把 test 从
   sealed 变为 unsealed。

global registry 记录：

- v001、A1-final、A2-final 的 source bytes 和 SHA-256；
- 两条 lineage freeze entries 和 event-chain heads；
- v001 baseline、A1/A2 formal train/validation result digests 与 gate decision；
- benchmark manifest、protocol bundle、resolved model/route、analysis code、
  bootstrap seed/RNG/quantile method 的 digests/config；
- 三个固定 route-preflight result digests、unseal 前 budget snapshot、
  `test_fence` 与 `test_stage_cap`；
- 完整 test cell/job matrix、固定 job order 与 max in-flight；
- `all_lineages_frozen=true`。

freeze 后任何一字节变化都使 registry 失效；只能重新设计实验，不能原地 repair。
registry 必须先在 persistent artifact root durable 落盘，并提交其 tracked digest，
才可调用 test。

### 6.3 一次性 test matrix

完整矩阵固定为：

```text
v001, A1-final, A2-final
  × 34 sealed test benchmark instances
  × 3 formal repeats
= 306 pre-registered jobs
```

“test 只评一次”定义为一次 atomic unseal event，内部仍保留冻结的正式三遍：

- 在首个 job 前原子写 `unsealed/started`；
- job order 固定为
  `sha256("moss-three-tier-test-job-v1\0" + instance_id + harness_role + repeat_index)`
  的升序，`max_in_flight=3`；worker 每次 durable claim 一个 pending job 后才 dispatch，
  禁止一次性 submit 306 个 futures；
- 每个 job 在 API dispatch 前 durable 写 `pending → started`；
- controller crash 后，仍属**同一 matrix ID / 同一次 unseal**；未 started 的 pending
  可按原顺序继续，不是第二次 matrix attempt；
- `completed` job 永不重跑；
- `started` 后若已有带 invocation/cache digest 的原子结果，恢复只补 terminal event；
  无可核验结果才记 `lost/infra-invalid`，**不得重发**；
- durable `started` event 同时冻结 `started_at_utc`、`deadline_at_utc`、child PID、
  boot ID 与 PID start ticks（防 PID 复用）；`deadline_at_utc =
  started_at_utc + 300s task timeout + 30s commit grace`；
  恢复时若原 child 已退出且无结果，立即记 `lost`；若仍存活，只等到该固定 deadline；
  deadline 到达后只接受在 deadline 前已 atomic replace + fsync、且 digest/finished_at
  均有效的结果，否则 kill/reap child 并记 `lost`。不得由操作者选择多等一会；
- 任一缺失/tamper/contract/infra 使整个主矩阵 `incomplete`，Builder no-go /
  experiment inconclusive；
- 首个永久 `lost` / tamper / contract / infra 后，停止 claim 新 job，等待已 in-flight
  jobs terminal，将全部仍 pending jobs durable 标记 `cancelled`，matrix 进入不可逆
  `aborted_incomplete`；不继续烧完矩阵；
- 不跨第二个 matrix attempt 拼接，不用另一版本补格；unseal 后 34 题整体视为已消费；
- `complete_valid` 前不向人、Proposer、Auditor 或调度器发布部分能力分；
  `aborted_incomplete` 后只发布状态、失败类别和成本，已完成的 partial capability
  scores 永不用于结论。

这比旧正式格“infra 整格重跑”更严格；旧规则继续适用于 pre-test train/validation，
不适用于 sealed test。

---

## 7. 指标、统计与过拟合归因

### 7.1 主统计量

对 test instance `i`、lineage `l`：

```text
d[l,i] = mean_3(final[l], i) - mean_3(v001, i)
Delta[l] = mean_i d[l,i]
Delta = (Delta[A1] + Delta[A2]) / 2
G_val[l] = formal_validation_gain[l]
G_val = (G_val[A1] + G_val[A2]) / 2
```

固定：

- 内部使用未舍入 fraction，展示时才乘 100；
- NumPy 固定 `2.1.3`，
  `rng = numpy.random.default_rng(20260728)`（PCG64）；
- 10,000 draws；
- 以 benchmark instance 为推断单位；
- 每 draw 用 `rng.integers(0, 34, size=34)` 有放回抽 instance index；抽中一个
  instance 时，将 v001、两条 lineage 和 3 repeats 整组带走；
- percentile 95% CI 使用
  `numpy.quantile(samples, [0.025, 0.975], method="linear")`；
- bootstrap index `0..33` 必须绑定 §3.3 已冻结的 domain-separated SHA 排序，
  analysis config 另记录 ordered task list digest；不得使用 filesystem、JSON object
  或 dictionary iteration order；
- 主 CI 只对 pooled `Delta`；个别 lineage 与 17/17 report blocks 只作约束/描述，
  不进行多重显著性择优。

3 repeats 降低 executor 随机性，但统计样本仍是 34 个 benchmark instances，
不是 102 次 task-run。

### 7.2 过拟合归因矩阵

| 观察 | 预注册标签 | 可以说什么 |
|---|---|---|
| 源码命中冻结 ID/path/tagged-ID matcher | `instance_conditioned_invalid` | 明确的 instance-conditioned candidate；不计能力分 |
| train 多过新题但 locked instance 连续回归 | `instance_tradeoff_rejected` | 为修局部实例破坏已掌握实例 |
| train strict gain 通过、validation 低于 ε 被拒 | `training_gain_validation_veto` | 与 training specialization、validation noise 或 stratum shift 均一致，不单作因果结论 |
| final train `>=0.15`、formal validation `<-0.05` | `training_benchmark_overfit_or_selector_failure` | optimizer/selector 未阻止 training benchmark specialization |
| `G_val>0` 且 `Delta<=0`，或 `G_val-Delta>=0.10` | `validation_conditioned_pattern` | 与 validation-benchmark overfitting 一致；只是 secondary diagnostic，不覆盖已冻结主 go/no-go |
| test `Delta>=0.05`、CI 下界 `>0`、两 lineage 都正 | `new_benchmark_sample_transfer` | 对一个新 BigCodeBench-Hard benchmark sample 的 pooled 迁移；两 lineage 均无负迁移 |
| 第二个独立来源也按同一 frozen finals 得到一致正效应 | `cross_benchmark_replication` | 与 Task-conditioned 机制一致的更强证据 |

行为集中度另报：

- 先定义 `d[i]=(d[A1,i]+d[A2,i])/2`、
  `positive_support=sum(max(d[i],0))`；
- `positive_support>0` 时，
  `max_instance_share=max(max(d[i],0))/positive_support`，否则记 `NA`；
- leave-one-instance-out 只重算 34 个 pooled point estimates，不重算/挑选 CI；
- `n_positive_instances = count(d[i] > 0)`；
- 逐实例 pass↔fail 翻转率。

收益集中在 1–2 个 instances 是 instance-level overfitting 的警告，不单独证明 Harness
记忆了实例；源码硬特判才作明确 invalid。

### 7.3 功效边界

旧 Q1 的 12-instance paired CI 半宽约 6.25 点。按 `sqrt(12/34)` 粗略外推，
34 instances 的半宽约 3.7 点；对 diffuse `+5` 点效应的粗略功效约 75%，不是保证。
同方差下约 40 instances 才接近常见的 80% 目标。

因此：

- CI 跨 0 只能判不明确；
- pooled bootstrap 会有意惩罚只来自 1–2 个 instances 的“增益”；
- 两条 lineage 是最低 repeatability 证据，不能可靠估计 lineage 方差。

---

## 8. Builder / specialization go-no-go

### Go：允许另立 Builder evolvability 协议

必须全部满足：

1. protocol、lineage state、formal train/validation 和 test matrix complete；
2. 全实验 0 tamper；frozen finals 与最终有效 formal/test matrix 为 0 contract violation、
   0 infra-invalid。预注册隔离的 proposal/canary/pre-test contract/infra attempts
   完整报告但不自动否定 go；
3. A1、A2 各自 training gain `>=0.15` 且严格大于 repeat variation；
4. A1、A2 各自 formal validation gain `>=-0.05`；
5. test `Delta>=0.05`、95% CI 下界严格 `>0`；
6. `Delta[A1]>0` 且 `Delta[A2]>0`。

允许的结论措辞：

> 在冻结的 BigCodeBench-Hard V1 sampling frames 下，validation-selector 约束的两条
> 通用 v001 lineage 都产生训练提升；两条在全新 34-instance test 上均无负迁移，
> pooled effect 达到预注册 transfer gate。该 optimizer 机制包具备进入 Builder seed
> evolvability 实验的资格。

Builder 实验必须使用新的 fresh test；本轮 34 题此后永久降级为已消费 benchmark，
不得再次声称 sealed。

### 主判定顺序与 No-go 分流

主判定按阶段条件树执行；按设计尚未调用的下游阶段记 `not_applicable`，绝不能记
`incomplete` 后吞掉一个正常的 pre-test no-go。secondary overfit tags 不覆盖主判定：

| 顺序 | 当前阶段所需条件 | 主判定 | 下一步 |
|---:|---|---|---|
| 0 | protocol/tamper 或两条 lineage required state 缺失/无效 | `experiment_incomplete_no_go` | 不作能力归因；test 未解封则仍 fresh |
| 1 | required training formal cell 缺失/无效 | `experiment_incomplete_no_go` | validation/test=`not_applicable` |
| 2 | training formal 完整，但任一 `G_train` 未过 §6.1 | `evolution_not_repeatable_no_go` | validation/test=`not_applicable`；修机制 |
| 3 | training 全过，但 required validation formal cell 缺失/无效 | `experiment_incomplete_no_go` | test=`not_applicable` |
| 4 | validation formal 完整，但任一 `G_val < -0.05` | `validation_tolerance_failed_no_go` | test=`not_applicable`；修 selector/回归保护 |
| 5 | train/validation 全过，但 global registry、budget fence 或固定 route preflight 未完成/失败，test 尚未 unseal | `experiment_incomplete_no_go` | test 仍 fresh；修前置条件后必须另立恢复/执行授权 |
| 6 | test 已 unseal，但 required test matrix 缺失/无效 | `experiment_incomplete_no_go` | 34 题已消费，不作能力归因 |
| 7 | test complete 且满足全部六项 Go | `builder_gate_go` | 另立 Builder 协议 |
| 8 | test complete，`Delta<=-0.05`、CI 上界 `<0`，且无 lineage `Delta>=0.05` | `harmful_transfer_no_go` | 强 harmful benchmark overfit 证据；修机制 |
| 9 | 其余所有完整 test 结果 | `test_inconclusive_no_go` | 包括 pooled 过线但一条 `<=0`、一正一负、`-0.05<Delta<0.05` 或 CI 跨 0；不进 Builder |

task-conditioned specialization / Q2′ 同样依赖本 go gate；否则比较的是不可靠 optimizer
产生的两个噪声 Harness。

`validation_conditioned_pattern`、集中度与 instance trade-off 只在主判定之后追加为
secondary diagnostics；例如 `Delta=0.06` 且 go 全满足时，即使
`G_val-Delta>=0.10` 也仍是 go + diagnostic，不会产生相互冲突的 no-go。

### Task-level 较强结论

本轮 go 仍不足以宣称 Task-level transfer。若要把结论升级为跨 benchmark：

- 在本轮 test 解封前，最好先冻结第二个独立 benchmark/data source 的来源、过滤与
  抽样算法；
- 使用完全相同的 v001/A1/A2 final hashes，不得在 Test-A 后 mutation；
- 两来源效应都 `>0`，无来源 `<=-0.05`，等权 pooled gain `>=0.05` 且 pooled CI
  下界 `>0`；
- 若第二来源在看完本轮结果后才选择，只能称后续 replication，不得伪装成同一轮
  预注册确认。

---

## 9. 预算、熔断与恢复

### 9.1 硬授权

基于 R1/R2 实耗和 evolved Harness 的高单价，旧整合案 35–60M 对应不同、更小的
矩阵范围，不适用于本方案扩大的 16/20/34 三层矩阵。本实验建议冻结：

| 预算分区 | executor tokens | 语义 |
|---|---:|
| global runtime preflight（candidate canary 计入各 lineage） | 0.5M | stage hard cap |
| A1 evolution（含 quick/canary/invalid/interrupted） | 16M | lineage hard cap |
| A2 evolution（同上） | 16M | lineage hard cap |
| formal training matrix（含唯一 v001 baseline） | 16M | planning reserve |
| formal validation matrix（含唯一 v001 baseline） | 17.5M | planning reserve |
| sealed test minimum ring fence | 34M | 前序绝不可借用的最低余额 |
| **总硬授权** | **100M** | 全实验不可超 |

Sonnet 另设调用门：

- 每 lineage 4 rounds；
- 每 round 最多 3 次（原 proposal + 2 次 contract-only repair）；
- 两条合计最多 24 次调用、最多 8 个有效 semantic proposals。
- interrupted dispatch 仍占 Sonnet call slot；若 raw response 已 durable 保存，恢复只解析
  同一 raw，不得再次调用。

所有 Sonnet/executor 调用都进入同一事件账本；100M 是 executor token 上限，不把
Sonnet 调用伪换算成 executor tokens。若用户无法在首次模型调用前授权 100M，回方案模式
缩设计；不得跑到中途再减题、降正式 repeats 或砍 A2。

A1/A2 各自不得借另一条的 16M。formal 16M/17.5M 是估算 reserve，可在两者之间使用；
所有前序阶段都不得侵占 test 34M。未消耗的 lineage/formal 额度返回全局余额，只能在
§9.3 动态 test fence 高于 34M 时补足；总计始终不得超过 100M。lineage hard cap
触发即 `incomplete_budget`，不是一个可拿去 formal qualification 的 final。

为使 executor 账本不依赖 generated Harness 自报的 `tokens`，`eval.py` 的 canonical
single-job API 必须在 import Harness 前安装 scorer-owned metered Anthropic wrapper：

- 固定 executor `claude-haiku-4-5`，Proposer `claude-sonnet-4-6`，均走
  `.env.local → config.py` 的 TokenRouter endpoint；manifest 记录 resolved identifiers
  与不含密钥的 endpoint ID；
- scorer 逐 executor SDK call 在 dispatch 前通过跨进程 budget coordinator 原子预留，
  terminal 后记录可信 input/output usage，并与 TokenRouter 可用 usage 对账；
- wrapper 只做透明 instrumentation，不改变 Harness 请求参数、step allocation、工具结果
  或冻结的 300s task timeout；本轮不新增 per-job call/token capability cutoff；
- 预算熔断是唯一例外：若**下一次内部 SDK call** 无法在 stage/global/test-fence 下完成
  预留，则该 call 不 dispatch，整个 evaluation job 记 `budget_incomplete`，不产生能力
  pass/fail。一个 job 可调用任意多次，只要每次调用都还有全局授权；
- Harness 只能通过冻结的 SDK/TokenRouter adapter 调模型；alternate client、直接网络和
  wrapper bypass 均为 contract violation，静态门与 runtime sentinel 双重阻断；
- runner 不得直接调用 `_eval_one.py` 或自行判分，所有 training/validation/test job
  都经 `eval.py` 唯一计分 API。

每个 executor SDK call 的 reservation 机械冻结为：

```text
payload_bytes = len(utf8(canonical_json(
  model + system + messages + tools + all generation parameters
)))
R_call = 4 * payload_bytes + 65_536 + requested_max_output_tokens
```

canonical JSON 排除 secret 值但保留等长占位符，整数与 Unicode 编码规则写入 protocol
bundle。该上界故意远大于 byte-level tokenizer 的输入上限，并覆盖固定 route framing；
`requested_max_output_tokens` 是原请求值，wrapper 不改写。P3 必须用冻结 route 的
最大结构 fixture 验证 `reported_input + reported_output <= R_call`，并证明所有模型
出口都经过 coordinator；任一项做不到，协议在首次正式调用前退回方案模式，不能把
100M 称为硬帽。

每次 call dispatch 前在同一文件锁内要求：

```text
global_charged + global_outstanding + R_call <= 100_000_000
AND stage/lineage charged + outstanding + R_call <= its frozen cap
AND (pre-test 时) global remaining after reservation >= active_test_reserve
```

`active_test_reserve=34_000_000` 直到 P5 算出 §9.3 `test_fence`，此后等于
`test_fence`。
formal training/validation 共享 `33.5M` pre-test formal pool；表中 `16M/17.5M` 是
计划分栏，不是彼此隔离的硬帽。terminal 且 usage 可信时只 charge actual、释放差额；
usage unknown 时 charge 全部 `R_call`。因此在上述 route accounting contract 内，
并发 calls 也不能越过 100M；不存在额外的 in-flight token overshoot。预算不足只产生
实验 incomplete，不把被截断执行计作任务失败。

test 解封前必须没有任何 outstanding reservation。三个固定 preflight 完成后定义：

```text
test_stage_cap = 100_000_000 - global_charged_at_unseal
```

并把 budget snapshot 与该 cap 写入 global registry。必须先满足
`test_stage_cap >= test_fence`；解封后所有剩余 executor 授权只属于 test，
每次 test SDK call 同时受 `test_stage_cap` 与 100M global cap 约束。`test_fence`
只是最低开跑条件，不是运行中遇到后立即截断的较小 cap。

### 9.2 统一账本

append-only ledger 是唯一权威 write-ahead event log；`state.json` 只是可由 ledger
重建的原子快照，不得反向覆盖 ledger。evaluation job、Proposer dispatch 与 job 内每个
executor SDK call 都有独立 `event_id`/parent-child relation，并通过追加 transition
events 表达，而不是原地修改 JSONL。每次 dispatch 前写：

```text
event_id, parent_event_id, event_kind, experiment_id, lineage, stage, candidate_hash,
benchmark/protocol/model hashes, reserved_tokens,
status=pending→started→terminal, reported_usage, charged_usage
```

以下全部计费/计数：

- smoke、canary、quick、formal；
- failed contract repair、invalid candidate；
- capability failure、infra failure、quota/5xx；
- timeout、interrupted、missing result；
- validation rejected candidate；
- test lost job。

写入顺序固定为：

1. 加文件锁；
2. 对 SDK call 先检查 §9.1 不等式并 append `reservation + started` transition；
   其他 invocation append `started`（均含 monotonic sequence、previous-event hash），
   `flush + fsync` ledger；
3. atomic replace derived snapshot，`fsync` snapshot 与 parent directory；
4. 解锁；
5. 才允许 SDK/API dispatch。

child/raw result 用临时文件 + atomic replace，必须携 invocation/cache digest。恢复时：

- ledger=`started` 且存在可核验 result/raw：只补 terminal event并重建 snapshot；
- pre-test evaluator 无结果：按同 cell 最多 3 次规则处理；
- sealed test 无结果：记 `lost`，永不重发；
- proposer raw 已存在：从 raw 继续 parse/contract gate，不再发 Sonnet。

若 SDK call 中断后 usage 不可知，预算账按该 call 的 `R_call` 计
`charged_usage`，不能记 0；evaluation job 本身不另造 token reservation，token 总额由
其全部 child-call events 唯一求和。若可信 terminal usage 超过 `R_call`，记
`route_accounting_contract_invalid` 并全局停止复核，不得继续使用该 reservation 公式。
event ID 幂等；锁、fsync、atomic snapshot 和 concurrent append 均须离线 fault-injection
测试。

### 9.3 Test fence

P5 valid formal 完成后，对 `h ∈ {v001,A1-final,A2-final}` 定义：

```text
r_train[h] = metered_tokens(h, formal_train) / (16 * 3)
r_val[h]   = metered_tokens(h, formal_validation) / (20 * 3)
r[h]       = max(r_train[h], r_val[h])
projection = 34 * 3 * sum_h r[h]
test_fence = ceil(max(34_000_000, 1.5 * projection))
```

只使用 exact frozen hash 的有效 formal cells；不用 rejected candidate 或 quick rate。
test 解封前必须同时满足：

- 全局剩余 executor budget `>= test_fence`；若 fence>34M，只能使用前序未消耗且总授权
  仍≤100M 的余额；
- manifest 预先列出的**恰好 3 个** sequential non-test preflight jobs
  （固定 synthetic/consumed fixture、v001、顺序、`max_in_flight=1`）全部首次有效；
  任一失败即不解封，不再追加 job 凑“连续 3 个”；
- 所有 pre-test SDK calls 已 terminal、`global_outstanding=0`，并按 §9.1 机械计算
  `test_stage_cap >= test_fence`；
- 全部 final/benchmark/protocol hashes 复验一致。

不足则不解封，报告 `budget_precondition_failed`，test 保持 fresh。

### 9.4 熔断

- pre-test train/validation/evolution evaluation：同 candidate/cell hash 的 infra attempt
  最多 3 次；仍失败则对应 lineage/experiment incomplete；
- 任一阶段累计 3 个 shared quota/5xx：全局熔断，不启动新 job；
- test unseal 后任何 quota/shared-gateway/dispatch 不确定或其他永久 invalid：
  按 §6.3 立即停止 claim、等待 in-flight、cancel pending，进入
  `aborted_incomplete`；started job不重跑；
- test 下一次内部 SDK call 无法通过 §9.1 原子 reservation 时，budget coordinator
  拒绝 dispatch，并按 §6.3 的永久 invalid 流程 deterministic abort；已作
  outstanding reservations 不会突破 100M，不能事后改题或 repeats。

---

## 10. 有效性风险

| 风险 | 影响 | 预注册处理 |
|---|---|---|
| validation 是旧 score-exposed stratum | selector 可能适配已知 benchmark 口味 | 不把 validation 当无偏结论；只认 fresh test |
| validation 与 train/test 非严格 iid dependency stratum | selector signal 可能偏移 | 在结果中显式报告；不扩大 Task 结论 |
| parent identity 泄漏 selection bit | Proposer 可间接感知是否换父代 | 不传 score/reason；最多 4 looks；两 lineage 隔离 |
| quick 单遍噪声 | 假提升/假回归 | training 16 扩容、strict +1 instance、locked confirmation、formal 3 遍 |
| 固定 validation 被多次查询 | validation overfitting | validation 只否决、ε 固定、look cap=4、sealed test |
| test 同一数据来源 | 不能证明完整 Task transfer | 结论限于新 benchmark sample；另做跨来源 replication |
| 两条 lineage 太少 | 无法估计 lineage variance | 只作最低资格；不外推所有 seed |
| Harness token 膨胀 | 预算不足或低效 gain | 100M fence；报告质量—成本 Pareto，不以复杂度作正证据 |
| test-once 遇 infra | 主矩阵可能永久 incomplete | test 前 3-job preflight、34M fence；started 不重跑 |
| raw state 位于 disposable worktree | 中断/清理丢证据 | 正式 artifact root 必须持久；hash manifest tracked |

---

## 11. 可直接进入执行模式的实施步骤

每一步只有满足绿色出口才进入下一步。

### P0：Baseline 与测试先行

1. 先运行当前全部离线测试并记录 baseline；
2. 在改实现前先写以下失败测试：

- split/manifest：互斥、机械顺序、文件 hash、无 extras/symlink；
- proposer visibility：validation/test sentinel 不进入 proposal、repair、resume；
- lineage isolation：A1/A2 不能跨读；seed bytes/SHA 相同；
- selector boundary：整数/Fraction 比较、`+1/16`、`ε=1/20`、首轮 parent
  初始化、ceiling min-count、平分拒绝、回归锁、rejected 不成 parent；
- linter/identity：三池 forbidden union、NFKC/boundary、source/semantic duplicate；
- stale cache：§4.3 任一 key 字段变化使缓存失效，同 bytes 不跨 lineage/cell/repeat 去重；
- invocation：旧 JSON 不得在新 subprocess 失败时冒充 pass；
- ledger/recovery：WAL 写序、fsync fault injection、raw/result commit gap、
  `R_call` 公式、并发原子 reservation、unknown usage；
- scorer metering：Harness 自报 tokens 不可信、SDK call 由评分器透明计量、
  timeout/unknown usage 入账，并断言计量层不改变请求参数、控制流或 runtime contract；
- freeze/test-once：未全 freeze 禁止 unseal；freeze 后改字节拒绝；固定顺序/
  `max_in_flight=3`；started deadline/PID-reuse；不重跑；首个永久 invalid cancel pending；
- embargo：`complete_valid` 前 stdout/公开路径无逐题结果；
- statistics：精确 Fraction gate/variance、固定 instance order、fixed RNG/quantile、
  分阶段穷尽判定树；
- legacy：现有 path guard、hidden redaction、model lock、tamper、正式 3 遍全部不变。

绿色出口：旧测试仍绿，新测试按预期为红；零 API。

### P1：核心状态机与隔离实现

1. 新增独立 `scripts/three_tier_runner.py`，不改旧轮历史 runner 的语义。
2. 实现 Candidate/Lineage/Test 三状态机、WAL ledger 和 derived snapshot。
3. 在 `eval.py` 增加 canonical single-job/plan API、exposure mode、metering、
   invocation/cache digests、atomic result；runner 不直接判分。
4. `proposer.py` 改为显式 payload schema，并把整个 round Sonnet dispatch 总数收紧为 3。
5. 实现 typed selector DTO、locked state、deterministic linter/identity gate、
   global/per-lineage budgets、freeze/test scheduler。

绿色出口：P0 核心红测转绿，全部 legacy 回归仍绿，fake evaluator crash/recovery E2E 通过；
零 API。

### P2：Benchmark builder（同样测试先行）

1. 先补 builder/manifest 的红测，再实现机械 builder；
2. 构造 training 16、validation 20 的不可变 views，不修改历史 benchmark；
3. 物化 reserve 34，执行同 importer/oracle/flaky/依赖门禁；
4. 生成三池互斥、逐文件 hash、exposure history、forbidden union、report block、
   protocol bundle 与 private test job manifest；
5. runtime verifier 在 snapshot 创建及每个 job claim/dispatch 前校验。

绿色出口：34/34 fresh test 可重建，三池交集为空，全部离线测试绿。

### P3：协议冻结与 runtime preflight

1. 在首个模型调用前同步 README/TEST/CLAUDE（AGENTS symlink 自动同步）；
2. 提交代码、题池、manifest、本文冻结值与 protocol bundle；
3. 核验用户已批准 100M hard authorization；
4. 运行 manifest 固定的 runtime/model smoke 与 consumed/synthetic canary；
5. 用最大结构 route fixture 验证 §9.1 reservation 上界、唯一模型出口、统一账本、
   熔断和 persistent/private/embargo 路径。

绿色出口：0 contract/tamper/infra，且预算授权满足；否则停。

### P4：Baseline 与两条 lineage

1. v001 × training/validation 各 3 遍；
2. 按固定顺序完成 A1 的 4-round state machine；
3. 写 A1 lineage freeze entry，对人只发布 infra/budget 状态；
4. 独立完成 A2，不读取 A1；A2 freeze 前 A1 能力结果继续 embargo；
5. 写 A2 lineage freeze entry。

绿色出口：两条均为有效 stop 且 freeze entries 完整；budget/infra/protocol fuse 则
`experiment_incomplete_no_go`，不进入 P5。

### P5：Pre-test qualification

1. 复用 P4 v001 baseline，运行 A1/A2 × training × 3；
2. 机械检查 2/2 `G_train>=0.15` gate；
3. 若通过，复用 P4 v001 baseline，运行 A1/A2 × validation × 3；
4. 机械检查 2/2 `G_val>=-0.05` tolerance gate。

绿色出口：两门全过才进入 P6；否则 test 不调用。

### P6：一次性 sealed test

1. 复验 final/benchmark/protocol hashes；
2. 检查 34M / 动态 1.5× fence 和 3-job route preflight；
3. 原子 unseal 306-job matrix；
4. 只恢复 pending，永不重跑 started/completed；
5. matrix 全 terminal 后一次性发布 summary。

绿色出口：完整有效 matrix；否则 `incomplete`。

### P7：机械分析与交付

1. 固定 seed bootstrap、go/no-go、过拟合归因矩阵；
2. 报告 per-lineage、17/17 blocks、集中度、翻转率、validation reject 和成本；
3. 更新 RESULTS/PROGRESS，并按实际实现/结果补充 README/TEST/CLAUDE；
4. 若 go，另写 Builder evolvability 冻结方案；若 pre-test no-go，test 仍 fresh；
   若 test 已解封后 incomplete/no-go，则 34 题已消费。两种情况分别按分流回方案模式。

---

## 12. 与旧文档的关系

| 文档 | 状态 | 关系 |
|---|---|---|
| `2026-07-27-hidden-final-verification-round.md` | 历史冻结、已执行 | evaluator/hidden/runtime 基础合同继续有效 |
| `2026-07-27-q1-independent-lineage-confirmation.md` | 历史冻结、已执行 | 提供旧 repeatability/external 证据，不回写 |
| `2026-07-27-q2-paired-feedback-confirmation.md` | 历史冻结、已执行 | 本轮 validation20 的两个 V1 block 来源；旧结果不复用 |
| `2026-07-28-next-round-integrated-plan.md` | 方向文档，第二阶段已被本文替代 | Builder 四谱系合并实验取消 |
| `2026-07-28-next-round-experiment-plan-v2.md` | 并发产生的历史方向文档，已被本文替代 | 仍混合 Builder seed 与 optimizer，且含未冻结跨源梯度；不执行 |
| `2026-07-28-round3-design-directions.md` | 历史方向文档 | Builder/Q2′ 前置条件改为本文 go gate |
| 本文 | 待批准 | 下一轮唯一资格协议来源 |
