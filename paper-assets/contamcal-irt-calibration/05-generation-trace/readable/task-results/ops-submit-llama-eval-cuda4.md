# ops submit llama eval cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_eval_cuda4_20260516T131657_result.json`
- **Structured JSON:** [`820c20294df9c0b5fac3.json`](../../sessions/82/820c20294df9c0b5fac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评测正常运行中：

- **PID**: 785949
- **GPU**: cuda:4，占用 13866 MiB
- **进度**: MMLU 评测中，~40 it/s，515/14042（约 5.5 分钟后进入 GSM8K）
- **预计总时长**: MMLU 14042 items + GSM8K + ARC + HumanEval，估计 ~15-20 分钟

脚本路径: `/root/contamcal-irt-calibration/scripts/run_llama3b_d000_eval.sh`
日志: `/tmp/llama3b_d000_eval.log`
输出目录: `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/`

---
