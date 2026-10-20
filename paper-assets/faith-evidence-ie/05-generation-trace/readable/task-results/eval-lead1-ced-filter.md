# eval lead1 ced filter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lead1_ced_filter_20260517T123015_result.json`
- **Structured JSON:** [`7b59fef110445f3c11f4.json`](../../sessions/7b/7b59fef110445f3c11f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

## CED Evidence Filter 运行结果

### --help 参数列表
| 参数 | 说明 |
|------|------|
| `--predictions` (required) | Path to predictions.json |
| `--data_dir` | DocRED 数据目录 (默认 /root/autodl-tmp/data/docred) |
| `--nli_model` | NLI 模型名/路径 |
| `--nli_device` | NLI 模型设备 |
| `--taus` | 过滤阈值列表 |
| `--output_dir` (required) | 输出目录 |

### 实际命令
```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.ced_evidence_filter \
  --predictions /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/predictions.json \
  --taus 0.3 0.5 0.7 \
  --nli_model cross-encoder/nli-deberta-v3-base \
  --output_dir /root/autodl-tmp/lead1_ced_filter_results
```
注意：需要 `source /etc/network_turbo` + `HF_ENDPOINT=https://hf-mirror.com` 才能下载 NLI 模型；默认的本地缓存路径已失效。

### 结果汇总

| 设置 | F1 | Ign-F1 | Evi-F1 | EDCR | Evidence Kept |
|------|-----|--------|--------|------|---------------|
| **Baseline** | 0.4601 | 0.4512 | **0.8063** | **0.6542** | 25246 (100%) |
| tau=0.3 | 0.4601 | 0.4512 | 0.7301 (-0.076) | 0.5797 (-0.074) | 15731 (62.3%) |
| tau=0.5 | 0.4601 | 0.4512 | 0.7297 (-0.077) | 0.5784 (-0.076) | 15632 (61.9%) |
| tau=0.7 | 0.4601 | 0.4512 | 0.7287 (-0.078) | 0.5776 (-0.077) | 15518 (61.5%) |

### 关键发现
- **F1/Ign-F1 完全不变**：CED filter 只移除 evidence 句子，不改变关系预测本身
- **Evi-F1 和 EDCR 反而下降**：过滤掉 ~38% evidence 后，Evi-F1 从 0.806 降到 ~0.730，EDCR 从 0.654 降到 ~0.578
- **tau 阈值敏感度低**：0.3/0.5/0.7 之间差异极小（保留率 62.3% vs 61.5%）
- Evi-Precision 大幅提升（0.80 → 0.90），但 Evi-Recall 大幅下降（0.61 → 0.61），整体 Evi-F1 净下降

输出保存在 `/root/autodl-tmp/lead1_ced_filter_results/`（含 filtered predictions、metrics 和 summary.json）。

---
