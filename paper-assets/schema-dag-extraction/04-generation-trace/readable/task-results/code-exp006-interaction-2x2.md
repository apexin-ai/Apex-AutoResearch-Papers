# code exp006 interaction 2x2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_interaction_2x2_20260515T173024_result.json`
- **Structured JSON:** [`5251894b92ceb4d7e5b7.json`](../../sessions/52/5251894b92ceb4d7e5b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成状态

**脚本已就绪，未提交**（cuda:0 被 exp012 Llama-8B exp1 占用中）。

### 脚本位置
`/root/schema-dag-extraction/scripts/run_exp006_interaction.py` (cqa1-38874)

### Dry-run 验证结果
| Cell | Batches | BCS Range | Mean BCS |
|------|---------|-----------|----------|
| low_count (6) / low_bcs | 10 | [0.8327, 0.8454] | 0.8417 |
| low_count (6) / high_bcs | 10 | [0.9526, 0.9732] | 0.9615 |
| high_count (22) / low_bcs | 10 | [0.8993, 0.9103] | 0.9076 |
| high_count (22) / high_bcs | 10 | [0.9732, 0.9732] | 0.9732 |

共 40 batches × 1000 samples = 40,000 extractions。

### 提交命令（GPU 空闲后执行）
```
submit_training_job:
  server: cqa1-38874
  gpu_ids: ["cuda:0"]
  exp_id: exp006_interaction_2x2
  account: root
  timeout_hours: 3
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && FLASHINFER_DISABLE_VERSION_CHECK=1 python scripts/run_exp006_interaction.py --max_samples 1000"
```

### 设计要点
- 从 500 个随机 batch pool 中选 BCS 最低/最高各 10 个，确保 low/high BCS 有清晰分离
- 复用现有 `run_extraction` (vLLM + guided_json v2) 和 `evaluate_all` (text_match)
- 分析输出：4-cell mean F1、count/BCS main effects、interaction term (cross-difference) + z-test

---
