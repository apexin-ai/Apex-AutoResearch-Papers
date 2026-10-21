# code contamination 60 scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_contamination_60_scripts_20260515T202717_result.json`
- **Structured JSON:** [`02adff338502c1497c41.json`](../../sessions/02/02adff338502c1497c41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 脚本路径
| 实验 | 脚本 |
|------|------|
| adaptive (ρ=0.6) | `/root/provenance_weight_training/run_contamination_60_adaptive.sh` |
| uniform (ρ=0.6) | `/root/provenance_weight_training/run_contamination_60_uniform.sh` |
| grid b=0.5 (ρ=0.6) | `/root/provenance_weight_training/run_contamination_60_grid_b05.sh` |

### 验证结果
- 数据文件 `scored_data_60.jsonl`：✅ 存在，907MB
- `bash -n` 语法检查：✅ 3 个脚本均通过
- output 目录：✅ 3 个目标目录均不存在，无覆盖风险
- 权限：✅ 已 chmod +x

### 参数修正
任务描述中有 2 处参数名与实际脚本不匹配，已修正：
- `--weighting_method fixed` → **`grid`**（脚本 choices 中无 `fixed`）
- `--fixed_b 0.5` → **`--grid_b_value 0.5`**（实际参数名）

---
