# ops bjb1 status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_status_check_20260514T142726_result.json`
- **Structured JSON:** [`1575772cf220a59d05f8.json`](../../sessions/15/1575772cf220a59d05f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/bjb1_status_report.md`。

**结果摘要**:
- 服务器 bjb1-21071 正常可达
- 4x RTX 5090 (32GB each) 全部空闲，显存占用 2MiB，利用率 0%
- 无 Python 训练/推理进程，无 tmux session，**无僵尸进程需要清理**
- 环境就绪：Python 3.12.3 + PyTorch 2.10.0+cu128 + transformers 4.57.1 + vllm 0.18.1 等全套 ML 栈
- 项目目录 `/root/autodl-tmp/struct_self_consist_ie/` 存在，含 code/data/checkpoints/output
- 磁盘：根分区 37%，数据盘 55%，空间充足
- **服务器完全就绪，可立即开始实验**

---
