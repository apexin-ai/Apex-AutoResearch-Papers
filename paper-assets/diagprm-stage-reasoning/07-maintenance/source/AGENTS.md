## 当前项目
当前绑定项目：**diagprm-stage-reasoning**

## 按需查阅
- 项目配置：`load_project_config("diagprm-stage-reasoning")` 或 `load_project_config("diagprm-stage-reasoning", section="execution")`
- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
- 路线图：`read_roadmap()` 读取研究方向和短期任务
- 产出目录：`/home/ubuntu/.agent-ml-research-prod_0510/projects/diagprm-stage-reasoning/artifacts/`（写文件后用 `register_artifact` 注册）

## Worker 操作规范

### paper-writing-norms

# 论文写作风格规范

> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。

---

## 一、总体写作哲学

### 1.1 故事驱动，不是数据堆砌

- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing

### 1.2 主线统一性

- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线

### 1.3 专有名词必须有定义

- 首次出现的专有名词/缩写必须给出完整定义和解释
- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug

### 1.4 写作前必读同类优秀论文

- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
- 重点学：
  - Abstract 怎么用最少篇幅讲完故事
  - Introduction 怎么从大问题切入到具体贡献
  - Related Work 怎么 positioning 自己（不是 survey）
  - Table/Figure 怎么压缩信息密度
- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文

---

## 二、Abstract 写作规范

### 2.1 四个必答问题（150-250 words）

Abstract 必须在很短的篇幅内清楚回答：
1. **研究什么问题** — 1-2 句话交代背景和痛点
2. **为什么重要** — 现有方法的不足（不用写太多）
3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
4. **结果说明什么** — 用具体实验结论支撑贡献

### 2.2 禁忌

- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
- **缩写必须定义**：Abstract 中首次出现的缩写必须展开

### 2.3 审稿人视角检验

写完后用这个标准自检：审稿人能否在 30 秒内判断——
- 问题是否重要？
- 方法是否清楚？
- 贡献是否可信？
- 结果是否有说服力？

---

## 三、Introduction 写作规范

### 3.1 完整叙事线（5 段结构）

Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：

1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献

### 3.2 整体叙事结构

```
现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
```

### 3.3 禁忌

- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
- **禁止缺少过渡**：每段之间必须有逻辑连接
- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
- 每条 Contribution 必须有对应的 section/table 支撑
- Contribution 列表中不能出现未在前文铺垫过的概念

---

## 四、Related Work 写作规范

### 4.1 目标

让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。

### 4.2 结构要求

- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口

### 4.3 禁忌

- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
- **目标不是展示读了多少论文**，而是做归纳和比较
- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work

### 4.4 引用充足度

- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
- 任何一类缺失，审稿人会立刻看出来调研不充分
- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足

---

## 五、去 AI 写作风格（硬规则）

以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**

### 5.1 严禁破折号（最显著的 AI 痕迹）

**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**

- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
- 替代方式：用逗号、括号或拆分为两个句子
- 强制检查命令：
  ```bash
  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
  ```
- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）

### 5.2 段落与句式

- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容

### 5.3 用词黑名单

- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
- 避免 "in the realm of" / "in the context of" — 直接说
- 避免 "paradigm shift" / "novel" 过度使用

### 5.4 校对清单（4 步）

1. 全文 proofread 语法和拼写
2. 检查所有代词/指示词（this, that, it）是否指代明确
3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写

---

## 六、图表与视觉规范

### 6.1 知识密度原则

- **图表的信息必须紧凑**——不能为了美观而留大量白空间
- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
- 能用 inline text 说清的不要占一整个 Figure

### 6.2 表格规范

- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
- 小数精度全表统一
- 最优加粗、次优下划线
- Caption 必须自包含

### 6.3 图片规范

- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
- 图中字体 >= 7pt（打印后仍可读）
- 栏宽约束需匹配目标 venue 模板要求
- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页

### 6.4 空间效率

- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
- 优先使用 `\subfigure` 合并相关图
- Table 能 inline 就不要单独浮动
- 图表占比与其对叙事的贡献成正比

---

## 七、投稿前通用准备

### 7.1 模板必须官方（硬规则）

- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
- **不要用**：
  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
  - 组里学长留的旧版本（来源不明、无法追溯）
- 风险：
  - 样式不符合 → desk reject
  - margin 不对 → 被审稿人质疑诚信
  - reference 格式错 → 被认为不规范
- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致

### 7.2 投稿要求逐项核对

- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
- 页数限制：查目标会议官网
- 匿名化要求：review 版 vs camera-ready 版本设置不同
- 行号开启（review 版常需）
- 字体大小、margin 不得修改 sty 文件

### 7.3 最终修改 10 项检查流程

提交前必须逐一检查：
1. 所有最新实验结果已全部录入
2. 根据实验结果将叙事调至最优状态
3. 附录所有内容在正文中被引用且融入叙事
4. 无数据堆砌（每个数字服务于叙事推进）
5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
6. 全文主线统一（idea 变化后各章节逻辑一致）
7. 所有专有名词有定义
8. 无 AI 风格标志（dash、-ing phrases、过度分段）
9. 图表知识密度高、无视觉遮挡
10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础

## 更多 Skills（按需加载）

执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。

- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`
- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`
- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`
- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`
- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`
- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`
- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`
- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`
- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`
- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`
- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`
- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`
- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`
- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说"提取图"/"抽图"/"extract figures"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`
- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`
- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说"有什么新论文"/"最近进展"/"research news"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`
- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`
- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`
