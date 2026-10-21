# code llama experiment prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_experiment_prep_20260514T132205_result.json`
- **Structured JSON:** [`60c3d88b6c2a816d633a.json`](../../sessions/60/60c3d88b6c2a816d633a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama-3.1-8B Dry-Run 验证结果

**状态**: GPU 0 上已有完整 unconstrained 全量实验在跑（PID 188372），60/551 样本已完成，0 解析失败。无需额外 dry-run，直接从运行中的实验提取验证数据。

### 关键指标（基于 53 样本统计）

| 指标 | 值 |
|------|-----|
| 平均推理时间 | **~2.9s/样本** |
| 最短 | 0.44s |
| 最长 | 6.19s |
| VRAM 占用 | **~16GB / 94GB** |
| 解析失败 | **0 / 60** |
| 估算全量 551 docs | **~26.6 min** |

### 验证通过项

- Llama-3.1-8B-Instruct 模型加载正常，16GB VRAM
- `run_constrained_extraction.py` unconstrained 模式正常运行
- 输出 JSONL 格式与 Qwen 一致：`doc_id`, `gold_entities`, `gold_relations`, `raw_output`, `parsed_output`, `inference_time_seconds`, `mode`
- 所有 60 个样本均成功解析（`parsed_output` 非 null），包含合理的 entities 和 relations

### 未验证

- **full_s1 模式**：GPU 0 被全量 unconstrained 占用，无法启动。需等当前实验完成后再测试。当前实验预计还需 ~24 分钟。

### 建议

全量 unconstrained 实验已在跑，无需干预。unconstrained 完成后可立即启动 full_s1 dry-run（3 样本）验证约束解码是否与 Llama 兼容。

---
