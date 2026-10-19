# KernelBench P2c：追加式自适应 Harness 资源分配

日期：2026-08-02
状态：方案已交付；尚未实现、尚未获得真实执行授权；P3 保持关闭

## 1. 决策摘要

P2c 是 P2b 之后的新阶段，不是对 P2b 上限的就地放宽。它从已经冻结的 P1/P2/P2b 事实中，
按 Task 分别选择更值得继续的 Harness 路线，并把新增预算按小段追加给这些路线。

本方案采用**带恢复资格和替补席的分段竞赛**，而不采用纯 bandit 或不可逆的标准 successive
halving：

- 每个 Task 只有四条路线，样本很少；
- 每次生成的新 Harness 会改变路线状态，后续回报不是固定分布的重复抽样；
- 路线起点不同，`architecture_reset` 从 reference 起步，不能用“相对自己起点的涨幅”排名；
- 已出现 Profiler 会话中断和可修复 Harness 合同错误，不能把它们当作性能失败；
- 两轮一段的冻结决策、明确公式和有限替补规则，比在线概率采样更容易从账本逐项复算。

P2c 的默认新增硬帽为：每题 16 次 Kernel 生成尝试、40 次模型调用和 3,600 GPU 秒；两题合计
32 次 Kernel 生成尝试、80 次模型调用和 7,200 GPU 秒。API 与 GPU 费用各为每题 50 美元、
全局 100 美元。两个 Task 的任一剩余预算都不能借给另一个 Task。

## 2. 目标与非目标

### 目标

- 在固定 KernelBench instance 上刷新本题的正确、可复算全局最好分；
- 把新增调用和 GPU 时间优先给绝对分数接近前沿、近期有可信进展、正确率可接受且结构仍有
  探索价值的 Harness 路线；
- 让 v008、单次格式错误或可恢复基础设施中断都不再天然等于整条路线的终点；
- 保留每次分配、父 Harness、父 Kernel、即时分数、Profiler 事实、错误和成本的完整因果链；
- 在恢复后仍能机械得到完全相同的排名、剩余预算和下一动作。

### 非目标

- 不声明通用 Task 迁移或 Builder 提升；
- 不修改 P1、P2、P2b 的账本、候选、版本号、上限或历史结论；
- 不修改 KernelBench commit、评分器、正确性/计时协议、GPU 或模型；
- 不利用 P3、隐藏测试或其他用户进程；
- 不补造 `ncu`、achieved occupancy、DRAM/L2 或 warp stall 等缺失硬件指标；
- 不自动实现、启动 P3，亦不因 P2c 成功自动增加 P2c 预算。

## 3. 阶段和事实隔离

```text
P1/P2 只读事实 ─┐
                 ├─> P2b 完成并冻结 ─> P2c source snapshot
P2b 只读产物 ───┘                              │
                                               ├─ R：恢复资格
                                               ├─ S1：两席宽赛
                                               ├─ S2：收窄竞赛
                                               └─ S3：前沿追击
                                                        │
                                                        └─ 停在 P3 授权门
```

P2c 使用新的 phase 名 `P2C`、独立 artifact root、`p2c_plan.json` 和 `ledger.jsonl`。建议路径为：

`/home/ubuntu/Projects/Moss/results/optimization_lab/kernelbench-p2c-adaptive`

准备器在 P2b writer 已退出后，把以下内容复制为不可变输入，而不是依赖仍可能增长的源文件：

- P2b 账本的完整快照、事件数和 SHA-256；
- P2b plan、P1/P2 冻结输入 manifest 及其 SHA-256；
- 每条路线所有有效 Harness/Kernel 配对、被拒原文、公开 ProfileSummary 和候选评分事实；
- 每题 P1/P2/P2b 的正确全局最好候选及评分协议哈希；
- 源阶段已消费的调用、GPU 秒和费用，仅作显示，不从 P2c 新预算中再次扣除。

源快照一旦写入 `p2c_plan.json` 就不得换成更新版本。若 P2b 后来又出现新事件，只能放弃尚未
启动的 P2c plan 并重新准备；P2c 已出现任何 `p2c_phase_changed:started` 事件后不得换源。

