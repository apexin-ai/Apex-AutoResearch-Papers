# analysis data consolidation precheck

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data_consolidation_precheck_20260528T054526_result.json`
- **Structured JSON:** [`6c865efe0ec1000d644d.json`](../../sessions/6c/6c865efe0ec1000d644d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

整合完成。核心结果：

**覆盖率**: 10/18 格子 4-seed 完整，8/18 格子 3-seed，共 9 个缺失数据点（均为 s45 或 s44）。

**Outlier 检测**: 无。最大偏差 L2norm k=0.75 s43=73.2%（+3.2pp from mean），在 5pp 阈值内。

**ROADMAP 检查清单**: 6 项全部通过（1 项 N/A，1 项有 per-task 注意事项）。

**数据完整性**: 18 组 s42+s43 均值与 ROADMAP 2-seed 表交叉验证，全部匹配。

**需关注**:
- Random k=0.9 s42=34.2% 来自 D273 决策记录，registry 无 strict 条目
- Random k=0.85 s43 per-task 数据有 L2norm 混入，整体 SR=47.2% 不受影响
- 9 个缺失 seed 中，s44 实验部分仍在 running（ROADMAP 标注 ⏳）

产出已注册: `art_20260528_e8226b`

---
