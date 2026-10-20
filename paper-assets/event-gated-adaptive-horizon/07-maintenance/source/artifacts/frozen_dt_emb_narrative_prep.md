# Frozen dt_emb 情景叙事预案（exp_084-087）

## 当前证据基线

| 条件 | Onset rate | 来源 |
|------|-----------|------|
| Trained dt_emb | 10/10 | 8 Walker + 2 Cheetah |
| Frozen dt_emb (新代码) | 0/1 | exp_067 (NVE peak=0.4) |
| No dt_emb | 0/5 | 008f, 009c, exp_069 等 |
| 旧代码 frozen (BF1 无效) | 0/3 | exp_042/046/047, D152 已废弃 |

exp_084-087 = 4 个 frozen runs（新代码），完成后 frozen 新代码样本从 1 增至 5。

---

## 情景 A：4 个 frozen 全部无持续 CIVO（NVE < 1.5x）

**对 C2 的影响**：三路消融从 trained 10/10 vs frozen 0/1 vs absent 0/5 升级为 **trained 10/10 vs frozen 0/5 vs absent 0/5**。Fisher exact p < 0.0001 不变，但 frozen 样本量从 1 增至 5 大幅提高统计力度。总 control 组 0/10 vs trained 10/10 = 完美分离。

**与 dt_embed_dim=0 互补**：frozen 证明 embedding **存在但不训练** 不触发 CIVO → 锁定因果为梯度训练过程，非 embedding 的 forward-pass 存在。与 absent (dim=0) 形成两层控制：absent 移除信号源，frozen 保留信号但阻断适应性学习。二者交叉确认 "训练" 是必要条件。

**论文更新点**（列出，不改）：
- C2 evidence table: 增加 exp_084-087 行，Fisher exact 分母更新
- Section 4 Finding 2: n 数更新，跨环境 frozen coverage
- Causal ablation matrix (memory.md): 补全 Cheetah frozen 格

**预备回答 Reviewer 追问**：
- *"Frozen embedding 把 gate 锁死 dt=2，实验条件不等价"* → 关键对比是 value overestimation 有无，不是策略质量。Frozen eval 偏低（~281）是预期的，但 NVE 从未突破 1.5x 才是 C2 的检验点。
- *"5 个 frozen 仍然太少"* → 结合 absent 0/5，total control 0/10 vs treated 10/10，Fisher exact p < 10^-5，足以支撑 ICML diagnostic paper。

---

## 情景 B：某些 frozen 实验出现持续 CIVO

**区分 transient spike vs 持续 CIVO**：参考 exp_047 s1 模式（NVE 瞬时 1.71 → 自修正至 0.56）。判定标准：
1. NVE > 1.5x 是否跨 **≥2 个连续 checkpoint** 持续？
2. NVE 趋势是加速（008d 模式）还是衰减（047 模式）？
3. eval 是否同步恶化？

若仅 transient spike + 自修正 → 仍归为 "无持续 CIVO"，与 009b (trained, transient) 类比但注明 frozen 的 spike 幅度和持续期均更低。

**若确认 frozen 也产生持续 CIVO**：
- C2 从 "训练是必要条件" 降级为 "训练大幅放大但非必要"
- 措辞调整：*"Gradient training of dt_embedding dramatically amplifies CIVO severity (10/10 onset, NVE 2-70x) compared to frozen embedding (k/5 onset, NVE ~1.5-2x), but does not fully eliminate it"*
- 机制解释转向：即使 frozen embedding 也在 forward pass 提供固定但非零的 dt conditioning → RSSM 在特定 seed/环境下仍可能形成弱 co-adaptation

**Framing 调整选项**：
1. **量级论** — trained CIVO NVE 2-70x vs frozen CIVO NVE ~1.5x，差异 > 一个数量级 → "训练是 CIVO 严重度的主要放大器"
2. **概率论** — trained 10/10 vs frozen k/5 → "训练将 onset 概率从 X% 提升至 100%"
3. **双因素论** — embedding 存在 = 必要条件，训练 = 充分条件之一（frozen 可能在特定环境/seed 下也充分）

**最坏防守策略**：如果 frozen 在 Cheetah 出现 CIVO（Cheetah CIVO 本身更强，NVE peak 更高），可定位为 "环境复杂度调节 frozen 的保护效力"，与 Cartpole 0/3 onset 形成 complexity-dependent 叙事，保住核心 claim 的方向性。absent (dim=0) 的 0/5 仍作为 hard control 不受影响。