## 4. 可排名事实和错误分类

### 4.1 score-bearing outcome

只有满足以下条件的评价才进入排名统计：

1. 候选源码、任务、评分协议和评价结果都有哈希绑定；
2. `valid_run=true`；
3. 已得到正确或不正确的确定结论；
4. 正确候选同时有速度结果。

正确性失败是有效的 score-bearing outcome，计入正确率但没有 speedup。以下事实不进入分数或
正确率分母：模型输出格式错误、Harness 合同错误、Provider/进程中断、评分环境无效、Profiler
中断和精确/近重复候选。它们仍完整计入相应调用、Kernel 尝试或 GPU 预算。

### 4.2 已评分但未封存

若 `candidate_evaluated` 已保存，而后续 Profiler 或进程中断：

- 直接导入该正确性和 speedup，不再次编译、检查正确性或测速；
- 先从原归档恢复 ProfileSummary；没有可恢复摘要时，只重跑 Profiler；
- Profiler 重跑使用新 attempt ID，新增 GPU 成本计入 P2c，旧尝试仍保留且不重复扣账；
- 两次 Profiler 尝试后仍不可用，就以 `profile.status=unavailable` 封存评分并继续搜索；
- 缺失硬件指标保持 `unavailable`，不得推断补齐。

### 4.3 可恢复的源阶段终止

下列 P2b 终止原因只影响恢复状态，不降低路线排名：

- 已开始但缺少归档的模型或 Profiler 会话；
- Provider/SSH/进程中断；
- 单次 Harness 或 Kernel 输出合同/格式错误；
- 有有效评分但 P2b round 未封存。

每条因此终止的路线先获得一个 **R 恢复名额**：最多产生一个新的 P2c Kernel 尝试。它从最后
一个有效父 Harness/Kernel 配对继续，不能覆写或假装补成原 P2b vNNN。R 名额是 P2c 新预算，
不属于原 64/120 合同。若源归档已经包含旧尝试的完整结果，则恢复该旧尝试只追加 recovered
事件、不重调模型或 GPU；随后获配的 R 续跑名额仍使用新的 P2c Harness/Kernel ID 和新预算。

候选本身不正确、重复、无可信提升或达到 P2b v008 不属于“错误恢复”，只能通过后续排名获得
预算。

## 5. 每题独立的前沿和 2% 语义

每个 Task 同时维护两个最好值。source snapshot 时二者都初始化为源阶段的精确最高正确分
`G0`：

- `G_raw`：相同冻结评分协议下，P1/P2/P2b/P2c 所有正确候选的最高原始 speedup；
- `G_credible`：P2c 中只有相对上一个 `G_credible` 至少提升 2% 时才更新的可信前沿锚点。

新分数高于 `G_raw` 但不足 2% 时，可称“数值最好”或“噪声区最好”，不能称“可信刷新”。它
可以作为下一轮父候选，但不能触发成功声明。所有 2% 比较都使用比值 `new / comparator >= 1.02`，
不用四舍五入后的看板文本。

两个 Task 的 `G_raw`、`G_credible`、路线排名、错误次数和预算完全隔离。只有 GPU4 执行队列是
共享且严格串行的。

## 6. 路线晋级公式

排名只在预先声明的 decision epoch 运行。每次先追加一个不可变 `p2c_decision_snapshot`，保存
输入事件范围、所有中间量、公式版本和排序结果；同一 epoch 内后到的结果不能改变已分配名额。

对某 Task 的路线 `l` 定义：

- `B_l`：该路线截至快照实际生成的 P2b/P2c 候选中的最高正确 speedup；冻结起点可作父候选和
  首块斜率比较基准，但不冒充该路线自己取得的分数；
- `G`：快照时该 Task 的 `G_raw`；
- `n_l, c_l`：最近最多 8 个 score-bearing 生成结果数和其中正确数；
- “最近块”：最近最多 2 个 score-bearing 结果；
- “粗结构族”：忽略变量名、常量微调、`num_warps` 和 `num_stages`，只保留 Triton Kernel 数、
  launch 图、program-id 维度、归约/分块拓扑、主要读写布局和是否使用框架 fallback 的签名。

