# diagnose phase diagram t25 a060 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase_diagram_t25_a060_s42_fp32_20260521T192819_result.json`
- **Structured JSON:** [`956513f9320ba8857ef7.json`](../../sessions/95/956513f9320ba8857ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**: 磁盘满 (ENOSPC)。`/dev/md0` 350G 数据盘被 3 个并发 T=25 实验耗尽，gen_15 训练跑完 5000 步后 `save_pretrained` 写 safetensors 时失败。三个实验同因倒下。

**进度**: 15/25 代完成，~6.4 GPU 小时。

**无法 Resume**: 诊断期间发现结果目录已被清空（03:32 被重置，只剩 config.json），必须从头重跑。

报告已写入 `artifacts/diag_t25_a060_s42_fp32.md`。

---
