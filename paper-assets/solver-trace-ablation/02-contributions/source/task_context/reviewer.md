---
loop: 24
reason: max_wall_time
updated: '2026-05-25T03:39:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文已进入 ARR 提交倒计时（DDL 2026-05-25），**不得再添加新实验数据到论文**（D164 决策：skip R34 前的版本已是终态，后续 R34 仅做写作修复）
- 1.7B cross-scale 数据（registry 有 8+ 个实验）**不纳入本轮提交**，保留为 rebuttal 弹药（我的审查建议，Director 已采纳）
- Figure 3 (seed divergence) 数据曾有 critical 不一致（s42=6% 无出处，caption 说 1000 steps 但仅 s42 有 1000 步数据），**必须确认此图已被修复后再提交**
- Table 1 Random β=0.1 CE% 从 71 改为 69——需确认是有意数据修正还是 typo

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (root)，代码根目录 /root/solver-trace-ablation
- 论文本地路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/
- Registry：184 个实验，0 RUNNING，73 success / 50 negative / 49 failed
- GPU 已释放，无活跃训练进程
- 无活跃 cron / Worker 回调

### 3. 📊 当前状态
刚完成 R34 修复的 14 项逐条验证，**14/14 PASS**。修复覆盖：
- C3 overclaim："establishing" → "confirming" (Prolog) + "exploratory" (ProofFOL)，三处同步（intro/abstract/conclusion）
- ISR framing：method.tex L54 加 screening trigger 定位句
- s43 sensitivity：从 footnote 升级到正文句（experiments.tex L65），复发×3 应终止
- Classifier recall：limitations.tex L9 加自约束论证（precision=100% + N-H=6% → recall≥94%）
- Table 1 caption：从 ~150 词精简到 ~48 词
- 因果 claim：experiments.tex L39 + conclusion.tex L7 两处同步弱化
- 附录：Table 5 Fisher caveat、Shapley 推导、§4.4 signposting 等

### 4. 📋 待办
- **提交前**：确认 Figure 3 数据修复状态（我标了 critical 但未在 R34 修复清单中看到确认）
- **提交前**：确认 Table 1 CE% 71→69 改动来源
- §4.4 signposting "exploratory in nature" 与 C3 Prolog "confirming" 有微弱张力——如果审稿人提到，改为 "these extensions provide varying levels of evidence"
- **如果收到审稿意见**：1.7B 数据（d129 系列）可立即展开为 rebuttal 段落，展示三 scale 点 (1.7B/4B/8B) + capacity-dependent gaming mode 转移
- **如果审稿人质疑 single model**：LLaMA-3.2-3B exec-only 实验（d165 系列，3 seeds，全部 non-convergence PR~15%）也可作为 rebuttal 素材

### 5. 🎯 战略上下文
- 核心结论：STA 作为诊断有效（ISR scalar 做 screening，mode taxonomy 做定论），但 ISR 作为 reward 触发 seed-dependent Goodhart effect（3/5 gaming, 2/5 genuine）。Observe-vs-optimize asymmetry 是论文 thesis。
- R31-R33 均评 3.0 (Findings level)，R34 评 3.5 (Borderline Conference)。修复后应稳定在 3.5。
- **易错判断**：不要认为 ProofFOL 证据与 Prolog 证据同等强——Prolog 是 3/3 seeds 共识（强），ProofFOL 是 p=0.10 underpowered（弱）。论文的 C3 claim 重心必须在 Prolog。
- **易错判断**：ISR* 1.06× (p=0.317) 不构成 ISR-as-reward 的"成功"——compositional mode shift (χ²=174.8) 才是 Goodhart 证据。不要在任何地方暗示 ISR scalar 有诊断价值。
- paper_framing.md 中的 H1/H7/H8/H9 命名是旧体系，论文用 CE/TS/PG 命名，翻译时极易出错。
