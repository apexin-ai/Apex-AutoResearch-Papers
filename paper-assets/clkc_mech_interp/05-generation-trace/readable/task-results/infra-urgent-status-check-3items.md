# infra urgent status check 3items

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-status-check-3items_20260522T150851_result.json`
- **Structured JSON:** [`f2475e56754ef7a107d2.json`](../../sessions/f2/f2475e56754ef7a107d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Gemma L17 Steering (PID 493756, cuda:2) — 🔄 运行中

- 进程存活，已运行 30min
- 日志仅 9 行（模型加载完毕），之后无输出 — **确认是 stdout 缓冲问题**
- GPU 2: 18.6GB 显存占用，21% 利用率 — 在做推理
- 结果文件尚未生成
- **无需干预**，正在正常运行，只是没有 flush stdout

### 2. Gemma Probe Training (PID 476334) — 🔄 运行中 (~50%)

- 进程存活，已运行 4h25m
- 进度：
  - ✅ zh_en: 2000/2000 done (178.4min)
  - ✅ zh_zh: 2000/2000 done (82.9min)
  - 🔄 en_zh: 98/2000 (~5%，刚开始)
  - ⏳ en_en: 尚未开始
- **预计还需 ~2-3 小时完成全部 4 个方向**

### 3. Llama Bootstrap n=2000 (PID 465851) — ✅ 完成

文件 `probe_results_bootstrap_n2000.json` (20KB, 22:39 生成)

关键结果：
| 指标 | 值 |
|------|-----|
| **asymmetry_peak mean_diff** | **0.0727** |
| **p_value (two-sided)** | **0.038** (显著) |
| CI | [0.0037, 0.1397] |
| n_seeds | 2000 |

en_en 方向 peak 在 layer 18-19 (acc ~0.75)，zh_zh 方向 peak 较低。**不对称性统计显著 (p=0.038)**。

### 4. Llama L13-all Steering (PID 494291, cuda:3) — 🔄 运行中

- 进程存活，已运行 29min
- 日志显示正在生成文本（pad_token_id 设置消息）
- GPU 3: 16.1GB 显存占用，25% 利用率
- 结果文件尚未生成
- **正常运行中**

---

**总结**: 1 项完成（Llama bootstrap，p=0.038 显著），3 项正常运行中，无需干预。Gemma steering 的无日志问题是缓冲导致，GPU 利用率证实在工作。

---
