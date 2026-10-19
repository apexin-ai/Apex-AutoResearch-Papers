# deploy bjb2 28827 cuda0 backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-cuda0-backfill_20260528T113020_result.json`
- **Structured JSON:** [`030c63bc42973007d9e7.json`](../../sessions/03/030c63bc42973007d9e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 汇总

**新实验已部署：**
- `eval-supp-obj-adapt-tau025-s43` → bjb2-28827 cuda:0，已启动并注册 RUNNING

**bjb2-28827 其他 3 个实验均仍在运行中（long-horizon benchmark）：**

| 实验 | GPU | 进度 | 当前可见 task SR |
|------|-----|------|-----------------|
| eval-supp-long-adapt-tau025-s47-r2 | cuda:1 | ~task 8/10 (LIVING_ROOM_SCENE1) | SCENE6=25%, STUDY1=90%, KITCHEN4=85%, KITCHEN3=100%, SCENE5=45%, SCENE2=75% |
| eval-supp-long-k2mean-s46 | cuda:4 | ~task 7/10 (LIVING_ROOM_SCENE6 done) | SCENE6=35%, STUDY1=85%, KITCHEN4=90%, KITCHEN3=100%, SCENE5=25%, SCENE2=70% |
| eval-supp-long-reconvla-s46 | cuda:5 | ~task 8/10 (LIVING_ROOM_SCENE1) | SCENE6=25%, STUDY1=90%, KITCHEN4=95%, KITCHEN3=95%, SCENE5=25%, SCENE2=75% |

三个 long 实验预计还需 1-2 小时完成，无 OOM 或异常。

---
