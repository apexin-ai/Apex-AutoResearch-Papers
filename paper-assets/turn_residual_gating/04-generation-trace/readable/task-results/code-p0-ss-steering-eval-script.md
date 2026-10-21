# code p0 ss steering eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0_ss_steering_eval_script_20260523T193821_result.json`
- **Structured JSON:** [`4033786bf314b20f5fc1.json`](../../sessions/40/4033786bf314b20f5fc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**创建的脚本：**
- `/root/turn_residual_gating/scripts/p0_ss_steering_eval.sh` — SS s42 checkpoint + β=0,3,5 steering AR eval (N=50)
- `/root/turn_residual_gating/scripts/p0_after_chain.sh` — 轮询等待 chain 进程结束后自动触发 P0

**Checkpoint 验证：**
- `runs/d048_ss_s42/epoch_2/` 完整 — `gate_params.pt` (3.3MB) + `lora/adapter_model.safetensors` (20MB) 均存在

**Chain 当前状态：**
- Step 2/7 (`d048_ss_s456_resume.sh`) 正在训练，已跑 ~1h40m
- 后续还有 5 步（s456 eval → Qwen-1.5B diag → Qwen-1.5B train → Qwen-1.5B eval → MMLU eval）
- Chain 脚本正在执行中，不能直接追加。`p0_after_chain.sh` 会自动等 chain 进程退出后接上

**启动方式（chain 结束后自动执行）：**
```bash
nohup bash scripts/p0_after_chain.sh > logs/p0_after_chain.log 2>&1 &
```

需要现在就启动后台轮询吗？

---
