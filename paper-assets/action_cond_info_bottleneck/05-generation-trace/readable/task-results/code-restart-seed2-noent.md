# code restart seed2 noent

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_restart_seed2_noent_20260516T030219_result.json`
- **Structured JSON:** [`12b94f80b7ab0c3a7878.json`](../../sessions/12/12b94f80b7ab0c3a7878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING，PID=736291。

总结：

- **PID 728882** 已确认死亡
- 发现一个**更早的重启进程** (PID 736291) 已在 cuda:1 上运行，参数与要求一致：
  - `lambda_ent=0`, `diversity_lambda=0.1`, `seed=1337`, `hidden_dim=64`, `alpha=0.01`, `beta=0.01`, `beta_warmup_steps=1000`
- 训练进度：Step 200/20000, loss=0.0409, 0.5 steps/s，预计 ~11h 完成
- 我的额外提交 (PID 736911) 因 GPU 冲突已失败并清理
- **注意**：原始 log 文件被误删（我清空 output dir 时 tmux session 的 log redirect 链断了），只能通过 `cat /proc/736286/fd/1 | grep "^Step"` 读取实时进度
- Registry 已更新：status=RUNNING, PID=736291, spec 含 `lambda_ent: 0`

---