五个归一化分量都在 `[0, 1]`：

1. **绝对名次 `A_l`（30%）**：按 `B_l` 降序；取最高未分组分数为组首，把与该组首之比
   不足 2% 的路线放入同一噪声组，再处理下一组。四条路线的组名次依次映射为
   `1, 2/3, 1/3, 0`，同组同值；没有正确生成候选的路线记 `priority=null`。
2. **距全局前沿 `F_l`（30%）**：令 `gap=(G-B_l)/G`。`gap<=0.02` 时为 1；
   `0.02<gap<0.10` 时为 `(0.10-gap)/0.08`；`gap>=0.10` 时为 0。
3. **近期可信斜率 `M_l`（20%）**：令 `B_before` 为最近块前的路线最好（首块没有更早生成结果
   时使用冻结起点），`B_after` 为块后的路线最好，`q` 为块中 score-bearing 数。若
   `B_after/B_before<1.02`，则为 0；否则
   `M_l=min(1, ((B_after/B_before)-1) / (0.02*q))`。错误/中断不伪装成负斜率。
4. **正确性 `C_l`（10%）**：使用 Beta(1,1) 平滑值 `(c_l+1)/(n_l+2)`。基础设施和格式
   错误不进入 `n_l`，正确性失败进入。
5. **结构新颖度 `N_l`（10%）**：最近块中，正确、达到 `0.90*G` 且粗结构族相对上个 decision
   snapshot 首次出现的候选数记为 `u_l`，`N_l=min(1,u_l/2)`。首次排名以最近块之前的冻结
   source 历史为比较集合。只有静态证据时照常计算粗签名，不用缺失硬件计数器猜测新颖度。

最终优先分：

```text
priority_l = 0.30*A_l + 0.30*F_l + 0.20*M_l + 0.10*C_l + 0.10*N_l
```

百分比“相对路线起点提升”只显示，不进入公式或停止条件。这样从 1.000× 到 19× 的
`architecture_reset` 不会仅因低起点获得虚高优势；但它若在接近全局前沿时出现至少 2% 的近期
提升，仍会通过 `F_l` 和 `M_l` 得到晋级机会。

路线进入性能名额的最低条件为：至少一个正确生成候选，且 `B_l>=0.80*G`。`M_l` 不能绕过
这个绝对分数地板，R 恢复名额则不受此条件限制。优先分相同时依次比较 `F_l`、`M_l`、较少的
P2c Kernel 尝试数和冻结的策略顺序；原始小于 2% 的 speedup 差只可作最后机械排序，不得写成
可信优势。

## 7. 分段追加策略

### R：恢复和对账

1. 零调用导入所有可恢复归档及“已评分但未封存”事实；
2. 只对缺少公开摘要的已评分正确候选恢复 Profiler，不重跑评分；
3. 每条因可恢复原因停止的路线最多获得 1 个新 Kernel 名额；
4. R 结果封存后才进行首次排名，单次 R 失败不会停止其他路线或另一个 Task。

### S1：两席宽赛

- 每题选择 2 条路线，每条追加一个包含 2 个 Kernel 的 tranche；
- 第一席给最高 `priority`；
- 第二席通常给次高 `priority`。若正常第二名 `M_l=0`，但有未入选路线满足
  `B_l>=0.90*G` 且 `M_l>0`，则 momentum wildcard 优先替换第二席，候选按 `M_l`、
  `priority` 排序；若没有 momentum 候选，只有在正常第二名 `N_l=0` 时，才由满足
  `B_l>=0.90*G` 且 `N_l>0` 的 novelty wildcard 替换，候选按 `N_l`、`priority` 排序；
- 每条路线整个 P2c 最多使用一次 wildcard；它是替补，不增加第三席。

### S2：收窄竞赛

- 所有 S1 tranche 都封存后重新排名；
- 第一名追加 2 个 Kernel；
- 最多再给一条 challenger 追加 2 个 Kernel。challenger 必须处于全局 2% 噪声带，或同时
  满足 `B_l>=0.90*G` 与 `M_l>0`；
