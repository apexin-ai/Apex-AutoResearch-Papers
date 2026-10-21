# diagnose exp 002 signals 3B d100 s123 v9

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_d100_s123_v9_20260516T061513_result.json`
- **Structured JSON:** [`b45429e5253c8aa918f4.json`](../../sessions/b4/b45429e5253c8aa918f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：实验未失败。**

v9 wrapper 脚本按 benchmark 分开启动独立进程：
- `=== d100_a32_s123 mmlu s4 ===` (line 63，仅补算 s4)
- `=== d100_a32_s123 gsm8k all ===` (line 124，PID 712011，正常完成后退出)
- `=== d100_a32_s123 arc_challenge all ===` (line 206，PID 713193，刚刚 14:17 完成)

用户观察到的"进程死亡"实际上是**每个 benchmark 子进程正常退出**，wrapper 随后启动下一个 benchmark 的新进程。

当前 d100_a32_s123 output 状态：

| benchmark | s1_embedding | s2_minkpp | s4_selfcritique | signals_merged |
|-----------|:---:|:---:|:---:|:---:|
| mmlu | ✓ (08:18) | ✓ (08:27) | ✓ (14:03) | **缺失** |
| gsm8k | ✓ (14:05) | ✓ (14:06) | ✓ (14:10) | ✓ (14:10) |
| arc_challenge | ✓ (14:12) | ✓ (14:13) | ✓ (14:17) | ✓ (14:17) |

唯一缺失：`signals_merged_mmlu.json`。原因是 mmlu 用 `--signal s4` 模式运行（仅补算 s4），不会触发 merge 步骤。

```json
{"root_cause":"非故障。Wrapper脚本为每个benchmark启动独立进程，PID 712011完成gsm8k后正常退出(exit 0)，PID 713193接力完成arc_challenge。用户误将进程正常退出判断为死亡。","error_type":"infrastructure","fix_steps":["无需修复进程问题","补跑 signals_merged_mmlu.json: python compute_signals.py --model-path ... --adapter-path .../d100_a32_s123/lora_adapter --benchmark mmlu --signal merge_only --output-dir .../Qwen2.5-3B_d100_a32_s123（或手动合并3个mmlu signal文件）"],"can_auto_fix":true,"partial_outputs":"mmlu(s1+s2+s4), gsm8k(全部+merged), arc_challenge(全部+merged)","missing_outputs":"signals_merged_mmlu.json"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "非故障。Wrapper脚本为每个benchmark启动独立进程，PID 712011完成gsm8k后正常退出(exit 0)，PID 713193接力完成arc_challenge。用户误将进程正常退出判断为死亡。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复进程问题",
      "补跑 signals_merged_mmlu.json: python compute_signals.py --model-path ... --adapter-path .../d100_a32_s123/lora_adapter --benchmark mmlu --signal merge_only --output-dir .../Qwen2.5-3B_d100_a32_s123（或手动合并3个mmlu signal文件）"
    ],
    "can_auto_fix": true,
    "partial_outputs": "mmlu(s1+s2+s4), gsm8k(全部+merged), arc_challenge(全部+merged)",
    "missing_outputs": "signals_merged_mmlu.json"
  }
}
```

</details>

---
