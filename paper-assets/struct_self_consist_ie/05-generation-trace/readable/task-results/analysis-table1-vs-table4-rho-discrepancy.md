# analysis table1 vs table4 rho discrepancy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1_vs_table4_rho_discrepancy_20260515T235236_result.json`
- **Structured JSON:** [`24bb289ba2eafe0eadde.json`](../../sessions/24/24bb289ba2eafe0eadde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the smoking gun. The two inference runs use **different model checkpoints**:
- mvp_pilot (Table 4): `qwen3-8b-scierc-merged`, max_model_len=2048
- exp_012_rerun_1024 (Table 1): `qwen3-8b-scierc-merged-v2`, max_model_len=4096

## 调查结论

### Table 1 SciERC 8B ρ 来源
- **实验**: `exp_012_rerun_1024` (May 15 06:17)
- **文件**: `output/exp_012_rerun_1024/samples.jsonl` → `output/analysis_unified_rho_full.json` (qwen_scierc_n8_seed42)
- **模型**: `checkpoints/qwen3-8b-scierc-merged-v2`
- **推理参数**: max_model_len=4096, max_tokens=1024
- **Instance filtering**: gold-empty excluded → n=529
- **值**: SJ=0.3599→.360, FK=0.2665→.267

### Table 4 SciERC 8B ρ 来源
- **实验**: `mvp_pilot_004` (May 14 17:02)
- **文件**: `output/mvp_pilot_004/report.json`
- **模型**: `checkpoints/qwen3-8b-scierc-merged` (v1, 非 v2)
- **推理参数**: max_model_len=2048, max_tokens 可能为 512
- **Instance filtering**: gold-empty excluded → n=529
- **值**: SJ=0.3825→.383, FK=0.2590→.259

### 差异根因

**不同模型 checkpoint + 不同推理设置。** Table 4 caption 声称 "8B recomputed under matched conditions"，但实际上 SciERC 8B 的数值直接沿用了最早的 mvp_pilot_004 报告（使用 `qwen3-8b-scierc-merged` v1 模型），没有用当前的标准 checkpoint（`-v2`）重新推理。

具体差异链：
1. **模型不同**: v1 vs v2 merged checkpoint → 不同的预测输出（greedy F1: 0.667 vs 0.663）
2. **推理设置不同**: max_model_len 2048 vs 4096, 可能还有 max_tokens 512 vs 1024
3. **samples 不同** → consistency scores 不同 → Spearman ρ 不同

CoNLL 8B 数值在两表中一致（SJ=.436, FK=.400），因为 `analyze_scale_ablation_4b.py` 正确引用了 `exp002_conll2003/samples.jsonl`（该实验从一开始就用正确参数生成）。

### 建议修复

**方案 A (推荐): 统一 Table 4 SciERC 8B 值为 Table 1 的值。**
```
SciERC NER & SJ & .360 & .422 & +.062 \\
           & FK & .267 & .326 & +.059 \\
SciERC RE  & SJ & .250 & .267 & +.017 \\
           & FK & .275 & .359 & +.084 \\
```

Table 4 caption 中 "8B recomputed under matched conditions" 修改为 "same 8B inference as Table 1" 或直接删除该说明。

**方案 B: 用 v2 模型对 4B 也重新推理，确保真正 matched conditions。** 这更彻底但工作量大。

---
