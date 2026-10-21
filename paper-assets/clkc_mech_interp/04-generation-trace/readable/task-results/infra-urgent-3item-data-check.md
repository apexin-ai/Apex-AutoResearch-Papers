# infra urgent 3item data check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-3item-data-check_20260522T122303_result.json`
- **Structured JSON:** [`7bcb8b08974ba7487cf6.json`](../../sessions/7b/7bcb8b08974ba7487cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 检查结果

### 1. Steering v2c (L28) 结果

文件: `steering_results.json`（注意 config 里 `position: "last"`，不是 all-position）

| alpha | steering flip% | control flip% | Fisher p | p→c | c→p | 定向合计 |
|-------|---------------|---------------|----------|-----|-----|---------|
| -20 | 14.71% | 16.91% | 0.740 | 0 | 2 | 2 |
| -10 | 10.29% | 9.56% | 1.000 | 0 | 1 | 1 |
| -5 | 4.41% | 3.68% | 1.000 | 1 | 0 | 1 |
| -2 | 3.68% | 2.94% | 1.000 | 1 | 0 | 1 |
| -1 | 4.41% | 2.94% | 0.749 | 2 | 0 | 2 |
| 1 | 0.74% | 0.74% | 1.000 | 0 | 0 | 0 |
| 2 | 2.21% | 1.47% | 1.000 | 0 | 0 | 0 |
| 5 | 3.68% | 4.41% | 1.000 | 0 | 0 | 0 |
| 10 | 7.35% | 6.62% | 1.000 | 0 | 0 | 0 |
| 20 | 12.50% | 17.65% | 0.309 | 1 | 0 | 1 |

n=136, probe_accuracy=77.6%, **所有 alpha 的 Fisher p 均不显著**。定向 flips 极少（每个 alpha 0-2 个），steering 效果基本为零。

**注意：** 文件里 position="last"，不是 "all"。目录下没有其他 JSON 文件，all-position 版本可能还没跑。

---

### 2. C3 MLP Bootstrap Llama L18

**进程 467703: 仍在运行**，接近完成（950/1000 iterations，ETA ~554s ≈ 9分钟）。

最新进度：
- delta = **0.0522**（MLP 比 LR 高 ~5.2%）
- LR accuracy = 0.5737
- MLP accuracy = 0.6259
- 趋势稳定，delta 从 0.0455 缓慢上升到 0.0522

结果文件 `c3_mlp_bootstrap_results_fix.json` **尚未生成**（等 1000 轮完成后写入）。`/root/clkc_mech_interp/data/` 下有一个旧版 `c3_mlp_bootstrap_results.json`（非 fix 版，不在 llama31 子目录）。

---

### 3. DE Translate Llama (plan_112)

**进程 462040: 仍在运行。**

- `de_conflict_train.jsonl`: **存在**，1096 行，1.2MB
- `de_conflict_test.jsonl`: **不存在**
- `.partial` 文件: 不存在
- 日志全是 `Setting pad_token_id to eos_token_id` 的生成信息，仍在跑

---
