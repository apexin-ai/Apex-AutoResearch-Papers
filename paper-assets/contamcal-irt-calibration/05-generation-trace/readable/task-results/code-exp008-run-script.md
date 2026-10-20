# code exp008 run script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-run-script_20260514T081342_result.json`
- **Structured JSON:** [`413e827c9e08c4a15525.json`](../../sessions/41/413e827c9e08c4a15525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建: `/root/contamcal-irt-calibration/exp008/run_exp008.sh` (111 行)

结构：
- **参数**: `bash run_exp008.sh GPU_IDS` (如 `1,4,5`)
- **Step 0**: 转换 d100 labels 为 `{index: 0/1}` 格式 (run_signal_survival.py 需要)
- **Step 1**: 4 regimes × 3 benchmarks = 12 次 compute_signals，输出到 `signals/{regime}/{bench}/`，跳过已有 merged 文件的组合
- **Step 2**: 3 次 signal_survival 分析 (per benchmark)，输出到 `results/{bench}/`
- 信号: embedding, minkpp, selfcritique (跳过 constat)
- Min-K++ ref model 统一用 base Qwen2.5-0.5B

注意: d100 labels 全为 1 (contaminated_count == total_items)，AUC 分析需要两类样本。如果 signal_survival 报错，需换用 d050 labels。

---
