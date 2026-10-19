# ssh plan014 script update d025

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan014_script_update_d025_20260514T010306_result.json`
- **Structured JSON:** [`316f23c7661716ea3335.json`](../../sessions/31/316f23c7661716ea3335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本语法检查全部通过，数据文件都存在。

---

**修改总结**

| 项目 | 原值 | 新值 |
|------|------|------|
| strategies | random, embedding_distance, dataflow_aware (3) | random, embedding_distance (2) |
| epochs | 3 | 2 |
| GPU | CUDA_VISIBLE_DEVICES=0 硬编码 | 主脚本接受 `--gpu` / `CUDA_ID` 环境变量 |
| 总 runs | 9 | 6 |

**6 runs 双卡分配**

| cuda:0 (`run_plan014_temp_cuda0.sh`) | cuda:1 (`run_plan014_temp_cuda1.sh`) |
|--------------------------------------|--------------------------------------|
| τ=0.05 × random | τ=0.1 × embedding_distance |
| τ=0.05 × embedding_distance | τ=0.2 × random |
| τ=0.1 × random | τ=0.2 × embedding_distance |

每卡 3 runs，工作量均衡（同 strategy 数据量相同，2 epochs 训练时间基本一致）。

**预估 wall time**：原 9 runs × 3 epochs 单卡串行。改为 3 runs × 2 epochs 双卡并行，单卡 wall time ≈ 原来的 3/9 × 2/3 = **约 22%**。若原先单 run 约 40min（Qwen-3B + LoRA + batch 8），双卡并行总 wall time ≈ 3 × 27min ≈ **~80min**。

**启动方式**：
```bash
nohup bash /root/structfuse-context/run_plan014_temp_cuda0.sh > /tmp/plan014_cuda0.log 2>&1 &
nohup bash /root/structfuse-context/run_plan014_temp_cuda1.sh > /tmp/plan014_cuda1.log 2>&1 &
```

---
