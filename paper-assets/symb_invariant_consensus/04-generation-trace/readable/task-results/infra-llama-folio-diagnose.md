# infra llama folio diagnose

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama-folio-diagnose_20260522T110253_result.json`
- **Structured JSON:** [`81882b6200ca1740c28c.json`](../../sessions/81/81882b6200ca1740c28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因确认**：vLLM 启动参数与代码请求冲突。

从 `ps aux` 可见 LLaMA vLLM 进程的启动命令：
```
python3 -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --port 8002 --enforce-eager --max-model-len 4096 --gpu-memory-utilization 0.9
```

而 `run_full_mvp.py` 默认 `--max-tokens 4096`（第212行）。

**冲突**：`max_model_len=4096` 是 input+output 总上限，代码请求 `max_tokens=4096` 给 output，留给 input 的配额为 0。prompt 有 ~766 字符，必然超出，所以 204 个 FOLIO 问题全部返回 400 错误。

对比：Mistral 和 Qwen2.5 的 vLLM 都用了 `--max-model-len 8192`，所以没出问题。

## 修复建议

**方案 A（推荐）**：重启 LLaMA vLLM，`--max-model-len 8192` 与其他模型一致，然后重跑 multi-seed。

**方案 B**：不改 vLLM，在脚本中加 `--max-tokens 2048`。FOLIO 是逻辑推理题，输出远不需要 4096 tokens，2048 绰绰有余。

**方案 C**：A+B 都做——vLLM 改 8192，max_tokens 降到 2048，留足余量。

需要我执行修复吗？

---
