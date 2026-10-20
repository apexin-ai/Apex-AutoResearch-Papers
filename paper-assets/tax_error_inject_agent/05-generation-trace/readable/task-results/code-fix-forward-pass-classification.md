# code fix forward pass classification

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-forward-pass-classification_20260515T165120_result.json`
- **Structured JSON:** [`f6ffb6f844f533aba439.json`](../../sessions/f6/f6ffb6f844f533aba439.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正在运行。vanilla 分类正确（Clean=4358, Injected=0）。Forward pass 以约 3 it/s 进行，1090 batches × 6 runs 预计约 40 分钟。

汇总修复结果：

### 修复完成

**Bug**: `classify_sample()` 逐 turn 检查 `[Error Type: ...]` tag → 只有含 tag 的 turn 被标记为 injected（760/9029），其他 injected trajectory 的 turns 被错误标为 clean。

**修复**: 
- `classify_sample()` → `classify_operator()`（仅返回 operator 类型，用于 per-operator 分析）
- `load_data()` 新增 `--vanilla-data` 参数，对比 vanilla 数据的 `messages[0]["content"]` 判断 trajectory 归属

**验证结果**:

| 数据集 | 修复前 clean/injected | 修复后 clean/injected |
|--------|----------------------|----------------------|
| taxei_full | 8269 / 760 | 4358 / 4671 |
| random_full | 8269 / 760 | 4358 / 4671 |
| vanilla | 4358 / 0 | 4358 / 0 |
| inject10 | 4288 / 70 | 3922 / 436 |
| inject25 | 4190 / 168 | 3268 / 1090 |
| inject50 | 3988 / 370 | 2179 / 2179 |

**Per-operator 分类**: 保持不变（P1=188, P2=192, C1=191, C4=189，共 760 tagged turns）

**Forward pass**: 已提交到 cuda:2（exp_id=`v4-training-dynamics-forward-v2`），包含 6 个 checkpoint + 绘图，输出到 `artifacts/training_dynamics_v2/`。

---
