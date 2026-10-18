# analyze eval pi05 random k075 long strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k075_long_strict_20260527T084042_result.json`
- **Structured JSON:** [`7039daedf0c838bf3adf.json`](../../sessions/70/7039daedf0c838bf3adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**eval_pi05_random_k075_long_seed42_strict — SR = 63.0%**

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato | 84% |
| T1 cream cheese + butter | 72% |
| T2 stove + moka pot | 78% |
| T3 black bowl → drawer | 74% |
| T4 white mug + plate | 64% |
| T5 book → back | 48% |
| T6 white mug + plate (v2) | 62% |
| T7 alphabet soup + cream | 54% |
| T8 both moka pots → stove | 12% |
| T9 yellow mug → microwave | 82% |

尽管 EXIT_CODE=143 出现在前次 retry，第二次运行实际 EXIT_CODE=0，全部 500 episodes 完成。

**westd-41074 GPU 状态：**
- GPU 0, 1: 空闲 (0%, 1 MiB)
- GPU 2, 3: 占用中 (~30%, ~11 GB)

---
