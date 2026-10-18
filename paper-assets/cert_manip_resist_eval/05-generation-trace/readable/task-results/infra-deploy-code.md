# infra deploy code

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deploy-code_20260521T180140_result.json`
- **Structured JSON:** [`c07d36125d1acbf20b69.json`](../../sessions/c0/c07d36125d1acbf20b69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署完成，全部验证通过

| 项目 | 结果 |
|------|------|
| **17 文件部署** | 全部到位 (`/root/cert_manip_resist_eval/`) |
| **pip install** | 成功安装 vllm 0.21.0 + 100+ 依赖 |
| **torch** | 2.11.0+cu128, CUDA=True, 4x GPU |
| **vllm** | 0.21.0 |

### 3 项验证结果

1. `Models: 6, Homo panels: 2, Hetero panels: 5` — 符合预期
2. `JudgeService.unload()` → `True` — GPU 释放逻辑正常
3. `run_evaluation` 参数: `['model_ids', 'pairs', 'dataset_name']` — 符合预期

---
