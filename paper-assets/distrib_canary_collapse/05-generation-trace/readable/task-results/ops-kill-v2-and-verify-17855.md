# ops kill v2 and verify 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-v2-and-verify-17855_20260522T023028_result.json`
- **Structured JSON:** [`51e416bb6051946beedb.json`](../../sessions/51/51e416bb6051946beedb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 进程正常运行中（已运行 1h32m）。汇总：

---

## 执行结果

### 1. v2 进程 kill 确认
| PID | 实验 | 状态 |
|-----|------|------|
| 552609 | t25_a060_s42_fp32 (v2, 无 --start_gen) | **已 kill** |
| 552687 | t25_a050_s42_fp32 (v2, 无 --start_gen) | **已 kill** |

残留：无 v2 tmux session 对应这两个实验。`phase_diagram_t20_a060_s43_fp32_v2` 是另一个实验 (t20, seed43)，不在冲突范围内，未动。

### 2. GPU 显存
6 块 GPU 均 ~14.5G/97G — 符合预期（v2 释放后只剩 v3 + 其他实验）。

### 3. Gen 目录完整性

**两个实验结构一致：**
| Gen | 来源 | 文件/大小 | 状态 |
|-----|------|-----------|------|
| 0-13 | v2 写入 | 2-3 files, 6.6-7.0M | 完整，metrics.json 一致 |
| 14-15 | v3 写入 | 4 items, 1.6G (含 checkpoint/) | 完整，checkpoint 含 model.safetensors 1.5G |
| 16 | v3 创建中 | 空目录 | v3 正在处理 |
| 17-25 | — | MISSING | 尚未到达 |

### 4. all_metrics.json
两个实验均**不存在** all_metrics.json — 应为实验结束时生成，当前不影响。

### 5. 数据完整性判定

**可继续等 v3 完成，无需重跑。** 理由：
- metrics.json 在 v2→v3 边界处（gen_12→13→14→15）数值连续无跳变，perplexity 单调递增符合预期
- v3 的 gen_14-15 含完整 checkpoint（model.safetensors 1.5G + config + tokenizer），v2 的 gen_0-13 不含 checkpoint（只有 metrics + synthetic_data），两者模式清晰区分
- v3 进程已运行 1h32m，当前在 gen_16，正常推进

---
