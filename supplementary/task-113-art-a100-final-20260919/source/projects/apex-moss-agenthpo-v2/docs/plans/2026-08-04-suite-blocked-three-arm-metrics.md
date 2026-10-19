# Suite-blocked 三臂执行与统计冻结说明

> 已由 `2026-08-04-balanced-interleaved-three-arm-metrics.md` 取代。本文件只描述已消费并停止的 v1r6，
> 不再授权新的正式 segment。

日期：2026-08-04

本说明只修订当前 YAHPO Gym/LCBench、CompilerGym cBench、SWE-bench Verified 三臂正式实验的任务流与报告口径；预算、三臂定义、评测器、模型签名、逐 cell 恢复和 test-then-learn 权限边界不变。它取代此前“平衡交错流 + 跨任务逐轮 running-best 汇总”的当前执行约定，不改写已经消费的 v1r1–v1r5 segment。

## 冻结执行顺序

正式流为三个连续 suite block：

1. YAHPO-LCBench 八题；
2. CompilerGym cBench 八题；
3. SWE-bench Verified 八题。

每个 suite 内保持既有八题顺序。任务 1–6 为 `online`：当前题三臂和八轮全部封存后，才允许只从当前题 B-online 公开轨迹蒸馏一次，结果只影响下一道未见题。任务 7–8 为 `sealed`：只评分、不学习。B-online checkpoint 跨 suite 边界继续前传；B-frozen 始终不吸收跨题经验。三臂在每题内的轮换顺序、每臂八轮和不可借用预算不变。

这样可把两个信号分开：每个 suite 第一题的 `B-online − B-frozen` 反映进入新 benchmark 时已有经验的迁移；同 suite 前六题的优势变化反映连续同域 test-then-learn 的增长。

## 冻结主指标

对 benchmark `b`、其中任务位置 `i`、arm `a`，主分数为固定八轮平均：

`task_mean(b, i, a) = sum(round_score(b, i, a, v), v=1..8) / 8`

只有 `correct=true` 且有限数值的 round score 使用原值；格式拒绝、错误、缺失、非数值或不正确轮次均记 0。分母始终为 8，不能只平均有效轮，也不能挑历史最好。

每个 suite 的学习期逐题配对优势为：

`delta_i = task_mean(b, i, B-online) - task_mean(b, i, B-frozen), i=1..6`

必须报告：六个 `delta_i`、六题平均优势、以任务位置 1–6 为自变量的普通最小二乘斜率，以及 `delta_6 - delta_1`。任务 7–8 的相同指标单列为 sealed holdout，不进入学习期斜率。

三个 benchmark 的原始分数量纲不同，禁止直接求总平均。跨 benchmark 摘要只使用各 suite 内的相对优势：

`relative_delta_i = delta_i / abs(task_mean(b, i, B-frozen))`

当分母绝对值不大于 `1e-12` 时该项为 undefined，不以任意大数代替。

## 产物和完成门禁

新协议使用 staging schema v3，并要求 `stream_policy=suite_blocked`。只有 24 个 instance receipt、72 个 arm receipt、576 个 round JSON 全部一致后，才能一次生成以下五份正式报告：

- `report/score_curve.html`
- `report/score_curve.json`
- `report/summary.json`
- `report/summary.md`
- `report/results.csv`

v1r5 的 38 个 round、4 个 arm、1 个 instance 及无结果的在途 evaluator operation 保留为旧协议消费证据，不导入新 Experience Bank、不补写、不退款、不用新代码原地恢复。新实验必须使用新 revision、新 staging 和新 artifact root。
