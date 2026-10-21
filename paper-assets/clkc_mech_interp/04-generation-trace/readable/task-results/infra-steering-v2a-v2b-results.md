# infra steering v2a v2b results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_steering-v2a-v2b-results_20260522T130027_result.json`
- **Structured JSON:** [`4dc9c64eb5ba9565ad10.json`](../../sessions/4d/4dc9c64eb5ba9565ad10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是汇总报告。

---

## 实验状态报告 (2026-05-22)

### 1. Steering v2a — L13 (PID 479381/479386) 🔄 RUNNING

运行时间: 1h30m | GPU 1: 16107 MiB | Probe acc: 0.7610

**当前进度**: 已完成 α=-20 到 α=+5，正在跑 α=+10。还剩 α=+10 和 α=+20。

| alpha | Steering flips | Control flips | Fisher p | p→c | c→p |
|-------|---------------|---------------|----------|-----|-----|
| -20.0 | 49/136 (36.0%) | 24/136 (17.6%) | **0.0009** | 1 | 5 |
| -10.0 | 31/136 (22.8%) | 25/136 (18.4%) | 0.4536 | 2 | 1 |
| -5.0 | 22/136 (16.2%) | 17/136 (12.5%) | 0.4893 | 2 | 1 |
| -2.0 | 16/136 (11.8%) | 9/136 (6.6%) | 0.2073 | 0 | 1 |
| -1.0 | 7/136 (5.1%) | 6/136 (4.4%) | 1.0000 | 0 | 0 |
| +1.0 | 11/136 (8.1%) | 6/136 (4.4%) | 0.3165 | 1 | 0 |
| +2.0 | 16/136 (11.8%) | 7/136 (5.1%) | 0.0794 | 3 | 0 |
| +5.0 | 27/136 (19.9%) | 9/136 (6.6%) | **0.0020** | 4 | 0 |
| +10.0 | *(running)* | | | | |

**初步判断**: L13 有信号。两个显著 alpha：
- α=-20: p=0.0009，但方向性弱（大量非定向 flips，c→p=5 占主导）
- α=+5: p=0.0020，方向清晰（p→c=4, c→p=0，纯向 contextual 方向）
- α=+2 接近显著 (p=0.079)，正方向趋势一致

---

### 2. Steering v2b — L18 (PID 479644/479649) 🔄 RUNNING

运行时间: 1h30m | GPU 2: 16107 MiB | Probe acc: 0.7390

**当前进度**: 同 L13，已完成 α=-20 到 α=+5，正在跑 α=+10。

| alpha | Steering flips | Control flips | Fisher p | p→c | c→p |
|-------|---------------|---------------|----------|-----|-----|
| -20.0 | 28/136 (20.6%) | 25/136 (18.4%) | 0.7597 | 0 | 4 |
| -10.0 | 18/136 (13.2%) | 17/136 (12.5%) | 1.0000 | 0 | 1 |
| -5.0 | 7/136 (5.1%) | 9/136 (6.6%) | 0.7976 | 0 | 0 |
| -2.0 | 3/136 (2.2%) | 5/136 (3.7%) | 0.7225 | 0 | 0 |
| -1.0 | 3/136 (2.2%) | 5/136 (3.7%) | 0.7225 | 0 | 0 |
| +1.0 | 4/136 (2.9%) | 3/136 (2.2%) | 1.0000 | 1 | 0 |
| +2.0 | 5/136 (3.7%) | 2/136 (1.5%) | 0.4470 | 1 | 0 |
| +5.0 | 9/136 (6.6%) | 7/136 (5.1%) | 0.7976 | 1 | 0 |
| +10.0 | *(running)* | | | | |

**初步判断**: L18 **negative**。所有 alpha 的 p > 0.44，无显著效应。Steering flips 和 control flips 基本持平。

---

### 3. Qwen Steering L23 (PID 485325) 🔄 JUST STARTED

运行时间: ~1 min | GPU 0: 14986 MiB | Probe acc: 0.7321

- 模型已加载，正在跑 baseline（84 samples）
- Alphas: -20, -10, -5, 5, 10, 20
- 预计还需 ~1.5h（参考 Llama 跑 10 个 alpha 用了 1.5h，Qwen 6 个 alpha 应更快）

---

### 4. DE Translate (PID 462040) 🔄 RUNNING

运行时间: 5h10m | GPU 3: 16194 MiB

- `de_conflict_train.jsonl`: **1096 行**（已完成）
- `de_conflict_test.jsonl`: **不存在**（未开始或正在处理）
- 日志无进度指标，仍在生成中

---

### GPU 总览

| GPU | Memory | Util | 任务 |
|-----|--------|------|------|
| 0 | 14995/97887 MiB | 2% | Qwen Steering L23 |
| 1 | 16107/97887 MiB | 8% | Llama Steering L13 |
| 2 | 16107/97887 MiB | 12% | Llama Steering L18 |
| 3 | 16203/97887 MiB | 21% | DE Translate |

---

### 待办

四个实验都还在跑，尚不能更新 registry 为 DONE。L13/L18 还剩 α=+10 和 α=+20 两个点，预计 20-30 分钟内完成。完成后需要再次检查以读取最终结果文件并更新 registry。

L13 初步结论倾向 **success**（α=+5 显著且方向正确），L18 倾向 **negative**，但需等 α=+10/+20 的结果确认。

---
