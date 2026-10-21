# code exp 008 signal survival

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-signal-survival_20260514T124254_result.json`
- **Structured JSON:** [`88c833a3c2a9167dab44.json`](../../sessions/88/88c833a3c2a9167dab44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结：**

`/root/contamcal-irt-calibration/exp008/signal_survival.py` 已创建并通过 dry-run 验证。相比原有 v2 代码新增：

1. **RRF 聚合分数**作为第 5 个 signal（`rrf_score`），自动从 `rrf_{benchmark}.json` 或 `exposure_rrf_{benchmark}.json` 加载
2. **Per-benchmark 分解**：每个 benchmark 独立输出 `survival_report.json`
3. **Cliff detection**：`cliff_ratio = max_single_step_drop / total_drop`，≥0.7 判为 cliff-like。Mock 数据中 Min-K++/ConStat/Self-Critique/RRF 均在 `sft_contam → rl_aligned` 检出 cliff，Embedding 为 stable
4. **Cross-benchmark 聚合**：mean/std AUC per signal × regime

原有文件（`signal_survival_analysis.py`, `run_signal_survival.py`, `plot_survival.py`, `run_exp008.sh`）保持不动，可继续使用。

**阻塞项**：等 exp-002 signal outputs 产出后即可用真实数据运行。

---
