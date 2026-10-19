# Moss 实验一审计报告：`aaf43ab` 无重试正式复跑

报告日期：2026-08-29
正式运行日期：2026-08-28
代码版本：`aaf43abdcf5bacedc38bf55de6194e731f8b7aef`
Campaign：`main-aaf43ab-noretry-20260828-v1`
执行机器：AWS EC2 `18.181.235.110`

## 1. 先说结论

这次正式复跑已经自然结束，EdgeBench 与 ALE-Bench 的 18 条 lineage 都遵守了预先固定的规则：遇到 API、答案格式、Harness 执行或冻结错误后，不 retry，也不 resume 失败轮次。

本次能够确认三件事：

1. Builder 确实可以提交新的下层 Harness，而不只是给 Solver 一段临时答题建议；
2. 新 Harness 会在下一轮被 Python 执行链实际采用，并且有两个新 Harness 真正进入官方 evaluator 获得分数；
3. 放松后的通用门禁没有把所有 Harness 修改锁死。

但本次**没有完成实验一核心假设的有效验证**：

- 没有任何 lineage 展示“新 Harness 在同一 instance 上持续提分”；
- 两个进入 evaluator 的新 Harness 分数都低于各自的 H0；
- 其余新 Harness 第一次执行时即失败，无法形成可冻结的高分 Harness；
- 只有 ALE S1 完成 freeze 和 3×3，但 A/B/C 冻结出的三个 Harness 哈希完全相同，都是初始 H0，因此矩阵只是同一 H0 的随机重跑，不能作为 Harness 专门化或跨题下降证据。

因此，对本次 campaign 最准确的判断是：

> Moss 的“Builder 提案 → 通用门禁 → commit → 下一轮采用新 Harness → evaluator”链路已经跑通；但当前新 Harness 的可执行稳定性不足，实验数据尚不能支持“Harness 会针对单个 instance 专门化”的论文主张。

## 2. 固定实验口径

| 项目 | 固定设置 |
|---|---|
| Benchmark | EdgeBench、ALE-Bench |
| Instance | 每个 benchmark 固定 A、B、C 三题 |
| Seed | S1、S2、S3 |
| 单条 lineage | 最多 8 轮 |
| 上层 Builder | `gpt-5.6-sol`，`reasoning_effort=high` |
| 下层 Solver | `gpt-5.6-sol`，`reasoning_effort=high` |
| API | Responses API，流式返回 |
| Provider 重试 | `provider_attempts=1` |
| 失败策略 | 不 retry；不 resume；后续槽位记为 `IncompleteRoundError` |
| 结构变化判定 | `builder_status=committed` 且 `next_harness_sha256 != harness_sha256` |
| Freeze | 从各自 lineage 的有效正式分数中冻结候选 |
| Cross-test | 同一 seed 的 A/B/C 都冻结成功后才运行 H0 与 3×3 |

固定题目：

| Benchmark | A | B | C |
|---|---|---|---|
| EdgeBench | `apple_incremental_game` | `molecular_self_assembly` | `treant_forest` |
| ALE-Bench | `ahc024` | `ahc026` | `ahc011` |

每一轮的真实流程为：

```text
当前 Task Harness Ht 做题
→ 官方 evaluator 返回公开分数和公开状态
→ Builder Harness 读取允许的信息并提出 Ht+1
→ 固定 Python 做结构检查、Contract Skill 绑定和 probe
→ 通过则 commit Ht+1；不通过则保留 Ht
→ 下一轮实际执行 workspace 中已提交的 Harness
```

本报告不把以下情况算作 Harness 进化：

- 同一个 Harness 多次生成不同答案导致分数波动；
- Builder 只产生建议但候选未通过门禁；
- `next_harness_sha256` 没有改变；
- 新 Harness 已提交但从未在下一轮真正执行。

## 3. 整体完成情况

| Benchmark / Seed | A/B/C evolve | Freeze | H0 / 3×3 | 终态 |
|---|---|---|---|---|
| ALE S1 | 三条均自然终止 | A/B/C 均完成 | 完成 3 个 H0 与 9 格 3×3 | `completed` |
| ALE S2 | 三条均自然终止 | A、B 完成；C 无有效候选 | 未运行 | `freeze_failed` |
| ALE S3 | 三条均自然终止 | A 无有效候选 | 未运行 | `freeze_failed` |
| Edge S1 | 三条均自然终止 | A、B 完成；C 无有效候选 | 未运行 | `freeze_failed` |
| Edge S2 | 三条均自然终止 | A 无有效候选 | 未运行 | `freeze_failed` |
| Edge S3 | 三条均自然终止 | A 无有效候选 | 未运行 | `freeze_failed` |

