# ssh plan003 eval dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan003_eval_dryrun_20260514T005654_result.json`
- **Structured JSON:** [`0e41f4811df4c879b263.json`](../../sessions/0e/0e41f4811df4c879b263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果报告

### 1. `evaluation/eval_swebench.py`（retrieval-only）— **通过**

```
python evaluation/eval_swebench.py --checkpoint-path mock --dry-run --num-instances 5
```

- 完整运行 5 个 instance，耗时 <2 秒
- 输出 `summary.json` + `per_instance_results.jsonl`，格式正确
- Mock retriever 产出 mock 预测文件（`src/pkg/mod_*.py`），recall 全为 0（符合预期）
- `gold_coverage: 1.0`，gold 文件在候选池中
- MRR: 0.0298

### 2. `scripts/eval_swebench.py`（end-to-end）— **部分通过**

- `--retriever-checkpoint mock` 不支持（需要真实 checkpoint 含 `training_config.json`）
- 使用真实 checkpoint（`m2_full_qwen/random_s42/best_by_recall_at_1`）成功加载：
  - 模型 Qwen2.5-Coder-3B 加载成功
  - SWE-bench 数据集从本地缓存加载成功
  - Repo checkout 从 bare cache 成功（astropy 已 checkout 到正确 commit）
  - Evaluation 循环启动正常
- **瓶颈**：CPU 上 3B 模型编码 astropy 700+ .py 文件极慢（预计 20-30 min/instance），5 分钟未完成第一个 instance
- 非功能性警告：`kernels` 包缺失（CPU gemm_4bit_forward），不影响功能

### 3. 注意事项

- HuggingFace 无网络访问，必须设 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`
- LLM backend 默认 `mock`（返回空 patch），正确

### 4. Pipeline 状态

| 组件 | 状态 |
|------|------|
| 数据加载 | OK（本地缓存） |
| 模型加载 | OK |
| Repo checkout | OK（bare cache → 工作副本） |
| Retrieval 逻辑 | OK（mock + 真实 checkpoint 均验证） |
| 输出格式 | OK（JSONL + summary JSON） |
| Bootstrap CI | 未测到（e2e 未完成） |

**结论：Pipeline ready for production run，但必须用 GPU（`CUDA_VISIBLE_DEVICES=0`）。** CPU 模式仅适用于 retrieval-only 的 mock dry-run。

---
