# infra westd16639 recovery downloads

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd16639-recovery-downloads_20260518T170047_result.json`
- **Structured JSON:** [`f2d56ebe6c3b77181117.json`](../../sessions/f2/f2d56ebe6c3b77181117.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。总结：

**GPU**: 4 张 Blackwell 全部正常，CUDA 计算和 transformers 推理通过。vLLM 0.21.0 的 CUDA graph 在 Blackwell 上有 bug，需 `--enforce-eager` 绕过。

**磁盘**: autodl-tmp 285GB 可用，充足。

**模型下载**:
- DeepSeek-R1-0528-Qwen3-8B、Phi-4-reasoning → 正在下载 ✅
- gemma-3-27b-it、Llama-4-Scout → 需要 HF Token ❌（gated model）

**实验 intermediates**: exp032 有 509 个，qwen3_nonthinking 有 518 个，arc60 仅 18 个，strategyqa200 仅 3 个，folio 155 个。路径在 `/root/autodl-tmp/sica_project/` 下。

**待用户操作**: 接受 gemma-3 和 Llama-4 的 HF license，然后在服务器上 `hf auth login`。

---
