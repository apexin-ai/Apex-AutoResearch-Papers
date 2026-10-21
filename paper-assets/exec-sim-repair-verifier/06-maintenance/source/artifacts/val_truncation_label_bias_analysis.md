# Val 集截断样本 Label 分布偏差分析

**日期**: 2026-05-12  
**数据**: `data/swebench_full/swebench_val.jsonl` (9335 samples)  
**Tokenizer**: Qwen3-4B, max_seq_length=2048, enable_thinking=False  

## 1. 截断 vs 非截断的 Label 分布

| Category | fail(0) | pass(1) | fail_rate |
|----------|---------|---------|-----------|
| Truncated (n=1883, 20.2%) | 697 | 1186 | **0.3702** |
| Non-truncated (n=7452, 79.8%) | 1555 | 5897 | **0.2087** |
| Overall (n=9335) | 2252 | 7083 | 0.2412 |

**偏差方向**: fail 样本被截断的概率显著更高（31.0% vs 16.7%），截断集中 fail 比例（37.0%）远高于非截断集（20.9%）。

## 2. Chi-squared 检验

| | fail | pass |
|---|---|---|
| Truncated | 697 (expected 454.3) | 1186 (expected 1428.7) |
| Non-truncated | 1555 (expected 1797.7) | 5897 (expected 5654.3) |

- **Chi² = 213.27, p ≈ 0, dof = 1**
- 截断与 label **高度显著相关**

## 3. Token 长度统计

| Group | mean | median | max |
|-------|------|--------|-----|
| Truncated | 4850 | 5418 | 9352 |
| Non-truncated | 970 | 881 | 1770 |
| Label=fail | 2092 | 898 | — |
| Label=pass | 1645 | 896 | — |

fail 样本平均 token 长度更大（2092 vs 1645），因为 fail 的 execution_output 通常包含详细的错误 traceback。

## 4. 按 Mutation Type 分解

| mutation_type | total | trunc | trunc% | fail% |
|---|---|---|---|---|
| gold | 4223 | 627 | 14.8% | 0.0% |
| mutation_operator_swap | 1783 | 628 | 35.2% | 44.3% |
| mutation_boundary_removal | 1401 | 0 | 0.0% | 40.8% |
| mutation_return_value | 999 | 159 | 15.9% | 73.9% |
| mutation_off_by_one | 929 | 469 | 50.5% | 16.5% |

### Mutation Type × Label 截断率

| mutation_type | fail_total | fail_trunc% | pass_total | pass_trunc% |
|---|---|---|---|---|
| gold | 0 | — | 4223 | 14.8% |
| mutation_boundary_removal | 572 | 0.0% | 829 | 0.0% |
| mutation_off_by_one | 153 | 12.4% | 776 | 58.0% |
| mutation_operator_swap | 789 | 79.6% | 994 | 0.0% |
| mutation_return_value | 738 | 6.8% | 261 | 41.8% |

**关键发现**: 截断偏差主要由特定 mutation type 驱动，而非 label 本身：
- `mutation_operator_swap`: fail 样本 79.6% 被截断，pass 样本 0% 被截断 → 极端偏差
- `mutation_off_by_one`: pass 样本 58.0% 被截断，fail 样本 12.4% → 反向偏差
- `mutation_boundary_removal`: 完全无截断（所有样本 < 2048 tokens）

## 5. 对评估的影响

1. **val loss 会低估 fail 样本的真实损失**：37% 的截断样本是 fail，但截断后 target（execution_output）被截尾，模型只需预测部分 output → loss 被人为压低
2. **fail 的 eval accuracy 可能被高估**：截断的 fail 样本 target 不完整，模型更容易"匹配"截断后的前缀
3. **不同 mutation type 受影响程度不同**：`mutation_operator_swap` 的 fail 样本几乎全被截断，该类别的评估基本不可信

## 6. 建议

- **短期**: 在 eval 报告中分离截断/非截断样本的指标，观察差异大小
- **中期**: 考虑增加 max_seq_length 到 4096（需要评估 GPU 内存），或对 execution_output 做智能截断（保留关键错误信息，去掉冗余 pytest 输出）
- **替代**: 不改 max_len 的话，可以对 val 集只保留 token_len ≤ 2048 的样本做"干净"评估，然后单独评估长样本
