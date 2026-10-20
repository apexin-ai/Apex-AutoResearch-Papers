# ops status check westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd21461_20260516T111002_result.json`
- **Structured JSON:** [`3b3ba416cdf507423c58.json`](../../sessions/3b/3b3ba416cdf507423c58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在跑，汇总如下：

## 状态汇总

### GPU
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 18.9/97.9 GB | 85% |
| 1 | RTX PRO 6000 Blackwell | 18.9/97.9 GB | 84% |

### w8_qwen_docred_ft_grammar_only (PID 18555, cuda:0)
- **状态**: RUNNING
- **运行时间**: 1h42m43s
- **日志进度**: [166/998] — **16.6%**
- **输出文件**: 299 行（可能包含之前的数据或多行输出）
- **最新样本**: New Haven Harbor, 37.1s
- **预计剩余**: ~8-9h（按 ~1.6 samples/min）

### w8_qwen_docred_ft_semantic_only (PID 20035, cuda:1)
- **状态**: RUNNING
- **运行时间**: 1h01m02s
- **日志进度**: [166/998] — **16.6%**
- **输出文件**: 172 行
- **最新样本**: New Haven Harbor, 38.4s
- **预计剩余**: ~5-6h（按 ~2.7 samples/min）

两个实验进度相同（都在第166个样本），但 grammar_only 启动早 ~40min。实验未完成，无法运行 violation checker 和更新 registry。

---
