# diag gemma2 d025 arc eval bug investigation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-d025-arc-eval-bug-investigation_20260520T223007_result.json`
- **Structured JSON:** [`b10076635734908fa328.json`](../../sessions/b1/b10076635734908fa328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完全一致：D=634, A=57。

## 调查结论

- **Bug 确认**: **No** — 不是 eval 脚本 bug
- **原因**: d025_s0 adapter 本身在 ARC 上产生极端 D 偏置（54.1%），这是 adapter 的固有行为，已通过独立 re-run 精确复现（0.6485, 760/1172, D=634, A=57）
- **影响范围**: **仅 d025_s0**。d000_s0/d005_s0/d050_s0 ARC 均正常 (85-87%)
- **其他 dosage ARC 结果可信**: 是。d000=85.84%, d005=86.77%, d050=85.49% 均在正常范围
- **d025_s0 ARC 实际结果**: 64.85% 是真实结果（非 bug）

**关键证据**:

| 检查项 | 结果 |
|--------|------|
| 数据源混淆 (MMLU vs ARC) | 排除：1172 items，gold labels 正确 |
| Eval 脚本差异 | 排除：md5sum 一致，命令参数相同 |
| Tokenizer/Chat template 差异 | 排除：d025_s0 与 d000_s0 完全一致 |
| Adapter 文件损坏 | 排除：文件大小正常 (216MB)，同 adapter MMLU 正常 |
| Transient GPU 错误 | 排除：独立 re-run 完全复现 |
| 同 adapter MMLU 表现 | 正常 (64.91%)，D 预测占比 25.3%（无偏置） |

**现象本质**: d025_s0 adapter 在 ARC 格式的 25-shot logprob 评估下，对 "D" token 的 logit 异常高（A 仅预测 57 次 = 4.9%），但在 MMLU 5-shot 下行为完全正常。这可能与 d025 dosage 在 seed=0 下选取的 contamination subset 与 ARC 25-shot prompt format 的特定交互有关。建议：
1. 检查 d025_s0 训练数据中 ARC contamination items 的 answer 分布
2. 考虑是否需要重训 d025_s0 或将其标记为 outlier

---
