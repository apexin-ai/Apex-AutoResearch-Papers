# Moss 实验一正式结果：单题 Harness 专门化

日期：2026-08-28
实验执行代码版本：`0bf3061`（执行时的 `main`；报告提交时 `main` 已继续前进）
正式证据目录：`results/experiment-one-2026-08-28/`

## 1. 先说结论

本次运行已经按照预先固定的“不重试”规则结束，两个 benchmark 的单题进化记录都已封存；ALE-Bench 还完成了三个 seed 的 H0 和全部 3×3，EdgeBench 因缺少合法冻结 Harness，按门禁没有运行矩阵。

结果支持一个较窄但真实的结论：

> Builder 能根据单个 instance 的公开分数和反馈，生成、提交并在下一轮实际采用不同的 Harness；改变 Harness 内的单题指导文字后，部分题明显提分，而且把这种 Harness 搬到别题时会出现显著下降或失败。

但它还没有证明我们最想要的强结论：

> 本次所有获得 evaluator 正式分数的进化 Harness，执行拓扑仍是 `一个 solve 模型调用 → emit`。真正增加角色、审核步骤或多次模型调用的 12 个 Harness 虽然被提交并在下一轮实际尝试，但全部在 evaluator 前终止。

所以，这轮最准确的名称是：

> **instance-conditioned Harness prompt/config specialization（按单题定制 Harness 内部指导）**

暂时不能写成：

> 已经验证多角色或多阶段 Harness 图结构能够在单题内稳定自进化并提分。

## 2. 固定实验方案

| 项目 | 固定设置 |
|---|---|
| Benchmark | EdgeBench、ALE-Bench |
| 题目 | 每个 benchmark 固定 A、B、C 三个 instance |
| 重复 | S1、S2、S3 三个 seed |
| 单题预算 | 最多 8 轮 |
| 上层 Builder | `gpt-5.6-sol`，`reasoning_effort=high` |
| 下层 Solver | `gpt-5.6-sol`，`reasoning_effort=high` |
| API | Responses API，流式传输 |
| 错误策略 | 正式 API、Solver、答案格式、门禁、evaluator 错误均不自动重试 |
| 0 分规则 | evaluator 没运行不记 0；只有 evaluator 正式返回 0 才记 0 |
| 进化判定 | Builder 提出的 next Harness 被提交，并在下一轮被 Solver 实际使用 |
| 交叉测试 | 每个 seed 必须同时具有 A/B/C 三个合法冻结 Harness，才运行 H0 和 3×3 |

固定 instance：

| Benchmark | A | B | C |
|---|---|---|---|
| EdgeBench | `apple_incremental_game` | `molecular_self_assembly` | `treant_forest` |
| ALE-Bench | `ahc024` | `ahc026` | `ahc011` |

每一轮的实际流程：

```text
当前 Task Harness Ht 做题
→ benchmark evaluator 返回公开分数和简短状态
→ Builder 查看公开结果和当前 Harness
→ Builder 提出下一版 Harness
→ 固定 Python 做结构检查和 probe
→ 通过则 commit 为 Ht+1；提案无效则保留 Ht
→ 下一轮实际运行留在 workspace 中的 Harness
```

Builder 看不到隐藏测试、私有 judge 日志或候选答案正文。它能看到的是公开分数、允许公开的短反馈和 Harness 结构信息。

## 3. 实际完成情况

| Benchmark | 单题 lineage | 正式 lineage 分数 | 合法冻结 Harness | H0 | 3×3 |
|---|---:|---:|---:|---:|---:|
| EdgeBench | 9/9 已按不重试规则终止 | 11 | 6/9 | 未运行 | 未运行 |
| ALE-Bench | 9/9 已按不重试规则终止 | 17 | 9/9 | 9 格，其中 8 格有分数 | 27 格，其中 26 格有分数 |

完整汇总表包含：

```text
moss-lineages.tsv  144 行：18 条 lineage × 8 个固定轮次槽位
moss-freeze.tsv     15 行：15 个合法冻结 Harness
moss-h0.tsv          9 行：ALE 三个 seed 的 H0
moss-cross.tsv      27 行：ALE 三个 seed 的全部 3×3
```

