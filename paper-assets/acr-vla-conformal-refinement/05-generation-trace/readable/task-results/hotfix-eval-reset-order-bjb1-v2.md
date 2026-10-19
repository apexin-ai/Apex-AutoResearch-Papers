# hotfix eval reset order bjb1 v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_eval-reset-order-bjb1-v2_20260513T234224_result.json`
- **Structured JSON:** [`0fcf7f9dde65ff22f72f.json`](../../sessions/0f/0fcf7f9dde65ff22f72f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个进程活跃（运行 3.5 分钟，CPU 200%+ 说明在做 MuJoCo 初始化），无 ValueError。

**修复报告**：

| 项目 | 内容 |
|------|------|
| **修改文件** | `/root/acr-vla-conformal-refinement/src/evaluate.py` 第 201 行 |
| **修改内容** | 在 `obs = env.set_init_state(init_state)` 之前插入 `env.reset()`，顺序：reset → set_init_state → 5 步零动作 |
| **进程 PID** | eval-spatial-v6-full: **117486** (GPU0), eval-acr-spatial-v2: **117814** (GPU1), eval-reconvla-spatial-v3: **118108** (GPU2) |
| **ValueError** | 3 个日志均为 0 次，修复生效 |
| **train_crm.py** | 未受影响（tmux session `crm-train-scalar-unc` 仍在运行） |

---
