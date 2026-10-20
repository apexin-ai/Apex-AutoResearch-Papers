# Idea Inbox

## 待验证

- [2026-05-13] [P0] Cross-scale 验证：Pythia-410M + Pythia-2.8B | 同家族不同 scale 验证 spectral leading indicator 的 generalizability。Pythia-410M 验证小模型是否也有 eff_rank 领先 PPL 的时间差，Pythia-2.8B 验证大模型是否信号更强/更弱。每个模型 3 代 × 20M tokens，预估 ~30 GPU-hours（410M ~8h, 2.8B ~22h on A6000）。支撑 C1 (leading indicator) + RC1 (scale generalization)。
- [2026-05-13] [P0] Fixed ratio baselines：w=0.3/0.5/0.7 三组固定比例实验 | PI 控制器效果的核心对照组。每组 3 代 × 20M tokens，用 Pythia-1B + wikitext-103。预估 ~15 GPU-hours（3 组 × ~5h each）。支撑 C3 (collapse mitigation vs fixed baselines)。
- [2026-05-13] [P0] PI 控制器参数敏感性 sweep：Kp ∈ {0.005, 0.01, 0.02, 0.05}, Ki ∈ {0.002, 0.005, 0.01, 0.02} | 4×4=16 组超参组合（可用 grid search），验证控制器对参数变化的鲁棒性。每组 3 代 × 20M tokens，但可用 Pythia-410M 降低成本。预估 ~20 GPU-hours（16 组 × ~1.2h on 410M）。从 16 组中选 top-3 在 Pythia-1B 上验证跨 scale 稳定性（额外 ~5h）。支撑 C2 (controller mechanism robustness)。
- [2026-05-13] [P0] Spectral metric 对比：effective rank vs condition number vs trace norm vs spectral gap | 验证 effective rank 确实是最早/最稳定的 leading indicator。在 MVP v7 的 G0-G2 数据上离线计算所有 4 种指标，比较各自的 leading time（rank 下降 vs PPL 上升的时间差）。预估 ~10 GPU-hours（复用 v7 checkpoint，只做 forward pass）。支撑 C1 + RC3 (metric choice justification)。
- [2026-05-13] [P1] Cross-dataset 验证：C4-subset (100M tokens subsample) | 不同 domain/scale 的数据集验证 leading indicator 的数据无关性。Pythia-1B + C4-subset，3 代 × 20M tokens。预估 ~25 GPU-hours（C4 tokenization 和数据准备额外开销）。支撑 C1 + RC4 (data scale concern)。
- [2026-05-13] [P1] 5 代长期稳定性实验 | 从 3 代扩到 5 代，观察 PI 控制器在更长 collapse 过程中的稳定性。Pythia-1B + wikitext-103，5 代 × 20M tokens。预估 ~15 GPU-hours。支撑 C3 (multi-generation stability)。关键观察点：控制器是否在 G4-G5 出现积分饱和 / oscillation。
- [2026-05-13] [P1] Golden ratio baseline 对比 | 用 golden ratio (φ≈0.618) 作为固定混合比例的 baseline，与 PI 控制器的动态比例对比。理论上 golden ratio 是"最佳固定点"，如果 PI 仍优于它则说明动态适应的必要性。Pythia-1B，3 代 × 20M tokens。预估 ~5 GPU-hours。支撑 C3。
- [2026-05-13] [P0] Pure real data baseline（无合成数据）| 每代只用真实数据训练（w=1.0 固定），作为 collapse 不发生时的上界参考。Pythia-1B + wikitext-103，3 代 × 20M tokens。预估 ~5 GPU-hours。支撑 C3（表明 synthetic data 确实引入了 collapse，控制器在 mitigate 而非 artifact）。
- [2026-05-13] [P0] Pure synthetic baseline（w=0，纯合成数据）| 每代只用合成数据训练（w=0.0 固定），证明 collapse 确实在当前实验设置中发生。Pythia-1B + wikitext-103，3 代 × 20M tokens。预估 ~5 GPU-hours。与 pure real baseline 对称，共同建立 collapse 存在性的实验证据。支撑 C3 前提条件。
- [2026-05-13] [P0] PI controller implementation | 非 GPU 工程任务。实现 PI 控制器核心模块：spectral effective rank 实时计算 → error signal → PI update → mixing ratio adjustment。v7 完成后第一个工程任务，需在 GPU 实验前完成。包含：控制器类、与训练 pipeline 的集成接口、unit test。预估 ~1-2 天开发时间。支撑 C2 (controller mechanism)。
- [2026-05-13] [P2] RedPajama-subset cross-domain 验证 | 第二个 cross-dataset 验证（与 C4 互补），用 RedPajama 的 1B token subset。Pythia-1B，3 代 × 20M tokens。预估 ~25 GPU-hours。支撑 RC4。优先级低于 C4，仅当 GPU 预算允许时做。
## ACTIVE
