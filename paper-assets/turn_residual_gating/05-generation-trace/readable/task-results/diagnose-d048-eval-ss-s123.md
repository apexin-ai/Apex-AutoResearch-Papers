# diagnose d048 eval ss s123

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d048_eval_ss_s123_20260523T173904_result.json`
- **Structured JSON:** [`019cd61f48d907f534a0.json`](../../sessions/01/019cd61f48d907f534a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：实验未失败，仍在正常运行

### Root Cause
**误报。** PID 110052 当前仍在运行，GPU 占用 30416MiB，利用率 47%。监控系统误判原因：eval 脚本不使用 W&B，且 AR 生成阶段不输出进度日志，导致 5 次轮询均未检测到 sentinel/W&B 活动信号。

### 当前进度

| 阶段 | 状态 | 说明 |
|------|------|------|
| Phase 1: TF 1/4 Base+ours | 完成 | `tf_base_ours/` |
| Phase 1: TF 2/4 Base+dongre | 完成 | `tf_base_dongre/` |
| Phase 1: TF 3/4 SS s123+ours | 完成 | `tf_ss_s123_ours/epoch_2_gar.json` (978KB) |
| Phase 1: TF 4/4 SS s123+dongre | 完成 | `tf_ss_s123_dongre/epoch_2_dongre_gar.json` (978KB) |
| Phase 2: AR 1/2 SS s123 beta=0,3,5 | **运行中** | 模型已加载，N=50 autoregressive 生成中 |
| Phase 2: AR 2/2 Base beta=0 | 待执行 | |
| Phase 3: Bootstrap CI | 待执行 | |

### 关键证据
- `nvidia-smi`: PID 110052 占用 30416MiB，GPU-Util 47%
- `/proc/110052/cmdline`: `python3.12 src/eval_attention_steering.py --checkpoint runs/d048_ss_s123/epoch_2 --gate-type threadgate --mode gen --max-convs 50 --beta 0 3 5`
- 日志最后更新 01:28:27（AR 模型加载完毕后），AR 生成本身不打印逐条进度，这是正常行为
- 无任何 Traceback / OOM / CUDA error

### Checkpoint 状态
完好。`runs/d048_ss_s123/epoch_2/` 包含 `gate_params.pt` (3.3MB) + `lora/` 目录。

### 建议
不需要任何操作。等待 AR 生成自然完成即可（N=50 × 3 beta × autoregressive，预计还需 20-40 分钟）。监控系统对 eval 脚本的判活逻辑需要修正——eval 不走 W&B，应只检查进程存活 + GPU 占用。

---
