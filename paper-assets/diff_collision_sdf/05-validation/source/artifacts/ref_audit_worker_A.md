# Reference Audit — Worker A (11 条)

审计日期：2026-05-29

---

## 逐条验证

### [black2024pi0] ✅
- 真实性: OK
- 标题: OK — "π₀: A Vision-Language-Action Flow Model for General Robot Control"
- 作者: OK — Kevin Black et al. (Physical Intelligence)
- 年份: OK — 2024 (arXiv v1: 2024-10-31)
- Venue: OK — arXiv:2410.24164（预印本，未标注会议）
- arXiv ID: OK — 2410.24164
- 正文引用上下文: OK — introduction.tex 引用为 Pi0 模型，related_work.tex 列为 VLA 代表工作，method.tex 引用为基线模型。均准确。

---

### [kim2024openvla] ✅
- 真实性: OK
- 标题: OK — "OpenVLA: An Open-Source Vision-Language-Action Model"
- 作者: OK — Moo Jin Kim et al. (Stanford, UC Berkeley, TRI, Google DeepMind, MIT)
- 年份: OK — 2024
- Venue: OK — CoRL 2024（PMLR v270, proceedings.mlr.press/v270/kim25c）
- arXiv ID: N/A（bib 未标注 arXiv ID；arXiv 为 2406.09246）
- 正文引用上下文: OK — related_work.tex 列为 VLA 代表工作。准确。

---

### [brohan2023rt2] ✅
- 真实性: OK
- 标题: OK — "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
- 作者: OK — Anthony Brohan et al.（arXiv 版第一作者；注意 CoRL proceedings 的 PMLR 条目为 zitkovich23a，即 proceedings 版第一作者为 Brianna Zitkovich，但学术界通行引用为 Brohan et al.）
- 年份: OK — 2023
- Venue: OK — CoRL 2023（PMLR v229, pp. 2165-2183）
- arXiv ID: N/A（bib 未标注；arXiv 为 2307.15818）
- 正文引用上下文: OK — related_work.tex 列为 VLA 代表工作。准确。

---

### [hu2025vlsa] ✅
- 真实性: OK
- 标题: OK — "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer"（项目别名 AEGIS）
- 作者: OK — Songqiao Hu et al.
- 年份: OK — 2025 (arXiv: 2024-12-09 提交，2512 编号)
- Venue: OK — arXiv:2512.11891（预印本）
- arXiv ID: OK — 2512.11891
- 正文引用上下文: OK — 论文中 SafeLIBERO benchmark 归因于此文（VLSA/AEGIS 确实构建了 SafeLIBERO），related_work.tex 描述其使用 control barrier functions，method.tex 引用作为评估 benchmark 来源。均准确。

---

### [zhang2025safevla] ✅
- 真实性: OK
- 标题: OK — "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning"
- 作者: OK — Borong Zhang et al. (PKU-Alignment)
- 年份: OK — 2025
- Venue: OK — NeurIPS 2025 **Spotlight**（已确认：papers.nips.cc, neurips.cc/virtual/2025/poster/116975, GitHub 标注 Spotlight）
- arXiv ID: N/A（bib 未标注；arXiv 为 2503.03480）
- 正文引用上下文: OK — introduction.tex 描述为 "constrained optimization"，related_work.tex 描述为 "training-time constrained RL"，均与 SafeVLA 使用 CMDP/safe RL 的方法一致。准确。
- 备注: SafeVLA 提出的 benchmark 是 Safety-CHORES（非 SafeLIBERO），论文中未混淆。

---

### [cofreeevla2026] ⚠️
- 真实性: OK
- 标题: OK — "CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation"
- 作者: OK — Xuanran Zhai et al.
- 年份: OK — 2026 (arXiv 提交: 2026-01)
- Venue: OK — arXiv:2601.21712（预印本）
- arXiv ID: OK — 2601.21712
- 正文引用上下文: **introduction.tex ⚠️ 存疑** — 第 10 行将 CoFreeVLA 描述为 "collision-free demonstrations"，但 CoFreeVLA 的核心方法是**碰撞风险估计器 + 动作门控**（risk estimator + gating），而非使用无碰撞示教数据。related_work.tex 第 7 行正确描述为 "collision risk gating~\cite{cofreeevla2026}"。introduction.tex 中的归因不够准确，建议改为 "collision risk gating" 或 "risk-guided action filtering"。

---

