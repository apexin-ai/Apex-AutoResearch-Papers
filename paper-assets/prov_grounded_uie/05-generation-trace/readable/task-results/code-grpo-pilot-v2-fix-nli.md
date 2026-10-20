# code grpo pilot v2 fix nli

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_pilot_v2_fix_nli_20260513T044531_result.json`
- **Structured JSON:** [`34fcfe4e5ee846d69bed.json`](../../sessions/34/34fcfe4e5ee846d69bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 执行总结

**Step 0 — 清理**: Kill 残留 dry-run 进程 (PID 84350)，删除 `grpo_v2_dryrun` 目录，GPU 1 释放。

**Step 1 — 代码修改**:
- `config.py`: iou_weight 0.5→**0.8**, nli_weight 0.3→**0.0**, w_provenance 0.4→**0.475**, w_structural 0.4→**0.475**, w_format 0.2→**0.05**
- `rewards.py`: `nli_w > 0` guard — 当 NLI 权重为 0 时跳过 NLI 模型加载和推理

**Step 2 — 验证**: import OK ✓

**Step 4 — Dry-run** (cuda:1, 2步):
- 无 OOM (peak 35.5GB/98GB)
- Reward 合理 (0.69~0.79)
- NLI 计算已跳过
- 每步 ~183s → 100步 ≈ **5.1小时**

**Step 5 — 收尾**:
- Dry-run 输出已删
- Registry `grpo_pilot_v2` → PENDING（含完整 spec 和 dryrun metrics）
- 飞书审批文档: https://feishu.cn/docx/ChNhde0c5oj4uJxFl87ccBqmn0f

等你审批后即可启动正式训练。

---