- 不满足 challenger 条件时只运行第一名，空出的预算保持未使用，不能转给另一个 Task。

### S3：前沿追击

- 每次只给当前第一名追加 2 个 Kernel，完成后重新排名；
- 每题最多执行两个 S3 tranche；
- 若上一 tranche 相对其开始时的路线最好或 `G_credible` 得到至少 2% 提升，则可继续；
- 没有可信提升时，只有“`B_l` 在 `G` 的 2% 噪声带内且出现新的正确粗结构族”可获得一次
  grace tranche；每条路线最多一次 grace；
- tranche 过程中出现数值全局最好不会临时增加轮次，等 tranche 封存后再决策。

每个普通 tranche 固定 2 个 Kernel，既避免单轮噪声决定去留，也避免一次预拨过多预算。多个
晋级路线的执行顺序在 decision snapshot 中冻结，并按一轮一轮交错、下个 epoch 反转首发顺序，
降低 GPU 时间漂移造成的顺序偏差。模型生成和 GPU4 评分始终只有一个在运行。

## 8. 父版本和“一版 Harness 对一个 Kernel”

P2c 版本使用独立命名空间，例如：

- route：`p2c:kernelbench_layernorm:architecture_reset`；
- tranche：`p2c-ln-architecture-reset-s1-t01`；
- Harness：`p2c-ln-architecture-reset-h001`；
- Kernel：`p2c-ln-architecture-reset-k001`；
- attempt：在上述 ID 后附 `-a001`、`-a002`，只表示调用尝试，不伪装成新版本。

每个已接受 Harness 版本只能绑定一个 Kernel generation attempt。即使 Kernel 原文格式无效，
该 Harness 也已消费；再次生成 Kernel 必须先生成带新 ID 的子 Harness。无效 Harness draft 没有
版本号，只保存 attempt 原文；其修复从最后一个有效 Harness 生成新子版本。

每条路线导入时保存：

- `source_route_id` 和源账本事件 ID；
- 最后有效 Harness、最快正确 Harness/Kernel 配对及其 SHA-256；
- 被拒但可用于避错的模型原文引用；
- `parent_policy_id`、`parent_candidate_id`、`base_candidate_id` 三个独立指针；
- 源阶段分数和成本，以及 P2c 当前剩余预算。

每个 tranche 的首轮默认从该路线的配对前沿继续：先取原始最快正确配对；若多个候选都在其
2% 噪声带内，则取最近的正确、粗结构最新颖配对。后续轮可沿刚生成的有效 Harness，也可显式
回滚到本路线已归档配对；不得读取另一 P2c 路线的 Kernel/Harness 正文。分配器可以看到本题
其他路线的聚合分数和粗结构签名，但生成器历史仍按路线隔离。

## 9. 错误恢复状态机

```text
allocated
  -> harness_call_started
       -> harness_archived
            -> kernel_call_started
                 -> kernel_archived
                      -> evaluation_started
                           -> valid_incorrect ---------> round_sealed
                           -> valid_correct_scored
                                  -> profile_started
                                       -> profile_complete/partial -> round_sealed
                                       -> profile_unavailable ------> round_sealed
                           -> environment_invalid ------> phase_paused
                 -> kernel_rejected --------------------> round_nondecision
       -> harness_rejected -----------------------------> repairable_attempt
```

所有 started 状态先追加预算预留事件，完成后追加结算；不能通过修改旧事件“退回”。恢复规则为：

