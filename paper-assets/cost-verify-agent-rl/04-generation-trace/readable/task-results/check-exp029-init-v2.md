# check exp029 init v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_init_v2_20260516T122757_result.json`
- **Structured JSON:** [`0226aae703088636e46b.json`](../../sessions/02/0226aae703088636e46b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp029 初始化通过。**

- **进程**: PID 861524 存活，运行 2 分 55 秒，状态 Ss+
- **GPU**: cuda:0 和 cuda:1 各占用 4715 MiB / 97887 MiB（模型已加载，尚未进入 rollout 高显存阶段）
- **日志**: FSDP workers 初始化完成，数据集加载完成 (8810/8810 + 494/494)，wandb run `exp029-alfworld-episode-level` 已创建 (run id: x4bbiddh)，正在进入训练循环
- **错误**: grep 匹配到的 "Error" 仅来自配置打印中的 `'truncation': 'error'` 字符串，无真实错误、无 OOM、无 Traceback

初始化成功，实验已进入正常运行阶段。

---
