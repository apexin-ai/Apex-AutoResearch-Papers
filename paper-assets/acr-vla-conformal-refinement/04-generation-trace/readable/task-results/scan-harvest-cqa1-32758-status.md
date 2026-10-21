# scan harvest cqa1 32758 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan-harvest_cqa1-32758-status_20260523T172001_result.json`
- **Structured JSON:** [`033dfbdb2aa41b447769.json`](../../sessions/03/033dfbdb2aa41b447769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新实验已启动，模型正在加载。

## 汇报

### cqa1-32758 全 6 GPU 状态

| GPU | exp_id | 状态 | SR / 进度 |
|-----|--------|------|-----------|
| cuda:0 | ~~eval-supp-obj-reconvla-s44~~ → **eval-supp-long-k2mean-s44** | ✅ DONE → 🆕 刚启动 | **76.0%** (已收割) → 加载中 |
| cuda:1 | eval-supp-long-adapt-tau025-s44 | 🔄 运行中 | 4/10 tasks |
| cuda:2 | eval-supp-long-vla-only-s43 | 🔄 运行中 | 8/10 tasks |
| cuda:3 | ~~eval-supp-k2mean-object-s44~~ → **eval-supp-long-reconvla-s44** | ✅ DONE → 🆕 刚启动 | **75.0%** (已收割) → 加载中 |
| cuda:4 | eval-supp-long-k2mean-s42 | 🔄 运行中 | 9/10 tasks (即将完成) |
| cuda:5 | eval-supp-long-crm-norm005-s44 | 🔄 运行中 | 4/10 tasks |

### 收割结果

| exp_id | SR | 3-seed 汇总 |
|--------|-----|-------------|
| eval-supp-obj-reconvla-s44 | **76.0%** | Object Reconvla 3-seed: 79.0 / 77.0 / 76.0 → **77.3±1.5%** |
| eval-supp-k2mean-object-s44 | **75.0%** | Object K2mean 3-seed: 79.5 / 78.0 / 75.0 → **77.5±2.3%** |

### 新部署

| GPU | 新 exp_id | 命令 |
|-----|-----------|------|
| cuda:0 | eval-supp-long-k2mean-s44 | `--mode vla_only --baseline_mode mean --K 2 --benchmark long --seed 44` |
| cuda:3 | eval-supp-long-reconvla-s44 | `--mode reconvla --K 10 --benchmark long --seed 44` |

填补 Long suite 最后两个 s44 缺口（K2mean + Reconvla），Long suite 5×3=15 全部实验现已覆盖。

---
