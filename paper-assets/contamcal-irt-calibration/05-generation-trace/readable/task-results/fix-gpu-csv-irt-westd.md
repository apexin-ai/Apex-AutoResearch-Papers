# fix gpu csv irt westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu-csv-irt-westd_20260519T131102_result.json`
- **Structured JSON:** [`dc495581a1e4691c808f.json`](../../sessions/dc/dc495581a1e4691c808f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 Fix 全部完成。汇报：

---

### Fix 1: GPU 清理 ✓
- PID 176524（evaluate.py for olmo2_d005）已 kill — `.done` 文件已存在，结果完整，属僵尸进程
- PID 173479 已不存在（被 176524 替代）
- GPU 1 的 100% util / 0 MiB 是驱动层报告异常，`/dev/nvidia1` 不存在，无实际进程
- 当前状态：**4 张卡全部空闲，无进程**

### Fix 2: phase2_summary.csv ✓
- 重新生成 **25/25 行全部 OK**（之前 7 MISSING）
- 补全：olmo2 全系列 5 个 + phi4_d100 + qwen14b_d100
- 文件：`/root/autodl-tmp/exp001/eval_results_v2/phase2_summary.csv`

### Fix 3: IRT fitting 重跑 ✓
- **MMLU: 25 respondents × 14042 items** — 确认从 21→25
- **ARC Challenge: 25 respondents × 1172 items** — 确认 25
- 模型：2PL（preliminary, pending 2PL+γ）
- 输出文件：
  - `/root/autodl-tmp/exp001/eval_results_v2/irt_dose_response.csv`（51 行 = header + 25×2 benchmarks）
  - `/root/autodl-tmp/exp001/eval_results_v2/irt_mmlu_dose_response.pdf`
  - `/root/autodl-tmp/exp001/eval_results_v2/irt_arc_challenge_dose_response.pdf`
- 注意：RuntimeWarning `invalid value encountered in scalar divide` 出现在第一次迭代（prev_nll=inf），不影响结果

---
