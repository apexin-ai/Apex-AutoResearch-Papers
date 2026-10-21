# check westd27271 pi05 model

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd27271_pi05_model_20260527T100415_result.json`
- **Structured JSON:** [`556e99d8fe3f692f28c1.json`](../../sessions/55/556e99d8fe3f692f28c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

**π0.5 模型**: 存在，路径 `/root/autodl-tmp/pi05_libero_finetuned`。之前已有多次 π0.5 评估记录（logs 和 eval_results 中有大量 pi05 相关文件）。

**OpenVLA 模型**: 有多个可用：
- `openvla-7b`
- `openvla-7b-finetuned-libero-10`
- `openvla-7b-finetuned-libero-goal`
- `openvla-7b-finetuned-libero-spatial`
- `openvla-7b-git`, `openvla-7b-hf`, `openvla-7b-meta`
- `openvla-libero-object`

**GPU 状态**: 两张 NVIDIA RTX PRO 6000 Black (各 ~98GB)，**两块都在使用中**：
- GPU 0: 15964MiB 占用, 87% 利用率 (PID 830291)
- GPU 1: 15980MiB 占用, 66% 利用率 (PID 735728)

**GPU 0 不空闲，无法立即部署 π0.5 实验。**

**磁盘**: `/root/autodl-tmp/` 250GB，已用 203GB，剩余 48GB (81% 使用率)。空间够用。

---
