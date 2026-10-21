# plan 7b 14b experiment plan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_plan_7b-14b-experiment-plan_20260518T061929_result.json`
- **Structured JSON:** [`50cdd8391fce480c643b.json`](../../sessions/50/50cdd8391fce480c643b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验计划已保存至 `artifacts/_project/report/experiment_plan_7b14b.md` (art_20260518_dfae9b)。

核心数字:

- **24 SFT runs**: 3 模型 × 4 dosages × 2 seeds
- **440-504 GPU-hours 总计** (SFT 184-248h + Eval 64h + Signals 192h)
- **Wall time**: 乐观 5 天, 保守 6-7 天 (4 GPU pipeline 并行)
- **成本**: ~2,500-3,000 CNY (4× A100 80GB)
- **全部单卡可跑**: 7B ~32GB, 14B ~55GB, 8B ~34GB

排布策略: 7B+8B 先跑 (Day 1-3), 完成的 checkpoint 立即进 eval/signal pipeline, 14B 最后 (Day 3-6)。三级降级方案 (Plan B: 16 runs / Plan C: 8 runs) 应对 deadline 风险。

---
