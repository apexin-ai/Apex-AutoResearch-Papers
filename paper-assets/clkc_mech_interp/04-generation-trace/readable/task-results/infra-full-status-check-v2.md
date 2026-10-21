# infra full status check v2

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-check-v2_20260522T093735_result.json`
- **Structured JSON:** [`3ff071a9339ddc2f95a9.json`](../../sessions/3f/3ff071a9339ddc2f95a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 总览

| GPU | 利用率 | 显存 | PID | 任务 |
|-----|--------|------|-----|------|
| 0 | 18% | 16.1/97.9 GB | 468898 | Steering v3 Llama |
| 1 | 14% | 16.5/97.9 GB | 85171 | Gemma ZH translate |
| 2 | 13% | 16.5/97.9 GB | 59571 | COMET Llama validation |
| 3 | 30% | 16.2/97.9 GB | 462040 | DE translate Llama |

---

### 1. COMET Llama (PID 59571, cuda:2) — **ACTIVE, 非 STUCK**

- 运行时间：10h22m，CPU 81.2%
- 任务：`validate_translation.py` back-translation 验证
- **test 集已完成**（`zh_conflict_test_validated.jsonl` 77KB，10:50 完成）
- **quality report 已完成**（`translation_quality_report.json` 25KB，10:50 完成）
- **train 集 back-translation 进行中**：**[800/1096] = 73%**
- `zh_conflict_train_validated.jsonl` 尚未写入（处理完 1096 条后才写）
- 日志最后更新 17:21（但 CPU 81% 说明仍在推理，日志每 20 条打印一次）
- **ETA：约 2-2.5h**（~296 条剩余）

### 2. Steering v3 Llama (PID 468898, cuda:0) — **ACTIVE**

- 运行时间：52min，CPU 53.4%
- Steering layer 28，probe accuracy=0.7757
- Baseline 已完成：`{both:35, neither:28, parametric:32, contextual:41}`
- 已生成 **1603 次 steered generation**（136 samples/alpha，约 **11-12 个 alpha 已评估**）
- 日志 1632 行，持续增长（17:38 最后更新）
- 无 "Alpha" 关键字（脚本用其他格式记录进度）
- **ETA：取决于总 alpha 数，若 15-20 个 alpha，约 20-40min 剩余**

### 3. Gemma ZH translate (PID 85171, cuda:1) — **ACTIVE，即将完成**

- 运行时间：4h31m，CPU 62.7%
- **train 集已完成**：1274/1274 行
- **test 集进行中**：**[280/316] = 89%**
- **ETA：约 10-15 min**

### 4. DE translate Llama (PID 462040, cuda:3) — **ACTIVE**

- 运行时间：1h47m，CPU 62.0%
- **注意：PID 是 462040，不是 462035**
- partial 文件：**750/1096 train = 68%**
- 完成的 train/test jsonl 尚未写入
- 78 个 "translated" 日志条目
- **ETA：约 1.5h**（346 条剩余）

### 5. Bootstrap n=2000 (optimized) — **ACTIVE，无 GPU**

- **Qwen fast**：818/2000 tasks，已用 24.8min，~33 tasks/min → **约 36min 剩余**
- **Llama fast**：第一组 (en_en) **已完成**（80.5min），现在跑 **zh_zh** split，刚启动
- 输出 JSON 均未生成（完成所有 split 后才写入）

### 6. C3 MLP bootstrap — **部分完成**

- **Qwen：DONE** ✓
  - `c3_mlp_bootstrap_results.json`：delta=+0.0384, CI=[-0.036, +0.113], **excludes_zero=False**, peak_layer=23
- **Llama fix：RUNNING**，layer 5，[400/1000] bootstrap
  - delta 趋势：~+0.050，ETA ~**5300s (≈88min)**
  - 输出文件尚未生成

---
