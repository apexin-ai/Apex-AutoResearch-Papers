# infra westd25068 model downloads

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd25068-model-downloads_20260518T170104_result.json`
- **Structured JSON:** [`81698fdfe8cd35ba00b5.json`](../../sessions/81/81698fdfe8cd35ba00b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。汇总关键发现：

**下载状态**:
- 4 个模型通过 hf-mirror.com 下载中（DeepSeek-R1-0528-Qwen3-8B, DeepSeek-R1-Distill-Llama-8B, Phi-4-reasoning, gemma-3-27b-it）
- Llama-4-Scout **失败**：gated model 需要 Meta 授权
- **磁盘空间严重不足**：仅剩 47G，4 个模型合计约 114GB。预计只有两个 8B 模型（共 ~32G）能完成下载，Phi-4 和 gemma-3 会因磁盘满失败

**实验状态**:
- exp-007（72B AWQ）和 exp-004-rerun（7B）**均已失败**（网络/下载问题），GPU 0 和 3 空闲
- exp-027 和 exp-028（Qwen3-14B thinking/non-thinking）在 GPU 1/2 上正常运行

**需要决策**:
1. 磁盘空间不足，是否清理部分旧模型（如 Mistral-7B、Llama-3.1-8B）腾出空间？
2. 是否重跑 exp-007 和 exp-004-rerun（GPU 0/3 空闲）？
3. Llama-4-Scout 需要到 HF 页面申请 Meta 授权

---
