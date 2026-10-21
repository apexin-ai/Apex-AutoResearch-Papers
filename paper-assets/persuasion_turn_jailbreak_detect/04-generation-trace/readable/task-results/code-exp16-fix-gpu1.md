# code exp16 fix gpu1

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-fix-gpu1_20260519T202812_result.json`
- **Structured JSON:** [`844c4abaac645c7e3b1f.json`](../../sessions/84/844c4abaac645c7e3b1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**警告：状态与用户描述不符，存在已运行的训练**

不要启动新脚本——服务器上已经有两条并发的训练流水线在跑 GPU 1。

**实际状态（current time: 04:33:12）：**

| 进程 | 当前任务 | etime | 父进程 |
|------|---------|-------|--------|
| PID 293489 → 298864 | s123 Stage 2（GRU，embedding 已预计算，CPU 阶段） | 06:01 | submit_training_job 启动的 `exp16_9class_train`（03:59 启动） |
| PID 303154 | s456 Stage 1（占 GPU 1 94%、10GB 显存） | 01:29 | PPID 300470（非 Pipeline A 子进程，独立的另一条流水线） |

**已完成的 checkpoint：**
- `9class_seed42/best/model.pt`（Stage 1，04:08）
- `9class_seed123/best/model.pt`（Stage 1，04:31:49——已有）
- `9class_gru_seed42/treatment/best.pt`（Stage 2，04:30）

**用户说"崩溃"，但实际：**
- `~/runs/.../exp16_9class_train.log` 末尾确实有 `httpx.ConnectError: Network is unreachable`（用户描述的报错）
- 但 Pipeline A（PID 293489）依然存活（etime 34:44）——可能上游 trap 没让它退出，或者错误发生在某个子步骤已恢复
- 同时不知道是谁又启动了 Pipeline B（PID 303154，PPID 300470，正在跑 s456 Stage 1）

**两条流水线写到相同输出目录**，会互相覆盖 `9class_seed456/`、`9class_gru_seed123/` 等 checkpoint。我**没有创建恢复脚本，也没启动新 tmux**，因为再启动第三条只会让冲突更严重。

模型缓存验证：`CACHE OK`（`TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1` 加载 DeBERTa 成功）。

**请确认下一步：**
1. **保留 Pipeline A，杀掉 Pipeline B**（PID 303154 及其 PPID 300470 树），让 A 自己跑完？
2. **杀掉两个，启动一个干净的恢复脚本**？（按用户原计划）
3. **保留 B，杀掉 A**？
4. **都先别动**，让我先 tail Pipeline A 当前日志看是否真的健康？

---
