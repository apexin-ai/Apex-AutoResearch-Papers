# code mvp features

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-features_20260514T165847_result.json`
- **Structured JSON:** [`a4c94e82e315de48fe2c.json`](../../sessions/a4/a4c94e82e315de48fe2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本 dry-run 全部通过。

**结果汇总：**

| 脚本 | dry-run 状态 | 说明 |
|------|-------------|------|
| `extract_features.py` | PASS | 加载 Pythia-410M → 提取 10 条文本的 entropy/tail_decay/ttr/hapax_ratio → 输出 features.csv (10×10) |
| `classify_and_eval.py` | PASS | 模拟 1000 条 → 3-class XGBoost → macro-F1=0.745, binary F1=0.873 → Verdict: PASS → 保存 mvp_results.json |

**注意事项：**
- `extract_features.py` 读取到了 `generations.jsonl` 中已有的 10 条数据（另一个 Worker 已开始写入），说明数据生成和特征提取可衔接
- 模型加载使用本地 snapshot 路径 + `local_files_only=True`，无需网络
- `torch_dtype` 有 deprecation warning（改用 `dtype`），不影响功能，正式运行时可修复

---
