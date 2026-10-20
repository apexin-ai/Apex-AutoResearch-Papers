# ops verify d054 startup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d054-startup_20260513T215139_result.json`
- **Structured JSON:** [`33dea6b666f498b43db5.json`](../../sessions/33/33dea6b666f498b43db5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
CWM v12 启动: ⚠️ 进程存活但疑似卡住
  PID 链: 181197 → 181201 → 181202 (python3 train_repo_cwm.py --seed 42)
  日志仅 4 行，最后更新 05:50:54，停在 "Class weights" 之后
  PID 181202 未出现在 nvidia-smi 进程列表 — 未分配 GPU 显存
  原因: cuda:1 已被 CWM seed123 (PID 142402, 16326 MiB) 占用
  v12 可能在模型加载阶段排队/死等 GPU 显存
transformers 版本: 未能直接验证（read_only 不支持分号），但 conda base 环境启动的

home seed123 进度: ❌ OOM 崩溃
  错误: torch.OutOfMemoryError — 尝试分配 1.36 GiB，GPU 仅剩 105.94 MiB
  崩溃在 step 0/6633，未产出任何训练数据
  PID 2998850: 已死 (EXIT_CODE=1)

westd GPU 状态:
  cuda:0: 占用 24914 MiB — CLS seed123 (PID 141203, train_repo_verifier.py --seed 123)
  cuda:1: 占用 16326 MiB — CWM seed123 (PID 142402, train_repo_cwm.py --seed 123)
  cuda:2: 占用 10768 MiB — eval CWM v11 ckpt600 (PID 180344, eval_repo_cwm.py)
  cuda:3: 占用 25744 MiB — CLS 8B (PID 140060, train_repo_verifier_8b.py --seed 42)
```

**需要处理的问题:**
1. **CWM v12 卡住**: GPU 1 被 CWM seed123 占着，v12 无法获取显存。需要等 seed123 完成或 kill 它，或者改 v12 到其他 GPU
2. **home seed123 OOM**: 需要降低 batch size 或启用 gradient checkpointing 后重跑
3. **westd 四卡全满**: 没有空闲 GPU，cuda:2 的 eval 任务完成后会释放

---
