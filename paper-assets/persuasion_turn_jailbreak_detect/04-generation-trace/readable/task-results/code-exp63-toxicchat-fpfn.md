# code exp63 toxicchat fpfn

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp63_toxicchat_fpfn_20260522T181539_result.json`
- **Structured JSON:** [`a1146fc6df769aec880d.json`](../../sessions/a1/a1146fc6df769aec880d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp63 完成，已注册。结论：**negative**。

**核心数据：**
- 9-class (MV): F1=0.652, FPR=0.510, P=0.589, R=0.730
- MLM (MV): F1=0.853, FPR=0.167, P=0.839, R=0.868
- MLM 正确 ∩ 9-class 错误：144 样本，其中 FP 占 64.6%（93/144），FN 占 35.4%（51/144）
- 9-class 正确 ∩ MLM 错误：46 样本，FP/FN 各占 50%

9-class 的 FPR 极高（0.510），FP 确实是更大的错误来源（64.6%），但未达到 >70% 的假设阈值——FN（35.4%）也是显著的错误贡献者，说明 9-class DAPT 的性能退化是 FP 和 FN 的混合问题，而非单一 FP 主导。

---
