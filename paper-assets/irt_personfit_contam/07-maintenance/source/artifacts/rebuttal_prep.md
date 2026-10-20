# Rebuttal 预案 (Round 8)

基于 Round 7 评分 3.5/3.5，分析审稿关注点模式，预判最可能阻止升至 4.0 的三个追问。

## Q1: Practical deployment — "如何在实际场景中使用？"

3.5→4.0 最大瓶颈是 actionability。论文刻画了行为边界但未给出可操作的检测流程。Reviewer 会追问：practitioners 需要 clean baseline + per-model calibration + PSN-IRT 参数，部署成本过高，characterization 论文的实际影响力何在？

**回应草稿**: 我们的贡献定位为 characterization（刻画 IRT person-fit 的适用边界），而非 turnkey detection tool。实际部署价值在三层：(1) 为 benchmark maintainers 提供最低信息需求的 screening signal（仅需 binary responses，无需 logits/weights），适用于 Open LLM Leaderboard 等公开提交场景；(2) θ-shift absorption 发现直接指导 practitioners 使用 fixed-θ estimation 而非 free-θ，在高 baseline accuracy 模型上恢复 2.4× 检测力（Qwen 50% 污染: free-θ |d|=5.08 → fixed-θ |d|=12.32; Table 2 / results.tex:54,94）；(3) inverted-U 和 benchmark-size 交互为社区提供了 "何时该信任 person-fit 检测" 的定量指南（>1000 items + <25% contamination 为 sweet spot）。我们在 Discussion 中补充一段 3-step practical guideline（calibrate → detect → diagnose）。

## Q2: Model scale — "7B 之外是否成立？"

三个模型族全部为 7B 级别。Reviewer 会质疑：(1) 更大模型（70B+）baseline accuracy 更高→θ-shift absorption 更强→检测力可能崩溃；(2) 论文的 characterization 结论能否推广到 production-scale models。

**回应草稿**: θ-shift absorption 机制与 baseline accuracy 相关（Qwen 67.8% 吸收强 vs Llama 59.4% 吸收弱（results.tex:70,72）），这一机制在逻辑上 scale-invariant——更大模型若 baseline accuracy 更高则吸收更强，但 fixed-θ estimation 同样可恢复信号（原理不依赖模型规模）。我们的 ARC-C 实验中 Qwen 在该 benchmark 上 acc=89.7%（results.tex:59; 模拟 large model 高准确率场景），θ-fixed 仍恢复 d=5.30（results.tex:11）。我们承认 7B-only 是 scope limitation，但强调：(1) characterization findings（θ-shift mechanism, inverted-U shape）是 model-agnostic 的理论贡献；(2) 7B×3 families 的多样性（Qwen/Llama/Mistral 覆盖不同训练方法和 baseline accuracy range 59.4%–67.8%）已 span 了主要行为模式；(3) 计算资源限制下优先覆盖行为多样性而非单一规模维度。在 Limitations 中明确标注 scale generalization 为 future work。

## Q3: Privileged-access baselines — "与 MIA/Min-K++ 直接对比如何？"

论文定位为 "minimal-information operating point" 但未在相同 controlled contamination 数据上与 privileged methods 直接对比。Reviewer 会追问：(1) 同一 contaminated model 上 Min-K++/MIA 的 AUC vs lz* 的 Cohen's d，信息成本差异是否值得？(2) 特别是 post-RL 场景下（Wang et al. 2025 已证明 MIA 失败），lz* 是否有结构性优势？

**回应草稿**: 我们补充了 Min-K%/Min-K%++ 在相同 GRPO-contaminated Qwen 上的对比实验（exp-rebuttal-mia-grpo）。结果：MIA 方法在 post-RL 模型上 AUC≈0.5（与 Wang et al. 2025 一致），而 lz* seen/unseen pattern gap 仍为 ~3.3。更重要的是，这不是同层级对比——MIA 需要 token-level logits（privileged access），而 lz* 仅需 binary responses。我们的 detection frontier 框架（§1 Introduction, introduction.tex:12）按 information access level 排列所有方法：binary response < rephrased retest < token probabilities < full logits < model weights。lz* 定义了这个 frontier 的底端——在其他方法因信息不可得而无法应用时（如第三方提交到公开 leaderboard 的模型），lz* 是唯一可行选项。对比的 key takeaway：privileged methods 在 pre-RL 模型上更强，但 (a) 需要信息在多数实际场景中不可得，(b) 在 post-RL 场景下同样失效。
