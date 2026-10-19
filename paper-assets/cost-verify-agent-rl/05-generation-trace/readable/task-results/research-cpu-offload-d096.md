# research cpu offload d096

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cpu-offload-d096_20260519T143608_result.json`
- **Structured JSON:** [`248343b83e2e9ed5c7b3.json`](../../sessions/24/248343b83e2e9ed5c7b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。总结：

**核心发现：**
1. v7 的 `optimizer_offload: True` **完全无效** — RAGEN 重写了 `update_actor` 但没包含 offload 逻辑，且 init 时 optimizer.state 为空导致首次 offload 也跳过
2. FSDP1 下 actor 的 CPUOffload **被硬编码关闭**（verl line 492），无法通过 config 开启
3. FSDP2 + `offload_policy: True` 是正确方案 — verl 原生支持，PyTorch 2.10 已就绪

**v9 config 已创建：**`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_cell_c_v9.yaml`

关键变更：
- `strategy: fsdp2` + `offload_policy: True` — FSDP2 原生 CPU offload，任何时刻 GPU 上只有 1-2 个 layer
- `enable_activation_offload: true` — 互补措施
- `gpu_memory_utilization: 0.20`（从 0.22 降低）— 为 weight sync 留空间
- 移除无效的 `optimizer_offload: True`

**主要风险：** FSDP2 在 RAGEN 上可能未充分测试，需通过 val_before_train 验证数值正确性。训练速度预计下降 2-3x。

报告位于 `artifacts/d096_cpu_offload_research.md`。

---
