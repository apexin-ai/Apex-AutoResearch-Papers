# verify pid807025 llama eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pid807025_llama_eval_20260516T154022_result.json`
- **Structured JSON:** [`84293141e7f746fc21b1.json`](../../sessions/84/84293141e7f746fc21b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：PID 807025 确认是 Llama d000 eval，正常运行中。**

- 命令：`python evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmarks gsm8k arc_challenge humaneval --mc-format aligned --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/ --batch-size 4`
- 进度：`mmlu_results.json` 已产出（说明 MMLU 已完成，当前正在跑 gsm8k/arc_challenge/humaneval 中的某个）
- 进程活跃，主要使用 nvidia5（对应 CUDA_VISIBLE_DEVICES 映射后的某块卡）
- 无需重启，让它跑完即可

---