全 campaign 的核心计数：

| 指标 | 数量 |
|---|---:|
| 固定 lineage | 18 |
| evaluator 返回的正式分数 | 21 |
| Builder 提交的真实 Harness 结构变化 | 11 |
| Builder 拒绝 | 10 |
| Solver API 错误 | 9 |
| Solver 答案格式错误 | 2 |
| 新 Harness 首次执行时的 `ValueError` | 6 |

注意：一次正常轮次可以同时产生一个 evaluator 分数和一个 Builder commit；因此上述类别不是互斥的轮次数量。

## 4. 18 条 lineage 的逐轮结果

### 4.1 ALE-Bench

| Seed / 题 | 正式分数序列 | Harness 变化与终止原因 |
|---|---|---|
| S1 / A | `50 → 0 → 32,009` | R3：H0 → `6a1c9435…`；R4 新 Harness `ValueError`，随后停止 |
| S1 / B | `0 → 0` | 没有 commit；R3 Solver API 错误，随后停止 |
| S1 / C | `30,946,596 → 12,652,398` | R2：H0 → `b6e9a090…`；R3 新 Harness `ValueError`，随后停止 |
| S2 / A | `81,555` | 没有 commit；R2 Solver API 错误，随后停止 |
| S2 / B | `464,165 → 452,547` | R2：H0 → `320ed844…`；R3 新 Harness `ValueError`，随后停止 |
| S2 / C | 无正式分数 | R1 Solver API 错误，随后停止 |
| S3 / A | 无正式分数 | R1 Solver API 错误，随后停止 |
| S3 / B | `0` | R1：H0 → `06bf4e18…`；R2 新 Harness `ValueError`，随后停止 |
| S3 / C | `3,324,013 → 0` | R2：H0 → `3a0f7c29…`；R3 APIError，随后停止 |

ALE-Bench 共得到 12 个 lineage evaluator 分数、5 次真实 Harness commit。所有 5 个已提交 Harness 都没有在后续获得更高的有效分数：其中 4 个首次执行即 `ValueError`，另 1 个在下一轮遇到 APIError。

### 4.2 EdgeBench

| Seed / 题 | 正式分数序列 | Harness 变化与终止原因 |
|---|---|---|
| S1 / A | `256,057,952 → 230,906,889` | R1：H0 → `0ec3b3fb…`；R2：`0ec3b3fb…` → `9c5c69a7…`；R3 新 Harness `ValueError` |
| S1 / B | `231,525,914` | 没有 commit；R2 `SolutionContractError` |
| S1 / C | 无正式分数 | R1 `SolutionContractError` |
| S2 / A | 无正式分数 | R1 Solver API 错误 |
| S2 / B | `237,577,442 → 234,898,084` | R1：H0 → `d1850102…`；R2：`d1850102…` → `f50bcdba…`；R3 新 Harness `ValueError` |
| S2 / C | 无正式分数 | R1 Solver API 错误 |
| S3 / A | 无正式分数 | R1 Solver API 错误 |
| S3 / B | `232,080,555 → 170,668,335` | R2：H0 → `6b43024e…`；R3 Solver API 错误 |
| S3 / C | `23,254` | R1：H0 → `7f112640…`；R2 新 Harness `ValueError` |

EdgeBench 共得到 9 个 lineage evaluator 分数、6 次真实 Harness commit。

只有两个新 Harness 在下一轮真正完成 Solver 和 evaluator：

| Lineage | H0 分数 | 新 Harness 分数 | 变化 |
|---|---:|---:|---:|
| Edge S1-A | 256,057,952 | 230,906,889 | -25,151,063（-9.82%） |
| Edge S2-B | 237,577,442 | 234,898,084 | -2,679,358（-1.13%） |

这两个样本证明了“新 Harness 实际生效且可评分”，但方向都是下降，不支持单题提分结论。

