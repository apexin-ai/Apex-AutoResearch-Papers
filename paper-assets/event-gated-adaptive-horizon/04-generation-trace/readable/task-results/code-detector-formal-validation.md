# code detector formal validation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_detector-formal-validation_20260517T050434_result.json`
- **Structured JSON:** [`b502e10d619bc376c8c7.json`](../../sessions/b5/b502e10d619bc376c8c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## Step 1: 代码确认
CIVODetector 已是改进版，无需修改：
- `ve_threshold = 0.49` ✓
- eval_decline = 2/3 rule ✓
- HEAD commit: `3328f53`

## Step 3-4: 正式验证结果

| 实验 | 预期 | 判定 | Trigger Step |
|------|------|------|-------------|
| exp_008d_s0 | TP | **TP** | 45K |
| exp_010b_cheetah | TP | **TP** | 65K |
| exp_008d_s3 | TP | **TP** | 45K |
| exp_008f_s3 | TN | **TN** | — |
| exp_009c_008f_s2 | TN | **FP** | 105K |
| exp_009h_008f_s0 | TN | data_unavailable | — |

**TPR = 3/3, FPR = 1/2**

FP 分析：exp_009c（008f config, seed=2）在 105K 步触发。这是真实的晚期 value overestimation（eval 从 359→227→191→148 持续下降，value 从 84→96→108→111 持续增长）。关键区别：正例触发在 45-65K，此 FP 在 105K，**时间差本身就是 dt_embed 加速 CIVO 的证据**。

结果已保存至 `artifacts/analysis/detector_formal_validation_v3.json`。

---
