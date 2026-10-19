# ColliForce-VLA Related Work Literature Map

> Generated: 2026-05-19 | Project: diff_collision_sdf (ICLR 2027)

---

## Category 1: 3D-aware VLAs

These methods improve spatial reasoning via depth, geometry, or point cloud representations, but **none explicitly targets collision avoidance**.

| 论文 | Venue / arXiv | 日期 | 方法概要 | 关系 | Baseline? | 代码 |
|------|--------------|------|---------|------|-----------|------|
| QDepth-VLA | arXiv 2510.14836 | Oct 2025 | VQ-VAE量化深度预测作为VLA辅助监督任务 | `method-component` | **Yes** — 最近方法论对标，辅助监督范式直接可比 | [GitHub](https://github.com/ucasmichael/QDepth-VLA) |
| DepthVLA | arXiv 2510.13375 | Oct 2025 | Mixture-of-Transformers融合预训练深度Transformer与VLM | `baseline` | **Yes** — 深度增强VLA代表，若代码可用 | 未开源（声称将发布） |
| Spatial Forcing | ICLR 2026, arXiv 2510.12276 | Oct 2025 | 隐式3D对齐VLA视觉表征与3D基础模型，训练加速3.8× | `baseline` | **Yes** — 隐式3D对齐SOTA，证明不需显式3D输入 | [GitHub](https://github.com/OpenHelix-Team/Spatial-Forcing) |
| SpatialVLA | RSS 2025, arXiv 2501.15830 | Jan 2025 | Ego3D位置编码+自适应空间对齐，1.1M真实数据训练 | `landscape` | No — 不同技术路线，related work讨论 | [GitHub](https://github.com/SpatialVLA/SpatialVLA) |
| 3D-CAVLA | arXiv 2505.05800 | May 2025 | Chain-of-thought推理+深度感知+ROI检测，LIBERO 98.1% | `landscape` | No — 侧重任务泛化非碰撞 | [GitHub](https://github.com/vineet2104/3dcavla) |
| Evo-0 | arXiv 2507.00416 | Jul 2025 | 插件式隐式3D几何特征模块(VGGT)，无需推理时3D输入 | `landscape` | No — 方法路线与Spatial Forcing类似 | [GitHub](https://github.com/MINT-SJTU/Evo-VLA) |
| GeoAware-VLA | arXiv 2509.14117 | Sep 2025 | 冻结预训练VGGT作为几何特征提取器替换标准图像编码器 | `landscape` | No — 视角泛化导向 | 未开源 |
| AugVLA-3D | ICRA 2026, arXiv 2602.10698 | Feb 2026 | VGGT深度驱动3D特征增强+action assistant正则化 | `landscape` | No — 3D增强路线，非碰撞导向 | 未开源 |
| StemVLA | arXiv 2602.23721 | Feb 2026 | 预测未来3D空间几何+时序注意力聚合历史4D表征 | `landscape` | No — 时空预测导向 | 声称开源，未找到repo |
| SA-VLA | arXiv 2602.00743 | Jan 2026 | 隐式空间表征融合+几何感知奖励+空间条件退火探索的RL微调 | `landscape` | No — RL微调框架 | 未开源 |
| ST-VLA | arXiv 2603.13788 | Mar 2026 | 2D引导→3D轨迹+空间掩码的分层4D时空理解 | `landscape` | No — 时空理解框架 | 未开源 |
| GST-VLA | arXiv 2603.09079 | Mar 2026 | 高斯空间Tokenizer生成128个3D各向异性高斯基元+DA-CoT | `landscape` | No — 新颖表征但非碰撞相关 | 未开源 |
| 3DS-VLA | CoRL 2025 | Aug 2025 | 2D-to-3D位置对齐+序列化3D空间约束定义抓取关键点 | `landscape` | No — 3D对齐方法 | 未开源 |
| Evo-Depth | arXiv 2605.14950 | May 2026 | 轻量深度增强VLA框架 | `landscape` | No — 轻量化深度增强 | 可能开源(MINT-SJTU组) |

### 详细分析

**必须对比的 Baselines (Cat 1):**

1. **QDepth-VLA** — 最关键的方法论对标。同样使用辅助3D监督范式（深度 vs. 我们的SDF），但(a)在2.5D相机空间操作，(b)解码器仅训练时使用无双向耦合，(c)无推理时梯度流。我们的消融A4（SDF vs depth vs binary occupancy作为辅助目标）直接与其对比。代码已开源，可复现。

2. **DepthVLA** — 深度增强VLA的另一代表，MoT架构。若QDepth-VLA为主要深度baseline则DepthVLA为次要，视代码可用性决定。

3. **Spatial Forcing** — 证明隐式3D对齐在VLA中有效的里程碑工作(ICLR 2026)。需展示我们的SDF梯度引导在碰撞场景优于通用3D对齐。代码已开源。

**整体观察:** 14篇3D-aware VLA中仅4篇有开源代码(QDepth-VLA, 3D-CAVLA, Evo-0, Spatial Forcing, SpatialVLA)。该领域快速扩张但代码开源率低。所有方法优化任务成功率/泛化能力，**无一报告碰撞指标**，验证了我们的research gap。

---

## Category 2: Collision-safe VLAs

这些方法**针对碰撞安全**，但通过外部后处理而非内化空间理解。

| 论文 | Venue / arXiv | 日期 | 方法概要 | 关系 | Baseline? | 代码 |
|------|--------------|------|---------|------|-----------|------|
| AEGIS/VLSA | arXiv 2512.11891 | Dec 2025 | 插件式CBF安全约束层：开集目标检测+深度→物理空间避障QP求解 | `direct-competitor` | **Yes** — SafeLIBERO上唯一已发表结果，CAR提升59.16% | [GitHub](https://github.com/THU-RCSCT/vlsa-aegis) |
| SafeVLA | NeurIPS 2025 Spotlight, arXiv 2503.03480 | Mar 2025 | CMDP约束学习框架：安全正负样本对比学习，安全性提升83.58% | `baseline` | **Yes** — NeurIPS Spotlight，RL-based安全对齐代表 | [GitHub](https://github.com/PKU-Alignment/SafeVLA) |
| CoFreeVLA | arXiv 2601.21712 | Jan 2026 | 短时域自碰撞风险估计器+风险门控+恢复策略(双臂) | `orthogonal` | No — 双臂自碰撞，非环境障碍物避障 | 未开源 |

### 详细分析

**AEGIS/VLSA — 最重要的直接竞品:**
- **SafeLIBERO结果:** 是。AEGIS **创建了** SafeLIBERO基准(4 suites, 16 tasks, 32 scenarios, 1600 episodes)。报告CAR 77.85%, TSR提升17.25%。
- **代码状态:** 已开源 [GitHub](https://github.com/THU-RCSCT/vlsa-aegis)，含SafeLIBERO数据集 [HuggingFace](https://huggingface.co/datasets/THURCSCT/SafeLIBERO)。
- **与我们的核心对比:** AEGIS是后处理(post-hoc CBF correction)，不改变VLA内部空间理解。我们是前向传播内(forward-pass internalized SDF gradient)。在密集杂乱场景中，后处理方法的"安全修正空间"小，内化方法可实现"预见性回避"。
- **风险:** AEGIS作者(清华RCSCT)可能将安全层内化——需监控。

**SafeVLA — 重要baseline:**
- **SafeLIBERO结果:** 否。使用自建Safety-CHORES基准。
- **代码状态:** 已开源 [GitHub](https://github.com/PKU-Alignment/SafeVLA)，含HuggingFace模型。
- **与我们的区别:** RL-based约束学习(CMDP) vs. 我们的几何方法(SDF梯度)。两种safety alignment范式的对比本身是有价值的论文贡献点。

**CoFreeVLA:**
- 聚焦双臂自碰撞(self-collision)而非环境障碍物避障。与我们问题设定不同，仅需related work简要提及。

**SafeLIBERO基准现状:** 目前**仅AEGIS一家**在SafeLIBERO上有结果。这既是机会（我们的结果将是第二个），也意味着缺乏多方对比数据。

---

## Category 3: Differentiable SDF in Robotics

这些方法在传统机器人规划中使用可微分SDF，**非VLA方法**，为我们的技术组件提供基础。

| 论文 | Venue / arXiv | 日期 | 方法概要 | 关系 | Baseline? | 代码 |
|------|--------------|------|---------|------|-----------|------|
| SAMP | arXiv 2509.11185 | Sep 2025 | 空间锚点网格上统一编码环境+机械臂SDF，碰撞感知运动策略 | `method-component` | No — 非VLA，但SDF梯度引导策略学习的关键参考 | 未开源 |
| Prof. Robot | CVPR 2025, arXiv 2503.11269 | Mar 2025 | 可微分机器人渲染中集成神经碰撞分类器+Eikonal正则化 | `method-component` | No — 非VLA，可微分SDF用于碰撞优化的关键参考 | [GitHub](https://github.com/qrcat/prof.robot) |
| CSSDF-Net | arXiv 2603.18669 | Mar 2026 | C-space连续可微SDF，spatial-hashing数据生成，零样本泛化 | `landscape` | No — 传统运动规划 | 未开源 |
| iSDF | RSS 2022, arXiv 2204.02296 | Apr 2022 | 在线MLP从深度流学习3D坐标→签名距离，提供碰撞代价和梯度 | `method-component` | No — 实时神经SDF的奠基工作 | [GitHub](https://github.com/facebookresearch/iSDF) |
| ReDSDF | IROS 2022, arXiv 2203.04739 | Mar 2022 | 正则化神经隐式距离场，任意尺度高维流形上的光滑距离场 | `method-component` | No — 反应式运动生成中SDF的关键参考 | [GitLab](https://git.ias.informatik.tu-darmstadt.de/ias_code/iros2022/redsdf) |
| Neural NMPC-SDF | IJRR 2025, arXiv 2511.21312 | Nov 2025 | 范围图像→潜向量→SDF解码，参数化NMPC碰撞约束 | `landscape` | No — 无人机导航，非操作 | [GitHub](https://github.com/ntnu-arl/sdf-nmpc) |
| CDFlow | arXiv 2509.13771 | Sep 2025 | Neural ODE建模C-space最小距离碰撞配置的完整分布 | `landscape` | No — C-space距离场理论工作 | 未开源 |
| CATNIPS | T-RO 2024, arXiv 2302.12931 | Feb 2023 | NeRF→Poisson点过程→概率碰撞约束+图搜索+样条优化 | `landscape` | No — 概率碰撞规避规划 | [GitHub](https://github.com/chengine/catnips) |

### 详细分析

**核心method-component参考:**

1. **SAMP** — 最接近我们技术路线的非VLA工作。在空间锚点上融合环境SDF+机器人SDF训练碰撞感知运动策略，碰撞率降低7%。证明SDF梯度可用于策略学习。我们将此范式迁移到VLA架构中。

2. **Prof. Robot** — CVPR 2025。证明可微分SDF可实现99%碰撞减少。Eikonal正则化确保梯度一致性的技术可借鉴。

3. **iSDF** — 实时神经SDF的奠基工作(Meta/Facebook Research)。在线从深度流训练MLP的范式与我们的SDF解码器设计相关。代码高质量开源。

4. **ReDSDF** — 正则化技术使SDF梯度场光滑，对我们的SDF-gradient-guided action refinement的梯度质量至关重要。

**整体观察:** SDF在机器人碰撞避障中的有效性已被充分验证(iSDF 2022 → SAMP 2025 → CSSDF-Net 2026)，但**所有工作都在传统运动规划框架内**，无一与VLA集成。这正是我们的gap。

---

## Category 4: Action Refinement VLAs

| 论文 | Venue / arXiv | 日期 | 方法概要 | 关系 | Baseline? | 代码 |
|------|--------------|------|---------|------|-----------|------|
| DFM-VLA | arXiv 2603.26320 | Mar 2026 | 离散流匹配迭代精修动作token序列，LIBERO 95.7% | `method-component` | No — 证明VLA内动作精修可行，但无碰撞引导 | 未开源，[项目页](https://chris1220313648.github.io/DFM-VLA/) |

### 详细分析

**DFM-VLA** 证明了VLA内部迭代动作精修的可行性——我们的SDF-gradient-guided action refinement是此范式的碰撞特化实例。区别：DFM-VLA的精修是通用的(离散流匹配驱动)，我们的精修是碰撞引导的(SDF梯度驱动)且单次前向传播(非迭代)。

---

## 补充论文 (Other)

| 论文 | Venue / arXiv | 日期 | 方法概要 | 关系 | 代码 |
|------|--------------|------|---------|------|------|
| OccVLA | arXiv 2509.05578 | Sep 2025 | 3D占用预测作为VLA隐式监督（自动驾驶） | `method-component` — 占用+VLA概念来源 | 未开源 |
| SparseOccVLA | arXiv 2601.06474 | Jan 2026 | 稀疏占用查询桥接视觉与语言(自动驾驶) | `landscape` | [GitHub](https://github.com/MSunDYY/SparseOccVLA) |
| ISS Policy | arXiv 2512.15020 | Dec 2025 | DiT扩散策略+隐式场景监督(点云→动作) | `landscape` | 未开源 |
| VLA Safety Survey | arXiv 2604.23775 | Apr 2026 | VLA安全综述：威胁/挑战/评估/机制 | `landscape` — 确认我们的gap | [Awesome-list](https://github.com/LiQiiiii/Awesome-VLA-Safety) |

---

## 关键发现

### 1. 必须对比的 Baselines（优先级排序）

| 优先级 | Baseline | 为什么必须对比 | 代码可用性 | 风险 |
|--------|----------|---------------|-----------|------|
| **P0** | AEGIS/VLSA | SafeLIBERO唯一已发表结果，post-hoc CBF vs. 我们的internalized SDF | 已开源 | 低 |
| **P0** | QDepth-VLA | 最近方法论对标，深度辅助监督 vs. SDF辅助监督 | 已开源 | 低 |
| **P0** | Vanilla VLA (π0/OpenVLA-OFT) | 无空间辅助监督的baseline | π0开源(openpi) | 低 |
| **P1** | SafeVLA | NeurIPS 2025 Spotlight，RL-based vs. geometric safety | 已开源 | 中 — 需适配到SafeLIBERO |
| **P1** | Spatial Forcing | ICLR 2026，通用3D对齐 vs. 碰撞特化SDF | 已开源 | 低 |
| **P2** | DepthVLA | 深度增强VLA代表(MoT架构) | 未开源 | 高 — 可能无法复现 |

### 2. 代码可用性风险

| 类别 | 总数 | 已开源 | 开源率 |
|------|------|--------|--------|
| Cat 1: 3D-aware VLAs | 14 | 5 (QDepth-VLA, 3D-CAVLA, Evo-0, SpatialVLA, Spatial Forcing) | 36% |
| Cat 2: Collision-safe VLAs | 3 | 2 (AEGIS, SafeVLA) | 67% |
| Cat 3: Diff SDF Robotics | 8 | 5 (Prof. Robot, iSDF, ReDSDF, Neural NMPC-SDF, CATNIPS) | 63% |
| Cat 4: Action Refinement | 1 | 0 | 0% |

**关键风险:** DepthVLA未开源（用QDepth-VLA替代），DFM-VLA未开源（仅作related work讨论非baseline），SAMP未开源（SDF梯度策略学习的关键参考需自行实现）。

**所有P0 baselines代码均可用**，实验计划不受代码可用性限制。

### 3. 与我们最近的工作及差异点

| 最近的工作 | 差异点 |
|-----------|--------|
| **AEGIS/VLSA** | Post-hoc CBF修正 vs. 我们的forward-pass SDF梯度引导。AEGIS不改变VLA内部表征，我们内化碰撞几何理解。 |
| **QDepth-VLA** | 2.5D深度辅助监督(相机帧) vs. 3D SDF辅助监督(工作空间帧)。QDepth无双向耦合无推理时梯度。 |
| **SAMP** | SDF梯度引导策略学习但非VLA。我们将SDF梯度引导迁移到VLA架构的action token空间。 |
| **DFM-VLA** | 通用动作精修(离散流匹配) vs. 碰撞特化精修(SDF梯度)。DFM-VLA是迭代的，我们是单次前向传播。 |
| **OccVLA** | 占用+VLA但在自动驾驶域。我们迁移到操作域+用SDF替代binary occupancy+加入梯度引导action generation。 |

### 4. SafeLIBERO 评测现状

- 目前**仅AEGIS/VLSA**在SafeLIBERO上有公开结果
- SafeVLA使用自建Safety-CHORES基准，CoFreeVLA使用真实机器人双臂任务
- 我们在SafeLIBERO上的结果将是**第二个公开结果**，直接与AEGIS可比
- SafeLIBERO数据集已在HuggingFace开放：[THURCSCT/SafeLIBERO](https://huggingface.co/datasets/THURCSCT/SafeLIBERO)

### 5. 需监控的竞争团队

| 团队 | 关注点 |
|------|--------|
| 清华RCSCT (AEGIS作者) | 是否将安全层从post-hoc内化到VLA架构 |
| OccVLA作者团队 | 是否将占用场从自动驾驶扩展到操作 |
| Spatial Forcing作者 (OpenHelix) | 是否将3D对齐特化到碰撞避障 |
| PKU-Alignment (SafeVLA作者) | 是否从RL转向几何方法 |
