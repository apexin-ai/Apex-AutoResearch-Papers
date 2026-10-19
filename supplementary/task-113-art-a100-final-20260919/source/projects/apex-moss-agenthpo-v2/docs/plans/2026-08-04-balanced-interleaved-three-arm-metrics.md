# 平衡交错三臂执行与固定八轮统计

日期：2026-08-04

本说明取代当日 suite-blocked 执行说明，控制 v1r7 及其后继 clean segment。三臂、每臂八轮、预算、评测器、恢复语义、test-then-learn 权限以及固定八轮平均统计均不变；只修订 24 题流顺序。

## 冻结执行流

八个 task block 依次对应每个 suite 的题目位置 1–8。每个 block 恰含 YAHPO-LCBench、CompilerGym cBench、SWE-bench Verified 各一道题；首发 suite 按 block index 对三套 suite 循环轮转：

- block 1：YAHPO → CompilerGym → SWE-bench；
- block 2：CompilerGym → SWE-bench → YAHPO；
- block 3：SWE-bench → YAHPO → CompilerGym；
- 后续重复该三步轮转。

这样三套 benchmark 大致同时经历模型服务、远端负载和 Builder 成熟阶段，且没有 suite 永远占据 block 的较早或较晚位置。每 suite 的位置 1–6 为 `online`，当前题三臂全部封存后只蒸馏 B-online 自身轨迹，checkpoint 只影响混合流中的下一道未见题；位置 7–8 为 `sealed`，只评分不学习。B-frozen 始终不吸收跨题经验。

staging 使用 schema v4，并必须逐字声明 `stream_policy=balanced_interleaved`。完整合同机械检查每个 block 的 suite 轮转、block index、6+2 learning mode、arm rotation 和逐 cell entitlement；suite-blocked 或任意其他排列均拒绝。

## 冻结统计

对 benchmark `b`、其中任务位置 `i`、arm `a`：

`task_mean(b, i, a) = sum(round_score(b, i, a, v), v=1..8) / 8`

仅 `correct=true` 的有限数值使用原值；合同拒绝、错误、缺失、不正确或非数值轮次均记 0，分母不缩小。每个 suite 的学习期配对优势为：

`delta_i = task_mean(b, i, B-online) - task_mean(b, i, B-frozen), i=1..6`

五报告必须分别给出六个 `delta_i`、六题平均、任务位置 1–6 的 OLS 斜率、`delta_6-delta_1`，以及位置 7–8 的 sealed holdout。原始分数不跨 benchmark 求平均；跨 benchmark 只汇总相对优势 `delta_i / abs(B-frozen task mean)`，分母不大于 `1e-12` 时记 undefined。

## Segment 边界

v1r6 已在 suite-blocked 合同下消费 42/576 rounds、5/72 arms、1/24 instances，并在用户切换顺序时停止；最后一个 started-without-artifact operation 保留、计费且永不重发。v1r7 必须使用新 revision、新 schema、新 staging、新 artifact root 和空 Experience Bank，不能复制 v1r6 的 checkpoint、Experience Record、round、arm 或 instance receipt。

只有 24/24 instance、72/72 arm、576/576 round 全部封存后，才能生成 `report/score_curve.html`、`score_curve.json`、`summary.json`、`summary.md`、`results.csv`。
