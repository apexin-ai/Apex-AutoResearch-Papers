# experiment mvp launch v3

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_launch_v3_20260513T102340_result.json`
- **Structured JSON:** [`0278314e5566e20c57da.json`](../../sessions/02/0278314e5566e20c57da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已提交，GPU 开始工作。

## 汇报

### 干跑结果（1 条 trace，cr=0.7）
| Method | KIRR | PPL | Retained/Planted |
|--------|------|-----|------------------|
| Full (no compression) | 1.0 | 2.19 | 7/7 |
| Uniform EA | 0.29 | 2.19 | 2/7 |
| TurnKV | 0.14 | 2.19 | 1/7 |

**修复了一个 bug**：kvpress 0.5.3 的 `press(model)` 上下文管理器 `yield` 不返回 model，evaluate.py 中 `with apply_press(...) as m` 导致 `m=None`。已修复为 `with apply_press(...)` + 直接使用 `model`。

### 实验提交确认

| 实验 | GPU | tmux session | PID | 压缩率 |
|------|-----|-------------|-----|--------|
| mvp_eval_01_cr70 | cuda:0 | `mvp_eval_01_cr70` | 84539 | 0.70 |
| mvp_eval_01_cr85 | cuda:1 | `mvp_eval_01_cr85` | 84683 | 0.85 |

10 条 traces × 3 methods (full + uniform_ea + turnkv)，预计每个实验 ~4 分钟完成。

---
