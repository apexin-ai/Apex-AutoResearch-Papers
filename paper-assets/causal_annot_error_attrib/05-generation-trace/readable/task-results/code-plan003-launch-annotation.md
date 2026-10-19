# code plan003 launch annotation

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-launch-annotation_20260520T104327_result.json`
- **Structured JSON:** [`f91be5d13641dc6d5590.json`](../../sessions/f9/f91be5d13641dc6d5590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**执行摘要：**
- 服务器上 `annotate.py` 缺少三个修复，已直接在服务器上打补丁：
  1. **VAST dedup**：按 (text, topic, label_name) 去重
  2. **API retry 改进**：统一 429/5xx 处理，改善日志输出
  3. **HumAID column check**：低样本列预警
- 注意：保留了服务器原有的 `label_field: "label_name"`（本地版本改为 `"label"` 会取到整数，是错误的）
- 所有 3 个模型都走同一 API 网关（`http://47.94.22.126/v1`），只需 `OPENROUTER_API_KEY`，无需单独 DeepSeek key
- 管线已在 tmux session `plan003` 中启动，正在运行 27 组组合（3 datasets × 3 models × 3 prompts），每组 1500 samples
- 日志：`/home/sonny/causal_annot_error_attrib/plan003_run.log`
- Registry 已更新为 RUNNING

---
