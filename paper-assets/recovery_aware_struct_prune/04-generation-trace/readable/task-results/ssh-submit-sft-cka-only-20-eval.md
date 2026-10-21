# ssh submit sft cka only 20 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_sft_cka_only_20_eval_20260520T162951_result.json`
- **Structured JSON:** [`31567a5ef7feafffec59.json`](../../sessions/31/31567a5ef7feafffec59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_gsm8k_sft_cka_only_20 提交结果
- 模型路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20`
- PID: 264517（bash）/ 264522（python）
- 验证：进程存活 ✓ | GPU memory — 模型仍在 CPU→GPU 传输中（RSS 14.7GB 且增长中） | 日志输出 ✓（model loaded, non-uniform MLP detected）
- 状态：**RUNNING**

GPU 显存尚未分配是正常的——12GB safetensors 从 CPU 迁移到 GPU 需要 1-2 分钟。日志和 RSS 增长确认进程健康。

---
