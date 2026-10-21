# investigate process gone and analyze

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_process_gone_and_analyze_20260527T122616_result.json`
- **Structured JSON:** [`b8d2145ffa195faaf195.json`](../../sessions/b8/b8d2145ffa195faaf195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成：

## 任务 1: eval_pi05_l2norm_k05_long_seed42_strict_w38

**结论: DONE(failed)**
- 进程在 T0 ep=10 (30%) 后消失，日志仅 30 行，最后写入 20:17 UTC
- 无 sentinel 文件、无结果 JSON、无错误信息（疑似被 kill 或 OOM）
- **替代实验已在跑**: `eval_pi05_l2norm_k05_long_seed42_strict`（PID 250745, CUDA:3, 同服务器 westd-38929）进展正常，T0=58.0%, 正在评估 T1
- `eval_pi05_l2norm_k05_long_seed42_strict`（无 _w38 后缀）registry 状态 RUNNING，部署在 westd-38929

## 任务 2: eval_openvla_l2norm_k085_object_seed42

**结论: DONE(success) — 重跑确认 SR=55.2%**
- Overall SR: 55.2% (276/500), EXIT_CODE=0, 耗时 254.8 min
- Per-task: 60%, 40%, 60%, 44%, 92%, 42%, 50%, 58%, 52%, 54%
- 与前次完全一致，**k=0.85→k=0.75 的非单调性（55.2%→57.4%）已确认为真实现象**
- Registry 已有正确 metrics 和 conclusion=success，无需额外更新

---
