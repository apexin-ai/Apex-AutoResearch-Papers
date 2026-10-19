# ApexTune QD-v4 (code-v4) — 搜索架构结构说明

Collection: `aif360-apextune-structure-history-20260912`
分支: `feat/fml-apextune-integration`（agent-ml-research）
提交序列（每项改动一个提交，全部带测试）:

| 提交 | 内容 |
|---|---|
| `384bc6c45` | code-v3 实现冻结基线（structure-first v3，本序列的对照起点） |
| `2da4922df` | 机制一：stall 驱动的 tune cooldown + seed/uniform restart |
| `a1440296c` | 机制二：ε-band elite pool（近优骨架可采样保留） |
| `841b0104c` | 机制三：AIF360 行为轴 QD frontier（取代 AST hash % 16） |
| `4ece41477` | 机制四：batch 级分解 bandit 观测 |
| `c5e2b303c` | 审计修复：失败 validation 步不再被强制要求主指标 |

运行入口: `uv run apextune-fml --task aif360 --round R --seed S --run-id ... --model gpt-5.6-sol --allow-model-override --allow-reconstructed --allow-noncomparable`（诊断口径）。

## 模块地图

```
core/research/llmloop/
  qd_archive.py            MAP-Elites 式行为档案（cell/elite/pool/history、parent 采样）
  budget_bandit.py         mutate/tune 二臂折扣 Thompson（batch 级观测）
  fml/
    campaign.py            FMLCampaignConfig（全部新参数）、SEARCH_KERNEL 声明、seed()
    _campaign_kernel.py    批次决策核心：stall 计账、restart/cooldown、HPO 编排、批级 bandit 观测
    _campaign_search.py    validation 记账、archive admission（admission_kind/pooled 标注）
    _campaign_persistence.py  campaign identity 哈希（新参数全部参与）、manifest/summary 落盘
    _campaign_state.py     state schema 与 summary payload（stall/pool 审计字段外显）
    aif360.py              AIF360 adapter；behavior_axes() 行为轴声明
    _aif360_support.py     BEHAVIOR_AXES 常量（固定绝对分箱）
    reporting.py           final-test 计分与三轮聚合审计（含本轮审计修复）
    cli.py                 frontier 轴装配：adapter.behavior_axes() 优先，AST bucket 回退
```

## 机制一：stall 响应（tune cooldown + 周期 restart）

- `stalled_batches`：持久计数器，一次「未产生全局最优的 batch 决策」加一，出现全局最优归零。崩溃恢复后延续。
- **tune cooldown**：`stalled_batches >= stall_cooldown_batches`（默认 6）时，bandit 只被提供 mutate 臂——平台期不再烧 tune。
- **周期 restart**：每满 `stall_restart_period`（默认 4）个 stalled batch，该批 parent 改为 restart 抽取，在两种来源间交替：
  - `seed`：持久化 seed 锚点（`state.seed_parent`，seed elite 被顶掉后依然可用，从原始 baseline 变异）；
  - `uniform_cell`：均匀随机 archive cell（无视 priority 排序）。
- 每批写入 `stall_audit` 有界环（batch_id、stalled、cooldown、restart 种类、parent 来源），并进 summary metadata。

## 机制二：ε-band elite pool

- `qd_archive.admit(pool_keep, pool_epsilon)`：cell 除单一 elite 外保留最多 `elite_pool_size`（默认 3）个、分数在 `elite_pool_epsilon`（默认 0.02，相对）容忍带内、**skeleton 互异**的近优成员；新 elite 上位时被顶掉的原 elite 也进 pool（带内），出带成员被修剪。
- `sample_parent(pool_share)`：选中 cell 后以 `elite_pool_share`（默认 0.25）概率抽 pool 成员作 parent（`member=pool`），使同分/近分中性变体真实可达——这是 v3「同分变体全部丢弃、无中性网络」问题的直接修复。
- 步记录带 `pooled` 与 `admission_kind ∈ {new_cell, displaced_elite, pooled, rejected}`。

## 机制三：行为轴 QD frontier（AIF360）

- `AIF360Adapter.behavior_axes()` 返回**固定绝对分箱**（常量，绝不随观测最优漂移）：
  - `abs_aod_mean`: edges `[0.01, 0.02, 0.05, 0.1, 0.2]`
  - `cls_acc_mean`: edges `[0.63510101010101, 0.65, 0.665]`