| 中断点 | 恢复动作 | 是否重调模型/重评分 | 预算和排名 |
|---|---|---|---|
| 模型 started，归档已有完整原文 | 校验哈希后追加 recovered | 否 | 原调用只计一次 |
| 模型 started，无完整原文 | 追加 abandoned；新 attempt ID 才可重试 | 可重调，不能复用 ID | 两次调用都计费；不进正确率 |
| Harness 合同错误 | 保存 rejected raw，从最后有效父版本生成新 Harness | 最多一次自动修复 | 调用计费；不降性能排名 |
| Kernel 输出格式错误 | 关闭该 Harness；新子 Harness 才能再生成 | 不可在同 Harness 下重调 | Kernel 尝试和调用都计数 |
| evaluation started，无结果 | 先找评分归档；否则用新 attempt ID 重评同一源码 | 最多重评一次 | 每次 GPU 单独结算；无结果不进排名 |
| 环境无效 | 全局 P2c 熔断并跑只读 preflight | 人工恢复后可重评 | 不算正确性失败，不形成搜索结论 |
| 已评分，Profiler 中断 | 不重评分；恢复/重跑 Profiler | 最多两次 Profiler attempt | 分数立即保留；GPU 显式计费 |
| 精确重复 | 绑定同协议已有结果，不再上 GPU | 否 | Kernel/模型尝试计数；不增加样本量 |

单个 artifact slot 最多 1 次自动格式修复；同一路线连续两个模型 artifact attempt 无效时，路线
标为 `operationally_paused`，而不是“性能淘汰”。环境恢复需新的成功 preflight 事件和人工 resume
动作；运行器不得在异常循环中自动消耗剩余预算。

未结算的 started 尝试在恢复预算时按预留上界计入，直到追加可审计的完成或纠正事件。纠错使用
`p2c_fact_corrected` 引用原 event ID，不删除、覆写或重用原 ID。

## 10. 停止条件

### 路线停止或暂停

- 达到 9 次 P2c Kernel generation attempt、20 次模型调用或 1,800 GPU 秒中的任一硬帽；
- 最近 3 个 score-bearing 结果全部不正确，且期间没有可恢复环境错误；
- 连续两个模型 artifact attempt 无效时进入 operational pause，等待人工决定，不写成性能失败；
- S1/S2 未晋级时保留为 frozen，不删除；后续只可能通过预注册 wildcard/grace 复活；
- 路线达到其已分配 tranche 边界，不允许私自继续下一轮。

R 的单个恢复 Kernel 会使一条路线理论上最多得到 `1 + 2 + 2 + 2 + 2 = 9` 个新增 Kernel；没有
R 名额的路线最多 8 个。

### Task 停止

- 达到 16 次 Kernel attempt、40 次模型调用、3,600 GPU 秒、50 美元 API 或 50 美元 GPU
  费用中的任一硬帽，或剩余预算不足以预留下一完整动作；
- S1/S2 后没有符合条件的路线；
- S3 的当前第一名既无 2% 可信提升，也已用完一次结构 grace；
- 所有路线都因正确性、操作暂停或路线硬帽而不可运行；
- 评分器/GPU/SSH preflight 无效时仅记 `paused_environment`，不记科学完成。

### 全局停止

- 两题合计达到 32 次 Kernel attempt、80 次模型调用、7,200 GPU 秒、100 美元 API 或 100
  美元 GPU 费用中的任一硬帽；
- 两个 Task 都到达自己的科学停止或预算停止；
- 用户中止。中止保留已完成事实和预留成本，恢复仍受原 plan 和剩余硬帽约束；
- P2c 完成后只冻结并报告，绝不自动进入 P3。

若最后一个允许的 tranche 得到新的 2% 可信全局提升，也只能记录“在 P2c 上限处仍有动量”，
不能静默增加预算。任何追加都必须再建立新 phase 和新授权预算。

## 11. 预算上限和记账口径

| 范围 | Kernel generation attempts | 模型调用 | GPU 秒 | API 美元 | GPU 美元 |
|---|---:|---:|---:|---:|---:|
| 每条路线 | 9 | 20 | 1,800 | 25 | 25 |
| 每个 Task | 16 | 40 | 3,600 | 50 | 50 |
| P2c 全局 | 32 | 80 | 7,200 | 100 | 100 |

每题 16 个 Kernel 的最坏分配可机械展开为 `R:4 + S1:4 + S2:4 + S3:4`；实际 recoverable
路线或 challenger 少于上限时不补满。40 次调用等于 16 个正常 Harness/Kernel 对所需的 32 次，
再加 8 次显式格式/中断恢复余量。7,200 GPU 秒是 P2b 全局 GPU 硬帽的一半，同时给昂贵的
Tier A Profiler 恢复留出空间；这是独立新预算，不是 P2b 余量结转。

