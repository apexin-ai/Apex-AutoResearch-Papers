# code eval swebench verify

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-swebench-verify_20260515T061841_result.json`
- **Structured JSON:** [`b5720c60224310d93b3a.json`](../../sessions/b5/b5720c60224310d93b3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均就绪，`--help` 正常。总结：

---

### 脚本状态：✓ 就绪

**1. `evaluation/eval_swebench.py`** — 检索质量评估（Retrieval-only）

| 项目 | 内容 |
|------|------|
| 输入 | `--checkpoint-path` (M2 best checkpoint 或 `mock`) |
| 检索 | 加载 StructFuse checkpoint encoder，cosine similarity 排序 |
| 指标 | Recall@{1,5,10,20}, MRR |
| 输出 | `per_instance_results.jsonl` + `summary.json` |
| dry-run | `--checkpoint-path mock --dry-run --num-instances 5`（无 GPU） |
| repo cache | `--repo-cache-dir /root/autodl-tmp/structfuse/swebench_repos/` |

**2. `scripts/eval_swebench_e2e.py`** — 端到端评估（Retrieval + LLM Agent patch）

| 项目 | 内容 |
|------|------|
| 输入 | `--retriever-checkpoint` + `--strategy {random,embedding_distance,dataflow_aware}` |
| API 调用 | env vars: `STRUCTFUSE_LLM_BACKEND=api`, `STRUCTFUSE_LLM_API_BASE`, `STRUCTFUSE_LLM_API_KEY`, `STRUCTFUSE_LLM_MODEL` |
| 检索 | StructFuse checkpoint encoder |
| 指标 | resolve rate + 95% bootstrap CI |
| 输出 | `results.jsonl` + `summary.json` |
| repo cache | `--repo-cache-dir` 支持 `org_name` 和 `org__name` 命名 |

**3. 预克隆 repos** — 12/12 就绪：django, flask, matplotlib, pytest, requests, scikit-learn, sphinx, sympy, astropy, pylint, seaborn, xarray

---
