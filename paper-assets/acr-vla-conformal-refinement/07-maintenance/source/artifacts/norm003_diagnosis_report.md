# norm003 Eval 诊断报告

**日期**: 2026-05-19 ~21:00 UTC

---

## 1. seed47 进程状态 (bjb1-32546 GPU 3)

| 项目 | 值 |
|------|-----|
| 状态 | **ALIVE** |
| 实际 PID | 894900 (python 主进程) |
| GPU 占用 | GPU 3, 3389 MiB, 31% util |
| 进度 | **5/10 tasks 完成** |
| 已完成结果 | T1=0%, T2=0%, T3=20%, T4=30%, T5=0% (5/50 successes) |
| JSON 文件 | 尚未生成（进程仍在运行） |
| Registry | status 已恢复为 RUNNING；conclusion=failed 为误标（cron 检测到被 kill 的旧进程 PID 892663 的 EXIT_CODE=129） |

## 2. seed48 进程状态 (bjb1-18228 GPU 1)

| 项目 | 值 |
|------|-----|
| 状态 | **ALIVE** |
| 实际 PID | 67825 (python 主进程) |
| GPU 占用 | GPU 1, 3389 MiB, 37% util |
| 进度 | **5/10 tasks 完成 + T6 进行中 (rollout 5/10)** |
| 已完成结果 | T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6=1/5 so far (6/50 + ongoing) |
| JSON 文件 | 尚未生成（进程仍在运行） |
| Registry | status=RUNNING；conclusion=failed 为误标（同上），无法设 null |

## 3. seed44-bjb2 失败诊断 (bjb2-28827)

| 项目 | 值 |
|------|-----|
| 实际状态 | **已成功完成** |
| Overall SR | **17% (17/100)** |
| JSON 路径 | `/root/logs/eval_object_obs_only_norm003_seed44.json` |
| 完成度 | 10/10 tasks × 10 rollouts，全部完成 |
| Wall clock | ~15.6h (56135s) |
| 误标原因 | startup recovery 扫描时发现实验处于 RUNNING 状态，但无 cron 监控和 PID 信息，自动标记为 failed |

**seed44-bjb2 per-task 结果**:

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 0% | 0/10 |
| salad_dressing | 20% | 2/10 |
| bbq_sauce | 40% | 4/10 |
| ketchup | 10% | 1/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 0% | 0/10 |
| milk | 30% | 3/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

**注意**: JSON 输出路径为 `/root/logs/` 而非 `/root/acr-vla-conformal-refinement/logs/`，可能是提交时工作目录不同导致。

## 4. Registry 操作记录

| 实验 | 操作 |
|------|------|
| eval-obs-only-object-norm003-seed44-bjb2 | conclusion: failed → **success**; 添加 notes |
| eval-obs-only-object-norm003-seed47-r2 | status: PREPARING → **RUNNING**; 添加 notes (conclusion=failed 无法清除) |
| eval-obs-only-object-norm003-seed48 | 添加 notes (status 已是 RUNNING, conclusion=failed 无法清除) |

## 5. 汇总

- seed47、seed48 **进程正常运行中**，约 3.5h 完成了 5/10 tasks，预计还需 ~3.5h 完成
- seed44-bjb2 **已成功完成**（SR=17%，与 seed42=16% 一致），被误标 failed
- ε=0.03 obs_only 现有数据点：seed42=16%, seed44=17%（n=2），seed47/seed48 预计 ~3.5h 后出结果补至 n=4
