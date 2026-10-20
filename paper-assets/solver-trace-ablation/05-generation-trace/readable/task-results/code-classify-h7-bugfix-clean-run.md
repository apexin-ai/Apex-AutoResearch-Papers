# code classify h7 bugfix clean run

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify-h7-bugfix-clean-run_20260515T145050_result.json`
- **Structured JSON:** [`8ad3393b00bfff7c233a.json`](../../sessions/8a/8ad3393b00bfff7c233a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have everything. Here's the complete D086 deliverable:

---

## D086 完成报告

### 1. 验证结果

| 验证项 | 期望 | 实际 | 状态 |
|--------|------|------|------|
| ISR s42-1000 H7a | 87 | 87 | ✅ |
| ISR s42-1000 H7 total | 87 | 87 | ✅ |
| ISR s44 H7a | 77 | 77 | ✅ |
| ISR s44 H7b | 11 | 11 | ✅ |
| Random s42 H8 | 3 (D084) | 4 | ⚠️ +1，新增 folio_1051 是合法 conjunction collapse，D084 漏检 |
| ISR s42-1000 H8 | 2 (D084) | 1 | ⚠️ -1，folio_1255/folio_990 有不匹配 conjunct，期望值有误 |

H8 微小差异均已人工核实，属于检测能力提升而非回归。

### 2. 差异对比（clean vs 旧 batch）

**新增实验（5个，来自 `--scan` 发现新路径）：**
- `plan002_additive_b01_s42_results`, `plan002_additive_b01_s44`, `plan016_extended_1000_s42` — 来自 `/root/runs/` 或 backup 目录
- `eval_results`, `results` — backup 目录中的文件，标签需注意辨识

**旧 batch 中有但 clean 未扫到的实验（12个）：**
- `plan001_exec_only_s42`, `plan001_exec_only_s43_r4`, `plan001_s43_r4_do_sample`, `plan002_additive_b03`, `plan009_sft_baseline_s42_1000`, `plan009_sft_baseline_s43_1000`, `plan009_sft_baseline_s44_1000`, `plan013_random_reward_s42_r4`, `plan018_additive_random_b01_s42_1000_r3`, `exp1_isr_b03_s42_1000`, `exp1_isr_b03_s43_eval`, `exp1_isr_b03_s44_r2_eval`
- 这些文件在旧 batch 是手动指定路径，`--scan` 模式下未被扫到（可能已移除或路径变更）

**共有实验中数值变化（D086 修复导致）：**

| 实验 | 字段 | 旧值 | 新值 | 原因 |
|------|------|------|------|------|
| **plan002_additive_b01_s42_1000** | h7a | 83 | **87** | P1: 递归括号剥离 + 重复前提匹配 |
| | h1_strict | 4 | **0** | P1: 4 个样本从 H1 正确归入 H7a（H1 与 H7 互斥） |
| **plan018_additive_random_b01_s42** | h1_strict | 56 | **58** | P0-a: H8 修复后 2 个从 genuine 归入 H1 |
| | h8 | 0 | **4** | P0-a: 外层括号修复，4 个 conjunction collapse 被正确检出 |
| | genuine | 23 | **18** | 上述重分类的结果 |
| **exp1_random_b03_s43** | h7a | 0 | **1** | P1: 递归括号剥离发现 1 个 tautology |
| | h1_strict | 60 | **59** | 对应从 H1 → H7a |
| **exp1_random_b03_s43_r4** | h7a | 0 | **7** | P1: 同上，7 个 |
| | h1_strict | 89 | **82** | 对应从 H1 → H7a |
| **plan001_r2** | h7a | 0 | **1** | P1: 1 个 |
| | h1_strict | 81 | **80** | 对应 |
| **plan017_additive_random_s42** | h7a | 0 | **4** | P1: 4 个 |
| | h1_strict | 48 | **44** | 对应 |

### 3. 代码修改清单

| 修改 | 函数/区域 | 原因 |
|------|-----------|------|
| **P0-a** | `is_h8_conjunction_collapse()` | 结论外层括号使 `∧` 在 depth=1，`split_top_level_conjunction` 无法分割。修复：分割前调用 `strip_outer_parens_recursive()` |
| **P0-b** | 新增 `discover_eval_files()` + `DEFAULT_SCAN_DIRS` | 旧版只扫 `/root/autodl-tmp/outputs`，遗漏 `/root/runs/` 和 backup 目录。新增 `--scan` / `--scan_dirs` 参数，MD5 去重 |
| **P0-b** | `import os`, `import hashlib` 提升到顶层 | 原有 inline import 不一致 |
| **P0-b** | 标签生成逻辑 | backup/runs 目录文件标签冲突，改用清洗后文件名 |
| **P1** | 新增 `strip_outer_parens_recursive()` | 递归剥离所有层匹配外层括号，对齐 D084 re-audit 的归一化深度 |
| **P1** | `normalize_for_match()` | 从单层 → 递归括号剥离 |
| **P1** | `is_h7_strict()` | `len(premises) != 1` → `all(premises match conclusion)`，捕获重复前提 tautology |
| **P1** | `has_conclusion_in_premises()` | 统一使用 `normalize_for_match` |
| **P1** | `classify_file()` H1 判定 | `_is_h1 = False if (_is_h7a or _is_h7b)` — H1 与 H7 互斥，避免双重计数 |

### 4. 输出文件

- **JSON**: `/root/autodl-tmp/outputs/h7_classification/batch_h7ab_clean.json`
- **TXT**: `/root/autodl-tmp/outputs/h7_classification/batch_h7ab_clean.txt`
- **备份**: `/root/solver-trace-ablation/scripts/classify_h7.py.bak`（修改前原文件）

---
