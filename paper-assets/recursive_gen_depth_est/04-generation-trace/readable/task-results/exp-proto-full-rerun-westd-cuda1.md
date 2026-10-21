# exp proto full rerun westd cuda1

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_proto_full_rerun_westd_cuda1_20260517T182509_result.json`
- **Structured JSON:** [`1244558bee7f697625a8.json`](../../sessions/12/1244558bee7f697625a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验全部完成。汇总结果：

## Prototypical Network Full Run 结果

| Holdout | Accuracy | MAE | Mean Pairwise AUC |
|---------|----------|------|-------------------|
| gpt2xl  | 68.35%   | 0.364 | 0.8926           |
| pythia  | 61.55%   | 0.454 | 0.8415           |
| olmo    | 70.01%   | 0.335 | 0.9004           |
| **Mean** | **66.64%** | **0.384** | **0.874**     |

- NaN fix 有效，3 个 holdout 均正常完成，无 NaN
- 与 RF baseline（66.4%）基本持平（66.6%），假设验证通过
- 实验已注册为 `learned_estimator_proto_fix_001`，状态 DONE/success
- 结果文件在 `westd-48862:/root/autodl-tmp/recursive_gen_depth_est/results/learned_estimator/prototypical_{gpt2xl,pythia,olmo}.json`

---
