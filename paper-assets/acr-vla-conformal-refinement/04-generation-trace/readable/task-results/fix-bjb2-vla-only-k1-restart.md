# fix bjb2 vla only k1 restart

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb2-vla-only-k1-restart_20260514T000132_result.json`
- **Structured JSON:** [`b25ac01500914648920e.json`](../../sessions/b2/b25ac01500914648920e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇报：**

代码修复**已经存在**。`main()` 函数中已有：
```python
if args.mode == "vla_only":
    args.K = 1
```

日志确认 `'K': 1` 生效。

**当前运行中的 eval (PID 125830)**:
- 命令：`python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42`
- 日志：`/root/autodl-tmp/eval_results/eval-object-v6.log`
- 启动时间：08:02，正在加载 LIBERO object 环境（10 个 task）
- K=1 已生效，无需重新启动

不需要额外操作 — 修复已到位，eval-object-v6 正以 K=1 运行中。

---
