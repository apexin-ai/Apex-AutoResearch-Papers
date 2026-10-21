# 7B Baseline Per-Task Death Rate

Model: Qwen2.5-7B-Instruct (always-internal mode)
Data source: westb-13313 `/results/prescreening/` (5 episodes per task)

## Per-Task Death Rate (prescreening, N=5 each)

| Task | Total | Deaths | Rate |
|------|-------|--------|------|
| chemistry-mix | 5 | 3 | 60.0% |
| chemistry-mix-paint-tertiary-color | 5 | 2 | 40.0% |
| find-animal | 5 | 3 | 60.0% |
| find-living-thing | 5 | 3 | 60.0% |
| **find-non-living-thing** | **5** | **0** | **0.0%** |
| find-plant | 5 | 3 | 60.0% |
| freeze | 5 | 3 | 60.0% |
| grow-fruit | 5 | 3 | 60.0% |
| identify-life-stages-1 | 5 | 3 | 60.0% |
| identify-life-stages-2 | 5 | 2 | 40.0% |
| inclined-plane-determine-angle | 5 | 3 | 60.0% |
| inclined-plane-friction-named-surfaces | 5 | 3 | 60.0% |
| inclined-plane-friction-unnamed-surfaces | 5 | 3 | 60.0% |
| lifespan-longest-lived | 5 | 3 | 60.0% |
| lifespan-longest-lived-then-shortest-lived | 5 | 3 | 60.0% |
| lifespan-shortest-lived | 5 | 3 | 60.0% |
| measure-melting-point-known-substance | 5 | 3 | 60.0% |
| measure-melting-point-unknown-substance | 9 | 5 | 55.6% |
| mendelian-genetics-known-plant | 7 | 4 | 57.1% |
| mendelian-genetics-unknown-plant | 7 | 4 | 57.1% |
| power-component | 5 | 3 | 60.0% |
| power-component-renewable-vs-nonrenewable-energy | 5 | 3 | 60.0% |
| test-conductivity | 5 | 3 | 60.0% |
| test-conductivity-of-unknown-substances | 5 | 3 | 60.0% |
| use-thermometer | 5 | 3 | 60.0% |
| **TOTAL** | **133** | **74** | **55.6%** |

## find-non-living-thing 跨实验验证

| Experiment | Episodes | Deaths | Rate |
|------------|----------|--------|------|
| prescreening | 5 | 0 | 0.0% |
| plan_c | 40 | 0 | 0.0% |
| plan-006-deep-internal | 20 | 0 | 0.0% |
| **Total** | **65** | **0** | **0.0%** |

## 结论

- find-non-living-thing 是唯一一个 7B death rate = 0% 的 task
- 72B 在该 task 上 death rate 也是 0%
- **这是一个天然 "non-death-prone" task**，不适合用于评估 death avoidance 能力
- 其他 24 个 task 的 7B death rate 在 40%-60% 之间（均值 ~58%）
