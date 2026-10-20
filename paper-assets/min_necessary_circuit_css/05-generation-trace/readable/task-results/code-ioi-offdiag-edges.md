# code ioi offdiag edges

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ioi-offdiag-edges_20260513T013335_result.json`
- **Structured JSON:** [`be2296886499b6ad0949.json`](../../sessions/be/be2296886499b6ad0949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**2 条 off-diagonal（method-specific）边：**

| 边 | CSS | 选中方法 | CIRCUS stability |
|---|---|---|---|
| `m0->a11.h10.v` | 1/3 | EAP-IG | 1.0 |
| `m7->a10.h7.v` | 1/3 | EAP-IG | 1.0 |

**位置解读：**

- **`m0->a11.h10.v`** — MLP-0（第 0 层 MLP 输出）→ Attention 11, Head 10 的 value 输入。从最早层的 MLP 跨接到倒数第一层的 attention head，是一条 long-range skip 边。
- **`m7->a10.h7.v`** — MLP-7（中层 MLP）→ Attention 10, Head 7 的 value 输入。mid-to-late 层连接。

两条边均仅被 EAP-IG 选中，ACDC 和 EP 均未选。它们在 CIRCUS stability 上得分 1.0（EAP-IG 内部阈值扫描完全稳定），但跨方法一致性为 1/3——典型的 EAP-IG 方法特异性边，可能反映 EAP-IG 的梯度归因对 MLP→Attention value 路径的高灵敏度，而非真正的电路结构。

---
