# knowledge 7b post pipeline prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_7b-post-pipeline-prep_20260520T003320_result.json`
- **Structured JSON:** [`0ae44f9a40416e5821bc.json`](../../sessions/0a/0ae44f9a40416e5821bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary.

---

## format_for_scaling.py 命令准备

### 前置步骤：compute_signals.py

Pipeline 的 Phase 4 用的是 `analyze_fewnerd_results.py`（产出 per-seed `report.json`），**不是** `compute_signals.py`。而 `format_for_scaling.py` 需要 `full_signal_report.json`（`compute_signals.py` 的产物）。所以 pipeline 完成后需先跑 compute_signals。

`compute_signals.py` 和 `format_for_scaling.py` 都已在服务器 `/root/autodl-tmp/struct_self_consist_ie/` 根目录下（72B pipeline prep 时上传的）。

### 7B 推理输出路径（3 seeds）

```
output/qwen25_7b_fewnerd_seed42/fewnerd/samples.jsonl
output/qwen25_7b_fewnerd_seed123/fewnerd/samples.jsonl
output/qwen25_7b_fewnerd_seed456/fewnerd/samples.jsonl
```

### 7B 完整命令

```bash
cd /root/autodl-tmp/struct_self_consist_ie

# Step 1: 每个 seed 跑 compute_signals（产出 full_signal_report.json）
for SEED in 42 123 456; do
  python compute_signals.py \
    --input-dir output/qwen25_7b_fewnerd_seed${SEED} \
    --model-size 7 --regime ft
done

# Step 2: format_for_scaling（取 seed42 作为代表值）
python format_for_scaling.py \
  --report output/qwen25_7b_fewnerd_seed42/full_signal_report.json \
  --model-size 7 --regime ft
```

**预期输出路径**：`output/qwen25_7b_fewnerd_seed{42,123,456}/full_signal_report.json`

### 14B 模板

```bash
cd /root/autodl-tmp/struct_self_consist_ie

for SEED in 42 123 456; do
  python compute_signals.py \
    --input-dir output/qwen25_14b_fewnerd_seed${SEED} \
    --model-size 14 --regime ft
done

python format_for_scaling.py \
  --report output/qwen25_14b_fewnerd_seed42/full_signal_report.json \
  --model-size 14 --regime ft
```

### 32B 模板

```bash
cd /root/autodl-tmp/struct_self_consist_ie

for SEED in 42 123 456; do
  python compute_signals.py \
    --input-dir output/qwen25_32b_fewnerd_seed${SEED} \
    --model-size 32 --regime ft
done

python format_for_scaling.py \
  --report output/qwen25_32b_fewnerd_seed42/full_signal_report.json \
  --model-size 32 --regime ft
```

### 注意事项

1. **output 目录命名**：以上路径基于日志推断（`qwen25_{size}b_fewnerd_seed{SEED}`），pipeline 完成后需用 `ls output/` 确认实际目录名
2. **seed 选择**：上面取 seed42 做 format_for_scaling 代表值。如需跨 seed 平均 rho/F1，需额外汇总脚本
3. **compute_signals.py 已在服务器**：72B pipeline 准备时已上传到项目根目录（May 20 02:27, 17KB），无需再次上传
4. **format_for_scaling.py 同理**：也在项目根目录（May 20 02:25, 5KB）

---
