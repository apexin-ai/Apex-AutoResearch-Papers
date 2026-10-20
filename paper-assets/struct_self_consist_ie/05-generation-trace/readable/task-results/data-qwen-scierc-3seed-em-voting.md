# data qwen scierc 3seed em voting

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_qwen_scierc_3seed_em_voting_20260514T211403_result.json`
- **Structured JSON:** [`b2b6948fba7cb195de2f.json`](../../sessions/b2/b2b6948fba7cb195de2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出

**服务器上**：3 个 `all_signals_report.json` 已生成
- `output/exp_001_seed42_v2/all_signals_report.json`
- `output/exp_001_seed123_v2/all_signals_report.json`
- `output/exp_001_seed456_v2_ner/all_signals_report.json`

**本地**：`artifacts/data/qwen_scierc_3seed_em_voting.json`

### EM 和 voting_conf 3-seed 汇总（full split）

| Signal | Metric | Mean±Std | CV% |
|--------|--------|----------|-----|
| **EM** | rho | 0.3293±0.0114 | 3.5% |
| **EM** | AUROC | 0.7797±0.0110 | 1.4% |
| **EM** | ECE | 0.3340±0.0018 | 0.5% |
| **voting_conf** | rho | 0.4217±0.0166 | 3.9% |
| **voting_conf** | AUROC | 0.7209±0.0115 | 1.6% |
| **voting_conf** | ECE | 0.3157±0.0039 | 1.2% |

### EM 和 voting_conf 3-seed 汇总（conditional split）

| Signal | Metric | Mean±Std | CV% |
|--------|--------|----------|-----|
| **EM** | rho | 0.4082±0.0061 | 1.5% |
| **EM** | AUROC | 0.7881±0.0086 | 1.1% |
| **EM** | ECE | 0.3065±0.0028 | 0.9% |
| **voting_conf** | rho | 0.3461±0.0069 | 2.0% |
| **voting_conf** | AUROC | 0.7013±0.0097 | 1.4% |
| **voting_conf** | ECE | 0.3120±0.0075 | 2.4% |

CV 均 <4%（full split），<2.5%（conditional split），跨 seed 稳定性良好。EM 在 AUROC 上最强（0.78-0.79），voting_conf 在 rho 上最强（0.42 full / 0.35 cond）。

---
