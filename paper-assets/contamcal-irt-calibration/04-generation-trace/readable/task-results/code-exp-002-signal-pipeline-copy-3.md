# code exp 002 signal pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-signal-pipeline_20260514T091323_result.json`
- **Structured JSON:** [`61f06289dbd9f5d5826d.json`](../../sessions/61/61f06289dbd9f5d5826d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

**exp-002 signal pipeline 代码已全部完成 + dry-run 验证通过。**

### 代码状态（9 个 Python 文件，1844 行）

| 模块 | 状态 |
|------|------|
| S1 Embedding (signal_embedding.py) | ✅ 已有 |
| S2 Min-K++ (signal_minkpp.py) | ✅ 已有，D016 合规 |
| S3 ConStat (signal_constat.py) | ✅ 已有 |
| S4 Self-Critique (signal_selfcritique.py) | ✅ 已有 |
| Main entry (compute_signals.py) | ✅ 已有 |
| RRF aggregation (aggregate_rrf.py) | ✅ 已有 |
| **Batch runner (run_batch.py)** | **✅ 新建** |

### 本次完成的工作
1. **新建 `run_batch.py`**（257 行）— 批量调度 9 个 tasks（3 dosages × 3 benchmarks），D016 合规，ConStat 自动跳过
2. **修复 offline mode** — 所有信号模块添加 `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1`，解决 AutoDL 上 HF 连接超时

### Dry-run 结果
- batch runner 2/2 tasks PASS（d005 × arc_challenge/gsm8k，GPU 1，~56 秒）
- 输出格式正确：per-item JSON with s1/s2/s3/s4 scores

### 生产运行
```bash
python run_batch.py --model-size 0.5B --gpu &lt;N>
```
预计 1.5-3 GPU-hours。正式提交由 Main Agent 调度。

---
