# ssh plan003 eval finalize

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan003_eval_finalize_20260514T004614_result.json`
- **Structured JSON:** [`c861af64aa69d2d5b1bf.json`](../../sessions/c8/c861af64aa69d2d5b1bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan003_eval_readiness.md`。

**核心结论：**

- **14/15 项就绪**，唯一缺失是 Qwen3.6-27B 模型未下载（~60GB）
- 所有 pip 依赖已装好：swebench 4.1.0, sb-cli 0.1.5, vllm 0.18.1, openai 2.24.0
- 两个 eval 脚本均功能完整：retrieval-only (`evaluation/eval_swebench.py`) + end-to-end (`scripts/eval_swebench.py`)
- M2 checkpoint 已产出（Qwen 6.2GB + StarCoder 6.1GB，各有 best_by_recall_at_1 和 best_by_val_loss）
- 数据集 300 instances 可离线加载，12 repos bare clone 兼容
- **推荐本地 vLLM 部署 Qwen3.6-27B**：2× 98GB RTX PRO 6000 Blackwell 完全够用，一卡 retriever 一卡 LLM，零边际成本
- **唯一 blocker：M2 训练完成**。训练完成后可立即启动 Stage A（retrieval-only），同时后台下载 Qwen3.6-27B 为 Stage B 做准备

---