### [spalter2024ikinqp] ✅
- 真实性: OK
- 标题: OK — "Towards Online Safety Corrections for Robotic Manipulation Policies"
- 作者: OK — Ariana Spalter, Mark Roberts, Laura M. Hiatt (U.S. Naval Research Laboratory)
- 年份: OK — 2024
- Venue: OK — arXiv:2409.08233（预印本）
- arXiv ID: OK — 2409.08233
- 正文引用上下文: OK — related_work.tex 描述为 "inverse kinematics QP"，与论文的 iKinQP-RL 方法一致。准确。

---

### [li2024langguided] ✅
- 真实性: OK
- 标题: OK — bib 标题 "Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation" 与 ICRA 发表版和早期 arXiv 版本一致。（注：arXiv 最新版 v3 标题为 "...for Generalizable and Collision-Aware Robotic Manipulation"，增加了 "Generalizable and"，但 ICRA proceedings 版和多数数据库使用短标题。）
- 作者: OK — Hang Li et al. (TUM)
- 年份: OK — bib 标注 2024 为 arXiv 年份（2024-06-29 提交），venue 为 ICRA 2025
- Venue: OK — ICRA 2025（IEEE International Conference on Robotics and Automation 2025）
- arXiv ID: N/A（bib 未标注；arXiv 为 2407.00451）
- 正文引用上下文: OK — related_work.tex 描述为 "diffusion-process collision costs"，与论文在去噪步骤中加入碰撞代价优化的方法一致。准确。

---

### [yang2025cape] ✅
- 真实性: OK
- 标题: OK — "CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance"（注：部分搜索结果 Via 写作 via，属排版差异，非错误）
- 作者: OK — Rui Heng Yang et al.
- 年份: OK — 2025 (arXiv: 2025-11-27)
- Venue: OK — arXiv:2511.22773（预印本）
- arXiv ID: OK — 2511.22773
- 正文引用上下文: OK — introduction.tex 和 related_work.tex 均描述为 "diffusion-process collision costs"，与 CAPE 在扩散过程中引入碰撞引导的方法一致。准确。

---

### [xiao2025safediffuser] ✅
- 真实性: OK
- 标题: OK — "SafeDiffuser: Safe Planning with Diffusion Probabilistic Models"
- 作者: OK — Wei Xiao, Tsun-Hsuan Wang, Chuang Gan, Ramin Hasani, Mathias Lechner, Daniela Rus
- 年份: OK — bib 标注 2025（venue 年份）
- Venue: OK — **ICLR 2025 confirmed**（proceedings.iclr.cc, iclr.cc/virtual/2025/poster/28682, OpenReview）
- arXiv ID: N/A（bib 未标注；arXiv 为 2306.00148，首次提交 2023-05）
- 正文引用上下文: OK — related_work.tex 描述为 "integrates barrier functions into diffusion denoising but does not learn intrinsic collision awareness"，与 SafeDiffuser 使用 control barrier functions 嵌入去噪过程的方法一致。准确。

---

### [park2019deepsdf] ✅
- 真实性: OK
- 标题: OK — "DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation"
- 作者: OK — Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, Steven Lovegrove (Facebook Research)
- 年份: OK — 2019
- Venue: OK — CVPR 2019（IEEE/CVF Conference on Computer Vision and Pattern Recognition, Long Beach, pp. 165-174）
- arXiv ID: N/A（bib 未标注；arXiv 为 1901.05103）
- 正文引用上下文: OK — related_work.tex 描述为 "Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation"。准确。

---

## 总结

| 状态 | 数量 | 引用 |
|------|------|------|
| ✅ OK | 10 | black2024pi0, kim2024openvla, brohan2023rt2, hu2025vlsa, zhang2025safevla, spalter2024ikinqp, li2024langguided, yang2025cape, xiao2025safediffuser, park2019deepsdf |
| ⚠️ 有问题 | 1 | cofreeevla2026 |
| ❌ 不存在/严重错误 | 0 | — |

**11 条引用全部真实存在，元数据（标题、作者、年份、venue、arXiv ID）均正确。**

**1 条引用上下文存疑：** `cofreeevla2026` 在 introduction.tex 第 10 行被描述为 "collision-free demonstrations"，但 CoFreeVLA 的核心方法是碰撞风险估计 + 动作门控，而非无碰撞示教。related_work.tex 的描述（"collision risk gating"）正确。建议修正 introduction.tex 中的描述。

### 特别关注项验证结果
- **SafeVLA (NeurIPS 2025)**: ✅ 确认被 NeurIPS 2025 接收（Spotlight）
- **SafeDiffuser (ICLR 2025)**: ✅ 确认 venue 和年份正确
- **CoFreeVLA arXiv ID 2601.21712**: ✅ 确认存在，2026 年 1 月提交
- **VLSA arXiv ID 2512.11891**: ✅ 确认存在，2025 年 12 月提交
