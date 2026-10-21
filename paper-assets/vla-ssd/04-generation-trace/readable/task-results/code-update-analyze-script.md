# code update analyze script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-analyze-script_20260515T110435_result.json`
- **Structured JSON:** [`5ccdaead48862eaae3ff.json`](../../sessions/5c/5ccdaead48862eaae3ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部改动验证通过。汇总：

| 改动 | 行号 | 状态 |
|------|------|------|
| ρ 下限 0.3→0.5 | L277 `best_rho > 0.5` | OK |
| `bootstrap_delta_rho()` | L249 定义, L294 调用 | OK |
| Δρ CI 排除 0 才 PASS | L303 `max_delta > 0.1 and ci_excludes_zero` | OK |
| subtask gate: `vla_AUC > 0.7 AND > dino_AUC + 0.05` | L323 | OK |
| `plot_per_layer_rho_profile()` | L210 定义, L414 调用 | OK |
| 三分支判定逻辑 | L331-337 | OK |
| 语法检查 | `ast.parse` SYNTAX_OK | OK |
| 原文件备份 | `analyze_results.py.bak` | OK |

文件从 377 行增长到 448 行（+71 行：bootstrap 函数、per-layer profile 图、更丰富的 criteria 字段）。

---
