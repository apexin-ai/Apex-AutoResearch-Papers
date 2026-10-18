# audit westd 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-41074_20260522T015238_result.json`
- **Structured JSON:** [`95b2b0c09e02211629ba.json`](../../sessions/95/95b2b0c09e02211629ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

巡检完成。摘要：

| GPU | 实验 | 状态 | 进度/SR |
|-----|------|------|---------|
| 0 | eval_pi05_l2norm_k085 | **DEAD** — 结果已保存 | SR=98.0% |
| 1 | eval_pi05_l2norm_k095 | **DEAD** — 结果已保存 | SR=98.2% |
| 2 | VTC M96 训练 | **ALIVE** | 81150/100000 (81.2%), ~10.5h 剩余 |
| 3 | VTC M64v6 训练 | **ALIVE** | 33950/100000 (34.0%), ~30.6h 剩余 |

两个 eval 进程完成评测后因 lerobot groot 模块的 dataclass 兼容问题崩溃（`non-default argument 'backbone_cfg' follows default argument`），但结果 JSON 在崩溃前已写入磁盘，数据完整。

**GPU 0 和 GPU 1 空闲，可以接新实验。** Registry 中这两个实验的状态应从 PREPARING 更新为 DONE。

---
