# ssh plan 014 postproc prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan-014-postproc-prep_20260515T024543_result.json`
- **Structured JSON:** [`c735686c1be72141069c.json`](../../sessions/c7/c735686c1be72141069c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 当前进度
- **plan-014 生成**: 595/996 seeds (~60%)，~15s/seed，预计 **~1.7h 后完成**（约 UTC 10:45）
- 已生成 416 行 JSONL，数据格式正确（seed_id, depth, text, model 字段齐全）

### 脚本已就绪
`/root/gen-depth-fingerprint/scripts/run_plan014_postproc.sh` 包含完整流水线：

| Step | 操作 | 预期耗时 |
|------|------|---------|
| 1 | 验证生成数据完整性（~4980 行） | <1s |
| 2 | 更新 `classify_multi.py` 的 `MODEL_FAMILIES`，添加 `qwen3-8b→qwen` | <1s |
| 3 | `extract_features_multi.py --model-name qwen3-8b` 增量提取特征，合并到 `features_all_models.csv` | ~30-60 min |
| 4 | `classify_multi.py --input data/features_all_models.csv` 运行 6 生成器 LOGO 评估 | ~2 min |

### 兼容性确认
- 数据格式完全兼容，`extract_features_multi.py` 的增量模式会自动发现 `data/qwen3-8b/generations_shard0.jsonl`
- `classify_multi.py` 的 LOGO 函数动态读取 `model_name.unique()`，无需硬编码生成器列表
- 唯一需要修改的是 `MODEL_FAMILIES` 字典（leave-one-family-out 评估需要），脚本已包含自动 patch

### 执行方式
生成完成后：
```bash
bash /root/gen-depth-fingerprint/scripts/run_plan014_postproc.sh
```
或用 nohup 后台执行（特征提取耗时较长）：
```bash
nohup bash /root/gen-depth-fingerprint/scripts/run_plan014_postproc.sh > /tmp/plan014_postproc.log 2>&1 &
```

---
