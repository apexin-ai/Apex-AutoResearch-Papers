# code nlp finetuning control v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nlp_finetuning_control_v1_20260522T052432_result.json`
- **Structured JSON:** [`1be6a1de624e5981e70f.json`](../../sessions/1b/1be6a1de624e5981e70f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已部署完成。状态总结：

**nlp_finetuning_control_v1** — RUNNING

| 项 | 状态 |
|---|---|
| 脚本 | `/root/autodl-tmp/vla-ssd/scripts/nlp_control_r2_probing.py` ✓ 语法通过 |
| 数据 | 10 tasks × 50 demos × 7-DoF actions ✓ |
| 模型下载 | PID 612748，ModelScope CDN，~400KB/s×2 streams |
| 实验进程 | PID 613202，自动等待下载完成后运行 |
| GPU | cuda:1 |
| 预计完成 | 下载 ~6h（瓶颈 shard1 9.29GB），probing ~15min |
| 输出 | `/root/autodl-tmp/vla-ssd/results/llama2chat_action_probe/` |

下载是瓶颈（AutoDL 出站带宽限制，ModelScope CDN 也只有 ~400KB/s）。`wait_and_run.sh` 每 60s 轮询模型文件大小，到齐后自动在 cuda:1 上启动 R² probing。无需人工干预。

---
