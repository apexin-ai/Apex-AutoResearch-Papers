# infra download qwen3 instruct

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_qwen3_instruct_20260513T232446_result.json`
- **Structured JSON:** [`3dfa7f96cb4b56864a71.json`](../../sessions/3d/3dfa7f96cb4b56864a71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- `Qwen/Qwen3-1.7B-Instruct` 在 HuggingFace 上不存在。Qwen3 系列不区分 base/instruct — `Qwen3-1.7B` 本身就是带对话能力的模型（标签含 "conversational"）
- 已有的 `Qwen3-1.7B` 模型完整可用（3.8GB，2 个 safetensors 分片）
- 创建了软链接 `/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct` → 同一模型
- exp004 配置 `model_path` 已指向该路径，无需修改
- 模型加载验证通过：`qwen3, vocab=151936, hidden=2048`

---
