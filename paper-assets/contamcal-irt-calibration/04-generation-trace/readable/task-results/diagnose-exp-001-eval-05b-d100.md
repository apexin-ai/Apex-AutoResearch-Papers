# diagnose exp 001 eval 05B d100

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d100_20260514T022332_result.json`
- **Structured JSON:** [`0afada786bbf42e738c5.json`](../../sessions/0a/0afada786bbf42e738c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。综合所有证据：

**时间线**：
- 09:33 启动，模型加载正常（bitsandbytes 警告非致命）
- MMLU 完成（14042 items，~5 min @ 50 it/s）
- ~09:38 开始 GSM8K，遇到大量 HuggingFace 连接超时（但重试后恢复）
- GSM8K 以 ~5.4s/it 稳定推进
- 10:12 UTC（10:12 CST）在 GSM8K 36%（474/1319）处被外部 SIGTERM
- 结果目录为空——evaluate.py 仅在全部完成后写文件，无增量保存

**SIGTERM 来源**：
- 无 OOM（dmesg 空）、无 Python 异常
- tmux session 已不存在，`remain-on-exit off`
- `/tmp/agent-ml-exit/exp_001_eval_05B_d100.exit` 记录了 `143|2026-05-14T02:12:14Z`
- agent-ml pipeline 框架发出的 kill

```json
{"root_cause":"agent-ml pipeline orchestrator killed tmux session (exit 143/SIGTERM at GSM8K 474/1319, 36%). No OOM, no Python error. /tmp/agent-ml-exit/exp_001_eval_05B_d100.exit confirms pipeline-level termination. HF connection timeouts during GSM8K dataset load were transient and recovered.","error_type":"infrastructure","fix_steps":["重新提交 eval job，使用相同参数: python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval","GSM8K 全量 1319 题 @ 5.4s/it 需约 2h，加上 arc_challenge + humaneval 预计总计 2.5-3h，确保 pipeline timeout 设置足够长","可选：给 evaluate.py 加 benchmark 级别的增量保存，避免前序 benchmark 结果因后续中断丢失"],"can_auto_fix":true,"partial_results":"MMLU 已完成评估（14042 items）但结果未落盘（evaluate.py 仅在全部 benchmark 完成后写 eval_results.json）。GSM8K 完成 36%。arc_challenge 和 humaneval 未开始。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "agent-ml pipeline orchestrator killed tmux session (exit 143/SIGTERM at GSM8K 474/1319, 36%). No OOM, no Python error. /tmp/agent-ml-exit/exp_001_eval_05B_d100.exit confirms pipeline-level termination. HF connection timeouts during GSM8K dataset load were transient and recovered.",
    "error_type": "infrastructure",
    "fix_steps": [
      "重新提交 eval job，使用相同参数: python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval",
      "GSM8K 全量 1319 题 @ 5.4s/it 需约 2h，加上 arc_challenge + humaneval 预计总计 2.5-3h，确保 pipeline timeout 设置足够长",
      "可选：给 evaluate.py 加 benchmark 级别的增量保存，避免前序 benchmark 结果因后续中断丢失"
    ],
    "can_auto_fix": true,
    "partial_results": "MMLU 已完成评估（14042 items）但结果未落盘（evaluate.py 仅在全部 benchmark 完成后写 eval_results.json）。GSM8K 完成 36%。arc_challenge 和 humaneval 未开始。"
  }
}
```

</details>

---
