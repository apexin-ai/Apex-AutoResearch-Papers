# ssh kill and diagnose

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-and-diagnose_20260512T213627_result.json`
- **Structured JSON:** [`47d813a8be33877e6ea9.json`](../../sessions/47/47d813a8be33877e6ea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正式 eval 已正常启动并在推理中。

---

## 总结

| 步骤 | 结果 |
|------|------|
| **1. Kill 卡死进程** | 17840、17369 均已终止（SIGTERM），GPU 显存完全释放 ✓ |
| **2. 单样本测试 (Step A)** | **成功**，27 秒完成。RE F1=0.5882, Evi F1=0.5500, Attribution=1.0 |
| **3. CUDA cache (Step B)** | ssh_read_only 不支持重定向查 cache 路径，但单样本测试无 JIT 卡死问题 |
| **4. 正式 eval (Step C)** | **已启动**，PID=40391，GPU 0 占用 18947 MiB，模型已加载并开始推理。GPU 1 空闲待用 |
| **日志路径** | `/tmp/sft_eval_v2.log` |
| **结果路径** | `./outputs/sft/eval_results_v2.json` |

985 个样本 batch_size=8，预计 ~50-60 分钟完成。

---
