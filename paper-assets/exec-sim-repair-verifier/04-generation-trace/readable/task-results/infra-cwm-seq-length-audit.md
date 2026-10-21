# infra cwm seq length audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cwm-seq-length-audit_20260518T134458_result.json`
- **Structured JSON:** [`38db3d076d018feb68ab.json`](../../sessions/38/38db3d076d018feb68ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到齐。

## 结论

| 项目 | max_seq_length |
|------|---------------|
| **Qwen3-8B CWM repo (65.17%)** | **2048** |
| **Qwen3-4B CWM repo (58.04%)** | **2048** |
| eval_repo_cwm.py 脚本默认值 | 8192 |
| GPU 1: DeepSeek CWM s42 (best) | 4096 |
| GPU 2 (D124): DeepSeek CWM s42 epoch2 | **8192** |
| GPU 3: DeepSeek CWM s123 | 4096 |

**关键发现：所有 Qwen canonical CWM repo eval (65.17% 和 58.04%) 用的都是 `max_seq_length=2048`。**

来源确认：
- 65.17% → `cwm_8b_ckpt400_test_merged/metrics.json`，所有 shard 日志和 JSON 都记录 `max_seq_length: 2048`（Qwen3-8B, ckpt-400）
- 58.04% → `results/repo_cwm_v12_conda_eval/eval_repo_cwm.json`，config 记录 `max_seq_length: 2048`（Qwen3-4B, ckpt-500）

D124 (GPU 2) 的 `seq_length=8192` 是非标准设置，比 canonical Qwen eval 的 2048 高 4 倍。`run_repo_eval.sh` 不传此参数（走脚本默认 8192），而 `run_8b_eval.sh` 默认用 6144。实际 canonical 结果都是手动指定或在之前某版脚本中硬编码的 2048。

---
