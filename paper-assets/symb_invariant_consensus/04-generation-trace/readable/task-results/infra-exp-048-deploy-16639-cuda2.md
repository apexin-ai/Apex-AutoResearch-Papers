# infra exp 048 deploy 16639 cuda2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp-048-deploy-16639-cuda2_20260518T203225_result.json`
- **Structured JSON:** [`b3347d3d47a14cc589b5.json`](../../sessions/b3/b3347d3d47a14cc589b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**LLaMA-3.1-8B-Instruct 不在 westd-16639 上，无法部署 exp-048。**

GPU 状态：cuda:2 空闲（RTX PRO 6000 Black, 98GB, 0% 占用）。

**可用模型列表：**
| 模型 | 目录名 |
|---|---|
| Mistral-7B-Instruct-v0.3 | `Mistral-7B-Instruct-v0.3` |
| Qwen2.5-14B-Instruct | `Qwen2.5-14B-Instruct` |
| Qwen3-14B | `Qwen3-14B` |
| DeepSeek-R1-0528-Qwen3-8B | `deepseek-r1-0528-qwen3-8b` |
| Gemma-3-27B-IT | `gemma-3-27b-it` |
| LLaMA-4-Scout | `llama-4-scout` |
| Phi-4-Reasoning | `phi-4-reasoning` |

**PW-600 数据也不存在。** 现有 ProofWriter 数据：
- `proofwriter_d012.json`
- `proofwriter_full.json`
- `proofwriter-OWA-D5-validation.jsonl`

**建议替代实验：** 用 Qwen2.5-14B-Instruct + 现有 ProofWriter 数据（如 `proofwriter_full.json`），或其他可用模型组合。需要你决定下一步。

---
