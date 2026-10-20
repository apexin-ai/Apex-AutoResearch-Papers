# diagnose phase diagram failures

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase_diagram_failures_20260521T192522_result.json`
- **Structured JSON:** [`d9e2a690d55839da5a87.json`](../../sessions/d9/d9e2a690d55839da5a87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验同一根因：磁盘满（os error 28）**

westd-17855 的 `/root/autodl-tmp/` 磁盘 350G 已 100% 占满（剩余 1.2M），两个实验均在 `model.save_pretrained()` 写 safetensors checkpoint 时崩溃。

| 实验 | 目标 gen | 已完成 gen | 失败位置 |
|------|---------|-----------|---------|
| t25_a050_s42_fp32 | 25 | 14 (gen_0~13) | gen_14 checkpoint 写入 |
| t20_a060_s43_fp32 | 20 | 3 (gen_0~2) | gen_3 checkpoint 写入 |

两个实验的训练步骤本身都正常完成（5000/5000 steps），仅在写 checkpoint 文件时因磁盘无空间失败。命令参数无问题，不需要修改。

**重试前提**：必须先清理 17855 磁盘，或转移到有空间的服务器。报告已写入 `artifacts/diagnose_phase_diagram_failures.md`。

---
