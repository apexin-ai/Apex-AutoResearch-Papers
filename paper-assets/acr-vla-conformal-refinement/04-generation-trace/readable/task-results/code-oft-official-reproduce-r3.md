# code oft official reproduce r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oft-official-reproduce-r3_20260522T104014_result.json`
- **Structured JSON:** [`e28db11bcda6af4172b4.json`](../../sessions/e2/e28db11bcda6af4172b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态汇报

环境搭建完成，eval 已启动：

| 项目 | 状态 |
|------|------|
| **Conda env** | `/root/autodl-tmp/envs/openvla-oft` (Python 3.10, torch 2.2.0+cu121) |
| **GPU** | RTX 4090 D, 15.9GB/24.6GB 使用中 |
| **模型** | 本地权重 `/root/autodl-tmp/models/openvla-oft/object/` 已加载 |
| **依赖** | openvla-oft, robosuite 1.4.1, mujoco 3.8.1, LIBERO (PYTHONPATH) |
| **Eval 配置** | libero_object, 10 tasks × 50 trials, seed=7 |
| **日志** | `/root/autodl-tmp/eval_results/openvla-oft-official/eval_output.log` |
| **tmux session** | `openvla-oft-eval` |

已设置每 8 分钟自动检查进度。10 tasks × 50 trials = 500 episodes，预计需要几个小时完成。

---
