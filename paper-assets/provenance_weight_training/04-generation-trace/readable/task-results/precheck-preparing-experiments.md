# precheck preparing experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_precheck_preparing_experiments_20260516T023929_result.json`
- **Structured JSON:** [`39969239883752455385.json`](../../sessions/39/39969239883752455385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成，结果如下：

---

✅ **contamination_60_tau07_seed42** — RUNNING cuda:0, 14% (831/6103), ETA ~3h20m，正常

✅ **grid_b0_3_seed42** — RUNNING cuda:1, 37% (2245/6103), ETA ~2h16m，正常

✅ **contamination_60_tau06_seed42** — 预检通过，数据 scored_data_60.jsonl (907M) / 模型 / output_dir 均就绪

✅ **grid_b0_1_seed42** — 预检通过，数据 scored_data.jsonl (930M) / 模型 / output_dir 均就绪

✅ **grid_b0_2_seed42** — 预检通过，数据 scored_data.jsonl (930M) / 模型 / output_dir 均就绪

---

⚠️ **GPU 占用情况**：4 卡全满，无法立即提交待提交实验

| GPU | 实验 | 进度 | 预计释放 |
|-----|------|------|----------|
| 0 | contamination_60_tau07_seed42 | 14% | ~3h20m |
| 1 | grid_b0_3_seed42 | 37% | ~2h16m |
| 2 | contamination_60_ess_only_seed42 | 87% | **~28min** |
| 3 | detect_remove_baseline_seed42 | 27% | ~2h36m |

GPU 2 最先释放（~28min），可按此顺序提交：GPU2 空出 → 提交第 1 个，GPU1 空出 → 提交第 2 个，GPU3 空出 → 提交第 3 个。

---
