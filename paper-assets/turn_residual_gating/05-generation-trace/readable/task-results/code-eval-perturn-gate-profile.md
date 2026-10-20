# code eval perturn gate profile

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_perturn_gate_profile_20260518T201703_result.json`
- **Structured JSON:** [`1e9fe245d9c09b2b0066.json`](../../sessions/1e/1e9fe245d9c09b2b0066.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。

## 修改汇总

**新增函数**:
- `_extract_per_turn_gates(gate_values, turns)` (L70-85): 从单次 forward pass 的 gate_values 中按 turn boundary 分段，对每个 turn 的每层 gate 值取均值
- `_compute_gate_dynamic_range(all_gate_profiles, num_layers)` (L88-109): 跨 conversation 聚合，计算每层的 first turn vs last turn 均值及 diff

**修改函数**:
- `measure_gar_per_turn`: 新增 `gate_values_ref`、`gate_profile` 参数；forward pass 后调用 `_extract_per_turn_gates` 提取 per-turn gate 数据
- `main()`: 新增 `--gate-profile` CLI flag；measurement loop 中收集 gate profiles；输出 JSON 增加 `gate_profile_per_turn` 和 `gate_dynamic_range` 字段；末尾打印 top-10 dynamic range 层

**gate 值处理**: gate 是 per-token 的 `(1, seq_len, 1)`，按 `boundaries["turns"]` 的 `content_start:content_end` 切片后取 `.float().mean()`

## 使用示例

```bash
python eval_phase2_gar.py \
  --checkpoint-dir /root/turn_residual_gating/checkpoints/tg_s42 \
  --gate-type threadgate \
  --gate-profile
```

---
