# fix eval bug bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-bug-bjb1_20260513T225755_result.json`
- **Structured JSON:** [`04c1b1c4ba0691fef1d0.json`](../../sessions/04/04c1b1c4ba0691fef1d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 执行摘要

**Step 1 - 清理残留进程**: Kill 了 4 个残留 evaluate.py 进程 (PID 73766, 100448, 102318, 104836) 和 2 个 tmux session。

**Step 2 - 修复 evaluate.py** (`rollout_single` L201-203):
- 删除了 `env.reset()`（覆盖 demo init_state 的 bug）
- 替换为 5 步零动作物理稳定: `obs, _, _, _ = env.step(np.zeros(7))`
- 额外修复: `10_nvidia.json` 是空文件导致 EGL 初始化失败，已写入正确的 vendor ICD 配置

**Step 3 - Sanity check 通过**:
- BUG CONFIRMED: `env.reset()` 使 eef_pos 偏移 0.0152（y 轴从 -0.015 归零）
- 修复后零动作稳定 drift 仅 0.004，PASSED

**Step 4 - 3 个 eval 已提交**:

| exp_id | GPU | PID | mode |
|--------|-----|-----|------|
| eval-spatial-v6-full | cuda:0 | 109802 | vla_only |
| eval-acr-spatial-v2 | cuda:1 | 110073 | acr_vla |
| eval-reconvla-spatial-v3 | cuda:2 | 110280 | reconvla |

---
