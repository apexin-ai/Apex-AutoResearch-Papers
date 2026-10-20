# code exp 012 prep v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_012_prep_v2_20260515T124303_result.json`
- **Structured JSON:** [`4349956d3ba046ca9d60.json`](../../sessions/43/4349956d3ba046ca9d60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。4 条件 × 6 深度 × 500 样本 = 12000 条文本，全部正确加载。

汇报：

**脚本路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/exp012_ppl_depth_correlation.py`

**数据格式**: 每个 `depth_X.jsonl` 一行一条 `{"text": "...", "doc_id": N}`，每个 depth 5000 条。4 个模型条件分别在 `data/`、`data_exp001_pythia/`、`data_exp002_olmo/`、`data_exp017_qwen_cont/`。

**脚本功能**:
- 用 Qwen2.5-1.5B-Instruct（已缓存）计算 log-PPL
- 用 Pythia-1.4B（需下载 ~2.8GB）计算 observer PPL
- 计算 PPL ratio、Spearman ρ、pairwise AUC（对比已硬编码的 15D OBD 基线）、6-class 阈值准确率
- 输出 JSON + 终端 summary 表格
- 支持 `--max_samples`、`--batch_size`、`--dry_run` 参数

**预估 GPU 时间**: 默认 500 samples/depth 约 12-20 分钟（RTX 4090）。两个模型顺序加载，先跑完 ref 再释放显存加载 obs，24GB 显存充裕。

**注意**: Pythia-1.4B 未缓存，首次运行需下载。建议运行前先 `source /etc/network_turbo` 加速下载。

---
