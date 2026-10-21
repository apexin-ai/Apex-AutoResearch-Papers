# ssh d064 investigate failure

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_investigate_failure_20260519T124714_result.json`
- **Structured JSON:** [`e046fde0dd3641643377.json`](../../sessions/e0/e046fde0dd3641643377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

**d064 没有失败，两条流水线正在正常运行。**

### 当前状态

| GPU | 当前任务 | 进度 | 速率 |
|-----|---------|------|------|
| 0 (Llama) | Greedy unconstrained | 554/998 (55%) | ~14s/doc |
| 1 (Qwen) | Beam-4 unconstrained | 620/998 (62%) | ~21.5s/doc |

Llama LoRA 训练已完成（loss=0.057, acc=98.07%），模型已 merge。

### 剩余工作（自动 cascade，无需干预）

- **GPU 0**: greedy unc → greedy con → beam-4 unc → beam-4 con（共 ~19-27h）
- **GPU 1**: beam-4 unc → beam-4 con（共 ~8-10h）
- **瓶颈**: GPU 0，预计 **5/20 晚间**全部完成，距 DDL 5/25 有 4+ 天余量

### 部分评估（进行中数据）

| 配置 | E-F1 | R-F1 | ET% | RV% | DR% | CF% | Parse Fail% |
|------|------|------|-----|-----|-----|-----|-------------|
| Qwen beam-4 unc (620) | 83.28 | 44.78 | 0.00 | 0.14 | 0.70 | 0.04 | 3.7% |
| Llama greedy unc (554) | 83.43 | 44.97 | 0.00 | 0.29 | 0.27 | 0.13 | 4.5% |

违约率极低，F1 健康。报告已注册 (`art_20260519_5ee027`)。

**建议**: 不要碰服务器，让 cascade 跑完。5/20 上午查 Qwen，晚间查 Llama。

---
