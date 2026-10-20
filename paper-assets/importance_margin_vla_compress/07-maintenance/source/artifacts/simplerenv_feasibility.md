# SimplerEnv 可行性调研报告

**日期**: 2026-05-24

## 1. SimplerEnv 概述

**仓库**: [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) (CoRL 2024, ICLR 2025)

**核心**：基于 SAPIEN + ManiSkill2 的仿真评估框架，用于评估真实世界机器人操控策略在仿真环境中的表现。

### 支持的 Tasks（9 个预设环境）

**Google Robot（控制频率 3Hz）**：
- Pick Coke Can / Pick Random Object / Move Near
- Open/Close Drawer / Place in Closed Drawer

**WidowX Bridge（控制频率 5Hz）**：
- Spoon on Towel / Carrot on Plate / Stack Cube / Eggplant in Basket

### 支持的 VLA 模型
- RT-1 / RT-1-X（原生支持）
- Octo（原生支持）
- **OpenVLA**（通过 [DelinQu fork](https://github.com/DelinQu/SimplerEnv-OpenVLA) 集成）
- **π0 / π0-FAST**（通过 openpi/lerobot 集成，已有社区支持）
- π0.5：**存在已知问题**（[openpi#799](https://github.com/Physical-Intelligence/openpi/issues/799)），SimplerEnv 上性能不稳定

### 评估方式
- **Visual Matching**：将真实图像叠加到仿真背景
- **Variant Aggregation**：多种环境变体（背景、光照、干扰物）取平均

### 版本
- **ManiSkill2（主分支）**：CPU 仿真，9 个 tasks，成熟稳定
- **ManiSkill3 分支**：GPU 加速 10-15x，但只移植了 4 个 Bridge tasks

## 2. 与 LIBERO 的互补性

| 维度 | LIBERO | SimplerEnv |
|------|--------|------------|
| 定位 | 终身学习/知识迁移 | 仿真复现真实策略 |
| Tasks | 130 个，分 4 个 suite | 9 个预设，多变体 |
| 机器人 | Franka Panda (tabletop) | Google Robot + WidowX |
| 观测 | 多相机 (agentview + wrist) | 单相机 (obs_camera) |
| 动作空间 | 7-DoF (delta pos + gripper) | world_vector + rot_axangle + gripper |
| 评估指标 | 成功率 (per-task, per-suite) | 成功率 (visual matching / variant agg) |
| GPU 需求 | 渲染用 EGL | 需 RTX GPU（ray-tracing） |

**互补性**：LIBERO 测试 long-horizon + 多任务泛化，SimplerEnv 测试 sim-to-real 保真度。论文中两个 benchmark 同时报告可以展示方法的全面性。

## 3. 竞品分析（Token Pruning for VLA）

### 已有工作在 SimplerEnv 上的评估

| 方法 | 发表 | SimplerEnv | LIBERO | 核心思路 |
|------|------|-----------|--------|---------|
| **SP-VLA** | arXiv 2506.12723 | ✅ 2.4x加速+6%提升 | ✅ 1.5x无损加速 | 动作感知调度 + 时空token pruning |
| **DTP** | arXiv 2601.16065 | ✅ SIMPLER benchmark | ❓ | 去除task无关区域的干扰token |
| **Compressor-VLA** | arXiv 2511.18950 | ❌ | ✅ 59% FLOPs↓ | 指令引导的视觉token压缩（cross-attn） |
| **LightVLA** | arXiv 2509.12594 | ✅ | ✅ | 可微分token pruning |
| **EfficientVLA** | OpenReview | ✅ | ❓ | Training-free 加速+压缩 |
| **Ours** | - | 🔜 | ✅ | Importance margin + smart compress |

**关键发现**: SP-VLA 是最直接的竞品，已在 SimplerEnv 上证明 token pruning 的有效性。我们需要在 SimplerEnv 上也能展示结果。

## 4. Pruning 适配方案

### SimplerEnv Policy 接口

```python
class PolicyInterface:
    def __init__(self, ...):        # 加载模型
    def reset(self, task_description): # 重置 episode 状态
    def step(self, image, task_description) -> (raw_action, action):
        # action = {world_vector: [3], rot_axangle: [3], gripper: [1], terminate_episode: [1]}
    def visualize_epoch(self, predicted_actions, images, save_path): # 可视化
```

### 当前 LIBERO 评估的 pruning 机制

**π0.5**（`eval_pi05_pruning_libero.py`）：
- 用 `types.MethodType` monkey-patch `policy.model.embed_prefix`
- 在 vision token embedding 后、进入 LLM 前截取并 prune
- Prune 策略：random / l2norm / attention-probe
- 完全在模型层面操作，与 env 无关

**OpenVLA**（`eval_openvla_l2norm_libero.py`）：
- 用 PyTorch forward hook 注册在 `multi_modal_projector` 输出
- Hook 截取 vision token embedding 并 prune
- 同样完全在模型层面

### SimplerEnv 适配所需改动

**关键洞察：pruning hook 与环境无关，只需替换 env loop。**

#### OpenVLA 适配（预计 2-3 小时）
1. 创建 `OpenVLAPruningPolicy` 类，实现 SimplerEnv 接口 (`reset` + `step`)
2. 在 `__init__` 中加载 OpenVLA + 注册 pruning hook（复用现有 hook 代码）
3. `step(image, task_description)` 中：图像预处理 → 推理 → 动作后处理
4. 动作映射：OpenVLA 输出 7-DoF → SimplerEnv `{world_vector, rot_axangle, gripper}` 格式
5. 参考 DelinQu fork 的 `simpler_env/policies/openvla/` 实现

#### π0.5 适配（预计 4-6 小时）
1. **难点**：π0.5 期望 3 个相机视角，SimplerEnv 默认只有 1 个 obs camera
   - 方案 A：重复单相机图像填充多视角 slot（损失信息但可行）
   - 方案 B：修改 SimplerEnv 环境增加额外相机（需要改 env 配置）
   - 方案 C：用 π0 而非 π0.5（π0 单相机更自然）
2. **动作映射**：π0.5 输出 action chunk → 取第一个动作 → 映射到 SimplerEnv 格式
3. **已知风险**：π0.5 在 SimplerEnv 上表现不稳定（openpi#799），可能需要额外调试

#### 建议优先级
1. **先做 OpenVLA**：适配简单，已有社区验证，baseline 数据充足
2. **π0.5 视情况**：如果 OpenVLA 结果好，再评估 π0.5 必要性

## 5. 安装状态

### 服务器 westd-27271
- **GPU**: 2x NVIDIA RTX PRO 6000 Blackwell (94GB each)
- **CUDA**: 12.8
- **磁盘**: 75GB 可用于 /root/autodl-tmp/
- **环境**: conda `simpler_env` (Python 3.10.20)

### 已验证 ✅
- SimplerEnv 仓库 clone（含 ManiSkill2_real2sim 子模块）路径：`/root/autodl-tmp/SimplerEnv/`
- ManiSkill2_real2sim 安装 (`pip install -e .`)
- SimplerEnv 安装 (`pip install -e .`)
- conda 环境 `simpler_env` 创建
- PyTorch 2.11.0+cu128 安装验证（torch.cuda.is_available() = True, 2 GPUs）
- Vulkan + SAPIEN 运行时依赖
- `import simpler_env` 成功
- `import mani_skill2_real2sim` 成功
- `import sapien.core` 成功

### 待完成
- ⬜ 端到端渲染测试（创建 env + 渲染一帧）
- ⬜ 下载 RT-1-X 或 OpenVLA checkpoint 进行 baseline 评估
- ⬜ Visual matching overlay 图片下载
- ⬜ 编写 OpenVLA pruning policy adapter

## 6. 建议实验方案

### Phase 1: OpenVLA Baseline（2-3 天）
- **Tasks**: 全部 9 个 SimplerEnv 预设环境
- **Episodes**: 每个 task 50 episodes（visual matching）
- **模型**: openvla-7b-finetuned（已在服务器上有多个版本）
- **Pruning sweeps**: keep_ratio = [1.0, 0.9, 0.8, 0.7, 0.5, 0.3]
- **预计时间**: 单 task baseline ~30min，全 sweep ~6h/task，总计 ~54h

### Phase 2: π0.5（可选，3-5 天）
- 先解决多相机 vs 单相机的适配问题
- 选 3-4 个代表性 tasks
- 与 SP-VLA 数据对比

### 关键对比
- Our method vs SP-VLA（在 SimplerEnv 上最直接的竞品）
- SimplerEnv 结果 + LIBERO 结果 = 论文更有说服力的 evaluation section
