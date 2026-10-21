# code plan 003 edcr script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_edcr_script_20260515T231827_result.json`
- **Structured JSON:** [`53ccb31fbcdb7e617da1.json`](../../sessions/53/53ccb31fbcdb7e617da1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出汇总：

**脚本**: `/root/autodl-tmp/scripts/edcr_diagnostic.py` (rtx5090-4x)

**当前 diagnostic table** (18 methods, 2 collapsed):

| 方法 | Rel-F1 | Evi-F1 | EDCR | ΔF1pp |
|------|--------|--------|------|-------|
| CED-reranker (N=8) | **0.4864** | 0.8188 | 0.6156 | +7.58 |
| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | +7.86 |
| RSFT-CED s43 (best) | 0.4683 | 0.8156 | 0.6388 | +5.77 |
| RSFT-CED 3-seed mean | 0.4596±0.0128 | 0.8143±0.0051 | 0.6434±0.0115 | -- |
| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | +4.43 |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | +4.33 |
| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.00 |
| DPO 3ep | 0.3429 | **0.8403** | **0.7294** | -6.77 |
| GRPO QLoRA kl001 | 0.2108 | 0.5666 | 0.8584 | -19.98 |

**关键发现**:
- 2 个 eval 坍塌 (RSFT-flatNLI s43, DPO 1ep)，标记 ✗，需重跑
- CED-reranker 在 evidence-producing 方法中 rel_f1 最高，但 EDCR 最低（evidence 质量相对最好）
- DPO 3ep EDCR 最高（0.7294，高于 baseline），但 rel_f1 大幅下降 → evidence 过拟合
- GRPO bf16 随 step 增加 rel_f1 先降后升、EDCR 持续下降 → 可作 EDCR-F1 tradeoff curve

**增量更新**: 新 eval 完成后 `python edcr_diagnostic.py --add "方法名:eval路径"` 即可加入。

---
