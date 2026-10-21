# NLI 语义门控验证 — 标注指南

## 任务说明

你将看到 100 对文本。每对包含一段**原文**和一段**改写文本**。你的任务是判断改写后的文本是否**保留了原文的核心含义**。

## 判断标准

**只关注语义内容。** 问自己："改写版本是否传达了与原文相同的关键信息、事实和观点？"

- **是（preserves_meaning = Yes）**：改写文本保留了核心含义。关键信息、事实性表述和主要观点都得到了保留。次要细节的少量省略是可以接受的。
- **否（preserves_meaning = No）**：改写文本丢失、歪曲或实质性改变了含义。重要信息缺失、被矛盾的内容替换、或被替换为不同的内容。

## 可以忽略的差异

以下差异**不影响**判断——只要核心含义不变，这些都是正常的：

- **风格差异**：正式/非正式、语气、学术/口语
- **长短差异**：改写版本可能更长或更短
- **用词差异**：用不同的词表达相同的意思
- **结构差异**：段落顺序调整、分段方式不同

## 示例

### 示例 1：是（含义保留）

**原文：** "The study found that sleep deprivation significantly impairs cognitive function, particularly working memory and attention span, in adults aged 25-40."

**改写：** "Research shows that not getting enough sleep really messes with your brain — especially your ability to remember stuff and stay focused. This was seen in people in their late 20s to early 40s."

**判断：是。** 核心事实内容完全一致（睡眠不足 → 认知功能受损 → 工作记忆 + 注意力 → 年龄段 25-40）。风格从正式变成了口语化，但含义没变。

### 示例 2：否（含义改变）

**原文：** "The algorithm achieves 95% accuracy on the test set but only 78% on out-of-distribution samples, suggesting limited generalization."

**改写：** "The algorithm performs well across all evaluation settings, demonstrating strong generalization capability with high accuracy scores."

**判断：否。** 原文强调的是泛化*不足*（95% vs 78%），而改写文本却声称具有*强*泛化能力。核心结论被颠倒了。

## 操作说明

- 每条判断大约需要 30-60 秒，请仔细阅读两段文本。
- 如果遇到不确定的边界案例，可以在"备注"栏中写下你的理由。
- 没有陷阱题，请相信你的直觉判断。
- 如果确实拿不准，倾向于选"是"（含义保留）。

## 额外判断：风格变化

除了"含义是否保留"之外，还需判断**是否能感受到明显的风格变化**（style_change_detected）：

- **是**：两段文本在风格上有明显不同（如正式↔口语、简洁↔冗长）
- **否**：风格差异不明显或几乎没有
