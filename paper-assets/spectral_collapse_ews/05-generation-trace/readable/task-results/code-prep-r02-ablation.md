# code prep r02 ablation

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-r02-ablation_20260518T064840_result.json`
- **Structured JSON:** [`e0399efd8a201c8c8bf7.json`](../../sessions/e0/e0399efd8a201c8c8bf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. run_phase1.py 代码修改（3处）

| 修改 | 位置 | 内容 |
|------|------|------|
| 新增 `--real_ratio` 参数 | line 98-99 | `type=float, default=0.5`，向后兼容 |
| `fixed_mix` 分支使用参数 | line 125-126 | `config.real_data_ratio = args.real_ratio`，替代硬编码 0.5 |
| `run_tag` 路径区分 | line 158-161 | 当 `real_ratio != 0.5` 时，tag 变为 `fixed_mix_r02_seed42` |

默认值 0.5 保持向后兼容，现有实验不受影响。

### 2. Launch script

已创建 `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r02.sh`，参数：`--condition fixed_mix --real_ratio 0.2 --generations 5 --seed 42 --k 0`。

### 3. 路径冲突检查

| | exp_004 (r=0.5) | exp_007 (r=0.2) |
|--|--|--|
| checkpoint | `checkpoints_phase1/fixed_mix_seed42/` (已存在) | `checkpoints_phase1/fixed_mix_r02_seed42/` (不存在) |
| results | `phase1_fixed_mix_seed42_results.json` (已存在) | `phase1_fixed_mix_r02_seed42_results.json` (不存在) |

无冲突。

### 4. Dry-run

`python run_phase1.py --help` 正常输出，`--real_ratio` 参数已列出。import 无语法错误。

---
