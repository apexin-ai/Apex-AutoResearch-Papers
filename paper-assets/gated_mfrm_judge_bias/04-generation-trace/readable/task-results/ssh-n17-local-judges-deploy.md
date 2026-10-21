# ssh n17 local judges deploy

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_local_judges_deploy_20260523T143909_result.json`
- **Structured JSON:** [`cff9a4a4d9f01d83d0dd.json`](../../sessions/cf/cff9a4a4d9f01d83d0dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个评测正在运行：
- LLaMA: 6200→6201（计数增加中），GPU 0 利用率 100%
- Qwen: 9281，GPU 1 利用率 100%
- Mistral: 9021，GPU 2 利用率 100%

## 部署总结

| 组件 | GPU | 端口 | Model Name | 状态 |
|------|-----|------|-----------|------|
| vLLM LLaMA-3.3-70B-AWQ | GPU 0 | 8001 | llama-3.3-70b-instruct | 运行中 |
| vLLM Qwen2.5-72B-AWQ | GPU 1 | 8002 | qwen2.5-72b-instruct | 运行中 |
| vLLM Mistral-Large-2-AWQ | GPU 2 | 8003 | mistral-large-instruct | 运行中 |

**评测进度**（目标 ~18000/judge）：
- judge_llama: 6201/18000 (34%)
- judge_qwen: 9281/18000 (52%)  
- judge_mistral: 9021/18000 (50%)

3 个 GPU 利用率均 100%，GPU 3 空闲。tmux sessions: `vllm_llama`, `vllm_qwen`, `vllm_mistral` (vLLM 服务) + `judge_llama`, `judge_qwen`, `judge_mistral` (评测脚本)。

---
