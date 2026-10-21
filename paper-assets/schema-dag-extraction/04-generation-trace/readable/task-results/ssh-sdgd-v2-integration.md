# ssh sdgd v2 integration

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sdgd-v2-integration_20260515T120937_result.json`
- **Structured JSON:** [`a67343bf6e94de292658.json`](../../sessions/a6/a67343bf6e94de292658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### sdgd_extract_gpu.py 修改
- 新增 `--merge_strategy` (union/confidence，默认 confidence) 和 `--confidence_threshold` (默认 -1.0) 参数
- confidence 模式下 `SamplingParams` 添加 `logprobs=1`
- 从 `output.outputs[0].cumulative_logprob / n_tokens` 提取归一化 confidence
- confidence 附加到每个 entity dict，合并阶段调用 `merge_with_confidence()`
- 结果 JSON 记录 `merge_strategy` 和 `confidence_threshold`
- 同时导入 `merge_with_confidence`，保留 `merge_all_samples` 用于 union 回退

### Decompose dry-run 结果
min_batch_size=8 生效：原始 8 个 batch（最小 3），合并后 4 个 batch（最小 14），分布均匀 [19, 18, 15, 14]。`graph_stats_before_merge` 字段保留了合并前的统计。

### 脚本
- `scripts/run_sdgd_v2_fewnerd.sh` — FewNERD, NER task, sim_matrix.pt
- `scripts/run_sdgd_v2_maven_minilm.sh` — MAVEN, event task, maven_minilm_sim_matrix.pt

两个脚本结构相同：Stage 1 CPU decompose（4 modes，sdgd_zero 带 min_batch_size=8）→ Stage 2 GPU extract（confidence merge）。`--help` 验证通过，新参数可正常解析。

---
