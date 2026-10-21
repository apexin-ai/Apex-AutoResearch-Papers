# deploy exp 074c icg seed123 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-074c-icg-seed123-25068_20260519T200415_result.json`
- **Structured JSON:** [`a5bc8516a74b8d94d9ac.json`](../../sessions/a5/a5bc8516a74b8d94d9ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**总结：**
- 杀掉 cuda:1 上已完成的 exp-073b Qwen vLLM（port 8001）
- 在 cuda:1 启动 Mistral-7B-Instruct-v0.3 vLLM（port 8001，tmux: `exp074c_vllm`）
- Dry-run 通过（204 items, 所有依赖 OK）
- 实验已启动（tmux: `exp074c_run`），正在处理中（1/204 开始）
- Registry: `exp-074c-icg-mistral-folio-seed123` → RUNNING，parent: exp-074
- 监控 cron 每 8 分钟检查一次进度

---
