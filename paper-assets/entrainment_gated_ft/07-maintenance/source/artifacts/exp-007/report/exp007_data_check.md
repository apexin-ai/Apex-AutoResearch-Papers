# exp-007 数据可用性检查报告

**日期**: 2026-05-19  
**目标**: 检查 340M / 1.3B 模型在 LAMBADA 上的 per-example logprob 数据是否可用

---

## 1. 340M Per-Example Logprob 数据

### lm-eval --log_samples JSONL: ❌ 不存在

`lm_eval_clean/340m/` 目录只有聚合 JSON 结果，无 `.jsonl` per-example 文件。

### 自定义 eval_logprob.py 产出: ⚠️ 部分存在

| 文件 | 覆盖模型 | 样本数 | 格式 |
|------|---------|--------|------|
| `analysis/lambada_per_example.csv` | GDN-pure, GDN-h12, HGRN2-pure, HGRN2-h3 | 5161 | CSV (doc_id, context_length, target, acc, logprob) |
| `analysis/lambada_matched_per_example.csv` | GDN-pure, GDN-h31, HGRN2-pure, HGRN2-h31 | — | CSV 同上 |
| `results/mvp_logprob/summary_logprob.json` | ALL 16 models × 5 depths | 500/model | 仅聚合统计（mean_correct_rank/logprob/margin），非 per-example |

**缺失**: 340M 全部 16 个模型都没有 lm-eval logsamples JSONL。CSV 只覆盖 4 个模型。

---

## 2. 1.3B Per-Example Logprob 数据

### lm-eval --log_samples JSONL: ⚠️ 部分存在

**已有 LAMBADA logsamples 的模型**:

| 模型 | 路径 | 样本数 |
|------|------|--------|
| GDN-h3-1 | `lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl` | 5153 |
| GDN-h6-1 | `lm_eval_clean/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl` | — |
| GDN-h24-1 | `lm_eval_clean/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl` | — |
| Transformer | `results_1.3b/lm_eval/transformer_baseline/.../samples_lambada_openai_*.jsonl` | — |
| RetNet-pure | `results_1.3b/lm_eval/retnet_pure/.../samples_lambada_openai_*.jsonl` | — |

**JSONL 格式确认**: 标准 lm-eval log_samples — 含 `doc_id`, `doc`, `target`, `resps` (logprob + bool), `perplexity`, `acc`。

**缺失的 1.3B 模型** (无 logsamples):
- GDN: pure, h12-1
- RetNet: h3-1, h6-1, h12-1, h24-1
- HGRN2: pure, h3-1, h6-1, h12-1, h24-1

---

## 3. 模型权重可用性

### 340M: ✅ 全部可用

路径: `/root/autodl-tmp/models/`

| 架构 | pure | h3-1 | h6-1 | h12-1 | h24-1 |
|------|------|------|------|-------|-------|
| GatedDeltaNet | ✅ | ✅ | ✅ | ✅ | ✅ (New) |
| RetNet | ✅ | ✅ | ✅ | ✅ | ✅ |
| HGRN2 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Transformer | ✅ baseline | — | — | — | — |

### 1.3B: ✅ 全部可用

路径: `/root/autodl-tmp/models_1.3b/`

| 架构 | pure | h3-1 | h6-1 | h12-1 | h24-1 |
|------|------|------|------|-------|-------|
| GatedDeltaNet | ✅ | ✅ | ✅ | ✅ | ✅ |
| RetNet | ✅ | ✅ | ✅ | ✅ | ✅ |
| HGRN2 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Transformer | ✅ baseline | — | — | — | — |

---

## 4. 结论

**exp-007 不能直接启动，需要先补跑 LAMBADA per-example 评估。**

### 需要执行的工作

| 规模 | 需跑模型数 | 说明 |
|------|-----------|------|
| **340M** | **16 个** | 全部模型都没有 lm-eval logsamples JSONL |
| **1.3B** | **11 个** | 缺 GDN pure/h12-1, RetNet h3-1/h6-1/h12-1/h24-1, HGRN2 全部 5 个 |

### 建议执行方案

```bash
# 340M: 在 westb-48145 上用 lm-eval 跑全部 16 个模型
# 1.3B: 补跑缺失的 11 个模型
# 均使用 --log_samples 参数，仅跑 lambada_openai task
lm_eval --model hf --model_args pretrained=<path> --tasks lambada_openai --log_samples --output_path <out>
```

预估时间: 340M 模型每个 ~2-3 min，1.3B 每个 ~5-8 min。总计约 **2-3 小时** (单 GPU 串行)。
