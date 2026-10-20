# verify exp003 rrf dryrun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp003-rrf-dryrun_20260514T133114_result.json`
- **Structured JSON:** [`fa11cf91bd96cc0c7109.json`](../../sessions/fa/fa11cf91bd96cc0c7109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

### exp-003 RRF 聚合脚本：成功

| 模式 | 状态 | 输出 |
|------|------|------|
| `--signal-dir` 单模型 | 通过 | mmlu 14042 items, gsm8k 1319, arc_challenge 1172 |
| `--generate-exposure` 批量 | 通过 | 同上，exposure 范围 [0.0, 1.0] |

3 个信号中 `s3_constat` 为 null（未实现），`detect_available_signals` 正确跳过，实际使用 `s1_embedding`, `s2_minkpp`, `s4_selfcritique` 三路 RRF 融合。

### exp-003 → exp-006 数据管线：**不兼容**

exp-003 `--generate-exposure` 输出格式：
```json
{
  "Qwen2.5-0.5B_d000_s42": {
    "mmlu": {"exposure_scores": [0.021, ...], "item_count": 14042, "signals_used": [...]},
    ...
  }
}
```

exp-006 `load_exposure_scores()` 期望格式：
```json
{
  "mmlu": [0.021, ...],
  "gsm8k": [...],
  "arc_challenge": [...]
}
```

**两处不兼容：**
1. **嵌套层级** — exp-003 多了 `model_id` 这一层（因为它按模型聚合）。exp-006 按单次 fit 跑，每次只需一个模型的 exposure。
2. **值类型** — exp-003 的值是 `{exposure_scores: [...], item_count, signals_used}` 字典，exp-006 直接期望 `[floats]` 数组。

### 修复建议

在 `rrf_aggregation.py` 的 `generate_exposure_json` 中增加一个 `--flat-format` 选项（或在 exp-006 侧加适配），将输出转为 `{benchmark: [floats]}` 扁平格式。改动很小——对单个 model_id 取 `exposure[model_id][bench]["exposure_scores"]` 拍平即可。

---
