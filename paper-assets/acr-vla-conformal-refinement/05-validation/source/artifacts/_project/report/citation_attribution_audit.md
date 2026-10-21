# Citation Attribution Audit — 2026-05-15

## 审计范围
- introduction_scenarioC.tex, method.tex, experiments.tex, related_work.tex
- 共 27 个唯一引用，每个均通过 WebSearch 验证方法归因准确性

## 审计结果

| Citation Key | 论文中的描述 | 实际方法 | 状态 | 备注 |
|---|---|---|---|---|
| black2024pi0 | VLA that generates actions via flow matching | π₀ is a Vision-Language-Action Flow Model | CORRECT | — |
| shukor2025smolvla | 450M-parameter flow-matching VLA | SmolVLA confirmed 450M params, flow matching action expert | CORRECT | — |
| liu2023libero | Standard manipulation benchmark | LIBERO is a NeurIPS 2023 benchmark with 130 manipulation tasks | CORRECT | — |
| fei2025liberoplus | Distribution shifts (object appearance, lighting, sensor noise) cause performance degradation | LIBERO-Plus covers 7 perturbation types; "object appearance changes" not a precise match—paper covers objects layout, background textures, camera viewpoints, etc. | NEEDS_REVIEW | 论文中 "object appearance changes" 应改为更准确的描述，如 "visual perturbations" |
| robustvla2025 | Combines RL post-training with Jacobian regularization | Confirmed: online RL post-training + Jacobian regularization + smoothness regularization | CORRECT | — |
| srpo2025 | Self-referential RL fine-tuning, using policy's own rollouts as training signal | Uses own *successful* rollouts as reference to reward *failed* trajectories via latent world model | NEEDS_REVIEW | "own rollouts as training signal" 方向正确但过于简化；核心是成功/失败轨迹对比 |
| digflow2025 | Regularizes the flow-matching denoising trajectory via a discrepancy-guided objective | DiG-Flow operates at representation level: computes distributional discrepancy between observation/action embeddings as gating signal (DiG-Block); flow matching path is NOT modified | **INCORRECT** | 论文不是 "regularize denoising trajectory"，而是在 representation level 用 discrepancy gating |
| chen2026reconvla | Draws multiple action samples and selects the best via conformal scoring—a pure sample selection strategy | ReconVLA uses CQR-based uncertainty bounds on single action output stream + SMD-based OOD detection; NOT multi-sample selection | **INCORRECT** | 已知问题确认。Introduction/Method/Related Work 三处均有错误描述 |
| liu2026scvla (sc_vla_2026) | Learns residual correction via RL, requiring per-task environment interaction | SC-VLA uses sparse world imagination + residual RL with progress-dependent dense rewards | CORRECT | — |
| li2025vlapilot (vla_pilot_2025) | Evolutionary optimization guided by MLLM verifier, 2.41s/step | Embodied Evolutionary Diffusion + EPS-CoT MLLM verifier, 2.41s confirmed | CORRECT | — |
| a2c2_2025 | Trains correction head **jointly with the VLA**, not a post-hoc module on frozen model | A2C2 trains correction head on **frozen** base VLA; IS a post-hoc module | **INCORRECT** | Introduction 中 "jointly with the VLA" 与实际完全相反 |
| braun2025cgs | CGS uses Mahalanobis-based nonconformity scores respecting cross-dimensional covariance | Confirmed: Mahalanobis distance from learned local covariance as nonconformity score | CORRECT | — |
| ross2011dagger | Compounding error in imitation learning | DAgger paper, central contribution is compounding error/covariate shift | CORRECT | — |
| silver2018residual | Introduced bounded residual corrections for combining learned and classical controllers; zero-initialization | Zero-initialization: CORRECT. **Bounded corrections: NOT in the paper**—no explicit bounding/clipping. "For classical controllers" overstates specificity | **INCORRECT** | 需删除 "bounded corrections" 归因；Silver et al. 用的是 zero-initialization，不是 bounded corrections |
| jiang2024transic | Learned binary gating to selectively apply residual actions across different task phases; ungated causes model collapse | Binary gate: CORRECT. Model collapse: CORRECT. "Across task phases" 不准确—gate 是 state-conditioned binary classifier，不是 phase-based | NEEDS_REVIEW | "across different task phases" 改为 "conditioned on the current state" |
| xiao2026pld | Scheduled magnitude bound ξ, progressively increasing during training | ξ bound exists; but "progressively increasing" 未确认—ξ 似乎是 per-benchmark 固定超参 (LIBERO=0.5, SimplerEnv=0.1) | NEEDS_REVIEW | "progressively increasing" 可能不准确，需要进一步确认或改为 "tuned per benchmark" |
| pan2025drc | Temporal decay of correction magnitude over episode; early corrections matter more | Decay is per-correction-event exponential persistence after each expert input, NOT within-episode weighting favoring early corrections | **INCORRECT** | 描述的 intuition 完全错误；DRC 的 decay 是每次纠正事件后的衰减，不是 episode 级别 |
| lipman2023flow | Foundational flow matching method | Flow Matching for Continuous Normalizing Flows, ICLR 2023 | CORRECT | — |
| ledoit2004well | Ledoit-Wolf shrinkage with analytically optimal shrinkage intensity | Linear shrinkage with consistent optimal intensity estimator | CORRECT | — |
| liu2026ttvla | Test-time RL with progress rewards, requires per-task reward design and gradient updates | Confirmed: test-time RL adaptation with step-by-step progress signals | CORRECT | — |
| angelopoulos2023gentle | CP provides distribution-free coverage guarantees under exchangeability | Confirmed: central theorem of the tutorial | CORRECT | — |
| zhao2024conformalized | CP for uncertainty in high-DOF action mappings in shared autonomy, flagging unreliable predictions | Uses adaptive CP on joystick-to-robot action mapping, proactive intervention seeking | CORRECT | — |
| wang2025cploop | CP regions as feedback constraints in trajectory optimization | Fb-CP framework, bidirectional feedback between CP and trajectory optimization | CORRECT | — |
| zhou2025acp_cbf | Combines ACP with CBFs for safe RL under distribution shift | Method description CORRECT, but **authors wrong in bib**: should be Hao Zhou, Yanze Zhang (not Zetian Zhou, Shuo Yang) | **INCORRECT** | Bib 文件作者需修正 |
| gu2025safe | Multitask failure detector on VLA features, CP-calibrated detection timing, safe fallback | Failure detection + functional CP for timing threshold: CORRECT. "Safe fallback behaviors" 轻微夸大—论文聚焦检测，不是 fallback 策略 | NEEDS_REVIEW | "triggering safe fallback behaviors" 可简化为 "triggering intervention" |
| xing2026diu | Closed-form posterior covariance via velocity field divergence, single-pass per-DOF UQ | Confirmed: divergence-uncertainty identity, single-pass without sampling | CORRECT | — |
| zollo2025vla_calibration | First systematic VLA calibration study; prompt ensembles + Platt scaling | Method description CORRECT, but **first author name wrong in bib**: Thomas Zollo (not Matteo Zollo) | **INCORRECT** | Bib 文件作者名需修正 |

