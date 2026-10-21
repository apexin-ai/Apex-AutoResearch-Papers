# fix bjb2 28827 ghost cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-28827-ghost-cleanup_20260524T100348_result.json`
- **Structured JSON:** [`5291aec4f38399e5e383.json`](../../sessions/52/5291aec4f38399e5e383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 ghost 实验已经在 registry 中标记为 DONE/success，无需更新。

---

## 汇报

### 1. Ghost 实验状态

5 个实验在 registry 中已为 **DONE/success**，不是 ghost RUNNING 状态：

| exp_id | status | conclusion |
|--------|--------|------------|
| eval-supp-crm-norm005-spatial-s46 | DONE | success |
| eval-supp-vla-only-spatial-s45 | DONE | success |
| eval-supp-crm-norm005-spatial-s45 | DONE | success |
| eval-supp-adapt-tau025-spatial-s45 | DONE | success |
| eval-supp-vla-only-spatial-s46 | DONE | success |

/tmp/ 下对应日志文件不存在，但 registry 已正确关闭。**无需清理。**

### 2. OpenVLA

**不存在。** 6 个 GPU 全部被 s47 实验占用，无 OpenVLA 进程。无需 kill。

### 3. 6 个新部署 s47 实验状态 — 全部存活

| GPU | Session | PID | VRAM | 当前进度 |
|-----|---------|-----|------|----------|
| 0 | goal-adapt-s47 | 205107 | 4594 MiB | put_the_bowl_on_the_stove 20/20 ✓ (100%) |
| 1 | goal-crm-s47 | 199883 | 4688 MiB | put_the_bowl_on_the_stove 20/20 ✓ (100%) |
| 2 | goal-k2mean-s47 | 205380 | 5043 MiB | put_the_bowl_on_the_stove 15/15+ |
| 3 | goal-reconvla-s47 | 200418 | 4592 MiB | put_the_wine_bottle 5/5+ |
| 4 | obj-reconvla-s47 | 200690 | 5152 MiB | pick_up_cream_cheese 9/10 |
| 5 | long-k2mean-s47 | 205647 | 6268 MiB | LIVING_ROOM_SCENE2 0/10 (刚开始) |

### 4. 失败的 s47 实验

**无。** 全部 6 个实验正常运行中。

---