- cell 由 evaluator 测得的行为（公平性水平 × 准确率余量）定义：行为等价的不同代码**坍缩进同一 cell**——v3 曾把同一行为散进 14 个 AST hash 桶造成伪多样性。
- AST-shape bucket 降级为每步 `ast_structure_bucket` 审计字段，并保留为未声明行为轴的 task（gcastle/art）的回退 frontier。

## 机制四：batch 级分解 bandit 观测

- 每个**消费了至少一次完整 validation** 的 batch 决策恰好产生一条 bandit 观测（v3 是每 validation 一条：100 条观测对 41 个决策、90% 为零）。
- reward = 全局最优改善量（metric 单位）+ `bandit_novelty_weight`（默认 0.02）× 新占据 cell 数 + `bandit_admission_weight`（默认 0.01）× 顶掉 elite 数；三成分原样写入观测 `components`，不进折扣统计。
- 每步 parent-relative improvement 仅保留为 step 审计字段；纯生成失败批按既有生成开销合同不进 bandit。

## Campaign identity 语义

`stall_cooldown_batches / stall_restart_period / elite_pool_size / elite_pool_epsilon / elite_pool_share / bandit_novelty_weight / bandit_admission_weight` 与行为轴（axes）全部参与 campaign_id 哈希：改任一参数即开新 campaign，不能静默续跑旧 state。`SEARCH_KERNEL` 相应新增 `stall_response / elite_retention / frontier_descriptor / bandit_reward / budget_bandit=active_batch_decision_observations` 声明。

## 三轮机制触发统计（QD-v4, gpt-5.6-sol, 诊断口径）

| 轮 | seed | batch 决策 | cooldown 批 | restart(seed/uniform) | pool 抽取 | pooled 步 | 行为 cell | final 归一化分 |
|---|---|---|---|---|---|---|---|---|
| r1 | 0 | 39 | 15 | 4/3 | 7 | 25 | 11 | 0.2287 |
| r2 | 1 | 35 | 21 | 3/3 | 7 | 21 | 7 | 0.1870 |
| r3 | 2 | 41 | 27 | 4/4 | 2 | 18 | 5 | 0.2273 |

new_best 溯源（机制因果证据）:

- r1 step 83（0.0321，破 0.0409 平台）出自 **uniform_cell restart** 批（cooldown 中）；step 87（0.0152）parent 来自 **pool 抽取**；step 100 收官 0.00125。
- r2 step 20/21 的 new_best parent 均来自 **pool 抽取**；此后 79 步未能再破平台（6 次 restart、7 次 pool 抽取落空）——逃逸是概率性的。
- r3 step 44（0.0309，破平台）发生在 **cooldown 强制 mutate** 批。

三轮聚合（`three_rounds_qd_v4.json`，审计 per-round `audit_errors=0`）:
normalized_score **0.2143 ± 0.0237**（min 0.1870 / max 0.2287）；abs_aod 0.0255 ± 0.0237；accuracy 0.6360 ± 0.0064。
聚合 `complete=false` 的全部原因是协议身份（模型 gpt-5.6-sol 非官方 gpt-5.4、reconstructed checkout）——诊断口径的正确纪律行为，非数据缺陷。

## 审计修复（c5e2b303c）

`reporting.py` 的逐步审计此前**无条件**要求 `metrics/filtered_results` 携带主指标（abs_aod_mean/shd_mean），而真实失败步（evaluator 崩溃、约束违反）诚实记录为 `success=false` + 空 metrics——首次含真实失败步的三轮聚合因此误报 `complete=false`。修复后该存在性要求仅作用于 `success is True` 的步，与文件内其他所有逐步检查的既有门一致；失败步若携带指标，数值一致性检查仍然执行。新增两条回归测试（诚实失败步通过审计；成功步缺指标仍拒绝）。

## 界限声明

三轮全部为诊断运行：provider `OpenAI` 模型 `gpt-5.6-sol`（官方为 `gpt-5.4`）、AIF360 checkout 为 reconstructed revision（`d2115a1d`，任务 pin `cf4ed193` 不可复现）。`comparable=false`、`leaderboard_eligible=false`；数值仅用于同条件代际诊断对比，不构成 leaderboard 声明，也不能与论文报告的 OpenEvolve/AIDE 数字作正式比较。
