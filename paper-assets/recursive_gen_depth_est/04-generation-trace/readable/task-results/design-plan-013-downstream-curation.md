# design plan 013 downstream curation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_design_plan_013_downstream_curation_20260515T212947_result.json`
- **Structured JSON:** [`75fe3992c75ef796cf52.json`](../../sessions/75/75fe3992c75ef796cf52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/plan_013_downstream_curation_design.md`。

核心设计:
- **数据**: Pythia nucleus d0–d3 各取 2500 samples，均匀混合 10k 总量
- **过滤**: 3 档 RF 过滤 (strict/moderate/soft) + 3 控制组 (oracle/random/unfiltered)，共 8 conditions
- **Finetune**: Pythia-410M LoRA (r=16)，3 epochs，5 seeds
- **评估**: WikiText-103 test PPL，paired t-test + Cohen's d
- **预算**: ~19 GPU·h，单卡约 14h 完成全部 40 runs
- **关键设计点**: RF predict_proba 用 cross-validated prediction 而非 train set 直接 predict，避免高估过滤质量

末尾已标注 `[APPROVAL NEEDED]`。

---
