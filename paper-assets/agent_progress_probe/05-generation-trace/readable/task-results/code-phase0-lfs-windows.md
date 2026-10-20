# code phase0 lfs windows

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0_lfs_windows_20260514T053644_result.json`
- **Structured JSON:** [`7c301262e571d277176a.json`](../../sessions/7c/7c301262e571d277176a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**产出文件：**
- `labeling_functions.py` — 3 个 LF 实现
- `window_extractor.py` — 滑动窗口提取 + 标注流水线
- `data/windows_labeled.jsonl` — 12,331 个标注窗口
- `label_statistics_report.md` — 统计报告

**关键数据：**

| 指标 | 值 |
|------|-----|
| 总窗口数 | 12,331 |
| LF1 (file_diff_delta) 覆盖率 | 82.7% |
| LF2 (test_pass_rate_transition) 覆盖率 | 0.3% |
| LF3 (outcome_backpropagation) 覆盖率 | 21.8% |
| LF 一致率 (≥2 非 abstain) | 58.7% |
| 高置信度 progress:stagnation | 98:1004 (10.2:1 不平衡) |

**注意事项：**
1. LF2 覆盖率极低——agent 很少在 10 步窗口内运行 ≥2 次测试，后续可考虑扩大窗口或替换为其他 LF
2. 高置信度标签严重偏向 stagnation（10:1），训练时需要 class weights 或过采样
3. Resolved 轨迹中 64.3% 标为 progress，Unresolved 中 53.6% 标为 stagnation——标签与 ground truth 方向一致，说明 LF 有区分力

---
