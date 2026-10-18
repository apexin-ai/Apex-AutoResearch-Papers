# code wild data pipeline plan 015

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wild_data_pipeline_plan_015_20260517T143556_result.json`
- **Structured JSON:** [`0be5d7b82e6251db5b91.json`](../../sessions/0b/0be5d7b82e6251db5b91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**数据下载**
- `data/wild/c4_10k.jsonl` — 10,000 样本, 22MB (C4 en validation, seed=42)
- `data/wild/fineweb_10k.jsonl` — 10,000 样本, 31MB (FineWeb sample-10BT, seed=42)

**脚本**
- `scripts/wild_data_features.py` — 特征提取，复用 19-feature pipeline + Pythia-1.4B，输出 CSV
- `scripts/wild_data_eval.py` — RF 分类 + depth 分布统计 + bar chart 可视化
- `scripts/download_wild_data.py` — 数据下载脚本（C4 从本地缓存 gz，FineWeb 通过 hf_hub_download parquet）

**Dry-run 验证**
- 两个脚本 `--help` 均正常
- 数据格式正确（JSONL，含 text_id/source/text）
- 3 个 artifact 已注册

**Python 环境**: `/root/miniconda3/bin/python3.12`（numpy/torch/transformers/sklearn/datasets 均已安装）

**下一步运行特征提取**（需要 GPU）:
```bash
cd /root/autodl-tmp/recursive_gen_depth_est
/root/miniconda3/bin/python3.12 scripts/wild_data_features.py \
  --input data/wild/c4_10k.jsonl,data/wild/fineweb_10k.jsonl \
  --device cuda:0
```

---
