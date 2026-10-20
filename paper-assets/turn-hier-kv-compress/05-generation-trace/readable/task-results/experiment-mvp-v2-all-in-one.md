# experiment mvp v2 all in one

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_v2_all_in_one_20260513T111411_result.json`
- **Structured JSON:** [`fc42770fa24bbce81199.json`](../../sessions/fc/fc42770fa24bbce81199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 1. 代码修复确认
| 文件 | 修复内容 | 状态 |
|------|---------|------|
| `eass.py` | `map_budget_to_scores` 添加 token-weighted budget 归一化 | ✓ 已同步到服务器 |
| `metrics.py` | `compute_perplexity` 改为两步法（prefix→KV cache→target） | ✓ 已同步到服务器 |
| `evaluate.py` | `apply_press(press, model)` + `bfloat16`，无 `as m`/`ea_press` | ✓ 无需修改 |

### 2. Traces
- 总计 **80 条**：48 standard + 32 adversarial
- 586 planted_info，0 缺失（所有 expected_answer 均出现在 messages 中）

### 3. 干跑结果（1 trace, CR=0.7）
| 方法 | PPL | KIRR |
|------|-----|------|
| Full | 7.75 | 0.0 |
| Uniform EA | 14.94 | 0.0 |
| TurnKV | 12.00 | 0.0 |

- PPL ratio (TurnKV/UniformEA) = **0.8033** — TurnKV PPL 显著低于 Uniform EA
- KIRR 单 trace 全为 0（Full 也是 0），需 80 traces 聚合

### 4. 实验提交
| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| mvp_eval_02_cr70 (CR=0.7) | cuda:0 | `mvp_eval_02_cr70` | 已提交 |
| mvp_eval_02_cr85 (CR=0.85) | cuda:1 | `mvp_eval_02_cr85` | 已提交 |

---
