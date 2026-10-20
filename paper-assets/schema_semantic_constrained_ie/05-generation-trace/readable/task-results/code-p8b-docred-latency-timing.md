# code p8b docred latency timing

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p8b_docred_latency_timing_20260518T151351_result.json`
- **Structured JSON:** [`945f90d0644f124f12ff.json`](../../sessions/94/945f90d0644f124f12ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并配置监控：

- **实验**: `p8b_docred_latency`，westd-21461 cuda:0
- **GPU**: NVIDIA RTX PRO 6000 Black（与 P8 SciERC 同型号）
- **流程**: unconstrained → full_s1 constrained → analyze_latency.py（串行）
- **数据**: DocRED dev 前 200 docs
- **tmux session**: `p8b_docred_latency`
- **监控**: 每 12 分钟自动检查进度，完成后自动汇报结果

模型已加载到 cuda:0（16GB VRAM），unconstrained 阶段正在运行。DocRED 文档较长，预计 1-3 小时完成全部流程。

---
