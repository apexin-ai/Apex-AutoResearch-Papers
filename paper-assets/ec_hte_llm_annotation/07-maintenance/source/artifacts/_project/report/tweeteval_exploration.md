# TweetEval 数据集探索报告

**日期**: 2026-05-20  
**目的**: 评估 CardiffNLP TweetEval 各子任务用于 EC-HTE 异质性处理效应分析的可行性

---

## 1. 数据集概览

TweetEval（Barbieri et al., 2020）包含 10 个 Twitter 文本分类子任务。数据来源为 `cardiffnlp/tweet_eval`（Hugging Face Datasets）。

### 1.1 各子任务样本量

| 子任务 | N_train | N_validation | N_test | N_total | 标签数 |
|--------|---------|-------------|--------|---------|--------|
| stance_feminist | 597 | 67 | 285 | 949 | 3 |
| stance_abortion | 587 | 66 | 280 | 933 | 3 |
| stance_atheism | 461 | 52 | 220 | 733 | 3 |
| stance_climate | 355 | 40 | 169 | 564 | 3 |
| stance_hillary | 620 | 69 | 295 | 984 | 3 |
| sentiment | 45,615 | 2,000 | 12,284 | 59,899 | 3 |
| hate | 9,000 | 1,000 | 2,970 | 12,970 | 2 |
| irony | 2,862 | 955 | 784 | 4,601 | 2 |
| offensive | 11,916 | 1,324 | 860 | 14,100 | 2 |
| emoji | 45,000 | 5,000 | 50,000 | 100,000 | 20 |

---

## 2. 标签分布

### 2.1 Stance 子任务（标签：none / against / favor）

| 子任务 | none | against | favor |
|--------|------|---------|-------|
| stance_feminist | 18.9% | 49.4% | 31.7% |
| stance_abortion | 27.1% | 54.3% | 18.6% |
| stance_atheism | 22.8% | 59.2% | 18.0% |
| stance_climate | 42.5% | 3.7% | 53.8% |
| stance_hillary | 25.8% | 57.1% | 17.1% |

**关键发现**：
- stance_climate 的 "against" 类仅 3.7%（13 条 train），严重不平衡
- 其余 stance 子任务均以 "against" 为主（49-59%）

### 2.2 其他子任务

| 子任务 | 标签 | 分布 |
|--------|------|------|
| sentiment | negative / neutral / positive | 15.5% / 45.3% / 39.1% |
| hate | non-hate / hate | 58.0% / 42.0% |
| irony | non_irony / irony | 49.5% / 50.5% |
| offensive | non-offensive / offensive | 66.9% / 33.1% |
| emoji | 20 个 emoji 类别 | ❤ 20.5% 最多，其余 2-11% |

---

## 3. 文本长度分布

| 子任务 | Mean | Median | Min | Max |
|--------|------|--------|-----|-----|
| stance_feminist | 106.1 | 114 | 34 | 139 |
| stance_abortion | 105.0 | 111 | 23 | 139 |
| stance_atheism | 106.8 | 111 | 34 | 140 |
| stance_climate | 101.4 | 106 | 33 | 134 |
| stance_hillary | 100.3 | 107 | 32 | 137 |
| sentiment | 106.9 | 113 | 10 | 200 |
| hate | 122.8 | 110 | 0 | 303 |
| irony | 77.9 | 77 | 4 | 998 |
| offensive | 124.7 | 101 | 7 | 580 |
| emoji | 71.0 | 76 | 6 | 142 |

**关键发现**：
- Stance 子任务文本长度集中在 100-140 字符（受旧 Twitter 140 字符限制）
- sentiment/hate/offensive 有更大变异，可能来自更新的推文
- irony 和 emoji 文本较短

---

## 4. 子群结构分析

### 4.1 文本特征分布（全部 splits 合并）

