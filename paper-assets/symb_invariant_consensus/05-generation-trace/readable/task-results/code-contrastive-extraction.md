# code contrastive extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_contrastive-extraction_20260518T140457_result.json`
- **Structured JSON:** [`b2834367631fd39db016.json`](../../sessions/b2/b2834367631fd39db016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. 24/24 extractions succeeded, 0 parse failures.

---

## 产出报告

### 1. 修改的文件

| 文件 | 变更 |
|------|------|
| `sica/constraint_extractor.py` | 新增 `CONTRASTIVE_EXTRACTION_PROMPT`、`ContrastiveConstraintExtractor` 类 |
| `sica/pipeline.py` | 新增 `ContrastiveScorer`、`ContrastiveSICAPipeline` 类 |
| `run_contrastive_folio.py` | 新建，contrastive 实验入口 |
| `scripts/run_contrastive_folio.sh` | 新建，shell 运行脚本 |

### 2. Contrastive Extraction Prompt 核心设计

Prompt 要求 LLM 对**每个候选答案**提取 supporting 和 opposing 约束：
- `stance`: "supporting" / "opposing"
- `target`: 约束针对的候选答案 (True/False/Unknown)
- `z3_formula`: Z3 布尔公式

关键指令：**"Focus on DISCRIMINATIVE constraints: ones where the logical content genuinely differentiates between candidate answers."**

### 3. Aggregation 权重处理

- MaxSAT 层：所有约束以频率权重正常求解（找最大可满足子集）
- 评分层：对每个 satisfied 约束，按 stance 标签计分
  - `supporting` → `scores[target] += weight`
  - `opposing` → `scores[target] -= alpha * weight`
- `alpha` 默认 1.0，可通过 `--scorer-alpha` 调整

### 4. 运行脚本

```bash
# 完整运行（需 vLLM + Qwen2.5-14B）
bash scripts/run_contrastive_folio.sh

# 仅测试几个例子
python run_contrastive_folio.py \
    --traces-dir results/folio_204_14b/intermediates \
    --mode vllm --dry-run 5
```

### 5. Dry-run 结果（2 examples, real vLLM）

| 问题 | GT | Contrastive | SC | 
|------|----|-------------|-----|
| folio_0 | Unknown | **Unknown (V)** | True (X) |
| folio_1 | True | True (V) | True (V) |

- Contrastive: **2/2 (100%)**, SC: 1/2 (50%)
- 提取成功率 24/24，平均每题 ~20s
- folio_0 的 stance 分布：supporting=9, opposing=16。opposing 约束成功惩罚了 True (-4.0) 和 False (-2.0)，Unknown 保持 0.0 胜出

---
