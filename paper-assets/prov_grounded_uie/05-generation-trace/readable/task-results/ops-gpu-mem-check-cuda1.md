# ops gpu mem check cuda1

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_mem_check_cuda1_20260512T233726_result.json`
- **Structured JSON:** [`329324c75be3db9516e0.json`](../../sessions/32/329324c75be3db9516e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这是 RTX 6000 Pro（96GB）双卡，不是之前假设的 48GB 卡。

## 结果

| 项目 | 值 |
|------|-----|
| cuda:1 总显存 | **96 GB** (97887 MiB) |
| cuda:1 当前已用 | **28 GB** (28277 MiB, PID 66475 grpo_pilot_v1b) |
| cuda:1 剩余 | **67 GB** (68976 MiB) |
| posthoc_nli_v3 预估需求 | **18-22 GB** |

**结论：完全能共存。** 剩余 67GB 远超 posthoc_nli_v3 的 ~20GB 需求，安全余量超过 45GB。可以直接在 cuda:1 上启动。

补充：cuda:0 也有 67GB 空闲（PID 40397 占用 ~30GB），两张卡都有充足空间。

---
