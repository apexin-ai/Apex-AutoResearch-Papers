# d068: Guided Beam Search with Constraint Penalty (Pilot — Partial)

**Status**: 实验仍在运行中（~20% 完成），以下为中间结果。

## 实验设置

- **模型**: Qwen3-8B LoRA fine-tuned (scierc_merged)
- **数据集**: SciERC test.json (551 samples, 非预期的 100 docs)
- **解码**: beam search, num_beams=4, mode=full_s1
- **Beta 值**: 0.0 (baseline), 0.5, 1.0, 2.0
- **方法**: beam 候选生成后，按 `score = seq_score - beta * (dr_violations + cf_violations)` 重排
- **服务器**: westd-16980 (beta 0.0, 0.5), westd-21461 (beta 1.0, 2.0)

## 代码实现

`run_constrained_extraction.py:746-808` — `run_single_pass_beam()` 函数：
- beta=0 时等价于标准 beam search（只返回 top-1）
- beta>0 时返回所有 beam 候选，逐个解析并计算 violation 数量，用 penalty 重排后选最优

## 中间结果（~100-140 samples/551）

### Violation Rate

| Beta | Samples | Entity Violations | Relation Vocab Violations | D/R Violations | CF Violations |
|------|---------|-------------------|---------------------------|----------------|---------------|
| 0.0  | 103     | 0/344 (0.0%)      | 0/230 (0.0%)              | 0/230 (0.0%)   | 0             |
| 0.5  | 141     | 0/461 (0.0%)      | 0/310 (0.0%)              | 0/310 (0.0%)   | 0             |
| 1.0  | 105     | 0/363 (0.0%)      | 0/254 (0.0%)              | 0/254 (0.0%)   | 0             |
| 2.0  | 107     | 0/368 (0.0%)      | 0/256 (0.0%)              | 0/256 (0.0%)   | 0             |

**所有 beta 值的 violation rate 均为 0%**。fine-tuned 模型的 beam 候选中无一出现 constraint violation，因此 penalty re-ranking 无实际效果。

### F1 Scores

| Beta | Entity P | Entity R | Entity F1 | Relation P | Relation R | Relation F1 |
|------|----------|----------|-----------|------------|------------|-------------|
| 0.0  | 0.7310   | 0.7553   | **0.7429** | 0.5217    | 0.5687     | **0.5442**  |
| 0.5  | 0.6958   | 0.7344   | 0.7146    | 0.4581     | 0.5299     | 0.4913      |
| 1.0  | 0.7147   | 0.7725   | 0.7424    | 0.4685     | 0.5613     | 0.5107      |
| 2.0  | 0.7131   | 0.7676   | 0.7394    | 0.4688     | 0.5607     | 0.5106      |

beta=0.0（标准 beam search）在 Entity F1 和 Relation F1 上均最优。beta>0 的 penalty re-ranking 反而略微降低了 F1，但由于 violation=0，re-ranking 实际上只是因为返回多序列 + 重新解析引入了噪声。

### Latency

| Beta | Docs (at snapshot) | Mean (s) | Median (s) | Total (s) |
|------|-------------------|----------|------------|-----------|
| 0.0  | 106               | 10.54    | 9.19       | 1117.5    |
| 0.5  | 144               | 7.60     | 6.91       | 1094.6    |
| 1.0  | 109               | 8.61     | 7.69       | 938.3     |
| 2.0  | 111               | 8.21     | 7.30       | 911.1     |

beta=0.0 的 mean latency 最高（10.54s），可能是因为 `num_return_sequences=1` 时 beam 搜索实现与 `num_return_sequences=4` 时略有不同。各组 latency 差异不大。

## 初步结论

1. **Guided beam re-ranking 对 fine-tuned 模型无效**：模型已经学会了正确的 schema 约束，beam 候选中不存在 violation，penalty 项始终为 0
2. **F1 略有下降**：beta>0 时 F1 反而降低 2-5 个点，原因待查（可能是多序列解码引入的解析差异）
3. **该方法更适合 zero-shot / few-shot 场景**：在模型未经 fine-tune 时，beam 候选中可能出现 violation，此时 penalty re-ranking 才能发挥作用

## 待办

- [ ] 等实验跑完全部 551 samples 后更新最终数字
- [ ] 考虑在 zero-shot 模型上测试 guided beam，验证上述假设
