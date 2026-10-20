# analysis run pooled 4bench irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_run-pooled-4bench-irt_20260515T130031_result.json`
- **Structured JSON:** [`dd5e3f636914544fb1d8.json`](../../sessions/dd/dd5e3f636914544fb1d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正在运行但进度很慢。关键发现：

- **当前状态**: PID 561357，已运行 25 分钟，MMLU chain 1 仍在 warmup/sampling 中
- **问题**: Stan 数据使用了全部 14042 MMLU items（未子采样），但先前运行使用了 2000 items 子采样（`subsampled: true`）
- **时间估计**: 全量 14042 items 下，MMLU 单个 fit 预计 2-3 小时，5 个 fit 总计 6-10 小时

先前（已有的子采样）MMLU 结果已经可用，结果合理：
- **MMLU gamma**: 0.1194 [-0.1731, 0.4104], rhat=1.007, ESS=736, div=0
- N_models=10, items=2000 (subsampled from 14042)

如果不需要全量 items 的 fit，可以 kill 当前进程并使用已有结果。或者修改脚本添加子采样加速。需要你决定下一步：

1. **继续等待** 当前全量运行（6-10 小时）
2. **Kill 并修改** 脚本添加子采样（如 2000 items），预计 30-60 分钟完成
3. **使用已有结果** 如果子采样结果已足够

---
