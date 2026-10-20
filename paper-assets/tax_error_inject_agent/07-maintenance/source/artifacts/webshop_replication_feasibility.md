# WebShop Replication 可行性调研报告

> 日期: 2026-05-16 | 目标: 评估 Claim 8 (WebShop 跨环境复制) 的可行性与 ROI

---

## 1. WebShop 环境概述

**论文**: Yao et al., "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents" (NeurIPS 2022)

**GitHub**: https://github.com/princeton-nlp/WebShop

**规模**: 1.18M 真实商品 + 12,087 条众包购物指令 + 1,600+ 人类 demonstration

### Action Space

仅 2 种动作类型（ALFWorld 有 ~13 种动词）：

| 动作 | 格式 | 说明 |
|------|------|------|
| search | `search[women jumpsuits]` | 搜索商品 |
| click | `click[B09QGK5XHZ]` | 点击元素（商品 ID、Buy Now、Back to Search、Prev/Next Page、属性选项、Desc/Overview） |

### Observation Format

4 种页面类型：
1. **Search page** — 搜索框
2. **Results page** — 商品列表（名称、价格、评分）
3. **Item page** — 商品详情（描述、属性、选项）
4. **Item-detail page** — 补充信息（完整描述）

两种渲染模式：
- **HTML mode**: 完整网页元数据
- **Simple/text mode**: 纯文本，适合 LLM 训练/评估

### Reward Function

程序化匹配评分，包含 4 个分量：
- **R_type**: 商品类别匹配（category path 重叠、标题关键词 overlap > 0.2）
- **R_attribute**: 语义属性匹配（材质、功能、风格等的满足比例）
- **R_option**: 选项匹配（颜色、尺码等）
- **R_price**: 价格约束满足

最终 reward = 上述分量的加权平均（在满足类别约束条件下），范围 [0, 1]。

### 已知 Baseline 成绩

| 方法 | Reward | Success Rate | 来源 |
|------|--------|-------------|------|
| Rule-based | — | 9.6% | WebShop 原文 (2022) |
| Best IL+RL | — | 29% | WebShop 原文 (2022) |
| ReAct (PaLM-540B, 1-shot) | ~62% | ~40% | ReAct (ICLR 2023), +10% abs over IL/RL |
| A³T Round 0 | 72.4% | 45.4% | A³T (EMNLP 2024) |
| A³T Round 3 | 73.9% | 49.0% | A³T (EMNLP 2024) |
| Human average | 75.5% | 50.0% | A³T |
| Human expert | 82.1% | 59.6% | WebShop 原文 |

### 安装复杂度

**依赖**: Python 3.8.13, Java 11 (OpenJDK), spaCy en_core_web_lg, FAISS (CPU), ChromeDriver (可选)

**数据**: 通过 Google Drive 下载商品数据 + 指令数据，需运行搜索引擎索引 (`run_indexing.sh`)

**RAM**: ~16 GB（加载完整商品数据库 + 搜索引擎）

**磁盘**: 预估 5-10 GB（1.18M 商品 JSON + Lucene 索引）

**复杂度评级**: 中等。比 ALFWorld 复杂（需要 Java + 搜索引擎），但有完善的 setup.sh 脚本。

---

## 2. GPT-5.2 Trajectory Collection

### ReAct 格式

WebShop 的 ReAct trajectory 格式（参照 ALFWorld 的 think-action-observation 模式）：

```
Instruction: I need a long-sleeve pink shirt for women, size M, under $30

Observation: [Search Page] Search bar available.
Thought: I should search for a long-sleeve pink shirt for women.
Action: search[long sleeve pink shirt women]

Observation: [Results Page]
[Back to Search]
Page 1 (Total results: 50)
[Next >]
[B09QGK5XHZ] Women's Long Sleeve Casual Pink Shirt - $24.99 ★★★★
[B08ABCDEFG] Women's Pink Blouse Long Sleeve - $18.50 ★★★
...
Thought: The first result looks promising and is under $30. Let me check it.
Action: click[B09QGK5XHZ]

Observation: [Item Page]
Women's Long Sleeve Casual Pink Shirt
Price: $24.99
Rating: ★★★★
Size: [S] [M] [L] [XL]
Color: [Pink] [White] [Blue]
[Description] [Overview] [Buy Now]
Thought: I need to select size M and color Pink.
Action: click[M]

Observation: [Item Page] ... Size: M selected ...
Action: click[Pink]

Observation: [Item Page] ... Color: Pink selected ...
Thought: All options match. Price is under $30. Buy it.
Action: click[Buy Now]

Reward: 0.85
```

### 与 ALFWorld 的关键区别

