# ops diagnose t15 a045 s42 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-t15-a045-s42-d102_20260523T044937_result.json`
- **Structured JSON:** [`c3405938450558974510.json`](../../sessions/c3/c3405938450558974510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## scale_14b_t15_a045_s42_fp32 — DONE ✓

**训练**: 成功完成，16 代 (gen_0–gen_15)，all_metrics.json 存在，clean exit。

**D102 指标**:

| 方法 | Forward | Reverse |
|------|---------|---------|
| PermG FDR | **3/8** | 0/8 |
| Diff xcorr FDR | 6/8 | 6/8 |
| Threshold onset | 2/8 | — |
| TY Granger | 6/8 | — |
| **K≥3 robust pairs** | **4/8** | — |

**末代指标**: ppl=34.16, mauve=0.0252

**与 410M 对比** (T=15 α=0.45):
- 410M: PermG **6/8** → 1.4B: PermG **3/8**
- 1.4B 信号明显更弱。PermG 从 6/8 降到 3/8，K≥3 为 4/8（主要由 ece→distinct pairs 贡献）。mauve pairs 全部未通过检测。
- 这与 T=10 观察到的 scale attenuation 趋势一致：更大模型对低-中 α 的 canary 信号更有抵抗力。

---
