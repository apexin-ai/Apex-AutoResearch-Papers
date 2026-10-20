# fix home val sweep hung

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_home-val-sweep-hung_20260514T062601_result.json`
- **Structured JSON:** [`13e0ab9f0ba171f48037.json`](../../sessions/13/13e0ab9f0ba171f48037.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

稳定运行中。160/9335，GPU 12.3/32.6 GiB（38%），充足余量。

---

**汇总：**

1. **卡死原因**：进程并非卡死，实际在正常推理（kill 时已到 5120/9335, acc=62.9%）。val_eval_results/ 为空是因为结果在每个 checkpoint 跑完才写盘。重跑时的 OOM 级联崩溃是因为残留 python 进程占了 17.9 GiB GPU 内存。

2. **修复内容**：
   - `eval_repo_cls.py`：添加 per-batch 120s signal timeout 安全网
   - `run_val_sweep.sh`：batch_size 16→8（避免 OOM），加 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`，加错误处理（失败自动清理残留文件），checkpoint 间加 3s sleep

3. **重跑状态**：已成功启动，checkpoint seed123/200 正在推理（160/9335, 12.3 GiB / 32.6 GiB）

4. **ETA**：~27 min/checkpoint × 13 = ~5.8h。第一个结果文件预计 ~00:00 出现。

需要我 25 分钟后检查第一个 checkpoint 是否完成吗？

---
