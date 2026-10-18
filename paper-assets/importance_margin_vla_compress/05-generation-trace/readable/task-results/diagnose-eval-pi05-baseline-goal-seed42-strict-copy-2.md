# diagnose eval pi05 baseline goal seed42 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_baseline_goal_seed42_strict_20260527T054137_result.json`
- **Structured JSON:** [`87f663cb4dcac52b771c.json`](../../sessions/87/87f663cb4dcac52b771c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注册表已更新为 RUNNING。

## 总结

**死因**：上次实验（12:55启动）运行正常到 Task 3 ep20（T0=92%, T1=100%, T2=96%），随后被另一个 OpenVLA 实验（PID 11249）启动挤上同一 GPU 1 导致 OOM 杀进程。

**已重新提交**：
- **exp_id**: `eval_pi05_baseline_goal_seed42_strict`
- **GPU**: 0（等待当前 OpenVLA random k=0.95 完成后自动启动，预计 ~2h 后）
- **tmux session**: `baseline_goal_strict`
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_baseline_goal_seed42_strict.log`
- **防护**：脚本轮询 GPU 0 显存 < 1GB 才启动，避免再次 OOM
- **代码确认**：`eval_pi05_pruning_libero.py` line 422 为 `if done:` strict 条件，无 reward 判定
- **预估完成时间**：GPU 0 空闲后 ~85 分钟完成（10 tasks × 50 eps），预计北京时间今天 17:30 前出结果，远在截止日期（5月28日20:00）之前

---