## 5. Builder 是否真的改变了下层 Harness

本次共有 11 次满足严格判定的结构提交：

```text
builder_status = committed
且
next_harness_sha256 != harness_sha256
```

关键证据例子：

```text
Edge S1-A R1
执行 Harness：8b8a89f9…（H0）
Builder 提交：0ec3b3fb…（H1）

Edge S1-A R2
实际执行 Harness：0ec3b3fb…（上一轮提交的 H1）
Evaluator 分数：230,906,889
Builder 再提交：9c5c69a7…（H2）
```

因此，这不是“Builder 每轮改一段答题 prompt，但 Solver Harness 始终没变”。至少在哈希、提交回执、下一轮执行输入和 evaluator 回执四层证据上，H1 已经替换 H0 并被执行。

不过，“Harness 发生变化”不等于“变化有效”。当前主要缺口是：Builder 能生成新结构，但这些结构大多不能稳定完成下一轮，或者完成后分数下降。

## 6. Builder 拒绝与 Solver 错误

### 6.1 Builder 拒绝：10 次

| 原因 | 次数 | 含义 |
|---|---:|---|
| API 状态为 completed，但没有可用正文 | 7 | 模型服务完成了请求，但 Builder 没拿到可解析提案 |
| `Task Harness capabilities must be an object` | 1 | Builder 输出的 capabilities 类型不符合 Harness schema |
| `model_call node cannot declare a skill` | 2 | Builder 把 Skill 声明放到了不允许的位置 |

这些拒绝表明通用门禁已经允许多种 Harness 变化，但仍保留了最基本的 schema 和执行安全要求。它们不是 benchmark evaluator 给出的拒绝。

### 6.2 Solver API 错误：9 次

| 类型 | 次数 |
|---|---:|
| Responses API 状态 completed，但没有可用正文 | 8 |
| `APIError` | 1 |

所有 provider 请求都保持 `provider_attempts=1`；错误后没有自动重试。

### 6.3 Solver 答案格式错误：2 次

EdgeBench 出现 2 次 `SolutionContractError`。这表示下层 Solver 的最终答案没有满足 EdgeBench 的公开交卷合同，evaluator 没有运行，因此不能把它们记成 0 分。

### 6.4 新 Harness 执行错误：6 次

6 个已提交的新 Harness 在下一轮第一次执行时产生 `ValueError`。这正是本次最主要的工程和研究阻塞：门禁能够证明结构在静态层面合法，但还没有充分保证多节点数据流、输入绑定和最终 `emit` 在真实运行时可用。

失败后出现的 `IncompleteRoundError` 只是固定 8 轮槽位的终止填充，不代表又调用了一次模型，也不算新的独立错误。

## 7. Freeze 与 ALE S1 3×3

只有 ALE S1 同时获得 A/B/C 的可冻结候选，因此只有它运行了 H0 与 3×3。

三个来源位置最终冻结出的 Harness 哈希完全相同：

```text
8b8a89f9cfe31274c9e0c90b55d474c53aa248075af22a2c41d32d1592f99974
```

也就是说，A、B、C 实际冻结的都是 H0，不是三个分别在 A、B、C 上进化出来的专门化 Harness。

### 7.1 H0 重跑

| H0 目标题 | 分数 / 状态 |
|---|---|
| A (`ahc024`) | 105,515 / `ACCEPTED` |
| B (`ahc026`) | API 失败 |
| C (`ahc011`) | API 失败 |

### 7.2 3×3 矩阵

| 来源 Harness | 目标 A | 目标 B | 目标 C |
|---|---:|---:|---:|
| A（实际 H0） | 26,151 | API 失败 | API 失败 |
| B（实际 H0） | 50 | API 失败 | API 失败 |
| C（实际 H0） | 81,982 | 0 / `WRONG_ANSWER` | 0 / `COMPILATION_ERROR` |

矩阵中的差异只能说明：同一个 H0 在不同随机生成和不同题上可能得到不同结果。因为三个来源 Harness 的内容哈希完全相同，不能用这张矩阵计算“native Harness 优于 transferred Harness”，也不能把 B/C 的 0 分解释为专门化迁移失败。

## 8. 与 EdgeBench 官方结果的对照