| 维度 | ALFWorld | WebShop |
|------|----------|---------|
| 每条 trajectory 步数 | 10-50 步 | **5-15 步**（更短） |
| 动作多样性 | ~13 种动词 × 多个宾语 | 2 种 (search/click) |
| Observation 长度 | 1-3 句 | **数十行**（商品列表/详情） |
| 子目标结构 | 多分支（找→拿→加工→放） | **线性**（搜→选→配→买） |
| 成功判定 | 二值（完成/未完成） | 连续 reward [0,1] |

### Trajectory 收集量估算

- **目标**: 500 条成功轨迹（与 ALFWorld 的 501 条对齐）
- **预估成功率**: GPT-5.2 on WebShop ≈ 55-65%（基于 A³T 用较弱模型达 ~50%）
- **需要尝试**: ~800-900 episodes
- **每条 trajectory token 数**: ~1,500-3,000 tokens（observation 较长但步数少）
- **总 token**: ~2M-2.7M tokens（input + output）

### API 成本估算

| 项目 | ALFWorld 实际 | WebShop 预估 |
|------|-------------|-------------|
| 成功 trajectory | 501 条 | 500 条 |
| 总尝试次数 | ~600 | ~850 |
| 每条 tokens | ~2,000 | ~2,500 |
| 总 tokens | ~1.2M | ~2.1M |
| API 费用 | $8.86 | **~$12-18** |

### 现成数据集

- **AGENTBANK** (EMNLP 2024 Findings): 50K+ trajectories 涵盖 16 tasks，含 WebShop。但数据格式是 GPT-3.5/4 生成，与 GPT-5.2 质量不同，且可能无法直接用于我们的 error injection pipeline。
- **A³T** (EMNLP 2024): 有 WebShop trajectory 数据，但 focus 是 self-training iterative refinement，格式未必兼容。
- **结论**: 没有现成可直接使用的数据集，需要自己收集。

---

## 3. Error Taxonomy 适配

### 逐个 Operator 分析

#### P1: Step Order Swap → ⚠️ 适用性低

**ALFWorld**: 动作序列有灵活性（可以先去 A 再去 B，或反过来），swap 后仍是"合理但错误"的 trajectory。

**WebShop**: 动作高度线性约束——必须先 search 再 click 商品，先选属性再 buy。多数 swap 会产生**语法上不合法**的序列（如在搜索前点击商品 ID），agent 无法理解而非需要"恢复"。

**适配方案**: 只能 swap 属性选择步骤（如先选颜色再选尺码 vs 反过来），但这种 swap 通常无害（不改变结果）。**有效 swap 空间极小。**

#### P2: Sub-goal Deletion → ✅ 部分适用

**ALFWorld**: 删除关键步骤（如跳过 heat/clean），agent 需要发现遗漏并补回。

**WebShop**: 可删除的子目标：
- 删除属性选择步骤（如跳过选颜色）→ agent 需发现产品配置不完整
- 删除搜索精化步骤（如跳过翻页）→ agent 可能买到不匹配的商品
- **不能删除 search 或 buy**（session 无法继续）

**适配方案**: 删除 option selection step。有效但场景有限（一个 trajectory 通常只有 1-3 个属性选择步骤）。

#### C1: Context Truncation → ✅ 适用

**ALFWorld**: 截断早期观察历史。

**WebShop**: 截断早期搜索结果、之前浏览过的商品信息。Observation 较长（商品列表），truncation 效果明显。

**适配方案**: 直接迁移，几乎无需修改。WebShop 的长 observation 反而让 truncation 更有意义。

#### C4: Observation Masking → ✅ 适用

**ALFWorld**: 将观察替换为 "You see nothing special."

**WebShop**: 将商品详情/搜索结果替换为空或通用文本。

**适配方案**: 直接迁移。可用 `"No results found."` 或 `"Page not available."` 替代 ALFWorld 的 generic observation。

### 适配总结

| Operator | ALFWorld 适用性 | WebShop 适用性 | 需要修改 | 备注 |
|----------|---------------|---------------|---------|------|
| P1 (step_order_swap) | ✅ 高 | ❌ 低 | 需重新设计 | 有效 swap 空间极小 |
| P2 (sub_goal_deletion) | ✅ 高 | ⚠️ 中 | 需适配 | 只能删 option selection |
| C1 (context_truncation) | ✅ 高 | ✅ 高 | 几乎不改 | 长 observation 更适合 |
| C4 (observation_masking) | ✅ 高 | ✅ 高 | 几乎不改 | 换 generic text 即可 |

### 是否需要新 Operator?

WebShop 特有的潜在 error operator：
- **S1 (search_query_corruption)**: 修改搜索 query（删关键词、加噪声）→ 影响搜索结果质量
- **A1 (attribute_swap)**: 替换已选属性（如选了 M 号但显示 L 号）→ 测试 agent 是否能检测

但新增 operator 会让跨环境对比变得不公平，**建议不新增**。

---

## 4. 工作量预估

### 详细分解

