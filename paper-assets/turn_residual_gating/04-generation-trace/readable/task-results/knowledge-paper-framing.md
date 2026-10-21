# knowledge paper framing

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper_framing_20260518T171218_result.json`
- **Structured JSON:** [`9f0dd114b6d70bd73012.json`](../../sessions/9f/9f0dd114b6d70bd73012.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`paper_framing.md` 已保存。包含全部 8 个要求的章节:

- **Title**: 推荐 T1 "ThreadGate: Recovering Goal Attention in Multi-Turn Dialogue via Learnable Residual Gating"
- **Story Arc**: 从 GAR 衰减悖论 (attention 关闭但 residual stream 保留 goal info) 切入, 引出 ThreadGate 作为首个架构级干预
- **Core Claims**: 6 条, 每条标注支撑实验和状态 (已验证/suggestive/待验证), C4 的 L4/L5 对齐措辞已校准为 suggestive
- **Key Selling Points**: 5 个, 重点突出首个干预方案、per-layer 自适应解决跨架构变异、Dongre residual probe 独立支撑
- **Reviewer Concerns**: 7 条, 含 R6 (为何不直接修 attention) 和 R7 (稀释 vs 结构性衰减) 两条额外预判
- **Dongre 关系**: 明确诊断 vs 方案互补定位
- **GAR 策略**: 训练用 ours, 主表用 Dongre, 附录用 ours
- **MVP Pass**: 原样搬入, 含 partial pass 处置逻辑

---
