# investigate westd27271 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_westd27271_gpu_status_20260525T051425_result.json`
- **Structured JSON:** [`f4412c4e37ecf48ed30e.json`](../../sessions/f4/f4412c4e37ecf48ed30e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

### GPU 0 — Baseline eval (PID 202124, wrapper 202119)
- **任务**: `--mode baseline --suite libero_object --seed 42`
- **进度**: Task 5/10，Ep 40/50，速度 ~2.2 eps/min
- **已完成 task 成功率**:
  - Task 2: 80% (40/50)
  - Task 3: 82% (41/50)
  - Task 4: 46% (23/50)
  - Task 5: 进行中 (39/40 暂时 97.5%)
- **预计剩余**: ~5.5 个 task × ~23 min/task ≈ 2 小时完成
- **日志**: 正常写入 `/root/runs/.../eval_openvla_baseline_object_seed42_v2.log`

### GPU 1 — 孤儿进程 (PID 213708)
- **任务**: `--mode random_prune --k_ratio 0.9 --suite libero_object --seed 42`
- **输出**: `eval_results/openvla_random_prune_k09_object_seed42_v2.json`（尚未生成，说明还在跑）
- **启动时间**: 12:03，从交互终端 (pts/0) 启动，**无日志文件**，无法查看进度
- **运行时长**: ~71 分钟，预计还需 ~2.5-3 小时

### 判断：孤儿进程是否保留？

**建议保留。** 理由：
1. 这是 OpenVLA random prune k=0.9 在 libero_object 上的评估，是正式实验需要的 random baseline 对照数据
2. 已经跑了 71 分钟，kill 掉就浪费了
3. 唯一问题是没有日志，但最终结果会写入 JSON 文件
4. 跑完后把结果注册到 registry 即可

两个 GPU 都在满负荷工作，没有浪费。

---
