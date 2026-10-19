# Q2 同题配对反馈形态确认实验

> 状态：已执行并终局（2026-07-27）；结果见 `RESULTS.md` 第四轮与
> `PROGRESS.md`“Q2 同题配对消混淆确认”。该实验是 Hidden Final Q2 的独立消混淆
> 确认，不修改旧实验、旧判定线或旧结论。

## 1. 研究问题与识别对象

旧 Q2 直接比较两个题池的绝对通过率；tdd val 的 v001 基准为 56.7%，spec val 只有
16.7%，所以 raw 主场差混入了题目难度。本实验只问：

> 已在 V1 训练集产生强专化的 tdd v005，相对通用 v001 的增益，是否在“有一个可见行为
> 测试”时显著高于“只有 import/callable 冒烟”时？

它不识别任务语义、bug 类型或 Builder 能力。

## 2. 冻结样本与唯一处理变量

使用旧正式池的**全部 20 道 val 任务**，不按旧结果筛题：

- block A：`tddgen_hidden/val` 的 10 道任务；
- block B：`specgen_hidden/val` 的 10 道任务。

每个底层任务生成两个配对版本：

- V0：只暴露 import/callable 冒烟；
- V1：暴露官方源码顺序的第一个行为测试。

同一任务的两个版本必须满足：

- `solution.py` 逐字相同；
- `_hidden/test_hidden.py` 逐字相同；
- entry point、依赖、超时和最终评分逐字相同；
- 只有 `test_solution.py` 不同；
- V0/V1 oracle 均通过可见测试，stub 均不能通过完整隐藏测试；
- manifest 记录每个文件 SHA-256 和 pair id。

配对产物写入：

- `benchmarks/q2_paired/tdd_val_v0`
- `benchmarks/q2_paired/tdd_val_v1`
- `benchmarks/q2_paired/spec_val_v0`
- `benchmarks/q2_paired/spec_val_v1`

旧 `tddgen_hidden/val` 必须与新 block A/V1 的三个题目文件哈希完全一致；旧
`specgen_hidden/val` 必须与新 block B/V0 完全一致。这样可机械复用已有效的旧格，
而不跨不同协议拼接结果。

## 3. 2×2 比较与结果复用

主 Harness：

- G：通用 `tddgen_hidden/v001`；它与 spec v001 的 SHA-256 相同；
- S：tdd 专化 `tddgen_hidden/v005`；其 Q1 train 提升 +20.8 点，满足专化前提。

spec v007 因 Q1 train 提升为 0，不满足专化前提，不进入主比较，也不为本实验重新挑版本。

每个 block 都有 `Harness(G/S) × Feedback(V0/V1)` 四格。以下有效结果按文件哈希复用：

- block A/V1：G=56.7%，S=53.3%；
- block B/V0：G=16.7%，S=20.0%。

新增四格：

1. G × block A/V0；
2. S × block A/V0；
3. G × block B/V1；
4. S × block B/V1。

每格仍为 3 遍、并发 4、`claude-haiku-4-5` + TokenRouter。不得重跑或覆盖复用格。

## 4. 主指标与冻结判定

对 block `b`、反馈 `f`，记三遍任务级平均通过率为 `score(H,b,f)`，专化 Harness 相对
通用 Harness 的增益为：

`gain(b,f) = score(S,b,f) - score(G,b,f)`

block 内反馈交互效应：

`interaction(b) = gain(b,V1) - gain(b,V0)`

主指标为两个等规模 block 的等权平均：

`interaction_all = (interaction(A) + interaction(B)) / 2`

不以任何 V0/V1 raw 通过率差作为主证据。以 task 为重采样单位、固定 seed `20260727`、
10,000 次 paired bootstrap，计算 `interaction_all` 的 percentile 95% CI；同一 task 的
Harness/反馈/三遍结果始终成组重采样。

冻结三分判定：

- **确认反馈形态专长**：`interaction_all >= +10` 点、95% CI 下界 `> 0`，且 A/B 两个
  block 的 interaction 均 `>= 0`；
- **方向反证**：`interaction_all <= 0`；
- **不明确**：其余情况。

次指标仅用于诊断：两个 block interaction、每格三遍波动、每任务四格结果、V1/V0 的
绝对难度变化。不得用次指标推翻主判定。

## 5. 生成物门禁与 canary

模型调用前：

1. 从冻结 parquet/旧 manifest 重建 V0/V1 可见测试；
2. 验证 20 对任务的非处理文件逐字一致、配对哈希和旧格复用哈希；
3. 在全新临时目录验证 stub hidden 失败、oracle visible/hidden 通过；
4. 跑现有评分、防作弊、Harness 回归测试；
5. 提交 benchmark、manifest、分析脚本、runner 与本文，之后不再改样本和判定线。

真实 canary：新增四格各取其 block 按 SHA-256 排序的第一题，单遍、并发 1。PASS 或
capability 均为有效；任何 tamper/contract/infra 错误隔离并暂停，不进入正式格。

## 6. 正式调度、预算与恢复

两 lane 受控并行，错开 30 秒；每 lane 只允许一个活动格：

- G lane：G×A/V0 → G×B/V1；
- S lane：S×A/V0 → S×B/V1。

全局最多 2 格、8 个 executor 请求。单格 infra 只暂停该 lane；同一格第 3 次 infra
失败则停止。一个格出现至少 3 个 quota/shared-gateway 错误时触发全局熔断。有效格永不
重跑；无效格整格隔离后从头跑，不跨尝试拼接。

依据旧正式格：

- G 两格预计 0.7–1.0M tokens；
- S 两格预计 2.8–3.5M tokens；
- canary 预计不超过 0.25M。

本实验新增有效正式预算上限冻结为 **7.0M executor tokens**；每个活动格启动前仍预留其
硬上限的 1.5 倍。预算不足或实测显著越过预估时暂停，不自行放宽。

## 7. 结果解释上限

- 本实验使用的是导致设计修订的旧 val 任务全集，所以是“同池消混淆确认”，不是完全独立
  的外部复制；不得使用“最终证明”措辞。
- 若确认，只能说 tdd v005 相对通用 Harness 的效果依赖可见反馈形态。
- 若方向反证，只反证该 v005 的预期方向，不证明所有 task-conditioned Harness 都无效。
- 若不明确，下一步应增加全新底层任务，而不是继续在这 20 道题上加重复。

## 8. 执行期基础设施纠错（首次正式格后、重跑前冻结）

首次 G/S×A/V0 两格均在同一任务的 3/3 repeats 报 `env_error`。本地审计证明候选代码删除
测试所需文件，使断言失败后 teardown 再抛 `FileNotFoundError`；pytest `returncode=1`，
属于候选能力失败。旧分类器仅因摘要含 `errors` 就误判基础设施错误。

在不接触模型、不给 Harness 隐藏反馈的前提下，冻结通用修复：

- pytest `returncode=1`（test call/setup/teardown error）一律为 capability；
- `returncode=-1/2/3/4/5`（硬超时/中断/内部/用法/无测试）为 infrastructure；
- `ERROR collecting`、`INTERNALERROR` 继续为 infrastructure；
- redacted `n_failed` 取 pytest `failed` 与 `errors` 计数的较大值，避免同一 test failure 与
  teardown error 双计，也避免纯 runtime error 显示为 0 失败。

两份首次完整格继续隔离，不重分类、不拼接。回归测试和本修订提交后，G/S×A/V0 均从头
重跑三遍；Harness、任务、模型、预算、主指标和判定线不变。
