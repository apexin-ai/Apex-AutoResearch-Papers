# analysis paper data audit pre lockdown

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_data_audit_pre_lockdown_20260526T043156_result.json`
- **Structured JSON:** [`63525fd344c81e28cc0d.json`](../../sessions/63/63525fd344c81e28cc0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结论：

**所有 8 个 Claims (C1-C8) 均有充分实验支撑，无阻塞缺口。**

关键发现：
- **C1-C3, C7**: Strong 级别证据，多 seed、多环境
- **C4-C5**: Moderate，定位为 supporting claims，可接受
- **C6**: 6 seeds，2/6 CIVO 崩溃 + 1/6 non-CIVO 失败，partially falsified 本身即为发现
- **C8**: 7+ 方法、3 层级、3 环境，Intervention Hierarchy 是系统性贡献

两个 RUNNING 实验：
- **exp_097** (C2 Cheetah s3): 当前 onset rate 2/3，完成后变 2/4 或 3/4。不影响 necessity 结论 (Fisher p<0.001)
- **exp_100** (C3 Walker s1): C3 已有 6 seeds (4 Walker + 2 Cheetah) 全 success。添加 NVE trajectory 但不阻塞

产出已注册: `art_20260526_c46dc7`

---
