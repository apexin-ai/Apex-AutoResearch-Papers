# Q1 全新留出与独立进化谱系确认实验

> 状态：已执行并终局（2026-07-28）；结果见 `RESULTS.md` 第五轮与
> `PROGRESS.md`“Q1 独立谱系与 external 确认”。本实验独立确认 Hidden Final Q1，
> 不修改旧结果。

## 1. 问题与结论单位

旧 Q1 只有一条 tdd 谱系：train `75.0%→95.8%`，旧 val `56.7%→53.3%`，验证变化位于
`(-5,+5)` 灰区。本实验同时检验：

1. 从相同 v001 和相同 train 出发，进化能否在独立谱系中重复产生 ≥15 点训练提升；
2. 满足训练前提的谱系，在此前从未运行过模型的新任务上平均提升还是下降。

## 2. 全新任务来源与环境冻结

数据源继续固定为 `bigcode/bigcodebench-hard` v0.1.4、commit
`298d2cc7b96612e15e47313c3603ee124cee0c1f`、Parquet SHA-256
`73a4270b43feb81abefad7bb1b592937c768ea45c3263bedc1cabd30a9a6ce79`。

在原冻结环境上只新增以下固定依赖：

- `matplotlib==3.9.2`
- `scipy==1.14.1`
- `scikit-learn==1.5.2`
- `seaborn==0.13.2`

设置 `MPLBACKEND=Agg`。候选 row 的 `libs` 必须是“旧 manifest allowed libs + 上述四个顶层
import”的子集；不得因依赖的传递安装临时扩大白名单。继续排除网络、进程、GUI 和既有
`SIDE_EFFECT_BLACKLIST`。

排除所有曾进入以下集合的 task id：

- 旧 38 道 qualified/formal/reserve；
- 旧 5 道 canary；
- Q2 的所有配对视图（与旧 val id 相同）。

对剩余 row 执行与旧隐藏池相同的 V1 门禁：stub hidden 失败、oracle visible 通过、
oracle hidden 连续两次通过、结果不 flaky。通过者按 `sha256(task_id)` 升序，机械冻结：

- 前 4 道：`benchmarks/q1_external/canary`；
- 后 12 道：`benchmarks/q1_external/val`；
- 其余只记录 reserve id，不生成正式任务。

manifest 保存环境包版本、白名单哈希、剔除原因、顺序和每个文件哈希。canonical solution
不落盘。样本和本文提交后才允许首次模型调用。

## 3. 难度 canary

通用 v001 在 4 道 canary 上单遍运行，0 tamper/contract/infra 为有效：

- 1–3/4 PASS：冻结难度，继续；
- 4/4：天花板，停止本实验，不移动题、不改可见级别；
- 0/4：地板，停止本实验；
- capability failure 正常计分，不换题。

canary 结果不得进入正式外部 val 分数。

## 4. 三条独立谱系

- R0：既有 `tddgen_hidden/v001→v005`，完整历史冻结复用；
- R1：`harnesses/tddgen_hidden_r01/v001`，起点与通用 v001 逐字相同；
- R2：`harnesses/tddgen_hidden_r02/v001`，起点与通用 v001 逐字相同。

R1/R2 都只使用既有 `benchmarks/tddgen_hidden/train` 8 题。各自：

- quick train 每版 1 遍、并发 4；
- 最多 6 个改进轮（v001 + 最多 v002–v007）；
- quick train 达 100% 时提前停止；
- Proposer 固定 `claude-sonnet-4-6`，只见该谱系自身代码、train 分数和失败 trace；
- 不共享另一谱系的代码、机制、分数、trace 或原始响应；
- 合同失败只允许使用候选和合同错误修复，最多 3 次；
- final 是按停止规则得到的最后版本，不得根据外部 val 选版本。

R1/R2 顺序执行，避免共享网关拥塞；顺序不构成信息传递。每条最多 6 个成功提案，合计最多
12 个；实际 API 调用含合同修复最多 18 次。生成原文、版本谱系和 quick 结果分别落盘。

## 5. 正式矩阵与主指标

所有 Harness 冻结后再开正式格。旧有效结果复用：

- v001 old train =75.0%；
- R0/v005 old train =95.8%。

新增 6 格，每格 3 遍、并发 4：

1. R1-final × old train；
2. R2-final × old train；
3. v001 × external val；
4. R0-final × external val；
5. R1-final × external val；
6. R2-final × external val。

按谱系 `r` 定义：

- `train_gain(r) = final_train(r) - v001_old_train`；
- `external_gain(r) = final_external(r) - v001_external`。

谱系训练前提：`train_gain >= +15` 点且大于三遍波动。只有满足前提的谱系进入外部泛化聚合，
但所有预注册格照常报告，不能按外部分数挑谱系。

主判定：

- 少于 2/3 谱系满足训练前提：**进化不可重复**，不判泛化/过拟合；
- 至少 2/3 满足时，以满足前提谱系的 task-paired external gain 等权平均为主效应；
- **可重复泛化**：平均 `>= +5` 点，固定 seed `20260727`、10,000 次“task 分层、谱系成组”
  bootstrap 95% CI 下界 `>0`，且无合格谱系 `<=−5`；
- **可重复过拟合**：平均 `<=−5` 点、95% CI 上界 `<0`，且无合格谱系 `>=+5`；
- 其余：**不明确**。

次指标：每条谱系的 train/external gain、版本数、quick 曲线、每任务变化和旧 val 结果。次指标
不得改写主判定。

## 6. 生成物门禁

每个新 Harness 在进入下一版 quick eval 前必须经过：

1. 原始响应保存；
2. 完整外层代码块提取；
3. compile/AST/冻结 MODEL、签名、import、工具参数和返回类型合同；
4. fake-tools 离线 smoke；
5. old train 首题单遍真实 canary；
6. 通过后才运行完整 quick train。

同一候选的 canary capability failure 允许进入 quick train；harness/contract/tamper/infra
不允许。任何新发现的合同边界先写回归测试。

## 7. 调度、预算与恢复

阶段顺序严格冻结：

1. 安装依赖、生成并提交 external pool；
2. v001 external canary；
3. R1 完整进化并冻结；
4. R2 完整进化并冻结；
5. 六个正式格受控并行：train-R1、train-R2、external-control 三 lane，各 lane 一格；
6. 机械分析，不再调用 Proposer。

预算：

- 两条新谱系 quick executor：期望 5–8M；
- 六格正式 executor：期望 8–12M；
- canary：期望 <0.3M；
- 本实验全部新增 executor 硬上限 **24M tokens**；
- Sonnet：最多 12 个成功提案、18 次含合同修复调用。

每个正式格开跑前预留硬上限 1.5 倍。单格 infra 整格隔离重跑；同格第 3 次 infra 失败停止。
任一格 ≥3 个 quota/shared-gateway 错误全局熔断。有效格永不重跑，不跨尝试拼接。

## 8. 信息隔离与解释上限

- external val 的任何分数、trace、任务文本都不得进入 Proposer 或版本选择。
- 新依赖任务仍来自同一 BigCodeBench-Hard 版本，不是跨数据源复制；确认结论只覆盖该分布。
- R0 的旧谱系不是与 R1/R2 同时生成；分析必须同时报告“含 R0 三谱系”及“仅新 R1/R2”
  的敏感性，不得隐藏时间批次差异。
- 若 canary 停止、谱系不可重复或主 CI 跨 0，结论保持受限，不新增事后任务或轮次。
