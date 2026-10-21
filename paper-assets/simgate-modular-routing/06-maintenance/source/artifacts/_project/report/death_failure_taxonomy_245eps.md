# Death Failure Taxonomy — 245 Episodes (Corrected)

数据源: baseline_245eps, 245 episodes, 11 tasks, seed=42

## 死亡统计
| 策略 | 死亡数 | 总数 | 死亡率 |
|---|---|---|---|
| Internal (LLM) | **105** | 245 | **42.9%** |
| Deterministic | 40 | 245 | 16.3% |

## Fatal Action 分类
**100% (105/105) 的致命动作都是 `focus on [X]`**

## Focus-on 目标分布
- workshop: 20.0%
- inventory: 17.1%
- kitchen: 10.5%
- 其他分散

## Per-task 死亡率
- 0% death: find-non-living-thing
- 最高: lifespan-longest-lived (56.0% internal vs 16.0% det)
- 10/11 tasks: 45-56% internal death rate

## 替换说明
替换 art_20260518_4fbf4e (prescreening 73 deaths) 和 art_20260518_367035 (prescreening 图表)