Kernel attempt 从 candidate model call started 时计数，格式无效或重复也不返还。正常 16 个 Kernel
需要 16 次 Harness 加 16 次 Kernel 模型调用；每题多出的 8 次模型调用只供 Harness 格式修复或
已开始无归档的显式 retry，不能转成突破 16 Kernel 上限的免费调用。

每个正确候选可做轻量摘要。完整 Tier A Profile 只用于：新的可信路线最好/全局最好、处于全局
2% 噪声带的新粗结构族，或恢复时确实缺少所需基线；每条路线最多 2 次、每题最多 6 次完整
Profile。Profiler retry 不增加此“成功完整 Profile”计数，但始终占 GPU 秒。

GPU 预算包含编译、正确性、测速、Profiler 和失败/中断尝试的实际或保守预留时间。费用必须用
plan 中冻结的单价换算；若自有 GPU 没有可审计单价，就把费用记为 0 并明确 `unpriced`，仍以
GPU 秒硬帽控制。登录态 Codex 当前可能报告 0 美元，但模型调用数和 usage 必须照记，且不得
自动切换 TokenRouter 或其他模型。

预算恢复从 started/reserved/settled 事件逐笔重放，不能信任某个可覆写的“最新剩余数”。每个
decision snapshot 同时保存 global、task、route 三层 `used/reserved/remaining`。

## 12. 追加账本事件

P2c ledger 是唯一事实来源。至少实现以下事件；所有事件都带 `phase=P2C`、`plan_sha256`、
`task_id`（适用时）、内容哈希和 `budget_before/budget_after`（发生资源变化时）：

| 事件 | 关键字段 |
|---|---|
| `p2c_source_snapshot_frozen` | 源 ledger/plan 哈希、事件数、评分协议、候选 manifest |
| `p2c_phase_changed` | `prepared/started/paused/completed`、原因、授权 ID |
| `p2c_route_imported` | 源 route、最后有效/最快配对、源停止分类、源成本 |
| `p2c_recovery_classified` | score 是否可复用、缺失 artifact、R 名额和理由 |
| `p2c_decision_snapshot` | `G_raw/G_credible`、A/F/M/C/N、priority、排序、公式版本 |
| `p2c_tranche_allocated` | stage、席位、路线、2 轮或 R 的 1 轮、wildcard/grace 理由 |
| `p2c_model_call_started/completed/failed` | attempt、kind、prompt hash、usage、费用、父指针 |
| `p2c_harness_archived/rejected` | policy hash、parent、合同错误和 raw archive |
| `p2c_candidate_archived/rejected` | Kernel hash、唯一 Harness ID、raw archive |
| `p2c_evaluation_started/completed` | evaluator hash、correct、精确 timing、speedup、GPU 成本 |
| `p2c_profile_started/completed/unavailable` | level、公开摘要、私有路径哈希、缺失指标、GPU 成本 |
| `p2c_attempt_abandoned/recovered` | 原 attempt ID、新 attempt ID（若有）、是否重调/重评 |
| `p2c_round_sealed/nondecision` | 最终事实、是否进入排名、错误类别、父 Harness/Kernel |
| `p2c_tranche_completed` | tranche 前后最好、2% 判定、正确率、新粗结构族、成本 |
| `p2c_route_state_changed` | eligible/frozen/operationally_paused/exhausted 和 reason code |
| `p2c_task_stopped` | scientific/budget/environment/user stop，不能混用 |
| `p2c_fact_corrected` | 被纠正 event ID、旧/新解释、证据；旧事件不变 |

event ID 对同一事实幂等，但 retry 必须有新 attempt ID。任何事件不得只写自由文本而缺少机械
reason code。P2b 账本只读且哈希不变是 P2c 完成审计的一部分。

## 13. 看板变化

新 `dashboard.html` 只从 P2c ledger 和冻结源快照重建，至少显示：

