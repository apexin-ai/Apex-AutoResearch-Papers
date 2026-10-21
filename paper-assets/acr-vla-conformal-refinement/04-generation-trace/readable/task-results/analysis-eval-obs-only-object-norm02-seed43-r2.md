# analysis eval obs only object norm02 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-obs-only-object-norm02-seed43-r2_20260516T072251_result.json`
- **Structured JSON:** [`08c448599647a30f2161.json`](../../sessions/08/08c448599647a30f2161.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

report.md 是自动生成的，无法手动更新。registry 已更新为 DONE + negative，report 会自动重建。

## 总结

**eval-obs-only-object-norm02-seed43-r2**: **16% (16/100) — NEGATIVE**

- 进程已退出，无错误（EXIT_CODE=0）
- 低于 argmin seed=43 baseline (17%) 1pp → 结论 negative
- 低于同配置 seed=42 (22%) 6pp，seed 间方差大
- Pooled 2-seed: obs_only 0.2 = **19%** vs argmin = **14.5%**，Δ=4.5pp，边际正向但单 seed 不稳定
- 高方差 task: bbq_sauce 和 chocolate_pudding 都是 40%，而 alphabet_soup 和 ketchup 是 0%
- seed=44 实验（eval-obs-only-object-norm02-seed44-r2）正在 bjb1-18228 运行中，将提供第三个数据点

---
