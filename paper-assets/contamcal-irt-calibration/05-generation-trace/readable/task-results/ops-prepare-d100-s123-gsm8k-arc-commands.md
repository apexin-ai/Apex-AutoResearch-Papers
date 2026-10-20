# ops prepare d100 s123 gsm8k arc commands

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-d100-s123-gsm8k-arc-commands_20260516T040531_result.json`
- **Structured JSON:** [`df89e7af62ad72be18ce.json`](../../sessions/df/df89e7af62ad72be18ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入并通过语法检查。

**文件**: `/root/contamcal-irt-calibration/exp002/run_3B_d100_s123_gsm8k_arc_signals.sh`

**内容**: 计算 gsm8k + arc_challenge 各 s1/s2/s4（共 6 个信号），skip-if-done 逻辑，alpha=32 前置校验，ref 用 d000_s123。

**运行方式**（mmlu s4 完成后在 cuda:4 上执行）:
```bash
CUDA_VISIBLE_DEVICES=4 nohup bash /root/contamcal-irt-calibration/exp002/run_3B_d100_s123_gsm8k_arc_signals.sh > /tmp/3B_d100_s123_gsm8k_arc.log 2>&1 &
```

**注意**: gsm8k/arc 的 eval_results 文件不存在（aligned/para_aligned 都没有），但 s1/s2/s4 不需要 eval_results（只有被 D098 排除的 s3 才需要），所以不影响运行。

---
