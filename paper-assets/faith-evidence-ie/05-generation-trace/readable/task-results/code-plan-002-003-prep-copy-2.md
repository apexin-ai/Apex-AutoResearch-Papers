# code plan 002 003 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_002_003_prep_20260515T195530_result.json`
- **Structured JSON:** [`d20cf7086a2c15b9e9e5.json`](../../sessions/d2/d20cf7086a2c15b9e9e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### Plan 002: Test Set Eval — 脚本就绪

**脚本**: `/root/autodl-tmp/freige/scripts/eval_test_set.sh`

```bash
# 用法
bash scripts/eval_test_set.sh /root/autodl-tmp/rsft_output_s43 test_rsft_s43
```

**关键发现**:
- 之前 `plan_002_test_eval_s44` 失败的原因：用了 `inference.py --split test`，DocRED test set **没有 gold labels**，所有指标返回 0
- 正确做法：用 `test_inference.py`，只生成 predictions + `codalab_submission.json`，需手动提交 CodaLab 评测
- 脚本已参数化（adapter_path, output_name, gpu_id, batch_size），支持 `--no-quantize`

**Best config 待定**（当前 dev set 排名）:

| Method | rel_f1 |
|--------|--------|
| RSFT-CED s43 | **0.4683** |
| RSFT-CED s44 | 0.4655 |
| RSFT-flatNLI s42 | 0.4539 |
| RSFT-flatNLI s43 | RUNNING |

等 `plan_001_flat_nli_seed43` 完成后确定最终 best。

### Plan 003: EDCR Pipeline — 代码就绪

**脚本**: `bash scripts/compute_edcr_table.sh`  
**代码**: `cross_method_table.py` 已更新，覆盖 11 个方法。

**代码状态**: 完全就绪，EDCR 已集成在 `evaluator.py` 的 `compute_edcr()` 中，所有 dev eval 已有 predictions + metrics。

**缺失项**:
- DPO-CED metrics.json 不在预期路径（`plan_012_dpo_ced` 结论 negative，rel_f1=0.3429，可能没保存到 eval_results）
- 部分旧 eval 缺少 `evi_f1_joint` 字段（`rsft_r1`, `rsft_s44` 等），如需要可重跑 evaluator
- 等 `plan_001_flat_nli_seed43` 完成后，需跑一次 dev eval 再更新表格

---
