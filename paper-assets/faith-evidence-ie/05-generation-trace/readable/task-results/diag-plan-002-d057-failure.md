# diag plan 002 d057 failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan_002_d057_failure_20260516T061247_result.json`
- **Structured JSON:** [`da44ad5b136cfd29c63e.json`](../../sessions/da/da44ad5b136cfd29c63e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 根因
DocRED `test.json` 有 1000 个文档但**无 `labels` 字段**（keys 只有 `vertexSet, title, sents`）。原 `DocREDProcessor.process("test")` 遍历 `doc.get("labels", [])` 构建 RelationSample → 返回 0 样本 → 0 predictions → 全部指标 0.0000。

**不是运行时错误，是代码逻辑不支持无 gold label 的 test split。**

### 代码修复状态
**已修好。** 当前 `inference.py` 已包含：
- `prepare_test_data()` (L148-195)：直接从 `vertexSet` 构建 entity list + prompt，不依赖 labels
- `convert_to_codalab()` (L198-250)：将预测转换为 CodaLab 提交格式
- `main()` 中 L420-427：`--split test` 时走 `prepare_test_data` 路径
- L454-460：test split 跳过 evaluate，生成 `codalab_submission.json`

### 资源就绪检查
| 资源 | 状态 |
|------|------|
| test.json | ✅ `/root/autodl-tmp/data/docred/test.json` (1000 docs) |
| RSFT CED s44 checkpoint | ✅ `/root/autodl-tmp/rsft_output_s44/checkpoint-510/adapter_config.json` |
| SFT adapter | ✅ `/root/autodl-tmp/sft_output` |
| Base model | ✅ `/root/autodl-tmp/models/Qwen3-4B` |
| GPU 3 | ✅ 0 MiB / 32607 MiB（空闲）|

### 修复方案：直接重新提交

代码已修好，只需重跑。遵循 D076 协议 + C001/C002 约束：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_ced_s44 --no-quantize"
```

### 预估 GPU 时间
Dev split (985 docs, batch_size=4, no-quantize) 约 2.5-3h。Test split (1000 docs) 类似，**预估 ~2.5-3h**。

### 产出
- `metrics.json`（含 n_documents, n_predictions, format_ok_rate 等，但无 F1——需提交 CodaLab）
- `predictions.json`（每文档详细预测）
- `codalab_submission.json`（CodaLab 提交文件，格式 `[{title, h_idx, t_idx, r, evidence}]`）

---
