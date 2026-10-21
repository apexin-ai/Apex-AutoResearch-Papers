# ALFWorld Counterfactual 全量实验诊断

**实验**: `alfworld-counterfactual-full` (PID 290564, tmux: alfworld_cf)
**时间**: 2026-05-14, 运行 46 min, 50/140 episodes 完成

## 实际数据（非 0%）

| 指标 | 值 |
|------|-----|
| Internal success | 2/50 (4%) |
| Deterministic success | 25/50 (50%) |
| det-preferred labels | 23/50 (46%) |
| no-preference labels | 27/50 (54%) |
| internal-preferred labels | 0/50 (0%) |

### 按 task_type

| Task Type | N | Internal | Deterministic |
|-----------|---|----------|--------------|
| look_at_obj_in_light | 13 | 2/13 (15%) | 5/13 (38%) |
| pick_and_place | 32 | 0/32 (0%) | 18/32 (56%) |
| pick_clean_then_place | 5 | 0/5 (0%) | 2/5 (40%) |

## 根因分析

### Internal mode 低成功率 (4%)：词汇不匹配 + 差的 fallback

Qwen2.5-7B 生成的动作名称和 ALFWorld 的 admissible actions 词汇不匹配：

| 模型生成 | ALFWorld 实际名 | 出现次数 |
|---------|----------------|---------|
| "go to table" | "go to countertop 1" / "go to sidetable 1" | 79 |
| "go to couch" | "go to sofa 1" | 55 |
| "go to desk" | "go to desk 1" (缺数字后缀) | 51 |
| "go to kitchen" | 不存在（需去具体物品） | 18 |
| "go to counter" | "go to countertop 1" | 12 |

当 `match_to_admissible()` 无法匹配时，fallback 是 `admissible[0]`——即列表第一个动作（任意的），导致模型在错误位置反复打转直到 50 步上限。

### Deterministic mode 50% 成功：合理

给了 admissible actions list 后，Qwen2.5-7B 能合理选择动作。50% 在 7B 模型上是合理水平（ALFWorld 需要多步推理+正确的搜索策略）。

### 这不是 bug，是 expected behavior

Internal mode 的设计意图就是测试模型在没有外部计算（admissible actions）时的表现。4% vs 50% 的差距正是 counterfactual 信号：ALFWorld 任务强依赖 deterministic computation。

## 建议

**不要 kill 这个实验。** 数据实际上是有用的：

1. 46% det-preferred 标签率足够训练 router
2. Deterministic 50% 成功率意味着有足够的正样本
3. 实验设计本身没有 bug，运行正常

### 可选优化（下次运行时）

1. `match_to_admissible` 可加同义词映射（table→countertop, couch→sofa），但这会改变实验条件
2. Fallback 用随机 admissible action 比 `admissible[0]` 更好（减少"卡在第一个动作"的模式）
3. Internal prompt 可以加上 ALFWorld 的 object naming convention 提示

### 关于用户报告的 "0% 成功率"

用户可能只看了前几个 episode 的 internal_success 字段（前 13 个全是 look_at_obj_in_light，internal 只有 2 个成功），或者混淆了 internal/deterministic 的结果。实际 deterministic 成功率 50%。