- 每题分开的 `G_raw`、`G_credible`、冻结 P1/P2/P2b 前沿和当前 P2c 数值最好；
- P2b 源曲线用灰色只读区，P2c R/S1/S2/S3 用不同背景区，不能把两个账本画成同一阶段；
- 每个 decision epoch 的 A/F/M/C/N、priority、名次、晋级/替补/未晋级理由；
- 每条路线的父 Harness/Kernel、当前 tranche、已分配与剩余轮次、正确率和粗结构族；
- 正确点、正确性失败、重复、格式错误、环境错误，以及“已评分未封存”的独立视觉状态；
- source cost 与 P2c incremental cost 分栏，以及 global/task/route 三层硬帽进度；
- Profile 级别、真实可用指标和显式 `unavailable`，理论 occupancy 不能标作 achieved；
- task stop、environment pause、budget stop 和 user stop 的不同状态；
- 页面顶部持续显示“P3 未授权/未启动”。

看板上的精确分数、排名分量和预算都必须能追溯到 event ID；页面是可丢弃物，不反向成为事实。

## 14. 测试矩阵

| 类别 | 必测场景 | 关键断言 |
|---|---|---|
| plan/snapshot | P2b 未完成、writer 活跃、源哈希变化、artifact 位于 worktree | 全部拒绝；准备零模型/零 GPU |
| 历史隔离 | 两 Task 同名策略和不同余额 | 排名/余额/停止互不读取，预算不可借用 |
| 事实归一 | 正确、不正确、格式错、环境错、重复、已评分未封存 | 只有规定事实进入 `n/c/B` |
| 2% 边界 | 1.019999、1.020000、原始分数四舍五入相同 | 只有精确比值达到阈值才可信 |
| 排名公式 | 五分量 golden cases、噪声并列、确定性 tie-break | 从 snapshot 可逐字节复算同一排序 |
| 低起点保护 | reference→19× 与 19.8× 前沿路线 | 起点涨幅不进入 priority；可信近期斜率仍有效 |
| 结构新颖度 | 只改 warps/stages、粗结构变化、低分新结构 | 前两者分别不新颖/新颖；低于 0.9G 无奖励 |
| 分配器 | R、S1 top-2、wildcard 替换、S2 challenger、S3 grace | tranche/席位/上限完全符合预注册规则 |
| 调度 | 两路线两轮、epoch 反转、两 Task 共用 GPU4 | 只有一个模型/GPU 动作，epoch 内结果不改分配 |
| 一对一合同 | Kernel 格式失败后重试、Harness 回滚 | 每个 Harness 最多一个 Kernel attempt，新调用有新父版本 |
| 模型恢复 | started 后有归档、无归档、单次/连续格式错 | 不重复 ID/计费；一次可修，连续两次 operational pause |
| 评分恢复 | started 后有结果/无结果/环境无效 | 能恢复则零 GPU；重评显式计费；环境错误不算 incorrect |
| Profiler 恢复 | 分数已保存、摘要缺失、两次中断 | 从不重评分；最终 unavailable；缺失指标不伪造 |
| 预算恢复 | started 未 settled、实际超预留、三层任一硬帽 | 保守计费，不能超 route/task/global cap |
| 追加账本 | 重跑同一完成事件、retry、事实纠正 | 完成幂等；retry 新 ID；旧事实永不覆写 |
| 看板 | 各类错误、未封存分数、排名和预算 | HTML 显示精确来源且不泄露私有路径 |
| 离线端到端 | fake 两题跑到最坏分配路径并恢复 | ≤32 Kernel、≤80 调用、≤7200 秒且零新增恢复调用 |
| 无 P3 入口 | CLI、runner、phase transition 全局搜索 | 不存在自动 P3/P4/Builder 路径 |

真实预检只对一个已冻结正确候选做：评分协议哈希检查、GPU4 可见性、一次轻量 Profile 和一次
中断恢复演练。预检不得调用模型，也不得把结果反馈为搜索分数。

## 15. 建议实现边界

新增而不改写 P2b 主路径：

