# audit table2 full reeval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table2_full_reeval_20260520T110921_result.json`
- **Structured JSON:** [`ff001084ac8de67ada6d.json`](../../sessions/ff/ff001084ac8de67ada6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`_cf_corrected` 文件不是 Table 2 所用的（DR% 偏移很大）。现在整理所有结果。

---

## A. 文件溯源表

| 行 | 服务器 | 完整路径 | 行数 | 模式 |
|---|--------|---------|------|------|
| Qwen unc | westd-16980 | `/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl` | 998 | unconstrained |
| Qwen con | westd-16980 | `/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl` | 998 | full_s1 |
| Llama unc | westd-16980 | `/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl` | 998 | unconstrained |
| Llama con | westd-16980 | `/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl` | 998 | full_s1 |

4 个文件全在 westd-16980 的 `outputs/` 目录，均 998 行（全量 DocRED dev）。

---

## B. eval_d064.py 完整输出

### Qwen LoRA DocRED unconstrained
```
=== qwen_unc ===
Samples: 998, Parse Fail: 71 (7.1%)
Entities pred: 18091, Relations pred: 15870
ET%=0.00  RV%=0.27  DR%=0.76  CF%=0.09
E-F1=82.15 (P=85.44 R=79.11)
R-F1=40.86 (P=36.41 R=46.56)
```

### Qwen LoRA DocRED constrained (Full S1)
```
=== qwen_con ===
Samples: 998, Parse Fail: 85 (8.5%)
Entities pred: 17799, Relations pred: 15563
ET%=0.00  RV%=0.00  DR%=0.01  CF%=0.27
E-F1=81.43 (P=85.41 R=77.81)
R-F1=40.56 (P=36.35 R=45.86)
```

### Llama LoRA DocRED unconstrained
```
=== llama_unc ===
Samples: 998, Parse Fail: 23 (2.3%)
Entities pred: 19106, Relations pred: 16171
ET%=0.00  RV%=0.15  DR%=0.49  CF%=0.08
E-F1=83.93 (P=84.93 R=82.96)
R-F1=43.72 (P=38.59 R=50.41)
```

### Llama LoRA DocRED constrained (Full S1)
```
=== llama_con ===
Samples: 998, Parse Fail: 25 (2.5%)
Entities pred: 19077, Relations pred: 16074
ET%=0.00  RV%=0.00  DR%=0.21  CF%=0.21
E-F1=83.94 (P=85.00 R=82.90)
R-F1=43.78 (P=38.79 R=50.24)
```

---

## C. 指标汇总表

| Metric | Qwen unc | Qwen con | Llama unc | Llama con |
|--------|----------|----------|-----------|-----------|
| E-F1 | 82.15 | 81.43 | 83.93 | 83.94 |
| E-P | 85.44 | 85.41 | 84.93 | 85.00 |
| E-R | 79.11 | 77.81 | 82.96 | 82.90 |
| R-F1 | 40.86 | 40.56 | 43.72 | 43.78 |
| R-P | 36.41 | 36.35 | 38.59 | 38.79 |
| R-R | 46.56 | 45.86 | 50.41 | 50.24 |
| DR% | 0.76 | 0.01 | 0.49 | 0.21 |
| RV% | 0.27 | 0.00 | 0.15 | 0.00 |
| CF% | 0.09 | 0.27 | 0.08 | 0.21 |
| ET% | 0.00 | 0.00 | 0.00 | 0.00 |
| PF% | 7.1 | 8.5 | 2.3 | 2.5 |

---

## D. 与当前 Table 2 tex 对比

Table 2 只展示 DR, CF, R-F1, E-F1 四列（无 ET/RV/P/R）。

| 字段 | tex 当前值 | eval 新值 | 一致? |
|------|-----------|----------|-------|
| Qwen unc DR | 0.76 | 0.76 | **YES** |
| Qwen unc CF | 0.09 | 0.09 | **YES** |
| Qwen unc R-F1 | 40.86 | 40.86 | **YES** |
| Qwen unc E-F1 | 82.15 | 82.15 | **YES** |
| Qwen con DR | 0.01 | 0.01 | **YES** |
| Qwen con CF | 0.27 | 0.27 | **YES** |
| Qwen con R-F1 | 40.56 | 40.56 | **YES** |
| Qwen con E-F1 | 81.43 | 81.43 | **YES** |
| Llama unc DR | 0.49 | 0.49 | **YES** |
| Llama unc CF | --- | 0.08 | **---**（tex 标注未计算，eval 产出 0.08）|
| Llama unc R-F1 | 43.72 | 43.72 | **YES** |
| Llama unc E-F1 | 83.93 | 83.93 | **YES** |
| Llama con DR | **0.20** | **0.21** | **NO** |
| Llama con CF | **0.26** | **0.21** | **NO** |
| Llama con R-F1 | **44.23** | **43.78** | **NO** |
| Llama con E-F1 | 83.94 | 83.94 | **YES** |

### 差异总结

Qwen 两行完全一致。Llama unconstrained 基本一致（CF 仅 tex 标 "---"，实际 0.08）。

**Llama constrained 有 3 处不一致**：
- **DR%**: tex=0.20, eval=**0.21**（差 0.01）
- **CF%**: tex=0.26, eval=**0.21**（差 0.05）
- **R-F1**: tex=**44.23**, eval=**43.78**（差 0.45 pp — 显著偏差）

R-F1=44.23 在论文其他地方出现于 beam search SciERC 结果，可能是 copy-paste 错误。

---

## E. eval 命令记录

```bash
# Qwen unconstrained
cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py \
  --input_path /root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl \
  --label qwen_unc

# Qwen constrained
cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py \
  --input_path /root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl \
  --label qwen_con

# Llama unconstrained
cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py \
  --input_path /root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_unconstrained_eval.jsonl \
  --label llama_unc

# Llama constrained
cd /root/schema_semantic_constrained_ie && python3 scripts/eval_d064.py \
  --input_path /root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl \
  --label llama_con
```

全部在 westd-16980 执行。

---

**结论**：Llama con DocRED 行需修正 3 个数字（DR 0.20→0.21, CF 0.26→0.21, R-F1 44.23→43.78）。Llama unc 的 CF 列应填入 0.08 而非 "---"。其余 12 个数字与 eval 完全一致。

---