## 统计
- **CORRECT**: 15/27
- **INCORRECT**: 7/27 (chen2026reconvla, a2c2_2025, digflow2025, silver2018residual, pan2025drc, zhou2025acp_cbf, zollo2025vla_calibration)
- **NEEDS_REVIEW**: 5/27 (fei2025liberoplus, srpo2025, jiang2024transic, xiao2026pld, gu2025safe)

## 需要修正的引用

### 🔴 INCORRECT — 必须修正

**1. chen2026reconvla (Introduction + Method + Related Work)**
- 错误：描述为 "draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy"
- 实际：ReconVLA 使用 CQR (Conformalized Quantile Regression) 对单次 action 输出计算校准不确定性区间 + SMD-based OOD 检测，不是多样本选择
- 修改建议：
  - Introduction: 改为 "applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states via Mahalanobis distance—an uncertainty quantification and failure detection framework that does not perform multi-sample selection"
  - Method (Eq. 4 上方): 改为 "inspired by conformal scoring methods such as ReconVLA" 而非 "conformal selection frontend of ReconVLA"
  - Related Work: 修正描述，强调 CQR-based UQ + OOD detection

**2. a2c2_2025 (Introduction)**
- 错误："trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model"
- 实际：A2C2 的 base VLA 是 frozen 的，correction head 是 post-hoc 添加并独立训练的
- 修改建议：改为 "adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection"

