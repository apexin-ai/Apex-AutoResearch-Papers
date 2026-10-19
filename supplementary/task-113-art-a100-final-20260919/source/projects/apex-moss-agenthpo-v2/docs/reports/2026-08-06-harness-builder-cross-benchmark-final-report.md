# Moss Harness Builder 跨 Benchmark 三臂正式实验报告

日期：2026-08-06  
状态：正式 campaign 已完成并封存  
实验单元：24 instances × 3 arms × 8 rounds = 576 rounds

## 1. 结论摘要

本实验完成了 YAHPO Gym/LCBench、CompilerGym cBench 和 SWE-bench Verified 三种异质任务结构的
三臂比较：

- `A`：只在 v001 构建一次 task-conditioned Harness，随后冻结 Harness；
- `B-frozen`：在当前 instance 内逐轮进化 Harness，但不读取跨题经验；
- `B-online`：与 B-frozen 从逐字相同空状态起步，允许读取已经封存的自身前题经验。

正式结果支持两个不同强度的结论：

1. **题内 Harness 进化有明确价值。** LCBench 的 8/8 个 instance 上，B-frozen 的有效轮均值均高于
   A；CompilerGym 在双方都满足有效性门槛的 6 个 instance 上也全部高于 A，并把 A 为 0/8 的
   `crc32`、`blowfish` 恢复为 8/8。SWE-bench 的分数存在二值 ceiling，不能用均值区分已解决候选，
   但 B-frozen 达到 4/8 门槛的 instance 为 6/8，A 只有 2/8，说明题内 Harness 主要提高了可靠生成率。
2. **跨题 B-online 尚未证明稳定优于 B-frozen。** LCBench 前六题为 4 胜 2 负，CompilerGym 为
   3 胜 3 负；两套 suite 的 held-out 各为 1 胜 1 负。SWE-bench 前六题只有 4/6 个 instance 同时满足
   B-frozen/B-online 的 4/8 门槛，未通过预注册的 5/6 suite gate，不能发布跨题总体性能结论。

因此，当前最稳健的论文陈述是：

> Moss 已在三种机制异质的 Benchmark 上证明 instance-conditioned、round-by-round Harness
> recompilation 能改善分数或生成可靠性；现有少量 held-out 结果尚不足以证明跨 instance Experience
> Bank 带来一致的正迁移。

## 2. 与相关工作的 held-out 对齐

当前协议已经包含一个小型 held-out 实验，与相关工作常用的“先优化、再冻结、最后测未见任务”结构对齐：

- 每个 suite 的位置 1–6 执行严格 test-then-learn；
- 当前 instance 三臂全部封存后，才允许 B-online 蒸馏自己的公开轨迹；
- 每个 suite 的位置 7–8 为 sealed held-out，只评分、不学习；
- 因而 held-out 共 6 个 instance，不存在从 held-out 分数回写 Experience Bank 的路径。

它在概念上接近 Meta-Harness 的 search/test 分离、Living-Harness 的 evolved-state reuse，以及
Penguin/GDPevo 的冻结 Benchmark 或 train/test 后复用 Skill/Agent State；不同之处是 Moss 冻结的是
经过可信编译的结构化 Harness 状态，并在三种不同动作空间中复用同一实验合同。

这只是小样本 exploratory holdout：每个 suite 只有两题，结果应逐题报告，不能把六题的原始分数混合，
也不能据此声称 Task-level 普适迁移。

## 3. 正式协议与统计口径

- 24 题按冻结的 balanced-interleaved 流串行执行；每个 task block 含三个 suite 的同位置题，首发
  suite 循环轮转。
- 每个 instance/arm 固定 v001–v008 八次尝试。
- `valid_mean` 和 `best` 只使用 `correct=true` 且 score 为有限数值的轮次。
- 少于 4/8 个有效轮标记 `insufficient_validity`，保留描述值但不进入推断比较。
- 每个 suite 前六题至少 5/6 同时满足 B-frozen 和 B-online 的 4/8，才通过跨题发布门禁。
- 不计算 benchmark 内 task 原始分数均值，也不跨 benchmark 混合原始分数。
- SWE-bench trust grade 为 `official_standard_candidate_visible_test_process`；它不是隐藏测试或对抗式
  防作弊评分。

