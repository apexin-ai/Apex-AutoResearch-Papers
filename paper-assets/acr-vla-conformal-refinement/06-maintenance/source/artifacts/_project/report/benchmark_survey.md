# VLA Benchmark 调研报告：超越 LIBERO

**日期**: 2026-05-19

---

## 1. Benchmark 对比总表

| Benchmark | 任务数 | Action Space | VLA Baseline 可用性 | Demo Data | 迁移难度 | 优先级 |
|-----------|--------|-------------|---------------------|-----------|----------|--------|
| **LIBERO-Goal** | 10 | 7D 连续 (delta EEF 6D + gripper 1D) | SmolVLA/pi0/OpenVLA checkpoint 已有 | 50 demos/task, HF 已有 | ★☆☆☆☆ 极低 | **P0** |
| **LIBERO-10 (Long)** | 10 | 同上 | 同上 | 同上 | ★☆☆☆☆ 极低 | **P0** |
| **CALVIN (ABC→D)** | 34 | 7D 连续 (delta EEF pos 3D + euler rot 3D + gripper 1D) | 无现成 SmolVLA checkpoint，需 fine-tune | ~23K trajectories, HF 有 LeRobot 格式 | ★★★☆☆ 中等 | **P1** |
| **SimplerEnv (Bridge)** | ~15 | 7D 连续 (delta xyz + axis-angle rot + gripper) | 无 SmolVLA-Bridge checkpoint | 评估专用，无自有 demo；依赖 Bridge V2 (~60K traj) | ★★★☆☆ 中等 | **P2** |
| **ManiSkill2/3** | 20+ families | 可配置 4-8D；`pd_ee_delta_pose` = 7D | Octo/RDT-1B 有 baseline，无 SmolVLA checkpoint | 4M+ frames, HF 有 | ★★★☆☆ 中等 | **P3** |
| **RLBench** | 100 (18-task subset) | 8D keyframe (SE3 pose + gripper + collision) | PerAct/RVT 等 3D 方法为主，无 VLA checkpoint | 100 demos/task, HF 有 | ★★★★☆ 高 | **P4** |
| **MetaWorld** | 50 | **4D** (delta pos 3D + gripper 1D, 无旋转) | SmolVLA 已评估 (68.24%), LeRobot 原生支持 | lerobot/metaworld_mt50 | ★★☆☆☆ 低 | **P4** |

### 关键字段说明
- **迁移难度**: 从当前 LIBERO pipeline 迁移所需的工程量
- **优先级**: P0 = 立即可做, P1 = 值得投入, P2-P3 = 有条件可做, P4 = 不推荐

---

## 2. LIBERO 同系列扩展（P0，最容易）

### LIBERO-Goal (10 tasks)
- **与当前实验的区别**: LIBERO-Object/Spatial 测试不同物体/空间布局的泛化，Goal 测试相同初始场景下不同目标的泛化
- **Action space**: 完全相同 — 7D (delta EEF 6D + gripper 1D), 20Hz, robosuite OSC
- **Demo data**: 50 demos/task，已在 `HuggingFaceVLA/libero` 数据集中（包含 Spatial+Object+Goal+10）
- **SmolVLA checkpoint**: `lerobot/smolvla_libero` 或 `HuggingFaceVLA/smolvla_libero` 已包含 Goal suite 训练
- **Episode 长度**: max 300 steps (longest demo ~270)
- **CRM 迁移**: **零代码改动**。只需在评估脚本中切换 suite name
- **预估工时**: < 0.5 天（含 CRM 重训练和评估）

### LIBERO-10 / LIBERO-Long (10 tasks)
- **特点**: 长 horizon 多步骤任务，最高 520 steps per episode
- **与 Object/Spatial 的区别**: 每个任务需要链式完成多个子目标（如 "pick up X → place on Y → open Z"）
- **SmolVLA 表现**: 仅 56-71%（显著低于 Object 93-96% 和 Spatial 63-90%），CRM 有更大改进空间
- **Demo data**: 同上，已在 HF 数据集中
- **CRM 迁移**: **零代码改动**
- **预估工时**: < 0.5 天
- **额外价值**: 长 horizon 任务上的提升更有说服力（error compounding 效应更显著，correction 价值更大）

