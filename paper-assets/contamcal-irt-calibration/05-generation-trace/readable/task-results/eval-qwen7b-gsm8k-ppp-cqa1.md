# eval qwen7b gsm8k ppp cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen7b-gsm8k-ppp-cqa1_20260521T014502_result.json`
- **Structured JSON:** [`257be53db959c51eb001.json`](../../sessions/25/257be53db959c51eb001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动并正在运行：

- **进程**: cuda:0 占用 14917 MiB，正在评测 d000 GSM8K（8-shot CoT）
- **tmux session**: `eval_gsm8k_7b`
- **日志**: `/root/contamcal-irt-calibration/logs/eval_qwen7b_s0_gsm8k.log`
- **bitsandbytes 警告**: 非致命，不影响 eval（未使用量化）
- **数据集**: 从缓存加载成功（1319 items，~330 batches at bs=4）
- **C009 验证通过**: md5=001a9bc23f808c47d25ef9eaeecb81f1, size=37591
- **C006 验证**: lora_alpha=32 ✓

**预估时间**: 5 个 dosage × ~10-15min/dosage ≈ 50-75 min 完成全部。结果输出到 `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{dose}_s0/gsm8k_results.json`。

---
