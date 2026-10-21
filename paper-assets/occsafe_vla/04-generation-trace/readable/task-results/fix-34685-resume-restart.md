# fix 34685 resume restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_34685-resume-restart_20260527T212534_result.json`
- **Structured JSON:** [`82b38d9215f5f07e4ef4.json`](../../sessions/82/82b38d9215f5f07e4ef4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验已经在正确 resume，不需要 kill。**

验证结果：

**detach_ln_v2_s2** (PID 26152, cuda:0):
- 命令已包含 `--resume True --resume_step 15000`
- `--vla_path` 指向 `...--15000_chkpt` checkpoint 目录
- 日志确认加载了 `proprio_projector--15000`, `action_head--15000`, `occ_head--15000`

**vanilla_object_s0** (PID 26367, cuda:1):
- 命令已包含 `--resume True --resume_step 10000`
- `--vla_path` 指向 `...--10000_chkpt` checkpoint 目录
- 日志确认加载了 `proprio_projector--10000`, `action_head--10000`

tqdm 显示 `0/50005` 是正常行为——`gradient_step_idx` 从 0 计数，但 `log_step = resume_step + gradient_step_idx`（finetune.py:1235）。

**注意事项：** `--max_steps 50005` 未针对 resume 调整，两个实验实际会训练 50005 个额外 gradient step（detach_ln_v2_s2 总计 65005 步，vanilla_object_s0 总计 60005 步）。如果目标是 50005 总步数，需要 kill 重启并调整 max_steps。

全 GPU 状态：4/4 活跃（cuda:0 detach_ln_v2_s2, cuda:1 vanilla_object_s0, cuda:2 full_occ_ln_v2_s3, cuda:3 detach_ln_v2_s3）。

```
finetune.py resume 机制: --resume True --resume_step &lt;N>，vla_path 指向 checkpoint 目录。
  load_checkpoint() 读取 {vla_path}/{module}--{step}_checkpoint.pt
  log_step = resume_step + gradient_step_idx
  optimizer/scheduler 不保存，resume 后重新初始化

detach_ln_v2_s2:
  状态: 已正确 resume，无需操作
  resume checkpoint: ...--15000_chkpt
  起始 step: 15000（log_step = 15000 + gradient_step_idx）
  训练中: 是（~300 gradient steps completed）

vanilla_object_s0:
  状态: 已正确 resume，无需操作
  resume checkpoint: ...--10000_chkpt
  起始 step: 10000（log_step = 10000 + gradient_step_idx）
  训练中: 是（~294 gradient steps completed）

全 GPU 状态: 4/4 活跃
```

---
