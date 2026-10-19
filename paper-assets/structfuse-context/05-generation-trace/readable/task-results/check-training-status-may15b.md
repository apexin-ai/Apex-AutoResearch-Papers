# check training status may15b

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-status-may15b_20260515T010612_result.json`
- **Structured JSON:** [`0111e0a7a97da1919704.json`](../../sessions/01/0111e0a7a97da1919704.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 1. Qwen random_s44 eval@1500 — **已 Early Stop，完成**

**关键数据**:

| Step | val_loss | R@1 | patience |
|------|----------|-----|----------|
| 500 | **0.4252** (best) | **0.6009** | - |
| 1000 | 0.4695 | 0.5638 | 1/2 |
| 1500 | 0.4918 | 0.5592 | 2/2 → **early stop** |
| final | 0.4943 | 0.5542 | - |

Best checkpoint at step 500: `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss`

**下一个 run 已自动启动**: Qwen **embedding_distance_s43** 在 GPU 0 运行中（PID 122645, 08:32 启动），当前 step 150，loss=0.5041。

**下一步**: 无需操作，embedding_distance_s43 已在跑。

---

## 2. StarCoder random_s43 — **训练中，接近 eval@1500**

**关键数据**:

| Step | val_loss | R@1 | patience |
|------|----------|-----|----------|
| 500 | **0.5279** (best) | 0.4708 | - |
| 1000 | 0.5430 | **0.4780** (best R@1) | 1/2 |

- 当前 step: **1300**/2810，运行 7h
- GPU 1: 100% util, 73°C, 54347/97887 MiB
- eval@1500 即将触发 — 如果 val_loss > 0.5279，将 early stop (2/2)

**下一步**: 等 eval@1500 结果，预期很快（~1h 内）。

---

## 3. M1 reextract v2 — **运行中，多 repo 并行处理**

总量 28276 instances，4 workers，已运行 ~29h。当前活跃 repo:

| Repo | 进度 | 完成度 |
|------|------|--------|
| sqlfluff/sqlfluff | 1100/1272 | 86.5% |
| conan-io/conan | 700/972 | 72.0% |
| pydicom/pydicom | 500/1315 | 38.0% |
| Project-MONAI/MONAI | 200/524 | 38.2% |

最新日志 09:07，活跃运行。此前已完成多个小 repo（feedparser, pyasn1, python-docx, deepdiff, paramiko, pygments, yamllint, graphene, bleach, freezegun, string2string 等）。

**下一步**: 无需操作，继续等待。当前 4 个大 repo 处理完后应接近尾声。

---
