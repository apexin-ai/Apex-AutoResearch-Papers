# code swebench eval pipeline

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_swebench_eval_pipeline_20260513T184700_result.json`
- **Structured JSON:** [`33eb2022ce2ea2f0ca1e.json`](../../sessions/33/33eb2022ce2ea2f0ca1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**完成。** 脚本已写入 `/root/structfuse/evaluation/eval_swebench.py`（原文件备份为 `.bak`）。

验证结果：
- `--help` 正常
- Dry-run（mock fallback）通过：5 instances，metrics 计算正确，输出格式正确
- Dry-run（真实 HF 数据）通过：加载 SWE-bench Lite 300 instances，gold files 正确提取
- 断点续跑通过：重跑时检测到已完成 instances 并跳过

**M2 训练完成后的使用命令：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
cd /root/structfuse/evaluation

# Qwen best_by_recall_at_1 checkpoint
python eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/&lt;strategy>_s&lt;seed>/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/qwen_&lt;strategy>_s&lt;seed>

# StarCoder best_by_recall_at_1 checkpoint
python eval_swebench.py \
    --checkpoint-path /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/&lt;strategy>_s&lt;seed>/best_by_recall_at_1 \
    --output-dir /root/autodl-tmp/structfuse/eval_results/starcoder_&lt;strategy>_s&lt;seed>
```

`&lt;strategy>` = `random` / `embedding_distance` / `dataflow_aware`，`&lt;seed>` = `42` / `123` / `456`。

---