## 4. 完整逐题结果

表格格式为 `有效轮均值 / 最佳分数 (有效轮数/8)`；`Online−Frozen` 只有双方均达到 4/8 时才显示。

### 4.1 YAHPO Gym / LCBench

| Pos | Instance | Split | A mean/best (valid) | B-frozen mean/best (valid) | B-online mean/best (valid) | Online−Frozen |
|---:|---|---|---:|---:|---:|---:|
| 1 | `167168` | online | 0.789872 / 0.815232 (7/8) | 0.854119 / 0.868898 (8/8) | 0.838057 / 0.853369 (7/8) | -0.016062 |
| 2 | `168331` | online | 0.690448 / 0.711457 (8/8) | 0.740247 / 0.747769 (7/8) | 0.770196 / 0.792518 (8/8) | +0.029949 |
| 3 | `168910` | online | 0.767184 / 0.804694 (8/8) | 0.798444 / 0.821551 (8/8) | 0.800740 / 0.834170 (7/8) | +0.002296 |
| 4 | `189866` | online | 0.717724 / 0.728459 (8/8) | 0.735223 / 0.745832 (8/8) | 0.755049 / 0.771847 (8/8) | +0.019827 |
| 5 | `167181` | online | 0.724135 / 0.740235 (7/8) | 0.765481 / 0.788622 (8/8) | 0.772476 / 0.784924 (7/8) | +0.006995 |
| 6 | `167190` | online | 0.813345 / 0.837018 (7/8) | 0.819109 / 0.824406 (8/8) | 0.806765 / 0.809760 (8/8) | -0.012344 |
| 7 | `34539` | sealed | 0.645158 / 0.672241 (8/8) | 0.655478 / 0.709240 (8/8) | 0.632441 / 0.650033 (6/8) | -0.023037 |
| 8 | `189908` | sealed | 0.901782 / 0.905158 (7/8) | 0.905934 / 0.907835 (7/8) | 0.924942 / 0.933141 (8/8) | +0.019008 |

有效性：A 60/64、B-frozen 62/64、B-online 59/64 个有效轮；三个 arm 的 8 个 instance 均达到
4/8。前六题 paired gate 为 6/6，通过。

### 4.2 CompilerGym cBench

| Pos | Instance | Split | A mean/best (valid) | B-frozen mean/best (valid) | B-online mean/best (valid) | Online−Frozen |
|---:|---|---|---:|---:|---:|---:|
| 1 | `dijkstra` | online | 1.450099 / 1.660517 (8/8) | 1.575902 / 1.724138 (7/8) | 1.278032 / 1.730769 (8/8) | -0.297870 |
| 2 | `crc32` | online | — / — (0/8) | 1.877310 / 2.122807 (8/8) | 2.109350 / 2.122807 (8/8) | +0.232041 |
| 3 | `stringsearch2` | online | 1.844540 / 2.086580 (8/8) | 1.958594 / 2.042373 (8/8) | 2.065543 / 2.190909 (8/8) | +0.106949 |
| 4 | `susan` | online | 2.272503 / 2.415348 (8/8) | 2.315676 / 2.411839 (8/8) | 2.287132 / 2.425493 (8/8) | -0.028544 |
| 5 | `qsort` | online | 1.194433 / 2.162712 (8/8) | 1.732718 / 2.162712 (8/8) | 1.794918 / 2.148148 (8/8) | +0.062199 |
| 6 | `bitcount` | online | 1.944227 / 2.040476 (8/8) | 2.051744 / 2.095355 (8/8) | 2.048020 / 2.095355 (8/8) | -0.003725 |
| 7 | `blowfish` | sealed | — / — (0/8) | 1.956333 / 1.977676 (8/8) | 1.961313 / 2.009278 (8/8) | +0.004980 |
| 8 | `bzip2` | sealed | 1.792597 / 2.053429 (8/8) | 1.845488 / 1.987693 (8/8) | 1.834902 / 2.002368 (8/8) | -0.010586 |

有效性：A 48/64、B-frozen 63/64、B-online 64/64 个有效轮；达到 4/8 的 instance 分别为
6/8、8/8、8/8。前六题 paired gate 为 6/6，通过。

