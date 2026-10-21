# gpu d066 docred beam sweep v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_d066_docred_beam_sweep_v2_20260520T025208_result.json`
- **Structured JSON:** [`401ecf1f5b51998dc63b.json`](../../sessions/40/401ecf1f5b51998dc63b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d066 Qwen DocRED beam sweep 方案已部署：

**当前状态**
- d065 LLaMA unc 在 GPU0 跑 345/998 docs（~2.5h 后完成）
- Wrapper 脚本（PID 712981）在等 GPU0 释放，之后顺序跑 k=2 unc → k=2 S1 → k=8 unc → k=8 S1
- Cascade 已杀，不会抢 GPU0
- 200-doc subset 和 greedy baseline eval 已准备好

**已收集的 baseline 数据（200-doc subset, 公平对比）**

| Config | ET% | RV% | DR% | CF% | E-F1 | R-F1 |
|--------|-----|-----|-----|-----|------|------|
| k=1 greedy unc | 0 | 0.24 | 0.20 | 0.03 | 81.34 | 44.56 |
| k=1 greedy S1 | 0 | 0 | 0 | 0.12 | 80.54 | 43.64 |

30 分钟后回来检查进度。

---
