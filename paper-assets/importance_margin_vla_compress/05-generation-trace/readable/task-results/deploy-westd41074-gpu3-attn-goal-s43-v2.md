# deploy westd41074 gpu3 attn goal s43 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu3_attn_goal_s43_v2_20260525T233818_result.json`
- **Structured JSON:** [`606901aa3893358be6e6.json`](../../sessions/60/606901aa3893358be6e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**部署失败 — Goal 模型权重不完整。**

westd-41074 上的情况：
- `/root/autodl-tmp/openvla-libero-goal/` 存在，但只有 config/tokenizer 等小文件（3 GB）
- 实际 safetensors 权重文件全部是 `.incomplete` 状态（下载中断）
- HF cache (`/root/autodl-tmp/.hf_cache/hub/models--openvla--openvla-7b-finetuned-libero-goal/`) 也只有 `refs`，无完整 snapshot

**结论**：Goal 模型在 westd-41074 上从未成功下载完成，无法启动 eval。按指示不尝试下载（AutoDL 下载 7B 模型太慢）。

**建议**：
1. 从 westd-27271（seed42 成功运行过，模型完整）用 `scp` 传输权重到 westd-41074
2. 或在 westd-41074 上用 ModelScope + network_turbo 恢复下载（约 14 GB，预计 30-60 min）
3. 或改为在 westd-27271 上跑 seed43（如果有空闲 GPU）

---