“144 行”不表示进行了 144 次有效模型和 evaluator 调用。某条 lineage 遇到不重试的终止错误后，剩余轮次槽位记为 `IncompleteRoundError`，只表示该 lineage 已经停止。

EdgeBench 没有矩阵不是漏跑：

- S1 缺 B 的合法冻结 Harness；
- S2 缺 C；
- S3 缺 C。

三个 seed 都不满足 A/B/C 同时齐全的门禁，因此没有绕过门禁，也没有补造 H0 或 3×3。

## 4. Builder 到底有没有真的改 Harness

Builder 共完成 28 次运行：

| 结果 | 次数 | 实际含义 |
|---|---:|---|
| `committed` | 23 | 候选 Harness 通过检查，成为下一轮实际 Harness |
| `rejected` | 5 | Builder 输出没有形成合法候选，旧 Harness 被保留 |

23 次 commit 的完整证据链全部成立：

```text
Builder candidate_harness_sha256
= commit receipt candidate_sha256
= 本轮 next_harness_sha256
= 下一轮实际执行的 harness_sha256
```

也就是说，23/23 个成功提交的 Harness 都在下一轮被实际采用，不是 Builder 只写了一段建议、Solver 仍沿用旧结构。

5 次 rejected 是：

```text
Edge S1-A：R2、R3、R4
ALE  S2-B：R1
ALE  S2-C：R2
```

这些轮次的 `commit_or_rollback` 事件写为 `rollback`，但实现上没有创建 rollback receipt，也没有把 workspace 倒回更早版本；准确行为是“提案无效，当前 Harness 保持不变”。

Freeze 也不是 rollback。Freeze 只读地选择历史最高正式分数对应的 Harness，写入跨测授权，不改 workspace 当前状态。交叉测试再根据 freeze receipt 显式加载这个历史最佳 Harness。

## 5. “Harness 变了”需要分成两层看

23 个已提交的新 Harness 中：

| 变化类型 | 提交数 | 下一轮获得 evaluator 正式分数 |
|---|---:|---:|
| 真正改变节点、角色或执行顺序 | 12 | 0 |
| 保持 `solve → emit`，改变 solve 节点的具体指导文字 | 11 | 8 |

因此本次可以确认：

- Harness artifact、hash 和内部配置确实发生变化；
- Builder 的 next Harness 确实被执行；
- prompt/config 的单题定制可以提分。

但本次不能确认：

- 多角色结构能稳定进入 evaluator；
- 多次模型调用结构能稳定提分；
- 工具调用或复杂工作流已经在正式结果中优于单节点 H0。

所有成功进入 evaluator 的实际拓扑都是：

```text
solve: model_call → emit
```

真正增加 `draft`、`review`、`audit`、`finalize` 等节点的 Harness，虽然在下一轮被实际采用，但随后出现 `ValueError`、`OpenAIResponsesError` 或 `SolutionContractError`，没有 evaluator 分数。

这是本次实验最重要的负结果，也是实验二前必须先修的地方。

## 6. 最关键的提分案例

### 6.1 ALE S3-C：从超时 0 分变成 2,715,861

```text
R1  H0（8b8a89f9…）  0 / TIME_LIMIT_EXCEEDED
Builder 提交 dcf9ef45…
R2  dcf9ef45…        2,715,861 / ACCEPTED
```

前后 Harness hash 不同，`dcf9ef45…` 在下一轮被实际采用。它仍是 `solve → emit` 拓扑，但 solve 节点中的单题指导已经变化。

冻结后重新在 C 上运行：

```text
C→C  16,424,595 / ACCEPTED
```

同 seed 下观察到的最佳 H0-C 是 A(H0)→C 的 7,059,767。冻结后的 `dcf9ef45…` 比这个值高约 132.65%。不过每格只有一次生成，仍需要更多重复才能估计稳定提升。

### 6.2 Edge S2-A：240,091,781 → 257,564,497

```text
R1  H0          240,091,781
R2  e7e3b6ec…   257,564,497
```

提升 17,472,716，约 `+7.28%`。但 Edge 没有形成 3×3，这里只有一次变更前和一次变更后观测，不能排除答案波动。

