# writing claim3 scalability section

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_claim3-scalability-section_20260515T140413_result.json`
- **Structured JSON:** [`1343e8be38ace075a1c3.json`](../../sessions/13/1343e8be38ace075a1c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Claim 3 scalability 小节已写入 `experiments_v1.md` (lines 88–107)。

**新增内容结构**:
- **Setup**: 131 repos → 123 成功 clone，按文件数分 4 tier，测量 timeout/处理时间/Z%
- **Completion and runtime**: 0% timeout，mean 8.93s/instance，p95=31.95s，max=633.68s，109.58h 总耗时；解释 2-hop bounded 保证
- **Structural connectivity by tier**: 内联表格，Z% 从 small 28.4% 到 xlarge 81.2% 单调递增，median Z% xlarge=96%
- **Bounded data-flow scalability guarantee**: bounded vs unbounded 对比，zero-timeout 确认可行性，Z% 递增表明 bounded scope 在大 repo 反而捕获更多结构关系
- **脚注**: 标注当前为 M1 pass，M1v2 re-extraction 将更新数据

所有数字标注 `plan_006_scalability` 来源。未引用 error_rate，未使用 "significantly"，未修改 Claim 1/2 部分。

---
