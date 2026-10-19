# ssh find argmin seed46 and verify perdof pid

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find-argmin-seed46-and-verify-perdof-pid_20260517T103212_result.json`
- **Structured JSON:** [`3747f85ca803f40811a3.json`](../../sessions/37/3747f85ca803f40811a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== argmin seed46 定位 ===
服务器搜索结果：
- bjb1-18228: 进程不存在，无日志/输出文件
- bjb1-32546: 进程不存在，已完成。日志: eval_argmin_object_seed46.log，输出: eval_object_reconvla_seed46.json
- bjb2-28827: 进程不存在，无日志/输出文件
- bjb2-40593: 进程不存在，无日志/输出文件

结果文件内容：
- mode: reconvla, benchmark: object, K=10, seed=46, n_rollouts=10
- overall_success_rate = 10.0% (10/100)
- 日志末尾: "Results saved to logs/eval_object_reconvla_seed46.json" — 正常完成

结论：已完成(SR=10.0%)，位于 bjb1-32546

=== perdof seed44 PID 验证 ===
- PID 531963: 存在，是 bash wrapper 进程（S 状态，CPU 0%）
- PID 531970: 存在，是实际 python 进程（Rl 状态，CPU 134%，运行中）
- 完整命令: `python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json`

确认：mode=crm_perdof ✓, seed=44 ✓, max_correction_norm=0.1 ✓。Registry PID 531963 是 bash wrapper，实际工作进程是 531970，两者都在运行。
```

---
