# check gpu experiments status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-experiments-status_20260522T144440_result.json`
- **Structured JSON:** [`c19d7c63c917b4dc57dc.json`](../../sessions/c1/c19d7c63c917b4dc57dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| 实验 | 服务器 | PID | GPU | 显存 | 进度 | 状态 |
|------|--------|-----|-----|------|------|------|
| **eval_70b_lora_scierc_beam4_s1** | westd-16980 | 957041 | cuda:0 | 40064 MiB | 7/551 | 运行中，刚开始推理 |
| **tcr_beam4_qwen_scierc** | westd-16980 | 956461 | cuda:0 | 18910 MiB | 84/551 | 运行中，模型已加载 |
| **eval_70b_zs_scierc_grammar_only** | westd-21461 | 59802 | cuda:0 | 39256 MiB | 21/551 | 运行中 |

**GPU 冲突问题：无冲突。** westd-16980 GPU0 总 97887 MiB，两个进程共用 ~59000 MiB（70B AWQ-INT4 ~40GB + 8B LoRA ~19GB），未 OOM，GPU 利用率 96%。

**Cron 监控已注册：** 3 个实验各 8 分钟轮询一次（session-only，7 天自动过期）。

---
