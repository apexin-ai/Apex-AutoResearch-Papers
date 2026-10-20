# ops pipeline diff diagnosis

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pipeline-diff-diagnosis_20260523T145132_result.json`
- **Structured JSON:** [`a2ad1a7c7e360ecf7b81.json`](../../sessions/a2/a2ad1a7c7e360ecf7b81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结构化报告：

---

## 诊断报告：ctrl_contam_llama vs ctrl_contam_pilot lz* 差异

### 1. 数据差异 — **根因**

| 维度 | ctrl_contam_llama | ctrl_contam_pilot |
|------|------------------|-------------------|
| train.jsonl 行数 | 8510 | 8510 |
| train.jsonl 大小 | 3,798,085 bytes | 3,893,393 bytes |
| **MMLU item selection seed** | **999** | **42** |
| seen_items_25pct 起始 | `[0, 9, 11, 20, 24, ...]` | `[0, 3, 10, 13, 14, ...]` |

**两个 pipeline 选择了完全不同的 3510 个 MMLU 题目作为 contam_25 污染集。**

来源追溯：
- `ctrl_contam_llama/prepare_data.py` line: `rng_contam = random.Random(999)`
- `ctrl_contam_pilot/gen_contam_25.py` line: `rng_contam = random.Random(42)`

### 2. 配置差异 — 无差异

lr=2e-4, epochs=3, batch=4, grad_accum=4, LoRA r=16/alpha=32, target=q/k/v/o_proj, dropout=0.05, max_length=512 — **完全一致**。

### 3. 模型差异 — 无差异

两边都使用 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct`，adapter_config 确认 base_model 相同。

### 4. 种子差异

| 种子类型 | llama | pilot |
|----------|-------|-------|
| Training seed | 42 | 42 |
| Data shuffle seed | 42 | 42 |
| **Item selection seed** | **999** | **42** |

### 5. Eval 差异 — 无实质差异

- `compute_lz_star` 和 `estimate_theta_mle` 实现逐行一致
- `mmlu_params.csv` 完全相同 (683,809 bytes)
- few-shot prompt 格式相同
- 差异仅在多模型路由逻辑（不影响 Llama 评估结果）

### 6. 结论

**根因：MMLU item selection seed 不同（999 vs 42），导致两个 pipeline 用了完全不同的 MMLU 污染题目子集。**

影响链：
1. 不同的 3510 个题目被注入训练 → 模型学到不同的 response pattern
2. 评估时 seen/unseen 划分也不同 → lz* 基于不同的 item subset 计算
3. 不同题目子集的 IRT 参数分布不同 → 同样的 accuracy 差异被 lz* 放大/缩小的程度不同

数值对比：
- acc_seen 很接近（0.7715 vs 0.7698），acc_unseen 也接近（0.6470 vs 0.6388）
- 但 lz* 差 64%（-2.805 vs -4.616），说明 seed=42 选出的题目子集在 IRT 参数空间中使 contamination 信号更极端

**修复方案：统一 item selection seed，使两个 pipeline 使用相同的 MMLU 污染子集后 lz* 应趋于一致。**

---
