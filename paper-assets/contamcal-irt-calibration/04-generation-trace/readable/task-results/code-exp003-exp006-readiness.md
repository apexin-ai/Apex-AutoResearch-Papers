# code exp003 exp006 readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003_exp006_readiness_20260514T131708_result.json`
- **Structured JSON:** [`e3a15a2701f6d7648872.json`](../../sessions/e3/e3a15a2701f6d7648872.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 memory.md。汇总：

## exp-003 RRF — 95% ready, 0h 补全
- 3 个脚本完整：RRF 融合 + 5 种消融 + evaluation (AUC/AP/precision@k)
- 输入格式与 exp-002 实际输出完全对齐（`signals_merged_{bench}.json`）
- ConStat 缺失自动降级为 3-signal RRF（`detect_available_signals`）

## exp-006 IRT Calibration — 95% ready, 0h 补全
- 7/7 baselines 全部实现（B0-B6），含 DCR fuzzy inference
- 8 个 metrics（超出要求的 5 个），含 LaTeX table 输出
- 4 个 Stan models 已编译 at `/root/contamcal-irt-calibration/stan_models/`（注意：不在 `artifacts/mvp_simulation/` 下，但代码路径正确）
- 已有 dry-run 验证结果，D018 排除逻辑已集成
- joint_fit ablation 也已实现

## exp-008 Signal Survival — 95% ready, 0h 补全
- 4 文件 1547 LOC，v3 含 N-regime + RRF composite + cliff detection + AUC heatmap

## 瓶颈
**exp-002 信号输出**：仅 d000 完整（3 signals × 3 benchmarks），d005 部分完成（2 signals × mmlu only），d025/d050/d100 未开始。ConStat 信号完全缺失（需 paraphrase eval）。所有下游实验都在等这个。

---
