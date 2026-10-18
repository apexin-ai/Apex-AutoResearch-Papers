# code retnet three arch

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_retnet_three_arch_20260519T065225_result.json`
- **Structured JSON:** [`dfd71bc41484f85f85d9.json`](../../sessions/df/dfd71bc41484f85f85d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

### 三架构 per-example 统计

| Arch | Pure Acc | H3-1 Acc | Helped | Hurt | Net |
|------|----------|----------|--------|------|-----|
| **GDN** | 0.5430 | 0.5133 | 462 | 615 | **-153** |
| **HGRN2** | 0.4842 | 0.5139 | 548 | 395 | **+153** |
| **RetNet** | 0.5166 | 0.5032 | 426 | 495 | **-69** |

RetNet 确认 net negative (-69)，与 GDN (-153) 同方向，但幅度较小。

### Jaccard overlap

所有架构对的 Jaccard 都极低（0.087-0.108），无论 helped 还是 hurt。attention 改变的具体样本几乎不重叠。

### Set intersection breakdown

**Helped** (union=1191): Only GDN 312, Only HGRN2 378, Only RetNet 273, All three 仅 17
**Hurt** (union=1267): Only GDN 448, Only HGRN2 261, Only RetNet 339, All three 仅 19

### 关键结论

- 2/3 linear-dominant 架构 (GDN, RetNet) 加 attention 后 LAMBADA 下降，1/3 gated-recurrence (HGRN2) 上升
- 三架构间 Jaccard ~0.10，attention 的 per-example 影响高度架构特异
- 支持 "attention effect depends on base architecture's recurrence mechanism" 的结论

产出文件：
- `analysis/lambada_three_arch_comparison.py`
- `analysis/lambada_three_arch_comparison.png` / `.pdf`

---
