# diagnose failed batch 20250516

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_failed_batch_20250516_20260516T124653_result.json`
- **Structured JSON:** [`3ae675733f9dfef27980.json`](../../sessions/3a/3ae675733f9dfef27980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### exp_002_signals_15B_s123_batch (cuda:0) — 实际已完成
- **所有 36 个信号文件 + 12 个 merged 文件已生成**，4 dosages × 3 benchmarks × 3 signals 全部存在
- 文件大小正常（mmlu merged 2.5MB, gsm8k merged 242KB）
- exit code=2 是因为任务框架的 wrapper 与脚本版本不匹配导致的 bash 语法错误，发生在所有计算**完成之后**
- **无需重提交**

### exp_002_signals_15B_d100_s123_cuda2 (cuda:2) — 实际已完成
- Log 明确显示 `===BATCH_COMPLETE_15B_d100_s123_cuda2=== Total:9 Completed:9 Skipped:0 Failed:0`
- **无需重提交**

### exp_006_mmlu_domain_gamma_n24_v2 (CPU/Stan) — 部分完成，已重提交
- 8 个 MMLU domains 中 4 个已完成：STEM_Math, STEM_Science, STEM_CS_Eng, Medical
- 4 个缺失：Humanities, Social_Sciences, Business_Law, Other
- 进程在 Medical 完成后死亡（原因不明，可能 OOM 或被外部 kill）
- **已重提交**，仅跑缺失的 4 个 domains：
  - 命令：`python run_mmlu_domain_gamma_n24.py --domains Humanities Social_Sciences Business_Law Other`
  - PID: **781756**
  - Log: `/root/autodl-tmp/exp006/mmlu_domain_gamma_n24_v2.log`
  - 当前状态：Stan 4 chains warmup 中，预计每 domain ~15-20 分钟

### faiss 问题
Log 中未出现 faiss 错误。两个 signals 实验实际都成功完成。报告中的 `ModuleNotFoundError("No module named 'faiss.swigfaiss_avx512_spr'")` 可能来自更早的失败尝试，当前版本已不存在此问题。

---

**总结**：只有 exp_006 需要补跑，已提交。exp_002 的两个实验虽然被标记为 failed，但数据实际完整，可以直接用于下游。

---
