# analyze plan 006 qwen3 1 7b rsft test

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan_006_qwen3_1_7b_rsft_test_20260517T195324_result.json`
- **Structured JSON:** [`fced5ce6bf9370562e58.json`](../../sessions/fc/fced5ce6bf9370562e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**状态: 推理成功完成 (EXIT_CODE=0)**，CodaLab 提交文件已生成，但存在两个显著质量问题。

### 输出文件
| 文件 | 大小 |
|------|------|
| `codalab_submission.json` | 2.5MB (27567 entries) |
| `predictions.json` | 8.6MB |
| `metrics.json` | 705B |

路径: `/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_test/`

### 关键数据
- 1000 docs 处理完毕，994 有预测输出，format OK 99.9%
- 推理耗时 3h (10.81 s/doc)
- Unique predictions: **15338**, 总条目 27567

### 两个严重问题

1. **截断率 85.7%** (857/1000 docs): `max_new_tokens=1024` 对 1.7B 模型不够，大部分文档关系预测不完整，recall 必然受损。

2. **重复率 44.4%** (12229/27567 条完全重复): 模型在生成过程中大量重复输出相同的 (title, h_idx, t_idx, r, evidence) 五元组，浪费 token 预算并加剧截断。

### 结论
文件可直接提交 CodaLab 获取 baseline 分数，但预期 F1 偏低。后续改进方向：增大 `max_new_tokens`、加 `repetition_penalty`、后处理去重。

---