### LIBERO-90 (90 tasks)
- **特点**: 90 个任务，测试大规模多任务泛化
- **Demo data**: `IPEC-COMMUNITY/libero_90_no_noops_lerobot` (569K frames)
- **评估成本**: 90 个任务 × 50 trials = 大量 GPU 时间
- **优先级**: 可选，如果时间充足

### LIBERO 扩展的论文价值
在 Object + Spatial 基础上加 Goal + Long 可以构成完整的 LIBERO 4-suite 评估（社区标准协议）。LIBERO-Long 的提升对论文叙事尤其有价值：CRM 在 error-compounding 严重的长 horizon 任务上效果更突出，印证了 correction 而非 selection 的核心论点。

---

## 3. Top-3 推荐 Benchmark

### 推荐 1: LIBERO-Goal + LIBERO-Long（P0，必做）

**理由**:
1. **零迁移成本**: 相同框架、相同 checkpoint、相同 action space，只需切换 suite 配置
2. **社区标准**: 几乎所有 VLA 论文都报告 4-suite 结果，只报 2 个 suite 会被 reviewer 质疑
3. **叙事价值**: LIBERO-Long 上 SmolVLA 仅 56-71%，CRM 有更大改进空间；长 horizon 任务的 error compounding 天然适合 correction 方法
4. **评估成本**: ~2-4 GPU-hours（RTX 4090），含 CRM 训练 + 评估

**迁移路线图**:
1. 在现有 precompute pipeline 中指定 Goal/Long suite → 生成 VLA prediction 数据（~1h）
2. 用相同 CRM 架构训练（可能需要 per-suite 或 unified 训练）（~1h）
3. 评估 10 tasks × 50 trials per suite（~2h）
4. 统计分析 + 表格更新（~0.5h）

### 推荐 2: CALVIN ABC→D（P1，强烈建议）

**理由**:
1. **Action space 直接兼容**: 7D (delta EEF pos 3D + euler rot 3D + gripper 1D)，与 LIBERO 结构相同
2. **跨 benchmark 泛化**: 证明方法不仅在 LIBERO 上有效，对 reviewer 说服力大增
3. **长 horizon 链式评估**: CALVIN 的 5-subtask chain 评估天然适合 correction 方法——前序步骤的小误差会 compound 到后续步骤
4. **社区认可度**: CALVIN 是仅次于 LIBERO 的第二大 VLA 操作 benchmark
5. **丰富的 demo data**: ~23K trajectories（远多于 LIBERO 的 500 total demos）

**迁移路线图**:
1. **获取/训练 SmolVLA-CALVIN checkpoint**（最大瓶颈）
   - 检查 HF 上是否已有 SmolVLA-CALVIN checkpoint
   - 若无，用 `fywang/calvin-task-ABCD-D-lerobot` 数据 fine-tune SmolVLA（~4h on A100）
   - 或用 pi0-CALVIN checkpoint 替代（如存在）
2. **适配 observation preprocessing**
   - CALVIN 用 PyBullet，观测格式略不同（需调整 image key 和 state 维度）
   - 旋转表示：CALVIN 用 euler angles，LIBERO 用 axis-angle → 可能需要转换
3. **CRM 训练**
   - 运行 frozen VLA 在 CALVIN demos 上生成 predictions
   - 用 (prediction, ground-truth) pairs 训练 CRM（~2h）
4. **评估**
   - CALVIN ABC→D protocol：1000 chains × 5 subtasks
   - 需要搭建 CALVIN 环境（PyBullet）
5. **预估总工时**: 1-2 周（含 SmolVLA fine-tune + 环境搭建 + 调试）
6. **预估 GPU-hours**: ~20-30h（fine-tune ~4h + precompute ~6h + CRM training ~2h + evaluation ~10h + 调试 buffer）

