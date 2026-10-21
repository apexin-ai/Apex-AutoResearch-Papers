# code exp backup1 het temp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_backup1_het_temp_20260520T171033_result.json`
- **Structured JSON:** [`c2833985dc6bcf7a35d7.json`](../../sessions/c2/c2833985dc6bcf7a35d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出

**脚本**: `artifacts/experiments/het_temp/run_het_temp.py` — 语法通过，dry run 通过。

### 可用温度数据对

| Dataset | Model | T_low | T_high | Seeds | T_low 路径 | T_high 路径 |
|---------|-------|-------|--------|-------|-----------|------------|
| SciERC | Qwen | T=0.8 | T=1.0 | 42, 123, 456 | `exp_026_t08[_seed*]` | `exp_026_t10_seed*` |
| SciERC | Qwen | T=0.5 | T=1.0 | 42, 123, 456 | `exp_026_t05[_seed*]` | `exp_026_t10_seed*` |
| CoNLL | LLaMA | T=0.7 | T=1.0 | 仅1个(默认) | `exp_017_llama_conll_n8_t07` | `exp_017_llama_conll`(需确认N=8) |

**无 T_low 数据**: CoNLL Qwen、FewNERD (所有 model)。

### 运行示例（SciERC T=0.8 vs T=1.0, seed42）

```bash
python run_het_temp.py \
  --t_low_path /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08/samples.jsonl \
  --t_high_path /root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl \
  --t_low_label "T=0.8" --t_high_label "T=1.0" \
  --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_backup1_het_temp/scierc_t08_t10_s42 \
  --n_repeats 10 --seed 42
```

---
