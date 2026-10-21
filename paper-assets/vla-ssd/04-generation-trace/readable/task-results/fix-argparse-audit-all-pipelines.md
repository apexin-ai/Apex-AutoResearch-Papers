# fix argparse audit all pipelines

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_argparse_audit_all_pipelines_20260521T090252_result.json`
- **Structured JSON:** [`650e1690d04353dbcea5.json`](../../sessions/65/650e1690d04353dbcea5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 修复结果汇总

| # | 脚本 | 修复前 | 修复后 | 状态 |
|---|------|--------|--------|------|
| 1 | `nora_goal_full_pipeline.py` | `nargs="+"`, `choices=["trained","untrained"]`, `default=["trained","untrained"]` | — | **无需修复** ✓ |
| 2 | `nora_spatial_full_pipeline.py` | 同上 | — | **无需修复** ✓ |
| 3 | `tracvla_spatial_full_pipeline.py` | `default="trained,untrained"`, 无 nargs/choices, `.split(",")` 解析 | `nargs="+"`, `choices`, `default=[list]`, 直接 `args.conditions` | **已修复** |
| 4 | `tracvla_object_full_pipeline.py` | 同 #3 | 同 #3 | **已修复** |
| 5 | `tracvla_spatial_probing_only.py` | `default="trained"`, 无 nargs/choices, `.split(",")` 解析 | `nargs="+"`, `choices`, `default=["trained"]` | **已修复** |
| 6 | `libero_object_full_pipeline.py` | `default="trained"`, `choices` 有但无 nargs, 单值字符串, 无条件循环 | `nargs="+"`, `default=["trained","untrained"]`, 条件循环, `TRAINED_CKPT`/`UNTRAINED_CKPT`/`RESULTS_BASE` | **已修复** |
| 7 | `libero_long_full_pipeline.py` | 无 `--conditions` 参数, 无 untrained 支持 | 新增完整条件支持: `nargs="+"`, `UNTRAINED_CKPT=openvla-7b`, 条件循环 | **已修复** |
| 8 | `libero_object_untrained_full_pipeline.py` | 专用 untrained 脚本, 无 --conditions | — | **无需修复**（#6 修好后可废弃） |

输出路径隔离确认：
- **libero_object**: trained → `results/libero_object/`, untrained → `results/libero_object_untrained/`
- **libero_long**: trained → `results/libero_long/`, untrained → `results/libero_long_untrained/`
- **tracvla_\***: trained → `results/tracvla_{spatial,object}/trained/`, untrained → `…/untrained/`
- **nora_\***: 同 tracvla 模式

---
