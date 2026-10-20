# analysis f1 stag traj length

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-traj-length_20260514T220222_result.json`
- **Structured JSON:** [`b32d589fec570b39a036.json`](../../sessions/b3/b32d589fec570b39a036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到服务器 `results/f1_stag_traj_length.json` 并注册为 artifact。

## 结果

Tercile 分界：short ≤ 8 windows, medium 9–18, long 19–144

| Bucket | Traj Range | #Traj | N_win | N_stag | F1_stag | Macro_F1 | R_stag | Err% |
|--------|-----------|-------|-------|--------|---------|----------|--------|------|
| short  | 1–8       | 191   | 375   | 88     | **0.8966** | 0.9327 | 0.8864 | 4.8  |
| medium | 9–18      | 175   | 599   | 155    | 0.8425  | 0.8958   | 0.7935 | 7.7  |
| long   | 19–144    | 177   | 850   | 242    | 0.8559  | 0.9008   | 0.8223 | 7.9  |
| **ALL**| 1–144     | 543   | 1824  | 485    | 0.8593  | 0.9055   | —      | —    |

**关键发现**：
- 短 trajectory（≤8 windows）F1_stag 最高 0.8966，错误率仅 4.8%
- 中等长度 trajectory F1_stag 最低 0.8425，主要因 recall_stag 掉到 0.7935（漏检 stagnation）
- 长 trajectory 反而略好于中等（0.8559 vs 0.8425），说明性能下降不是单调的
- 差异主要来自 recall_stag（短 0.886 → 中 0.794 → 长 0.822），precision_stag 三组接近（~0.89–0.91）

---
