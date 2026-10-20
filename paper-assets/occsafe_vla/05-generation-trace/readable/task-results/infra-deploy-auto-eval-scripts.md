# infra deploy auto eval scripts

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy_auto_eval_scripts_20260520T191916_result.json`
- **Structured JSON:** [`364f01f5dd9af1da023d.json`](../../sessions/36/364f01f5dd9af1da023d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### westd-10894 (vanilla)
- **Monitor PID**: 199374，已在后台运行
- **日志确认**: 3 个训练 PID 全部存活，脚本正在每 5 分钟轮询
- **脚本路径**: `/root/occsafe_vla/monitor_and_eval.sh`
- **日志路径**: `/root/occsafe_vla/eval_results/monitor.log`
- **状态文件**: `/root/occsafe_vla/eval_results/monitor_status.txt`

### westd-34685 (occ)
- **脚本已写入**: `/root/occsafe_vla/monitor_and_eval_occ.sh`（未启动）
- PID 映射: (27667→GPU0→occ_s0), (28827→GPU1→occ_s1), (29970→GPU2→occ_s2)
- 启动命令：`nohup bash /root/occsafe_vla/monitor_and_eval_occ.sh > /root/occsafe_vla/eval_results/monitor.log 2>&1 & disown`

### 脚本逻辑
- 每 300 秒检查训练 PID 是否存活
- PID 消失 → 找 `openvla-7b+*_chkpt` 最新 checkpoint → 在对应 GPU 启动 `evaluate_safelibero.py`
- 多组 eval 并行执行（不同 GPU）
- 用 `.launched_*` / `.done_*` 标记文件跟踪状态，避免重复启动
- 3 组全部完成后自动退出

---
