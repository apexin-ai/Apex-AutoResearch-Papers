# code exp 006 v2 code mod

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_v2_code_mod_20260514T180337_result.json`
- **Structured JSON:** [`834c1ac878968ff9c0e8.json`](../../sessions/83/834c1ac878968ff9c0e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

NUTS warmup 正在运行，4 条 chains 都已产出 warmup samples，速度约 5-10 it/s。按 2000 iterations/chain 计算：

- chain 4 最快: 300/2000 @ 10 it/s → ~3 min remaining
- chain 3 最慢: 200/2000 @ 6 it/s → ~5 min remaining

**估算总时间: warmup + sampling ~10-15 分钟完成。** 与 MMLU 的 6 小时零采样形成鲜明对比——GSM8K (1319 items, ~5300 params) 对 NUTS 完全可行。

总结已完成的工作：

**代码修改（5 项全部完成）：**
1. `--max-items`: 截断 → 随机抽样 (seed=42)
2. `--aligned-only`: 已存在，无需改
3. `--signals-dir`: 已存在，本次运行使用 exp-002 signals
4. `--benchmark`: 新增单 benchmark 便捷参数
5. `--method nuts/advi`: 新增 ADVI 支持（`fit_stan_model_advi` + `run_benchmark_fit` 双分支）

**实验已启动：**
- `exp_006_irt_05B_gsm8k` RUNNING on cqa1-21977
- 4 models x 1319 items, NUTS 4 chains x 1000 samples
- Warmup 进展良好，预计 10-15 分钟完成全部 pipeline

---
