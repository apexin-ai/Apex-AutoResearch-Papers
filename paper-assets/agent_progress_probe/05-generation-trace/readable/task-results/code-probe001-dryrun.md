# code probe001 dryrun

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe001_dryrun_20260514T071715_result.json`
- **Structured JSON:** [`8ec4c7993304d9f65e81.json`](../../sessions/8e/8ec4c7993304d9f65e81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完毕。data/ 目录恢复干净（已有真实数据文件：`swe_agent_trajectories_5000.jsonl`、`windows_labeled.jsonl`、`embeddings.ckpt.pt`）。

---

## Dry-run 验证报告

| 步骤 | 状态 | 说明 |
|------|------|------|
| **同步 train_probe.py** | PASS | 已 patch `--min_confidence` 参数和 confidence 过滤逻辑 |
| **生成 dummy embeddings** | PASS | 200 windows, 20 instances, conf 分布 1:87 / 2:74 / 3:39 |
| **Test 1: --min_confidence 2** | PASS | 正确过滤 113/200 windows，3 epochs 无报错，best_model.pt 生成 |
| **Test 2: --min_confidence 0** | PASS | 全量 200 windows，2 epochs 无报错 |
| **输出文件** | PASS | `best_model.pt`(5.3MB) + `split_info.json` + `train_history.json` 均生成 |
| **evaluate.py** | PASS | GRU Probe + 全部 4 个 baselines 评估完成，输出对比表格 |
| **清理** | PASS | dummy 文件已清除，不影响 emb_001 输出 |

**注意**：evaluate.py 需要 `--split_info`、`--windows`、`--trajectories` 三个额外参数，真实运行时需提供 `split_info.json`（train_probe.py 生成）、`windows_labeled.jsonl` 和 `swe_agent_trajectories_5000.jsonl`。data/ 目录已有这两个真实文件。

emb_001 完成后 probe_001 可零 debug 启动。

---
