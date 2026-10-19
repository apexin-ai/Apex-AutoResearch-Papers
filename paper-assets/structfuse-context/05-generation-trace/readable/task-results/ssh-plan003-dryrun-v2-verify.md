# ssh plan003 dryrun v2 verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan003_dryrun_v2_verify_20260514T010818_result.json`
- **Structured JSON:** [`4288a0fc7d258187225d.json`](../../sessions/42/4288a0fc7d258187225d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。

---

### 产出汇总

#### 1. 两份 eval_swebench.py 功能区别

| | `evaluation/eval_swebench.py` (550行) | `scripts/eval_swebench_e2e.py` (576行，已重命名) |
|---|---|---|
| **阶段** | Stage A: Retrieval-only | Stage B: End-to-end |
| **核心流程** | 编码 query+候选文件 → 余弦排序 → Recall@k / MRR | 检索 top-k → LLM agent 生成 patch → verify patch → resolve rate |
| **关键函数** | `rank()`, `recall_at_k()`, `reciprocal_rank()` | `generate_patch()`, `verify_patch()`, `compute_bootstrap_ci()` |
| **GPU 需求** | 编码模型推理 | 编码 + LLM 推理（支持 API / mock 后端） |
| **输出指标** | Recall@1/5/10/20, MRR, gold_coverage | Resolve rate + 95% bootstrap CI |

#### 2. 重命名完成

`scripts/eval_swebench.py` → `scripts/eval_swebench_e2e.py`

#### 3. Dry-run 输出

```
Instances: 5 total, 5 valid, 0 errors
  Recall@ 1: 0.0000
  Recall@ 5: 0.0000
  Recall@10: 0.0000
  Recall@20: 0.2000
  MRR:       0.0400
  Gold coverage: 1.0000
```

#### 4. summary.json

```json
{
  "config": {
    "checkpoint_path": "mock",
    "swebench_split": "lite",
    "pool_size": 0,
    "top_k": [1, 5, 10, 20],
    "dry_run": true,
    "timestamp": "2026-05-14 09:09:50"
  },
  "total_instances": 5,
  "valid_instances": 5,
  "errors": 0,
  "recall@1": 0.0,
  "recall@5": 0.0,
  "recall@10": 0.0,
  "recall@20": 0.2,
  "mrr": 0.04,
  "gold_coverage": 1.0
}
```

#### 5. per_instance_results 样本

5 条实例全部成功。mock retriever 生成随机 `src/pkg/mod_*.py` 候选，仅第 5 条 (`astropy__astropy-12907`) 在 top-20 中命中真实 gold file `astropy/modeling/separable.py`（排名第 17，score=0.51），所以 Recall@20=0.2, MRR=0.04。pipeline 逻辑正确，gold_coverage=1.0（所有 gold file 都在候选池中）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "config": {
      "checkpoint_path": "mock",
      "swebench_split": "lite",
      "pool_size": 0,
      "top_k": [
        1,
        5,
        10,
        20
      ],
      "dry_run": true,
      "timestamp": "2026-05-14 09:09:50"
    },
    "total_instances": 5,
    "valid_instances": 5,
    "errors": 0,
    "recall@1": 0.0,
    "recall@5": 0.0,
    "recall@10": 0.0,
    "recall@20": 0.2,
    "mrr": 0.04,
    "gold_coverage": 1.0
  }
}
```

</details>

---
