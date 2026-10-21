# code eval 3B d005 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_3B_d005_s123_20260515T151021_result.json`
- **Structured JSON:** [`06d83b40d27c506d4f40.json`](../../sessions/06/06d83b40d27c506d4f40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法提交，cuda:2 上已有同类 eval 进程在运行。**

PID 580698 的命令：
```
python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned \
  --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned
```

这就是 `exp_001_eval_3B_d005_s123` 要做的事——相同 adapter、相同 benchmarks、相同 output-dir 后缀。看起来这个 eval **已经在跑了**。

根据约束 C001（目标 GPU 上有同类进程则不提交），我不提交。

建议：确认这个进程是否就是之前提交的同一实验。如果是，只需将 registry 状态更新为 RUNNING 并关联即可。需要我查一下 registry 当前状态吗？

---
