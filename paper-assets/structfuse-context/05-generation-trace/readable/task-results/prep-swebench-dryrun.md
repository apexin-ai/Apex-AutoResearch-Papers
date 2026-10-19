# prep swebench dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_swebench-dryrun_20260514T220727_result.json`
- **Structured JSON:** [`e840573306214406efdf.json`](../../sessions/e8/e840573306214406efdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成。核心结论：

**检索评估 ✅ 全部就绪** — SWE-bench Lite 数据(300 instances)、12个预克隆仓库(667MB)、评估脚本(`eval_swebench.py` + `eval_swebench_e2e.py`)、swebench 包均已到位。M2 `dataflow_aware` checkpoint 产出后可直接运行。

**需关注的 gap**：
- `dataflow_aware` checkpoint 尚未产出（M2 训练中），现有 `random_s42/s43/s44` 可先跑 baseline
- E2E 评估需要 LLM backend：本地 vllm 已装但 GPU 被 M2 占用，外部 API 需配置 `STRUCTFUSE_LLM_API_KEY`
- Docker 不可用，但两个评估脚本均不依赖 docker，无影响
- 磁盘空间充足（数据盘 817G 可用）

报告已注册：`art_20260514_a7df8a`

---
