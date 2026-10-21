# audit westd38929 full 20260526c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929-full-20260526c_20260526T190117_result.json`
- **Structured JSON:** [`45e93c264e38acf699c4.json`](../../sessions/45/45e93c264e38acf699c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

xvla_random_k05_spatial_seed43 已完成。汇总如下：

```
GPU 0: 占用  PID=623613,  显存=16339/97887 MiB
        实验=eval_openvla_l2norm_k05_long_seed42
        进度=Task 5/10, Ep 20/50  运行 5h06m  状态=运行中

GPU 1: 占用  PID=668245,  显存=15861/97887 MiB
        实验=eval_openvla_random_k085_long_seed42_v3
        进度=Task 4/10, Ep 40/50  运行 3h38m  状态=运行中

GPU 2: 占用  PID=732931,  显存=16169/97887 MiB
        实验=eval_openvla_l2norm_k075_long_seed42 (新实验，非原始追踪列表)
        进度=Task 2/10, Ep 30/50  运行 1h31m  状态=运行中

GPU 3: 占用  PID=514356,  显存=15762/97887 MiB
        实验=eval_openvla_attn_k085_long_seed42_v3
        进度=Task 9/10, Ep 40/50  运行 7h51m  状态=运行中(即将完成)

已完成实验：
- eval_xvla_random_k05_spatial_seed43: SR=72.6% (363/500)
  per-task: 100%/38%/88%/92%/88%/0%/94%/68%/92%/66%
  完成时间: 2026-05-24 07:29 UTC

空闲 GPU: 无
```

注意：
- PID 155546 (eval_xvla_random_k05_spatial_seed43) 已于 5/24 完成，无 exit 文件（日志在项目 logs/ 目录）
- GPU 2 上运行的 l2norm_k075 不在原始追踪列表中，是后续启动的新实验
- GPU 3 的 attn_k085 在 Task 9/10 ep 40/50，预计 ~30 分钟内完成

---
