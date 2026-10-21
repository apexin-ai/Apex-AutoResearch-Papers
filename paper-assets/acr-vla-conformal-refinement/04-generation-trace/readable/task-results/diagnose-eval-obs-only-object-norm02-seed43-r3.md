# diagnose eval obs only object norm02 seed43 r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm02-seed43-r3_20260520T135439_result.json`
- **Structured JSON:** [`dc8bf4cae718da725555.json`](../../sessions/dc/dc8bf4cae718da725555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败根因：tmux session 被外部终止（SIGHUP）**

- EXIT_CODE=129 = 收到 SIGHUP（信号1），即进程失去控制终端
- 服务器 uptime 35 天，未发生重启
- tmux 会话 `eval-obs-only-object-norm02-seed43-r3` 已不存在（当前仅有 5 个其他会话）
- dmesg 无权限访问，但 SIGHUP 不是 OOM 的特征（OOM 会是 SIGKILL/exit 137）
- 最可能原因：**有人/脚本清理了该 tmux session**，或 tmux 服务器短暂崩溃后重建

**进度**：完成 8/10 个 task，第 9 个 task（chocolate_pudding）跑到 rollout 5/10 时中断，第 10 个 task 未开始。无 JSON 结果文件产出。

已完成 task 的 SR：

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 30% |
| bbq_sauce | 20% |
| ketchup | 10% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | 20% |

8 个已完成 task 合计 10/80 = 12.5%，与 r2 的 SR=16% 量级一致。

**是否需要重试**：r2 已成功产出 SR=16%，r3 本身是冗余 run。从已完成的 8/10 task 看趋势约 12.5%，与 r2 接近，重试价值不大。如果需要完整 r3 数据可以重跑，但对结论影响很小。

---
