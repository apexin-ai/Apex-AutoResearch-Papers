# debug specificity control check result

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_specificity_control_check_result_20260518T184329_result.json`
- **Structured JSON:** [`4d6a095907a6d850c523.json`](../../sessions/4d/4d6a095907a6d850c523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果报告：

## specificity_control_action 结果 — **Negative**

**总体：Bottom-24 d=0.565 vs Top-24 d=0.65，ratio=1.15**

Specificity 假设未通过：ablate 非 instruction heads（bottom-24）造成的 action shift 与 instruction heads（top-24）几乎相当，差异仅 13%。

### Per-task breakdown

| Task | Bottom-24 d | 对比 Top-24 d=0.65 |
|------|------------|-------------------|
| open_middle_drawer (cabinet) | **0.405** | 明显低，specificity 成立 |
| open_top_drawer_put_bowl | **0.628** | 接近，specificity 不成立 |
| push_plate_to_stove | **0.659** | 几乎相等，specificity 不成立 |

### 关键数字

- Paired MSE: 0.034 (p=1.86e-92)
- Token divergence: 0.598
- KL divergence: 4.166
- Control-8 heads (参考): d=0.41

### 解读

只有最简单的 cabinet 任务显示 specificity gap（d=0.405 vs 0.65）。更复杂的两个任务中，ablate 任意 24 heads 都造成相似幅度的 action disruption，说明 action shift 的大部分来源是通用的 capacity loss，而非 instruction-specific 通路被切断。

Registry 已更新为 DONE/negative，cron 已清理。

---
