# analysis w3 exp001 record gap

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w3_exp001_record_gap_20260521T203950_result.json`
- **Structured JSON:** [`e2087426e54f1ab43fcb.json`](../../sessions/e2/e2087426e54f1ab43fcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### Facet Levels（均符合设计）
| Facet | Levels | Values |
|-------|--------|--------|
| precision | 3 | bfloat16, float16, float32 |
| temperature | 3 | 0.0, 0.3, 0.7 |
| prompt_template | 6 | 1–6 |
| seed | 6 | 42, 123, 456, 789, 1024, 2048 |
| ordering | 4 | 1–4 |

### 理论 vs 实际
- 理论：3×3×6×6×4 = **1,296 conditions** (259,200 records)
- 实际：**1,196 conditions** (239,200 records)
- 缺失：**100 conditions** (20,000 records)

### 缺失模式
**所有 100 个缺失条件都是 `float32 × temperature=0.0`**，其他 precision×temperature 组合完整无缺。

细分：
- **prompts 1–4**：在 float32×temp=0.0 下**全部缺失**（4 prompts × 6 seeds × 4 orderings = 96 条件）
- **prompt 5**：仅 seed=42 缺失（4 orderings = 4 条件）
- **prompt 6**：完整

### 原因推断
float32 占用 2 倍显存（相比 bf16/fp16），temp=0.0 批次很可能触发了 **OOM 或 GPU 崩溃**。从缺失分布看，batch 按 prompt_template 顺序执行：prompts 1–4 全部丢失，prompt 5 在 seed=42 处中断，之后恢复，prompt 6 正常完成。

### 补救
只需补跑 100 个缺失条件：`float32 × temp=0.0 × (prompts 1–4 全部 + prompt 5 seed=42) × 全部 orderings`。

### 报告路径
`/root/nlp_variance_gtheory/results/exp001_analysis/w3_record_gap_analysis.json`

---