| 子任务 | N_total | Has # | Has @ | Has URL | ALL CAPS | Has Emoji |
|--------|---------|-------|-------|---------|----------|-----------|
| stance_feminist | 949 | 100.0% | 31.6% | 0.0% | 0.0% | 0.0% |
| stance_abortion | 933 | 97.2% | 38.2% | 0.0% | 0.0% | 0.0% |
| stance_atheism | 733 | 100.0% | 22.0% | 0.0% | 0.0% | 0.0% |
| stance_climate | 564 | 100.0% | 41.5% | 0.0% | 0.0% | 0.0% |
| stance_hillary | 984 | 97.8% | 59.9% | 0.0% | 0.0% | 0.0% |
| sentiment | 59,899 | 23.0% | 32.5% | 0.8% | 0.1% | 1.3% |
| hate | 12,970 | 31.3% | 41.8% | 1.1% | 0.7% | 6.9% |
| irony | 4,601 | 45.2% | 40.3% | 0.7% | 0.2% | 10.5% |
| offensive | 14,100 | 18.2% | 89.5% | 0.0% | 0.2% | 11.3% |
| emoji | 100,000 | 44.7% | 67.7% | 0.1% | 0.1% | 0.0% |

### 4.2 长度分组（基于 33/66 百分位数）

| 子任务 | 短文本阈值 | 长文本阈值 | Short | Medium | Long |
|--------|-----------|-----------|-------|--------|------|
| stance_feminist | ≤100 | ≤123 | 325 | 347 | 277 |
| stance_abortion | ≤98 | ≤122 | 315 | 312 | 306 |
| stance_atheism | ≤97 | ≤124 | 247 | 252 | 234 |
| stance_climate | ≤96 | ≤120 | 193 | 192 | 179 |
| stance_hillary | ≤93 | ≤118 | 336 | 329 | 319 |
| sentiment | ≤94 | ≤118 | 20,197 | 20,325 | 19,377 |
| hate | ≤87 | ≤137 | 4,327 | 4,398 | 4,245 |
| irony | ≤60 | ≤96 | 1,552 | 1,530 | 1,519 |
| offensive | ≤69 | ≤151 | 4,701 | 4,702 | 4,697 |
| emoji | ≤62 | ≤87 | 33,361 | 35,484 | 31,155 |

### 4.3 子群分析小结

**Stance 子任务**：
- 几乎所有文本都含 hashtag（97-100%）→ hashtag 不能作为有效子群变量
- URL、ALL CAPS、emoji 频率为 0% → 无法用作子群变量
- 仅 @mention 和文本长度可作为二分子群（有/无 mention），但 mention 占比在 22-60% 之间
- 子群变量极其有限

**sentiment / hate / offensive**：
- Hashtag 和 @mention 覆盖 18-90%，可作为有效二分子群
- URL 和 ALL CAPS 过于稀疏（<1%），不适合作为子群
- Emoji 在 irony (10.5%)、offensive (11.3%)、hate (6.9%) 中有一定比例
- 文本长度三分组较均匀

---

## 5. 数据示例

### stance_feminist
```
[against] @user @user is the UK's answer to @user and @user  #GamerGate #SemST
[none]    @user @user nah abi gonna get married to a rich white guy...
[favor]   RT @user Look for our latest indiegogo campaign coming out soon to help turn young girls into great leaders. #womensrigh
```

### stance_hillary
```
[against] If a man demanded staff to get him an ice tea he'd be called a sexists elitist pig.. Oink oink #Hillary #SemST
[none]    We're out here in G-town, and where are you  #sctweets #SemST
[favor]   If you're not watching @user speech right now you're missing her drop tons of wisdom. #SemST
```

### sentiment
```
[positive] "QT @user In the original draft of the 7th book, Remus Lupin survived the Battle of Hogwarts..."
[neutral]  "Ben Smith / Smith (concussion) remains out of the lineup Thursday..."
```

### hate
```
[non-hate] @user nice new signage. Are you not concerned by Beatlemania-style hysterical crowds...
[hate]     @user @user real talk do you have eyes or were they gouged out by a rapefugee?
```

---

## 6. HTE 可行性评估

### 6.1 样本量要求

EC-HTE 实验需要每个子群 × Z-level × treatment 组合有足够样本。假设：
- Z 二分为 2 个子群
- Treatment 有 2-3 个水平（不同 LLM prompt 策略）
- 最低要求：每 cell ≥ 100（理想 ≥ 500）

