# diagnose d158 14b ced score r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d158_14b_ced_score_r2_20260525T050940_result.json`
- **Structured JSON:** [`763512880e07d6703f87.json`](../../sessions/76/763512880e07d6703f87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验没有失败，是成功完成了。**

日志最后显示完整的 scoring 流程已跑完（24216/24216 records），并输出了最终统计报告：

- `rsft_scores.jsonl` — 83.7MB，全部 24216 条评分结果
- `rsft_train.jsonl` — 9.9MB，筛选后 3016 条训练样本
- `rsft_report.json` — 统计报告

### 关键产出指标

| 指标 | 值 |
|------|-----|
| 总记录 | 24216 (3027 unique docs) |
| 筛选后 | 3016 samples (12.5% selection rate) |
| mean f1_reward | 0.602 |
| mean ced_reward | 0.568 |
| mean combined_score | 0.668 |
| 截断样本 gap | trunc mean_f1=0.460 vs non-trunc=0.618, gap=0.157 |

### 当前 GPU 状态

- GPU 0: 14.1GB/97.9GB 在用 (PID 356446，可能是后续任务)
- GPU 1-3: 空闲

### 磁盘

- `/root/autodl-tmp/`: 84GB 可用 (77% used)

**结论**：CED scoring 任务已于 13:07 成功完成。wall_clock=4204s（~70分钟）是正常的处理时间（24216条记录，每500条约75秒）。如果 registry 标记为 failed，可能是退出码检测或超时阈值配置问题，而非实际运行错误。

---
