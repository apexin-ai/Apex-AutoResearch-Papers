# check gpu and phi3 status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_and_phi3_status_20260523T235401_result.json`
- **Structured JSON:** [`78597ccdc0939da76b55.json`](../../sessions/78/78597ccdc0939da76b55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报

| 项目 | 状态 |
|------|------|
| **GPU 0** | RTX PRO 6000 Black (98GB), 40°C, 89W, 显存 681MiB/97887MiB, 利用率 0%（Phase 2 是 CPU-bound Ridge 回归） |
| **GPU 1** | RTX PRO 6000 Black (98GB), 36°C, 36W, 显存 0MiB, 空闲无进程 |
| **phi3_nlp_control 进程** | PID 775588, 07:53 启动（运行约 1 分钟），CPU 3623%，`python scripts/phi3_nlp_control_probe.py --gpu 0` |
| **最近产出** | `results/phi3_nlp_control/` 目录已创建（May 24 07:30），日志正在写入 |

**日志进度**：
- Phase 1（hidden state 提取）已完成：5000 samples, 10 tasks, 耗时 1.4s
- Phase 2（Ridge R2 probing）进行中：已完成 L0 (R2=0.1555), L4 (R2=0.1554), L8 (R2=0.1555)，每层约 20s
- 按每 4 层采样、32 层总计，还剩约 6 层（L12–L32），预计 ~2 分钟内完成

**判断：实验正常运行中**，Phase 2 CPU 密集计算进行中，GPU 仅用于模型加载/推理（Phase 1 已结束）。R2 值在前 3 层均 ~0.155，符合 NLP-only 模型作为 control baseline 的预期（无视觉 grounding → 低 action 预测能力）。

---
