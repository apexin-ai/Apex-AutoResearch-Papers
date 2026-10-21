# run mf4 seed experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mf4_seed_experiments_20260521T050755_result.json`
- **Structured JSON:** [`4ad2b25e2dd295570f20.json`](../../sessions/4a/4ad2b25e2dd295570f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

| 实验 | 状态 | 说明 |
|------|------|------|
| exp_conll_mf4_s123 | RUNNING (registry) / 等待模型 | rsync 未完成，auto_launch 脚本等待中 |
| exp_conll_mf4_s456 | RUNNING (registry) / 等待模型 | 同上 |
| exp_fewnerd_mf4_s42 | QUEUED | 等 FewNERD 模型 rsync 完成 |
| exp_fewnerd_mf4_s123 | QUEUED | 同上 |
| exp_fewnerd_mf4_s456 | QUEUED | 等 FewNERD 模型 + CoNLL s123 完成释放 cuda:2 |

**问题发现**：两个模型的 rsync 都还未完成。CoNLL 模型的 safetensors 文件只有 ~200MB（应为 ~4GB/shard），导致第一次提交失败（`SafetensorError: incomplete metadata`）。已部署自动启动脚本 (PID 998732)，模型就绪后自动按 GPU 分配启动全部 5 个实验。rsync 从 12:41 开始，预计还需 ~20-30 分钟完成。

---
