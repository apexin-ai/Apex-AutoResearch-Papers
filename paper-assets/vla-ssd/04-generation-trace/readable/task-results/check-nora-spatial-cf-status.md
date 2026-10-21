# check nora spatial cf status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_nora_spatial_cf_status_20260523T164458_result.json`
- **Structured JSON:** [`e5796db9b038f99ea846.json`](../../sessions/e5/e5796db9b038f99ea846.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**运行状态：已完成。**

- 进程列表中没有 `nora_spatial_untrained_counterfactual.py` 在运行
- `counterfactual_combined.json`（36KB，最后修改 May 24 00:22）已生成完毕

**结果完整性：完整。**

- 配置：10 tasks × 10 demos × 50 timesteps，模型 `qwen25-vl-3b-base-untrained`，13 层分析
- 4 个 counterfactual conditions 全部完成：`wrong` / `empty` / `shuffled` / `paraphrased`
- 每个 condition 每层 n_samples = 5000（= 10 tasks × 10 demos × 50 timesteps），数据量正确
- JSON 结构完整，尾部有 `ranking_by_cosine_distance` 汇总

**关键结果预览**（mean cosine distance 排序）：

| Condition | Mean Cosine Distance |
|-----------|---------------------|
| empty | 0.0807 |
| shuffled | 0.0313 |
| paraphrased | 0.0047 |
| wrong | 0.0020 |

输出目录还有 3 个辅助文件：`action_r2_probing.json`、`cross_instruction_classification.json`、`l1_attention_profile.json`。

---
