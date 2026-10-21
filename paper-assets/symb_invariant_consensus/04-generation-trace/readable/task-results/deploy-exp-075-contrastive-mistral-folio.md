# deploy exp 075 contrastive mistral folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-075-contrastive-mistral-folio_20260519T172758_result.json`
- **Structured JSON:** [`2551f35231f3ef2aa43d.json`](../../sessions/25/2551f35231f3ef2aa43d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

- **vLLM**: Mistral-7B-Instruct-v0.3 在 cuda:2 (port 8002) 启动成功。遇到 FlashInfer 不兼容 Blackwell GPU 的问题，通过设置 `VLLM_ATTENTION_BACKEND=FLASH_ATTN` + `VLLM_USE_FLASHINFER_SAMPLER=0` 解决。KV cache 592K tokens，bf16。
- **实验**: tmux session `exp075_run` 已启动，正在处理（1/204 已开始）
- **Registry**: `exp-075-contrastive-mistral-folio` 状态已更新为 RUNNING，spec 已写入

---
