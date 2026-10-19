# Reference Audit — Worker B (11 entries)

Audit date: 2026-05-29

---

## 1. [ortiz2022isdf] ✅

- **真实性**: OK
- **标题**: OK — "iSDF: Real-Time Neural Signed Distance Fields for Robot Perception"
- **作者**: OK — Joseph Ortiz et al.
- **年份**: OK — 2022
- **Venue**: OK — RSS 2022 (Robotics: Science and Systems XVIII)
- **arXiv ID**: 2204.02296
- **正文引用上下文**: OK — related_work.tex: "SDFs serve perception~\cite{ortiz2022isdf}"，iSDF 确实是用于机器人感知的实时神经 SDF 系统。

---

## 2. [zhi2021diffco] ⚠️

- **真实性**: OK
- **标题**: ⚠️ 小差异 — bib 用 arXiv 版标题 "Auto-Differentiable ... Multi-class"，IEEE T-RO 正式版为 "Autodifferentiable ... Multiclass"（去连字符、合成一词）。建议统一为正式发表版标题。
- **作者**: OK — Yuheng Zhi et al.
- **年份**: OK — IEEE T-RO 发表于 2022；bib key 中 "2021" 反映 arXiv 预印本年份（2102.07413，2021年2月），不影响引用正确性但 key 与 year 字段不一致。
- **Venue**: OK — IEEE Transactions on Robotics, vol. 38, no. 5, pp. 2668–2685, 2022
- **arXiv ID**: 2102.07413
- **正文引用上下文**: OK — related_work.tex: "differentiable collision detection~\cite{zhi2021diffco}"，DiffCo 确实是可微分碰撞检测方法。

---

## 3. [huang2023voxposer] ⚠️

- **真实性**: OK
- **标题**: OK — "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models"
- **作者**: OK — Wenlong Huang et al.
- **年份**: OK — 2023
- **Venue**: OK — CoRL 2023 (7th Conference on Robot Learning, Atlanta)
- **arXiv ID**: 2307.05973
- **正文引用上下文**: ⚠️ 轻微不当 — related_work.tex: "SDFs serve ... planning~\cite{huang2023voxposer,vasilopoulos2023ramp}"。VoxPoser 使用的是 LLM 生成的 3D value maps（affordance/cost 体素场），并非严格意义上的 SDF。将其归为 SDF 用于 planning 的例子有些牵强。RAMP 引用正确，VoxPoser 更适合归入 "spatial representations for planning" 而非 "SDF for planning"。

---

## 4. [liu2023libero] ✅

- **真实性**: OK
- **标题**: OK — "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
- **作者**: OK — Bo Liu et al.
- **年份**: OK — 2023
- **Venue**: OK — NeurIPS 2023 (Datasets and Benchmarks Track)
- **arXiv ID**: 2306.03310
- **正文引用上下文**: OK — related_work.tex: "SafeLIBERO extends LIBERO~\cite{liu2023libero}"，SafeLIBERO 确实基于 LIBERO 扩展。

---

## 5. [lipman2023flow] ✅

- **真实性**: OK
- **标题**: OK — "Flow Matching for Generative Modeling"
- **作者**: OK — Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le (Meta AI / Weizmann)
- **年份**: OK — 2023
- **Venue**: OK — ICLR 2023
- **arXiv ID**: 2210.02747
- **正文引用上下文**: OK — method.tex: "Pi0 ... with flow matching~\cite{lipman2023flow}"，Pi0 确实使用 flow matching 作为生成建模方法。

---

## 6. [gururangan2018annotation] ✅

- **真实性**: OK
- **标题**: OK — "Annotation Artifacts in Natural Language Inference Data"
- **作者**: OK — Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel R. Bowman, Noah A. Smith
- **年份**: OK — 2018
- **Venue**: OK — NAACL 2018 (ACL Anthology: N18-2017)
- **arXiv ID**: N/A（ACL Anthology 发表）
- **正文引用上下文**: OK — related_work.tex 两处引用：(1) "concerns about metric reliability~\cite{karwowski2024goodhart,gururangan2018annotation}" (2) "any binary safety metric faces a base-rate problem when most episodes are collision-free through inaction~\cite{gururangan2018annotation}"。原文讲标注伪影导致模型用捷径得高分，类比 action-collapsed 机器人通过不动获得高 CAR 分数。类比合理。

---

## 7. [karwowski2024goodhart] ✅