**风险**: SmolVLA 在 CALVIN 上的 baseline 表现未知。若 baseline 已很高（>90%），CRM 的改进空间有限。

### 推荐 3: SimplerEnv / Bridge V2（P2，可选）

**理由**:
1. **Real-to-sim 桥梁**: SimplerEnv 是专门评估真实世界 VLA 在仿真中表现的 benchmark，"我们的方法在 real-to-sim 迁移场景也有效"对 reviewer 有独特说服力
2. **Action space 兼容**: 7D (delta xyz + axis-angle rot + gripper)，与 LIBERO 完全相同
3. **训练数据丰富**: Bridge V2 有 ~60K trajectories（`jesbu1/bridge_v2_lerobot`）

**迁移路线图**:
1. **获取 SmolVLA-Bridge checkpoint**（最大瓶颈）
   - 检查是否有现成 checkpoint
   - 若无，需 fine-tune SmolVLA on Bridge V2 data（~6-8h on A100）
2. **安装 SimplerEnv**（基于 SAPIEN/ManiSkill2）
3. **CRM 训练**: 在 Bridge V2 demos 上 precompute + 训练
4. **评估**: SimplerEnv Visual Matching + Variant Aggregation protocols
5. **预估总工时**: 2-3 周
6. **预估 GPU-hours**: ~40-50h

**风险**: SimplerEnv 任务较简单（pick coke can, open drawer），可能看不到显著改进。且需要处理不同 robot embodiment（WidowX vs Franka）。

---

## 4. 不推荐的 Benchmark

### RLBench — 不推荐（P4）
- **根本问题**: 主流方法（PerAct, RVT）使用 **keyframe-based** action space，预测下一个关键帧的 SE3 pose，而非连续控制。与 flow-matching VLA + continuous correction pipeline 根本不兼容
- **VLA 社区不常用**: 近期 VLA 论文（OpenVLA, pi0, SmolVLA）均未在 RLBench 上评估
- **迁移成本**: 需要重新定义 action space 或将 keyframe 转换为连续控制，工程量巨大

### MetaWorld — 不推荐（P4）
- **Action space 不兼容**: 仅 4D (pos 3D + gripper 1D)，**无旋转控制**
- CRM 的核心设计是 6D correction (3 pos + 3 rot)，在 MetaWorld 上退化为 3D pos-only correction
- 尽管 SmolVLA/LeRobot 原生支持，action space 差异使得实验结果无法与 LIBERO 直接对比
- 任务过于简单，不足以展示 correction 方法的价值

### ManiSkill2/3 — 暂不推荐（P3）
- 可配置 7D action space，理论上兼容
- 但无 SmolVLA checkpoint，社区 VLA 评估较少
- 环境搭建（SAPIEN）和 demo 格式转换工作量不小
- 对论文增量价值不如 CALVIN

---

## 5. 各 Benchmark 详细信息

### 5.1 SmolVLA 已有 Checkpoint 与评估

| Checkpoint | Benchmark | 表现 |
|------------|-----------|------|
| `lerobot/smolvla_base` | 预训练 base (450M) | — |
| `HuggingFaceVLA/smolvla_libero` | LIBERO 4-suite | Spatial 90%, Object 96%, Goal 92%, Long 71% |
| SmolVLA 2.25B | LIBERO avg | 88.75% |
| SmolVLA 2.25B | MetaWorld avg | 68.24% |

### 5.2 其他 VLA 在各 Benchmark 上的表现

**LIBERO** (社区标准):
| Model | Spatial | Object | Goal | Long | Avg |
|-------|---------|--------|------|------|-----|
| SmolVLA 0.45B | 90% | 96% | 92% | 71% | 87.3% |
| OpenVLA-OFT | 97.6% | 98.4% | 97.9% | 94.5% | 97.1% |
| pi0.5 | — | — | — | — | 96.85% |
| Cosmos-Policy | — | — | — | — | 98.5% |
| SRPO | — | — | — | — | ~97% (std) / 82.1% (Plus) |