### 6.3 ALE S1-C：最终超过起点，但冻结复测不够稳定

```text
R1  H0       15,866,583
R2  88f5              0 / TLE
R3  0d18      2,803,468
R4  0dae     17,131,980 / ACCEPTED
```

R4 相对 R1 提高约 `+7.98%`。但冻结后的 C→C 是 14,054,778，而同 seed 的 H0 在 B→C 得到 16,615,646，因此这个案例没有明显超出 H0 的自然波动范围。

## 7. 不能误写成结构提分的案例

ALE S2-C：

```text
R1  H0       13,461,443
R2  c12e     11,964,232
R3  c12e     15,636,948
```

R2 和 R3 使用同一个 `c12e4962…` Harness。R3 比 R2 高不能算结构进化，只能算相同 Harness 下生成了不同答案。

Edge S1-A 的同结构波动更大：

```text
固定 e763fcab…：248,098,812 → 0 → 251,604,383 → 256,674,857
```

因此，单看分数曲线会把 Solver 的答案波动误判为 Harness 提分。后续实验必须同时报告 Harness hash、结构类型和同结构重复。

## 8. 18 条单题 lineage

### 8.1 EdgeBench

| Seed | 题 | 逐轮正式结果 | 冻结 |
|---|---|---|---|
| S1 | A | 255,985,171 `[H0]` → 248,098,812 `[e763]` → 0 `[e763]` → 251,604,383 `[e763]` → 256,674,857 `[e763]` → `ValueError [ccff]` | R5 e763，256,674,857 |
| S1 | B | R1 `SolutionContractError [H0]` | 无 |
| S1 | C | 43,784 `[H0]` → `SolutionContractError [4608]` | R1 H0，43,784 |
| S2 | A | 240,091,781 `[H0]` → 257,564,497 `[e7e3]` → `ValueError [921f]` | R2 e7e3，257,564,497 |
| S2 | B | 230,389,334 `[H0]` → `OpenAIResponsesError [bc84]` | R1 H0，230,389,334 |
| S2 | C | R1 `SolutionContractError [H0]` | 无 |
| S3 | A | 246,582,293 `[H0]` → `ValueError [d8db]` | R1 H0，246,582,293 |
| S3 | B | 215,905,703 `[H0]` → `ValueError [4a31]` | R1 H0，215,905,703 |
| S3 | C | R1 `OpenAIResponsesError [H0]` | 无 |

### 8.2 ALE-Bench

| Seed | 题 | 逐轮正式结果 | 冻结 |
|---|---|---|---|
| S1 | A | 32,015 `[H0]` → 31,978 `[fab8]` → `ValueError [34d6]` | R1 H0，32,015 |
| S1 | B | 428,223 `[H0]` → `ValueError [c49f]` | R1 H0，428,223 |
| S1 | C | 15,866,583 `[H0]` → 0/TLE `[88f5]` → 2,803,468 `[0d18]` → 17,131,980 `[0dae]` → `ValueError [348d]` | R4 0dae，17,131,980 |
| S2 | A | 31,980 `[H0]` → `ValueError [0aee]` | R1 H0，31,980 |
| S2 | B | 0/WA `[H0]` → 0/WA `[H0]` → `ValueError [0ade]` | R1 H0，0 |
| S2 | C | 13,461,443 `[H0]` → 11,964,232 `[c12e]` → 15,636,948 `[同一 c12e]` → `OpenAIResponsesError [344e]` | R3 c12e，15,636,948 |
| S3 | A | 104,623 `[H0]` → `ValueError [44d4]` | R1 H0，104,623 |
| S3 | B | 0/WA `[H0]` → `ValueError [051b]` | R1 H0，0 |
| S3 | C | 0/TLE `[H0]` → 2,715,861 `[dcf9]` → `SolutionContractError [8dd7]` | R2 dcf9，2,715,861 |

## 9. ALE-Bench H0 与 3×3

矩阵的行表示 Harness 从哪道题冻结，列表示固定该 Harness 后重新做哪道题。它不是把来源题的旧答案直接提交给目标题。

所有 36 个 H0/cross cell 均满足：

```text
builder_constructed_count = 0
builder_call_count = 0
memory_read_count = 0
```

