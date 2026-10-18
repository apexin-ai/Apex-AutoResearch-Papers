# fix cqa1 redeploy attn k095 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_redeploy_attn_k095_goal_20260527T053432_result.json`
- **Structured JSON:** [`b6074a28ed959344f777.json`](../../sessions/b6/b6074a28ed959344f777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并运行。

**汇总：**
- GPU1 上 π0.5 Goal baseline strict (PID 972711/972716) 已 kill
- OpenVLA Attn k=0.95 Goal v2 (PID 11249) 已在 GPU1 上运行，正在执行 Task 1/10，模型已加载（15.1 GB），attention pruning 256→243 tokens
- Registry 已更新：v1 标记为 killed，v2 已创建并关联 parent
- cqa1 四卡状态：GPU0 OV Random k=0.95 Goal / GPU1 OV Attn k=0.95 Goal v2 / GPU2 π0.5 Attn k=0.95 Long / GPU3 OV Attn k=0.5 Goal

---
