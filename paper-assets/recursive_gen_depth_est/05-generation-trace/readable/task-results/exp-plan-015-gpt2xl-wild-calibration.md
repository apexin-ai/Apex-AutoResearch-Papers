# exp plan 015 gpt2xl wild calibration

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_015_gpt2xl_wild_calibration_20260515T223324_result.json`
- **Structured JSON:** [`44037e63c2b9d1286db0.json`](../../sessions/44/44037e63c2b9d1286db0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## GPT-2 XL Wild-Data Calibration 结果

| 指标 | Pythia RF | GPT-2 XL RF |
|------|-----------|-------------|
| CV accuracy | 0.7878 ± 0.0056 | **0.8412 ± 0.0040** |
| C4 d0 预测率 | 79.76% | **77.62%** |
| C4 d1 预测率 | 19.68% | 9.04% |
| C4 d2 预测率 | 0.34% | 3.72% |
| C4 d3 预测率 | 0.22% | 9.62% |
| WikiText d0 率 | 100% | 99.27% |
| C4 mean P(d0) | 0.80 | 0.68 |

**结论：wild-data calibration 跨 model cell 成立。** 两个 RF 都将 C4 判为 majority d0（差距仅 2.14%）。GPT-2 XL RF 分辨率更高（CV 84.1% vs 78.8%），但对 C4 的 d3 误判率偏高（9.6% vs 0.2%），说明 GPT-2 XL cell 的 d3 特征空间与 C4 某些 web text 有部分重叠。

输出文件：`gpu-6000pro-2:/root/autodl-tmp/recursive_gen_depth_est/results/plan_015_wild_data/gpt2xl_c4_calibration.json`

---
