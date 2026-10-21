# debug exp6 vanilla inconsistency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp6-vanilla-inconsistency_20260518T144423_result.json`
- **Structured JSON:** [`781b53ea612088e28890.json`](../../sessions/78/781b53ea612088e28890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整排查报告。

---

## 排查报告

### 1. 根因

exp6 脚本 (`src/exp6_actorattack_perturbation.py`) 使用了**错误的 checkpoint**，涉及 3 个 variant-seed 组合：

| variant | seed | exp2 正确路径 | exp6 错误路径 | MD5 不同 |
|---|---|---|---|---|
| vanilla | 123 | `plan_002_seed123/gru/baseline/best.pt` | `vanilla_seed123_gru/best.pt` | ✓ |
| vanilla | 456 | `plan_002_seed456/gru/baseline/best.pt` | `vanilla_seed456_gru/best.pt` | ✓ |
| binary | 42 | `mf1_binary_seed42/` (DeBERTa+GRU) | `plan_013_none_collapse/` (BACKUP) | ✓ |

评估逻辑、数据加载、F1 计算方式完全一致，唯一差异就是 checkpoint 路径。

### 2. 修正范围

**已修正** exp6 脚本和结果文件。修正前后 clean_k1 对比：

| variant | 修正前 | 修正后 | exp2 值 | 一致 |
|---|---|---|---|---|
| vanilla mean | 0.439 | **0.337** | 0.337 | ✓ |
| binary mean | 0.765 | **0.737** | 0.737 | ✓ |
| 其他 5 个变体 | — | 无变化 | — | ✓ |

McNemar 测试也已用正确 checkpoint 重算。

### 3. 定性影响

| 问题 | 结论 |
|---|---|
| "所有变体均退化" | **仍成立**（topic k1 除外，delta +0.012），但 vanilla 和 binary 的退化幅度显著变小 |
| vanilla delta_k1 | -0.146 → **-0.068**（退化减半，因为 baseline 本就很低，floor effect） |
| binary delta_k1 | -0.126 → **-0.068**（seed42 delta 从 -0.176 变为 -0.001） |
| 9class vs vanilla McNemar | **不变**，仍全部 p<0.001，方向 A>B，修正后差距更大 |
| 论文叙事影响 | 需要修正 perturbation table 中的 vanilla 和 binary 行；结论不变但措辞需调整退化幅度 |

---
