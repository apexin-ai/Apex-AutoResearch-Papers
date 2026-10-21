# code plan 004 prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-prep_20260515T000826_result.json`
- **Structured JSON:** [`2072c7a2a4369ce68344.json`](../../sessions/20/2072c7a2a4369ce68344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan-004 downstream utility 准备完成。

### 总结

**模型**: OLMo-2-0425-1B (1485M params) 已在 `/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B/`，加载验证通过。

**数据** (`data/downstream/`):

| 变体 | 训练集 | 测试集 |
|------|--------|--------|
| depth0_only (纯人类文本) | 797 | 3138 |
| depth01 (depth ≤1) | 3,951 | 3138 |
| all (全部 depth) | 12,299 | 3138 |
| size_matched (随机采样) | 3,951 | 3138 |
| binary_filtered (NLL 阈值) | 3,951 | 3138 |

Binary baseline 的 depth 分布 `{0:678, 1:921, 2:848, 3:787, 4:717}`，模拟了不完美 binary detector 的效果。

**脚本**:
- `finetune_downstream.py` — HF Trainer CLM 微调，dry-run 验证通过 (loss=2.18)
- `run_downstream.sh` — 编排 5 variants × 3 seeds
- `prepare_downstream_data.py` / `compute_binary_baseline.py` — 数据构建

**启动训练**: `cd /root/gen-depth-fingerprint && bash run_downstream.sh 3`

---
