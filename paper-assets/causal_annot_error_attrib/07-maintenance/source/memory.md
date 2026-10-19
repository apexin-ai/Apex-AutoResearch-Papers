# Project Memory

## MVP 验证发现 (2026-05-20)

### Exposure DAG: bias-toward-null 保证在 K=3 下失效（核心发现）
**100k 随机 C 搜索：85% 违反 bias-toward-null，83.4% 产生符号反转。** 二分类 K=2 下全部满足 toward null 保证。

具体 named structure 结果：
- C3_STRUCTURAL_12: β_2=-0.5 → γ̂_2=+0.06（符号反转）
- C4_WEAK_DIAG: β_1=1.0 → γ̂_1≈0（近消失）
- C5_NEAR_PERM: β_2=-0.5 → γ̂_2=+1.25（符号反转 + 2.5x 放大，最极端）

**关键洞察**：exposure 误分类场景下，多分类 C 矩阵的交叉污染使得回归将某类的 Y 值归因到错误标签，产生符号反转。

### Dirichlet 子空间分析：高精度 LLM 仍有显著违反
即使 min(diag(C))≥0.9，amplification 违反率仍达 11.9%。符号反转随精度提高消失，但 amplification 稳定在 ~12%。

### Confounding DAG: 偏差方向性质
100k 随机 C 搜索均未发现负偏差。K=3 误分类偏差始终与 OVB 同向。

### DGP 参数
- Confounding DAG: P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma=1.0
- Exposure DAG: P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5], sigma_Y=1.0

## plan_001 完整 Taxonomy 结果 (2026-05-20)

### 结构性保证：τ sign_flip = 0% 跨所有拓扑和所有 τ 大小
**这是论文 Claim 1 的核心 positive result**。K=3 非差异性误分类改变 treatment effect 幅度但不翻转方向。小 τ (0.05, 0.1) 确认是结构性的。Exposure DAG 是唯一例外（83.4% sign reversal）。

### 拓扑行为分层
- **Mediation/Front-door**: violation ≈100%, amplification ≈100%, misclass_amplifies ≈100% — 最受影响
- **Collider**: misclass_amplifies = 0% — 误分类减弱 collider bias（独特）
- **M-bias**: violation 53.2%, amplification 10.4% — 最鲁棒
- **Exposure**: sign_flip 83.4% — 唯一翻转拓扑（C 直接作用于 design matrix）

## plan_002 K=5,7 扩展结果 (2026-05-20)

### Sign_flip 随 K 恶化（核心发现）
**K 增大引入更多错分模式，符号反转概率系统性上升**：
- Mediation: 83.8%(K=3) → 96.6%(K=5) → **100%(K=7)**
- Collider: 66.6%(K=3) → 95.5%(K=5) → **99.2%(K=7)**
- Confounding/Exposure: K=3 已近饱和，K=5,7 达 100%

### 但 worst-case bound 和 bias 均值反而下降（除 exposure）
**反直觉的 nuance**：高精度约束(diag≥0.9)下，K 增大每个 off-diagonal 元素分摊更小 → confounding worst-case 从 0.162(K=3) 降至 0.092(K=7)。**唯一例外是 exposure**（0.253→0.282），因为 exposure 的 bias 来自 design matrix 的交叉污染，不受对角占优约束的同样保护。

### Eigendecomposition：bias 方差随 K 分散
Top-1 PC 解释 bias 方差的比例：78%(K=3) → 67%(K=5) → 61%(K=7)。K 增大后 bias 不再集中在单一方向，增加了诊断和校正难度。

### 对论文 story 的影响
Claim 1 证据链完整：plan_001(K=3 taxonomy) + plan_002(K scaling) + plan_008(binarization collapse)。可 claim "K 增大使符号反转风险恶化，practitioners 处理高 K 分类任务时风险更大"。

## plan_008 Binarization Collapse 结果 (2026-05-20)

### 拓扑依赖性：折叠偏差跨度 150 倍
IV (Δ_mean=0.926) > Exposure (0.516) >> Mediation (0.045) > Confounding (0.025) > Collider (0.017) > M-bias (0.006)。Sign flip 只在 IV (17.5%) 和 Exposure (14.0%)。plan_001 和 plan_008 的拓扑危险性排序一致。

## plan_004 ASV 框架结果 (2026-05-20)

### v2 发现 + v3 修正
v2 问题：(1) 单调性 75% 违反 (2) sign-flip ASV 对 confounding/mediation 返回 None

v3 修正（D007 + Director magnitude 阈值修正）：
- **Envelope monotonicity**: violations = 0（构造性保证）
- **Magnitude ASV (10% relative threshold)**: 对所有拓扑有信息
  - τ=0.5: 0.076–0.487（部分 C₀ 下安全）
  - τ=0.1: 0.014–0.093（不安全）
  - τ=0.05: 0.008–0.047（极不安全）
