# 7B Main Experiment Per-Task Death Rate

## 数据源
- **文件**: `/root/autodl-tmp/simgate-modular-routing/data/scienceworld-counterfactual/episodes.jsonl` (server: westb-14838)
- **模型**: Qwen2.5-7B-Instruct (field: `internal`)
- **Death 判定**: `internal.final_score == -100.0` (与 `internal.death == True` 完全一致，105/105 match)
- **总量**: 245 episodes across 11 tasks

## Per-Task Death Rates

| Task | 7B Deaths | 7B Total | 7B DR | 72B DR (provided) | Delta (7B−72B) |
|------|-----------|----------|-------|--------------------|----------------|
| chemistry-mix | 9 | 20 | 45.0% | 50% | −5.0pp |
| find-animal | 10 | 20 | 50.0% | 40% | +10.0pp |
| find-non-living-thing | 0 | 40 | 0.0% | 0% | 0.0pp |
| freeze | 11 | 20 | 55.0% | 45% | +10.0pp |
| grow-fruit | 9 | 20 | 45.0% | 40% | +5.0pp |
| identify-life-stages-1 | 11 | 20 | 55.0% | 45% | +10.0pp |
| identify-life-stages-2 | 10 | 20 | 50.0% | 30% | +20.0pp |
| inclined-plane-determine-angle | 11 | 20 | 55.0% | 45% | +10.0pp |
| lifespan-longest-lived | 14 | 25 | 56.0% | 25% | +31.0pp |
| lifespan-longest-lived-then-shortest-lived | 9 | 20 | 45.0% | 20% | +25.0pp |
| measure-melting-point-unknown-substance | 11 | 20 | 55.0% | 25% | +30.0pp |

## Aggregates

- **Overall**: 105/245 = 42.9%
- **Death-prone (excl. find-non-living-thing)**: 105/205 = **51.2%**
- **7B DR range (death-prone tasks)**: 45.0%–56.0%

## 同文件中的 72B (deterministic) 实际数据

注意：同一 counterfactual 文件中 `deterministic.final_score == -100` 的 72B death rate 与任务描述中提供的"72B DR"不一致（后者可能来自 `results/backbone_72b/` 独立实验）：

| Task | 72B DR (paired, this file) | 72B DR (provided) |
|------|----------------------------|-------------------|
| chemistry-mix | 25.0% (5/20) | 50% |
| find-animal | 25.0% (5/20) | 40% |
| find-non-living-thing | 0.0% (0/40) | 0% |
| freeze | 25.0% (5/20) | 45% |
| grow-fruit | 20.0% (4/20) | 40% |
| identify-life-stages-1 | 10.0% (2/20) | 45% |
| identify-life-stages-2 | 20.0% (4/20) | 30% |
| inclined-plane-determine-angle | 20.0% (4/20) | 45% |
| lifespan-longest-lived | 16.0% (4/25) | 25% |
| lifespan-longest-lived-then-shortest-lived | 10.0% (2/20) | 20% |
| measure-melting-point-unknown-substance | 25.0% (5/20) | 25% |
| **TOTAL** | **16.3% (40/245)** | — |

建议确认论文中使用哪组 72B 数据。如果使用 paired counterfactual 数据，Delta 会更大。

## N 不等于 22 的 tasks
- **find-non-living-thing**: N=40（比其他 task 多一倍）
- **lifespan-longest-lived**: N=25
- 其余 9 个 task: N=20（非 22）
