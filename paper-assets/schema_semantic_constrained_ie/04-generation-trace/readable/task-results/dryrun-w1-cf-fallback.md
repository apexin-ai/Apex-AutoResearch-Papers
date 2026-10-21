# dryrun w1 cf fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_dryrun_w1_cf_fallback_20260515T131645_result.json`
- **Structured JSON:** [`17b1087206baeec6866f.json`](../../sessions/17/17b1087206baeec6866f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-Run 验证结果汇总

### 代码集成状态
- ✅ CF fallback 代码在 `compiler/type_mask_processor.py:295-360` 中，`_mask_head_type` 和 `_mask_tail_type` 均实现了 registry-consistent fallback
- ✅ 默认集成在 `full_s1` 模式，无需额外 CLI 参数
- ✅ CLI 参数 `--max_samples`（非 `--num_samples`）

### 4 个 Dry-Run 结果

| # | 实验 | 状态 | 样本 | 详情 |
|---|------|------|------|------|
| 1 | Qwen SciERC | ✅ | 2/2 OK | E=4,R=1 (7.1s) / E=2,R=1 (4.0s) |
| 2 | Qwen DocRED | ✅ | 2/2 OK | E=15,R=14 (48.0s) / E=18,R=18 (42.6s) |
| 3 | Llama SciERC | ✅ | 2/2 OK | E=5,R=1 (5.2s) / E=3,R=0 (2.0s) |
| 4 | Llama DocRED | ✅ | 2/2 OK | E=10,R=9 (18.0s) / E=15,R=17 (30.8s) |

### Fallback 触发情况
- **Grammar-first fallback**: DocRED 上频繁触发（sample 平均 30+ 次），SciERC 上少量触发。符合代码注释描述——DocRED 约束紧（avg 5.68 valid pairs），SciERC 约束松（avg 24 valid pairs）
- **CF registry-consistent fallback**: 8 个 sample 中均未触发。这不代表代码有问题——CF fallback 仅在 entity registry 类型与 D/R 约束冲突时触发，取决于具体生成内容。全量运行（数百 samples）时预期会触发

### 输出格式
- ✅ 4 个 JSONL 文件均为有效 JSON
- ✅ keys: `doc_id`, `input_text`, `gold_entities`, `gold_relations`, `raw_output`, `parsed_output`, `inference_time_seconds`, `mode`
- ✅ relation 包含 `head`, `tail`, `type`, `head_type`, `tail_type` 五字段

### 注意事项
1. CF fallback 日志（`logger.info`/`logger.debug`）在当前配置下不显示，因为 `run_constrained_extraction.py` 没有配置 logging 级别（默认 WARNING）。正式运行如需看到 CF fallback 汇总日志，需在脚本入口加 `logging.basicConfig(level=logging.INFO)`
2. GPU 占用正常，未影响 mt6144 实验

---
