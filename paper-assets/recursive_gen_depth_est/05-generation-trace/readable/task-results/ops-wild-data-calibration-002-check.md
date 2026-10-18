# ops wild data calibration 002 check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wild_data_calibration_002_check_20260516T011141_result.json`
- **Structured JSON:** [`ba4df8f8805fbca266f5.json`](../../sessions/ba/ba4df8f8805fbca266f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**wild_data_calibration_002: 失败**

| 阶段 | 状态 |
|------|------|
| Steps 1-2 (Tokenizer + RF训练) | 成功 |
| OpenWebText 加载 | 成功 (5000 passages, 23s) |
| **C4 加载** | **挂起** — `load_dataset("allenai/c4")` 调用后无任何输出 |
| Feature extraction / Classification | 未执行（或空结果） |

**根因**: `allenai/c4` HF streaming 在 AutoDL 代理环境下挂死。日志中无 error/exception/traceback — `load_dataset` 调用静默挂起，进程最终被终止。结果 JSON 存在但 `datasets` 和 `cross_model_consistency` 均为空。

**修复方向**: 重试时应将 C4 替换为另一个 wild dataset（如 `HuggingFaceFW/fineweb` 或 `RedPajama`），或给 `load_dataset` 加 timeout，或预下载 C4 数据到本地。

已更新 registry (status=DONE, conclusion=failed) 并删除 cron 监控。

---
