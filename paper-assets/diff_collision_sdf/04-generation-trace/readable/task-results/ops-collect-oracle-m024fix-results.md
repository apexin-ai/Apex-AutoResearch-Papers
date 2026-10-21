# ops collect oracle m024fix results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_oracle_m024fix_results_20260522T183426_result.json`
- **Structured JSON:** [`771f8c5a65e8d61d7383.json`](../../sessions/77/771f8c5a65e8d61d7383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果：

## Oracle A3 M024fix 结果 (force_refine, 40 episodes/task)

| Task | CAR (M024fix) | CAR (Buggy) | Δ | avg_max_disp |
|------|:---:|:---:|:---:|:---:|
| task0 pick_orange_juice | **97.5%** | 95.0% | +2.5 | 0.0028m |
| task1 put_wine_on_rack | **65.0%** | 57.5% | +7.5 | 0.0381m |
| task2 put_cream_in_area | **97.5%** | 92.5% | +5.0 | 0.0000m |
| task3 pick_bbq_sauce | **82.5%** | 80.0% | +2.5 | 0.0134m |
| **Overall** | **85.6%** | 81.2% | **+4.4** | — |

- **TSR = 0%**（所有 task），force_refine 每步都 refine（refine_count=300/episode），完全牺牲了 task completion
- **CAR = 85.6% > LoRA baseline 82%** → conclusion = **success**
- M024 坐标修复后，所有 task 的 CAR 均有提升，验证了 delta→absolute 修复的有效性

## A1 Rerun 状态

**已自动启动**，PID 931014，GPU 3，tmux session `eval_a1_obj_rerun`，02:30 启动（oracle 完成后立即触发）。

## 服务器当前负载（4 GPU 全部在用）

| GPU | 任务 | PID |
|-----|------|-----|
| cuda:0 | A1 lora spatial eval (a1_lora_v11) | 727358 |
| cuda:1 | Baseline fullft spatial eval (baseline_fullft_v11) | 697980 |
| cuda:2 | A3 m024fix object eval 200ep (a3_m024fix_v11) | 780772 |
| cuda:3 | A1 object rerun (a1_rerun_v11) | 931014 |

---
