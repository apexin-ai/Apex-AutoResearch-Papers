# fix exp004 feat extract

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp004_feat_extract_20260515T221134_result.json`
- **Structured JSON:** [`e831e7504bef7df29c9e.json`](../../sessions/e8/e831e7504bef7df29c9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

**修复内容**：
- `scripts/run_exp004_qwen7b_depth.py` 的 `--scorer_path` 默认值从 `.../Qwen2.5-1.5B-Instruct` 修正为 `.../Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`（ModelScope 嵌套路径）

**正确的 scorer 路径**：
`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`

**恢复脚本**：`scripts/exp004_resume_feat.sh`
- 直接 import 主脚本的 `extract_all_features` + `run_analysis` 函数
- 只加载 1.5B scorer（不加载 7B generator），feat_batch_size=8
- 输出到 `results_exp004_qwen7b/`

**验证结果**：
- Scorer dry-run 通过：`Qwen2ForCausalLM, vocab=151665`
- 函数 import 通过
- 数据完整：6 depths × 5000 = 30000 samples

**预估时间**：feature extraction ~1-1.5h（1.5B 模型 + batch=8 + 30k samples），classification ~5min。

可以用 `submit_on_allocated` 提交 `bash scripts/exp004_resume_feat.sh`。

---
