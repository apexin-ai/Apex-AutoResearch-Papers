# ops check running experiments 20260516

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_experiments_20260516_20260516T105323_result.json`
- **Structured JSON:** [`a7ceaefb27d9174554e7.json`](../../sessions/a7/a7ceaefb27d9174554e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

---

## 实验状态报告

### westd-16980 (2× RTX PRO 6000 Black, 98GB)

| GPU | PID | 实验 | 进度 | 状态 |
|-----|-----|------|------|------|
| 0 | 351214 | `benchmark_latency_docred.py` | 未知 | ⚠️ **不在预期列表中** |
| 1 | 345222 | **w8_llama_docred_ft_grammar_only** | 643/998 (64.4%) | ✅ 正常运行 |

- w8_llama 日志: `/tmp/w8_llama_docred_ft_grammar_only.log`
- 输出文件最后修改: 18:54:57 CST (刚刚)，持续写入中

**空闲 GPU: 无** (GPU 0 被 benchmark 脚本占用)

---

### westd-21461 (2× RTX PRO 6000 Black, 98GB)

| GPU | PID | 实验 | 进度 | 状态 |
|-----|-----|------|------|------|
| 0 | 18555 | **w8_qwen_docred_ft_grammar_only** | 254/998 (25.5%) | ✅ 正常运行 |
| 1 | 20040 | **w8_qwen_docred_ft_semantic_only** | 128/998 (12.8%) | ✅ 正常运行 |

- grammar_only 日志: `/root/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log` — 显示 [166/998]
- semantic_only 日志: `/root/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log` — 模型已加载完毕，开始推理
- 两个输出文件均在最近30s内被修改，持续写入

**空闲 GPU: 无**

---

### 已完成的 w7 实验 (westd-16980)

- w7_qwen_scierc_ft_semantic_only: ✅ 551/551 完成
- w7_llama_scierc_ft_grammar_only: ✅ 551/551 完成
- w7_llama_scierc_ft_semantic_only: ✅ 551/551 完成

---

### 汇总与建议

**3个 RUNNING 实验全部确认在跑，进程正常，GPU 利用率 83-89%。** Cron 监控显示 0 可能是注册/检测逻辑问题，不是实验本身的问题。

**需要操作：**
1. 3个 w8 实验需重新注册 cron 监控（进程实际在跑但 cron 检测不到）
2. westd-16980 GPU 0 上的 `benchmark_latency_docred.py` (PID 351214) 不在 registry 中——确认是否是你手动启动的，是否还需要

**空闲 GPU: 0** — 两台服务器4块GPU全部占满。

---
