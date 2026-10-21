# check pi05 eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-eval-progress_20260522T020935_result.json`
- **Structured JSON:** [`904a2c31a0c9947f1341.json`](../../sessions/90/904a2c31a0c9947f1341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 evals are **running**, on task 1/10. Progress is early (~5%).

## 状态汇总

### bjb1-32546 — Object (π0.5 CRM)

| Seed | 当前 Task (1/10) | Rollout 进度 | Task 1 成功率 |
|------|-----------------|-------------|--------------|
| 42 | pick_up_alphabet_soup... | 10/20 | 10/10 (100%) |
| 43 | pick_up_alphabet_soup... | 10/20 | 10/10 (100%) |
| 44 | pick_up_alphabet_soup... | 10/20 | 9/10 (90%) |

进程运行时间 ~1h05m，RSS ~3.5MB（wrapper进程）。

### bjb2-28827 — Spatial (π0.5 CRM)

| Seed | 当前 Task (1/10) | Rollout 进度 | Task 1 成功率 |
|------|-----------------|-------------|--------------|
| 42 | pick_up_black_bowl... | 10/20 | 8/10 (80%) |
| 43 | pick_up_black_bowl... | 10/20 | 8/10 (80%) |
| 44 | pick_up_black_bowl... | 10/20 | 9/10 (90%) |

进程运行时间 ~53min，RSS ~3.5MB（wrapper进程）。

### 进度估算

- 每个 eval: 10 tasks × 20 rollouts = 200 rollouts total
- 当前：~10/200 (**5%**)，已耗时 ~1h
- 预计剩余：**~19h**（若线性外推，但后续 task 可能更快/更慢）
- 配置：K=10, conformal_threshold=0.074855, max_steps=300

### 异常

无异常。所有 6 个进程正常运行，无 OOM/crash。日志中的 WARNING 是正常的 vision tower key 警告。

---
