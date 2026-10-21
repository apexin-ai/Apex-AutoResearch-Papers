# code fix mid gar aggregation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_mid_gar_aggregation_20260520T194702_result.json`
- **Structured JSON:** [`a541a5a3b23d0a3b7094.json`](../../sessions/a5/a541a5a3b23d0a3b7094.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改后的代码正确。全部产出总结：

---

### 1. eval_attention_steering.py diff (lines 444-470)

**旧逻辑** (bug): `min_turns` 截断所有曲线到最短对话长度，然后在截断后的 avg 上算 mid_gar → N=50 gen 模式下最短对话 2 turns，mid_gar 退化为 turns 0-1 的均值。

**新逻辑** (lines 444-490):
- `avg_gar_per_turn` 改为 **padded average**（每个 turn 只对有该 turn 的对话取均值），不再截断
- `mid_gar` 改为 **per-conversation** 计算：每个对话独立算 `mean(curve[2:8])`，仅 ≥3 turns 的对话参与
- 新增输出字段：`mid_gar_std`, `n_valid_convs`, `per_conv_mid_gar`
- 向后兼容：`avg_gar_per_turn` 和 `mid_turns_avg_gar` 字段名不变

### 2. recalc_steering_mid_gar.py
路径: `/root/turn_residual_gating/scripts/recalc_steering_mid_gar.py`

用法: `python3 scripts/recalc_steering_mid_gar.py &lt;input.json> [output.json]`

### 3. N=5 验证结果

| Beta | Old mid_gar | New mid_gar | delta |
|------|-------------|-------------|-------|
| 0.0 | 0.028040 | 0.028040 | +0.000000 |
| 0.5 | 0.028680 | 0.028680 | -0.000000 |
| 1.0 | 0.034853 | 0.034853 | +0.000000 |
| 2.0 | 0.062009 | 0.062009 | +0.000000 |
| 5.0 | 0.679491 | 0.679491 | -0.000000 |
| 10.0 | 0.958999 | 0.958999 | -0.000000 |

完全一致——N=5 的 5 个对话都是 10 turns（硬编码数据），不受截断 bug 影响。

### 4. N=50 结果

JSON 尚未生成（实验仍在跑，最后一个 beta 约 conv 46/50）。但注意：**当前运行的 N=50 进程用的是旧代码**（修改只改了磁盘上的文件，已加载的进程不受影响），产出的 JSON 里 `mid_turns_avg_gar` 仍会是错误值，但 `gar_curves` 是正确的原始数据。等 N=50 完成后，用重算脚本即可修正：

```bash
python3 scripts/recalc_steering_mid_gar.py runs/attention_steering/&lt;n50_file>.json runs/attention_steering/&lt;n50_file>_fixed.json
```

---
