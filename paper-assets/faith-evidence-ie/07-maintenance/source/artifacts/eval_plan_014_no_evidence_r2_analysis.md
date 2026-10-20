# Eval: eval_plan_014_no_evidence_r2

## 状态：✅ 成功（EXIT_CODE=0）

## 配置
- 模型：Qwen3-4B + SFT no-evidence adapter (`/root/autodl-tmp/sft_no_evidence_output`)
- 数据：DocRED dev split, 985 documents, 12275 gold triples
- 模式：`no_evidence=true`, `quantize=false`
- batch_size=4, max_new_tokens=1024, seed=42
- 推理时间：6251.6s（~1h44m, 6.35 s/doc）
- W&B run ID：无

## Metrics

| 指标 | 值 |
|------|-----|
| **F1 (rel_f1)** | **0.4876** |
| **Ign-F1** | **0.4721** |
| Precision | 0.4901 |
| Recall | 0.4851 |
| Ign-Precision | 0.4654 |
| Ign-Recall | 0.4791 |
| TP | 5894 |
| Pred count | 12025 |
| Gold count | 12151 |
| Evi-F1 | 0.0000（预期，no-evidence 模式） |
| EDCR | 0.0000 |
| Format OK | 978/985 (99.3%) |
| Truncated | 307/985 (31.2%) |
| Total predictions | 21181 |

## No-Evidence 模式验证

✅ 确认生效。`config.no_evidence=true`，模型 raw_output 只包含 `{head, relation, tail}` 三元组，无 evidence 字段。eval 框架在 parsed_triples 中填充 `evidence: []`。evi_pred_total=0, n_evidence_valid=0, evidence_format_rate=0.0。

## Baseline 对比：Evidence Tax 量化

| 模型 | rel_f1 | Ign-F1 | 差异 |
|------|--------|--------|------|
| evidence-SFT (flat-NLI) | 0.4106 | — | baseline |
| **no-evidence SFT** | **0.4876** | **0.4721** | **+0.0770 (+18.8%)** |
| no-evidence 中间 eval (参考) | 0.4893 | — | 历史参考 |

**Evidence tax = 7.7 个 F1 点（相对下降 18.8%）。**

本次 rel_f1=0.4876 与之前中间 eval 报告的 0.4893 基本一致（差 0.0017），结果可复现。

## 关键发现

1. **Evidence tax 显著**：生成 evidence 使 rel_f1 从 0.4876 降至 0.4106，下降 7.7 个点。模型在生成 evidence 时占用 token 预算和注意力，影响关系抽取精度。
2. **Truncation 问题**：307/985 (31.2%) 的文档被截断。no-evidence 模式下截断率仍较高，说明 max_new_tokens=1024 对复杂文档仍不够。evidence 模式下截断会更严重。
3. **Precision-Recall 平衡**：precision=0.4901, recall=0.4851，两者接近平衡。
4. **格式合规率高**：99.3% 的输出可解析，SFT 效果好。

## 结论

**Positive result.** No-evidence ablation 成功量化了 evidence tax。加 evidence 生成后 rel_f1 下降 ~7.7 点是显著代价，为后续优化（分阶段生成、更长 context、evidence 压缩）提供了明确的改进目标。
