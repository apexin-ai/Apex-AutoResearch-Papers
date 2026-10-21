# scan harvest bjb1 32546 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan-harvest_bjb1-32546-status_20260523T171954_result.json`
- **Structured JSON:** [`3580511f7f023c76881f.json`](../../sessions/35/3580511f7f023c76881f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| GPU | exp_id | 状态 | 进度 | SR |
|-----|--------|------|------|-----|
| cuda:0 | eval-supp-goal-vla-only-wrapper-s44-r2 | **已完成** ✓ | 10/10 tasks | **85.0%** (170/200) |
| cuda:1 | eval-supp-long-adapt-tau025-s43 | 运行中 | ~task 8/10 (STUDY_SCENE1) | - |
| cuda:2 | eval-supp-long-crm-norm005-s43 | 运行中 | ~task 8/10 (STUDY_SCENE1) | - |
| cuda:3 | eval-supp-long-reconvla-s43 | 运行中 | ~task 8/10 (LIVING_ROOM_SCENE6) | - |
| cuda:4 | eval-supp-long-k2mean-s43 | 运行中 | ~task 8/10 (STUDY_SCENE1) | - |
| cuda:5 | eval-supp-long-vla-only-s44 | 运行中 | ~task 8/10 (LIVING_ROOM_SCENE6) | - |

- **cuda:0 空闲可部署**，已更新 registry 为 DONE（SR=85.0%）
- 其余 5 个实验都在正常运行（GPU util 20-35%，~3GB VRAM），预计还需 ~1-2h 完成

---
