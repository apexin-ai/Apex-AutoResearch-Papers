# ops prep 3B d100 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-3B-d100-eval_20260514T115218_result.json`
- **Structured JSON:** [`28275bb0d11a1c61b735.json`](../../sessions/28/28275bb0d11a1c61b735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已就绪。

**状态汇总：**
- **3B d100 SFT**: 3992/4159 steps (96%)，~12 min 剩余，GPU 3
- **Eval 自动接力**: tmux session `eval_3B_d100` 已启动，正在等待 PID 319555 结束
- **流程**: SFT 完成 → 验证 checkpoint → 自动启动 4 benchmark aligned eval (MMLU/GSM8K/ARC/HumanEval) on GPU 3
- **日志**: `/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log`
- **输出**: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/`

---
