# infra baseline readiness check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_baseline-readiness-check_20260519T135553_result.json`
- **Structured JSON:** [`ced7adc7d3d48534a3c3.json`](../../sessions/ce/ced7adc7d3d48534a3c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/baseline_readiness_check.md`。

**汇总：**

| Baseline | 数据 | 脚本 | 结果 | 需要操作 |
|----------|------|------|------|----------|
| **Min-K%** | ✓ | ✓ | ✓ 9/9 完成 | 无 |
| **DetectGPT** | ✓ | 部分 | 8/9（缺 pythia_nucleus） | 部署 `detectgpt_baseline.py` 补跑 1 cell |
| **Binoculars** | ✓ | 缺失 | 0/9 | 部署 `binoculars_ordinal_eval.py` + 全量运行 |

**需部署的本地 artifacts：**
1. `artifacts/detectgpt_baseline.py` — 补 pythia_nucleus 一个 cell
2. `artifacts/binoculars_baseline/binoculars_ordinal_eval.py` — 必须部署，全部 9 cell 待跑

数据完整（9 cell 全部有 depth_0–3.jsonl），磁盘 83GB 剩余充足，环境已验证可用（mink/detectgpt 已成功运行过）。

---
