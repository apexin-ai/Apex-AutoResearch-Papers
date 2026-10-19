# knowledge paper framing draft

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper-framing-draft_20260517T155310_result.json`
- **Structured JSON:** [`af57543b22030c27d672.json`](../../sessions/af/af57543b22030c27d672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`paper_framing.md` 已写入。核心结构：

- **Core Insight**: joint training 梯度污染 → decoupled training 是必须的 architectural constraint
- **8 条 Claims**: 4 条 VERIFIED (梯度污染/scorer-only 失败/connector+scorer 成功/log-barrier loss), 4 条 PENDING (性能保持/效率/鲁棒性/connector-only ablation)
- **Story Arc**: uniform processing 问题 → 朴素 IB 方案的系统性失败 → decoupled training 洞察 → 方法 → 验证
- **7 个 Reviewer Concerns** 含应对策略（单 backbone、无真机、vs BC-IB/LightVLA 等）
- **11 项 Ablation** 标注完成状态
- **写作时间线** 对齐 5/26 abstract、5/29 paper deadline

---