其中 34 个成功完成的 cell 各进行了一次 Solver 调用；两个格式无效 cell 没有完成 Solver 调用：S1 `C→B` 和 S2 `H0→C`。

### 9.1 S1

H0：A=`0/CE`，B=`447,266/AC`，C=`10,272,260/AC`

| Harness 来源 \ 目标题 | A | B | C |
|---|---:|---:|---:|
| A（实际为 H0） | 24,536 | 450,545 | 0/CE |
| B（实际为 H0） | 39,053 | 0/TLE | 16,615,646 |
| C（0dae） | 32,012 | 无正式分数/`SolutionContractError` | 14,054,778 |

S1 的 A、B 冻结 Harness 都是 H0，只有 C 行是进化后的 prompt/config Harness。

### 9.2 S2

H0：A=`32,020/AC`，B=`0/WA`，C=无正式分数/`SolutionContractError`

| Harness 来源 \ 目标题 | A | B | C |
|---|---:|---:|---:|
| A（实际为 H0） | 31,974 | 0/WA | 0/CE |
| B（实际为 H0） | 81,723 | 0/WA | 5,272,404 |
| C（c12e） | 0/WA | 459,551 | 11,441,689 |

支持专门化的证据：C Harness 在 C 上为 11,441,689，搬到 A 后为正式 0/WA。

反例：同一个 C Harness 搬到 B 后为 459,551/AC，说明它并非只能服务 C。

### 9.3 S3

H0：A=`101,933/AC`，B=`0/WA`，C=`0/WA`

| Harness 来源 \ 目标题 | A | B | C |
|---|---:|---:|---:|
| A（实际为 H0） | 32,021 | 0/WA | 7,059,767 |
| B（实际为 H0） | 31,995 | 449,184 | 0/TLE |
| C（dcf9） | 105,215 | 0/WA | 16,424,595 |

支持专门化的证据：C Harness 在 C 上高分，搬到 B 后为 0/WA。

反例：同一个 C Harness 搬到 A 后仍为 105,215/AC，不低于该 seed 的 H0 baseline 101,933。

## 10. 错误与停止原因

按 18 条 lineage 的第一个终止错误统计，不重复计算后续 `IncompleteRoundError`：

| 错误 | Edge | ALE | 合计 |
|---|---:|---:|---:|
| `ValueError` | 4 | 7 | 11 |
| `SolutionContractError` | 3 | 1 | 4 |
| `OpenAIResponsesError` | 2 | 1 | 3 |

含义：

- `SolutionContractError`：Solver 已产生内容，但未通过 evaluator 前的答案格式合同；没有 evaluator 分数。
- `OpenAIResponsesError`：Solver 的模型/API 阶段失败；没有 evaluator 分数。
- `ValueError`：大多发生在 Solver 返回后、evaluator 前的本地处理阶段；当前 abandonment receipt 只保存了异常类，没有保存详细消息，因此不能再臆测更细的原因。
- `IncompleteRoundError`：前一错误触发 no-retry/fail-closed 后，对剩余轮次的状态填充，不是一条新的独立错误。

正式 0 分全部来自 evaluator，例如 WA、TLE、Compilation Error；没有把上述错误当作 0。

三次 API/模型层错误的原始审计记录为：

| Benchmark | 轮次 | 开始时间（UTC） | 错误时间（UTC） | 原始错误类型 |
|---|---|---|---|---|
| EdgeBench | S2-B R2 | 2026-08-28 06:53:44 | 2026-08-28 07:08:59 | `OpenAIResponsesError` |
| EdgeBench | S3-C R1 | 2026-08-28 07:19:50 | 2026-08-28 07:24:14 | `OpenAIResponsesError` |
| ALE-Bench | S2-C R4 | 2026-08-28 07:14:25 | 2026-08-28 07:17:03 | `OpenAIResponsesError` |

审计 JSONL 只保存了 `error_type=OpenAIResponsesError`，没有保存 provider 返回的 HTTP 状态码或消息正文。因此目前能严谨提供的“具体报错”就是错误类型、操作编号和时间，不能补写成 504、限流或 key 失效。本次也没有对这三次错误自动 retry。

