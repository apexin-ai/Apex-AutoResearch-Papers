# code prep all rcrit scripts

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-all-rcrit-scripts_20260518T095203_result.json`
- **Structured JSON:** [`0cc987c98b8a707f0889.json`](../../sessions/0c/0cc987c98b8a707f0889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### run_phase1.py 代码状态
- **无需改代码**。`--real_ratio`、`--seed`、`--condition` 全部已支持。
- pure collapse 条件名：`pure_collapse`
- 路径冲突：**无冲突**。run_tag 生成逻辑已包含 seed 和 ratio 区分：
  - `pure_collapse_seed{43,44}` — 各自独立
  - `fixed_mix_seed{43,44}` — r=0.5 默认值，不加 ratio 后缀但 seed 不同
  - `fixed_mix_r02_seed{43,44}` — ratio 非 0.5 时自动加 `_r0X` 前缀
  - r=0.05 → `fixed_mix_r005_seed42`，r=0.3 → `fixed_mix_r03_seed42` 等，全部唯一

### 创建的 10 个脚本

| # | 脚本 | condition | ratio | seed | gens |
|---|------|-----------|-------|------|------|
| 1 | `launch_fixed_mix_r03.sh` | fixed_mix | 0.3 | 42 | 10 |
| 2 | `launch_fixed_mix_r01.sh` | fixed_mix | 0.1 | 42 | 10 |
| 3 | `launch_fixed_mix_r005.sh` | fixed_mix | 0.05 | 42 | 10 |
| 4 | `launch_fixed_mix_r07.sh` | fixed_mix | 0.7 | 42 | 10 |
| 5 | `launch_pure_collapse_s43.sh` | pure_collapse | — | 43 | 10 |
| 6 | `launch_pure_collapse_s44.sh` | pure_collapse | — | 44 | 10 |
| 7 | `launch_fixed_mix_r05_s43.sh` | fixed_mix | 0.5 | 43 | 10 |
| 8 | `launch_fixed_mix_r05_s44.sh` | fixed_mix | 0.5 | 44 | 10 |
| 9 | `launch_fixed_mix_r02_s43.sh` | fixed_mix | 0.2 | 43 | 10 |
| 10 | `launch_fixed_mix_r02_s44.sh` | fixed_mix | 0.2 | 44 | 10 |

注意：现有 `launch_fixed_mix_r02.sh` 用的是 `--generations 5`（旧实验），新脚本统一用 `--generations 10`。

---