对于 2 子群 × 3 treatment = 6 cells：
- 需要 N ≥ 600（最低），理想 N ≥ 3,000

### 6.2 推荐度评估

| 子任务 | N_train | N_test | 标签数 | 推荐度 | 原因 |
|--------|---------|--------|--------|--------|------|
| **sentiment** | 45,615 | 12,284 | 3 | ⭐⭐⭐⭐⭐ | 样本量极充足；3类标签适合分类；子群变量丰富（hashtag 23%、mention 33%、长度均匀）；广泛使用的 benchmark |
| **hate** | 9,000 | 2,970 | 2 | ⭐⭐⭐⭐ | 样本量充足；二分类；子群变量可用（hashtag 31%、mention 42%、emoji 7%）；社会敏感话题，LLM 可能有 HTE |
| **offensive** | 11,916 | 860 | 2 | ⭐⭐⭐⭐ | train 充足但 test 仅 860；二分类；mention 占 90% 导致该变量不平衡；与 hate 互补 |
| **irony** | 2,862 | 784 | 2 | ⭐⭐⭐ | 样本量边缘可用；讽刺检测对 LLM 有挑战性，可能产生有趣 HTE；emoji 10.5% 可作子群 |
| **emoji** | 45,000 | 50,000 | 20 | ⭐⭐ | 样本量极大但 20 类标签使每类较少；emoji 预测任务与 HTE 研究主题不够匹配 |
| **stance_hillary** | 620 | 295 | 3 | ⭐⭐ | 政治话题最匹配 paper framing；但 N=984 总量太小，子群划分后每 cell <100 |
| **stance_feminist** | 597 | 285 | 3 | ⭐⭐ | 同上，政治话题相关但样本量不足 |
| **stance_abortion** | 587 | 280 | 3 | ⭐⭐ | 同上 |
| **stance_atheism** | 461 | 220 | 3 | ⭐ | 样本量最小之一；宗教话题有争议但 N 不足 |
| **stance_climate** | 355 | 169 | 3 | ⭐ | 样本量最小；"against" 仅 3.7%（13条），严重不平衡，无法有效分析 |

### 6.3 综合推荐

#### 首选方案：**sentiment**
- **优势**：N=45,615 train 远超需求；3类标签（neg/neu/pos）结构清晰；子群变量多样（hashtag、mention、长度）；学术界广泛使用
- **HTE 假设**：LLM 对含 hashtag vs 不含 hashtag 的推文情感判断可能有系统性差异；短文本 vs 长文本的准确率可能不同
- **建议采样**：从 train 中采样 3,000-5,000 条即可满足实验需求

#### 次选方案：**hate** 或 **offensive**
- **优势**：样本量充足（9K-12K）；二分类任务对 LLM 有挑战性（涉及社会偏见/价值判断）
- **HTE 假设**：LLM 可能对含 emoji/hashtag 的推文系统性高估或低估 hate speech；不同 prompt 策略可能产生异质性效应
- **注意**：这些任务涉及敏感内容，使用时需注意伦理考量

#### Stance 子任务的局限
- **核心问题**：所有 stance 子任务的 N < 1,000，子群划分后每 cell 仅 50-150 条，统计功效不足
- **子群结构贫乏**：几乎所有文本都含 hashtag，无 URL/emoji，只有 @mention 和长度可用
- **如果必须使用 stance**：建议合并多个 stance 子任务（total N ≈ 4,163），用"话题"本身作为一个子群维度，但需要额外验证跨话题合并的合理性

---

## 7. 建议的下一步

1. **使用 sentiment 子任务**作为主要实验数据集
2. 定义子群变量：
   - Z1: has_hashtag（23% vs 77%）
   - Z2: has_mention（33% vs 67%）
   - Z3: text_length（short/medium/long 三等分）
3. 从 train 中采样 ~5,000 条，保持标签和子群分布平衡
4. 设计 3 种 LLM annotation prompt 策略作为 treatment
5. 用 test set 作为 held-out 验证集

---

## 附录：原始数据文件

完整探索数据保存在 `results/tweeteval_raw.json`。
