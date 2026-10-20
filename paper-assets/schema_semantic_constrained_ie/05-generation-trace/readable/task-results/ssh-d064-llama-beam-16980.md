# ssh d064 llama beam 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_llama_beam_16980_20260519T142541_result.json`
- **Structured JSON:** [`fc4a0fec640aef0f3c11.json`](../../sessions/fc/fc4a0fec640aef0f3c11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 beam search 都在正常产出。

## 报告

### 启动状态：成功

| Job | GPU | Mode | PID (bash/python) | 输出已产出 |
|-----|-----|------|-------------------|-----------|
| beam-4 unconstrained | cuda:0 | unconstrained | 647117 / 647122 | 4/998 docs |
| beam-4 constrained | cuda:1 | full_s1 | 647329 / 647334 | 2/998 docs |

### Checkpoint 来源
使用 **westd-16980 上已有的** Llama LoRA DocRED merged checkpoint（May 16，w5 训练版本，分片格式 4×safetensors）。westd-21461 上有 d064 新训练的版本（May 19，单文件格式），但 AutoDL 实例间无法直连 scp。两者架构相同（Llama 3.1 8B），权重来自不同训练 run。

### 预估完成时间
当前速度约 ~22s/doc（unconstrained），998 docs 预估 **~6h**，约 5/20 凌晨 4:30 完成。Constrained 因额外约束计算会稍慢。

### 日志路径
- `/root/autodl-tmp/schema_outputs/d064_beam4_unc_16980.log`
- `/root/autodl-tmp/schema_outputs/d064_beam4_con_16980.log`

### 输出路径
- `/root/autodl-tmp/schema_outputs/d064_llama_docred_beam4_unconstrained_16980.jsonl`
- `/root/autodl-tmp/schema_outputs/d064_llama_docred_beam4_constrained_16980.jsonl`

### 注意
- westd-21461 无任何进程被干扰
- 若需严格一致性（用 d064 新 checkpoint），后续可在 westd-21461 beam search 完成后对比结果，或找中间存储做模型中转

---
