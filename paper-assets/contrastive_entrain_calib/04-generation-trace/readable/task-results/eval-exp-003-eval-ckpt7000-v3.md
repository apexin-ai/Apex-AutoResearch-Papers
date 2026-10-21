# eval exp 003 eval ckpt7000 v3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-003-eval-ckpt7000-v3_20260521T081249_result.json`
- **Structured JSON:** [`89db6b27661d0c586318.json`](../../sessions/89/89db6b27661d0c586318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务完成。** 总结：

### 失败诊断
- **v1**: 正常运行到 80/362 后被 SIGTERM kill (EXIT_CODE=143)，外部进程清理
- **v2**: LoRA 加载时 GPU 内存不足（accelerate 报缺 2.3GB），随后被 SIGTERM kill
- **根因**: cuda:3 被叠加提交多个 eval 任务（发现 PID 191750 + PID 193010 同时占 cuda:3，29.7GB / 32.6GB），导致内存争抢和进程被 kill

### v3 提交
- **exp_id**: `exp-003-eval-ckpt7000-v3`
- **GPU**: cuda:0（避开 cuda:3 的 collision 问题）
- **PID**: 861274
- **状态**: RUNNING，模型/LoRA/NLI 全部加载成功，无内存警告
- **预计完成**: ~60-75 分钟（约 17:45-18:00 服务器时间）
- **日志**: `~/runs/contrastive_entrain_calib/exp-003-eval-ckpt7000-v3.log`
- **Registry**: 已更新为 RUNNING，parent=exp-003
- **report.md**: 已自动更新

---
