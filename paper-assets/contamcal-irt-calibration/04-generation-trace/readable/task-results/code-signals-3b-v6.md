# code signals 3B v6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_signals_3B_v6_20260515T201034_result.json`
- **Structured JSON:** [`cbede22b1037452269af.json`](../../sessions/cb/cbede22b1037452269af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

signals_3B_v6 已启动并注册。

**总结：**
- Orphan PID 617201/617202 已不存在（无需 kill）
- GPU 3 上有一个 1.5B evaluate 进程（PID 627614，6.4GB），与 signals 3B 共存无问题
- 直接用 compute_signals.py（run_batch.py 不支持 `_v2` 命名），9 个任务顺序执行：3 benchmarks (mmlu/gsm8k/arc_challenge) × 3 signals (s1/s2/s4)
- 跳过 s3_constat（d000_v2 无 eval_results）
- checkpoint: `Qwen2.5-3B_d000_v2_s42/lora_adapter`，ref_model 为自身
- tmux session: `signals_3B_v6`，log: `/root/autodl-tmp/exp002/signals/signals_3B_v6.log`
- GPU 3 显存 12.7GB/24GB，正常运行中

---
