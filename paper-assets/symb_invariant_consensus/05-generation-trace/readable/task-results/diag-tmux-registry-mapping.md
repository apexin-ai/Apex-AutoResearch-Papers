# diag tmux registry mapping

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_tmux-registry-mapping_20260519T050158_result.json`
- **Structured JSON:** [`d442c65f1530ec3eb7e5.json`](../../sessions/d4/d442c65f1530ec3eb7e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌已清晰。

## 映射关系

| tmux session | Registry exp_id | 结果目录 | 状态 |
|---|---|---|---|
| `exp032` (已退出) | `exp-039-14b-pw600-16639` | `exp032_qwen25_14b_pw600/` | Registry 标记 **failed**，但实际 **已完成** |
| `exp033` (运行中) | `exp-040-qwen3-pw600-16639` | `exp033_qwen3_14b_pw600_nonthinking/` | 运行中 391/600 |

Registry `notes` 字段已明确记录了映射（"实际目录: exp032..., tmux: exp032"），没有 exp-039/exp-040 目录，因为实际路径用的是 exp032/exp033。

## 问题：exp-039 被误判为 failed

exp-039 的 cron hook 5 次检测不到 sentinel/W&B，自动标记为 failed。但实际日志显示实验完整完成：

**exp032 / exp-039 最终结果 (Qwen2.5-14B, ProofWriter-600)**:
- SICA: **71.5%** (429/600)
- SC: **73.5%** (441/600)
- Delta: **-2.0pp** (SC > SICA)
- Extraction rate: 99.2%
- Wall time: 659.6 min

## exp-040 进度

tmux `exp033` 当前 391/600，ETA ~362 min（约 6 小时），端口 8001 正常响应。

## 需要修复

exp-039-14b-pw600-16639 的 registry 条目需要更新：
1. `conclusion`: `failed` → `negative`（SC > SICA，delta=-2.0pp）
2. `status`: 保持 `DONE`
3. 添加 `metrics`: `{sica_accuracy: 71.5, sc_accuracy: 73.5, delta_pp: -2.0, n_problems: 600, extraction_rate: 99.2, wall_time_min: 659.6}`
4. 移除 `failure_reason`
5. 添加 `checkpoint_path` 和 `log_path`

是否需要我现在执行这个 registry 修复？

---
