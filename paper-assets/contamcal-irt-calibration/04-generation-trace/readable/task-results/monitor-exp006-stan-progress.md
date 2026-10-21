# monitor exp006 stan progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp006_stan_progress_20260514T144601_result.json`
- **Structured JSON:** [`f4b1c509bb0f8b3fe039.json`](../../sessions/f4/f4b1c509bb0f8b3fe039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp-003 RRF 产出
**不存在。** exp003 目录只有源代码（`rrf_aggregation.py`, `ablations.py`, `evaluate_rrf.py`），没有 output 目录，没有 `exposure_scores.json` 或 `exposure_aggregated.json`。全项目 `find` 也没有 `exposure*` 文件。

但这可能不是问题——`run_exp006.py` 直接从 exp002 信号加载并内部调用 `load_exposure_scores()`，不需要 exp003 预先生成独立文件。

### exp-006 Stan NUTS — 正在运行

**4 chains 全部存活，CPU 占用 99.9%：**

| Chain | PID | 启动时间 | 已运行 |
|-------|-----|---------|--------|
| 1 | 386298 | 22:19 | ~28 min |
| 2 | 386299 | 22:19 | ~28 min |
| 3 | 386300 | 22:19 | ~28 min |
| 4 | 386301 | 22:19 | ~28 min |

**配置：** `num_warmup=1000, num_samples=1000, max_depth=12, delta=0.95`
**当前 benchmark：** MMLU（9 models × 14042 items）
**参数规模：** ~56K（theta×9 + a/b/c/d×14042 + gamma×9 + tau×9）+ 126K log_lik 输出

**进度：** 所有 4 条 chain 的 CSV 文件仅有 48 行（全是 header），尚未写出任何 sampling 数据行 → **仍在 warmup 阶段**。

### 时间估计

初始速度 ~2 it/s（log 显示），但 NUTS 在 warmup 后期 tree depth 增大后会显著变慢。56K 参数 + max_depth=12 的 NUTS，28 分钟还在 warmup 中是正常的。保守估计：

- MMLU warmup: 可能需要 1-3 小时
- MMLU sampling: 类似时间
- 还有 gsm8k, arc_challenge, humaneval 三个 benchmark 要跑
- **总计预估：8-24 小时**

### 其他活跃进程
- `exp_001_eval_05B_raw`（GPU 1，已暂停 T 状态）
- `Qwen2.5-0.5B_d100_s42_aligned` eval（两个实例在 GPU 0/2 上运行）

**结论：** Stan NUTS 正在正常运行，不需要重启。建议数小时后再检查。

---