EdgeBench 官方任务规格为每个 task 提供 baseline、rank-30、rank-1 和 super-anchor 原始分数，并给出 0–100 归一化方法。本次只比较所选三个单任务，不宣称等于完整 leaderboard 总分。

| Task | Moss 本次最好原始分 | 官方 baseline | 官方 rank-30 | 官方 rank-1 | Moss 归一化分 | 官方 README 当前展示最好值 |
|---|---:|---:|---:|---:|---:|---:|
| apple | 256,057,952 | 45,000,000 | 262,328,915.6667 | 282,791,094 | 19.423 | 50.6 |
| molecular | 237,577,442 | 69,170,000 | 235,032,102.6667 | 300,187,365.6667 | 22.344 | 34.7 |
| treant | 23,254 | 5,369 | 88,189 | 330,195 | 4.319 | 18.0 |

其中 molecular 的原始分略高于官方 task spec 中的 rank-30 anchor，但仍明显低于 rank-1；归一化分与官方 README 的完整展示口径也不能简单解释为同一参赛总分。

ALE-Bench 本次得到的是 public evaluator 的原始 `aggregate_score`。官方最终榜单使用 private evaluation 后的 `Rank/Performance`，因此本报告不把 public 原始分直接换算或冒充官方排名。

## 9. 本次结果对实验一假设的判断

### 已得到直接证据

- Builder 能生成并提交不同的下层 Harness；
- 新 Harness 会在下一轮被实际采用；
- 至少两个新 Harness 完成了真实 benchmark evaluator；
- Contract Skill 能阻止部分不合规答案进入 evaluator；
- no-retry、失败终止、哈希和回执审计按设计工作。

### 尚未得到证据

- Harness 在单个 instance 上经过多轮后稳定提分；
- 能冻结出 A、B、C 三个内容不同的高分 Harness；
- `H_A` 在 A 上高分、搬到 B/C/D 后系统性下降；
- 当前数据足以证明 Harness 应该过拟合到单个 instance。

### 当前数据中的反向信号

- 两个可评分新 Harness 都比其 H0 低；
- 6 个新 Harness 在首次真实执行时失败；
- 唯一完成的 3×3 使用的是三个完全相同的 H0。

因此，本次不能以“实验一通过”收尾。正确状态是：**正式 campaign 已完整执行并封存，但科学验收未通过。**

## 10. 下一轮需要先解决什么

如果后续另开新 campaign，不应修改或续跑本次失败轮次。应先做一个独立的 Harness 可执行性资格门：

```text
Builder 提出 H1
→ 静态 schema 检查通过
→ Contract Skill 仍绑定到最终答案节点
→ 用真实 task 输入执行所有节点
→ 每个节点的数据依赖可解析
→ 最终 emit 产生合规候选
→ evaluator 返回正式分数
```

建议验收条件不是“哈希改变”，而是至少连续两代新 Harness 都能完成真实执行和 evaluator。通过这个资格门后，再重新启动 A/B/C、S1/S2/S3 的专门化 campaign，才能有效区分：

```text
Harness 结构进化带来的提升
vs.
同一 Harness 下 Solver 随机重答带来的波动
```

## 11. 证据与可复现信息

AWS 原始 campaign：

```text
/home/ubuntu/Projects/moss-exp1-runs/main-aaf43ab-noretry-20260828-v1
```

本地只读归档：

```text
C:\Users\Huawei\Documents\Moss\experiment-one-artifacts\main-aaf43ab-noretry-20260828-v1.tar.gz
SHA256: 83f9acd588c5fdbcbe12a65b28eb1e86cb70f81140897d463048b3603ac5a917
```

核验后解压目录：

```text
C:\Users\Huawei\Documents\Moss\experiment-one-artifacts\verified-83f9acd5\main-aaf43ab-noretry-20260828-v1
```

代码和运行证据共同记录了：模型配置、任务绑定、Harness 哈希、候选哈希、公开反馈、evaluator 回执、Builder commit/rollback 和失败后的终止状态。

仓库中已有的 `2026-08-28-moss-experiment-one-results.zh-CN.md` 属于较早的 `0bf3061` campaign；本报告只描述最新版 `aaf43ab` 的无重试正式复跑。两次 campaign 不应混合统计，也不应用早期 campaign 的成功样本替代本次复跑的失败轮次。