**3. digflow2025 (Related Work)**
- 错误："regularizes the flow-matching denoising trajectory via a discrepancy-guided objective"
- 实际：DiG-Flow 在 representation level 计算 observation/action embedding 之间的分布差异作为 gating signal (DiG-Block)，flow matching path 本身不被修改
- 修改建议：改为 "uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance control between the foundation model and the flow expert"

**4. silver2018residual (Introduction + Related Work)**
- 错误：归因了 "bounded corrections"
- 实际：Silver et al. 使用 zero-initialization 使 residual 从零开始，但没有显式的 bounded/clipped corrections
- 修改建议：
  - Related Work: 改为 "introduced the framework, using zero-initialization to ensure the learned residual starts as a no-op and gradually improves upon the base policy"
  - 删除所有 "bounded corrections" 归因到 Silver et al. 的地方

**5. pan2025drc (Related Work)**
- 错误："applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones"
- 实际：DRC 的 decay 是每次专家纠正事件后的指数衰减持续性，不是 episode 级别的时间权重
- 修改建议：改为 "applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over subsequent timesteps after application"

**6. zhou2025acp_cbf (references.bib)**
- 错误：作者 "Zetian Zhou, Shuo Yang, Wenhao Luo"
- 实际：应为 "Hao Zhou, Yanze Zhang, Wenhao Luo"
- 修改建议：更新 bib 中的 author 字段

**7. zollo2025vla_calibration (references.bib)**
- 错误：作者 "Matteo Zollo"
- 实际：应为 "Thomas Zollo"
- 修改建议：更新 bib 中的 author 字段

### 🟡 NEEDS_REVIEW — 建议修正

**8. fei2025liberoplus (Introduction)**
- "object appearance changes" 不是 LIBERO-Plus 的精确描述；论文覆盖 objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise
- 建议改为 "visual and physical perturbations" 或列举更准确的类别

**9. srpo2025 (Related Work)**
- "using the policy's own rollouts as training signal" 过于简化
- 建议改为 "using the policy's own successful rollouts as reference to shape rewards for failed trajectories"

**10. jiang2024transic (Related Work)**
- "across different task phases" 不准确，gate 是 state-conditioned 的
- 建议改为 "conditioned on the current state to decide whether to apply correction at each step"

**11. xiao2026pld (Related Work)**
- "progressively increasing the allowed correction range during training" 未确认
- 建议改为 "introducing a magnitude bound ξ for the residual actor, tuned per benchmark"

**12. gu2025safe (Related Work)**
- "triggering safe fallback behaviors" 轻微夸大
- 建议改为 "triggering intervention when anomalous states are detected"

## 总结
27 个引用中有 7 个方法归因错误（包括 2 个 bib 作者错误），5 个需要措辞调整。最严重的问题是 chen2026reconvla（核心机制描述完全错误，出现在三个章节）和 a2c2_2025（训练方式描述与实际相反）。这两个修正是提交前的 blocking items。silver2018residual 的 "bounded corrections" 归因错误也需要修正，因为它影响了 Related Work 中 magnitude control 叙事的准确性。
