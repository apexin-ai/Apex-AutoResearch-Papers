# fix ss s123 tf numturns bug

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ss_s123_tf_numturns_bug_20260523T173656_result.json`
- **Structured JSON:** [`817fcd3fe7ac0caf5de3.json`](../../sessions/81/817fcd3fe7ac0caf5de3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s456 script calls `eval_phase2_gar.py` — our fix is already in place. No script changes needed.

## 修复后的 SS s123 TF GAR
- GAR-ours mid_turns_avg (turns 3+): **0.495177** (208 values from 127 convs with 3+ turns)
- GAR-dongre mid_turns_avg (turns 3+): **0.381566** (208 values from 127 convs with 3+ turns)

(补充指标: turns 2+ avg: ours=0.506998, dongre=0.387424; overall avg: ours=0.522328, dongre=0.395046)

## Bug 根因
- **原因**: `eval_phase2_gar.py` 第 513 行用 `min_turns = min(len(c) for c in all_gar_curves)` 把所有 conversation 的 GAR curve 截断到最短长度。`eval_200.json` 数据中 71/200 条 conversation 只有 2 个 assistant turn，导致 `min_turns=2`。然后第 524 行 `mid_turns_gar = np.mean(avg_gar[2:])` 对长度为 2 的数组取 `[2:]` → 空数组 → NaN
- **s42 为什么没问题**: s42 用的是 `ultrachat_eval_heldout.json`（所有 conversation ≥ 3 turns），`min_turns=3`，`avg_gar[2:]` 至少有 1 个元素
- **影响范围**: 仅影响 TF eval 结果的 `mid_turns_avg_gar` 和 `num_turns` 字段。raw `gar_curves` 数据完好无损，AR eval 不受影响

## 修复内容 (`src/eval_phase2_gar.py`)
1. `mid_turns_gar` 改为从所有 conversation 的 turns 3+（index 2+）直接池化计算，不再依赖 min_turns 对齐
2. `num_turns` 改为 `max_turns`，新增 `min_turns` 字段
3. 修改不影响运行中的 AR eval（PID 110052 用的是 `eval_attention_steering.py`）

## s456 eval 脚本是否已修复
- **已修复**: s456 脚本直接调用 `eval_phase2_gar.py`，代码层面的 fix 已生效，无需改脚本

---
