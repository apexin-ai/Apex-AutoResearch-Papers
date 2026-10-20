# ops gpu diagnostic both servers

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_diagnostic_both_servers_20260516T053336_result.json`
- **Structured JSON:** [`02d3c7ca2ec2bcfd1453.json`](../../sessions/02/02d3c7ca2ec2bcfd1453.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### westd-16980 (2× RTX PRO 6000 Blackwell, 98GB each)

| GPU | 显存使用 | GPU利用率 | 进程PID | 进程命令 |
|-----|---------|----------|---------|---------|
| GPU 0 | 14701 / 97887 MiB (15%) | 86% | **334612** | `w6_mistral_scierc_constrained` — Mistral-7B SciERC constrained eval |
| GPU 1 | 17427 / 97887 MiB (18%) | 84% | **321568** | `w5_qwen_docred_lora_constrained_eval` — Qwen LoRA DocRED constrained eval |

**关键进程：**
- PID 321568 (`w5_qwen_docred_lora_constrained_eval`) — **存活**，CUDA_VISIBLE_DEVICES=1，运行 219 分钟，CPU 100%
- PID 334612 (`w6_mistral_scierc_constrained`) — **存活**，CUDA_VISIBLE_DEVICES=0，运行 4 分钟，CPU 102%

---

### westd-21461 (2× RTX PRO 6000 Blackwell, 98GB each)

| GPU | 显存使用 | GPU利用率 | 进程PID | 进程命令 |
|-----|---------|----------|---------|---------|
| GPU 0 | 15291 / 97887 MiB (16%) | 90% | **7740** | `w6_mistral_docred_unconstrained` — Mistral-7B DocRED unconstrained eval |
| GPU 1 | 15361 / 97887 MiB (16%) | 87% | **7813** | `w6_mistral_scierc_constrained` — Mistral-7B SciERC constrained eval |

**关键进程：**
- PID 6789 (`w6_mistral_docred_constrained`) — **已死亡**，不存在
- PID 5571 (`w6_mistral_docred_unconstrained`) — **已死亡**，不存在
- 但有**新进程**替代：PID 7740 (unconstrained, GPU 0) 和 PID 7813 (constrained SciERC, GPU 1)，均运行约 3.5 分钟
- `/tmp/w6_mistral_docred_constrained.log` 内容显示只有 pad_token_id 警告，说明旧进程已结束（或被重启）

---

### 总结

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| westd-16980 | **忙** — w6_mistral_scierc_constrained (PID 334612) | **忙** — w5_qwen_docred_lora_constrained_eval (PID 321568) |
| westd-21461 | **忙** — w6_mistral_docred_unconstrained (PID 7740) | **忙** — w6_mistral_scierc_constrained (PID 7813) |

**4 块 GPU 全部在用，无空闲 GPU。** 原 PID 6789 和 5571 已不存在，westd-21461 上当前跑的是新启动的进程。

---
