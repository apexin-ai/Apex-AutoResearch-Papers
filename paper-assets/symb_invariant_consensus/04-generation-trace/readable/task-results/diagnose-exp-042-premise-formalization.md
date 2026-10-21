# diagnose exp 042 premise formalization

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-042-premise-formalization_20260518T190415_result.json`
- **Structured JSON:** [`061c77169ee0d05304aa.json`](../../sessions/06/061c77169ee0d05304aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"root_cause":"vLLM server on port 8002 (GPU 2) was not started for exp-042. The previous vLLM (exp-028, Qwen3-14B) gracefully shut down at 02:11:18 ('INFO: Shutting down' in /tmp/vllm_exp028.log). exp-042 launched ~33min later at ~02:44 with no vLLM on port 8002. Script never produced Python output — spent 533s in the wrapper (likely health-check retries or sleep waiting for vLLM) before being SIGTERM'd by watchdog.","error_type":"infrastructure","fix_steps":["Start vLLM on GPU 2 port 8002 with Qwen2.5-14B-Instruct: CUDA_VISIBLE_DEVICES=2 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8002 --dtype auto --trust-remote-code --enforce-eager","Wait for health check: curl http://localhost:8002/v1/models returns 200","mkdir -p results/exp042_premise_formalization && re-run: python -u premise_formalization.py --api-base http://localhost:8002/v1 --model auto --k 12 --data data/folio_full.json --output results/exp042_premise_formalization/results.json --seed 42"],"can_auto_fix":true,"partial_results":"无，0/204题已完成（输出目录不存在）"}
```

**关键证据链**:
- `/tmp/vllm_exp028.log` 尾部: `INFO: Shutting down` → `Shutdown complete` @ 02:11:18
- exp-042 log 只有 3 行（conda warning + Terminated + EXIT_CODE=143），无 Python 输出
- `nvidia-smi`: GPU 2 = 0 MiB，无 vLLM 进程
- 无 `/tmp/vllm_exp042*.log` — 没有为 exp-042 启动过 vLLM
- 注意：exp-028 用的是 **Qwen3-14B**（thinking mode），而 exp-042 需要 **Qwen2.5-14B-Instruct**，模型不同

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "vLLM server on port 8002 (GPU 2) was not started for exp-042. The previous vLLM (exp-028, Qwen3-14B) gracefully shut down at 02:11:18 ('INFO: Shutting down' in /tmp/vllm_exp028.log). exp-042 launched ~33min later at ~02:44 with no vLLM on port 8002. Script never produced Python output — spent 533s in the wrapper (likely health-check retries or sleep waiting for vLLM) before being SIGTERM'd by watchdog.",
    "error_type": "infrastructure",
    "fix_steps": [
      "Start vLLM on GPU 2 port 8002 with Qwen2.5-14B-Instruct: CUDA_VISIBLE_DEVICES=2 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8002 --dtype auto --trust-remote-code --enforce-eager",
      "Wait for health check: curl http://localhost:8002/v1/models returns 200",
      "mkdir -p results/exp042_premise_formalization && re-run: python -u premise_formalization.py --api-base http://localhost:8002/v1 --model auto --k 12 --data data/folio_full.json --output results/exp042_premise_formalization/results.json --seed 42"
    ],
    "can_auto_fix": true,
    "partial_results": "无，0/204题已完成（输出目录不存在）"
  }
}
```

</details>

---
