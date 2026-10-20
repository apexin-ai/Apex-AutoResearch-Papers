# fix 34685 maxsteps correction

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685-maxsteps-correction_20260527T213720_result.json`
- **Structured JSON:** [`d687b8f33692ed47d7e5.json`](../../sessions/d6/d687b8f33692ed47d7e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张 GPU 满载运行。

```
detach_ln_v2_s2:
  旧进程 killed: kill -9 + 确认 0 残留进程
  新 max_steps: 35005
  tqdm 显示: 10/35005 ✅
  当前 step: 10
  训练中: 是

vanilla_object_s0:
  旧进程 killed: kill -9 + 确认 0 残留进程
  新 max_steps: 40005
  tqdm 显示: 7/40005 ✅
  当前 step: 7
  训练中: 是

cuda:2/3 未受影响: ✅ (full_occ_ln_v2_s3 + detach_ln_v2_s3 持续运行，GPU 利用率 95-99%)
```

---
