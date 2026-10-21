# p0 stdout rescue 3servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_p0_stdout-rescue-3servers_20260526T223630_result.json`
- **Structured JSON:** [`ac3cab73c3cce0e34df1.json`](../../sessions/ac/ac3cab73c3cce0e34df1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部诊断完毕。

```
=== cqa1-33015 GPU 1 (PID 617728) — π0.5 Attn k=0.7 Long ===
进程状态: 已死（已完成）
stdout指向: N/A（进程已结束）
tmux session: 有 tmux socket
日志文件: logs/eval_pi05_attention_k07_long_seed42.log (7944 bytes)
结果: ✅ 已完成，SR=50.8%，结果保存至 eval_results/pi05_attention_k0.70_libero_10_seed42.json
结论: 安全 — 实验已正常完成并保存结果

=== westd-38929 GPU 3 (PID 811418) — OV Random k=0.75 Goal ===
进程状态: 存活（已运行 2h07m）
stdout指向: pipe → tee logs/eval_openvla_random_k075_goal_seed42.log
tmux session: 有 tmux socket
日志文件: logs/eval_openvla_random_k075_goal_seed42.log (4076 bytes, 持续写入)
进度: Task 6/10 进行中（Task 5 完成 SR=92%）
结论: 安全 — 通过 `2>&1 | tee` 重定向，日志正常写入文件

=== westd-27271 GPU 0 (PID 499267) — OV Attn k=0.75 Goal ===
进程状态: 存活（已运行 2h07m）
stdout指向: pipe → tee logs/eval_openvla_attn_k075_goal_seed42.log
tmux session: 有 tmux socket
日志文件: logs/eval_openvla_attn_k075_goal_seed42.log (2657 bytes, 持续写入)
进度: Task 7/10 进行中（Task 6 完成 SR=74%）
结论: 安全 — 通过 `2>&1 | tee` 重定向，日志正常写入文件
```

**总结：3 个实验全部安全。** cqa1 的已完成（SR=50.8%），另外两个正在通过 `tee` 写日志，预计再跑 ~1.5h 完成。无需任何干预。

---
