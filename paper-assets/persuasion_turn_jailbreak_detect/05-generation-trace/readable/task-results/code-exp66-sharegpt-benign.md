# code exp66 sharegpt benign

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp66_sharegpt_benign_20260523T083405_result.json`
- **Structured JSON:** [`29f8ad52f610926a732c.json`](../../sessions/29/29f8ad52f610926a732c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp66 完成。结果摘要：

| N | Seed | SG FPR | IID F1 | DD F1 | AA F1 | FITD F1 |
|---|------|--------|--------|-------|-------|---------|
| 0 | 42 | **0.390** | 1.000 | 1.000 | 0.971 | 1.000 |
| 5 | 42 | 0.210 | 1.000 | 0.953 | 0.891 | 1.000 |
| 10 | 42 | 0.075 | 0.987 | 0.874 | 0.841 | 1.000 |
| 10 | 123 | 0.155 | 0.987 | 0.944 | 0.849 | 1.000 |
| 10 | 456 | 0.085 | 0.987 | 0.900 | 0.866 | 1.000 |
| 15 | 42 | 0.095 | 1.000 | 0.917 | 0.874 | 1.000 |
| 20 | 42 | 0.100 | 1.000 | 0.926 | 0.858 | 1.000 |
| 25 | 42 | **0.010** | 0.987 | 0.849 | 0.816 | 1.000 |
| 25 | 123 | **0.010** | 1.000 | 0.711 | 0.711 | 1.000 |
| 25 | 456 | 0.060 | 1.000 | 0.944 | 0.849 | 1.000 |

**关键发现**：ShareGPT FPR 从 N=0 的 0.39 降至 N=25 的 0.01-0.06，复现了 WildChat/OASST2 的 FPR 降低 pattern。注意 GRU-only 重训（固定 DeBERTa encoder）下，N=25 时 DD/AA OOD F1 有一定下降（seed 123 较明显），这是 FPR-recall tradeoff。FITD F1 保持 1.0。

脚本和数据文件：
- `scripts/prepare_sharegpt.py` — ShareGPT 数据预处理
- `scripts/exp66_sharegpt_benign_adaptation.py` — 实验脚本
- `data/sharegpt_benign_eval_200.json` / `sharegpt_benign_adapt_50.json` — 数据集
- `results/exp66_sharegpt_benign_adaptation.json` — 完整结果

---
