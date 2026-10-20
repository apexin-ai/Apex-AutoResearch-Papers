# check a040 v2 exit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_a040_v2_exit_20260519T182329_result.json`
- **Structured JSON:** [`5ef1118697c3800a986a.json`](../../sessions/5e/5ef1118697c3800a986a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 诊断结论

**实验成功**：EXIT_CODE=0，10 generations 全部完成（gen_0-gen_10），wall_clock 4.26 GPU-hours。

## D105 MMCT 分析结果（α=0.40, Pythia-410M, WikiText, s42, fp32）

**Lead-lag 方法汇总：**
| 方法 | 显著/总计 |
|------|----------|
| PermG fwd | **0/8** |
| PermG rev | 0/8 |
| K≥4(3σ) | 1/8 |
| K≥3(3σ) | 6/8 |
| threshold_onset(3σ) | 8/8 |
| naive_xcorr | 8/8 |
| diff_xcorr | 3/8 |
| TY Granger | 4/8 |

**Onset boundary 含义：**
- α=0.25 → PermG=0/8, α=0.40 → PermG=0/8, α=0.50 → PermG=6/8
- **PermG onset 在 (0.40, 0.50) 区间**
- 但 α=0.40 已有明显 degradation drift（distinct 指标 -35%~-48%），K≥3=6/8 说明弱方法检测到信号，只是 PermG（最严格方法）尚未触发

**K≥4 唯一达标 pair：** ece→distinct_1（naive + diff + thresh + TY 共 4 票）

Registry 已更新为 DONE(success)，cron 已删除。

---
