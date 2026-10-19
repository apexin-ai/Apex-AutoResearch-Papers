# check eval progress all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress-all_20260514T181427_result.json`
- **Structured JSON:** [`8fdd31bf48b8e60a5c47.json`](../../sessions/8f/8fdd31bf48b8e60a5c47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5个进程全部存活，argmin 的 python 子进程（PID 231426）状态是 R (running)。

## 汇总报告

| # | 实验 | 服务器 | 已完成 Tasks | 当前位置 | 已运行 | 预估剩余 | 状态 |
|---|------|--------|-------------|----------|--------|----------|------|
| 1 | eval-acr-spatial-v3 | bjb1 cuda:0 | **4/10** | task 5 进行中 | ~6h | ~9h | 正常运行 |
| 2 | eval-argmin-only-spatial | bjb1 cuda:1 | **0/10** | task 1, <5 rollouts | ~33min | ~10-15h | 正常运行 |
| 3 | eval-tiny-correction-spatial | bjb1 cuda:2 | **0/10** | task 1, rollout 5/10 | ~32min | ~5-6h | 正常运行 |
| 4 | eval-acr-object-v3 | bjb1 cuda:3 | **4/10** | task 5 进行中 | ~6h | ~9h | 正常运行 |
| 5 | eval-vla-mean-spatial | bjb2 cuda:0 | **7/10** | task 8, rollout 5/10 | ~15h | ~4-5h | 正常运行 |

### 已出结果的成功率

**eval-acr-spatial-v3** (acr_vla + CRM perdof, spatial, 10 rollouts):
- task 1: 10% (1/10), task 2-4: 0% → 前4个task平均 **2.5%**

**eval-acr-object-v3** (acr_vla + CRM perdof, object, 10 rollouts):
- task 1-4 全部 0% → 前4个task平均 **0%**

**eval-vla-mean-spatial** (vla_only mean baseline, spatial, 10 rollouts):
- 70%, 100%, 0%, 30%, 0%, 0%, 80% → 前7个task平均 **40%** (28/70)

**eval-tiny-correction-spatial** (acr_vla + max_correction_norm=0.05, spatial):
- task 1 进行中: 4/5 成功 (80%)

**eval-argmin-only-spatial** (reconvla K=10, spatial):
- 暂无结果（K=10 每步推理10次，速度慢约10x，正常）

### 关键发现

1. **vla-mean baseline (40%) 远高于 acr-vla (2.5%)**，CRM 的 correction 可能在损害性能而非改善
2. **tiny-correction (norm≤0.05) 在 task 1 表现 4/5=80%**，远优于无限制 correction 的 1/10=10%，说明大幅 correction 是有害的
3. **object benchmark 全军覆没**（acr-vla 前4个task 0%）
4. 无异常/卡住，所有实验正常推进

---
