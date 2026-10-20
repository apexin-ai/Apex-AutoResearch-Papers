# 叙事审查：D026/D027 新发现对 Paper Narrative 的影响

## (a) Claims 影响

### Claim 1（TaxEI 引入高方差，不改善性能）
- 当前表述：强调 cross-seed SD 2.6× 作为主效应
- **调整**：D027 揭示训练 loss 跨 seed 极稳定（SD=0.0004），方差完全来自 eval 端。应修改为"训练过程高度稳定但 eval 方差爆炸"——这比笼统说"training instability"更精确，也更有力：模型稳定地收敛到了错误的解。

### Claim 2（Taxonomy 标签特异性伤害多步协调任务）
- **强化**：D026 的 loop_repetition 数据（TaxEI 49 vs Vanilla 22 vs Random 6）提供了机制解释——taxonomy 标签导致 fixation，而多步协调任务对 fixation 最敏感。pick_cool (-19pp) 和 pick_two (-14pp) 的退化现在有了行为层面的证据支撑。

### Claim 3（注入增加训练不稳定性）
- **需重新表述**：D027 证明"训练不稳定"是误称。训练本身极稳定，不稳定性在 generalization 而非 optimization。建议改为："Error injection produces stable convergence to solutions that generalize unpredictably"。这是更深层的 negative result。

### Claim 6（任务结构边界条件）
- **强化**：D026 的 fixation 模式为"为什么 embodied planning 不适合 error injection"提供了新的机制论据——在开放动作空间中，fixation 比在有限 API 集合中代价更高。

### Claims 4, 5, 7, 8
- 不受 D026/D027 直接影响，无需调整。

## (b) Paper Framing 调整

### 核心叙事：需微调但不需重构
当前叙事"error injection 从 tool-use 迁移到 embodied planning 时失败"依然成立。D026/D027 不改变结论方向，但将叙事从"注入增加噪声"深化为"注入导致模型稳定地学到有害模式"。

**建议叙事升级**：
> 旧：Error injection destabilizes training（暗示优化问题）
> 新：Error injection produces stable but harmful convergence — models memorize injected patterns (lower training loss) while losing generalization to clean tasks, and develop behavioral fixation (2.2× loop repetition)

### "训练稳定 eval 不稳定"的呈现位置
- **§4 Results 的独立 subsection（§4.3 Training-Evaluation Paradox）**
- 核心数据：training loss TaxEI 50% = 0.259 vs Vanilla = 0.294（更低），但 eval TaxEI 50% = 56.0% vs Vanilla = 65.3%（更差）
- 配合 D027 的"初期难学但最终 overfit 更深"（avg loss 最高 → final loss 最低），构成完整的 memorization 证据链
- 文献锚点：Arpit et al. 2017 + Zhou et al. 2023 LIMA

### Loop repetition 发现的呈现位置
- **§5 Analysis / §5.1 Failure Mode Taxonomy**（Claim 6 的 subsection）
- 不适合放 Results（不是定量主实验），适合放 Analysis 作为机制解释
- 与 per-operator 分析（C4 唯一正向 +9.1pp）形成呼应：C4 是信息缺失型，fixation 代价低；P1/P2/C1 是序列错误型，fixation 直接致命

## (c) 8 页长文整合方案

建议 section 结构：

| Section | 内容 | 新发现整合 |
|---------|------|-----------|
| §1 Intro | 动机 + thesis | 加一句 teaser: "models stably converge to harmful solutions" |
| §2 Related Work | PALADIN, EEF, curriculum learning | 不变 |
| §3 Method | TaxEI 设计 + 实验设置 | 不变 |
| §4 Results | 主实验 + dose-response + recovery | — |
| §4.3 Training-Eval Paradox | **NEW** training dynamics 悖论 | D027 全部数据 |
| §5 Analysis | 为什么失败 | — |
| §5.1 Failure Mode Analysis | **NEW** 定性失败分析 | D026 loop repetition |
| §5.2 Task Structure Hypothesis | tool-use vs embodied 对比 | fixation 作为新论据 |
| §6 Discussion | 边界条件 + 启示 | per-sample loss（若完成） |
| §7 Conclusion | — | — |

**关键因果链**：
- D027 (§4.3) → D026 (§5.1) 形成因果链：模型 overfit 注入模式（§4.3 的 loss 证据）→ 行为上表现为 fixation（§5.1 的 loop repetition）→ fixation 在开放动作空间中致命（§5.2 的结构论证）
- Per-sample loss 实验（待运行）若确认 injected samples loss 更低，填补 §4.3→§5.1 之间的"模型具体学到了什么"环节

## (d) 审稿攻击面

### 攻击 1："Loop repetition 怎么定义的？阈值敏感吗？"
- **预防**：明确定义（连续 N 次相同动作），报告不同 N 下的计数，展示 TaxEI 在所有合理阈值下都显著高于 baseline

### 攻击 2："Training loss 更低可能是因为 TaxEI 数据量更大（9K vs 4K），不是 memorization"
- **预防**：dose-response 固定总量 4,358 的实验中同样出现此模式（50% injection final loss 最低）。数据量恒定时 paradox 依然存在

### 攻击 3："Loop repetition 可能是 generation length 的副产物，不是 fixation"
- **预防**：控制 generation length 后重新统计；或报告 loop_repetition / total_steps 比率而非绝对计数

### 攻击 4："训练 loss 稳定但 eval 不稳定，说明你的 eval 有问题，不是方法有问题"
- **预防**：Vanilla 的 eval SD 只有 3.3pp，同一 eval pipeline 下方差差异 2.6×。eval 本身不是问题源

### 攻击 5："Per-sample loss 分析是 post-hoc，容易 cherry-pick"
- **预防**：报告全部样本的 loss 分布（histogram），不只报均值；预注册分析计划（脚本已写好再跑）
