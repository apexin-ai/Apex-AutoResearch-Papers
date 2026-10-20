# ops check gpu quick

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-quick_20260522T143552_result.json`
- **Structured JSON:** [`17b86ee5bba745868007.json`](../../sessions/17/17b86ee5bba745868007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. GPU 占用**
4× NVIDIA RTX PRO 6000 Blackwell (98GB)，全部空闲。GPU 1 Util 100% 但显存 0MiB 且无进程——可能是残留状态，无训练在跑。

**2. Multi-seed checkpoints/results 状态**

| 条件 | Checkpoint | Results |
|------|-----------|---------|
| contam_15_s2 | ✅ | ✅ `contam_15_s2_results.json` |
| contam_25_s2 | ✅ | ✅ `contam_25_s2_results.json` |
| contam_25_s3 | ✅ (训练完成) | ❌ 尚未评估 |
| contam_50_s2 | ❌ | ❌ |
| contam_50_s3 | ❌ | ❌ |

**3. 当前卡在哪一步**
- `contam_25_s3` 训练已完成（checkpoint 存在），但评估（生成 results JSON）还没跑。
- `contam_50_s2` 和 `contam_50_s3` 训练和评估都还没开始。
- 当前无任何进程在运行，GPU 空闲。

---