### 4.3 SWE-bench Verified

| Pos | Instance | Split | A mean/best (valid) | B-frozen mean/best (valid) | B-online mean/best (valid) | Online−Frozen |
|---:|---|---|---:|---:|---:|---:|
| 1 | `sphinx-doc__sphinx-8459` | online | 1.000000 / 1.000000 (1/8) | 1.000000 / 1.000000 (7/8) | 1.000000 / 1.000000 (5/8) | +0.000000 |
| 2 | `django__django-14500` | online | 1.000000 / 1.000000 (5/8) | 1.000000 / 1.000000 (6/8) | 1.000000 / 1.000000 (8/8) | +0.000000 |
| 3 | `pytest-dev__pytest-7205` | online | — / — (0/8) | — / — (0/8) | 1.000000 / 1.000000 (3/8) | ineligible |
| 4 | `matplotlib__matplotlib-25775` | online | 1.000000 / 1.000000 (3/8) | 1.000000 / 1.000000 (6/8) | 1.000000 / 1.000000 (6/8) | +0.000000 |
| 5 | `pydata__xarray-4356` | online | 1.000000 / 1.000000 (1/8) | 1.000000 / 1.000000 (4/8) | 1.000000 / 1.000000 (6/8) | +0.000000 |
| 6 | `sympy__sympy-21930` | online | 1.000000 / 1.000000 (5/8) | 1.000000 / 1.000000 (6/8) | 1.000000 / 1.000000 (3/8) | ineligible |
| 7 | `astropy__astropy-13977` | sealed | 1.000000 / 1.000000 (2/8) | 1.000000 / 1.000000 (7/8) | 1.000000 / 1.000000 (5/8) | +0.000000 |
| 8 | `pylint-dev__pylint-4604` | sealed | — / — (0/8) | — / — (0/8) | 0.045455 / 0.045455 (1/8) | ineligible |

有效性：A 17/64、B-frozen 36/64、B-online 37/64 个有效轮；达到 4/8 的 instance 分别为
2/8、6/8、5/8。前六题 paired gate 只有 4/6，失败，因此不发布 SWE 跨题均值、斜率或总体
B-online 优势。已通过门禁的五个 B-frozen/B-online pair 均受 `score=1` ceiling 限制，区别主要体现在
有效生成率。

## 5. Held-out 结果

| Suite | Held-out 1 | B-online vs B-frozen | Held-out 2 | B-online vs B-frozen | 解释 |
|---|---|---:|---|---:|---|
| LCBench | `34539` | -0.023037 | `189908` | +0.019008 | 一负一正，无一致方向 |
| CompilerGym | `blowfish` | +0.004980 | `bzip2` | -0.010586 | 一正一负，幅度较小 |
| SWE-bench | `astropy-13977` | 0.000000 | `pylint-4604` | ineligible | 前者 ceiling tie，后者有效性不足 |

这个 held-out 结果没有显示稳定的跨题正迁移。它仍然有研究价值：Moss 的 B-online 经验没有因为
题内调优而自动在未反馈题上占优，说明后续工作应优化 Experience Record 的选择、压缩与适用条件，
而不是扩大“已经证明泛化”的叙事。

## 6. 轮次、有效性与失败分类

576 个正式 round 的终态如下：

| Outcome | Rounds |
|---|---:|
| `valid` | 446 |
| `contract_rejected` | 95 |
| `planner_contract_rejected` | 28 |
| `planner_operation_abandoned` | 1 |
| `planner_operation_failed` | 5 |
| `solution_operation_failed` | 1 |

按 suite 的有效轮数为：LCBench 181/192，CompilerGym 175/192，SWE-bench 90/192。SWE 的主要限制
不是已评分 patch 的分数，而是严格 patch/执行合同下能否稳定产生可评分候选。

正式 operation journal 记录了 6 个 terminal failed operation，全部为
`provider_or_transport_error`：pytest A planner v001、xarray A sham planner v002–v005，以及 sympy
B-frozen solution v001。另有两个 started-without-result operation 被永久计费并通过明确的 abandoned
round 恢复：v1r8 被排除的 scikit-learn A sham planner v002，以及 v1r9 pytest A sham planner v002。
这些 operation ID 均未重发。

