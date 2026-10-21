# paper revision related work

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_revision-related-work_20260527T022539_result.json`
- **Structured JSON:** [`f0214f43f7622807c205.json`](../../sessions/f0/f0214f43f7622807c205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

**§2.1 (5句→4句)**：
- Safety 方法合并为 1 句 bulk citation（移除按 inference/training 分列的两个 `\cite`，合并为一个）
- Spatial-VLA 方法：4 个分类各带独立 citation → 1 句枚举分类 + 单个合并 `\cite{...19 papers...}`，用 em-dash 包裹
- 删除 "At least fifteen such methods" 独立句，将 "yet none evaluates collision avoidance" 嵌入前句

**§2.2 (4句→2句)**：
- 删除 implicit regularization 句（`lippl2024implicit`）
- 删除 gradient starvation 描述（`pezeshki2021gradient`）
- BN sensitivity 从独立句吸收进第一句末尾，用逗号连接
- LoRA gap statement 保持不变（已是 1 句）

所有引用保留（除 `lippl2024implicit` 和 `pezeshki2021gradient` 随删除内容移除），三个覆盖要求（VLA safety 现有工作、auxiliary objectives 影响、本文 gap）均满足。

---