- **真实性**: OK
- **标题**: OK — "Goodhart's Law in Reinforcement Learning"
- **作者**: OK — Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse (Oxford)
- **年份**: OK — 2024
- **Venue**: OK — ICLR 2024
- **arXiv ID**: 2310.09144
- **正文引用上下文**: OK — introduction.tex: "standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}"；related_work.tex: "concerns about metric reliability"。CAR 作为 proxy metric 被 action collapse 失效，符合 Goodhart 定律的内涵。

---

## 8. [chi2023diffusionpolicy] ⚠️

- **真实性**: OK
- **标题**: OK — "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
- **作者**: OK — Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song
- **年份**: OK — 2023
- **Venue**: OK — RSS 2023（后续有 IJRR 2025 扩展版）
- **arXiv ID**: 2303.04137
- **正文引用上下文**: ⚠️ 分类不当 — related_work.tex: "VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}"。Diffusion Policy 是 visuomotor policy，**没有语言组件**，不是 VLA 模型。与同列的 RT-2、Pi0、OpenVLA（均使用 VLM backbone）不同。建议将 Diffusion Policy 从该句移除，或改为更准确的分类描述（如 "visuomotor and VLA models"）。

---

## 9. [li2024cdf] ✅

- **真实性**: OK
- **标题**: OK — "Configuration Space Distance Fields for Manipulation Planning"
- **作者**: OK — Yiming Li, Xuemin Chi, Amirreza Razmjoo, Sylvain Calinon (IDIAP/EPFL)
- **年份**: OK — 2024
- **Venue**: OK — RSS 2024 (Delft, Netherlands)
- **arXiv ID**: 2406.01137
- **正文引用上下文**: OK — related_work.tex: "CDF~\cite{li2024cdf} ... extend SDFs to configuration space for manipulation planning"，准确描述。

---

## 10. [li2024rdf] ✅

- **真实性**: OK
- **标题**: OK — "Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation"
- **作者**: OK — Yiming Li, Yan Zhang, Amirreza Razmjoo, Sylvain Calinon (IDIAP/EPFL)
- **年份**: OK — 2024
- **Venue**: OK — ICRA 2024 (Yokohama, pp. 15351–15357)
- **arXiv ID**: 2307.00533
- **正文引用上下文**: OK — related_work.tex: "RDF~\cite{li2024rdf} represents robot geometry as composable per-link SDFs, enabling whole-body collision queries"，准确描述。CDF 和 RDF 确实都是 Yiming Li（IDIAP）的工作。

---

## 11. [vasilopoulos2023ramp] ✅

- **真实性**: OK
- **标题**: OK — "RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions"
- **作者**: OK — Vasileios Vasilopoulos, Suveer Garg, Pedro Piacenza, Jinwook Huh, Volkan Isler (Samsung Research)
- **年份**: OK — 2023
- **Venue**: OK — IROS 2023 (pp. 10551–10558)
- **arXiv ID**: 2305.10534
- **正文引用上下文**: OK — related_work.tex: "planning~\cite{huang2023voxposer,vasilopoulos2023ramp}"，RAMP 确实用隐式 SDF 做运动规划。

---

## 总结

| 状态 | 数量 | 条目 |
|------|------|------|
| ✅ OK | 8 | ortiz2022isdf, liu2023libero, lipman2023flow, gururangan2018annotation, karwowski2024goodhart, li2024cdf, li2024rdf, vasilopoulos2023ramp |
| ⚠️ 有问题 | 3 | zhi2021diffco, huang2023voxposer, chi2023diffusionpolicy |

### 需要修复的问题

1. **[zhi2021diffco]** (低优先级): bib key "2021" 与 year "2022" 不一致；标题用的是 arXiv 版而非 IEEE T-RO 正式版（"Auto-Differentiable" vs "Autodifferentiable"）。非严重错误，但建议统一。

2. **[huang2023voxposer]** (低优先级): 正文将 VoxPoser 归为 "SDF for planning" 的例子，但 VoxPoser 使用的是 LLM 生成的 3D value maps，不是 SDF。建议在该句中改为更准确的表述，如将 "planning" 的引用改为 RAMP 和其他真正使用 SDF 的规划方法。

3. **[chi2023diffusionpolicy]** (中优先级): 正文将 Diffusion Policy 归入 "VLA models" 类别，但 Diffusion Policy 是 visuomotor policy，没有语言组件。建议从 VLA 列表中移除，或将句子改为 "Visuomotor and VLA models"。