## 11. 对“Harness 专门化”假设的判断

### 已被支持

- Builder 能生成并提交不同 Harness artifact。
- 23 个已提交 Harness 全部在下一轮被实际采用。
- 单题定制 Harness 的 prompt/config 能在部分 instance 上明显提分。
- 部分单题定制 Harness 搬到别题后会显著下降或失败。

### 有明确反例

- S2 C Harness 搬到 B 得 459,551。
- S3 C Harness 搬到 A 得 105,215。
- 同一个 H0 或进化 Harness 在同一题上的分数波动很大。

因此不能写“专门化 Harness 必然在所有其他题上变差”。

### 尚未被支持

- 多角色、多阶段、工具化 Harness 结构能够稳定进化并提分。
- 分数会随着轮次持续单调上升。
- 当前观测到的全部提升都主要由 Harness 造成，而不是 Solver 答案随机性。
- Harness 普遍应该完全过拟合到单个 instance。

最稳妥的论文表述：

> 单题 Harness 会出现可测量的 instance 专门化：Builder 指导的 Harness prompt/config 变化能够改善产生它的优化题，在其他题上可能明显退化；但这种效应并非绝对，部分指导仍可跨题复用。

## 12. 与官方榜单的关系

本次分数来自冻结版本的官方 evaluator 接口，因此是正式、可重放的单 instance 分数。

但不能直接宣称超过官方完整榜单：

- 每个 benchmark 只选择了三个 instance；
- 每条 lineage 最多 8 轮，不等于论文或榜单的完整时间预算；
- EdgeBench 与 ALE-Bench 的分数尺度不同，不能混合求一个总分；
- 每个 cross cell 只有一次 Solver 生成，随机波动很大。

后续要做榜单宣传，应另开 leaderboard campaign：冻结最终 Moss 方法，使用官方题目范围、预算和汇总规则，再和官方榜单同口径比较。本报告不把单题分数冒充完整榜单分数。

## 13. 对实验二的直接建议

不建议马上把现有失败 Harness 直接送入实验二，然后宣称 Builder 能救回“结构”。原因是本次所有真正改变拓扑的 Harness 都没有 evaluator 分数，当前系统先要解决多节点 Harness 的执行稳定性。

建议分两步：

### P0：先补齐真正的结构进化能力

选择 ALE 的一个短 smoke instance，要求至少完成：

```text
H0: solve → emit
Ht: draft → verify → emit
```

并让 Ht 真正完成每个模型节点、通过 Contract Skill、进入 evaluator。验收条件不是 hash 变化，而是 trace 中出现多次模型调用，且 evaluator 返回正式分数。

### P1：再做实验二“救回错误 Harness”

可以沿用实验一的两个错误迁移起点：

```text
ALE S2 C Harness → A：0/WA
ALE S3 C Harness → B：0/WA
```

固定 Builder，让它只看目标题公开分数、短反馈和当前 Harness，连续改造下层 Harness。同时运行 answer-only 对照：Harness 不变，只让 Solver 重答。

实验一和实验二最终应形成：

```text
在 C 上得到专门化 Harness
→ 搬到 A/B 后失败
→ 固定 Builder 在目标题现场改造真正的 Harness 结构
→ 目标题重新获得高分
→ answer-only 不能达到同等改善
```

## 14. 证据位置与完整性

本地正式证据：

```text
results/experiment-one-2026-08-28/formal/
results/experiment-one-2026-08-28/logs/
results/experiment-one-2026-08-28/moss-lineages.tsv
results/experiment-one-2026-08-28/moss-freeze.tsv
results/experiment-one-2026-08-28/moss-h0.tsv
results/experiment-one-2026-08-28/moss-cross.tsv
```

压缩归档：

```text
results/experiment-one-2026-08-28/moss-exp1-formal-20260828.tar.gz
SHA-256: 61f25e5614ff5497bdc677b68ba09fc74e8ddc6be5fb2b6bbdb1e2056d0deddc
```

本地与 AWS 上的压缩包 hash 一致。TSV 与原始 `result.json`、`freeze_receipt.json`、H0/cross `receipt.json` 逐项审计，未发现分数字段不一致。
