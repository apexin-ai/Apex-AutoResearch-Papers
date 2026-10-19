# exec download expert data

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_download-expert-data_20260512T140904_result.json`
- **Structured JSON:** [`bbfcdafd0817f9a3eff0.json`](../../sessions/bb/bbfcdafd0817f9a3eff0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**1. 下载成功**（Google Drive 受限，改用 HuggingFace Datasets 下载）。数据已放到 `/root/autodl-tmp/error_diag_dpo_recovery/eto_repo/data/`。

**2. Expert data 统计**
- 总量：**3,119 条** expert trajectories
- 格式：每条含 `id`, `game_file`, `conversations`（多轮 human/gpt 对话）
- Task type 分布：

| Task Type | Count |
|-----------|-------|
| pick_and_place | 759 |
| pick_two_obj | 662 |
| pick_clean_then_place | 576 |
| pick_cool_then_place | 472 |
| pick_heat_then_place | 371 |
| look_at_obj | 279 |

**3. Expert-Failure overlap**
- Expert unique trials: 3,119
- Failure unique trials: 61
- **Trial-level overlap: 56**（即 56 条 failure 轨迹能直接找到对应的 expert 轨迹，可构建 56 个 DPO pairs）

---