## 7. 资源、调用与账本完整性

| Segment | Journal events | Operations | Completed | Failed | Started/charged | Model calls | Evaluator tx | CPU evaluator seconds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| v1r8 source prefix journal | 1,244 | 415 | 414 | 0 | 1 | 286 | 129 | 1,695.356 |
| v1r9 successor | 3,659 | 1,220 | 1,213 | 6 | 1 | 853 | 367 | 3,217.339 |
| Total consumed evidence | 4,903 | 1,635 | 1,627 | 6 | 2 | 1,139 | 496 | 4,912.695 |

总调用中包含 v1r8 scikit-learn 排除尾部的 3 个已消费 model call；它们不进入学习或性能结果。
18 次 distillation 均为 completed，分别对应三个 suite 的 6 个 online instance。

1,139 个记账 model call 中有 1,131 个可信 result artifact；其余 8 个对应上述 6 个 terminal failure
与 2 个 started-without-result。可见 artifact 的 usage 合计：

- input tokens：220,231,232，其中 cached input tokens 184,561,920；
- output tokens：1,615,860；
- reasoning output tokens：719,173；
- ledger `api_cost_usd`：0.0，原因是使用 ChatGPT 登录态 `codex exec`，不应解释为实际算力成本为零。

完整性锚点：

- v1r8 trusted operation head：`0580a40de229e7482b7e0db04ffdb0942e7a07614f6a7b5a4e1a9b3fb22aacf3`；
- v1r9 trusted operation head：`5eb0ead96c8e084824326725def4de8fec0fb56c9de4f4b94f14e34426dbae5c`；
- v1r9 campaign summary：`d76c13fa1d49abdbaf1a90130649296c5d641c3ed69b4900ea948d5031eab150`；
- references-only composition manifest：`169fcd18a950b65b081911791d7761369bb5e441a1e8daf27a662656237b2415`。

两个 journal 均已独立重放并与外置 trusted head 一致。正式 runner 由 systemd 于
2026-08-06 07:27:49 UTC 以 `0/SUCCESS` 自然退出；没有为了生成报告而重启 runner、模型或 evaluator。

## 8. 与 Meta-Harness、Living-Harness、Penguin 的证据边界

- 相对 Meta-Harness，本实验没有证明 Moss 在开放代码搜索空间中找到更强的全局 Harness；它证明的是
  受约束 Harness recompilation 在逐 instance、逐 round 反馈下的效果和恢复可靠性。
- 相对 Living-Harness，本实验不仅更新 Memory/State Graph，而是改变角色、工具/记忆路由、工作流与
  恢复配置；但跨题状态复用没有稳定胜过无跨题经验的 B-frozen。
- 相对 Penguin，本实验的直接优化对象不是 AGENTS.md/Skill/有限配置，而是类型化 HarnessDecision；
  结果说明这一更细粒度结构优化对题内适应有效，但尚不能替代独立的 held-out 泛化证据。

下一步若要与相关工作同台比较，应在相同模型、相同 evaluator transaction 与 model-call 预算下，加入
Meta-style open code search、Penguin-style Agent-State/Skill optimization 和 Moss typed compilation 三个
optimizer，并继续保留独立 held-out。该实验需要新的冻结方案，不能向当前已完成 campaign 追加 arm。

## 9. 产物索引

- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/results.csv`：72 个 instance-arm 行；
- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/summary.json`：完整结构化结果与 provenance；
- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/summary.md`：机械生成的完整 72 行表；
- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/score_curve.json`：逐题曲线数据；
- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/report/score_curve.html`：可视化报告；
- `results/optimization_lab/hb-three-arm-composite-v1r8-v1r9/composition_manifests/169fcd18a950b65b081911791d7761369bb5e441a1e8daf27a662656237b2415.json`：只引用、不复制 receipt 的 composition manifest。

报告生成代码修复提交为 `3d32499`，经验记录提交为 `abc7113`。该修复只允许被 continuation snapshot
精确原始 SHA 绑定的历史 pretty JSON staging plan；所有 instance/arm receipt 的 canonical JSON、sealed
状态和逐层内容哈希要求保持不变。
