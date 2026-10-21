# Director Handoff — 2026-05-21

## 当前状态

论文经过 R24-R29 六轮内部审稿打磨，已达到 text-editing 收益极限。最新 commit 91288e2 包含 R29 quick fixes。

**论文审稿状态**：R29 审稿已提交（apr_20260521T164232_yyxq），推荐 continue 模式，等待用户审批。

**DDL**：EMNLP 2026 via ARR，2026-05-25（4 天）。

## 最近完成的工作

### R28 fixes (commit 87d3e5a)
- Abstract: "initial characterization" → "systematic empirical comparison"，7-8B 证据领衔
- Intro: C1 novelty 锐化 ("qualitative reversal in safety-critical application")
- Related Work: Tuned Lens 引用加为脚注
- Appendix: MLP 正则化细节 + ensemble Z.1 disclaimer 强化
- Limitations: HarmThoughts 是唯一有 step-level CP 标注的公开数据集
- Discussion 压缩 + enlargethispage 8→11，主文 8 页合规

### R29 fixes (commit 91288e2)
- Method 3.5: conditional inference caveat（"p-values are conditional on selected layer and window"）
- Method 3.3: CR-composite 设计动机
- Experiments 4.3: E5-Mistral 标注 "PCA-reduced to 384d"
- Discussion: 7-8B cross-validated vs 32B descriptive 区分
- Related Work + bib: 添加 Li et al. (2023) ITI + Levinstein & Herrmann (2024)

## 内部审稿分数轨迹

R24→R25→R26→R27→R28→R29: 3.5→3.5→3.0→3.5→3.0→3.0
用户明确指示："内部审核仅作参考，不代表真实水平"。

## 结构性限制（无法通过 text editing 解决）

1. **单数据集 (HarmThoughts)**：唯一有 step-level CP 标注的公开数据集，无法扩展
2. **3/4 Qwen 架构**：crossing-rate bias mechanism 是 Qwen-specific，仅 1 个 Llama 模型
3. **32B 统计效力不足**：n=19-20，nested CV 不可行

## review_issues.yaml 状态

跨轮次 issue tracker 已更新至 R29。关键 recurring issues：
- R26-N1 (conditional inference): 4 轮，R29 已加 caveat → 可标 resolved
- R23-N2 (3/4 Qwen): 7 轮，hedging 到位但结构性限制无法解决
- R22-W2/R23-N5 (单数据集): structural limitation，rebuttal ready

## GPU 状态

westd-15904 cuda:0 挂项目名下但 0% 利用率。**无补充实验计划**——结构性限制无法通过实验解决。建议释放或询问用户是否有其他用途。

## Reviewer 的关键判断（R29 评估）

Reviewer 判断当前论文已达 text-editing 收益极限：
- 进一步迭代边际收益趋近于零，且有引入 regression 的风险
- 真正值得做的已全部完成（MF1 conditional inference、MF2 E5 label、SF5 CR rationale、SF6 7-8B/32B 区分、missing refs）

## 下一步

1. **等待 R29 审稿审批**（apr_20260521T164232_yyxq）
2. **GPU westd-15904 处置**：向用户确认是否释放
4. **ARR 提交准备**：DDL 2026-05-25，论文 PDF 已编译合规（8 页主文）

## 不能做 / 不要再试的事

- 不要继续追求通过 text editing 提升内部审稿分数——已达极限
- 不要为了内部审稿的 recurring issues 做大幅 rewrite——用户说过仅作参考
- enlargethispage 已经 10+11=21 baselineskip，极度激进，不要再加
