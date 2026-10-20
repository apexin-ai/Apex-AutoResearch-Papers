# diag mvp2 eval lr5e6 r1 ckpt40

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp2_eval_lr5e6_r1_ckpt40_20260514T213807_result.json`
- **Structured JSON:** [`c1fd64e29a6c5a33e85a.json`](../../sessions/c1/c1fd64e29a6c5a33e85a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：被监控系统误杀（SIGTERM）

进程 **不是 OOM、不是脚本错误、不是 checkpoint 问题**。

**证据链：**

1. **exit -15 = SIGTERM**：进程被外部信号终止，非 Python 崩溃（无 traceback）、非 OOM killer（OOM 是 SIGKILL/-9）
2. **推理正常进行中被杀**：日志显示 inference 已完成 10/62 batches（16%），每 batch 约 93-122s，运行约 17 分钟后被终止
3. **任务描述确认**：`process dead 5× with no sentinel/W&B — auto-resolved as failed` — 监控系统检测到进程没有产出 sentinel 文件或 W&B 心跳信号，连续 5 次判定为"死亡"，自动发送 SIGTERM 杀掉了进程
4. **checkpoint-40 完整**：adapter_model.safetensors (264MB) + 全部配置文件齐全
5. **cuda:2 当前状态**：9.7GB / 32.6GB，显存充裕
6. **日志无任何 Python error/traceback/OOM**

### 本质问题

eval 任务预计总运行时间 ~100 分钟（62 batches × ~100s），但 eval 脚本（`batch_eval`）不产生 W&B 日志或 sentinel 文件，监控系统误认为进程已死。

### 建议修复方案

**可以直接重试**，但需要绕开监控系统的误杀机制。两个选项：

1. **推荐：在 tmux 中直接运行**，不通过会被监控的调度方式启动：
   ```bash
   tmux new -s eval_lr5e6_ckpt40
   CUDA_VISIBLE_DEVICES=2 bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh
   ```

2. **如果必须用监控调度**：给 eval 脚本加 sentinel/心跳输出，或调大监控的超时阈值，使其能容忍 ~2 小时无 W&B 信号的 eval 任务。

**无需改任何模型/数据/batch_size 参数**，eval 本身运行正常。

---
