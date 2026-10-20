# diagnose eval gsm8k sft qwen cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_sft_qwen_cka_only_20_20260520T153814_result.json`
- **Structured JSON:** [`1fd8cce86d7ba7c70fa7.json`](../../sessions/1f/1fd8cce86d7ba7c70fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验实际上**成功完成**了，不是失败。日志最后几行：

```
EXIT_CODE=0
GSM8K Accuracy: 0.5150 ± 0.0353 (103/200)
Results saved to /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_cka_only_20.json
```

200/200 样本全部跑完，耗时 4h00m04s（平均 72s/sample）。慢的原因是 73% 的生成被截断到 max_new_tokens=2048：

- eos_rate: 27%（仅 54/200 自然结束）
- avg_response_length: 1536 tokens
- truncated: 146/200

```json
{"root_cause":"非失败。EXIT_CODE=0，200/200完成。用户报告的EXIT_CODE=143可能是监控脚本误判（实际进程正常退出后tmux/wrapper层面的信号）","error_type":"infrastructure","fix_steps":["无需修复，结果已保存","如需加速未来eval，可降低max_new_tokens或加batch","eos_rate仅27%说明模型倾向生成冗长推理链，可考虑SFT时加入更短的CoT样本"],"can_auto_fix":false,"partial_results":"完整结果已保存: acc=0.5150±0.0353 (103/200), eos_rate=27%, avg_len=1536"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "非失败。EXIT_CODE=0，200/200完成。用户报告的EXIT_CODE=143可能是监控脚本误判（实际进程正常退出后tmux/wrapper层面的信号）",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，结果已保存",
      "如需加速未来eval，可降低max_new_tokens或加batch",
      "eos_rate仅27%说明模型倾向生成冗长推理链，可考虑SFT时加入更短的CoT样本"
    ],
    "can_auto_fix": false,
    "partial_results": "完整结果已保存: acc=0.5150±0.0353 (103/200), eos_rate=27%, avg_len=1536"
  }
}
```

</details>

---
