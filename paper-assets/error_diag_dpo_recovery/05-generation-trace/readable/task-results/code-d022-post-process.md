# code d022 post process

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d022_post_process_20260512T191159_result.json`
- **Structured JSON:** [`7d2f4350a3a2f56d80d7.json`](../../sessions/7d/7d2f4350a3a2f56d80d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## D022 CSF 后处理结果

### 创建的文件
- `src/post_process_trajectories.py` — CSF 检测和轨迹重分类脚本
- `src/classify_errors.py` — 已更新，加入 CSF 预过滤

### Dry-run 结果（321 条 v5 轨迹，数据仍在收集中）

| 分类 | 数量 | 占比 |
|------|------|------|
| true_success | 118 | 36.8% |
| **truncated_success (CSF)** | **1** | 0.3% |
| true_failure | 202 | 62.9% |
| └ 其中 CSF pattern 但任务未完成 | 58 | — |

**原始成功率: 36.8% → 真实成功率: 37.1%**（几乎没有变化）

### 关键发现

**truncated_success 极少（仅 1 条）**，原因：
- **pick_cool_then_place**：模型**从未成功执行 cool 操作**（0 条 "You cool" observation），30 条 CSF pattern 全部是假完成
- **pick_heat_then_place**：极少成功 heat，6 条 CSF pattern 都缺少 heat 步骤
- **pick_clean_then_place**：13 条 CSF pattern 大多跳过了 clean 步骤
- **pick_two_obj**：7 条 CSF pattern 通常只放了 1 个对象

58 条 CSF-pattern-incomplete 轨迹的共同特征：agent 认为自己完成了任务（进入 finish/exit 循环），但实际上**漏掉了关键中间步骤**（冷却/加热/清洁）或只完成了部分目标。这些仍然是 true_failure，但标记了 `csf_details` 字段供后续分析。

### classify_errors.py 更新
CSF 预过滤已集成。dry-run 验证：99 条失败 → 28 条 CSF 排除 → 71 条进入错误分类 → 57 条匹配到 expert 并完成分类。

---
