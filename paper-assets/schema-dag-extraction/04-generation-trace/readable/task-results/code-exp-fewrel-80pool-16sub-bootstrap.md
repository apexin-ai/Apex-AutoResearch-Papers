# code exp fewrel 80pool 16sub bootstrap

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_fewrel_80pool_16sub_bootstrap_20260516T014220_result.json`
- **Structured JSON:** [`08fb3ac853dc69b12504.json`](../../sessions/08/08fb3ac853dc69b12504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**脚本路径**: `/root/schema-dag-extraction/src/run_fewrel_80pool_16sub_bootstrap.py`

**Dry-run 结果 (preprocess stage)**:
- 数据: train+val 合并 56000 samples, 80 relations, 均衡采样 960 条 (12/rel)
- 80-rel sim matrix 加载成功 (80×80)
- 100 batches 生成完成，每 batch: 80→16 types→8 types

**BCS 分布** (mean pairwise cosine similarity):
| 指标 | 值 |
|------|------|
| Min | 0.4578 |
| Q1 | 0.5281 |
| Median | 0.5568 |
| Q3 | 0.5820 |
| Max | 0.6836 |
| Mean±Std | 0.5570±0.0438 |

**推理规模**: ~9600 total inferences, 预计 GPU 时间 ~19 min

**输出文件**:
- `artifacts/fewrel_80pool_16sub/preprocess.json` (305K) — 含 samples + batches + relation_defs
- `artifacts/fewrel_80pool_16sub/batch_config.json` (68K) — 100 batches 的 pool_16/types/BCS

**三阶段运行方式**:
```bash
# Stage 1 已完成（preprocess）
# Stage 2: GPU 推理
python3 src/run_fewrel_80pool_16sub_bootstrap.py --stage extract
# Stage 3: Bootstrap CI 分析
python3 src/run_fewrel_80pool_16sub_bootstrap.py --stage analyze
# 或一步到位:
python3 src/run_fewrel_80pool_16sub_bootstrap.py --stage all
```

支持 `--resume` 断点续传，每个 batch 推理后增量保存到 `results_incremental.jsonl`。

---
