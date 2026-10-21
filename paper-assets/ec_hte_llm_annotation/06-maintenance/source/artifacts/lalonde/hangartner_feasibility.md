# Hangartner et al. (2021) Counterspeech RCT — 可行性报告

## 判定：❌ NO-GO

**原因：数据中不包含任何推文文本（tweet text）。** 所有 119 个变量均为预计算数值特征（BERT toxicity scores、VADER sentiment scores、keyword counts、用户元数据等）。无法对原始文本做 LLM 标注，核心前提不成立。

## 数据来源

- Harvard Dataverse: https://doi.org/10.7910/DVN/ARZ9PU
- 许可证：CC0 1.0
- 主数据文件：`main_dataset.tab`（1580 observations × 119 variables）

## 变量结构

### Treatment
- `treatment_main`：主 treatment 指标（1 = counterspeech, 0 = control）
- `treatment`：treatment 类型（"1D" 等，可能代表不同 counterspeech 策略）
- `treatment_dummy`：二元 treatment 虚拟变量

### Outcomes
- `post_HS` / `post_HSsum`：干预后 hate speech 指标
- `tox_bert_post`：干预后 BERT toxicity score
- `num_hate_tweets_post`：干预后 hate speech 推文数
- `deletion_rate` / `outcome_deleted_specific`：推文删除率
- 时间窗口细分：d0p/d1p（day 0/1 post）、w1p-w4p（week 1-4 post）

### Pre-treatment covariates
- `pre_HS` / `pre_HSsum`：干预前 hate speech
- `tox_bert_pre`：干预前 BERT toxicity
- 用户元数据：`followers_count`、`friends_count`、`statuses_count`、`lang`、`location` 等
- `anchor_*`：锚定推文特征（source, width, retweet, media, hashtag）—— 均为数值编码

### 样本量
- N = 1580（含 attrition）
- Treatment/control 分组需进一步统计，但大致平衡

## 关键缺失

| 需要 | 状态 |
|------|------|
| 推文原始文本 | ❌ 不存在 |
| 可供 LLM 标注的文本字段 | ❌ 不存在 |
| Hate speech 类型分类（explicit/implicit） | ❌ 仅有连续 toxicity score |
| 离散类别标签作为 effect modifier | ❌ 无 |

## 原因分析

Twitter/X 数据涉及用户隐私，论文作者在复制数据中完全去除了推文文本，只保留了预计算的 NLP 特征（BERT toxicity、VADER sentiment、keyword counts）。这是社交媒体实验数据公开的常见做法。

## 下一步建议

此数据集不适用于我们的 LLM 标注误分类 → 因果推断研究。需要寻找包含原始文本的 RCT 数据集。候选方向：
1. 有原始文本的 survey experiment 数据（如 open-ended responses + treatment）
2. 自然语言处理领域的 A/B 测试数据
3. 合成数据方案（用已知 DGP 生成带文本的模拟 RCT）
