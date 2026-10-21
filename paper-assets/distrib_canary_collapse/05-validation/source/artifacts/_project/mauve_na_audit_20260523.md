# MAUVE N/A Audit (2026-05-23)

## 受影响的 generations

### T=15 s43 实验

| 实验 | 服务器 | gen 目录数 | 有 metrics.json | 受影响 gen | mauve 状态 |
|------|--------|-----------|-----------------|-----------|------------|
| t15_a060_s43_fp32_14b | westd-17855 | 14 (gen_0–13) | 13 (gen_0–12) | **无** | 全部有效值 |
| t15_a050_s43_fp32_14b | westd-17855 | 14 (gen_0–13) | 13 (gen_0–12) | **gen_0–12 (全部)** | 全部 null |
| t15_a045_s43_fp32_14b | westd-17855 | 12 (gen_0–11) | 11 (gen_0–10) | **gen_0–10 (全部)** | 全部 null |
| t15_a075_s43_fp32_14b | westd-19828 | 10 (gen_0–9) | 9 (gen_0–8) | **gen_0–8 (全部)** | 全部 null |

### T=10 s44 实验

| 实验 | 服务器 | gen 目录数 | 有 metrics.json | 受影响 gen | mauve 状态 |
|------|--------|-----------|-----------------|-----------|------------|
| t10_a045_s44_fp32_14b | westd-17855 | 5 (gen_0–4) | 4 (gen_0–3) | **无** | 全部有效值 |
| t10_a050_s44_fp32_14b | westd-17855 | 8 (gen_0–7) | 7 (gen_0–6) | **gen_0–6 (全部)** | 全部 null |
| t10_a060_s44_fp32_14b | westd-17855 | 8 (gen_0–7) | 8 (gen_0–7) | **gen_0–7 (全部)** | 全部 null |
| t10_a075_s44_fp32_14b | westd-19828 | 8 (gen_0–7) | 7 (gen_0–6) | **gen_0–6 (全部)** | 全部 null |

### 汇总

- **需补算 mauve 的 gen 总数**: 13 + 11 + 9 + 7 + 8 + 7 = **55 个 generation**
- **正常的实验**: t15_a060_s43 (13 gen 全部有效), t10_a045_s44 (4 gen 全部有效)
- **规律**: 每个实验内部要么全部有效、要么全部 null，说明 gpt2-large 缓存在实验启动时即确定

## metrics 文件格式

每个 `gen_X/metrics.json` 结构：

```json
{
  "token_entropy": 2.973,
  "self_bleu": 0.0116,
  "ece": 0.0081,
  "effective_rank": 52.67,
  "perplexity": 19.83,
  "distinct_1": 0.098,
  "distinct_2": 0.519,
  "distinct_3": 0.817,
  "mauve": 0.033,          // <-- 需补算的字段，当前为 null
  "generation": 0,
  "intervention_triggered": false,
  "trigger_gen": null,
  "effective_alpha": 0.6
}
```

## 补算输入数据

- 路径: `results/phase_diagram/<exp>/gen_X/synthetic_data/`
- 格式: HuggingFace Arrow dataset，单字段 `text` (string)
- 文件: `data-00000-of-00001.arrow` + `dataset_info.json` + `state.json`
- 加载: `datasets.load_from_disk("gen_X/synthetic_data/")`

## 补算建议

1. 先在服务器上缓存 gpt2-large（或从 ModelScope 下载到本地路径后设 `MAUVE_FEATURIZE_MODEL_PATH`）
2. 对 55 个 gen 批量运行 mauve 计算，参考文本用训练的原始 C4 数据
3. 将结果回填到对应 `metrics.json` 的 `"mauve"` 字段
4. 未完成 eval 的 gen（每个实验最后 1 个 gen 目录只有 `synthetic_data/` + `trainer/`，无 metrics.json）需等训练完成后一并处理
