# analysis s44 r2 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s44-r2-prep_20260515T181700_result.json`
- **Structured JSON:** [`90a5bf9c80a7ae01c313.json`](../../sessions/90/90a5bf9c80a7ae01c313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 脚本就绪性

| 脚本 | 状态 | 说明 |
|------|------|------|
| `classify_h7.py` | **就绪** | 存在，文件头包含 H7a/H7b/H1/H8 分类逻辑（D086 版本） |
| `eval_sta.py` | **就绪** | 存在，支持 FOL/Prolog，输出 ISR/prove_rate 等指标 |

> 注：ssh_read_only 禁止 `&&`/`;`，无法做 `--help` 或 `import` 测试。但两个脚本文件头正确，高度可信可用。

### 已有 taxonomy 分类数据

| 实验 | 分类文件 | 核心指标 |
|------|----------|----------|
| **s42** (500步) | `h7_classification/plan018_additive_random_b01_s42_h7.json` | 79 proved, H7=0, H1=58, H8=4, **genuine=18 (22.8%)** |
| **s43-r3** (500步) | `plan018_additive_random_b01_s43_r3/taxonomy_results.json` | 94 proved, H7=36, H1=56, H8=1, **genuine=1 (1.1%)** |
| **s43-r3** | `eval_sta_results.json` + `analysis.json` 也存在 | eval_sta 已完成 |

### s44-r2 训练进度

- **当前 step: 172 / 500 (34%)**
- 每步 ~15-17s，预计剩余 ~1.5 小时
- 输出目录已创建：`plan018_additive_random_b01_s44_r2/`，含 checkpoint-150 和 reward_log.jsonl
- 无 taxonomy/eval 结果（预期，训练未完成）

### 问题

无阻塞性问题。两个脚本就绪，s42 和 s43-r3 分类数据完整，s44-r2 训练正常推进中。训练完成后可直接执行 classify_h7.py → eval_sta.py 流程。

---