**CALVIN** (ABC→D, avg chain length out of 5):
| Model | Avg Chain Length |
|-------|-----------------|
| RoboFlamingo | 2.48 |
| SuSIE | 2.69 |
| GR-1 | 3.06 |
| 3D Diffuser Actor | 3.83 |

**SimplerEnv**: RT-1, RT-1-X, RT-2-X, Octo, OpenVLA 均有评估。SmolVLA 无报告。

### 5.3 Demo Data 可用性汇总

| Benchmark | HuggingFace Dataset | 格式 | 规模 |
|-----------|-------------------|------|------|
| LIBERO (all suites) | `HuggingFaceVLA/libero` | LeRobot v3 | 273K frames, 1693 eps |
| LIBERO-90 | `IPEC-COMMUNITY/libero_90_no_noops_lerobot` | LeRobot | 569K frames |
| CALVIN | `fywang/calvin-task-ABCD-D-lerobot` | LeRobot | ~23K trajectories |
| Bridge V2 | `jesbu1/bridge_v2_lerobot` | LeRobot | ~60K trajectories |
| MetaWorld | `lerobot/metaworld_mt50` | LeRobot | 50 tasks |
| ManiSkill2 | `haosulab/ManiSkill_Demonstrations` | HDF5 | 4M+ frames |
| RLBench | `hqfang/rlbench-18-tasks` | HF | 18 tasks × 100 demos |

---

## 6. 迁移的核心瓶颈

所有跨 benchmark 迁移的 **共同瓶颈** 是：CRM 依赖 SmolVLA 的 `obs_features`（960D VLM hidden states）。这意味着：

1. **需要目标 benchmark 上的 SmolVLA checkpoint** — CRM 输入的 obs features 必须来自在该 benchmark 上训练过的 VLA，否则特征语义不匹配
2. **需要在该 benchmark 的 demo data 上运行 frozen VLA** — 生成 (predicted_action, ground_truth_action, obs_features) 三元组用于 CRM 训练
3. **CRM 架构本身是 benchmark-agnostic 的** — MLP 结构不需要改，只是输入维度可能因 action dim 不同而微调

**LIBERO 同系列扩展绕开了这个瓶颈**：SmolVLA-LIBERO checkpoint 已经覆盖 Goal/Long suite。

---

## 7. 行动建议

### 立即执行（本周内）
1. 在 LIBERO-Goal 和 LIBERO-Long 上运行 CRM pipeline — **零代码改动，只改配置**
2. 将结果加入论文的 main results table，构成完整 4-suite 评估

### 近期可选（1-2 周）
3. 调查 CALVIN 的可行性：
   - 搜索是否存在 SmolVLA-CALVIN 或 pi0-CALVIN checkpoint
   - 若有，评估迁移工作量
   - 若无，估算 fine-tune SmolVLA on CALVIN 的成本

### 论文策略
- **最低要求**: LIBERO 4-suite (Spatial + Object + Goal + Long) — 社区标准
- **加分项**: + CALVIN 或 SimplerEnv — 证明跨 benchmark 泛化
- **理想情况**: 4-suite LIBERO + LIBERO-Plus (robustness) + CALVIN — 全面覆盖

---

## 8. 参考来源

- SmolVLA Paper: arXiv:2506.01844
- SmolVLA HuggingFace: huggingface.co/blog/smolvla
- LeRobot Docs: huggingface.co/docs/lerobot
- LIBERO GitHub: github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN GitHub: github.com/mees/calvin
- SimplerEnv GitHub: github.com/simpler-env/SimplerEnv
- BridgeData V2: rail-berkeley.github.io/bridgedata
- ManiSkill3 Docs: maniskill.readthedocs.io
- RLBench GitHub: github.com/stepjam/RLBench
- MetaWorld GitHub: github.com/Farama-Foundation/Metaworld
- OpenVLA-OFT: openvla-oft.github.io
- LIBERO-Plus: arXiv:2510.13626
- LIBERO-PRO: arXiv:2510.03827
