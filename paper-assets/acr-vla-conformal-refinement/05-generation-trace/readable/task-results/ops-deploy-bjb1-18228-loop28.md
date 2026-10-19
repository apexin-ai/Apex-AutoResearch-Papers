# ops deploy bjb1 18228 loop28

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb1-18228-loop28_20260526T101530_result.json`
- **Structured JSON:** [`6bd407a9a4d77c16ec35.json`](../../sessions/6b/6bd407a9a4d77c16ec35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现重大冲突，停止部署。

**环境实际状态（与任务描述不符）：**

GPU 占用情况（3 个忙，1 个空闲）：
- **GPU 0** (PID 2558, 已跑 6h31m)：`pi05 crm_obs_only long seed=42` ← **与待部署实验 3 完全重复**
- **GPU 1** (PID 2916, 已跑 6h30m)：`pi05 crm_obs_only long seed=43`
- **GPU 2**：真正空闲（1 MiB）
- **GPU 3** (PID 3764, 已跑 6h28m)：`pi05 adaptive_conformal_crm long seed=42`（不是任务说的 adaptive-goal-s43）

**Git 状态：** HEAD = `a594db5 Add 3 CRM loss variants` ✓

**关键问题：**
1. 任务描述说 cuda:0/1/2 空闲，实际只有 cuda:2 空闲，没有 tmux session 但有 3 个 python 进程直接在跑（已 6h+）
2. **实验 3 (CRM Long s42) 已在 GPU 0 跑了 6h31m**，重复部署会浪费资源
3. 进程实际跑的是 `src/evaluate.py`（不是 `evaluate.py`），路径可能不同
4. 实际在跑的是 long suite 的扫描，不是任务描述的 goal/object suite

**建议方案（请确认）：**

只有 1 个 GPU (cuda:2) 可用，3 个待部署实验中：
- 实验 3 (CRM Long s42) 已完成 6h+，应**取消部署**（避免重复）
- 实验 1 (Adaptive Goal s44) 或 实验 2 (Adaptive Object s43)：择一部署到 cuda:2

另外需先确认正确入口是 `evaluate.py` 还是 `src/evaluate.py`，以及命令参数 `--n_rollouts_per_task` vs 在跑进程用的 `--n_rollouts`。

请指示：
- A) 取消实验 3，部署实验 1 (Adaptive Goal s44) 到 cuda:2
- B) 取消实验 3，部署实验 2 (Adaptive Object s43) 到 cuda:2
- C) 等待现有 3 个进程完成后再部署
- D) 其他

---