- **关键洞察**：小 τ ASV << 1 = LLM 标注误差对小效应因果推断不安全 → 连接 Claim 3 correction 需求
- **Type I/II (小 τ)**: ASV-informed 正确保守（H₁ 下 0% 拒绝，因为 ASV<1 → 标记不安全）

### ASV 三类定义（最终版）
1. **Sign-flip ASV**: min δ 使 sign 翻转（Exposure 专用，其他拓扑 = None）
2. **Magnitude ASV**: min δ 使 |bias| > 0.1×|τ̂|（通用，所有拓扑有信息）
3. **Significance ASV**: min δ 使 |plim τ̂(C(δ))| < 1.96×SE（假设检验 filter）

## plan_005 ASV 扩展结果 (2026-05-20, fixed)

### 6 拓扑 ASV 全覆盖（Reviewer CRITICAL 修复后）
修复 4 点：C1 significance ASV 函数 + C2 magnitude τ≈0→0.0 + W1 IV τ_true=plim(I)=0.6598 + W2 M-bias τ_true=plim(I)=0.5128

### τ_true 必须用 plim(I) 而非 DGP 参数
**设计决策**：ASV 衡量 annotation error **额外引入**的 bias，不含估计量固有的多类别污染。因此 τ_true = plim(C=I)，不是 DGP 直接参数。IV plim(I)=0.6598≠β₁=0.5；M-bias plim(I)=0.5128≠τ=0.5。Front-door 已正确。

### Significance filter Type I/II（修复后）
| 拓扑 | Type I | Power τ=0.05 | Power τ=0.1 |
|------|--------|-------------|-------------|
| M-bias | 0% | 95.8-99.2% | 100% |
| IV | 0% | 0% | 0% |
| Front-door | 0% | 100% | 100% |

- **IV power=0% 是正确的**：Wald 估计量极脆弱，signif_ASV≈0（annotation error 立即摧毁 significance），ASV filter 保守阻止所有拒绝。对 IV，应改用 magnitude ASV 报告脆弱性
- **M-bias 高 power**：误分类减弱 spurious bias，不影响真实效应的检测
- 与 plan_004 confounding/mediation/collider 结果合并 → 6 拓扑 significance filter 完整验证

## plan_007 Correction Guidance 结果 (2026-05-20)

### PPI++ 全面碾压（Claim 3 核心支撑）
Grand mean: bias_red 93.8%, coverage 96.8%, win rate 95.2% (40/42 scenarios)。唯一满足名义 95% coverage 的方法。

### Frisch-Waugh 不变性：理论到实证完全验证
naive_plugin 和 MLA 在 OLS 拓扑（confounding/mediation/collider/mbias）下 bias_red 精确 0.0%。原因：C⁻¹ 变换 dummy matrix 不改变 [intercept, D*] 的列空间，T 系数 OLS 估计不变。
但在 exposure/iv/frontdoor 下两者显著恶化（-40% ~ -113%），因为这些拓扑的估计量不是简单 OLS on T → FWL 不适用。

### DSL 拓扑敏感性（新发现，可作为 contribution）
DSL 仅在 confounding (49.8%) 和 mediation (70.3%) 有效——这两种拓扑 misclassification error 主要通过 dummy 系数传播，DSL 的 EM 迭代能捕获。其余 5 拓扑系统性失败，最差 mbias -768%。**失败原因是结构性的，非个别 C 问题。**

### PPI++ 的阿喀琉斯之踵
mbias + realistic_llm: bias_red = -25.1%（恶化），但 coverage 99%。说明 PPI 的置信区间正确反映了增大的不确定性，bias 校正本身失效。论文应诚实报告此弱点。

### MC-SIMEX 不稳定
Grand mean 20.9%，在 iv (64.7%) 尚可但 frontdoor (-55.7%) 崩溃。不适合作为通用推荐。

## plan_006 ASV 实证校准 — humaid 先行结果 (2026-05-20)

### 真实 LLM confusion matrices (K=10, HumAID)
- deepseek 最好（mean_diag 0.724），qwen3 次之（0.710），llama4 最差（0.678）
- Class 6 ("other_relevant_information") 是所有模型的主要混淆目标
- Macro F1: 0.614–0.690（全部 <0.93，K=10 高难度任务）

### 理论-实证一致性验证
- ✅ IV 最脆弱（12-42% bias）— 与 plan_005 signif_ASV≈0 一致
- ✅ Collider 最稳健（4-6% bias）— 与 plan_001 misclass_amplifies=0% 一致
- ✅ Magnitude ASV 仅触发 mediation/exposure/IV/frontdoor，与理论预测吻合
- ✅ 0 sign flips — K=10 真实 LLM C 对角占优仍保护符号

### Inter-model error independence
Error correlation 0.05-0.16（低），Kappa 0.39-0.49（fair-moderate）。模型犯错较独立 → 对 PPI++ 有利。

### ASV filter 过于保守
ASV-unsafe 49.2%，但 unsafe 时 power 直接归零。实际应有梯度式衰减——这是方法论改进方向。

