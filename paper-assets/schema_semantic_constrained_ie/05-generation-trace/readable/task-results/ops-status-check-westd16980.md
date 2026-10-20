# ops status check westd16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd16980_20260516T104956_result.json`
- **Structured JSON:** [`e1a5775d844d42ae6533.json`](../../sessions/e1/e1a5775d844d42ae6533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. w8_llama_docred_ft_grammar_only (cuda:1) — **RUNNING**

| 指标 | 值 |
|------|-----|
| 进度 | 625/998 samples (**62.6%**) |
| PID | 345222 (CPU time: 159min) |
| tmux | `w8_llama_docred_grammar` |
| GPU 1 | 16,921 / 97,887 MiB, 89% util |

日志路径: `/tmp/w8_llama_docred_ft_grammar_only.log`（`~/runs/` 下的路径不存在）

---

### 2. DocRED latency benchmark (cuda:0) — **RUNNING**

| 阶段 | 状态 | mean | median | std |
|------|------|------|--------|-----|
| unconstrained | DONE | 21.023s | 15.588s | 17.729s |
| grammar_only | DONE | 21.366s | 15.793s | 17.990s |
| semantic_only | IN PROGRESS | — | — | — |

PID 351214 (CPU time: 73min), 结果文件尚未写入。

---

### 3. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|----------|--------|
| 0 | RTX PRO 6000 Blackwell | 17,343 / 97,887 MiB | 85% |
| 1 | RTX PRO 6000 Blackwell | 16,921 / 97,887 MiB | 89% |

---

两个实验都在正常运行，无需干预。grammar_only 按当前速率预估还需约 1-1.5 小时完成剩余 373 samples；latency benchmark 还有 semantic_only 剩余 samples + 可能的后续模式要跑。

---