- `optimization_lab/p2c_plan.py`：源快照、预算、路线和授权合同；
- `optimization_lab/p2c_ranking.py`：事实归一、粗结构族、五分量和分配器；
- `optimization_lab/p2c_runner.py`：R/S1/S2/S3、串行队列和恢复状态机；
- `optimization_lab/p2c_dashboard.py`：只读物化视图；
- `scripts/prepare_kernelbench_p2c.py`：零调用准备与冻结；
- `scripts/run_kernelbench_p2c.py`：只接受已签名 plan 和显式授权文件；
- 对应 `tests/test_p2c_plan.py`、`test_p2c_ranking.py`、`test_p2c_runner.py`、
  `test_p2c_dashboard.py`。

可以复用 `ExperimentRegistry`、候选/策略 archive、评分 adapter 和 SSH Profiler，但 P2c 事件前缀、
plan、预算恢复与 runner 必须独立。实现时先写上述红测，再做 fake 全流程；不得为了复用而放宽
P2b 的 8/15、120/14,400 合同。

## 16. 启动门禁

以下条件必须全部满足，`run` 才能从 prepared 进入 started：

1. 用户在实现和预检报告完成后，另行明确授权 **P2c 真实执行及本方案预算**；本计划本身不是
   执行授权；
2. P2b 已追加 phase completed/frozen 事实，进程退出，writer lock 可非阻塞取得；早停路线允许
   因已审计的 recoverable reason 少于 8 轮；
3. P1/P2/P2b 源账本、plan、候选、Harness、任务、KernelBench commit 和评分协议哈希全部通过；
4. 准备器已写不可变 source snapshot，P2b 原账本在准备前后 SHA-256 相同；
5. `gpt-5.6-sol`、`a100jump` GPU4/A100-SXM4-80GB、正确性/性能次数和串行设置与冻结协议一致；
6. P2c 单测、fake 最坏路径、断点恢复、预算审计、隐私检查和“无 P3 入口”测试全绿；
7. A100 只读 preflight 成功；`nsys`/Triton cache/`cuobjdump` 能力重新记录，`ncu` 与硬件计数器
   缺失继续明确为 unavailable；
8. `p2c_plan.json` 精确冻结 32/80/7,200、两个 16/40/3,600 task cap、美元帽、单价状态和
   formula version；
9. 初始 dashboard 能从空 P2c ledger + source snapshot 重建，私有目录权限和剩余磁盘合格；
10. 没有 P3、P4、Builder、TokenRouter fallback 或自动扩预算入口。

任一门禁失败都只能保持 `prepared` 或 `paused_environment`。不得用部分 P2b 实时账本先跑一题，
也不得因另一题有闲置预算而突破本题硬帽。

## 17. 当前证据如何进入首个快照

以下只说明公式行为，不是提前冻结晋级结果；真实排名必须等待 P2b 完成后的 source snapshot：

- LayerNorm `architecture_reset` 的 `18.757→19.160` 达到约 2.15% 路线最好提升，会贡献近期可信
  斜率；从 1.000× 起步的巨大百分比不进入公式；
- `counterfactual` 当前最好 19.659×，其 v005 Harness 合同错误不算 incorrect，也不降低
  `C_l`，并先获得 R 名额；
- `profile_exploit` v001 的 19.273× 评分直接保留，Profiler 中断不重评分，该路线先恢复摘要并
  获得 R 名额；
- `recombinant_frontier` 的 19.818× 是强绝对前沿事实，但若相对既有 P1 约 19.86× 不足 2%，
  只能称处于同一噪声带，不能称可信刷新；
- Matmul+Sigmoid+Sum 与 LayerNorm 分开快照、分开排名，当前仍增长的 P2b 事实不得被本计划
  提前截取。

## 18. 完成边界

P2c 完成时冻结所有 Harness/Kernel 配对、排名快照、错误、成本和 task stop reason，生成一次
只读总结后停止。P2c 的结果仍只支持“固定两个 benchmark instance 上的任务专化搜索”结论。
P3、扩 Task 或再次追加自适应预算都需要新的方案、phase、硬帽和用户授权。
