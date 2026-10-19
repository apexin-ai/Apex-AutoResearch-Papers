# ops server audit bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-audit-bjb2-28827_20260516T121700_result.json`
- **Structured JSON:** [`cf3e6b66a57a94c94b68.json`](../../sessions/cf/cf3e6b66a57a94c94b68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个实验都在运行。以下是审计报告：

---

## bjb2-28827 审计报告

| exp_id | GPU | PID | tasks_done/10 | n_rollouts | 当前进度 | 状态 |
|--------|-----|-----|---------------|------------|---------|------|
| eval-argmin-object-seed45 | 5 | 221413 | 2/10 | 10 | task3 rollout 5/10 | **ALIVE** |
| eval-vla-only-object-seed45 | 4 | 221413* | 9/10 | 20 | task10 进行中 | **ALIVE** |
| eval-perdof-object-norm02-seed45 | 1 | 222830 | 1/10 | 20 | task2 进行中 | **ALIVE** |
| eval-scalar-object-seed45 | 0 | 224628 | 1/10 | 20 | task2 进行中 | **ALIVE** |
| eval-obs-only-object-default-seed45 | 3 | 242264 | 0/10 | 20 | task1 rollout 5/20 | **ALIVE** |
| eval-vla-mean-object-seed45 | 2 | 248661 | 0/10 | 10 | task1 rollout 5/10 | **ALIVE** |

*vla_only 的 python PID 与 argmin 相同数字是巧合，实际是 PID 221413（wrapper PID 221407）。

### GPU 使用

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| cuda:0 | 5201 MiB | 19% | scalar_seed45 |
| cuda:1 | 5200 MiB | 18% | perdof_norm02_seed45 |
| cuda:2 | 5628 MiB | 18% | vla_mean_seed45 |
| cuda:3 | 5664 MiB | 17% | obs_only_default_seed45 |
| cuda:4 | 1906 MiB | 18% | vla_only_seed45 (K=1, 轻量) |
| cuda:5 | 4700 MiB | 18% | argmin_seed45 |

**空闲 GPU：无（6 卡全部占用）**

### 关键发现

1. **所有 6 个实验均存活**，无死亡进程。之前 harvest Worker 报告的 "4 new JSONs" 来自其他实验（非 seed45）。
2. **vla_only 即将完成**（9/10 tasks done），预计 ~1-2h 内产出 JSON。
3. **启动参数差异**：argmin 和 vla_mean 用 n_rollouts=10，其余 4 个用默认 n_rollouts=20（运行时间翻倍）。
4. **vla_only 用 K=1**（非 K=10），与其他实验不一致。
5. **无 JSON 输出文件**：目前 0/6 实验完成。
6. **预计完成时间**：
   - vla_only：最快（~1-2h）
   - argmin：中等（n_rollouts=10，当前 task3，~3-4h）
   - vla_mean：较慢（n_rollouts=10，刚开始，~5-6h）
   - perdof/scalar/obs_only：最慢（n_rollouts=20，~8-12h）

### vla_only 部分结果（9/10 tasks）

| task | success/total | SR |
|------|---------------|-----|
| alphabet_soup | 0/20 | 0% |
| cream_cheese | 1/20 | 5% |
| salad_dressing | 5/20 | 25% |
| bbq_sauce | 4/20 | 20% |
| ketchup | 0/20 | 0% |
| tomato_sauce | 0/20 | 0% |
| butter | 1/20 | 5% |
| milk | 3/20 | 15% |
| chocolate_pudding | 3/20 | 15% |

累计：17/180 = 9.4% SR（待 task10 完成后更新）

---
