# Investigation: CRM Object Eval on bjb2-28827

**Date**: 2026-05-23 11:30 CST  
**Server**: bjb2-28827 (6x RTX 4090)

## 1. CRM Object Eval x3: ALL COMPLETED SUCCESSFULLY

进程没有消失/崩溃——它们**正常完成**后退出。结果文件已写入：

| Seed | Overall Success Rate | File | Completed At (CST) |
|------|---------------------|------|-------------------|
| 42 | **50.5%** (101/200) | `logs/eval_object_crm_obs_only_seed42.json` | 10:30 |
| 43 | **53.5%** (107/200) | `logs/eval_object_crm_obs_only_seed43.json` | 10:28 |
| 44 | **51.5%** (103/200) | `logs/eval_object_crm_obs_only_seed44.json` | 10:29 |
| **Mean** | **51.83% +/- 1.53%** | | |

### Per-task breakdown (seed42 / seed43 / seed44):
| Task | s42 | s43 | s44 |
|------|-----|-----|-----|
| alphabet_soup | 70% | 70% | 70% |
| cream_cheese | 50% | 50% | 70% |
| salad_dressing | 50% | 50% | 45% |
| bbq_sauce | 30% | 35% | 35% |
| ketchup | 40% | 35% | 35% |
| tomato_sauce | 45% | 50% | 45% |
| butter | 40% | 65% | 45% |
| milk | 45% | 45% | 40% |
| chocolate_pudding | 70% | 75% | 75% |
| orange_juice | 65% | 60% | 55% |

Checkpoint: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`  
Parameters: K=10, obs_dim=960, n_action_steps=50, max_steps=280  
Original tmux session `eval-crm-object-s42` bash process (PID 366358) is zombie; python exited normally.

## 2. GPU Status

| GPU | PID | Mode | Benchmark | Seed | VRAM | Status |
|-----|-----|------|-----------|------|------|--------|
| 0 | 491158 | adaptive_conformal_crm | object | 42 | 5617MiB | RUNNING (started 11:25) |
| 1 | 491422 | reconvla | object | 42 | 5692MiB | RUNNING (started 11:25) |
| 2 | 491627 | crm_obs_only (norm=0.05) | **goal** | 42 | 5608MiB | RUNNING (started 11:25) |
| 3 | 455214 | vla_only | object | 42 | 2841MiB | RUNNING (started 09:58) |
| 4 | 455415 | vla_only | object | 43 | 3308MiB | RUNNING (started 09:58) |
| 5 | 455618 | vla_only | object | 44 | 3308MiB | RUNNING (started 09:58) |

**Free GPUs: NONE. All 6 cards occupied.**

## 3. VLA-only Object Eval Progress (GPUs 3-5)

Running 1.5h, ~60% complete (6/10 tasks). ETA: 12:30-13:00 CST.

Current progress per seed:
- **seed42**: 6/10 tasks done (alphabet_soup=85%, cream_cheese=75%, salad_dressing=85%, bbq_sauce=85%, ketchup=90%, tomato_sauce=75%)
- **seed43**: 5/10 tasks done + task 6 in progress (alphabet_soup=70%, cream_cheese=70%, salad_dressing=75%, bbq_sauce=85%, ketchup=80%)
- **seed44**: 5/10 tasks done + task 6 in progress (alphabet_soup=70%, cream_cheese=70%, salad_dressing=75%, bbq_sauce=90%, ketchup=90%)

VLA-only success rate significantly higher than CRM obs-only (estimated ~80% vs 51.8%).

## 4. New Experiments (GPUs 0-2, started 11:25)

| Tmux Session | GPU | Mode | Benchmark | Notes |
|-------------|-----|------|-----------|-------|
| obj_adapt | 0 | adaptive_conformal_crm | object | tau=0.074855 |
| obj_reconvla | 1 | reconvla | object | K=10 |
| goal_crm005 | 2 | crm_obs_only | goal | norm=0.05, task1 5/20 rollouts done |

## 5. Recommendations

1. **No need to rerun CRM Object eval** -- all 3 seeds completed successfully
2. Wait for VLA-only object eval to finish (~1-1.5h), then compare VLA-only vs CRM obs-only
3. GPUs 0-2 new experiments just started, running normally
4. Clean up zombie tmux session `eval-crm-object-s42` (PID 366358)