| 阶段 | 工作量 | GPU 时间 | API 成本 | 备注 |
|------|--------|---------|---------|------|
| 环境搭建 | 1-2 天 | 0 | $0 | Java + 搜索引擎 + 16GB RAM 需求在 AutoDL 上可行 |
| Trajectory 收集 | 2-3 天 | 0 | $12-18 | 500 条成功 trajectory |
| Error injection 适配 | 3-5 天 | 0 | $0 | P1 需重新设计，P2 需适配，C1/C4 小改 |
| SFT 数据构造 | 1 天 | 0 | $0 | 复用 formatter，适配 WebShop 格式 |
| 训练 (3 seeds × 3 conditions) | 2-3 天 | ~20-25 GPU-h | $0 | 9 runs, 每 run ~2.5 GPU-h |
| Eval | 1-2 天 | ~8-12 GPU-h | $0 | WebShop eval 需要运行环境服务 |
| 统计分析 + 整合 | 1 天 | 0 | $0 | |
| **总计** | **~12-17 天** | **~30-37 GPU-h** | **~$12-18** | |

### 风险因素

1. **环境搭建风险 (高)**: WebShop 需要 Java 11 + Lucene 搜索引擎 + ~16GB RAM。AutoDL 根分区 30GB 可能不够，需要把数据放 /root/autodl-tmp/。Python 3.8.13 要求可能与现有 conda 环境冲突。
2. **P1 operator 有效性 (高)**: WebShop 的线性 action space 让 step_order_swap 几乎无法产生有意义的错误。如果放弃 P1，taxonomy 从 4 operator 缩减到 3，跨环境对比不对等。
3. **Eval 环境依赖 (中)**: eval 时需要 WebShop 服务器持续运行（搜索引擎 + web server），占用额外 RAM 和 CPU。与 SFT 训练可能争抢资源。
4. **Reward 语义差异 (中)**: WebShop reward 是连续值 [0, 1]（属性匹配度），ALFWorld 是二值成功/失败。需要选择 threshold 或改用 reward mean，影响统计方法一致性。

---

## 5. 对论文 Story 的影响

### 正面

- **增强 generalizability claim**: 证明 TaxEI 不仅在 embodied planning (ALFWorld) 无效，在 web navigation (WebShop) 也无效 → negative result 更 robust。
- **不同环境特征**: WebShop 有 semi-structured observation 和 explicit reward，与 ALFWorld 的 free-text + binary success 形成对比。

### 负面/风险

- **Operator 不对等**: P1 在 WebShop 几乎无效，taxonomy 从 {P1,P2,C1,C4} 缩减为 {P2,C1,C4}，reviewer 可能质疑公平性。
- **Reward 语义不同**: ALFWorld 用 success rate (binary)，WebShop 用 reward score (continuous)，指标不直接可比。
- **投入产出比**: 12-17 天 + ~35 GPU-h，产出可能只是"另一个环境上的相同结论"。如果结果不一致（如 TaxEI 在 WebShop 上有效），反而会 complicate narrative。
- **GPU 预算压力**: ROADMAP 估算剩余 ~55 GPU-h，WebShop 占 ~35 GPU-h (64%)，挤压其他 Wave 2/3 实验。

---

## 6. 结论与建议

### 技术可行性: ✅ 可行，但 P1 operator 适配是硬伤

环境搭建和 trajectory 收集无技术障碍。C1/C4 可直接迁移。但 P1 (step_order_swap) 在 WebShop 的线性 action space 下几乎失效，导致 taxonomy 不完整，削弱跨环境对比的说服力。

### ROI 评估: ⚠️ 较低

| 投入 | 产出 |
|------|------|
| 12-17 天工作量 | 论文增加 ~1 页实验 |
| ~35 GPU-h (64% 剩余预算) | 强化 negative result 但无新 insight |
| ~$15 API 费 | 如果结果不一致反而 complicate story |

### 建议方案

**方案 A (推荐): 降级为 Discussion**
- 在 Discussion/Limitation section 用 1-2 段讨论 WebShop 作为 future work
- 分析 WebShop 与 ALFWorld 的结构性差异（线性 vs 分支 action space、continuous vs binary reward）
- 论证为什么 WebShop 的特征可能导致 TaxEI 同样无效（或可能有效）
- **成本: 0 天 / 0 GPU-h / $0**

**方案 B: 精简复制**
- 只做 C1 + C4（context operators），放弃 P1/P2（planning operators 在 WebShop 适用性差）
- 只做 full dose，不做 dose-response
- 3 seeds × 2 conditions (TaxEI-context vs Vanilla)
- **成本: ~8 天 / ~15 GPU-h / ~$12**
- **风险: 只用 2 个 operator 做对比，reviewer 可能认为 cherry-picking**

**方案 C: 完整复制**
- 如上文所述全流程
- **成本: ~15 天 / ~35 GPU-h / ~$15**
- **风险: P1 失效、GPU 预算紧张、结果可能 complicate narrative**