### 待补充
需 vast (K=3) + civil_comments (K=2) 数据验证 Baumann claim (F1>0.93 仍有风险) 和 K 值对比。

## plan_009 Pathological Matrices 结果 (2026-05-20)

### 3 风险层级
- **Low risk**: mbias (mean_bias 0.006-0.039)
- **Medium risk**: confounding/mediation/collider/frontdoor (R²=0.70-0.77, condition_number 最一致预测因子)
- **High risk**: exposure/IV (不可预测，R²低)

### IV 过滤问题
3000/28000 (10.7%) non-finite Wald estimates 被静默排除。regression 仅基于 89.3% 的样本。

## plan_010 annot_sensitivity Toolkit (2026-05-20)

### 设计决策
- **Bias 计算用 precomputed sufficient stats + plim**（2M 样本），不跑 MC——秒级响应，非分钟级
- **IV 拓扑用 Wald estimator**（W1 修复 2026-05-21）：`RF / (C @ FS)[1]`，near-permutation C → -904.8% bias + sign flip
- **recommend_correction 编码 plan_007 全部结论**：has_gold → PPI++; confounding/mediation → DSL; 其余 → MC-SIMEX; naive_plugin/MLA 标注 FWL=0%
- **K 不硬编码**：API 接受任意 K 的 C 矩阵，precomputed stats 按 (topology, params, K) 缓存
- **τ_true = plim(C=I)**：与 plan_005 一致，衡量 annotation error 额外引入的 bias
- **condition number 警告**：C condition > 1e12 时 warn，> 100 时在 recommend_correction 中提示
- **测试**: 47/47 passed（含 IV Wald 4 tests + correction 8 tests）

## Local Model Inference (2026-05-21)

### RTX 5090 + Qwen2.5-7B-Instruct 本地推理
- **vLLM 与 RTX 5090 (Blackwell sm_120) 不兼容**（flash_attn 不支持），改用 transformers + model.generate() (batch_size=8)
- annotate.py 添加 `--local-model` 参数 + `LocalAnnotationPipeline` 类
- model_key = "qwen2.5-7b"，model 字段为 "qwen2.5-7b-local"

### 标注结果（civil_comments K=2 + vast K=3）
| Dataset | Prompt | Accuracy | Diag Avg |
|---|---|---|---|
| civil_comments | zero-shot | 74.2% | 0.717 |
| civil_comments | few-shot-3 | 68.9% | 0.730 |
| civil_comments | few-shot-5 | 73.9% | 0.749 |
| vast | zero-shot | 48.0% | 0.473 |
| vast | few-shot-3 | 46.1% | 0.453 |
| vast | few-shot-5 | 46.5% | 0.459 |

- civil_comments: 质量可用（69-74%），7B 模型对 toxicity 判断合理
- vast: 质量较低（46-48%），7B 模型对 stance detection 困难——但正好提供 "7B vs 235B 对比" 维度
- 全部 parse rate ≥ 99.9%

## Director 决策记录 (2026-05-20)

### 数据集决策（最终确认）
- HumAID (K=10), VAST (K=3), Civil Comments (K=2)
- 数据位置：`/home/sonny/causal_annot_error_attrib/results/`（注意是 results/ 不是 data/）

### API 模型决策
- Llama 4 Maverick, Qwen 3 235B, DeepSeek Chat V3
- API endpoint: `http://47.94.22.126/v1`，全部用 OPENROUTER_API_KEY
- **2026-05-20 API 402 事故**：运行中余额耗尽，~10/27 任务完成，civil_comments 全废

### home-1x5090 服务器
- account: sonny, Python 3.10.12, Ubuntu 22.04
- 项目目录 `/home/sonny/causal_annot_error_attrib/`

### ASV 框架决策 (D005-D008)
- D005: C(δ) 参数化选定方案 A 线性插值
- D006: 区分 Vulnerability/Protection 双方向 ASV
- D007: Envelope monotonicity 替代 raw monotonicity
- D008: ASV 阈值从 sign-flip 改为 magnitude-based（0.1×|τ̂|），sign-flip ASV 保留给 Exposure

### Lee & Wood-Doughty (2024) 技术区分
本项目：observed exposure/confounder with noisy LLM annotation。LWD：unobserved confounding with proxy。关键区别：我们的 C 可从 validation data 估计。

## ASV C(δ) 参数化调研 (2026-05-20)

### 关键文献
- VanderWeele & Ding (2017): E-value 框架——单标量参数化 + 单调 + 可解释
- VanderWeele & Li (2019): 测量误差灵敏度分析——Se/Sp ratio 参数化
- Lash, Fox & Fink (2009): QBA 框架——(Se, Sp) 对参数化
- Brenner (1993): 多分类混杂误分类偏差方向可反转

### 与 E-value 的对应
方案 A 在 K=2 时精确退化到 VanderWeele & Li (2019) 框架。
