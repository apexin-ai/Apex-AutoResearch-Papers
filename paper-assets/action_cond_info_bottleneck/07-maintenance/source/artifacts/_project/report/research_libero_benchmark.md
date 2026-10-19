# LIBERO Benchmark + LIBERO-Plus 调研报告

调研日期：2026-05-15

---

## 1. LIBERO Benchmark

### 1.1 基本信息

| 项目 | 内容 |
|------|------|
| 论文 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) (NeurIPS 2023 D&B) |
| GitHub | https://github.com/Lifelong-Robot-Learning/LIBERO |
| 项目主页 | https://libero-project.github.io |
| License | MIT (代码), CC BY 4.0 (数据集) |
| 模拟器 | robosuite (MuJoCo) |
| 机器人 | Franka Panda 7-DOF |

### 1.2 安装

**方式 A：pip**
```bash
pip install libero
```

**方式 B：from source（推荐）**
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
pip install -e .
```

**方式 C：通过 LeRobot**
```bash
pip install -e ".[libero]"
```

无头渲染需设置：`export MUJOCO_GL=egl`

### 1.3 五个 Task Suite

所有任务都是 language-conditioned manipulation，使用 Franka Panda 机械臂。

| Suite | CLI 名称 | 任务数 | 描述 |
|-------|----------|--------|------|
| **LIBERO-Spatial** | `libero_spatial` | 10 | 同一目标（拿黑碗放盘子），碗在不同空间位置。测试 **空间关系知识** 迁移 |
| **LIBERO-Object** | `libero_object` | 10 | 同一目标结构（拿 X 放篮子），不同物体。测试 **物体知识** 迁移 |
| **LIBERO-Goal** | `libero_goal` | 10 | 同一场景，不同目标（开抽屉、放碗到炉子上等）。测试 **目标/程序知识** 迁移 |
| **LIBERO-90** | `libero_90` | 90 | LIBERO-100 中的短期任务，跨 spatial/object/goal 的混合分布偏移。用于 **预训练** |
| **LIBERO-Long** | `libero_10` | 10 | LIBERO-100 中的长期多步骤任务。用于预训练后的 **下游评测** |

**LIBERO-Spatial 示例任务（全部 10 个）：**
1. pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate
2. pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
3. pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate
4. pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate
5. pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate
6. pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate
7. pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate
8. pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate
9. pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
10. pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate

**LIBERO-Object 示例任务：** pick_up_the_{alphabet_soup, cream_cheese, salad_dressing, bbq_sauce, ketchup, tomato_sauce, butter, milk, chocolate_pudding, orange_juice}_and_place_it_in_the_basket

**LIBERO-Goal 示例任务：** open_the_middle_drawer_of_the_cabinet, put_the_bowl_on_the_stove, put_the_wine_bottle_on_top_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, put_the_bowl_on_top_of_the_cabinet, push_the_plate_to_the_front_of_the_stove, put_the_cream_cheese_in_the_bowl, turn_on_the_stove, put_the_bowl_on_the_plate, put_the_wine_bottle_on_the_rack

### 1.4 数据下载

每个任务有 **50 条人类遥操作演示**，通过 SpaceMouse 以 20 Hz 采集。

**方式 A：官方脚本**
```bash
# 全部下载
python benchmark_scripts/download_libero_datasets.py

# 下载特定 suite
python benchmark_scripts/download_libero_datasets.py --datasets libero_spatial
python benchmark_scripts/download_libero_datasets.py --datasets libero_object
python benchmark_scripts/download_libero_datasets.py --datasets libero_goal
python benchmark_scripts/download_libero_datasets.py --datasets libero_100  # 含 libero_90 + libero_10

# 通过 HuggingFace 下载（推荐，原始链接可能过期）
python benchmark_scripts/download_libero_datasets.py --use-huggingface
```

默认下载位置：LIBERO 根目录下的 `./datasets/`

**方式 B：HuggingFace 直接下载**

| 数据集 | 格式 | 大小 |
|--------|------|------|
| `yifengzhu-hf/LIBERO-datasets` | 原始 HDF5 | ~100 GB 总计 |
| `physical-intelligence/libero` | LeRobot (Parquet) | ~34.9 GB |
| `HuggingFaceVLA/libero` | LeRobot | ~1.9 GB |
| `lerobot/libero` | LeRobot (视频 AV1) | ~1.94 GB |

**各 suite 近似大小（原始 HDF5 格式）：**

| Suite | 大小 |
|-------|------|
| libero_spatial | ~6.6 GB |
| libero_object | ~9.3 GB |
| libero_goal | ~6-9 GB |
| libero_10 (Long) | ~12.8 GB |
| libero_90 | ~60-70 GB |
| **总计** | **~100 GB** |

### 1.5 数据格式

**文件格式：** HDF5（每个任务一个 `.hdf5` 文件）

**HDF5 结构：**
```
data/
  demo_0/
    obs/
      agentview_rgb          # (T, 128, 128, 3) uint8 — 第三人称相机
      eye_in_hand_rgb        # (T, 128, 128, 3) uint8 — 腕部相机
      gripper_states         # (T, 1) — 夹爪开合度
      joint_states           # (T, 7) — 7 个关节角度
      ee_states              # (T, 6) — 末端执行器位置 + 轴角朝向
      ee_pos                 # (T, 3) — 末端执行器 xyz 位置
      ee_ori                 # (T, 3) — 末端执行器轴角朝向
    actions                  # (T, 7) — 7-DOF 动作
    states                   # (T, D) — 完整模拟器状态
    robot_states             # (T, D) — gripper_pos + ee_pos + ee_quat 拼接
    rewards                  # (T,) — 稀疏: 全 0，最后成功步为 1
    dones                    # (T,) — episode 结束时为 1
  demo_1/ ...
  demo_49/ ...
```

**观测空间：**

| 键 | 维度 | 含义 |
|----|------|------|
| `agentview_rgb` (→ `agentview_image`) | (128, 128, 3) | 工作区 RGB 图像 |
| `eye_in_hand_rgb` (→ `robot0_eye_in_hand_image`) | (128, 128, 3) | 腕部 RGB 图像 |
| `gripper_states` (→ `robot0_gripper_qpos`) | (1,) 或 (2,) | 夹爪指位置 |
| `joint_states` (→ `robot0_joint_pos`) | (7,) | Franka Panda 7 关节角 |
| `ee_pos` | (3,) | 末端执行器 xyz 位置 |
| `ee_ori` | (3,) | 末端执行器轴角朝向 |

**LeRobot 格式中** proprioceptive state 为 8 维：`observation.state` = [ee_pos (3) + ee_axis_angle (3) + gripper_qpos (2)]

**动作空间：**

| 维度 | 含义 |
|------|------|
| 0-2 | 末端执行器位置增量 (dx, dy, dz) |
| 3-5 | 末端执行器朝向增量 (轴角 / 欧拉角) |
| 6 | 夹爪命令 (1=闭合, -1=打开) |

- 总计 **7 维连续动作**，Box(-1, 1, shape=(7,))
- 控制模式：**OSC_POSE**（操作空间控制）
- 频率：**20 Hz**（原始），LeRobot 格式 **10 Hz**
- 支持 `relative`（增量，默认）和 `absolute` 两种控制模式
- 奖励：稀疏 — 中间步全 0，任务完成时 +1

### 1.6 评测

**原生 LIBERO 评测：**

```bash
python libero/lifelong/evaluate.py \
  --benchmark LIBERO_SPATIAL \
  --task_id 0 \
  --algo base \
  --policy bc_transformer_policy \
  --seed 10000 \
  --ep 50 \
  --load_task 0 \
  --device_id 0
```

参数说明：
- `--benchmark`: `LIBERO_SPATIAL` / `LIBERO_OBJECT` / `LIBERO_GOAL` / `LIBERO_90` / `LIBERO_10`
- `--task_id`: suite 内的任务索引
- `--algo`: 终身学习算法 (`base`, `er`, `ewc`, `packnet`, `multitask`)
- `--policy`: 策略架构 (`bc_rnn_policy`, `bc_transformer_policy`, `bc_vilt_policy`)
- `--save-videos`: 可选，录制评测视频

**评测协议：**
- 20 个并行环境同时运行 (`n_eval: 20`, `num_procs: 20`)
- 每个 episode 最多 600 步 (`max_steps: 600`)
- 开头 5 步零动作用于物理稳定
- episode 在 `done=True` 或达到最大步数时终止

**输出指标：**
- **Success rate** = num_success / num_envs（每个任务）
- **Loss** = 测试集损失
- 结果保存路径：`{save_dir}/{benchmark}_{algo}_{policy}_{seed}_[ep|load]_{task_id}.stats`

**终身学习指标（跨任务序列）：**
- **FWT (Forward Transfer)**: 序列训练后在新任务上的成功率
- **NBT (Negative Backward Transfer)**: 早期任务性能退化（灾难性遗忘）
- **AUC (Area Under Curve)**: 综合 FWT 和 NBT 的累积成功率

**原生训练命令：**
```bash
export CUDA_VISIBLE_DEVICES=0 && \
export MUJOCO_EGL_DEVICE_ID=0 && \
python libero/lifelong/main.py seed=10000 \
  benchmark_name=LIBERO_SPATIAL \
  policy=bc_transformer_policy \
  lifelong=base
```

**LeRobot 评测：**
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```
标准协议：每个任务 10 个 episode，4 个标准 suite = 400 个 episode。

---

## 2. LIBERO-Plus 扰动评测

### 2.1 基本信息

| 项目 | 内容 |
|------|------|
| 论文 | [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626) (CVPR 2026) |
| GitHub | https://github.com/sylvestf/LIBERO-plus |
| 项目主页 | https://sylvestf.github.io/LIBERO-plus/ |
| HF 资产 | https://huggingface.co/datasets/Sylvest/LIBERO-plus |
| 训练数据 (RLDS) | https://huggingface.co/datasets/Sylvest/libero_plus_rlds |
| LeRobot 格式 | https://huggingface.co/datasets/lerobot/libero_plus |

### 2.2 LIBERO-Plus 是什么

在原始 LIBERO 基础上增加了：
- **10,030 个任务变体**，通过系统化扰动生成
- **7 个扰动维度**，**21 个子维度**
- **5 个难度级别** (L1-L5)，按多模型共识分层（4 个参考模型中几个能解决该任务）
- **20,000+ 训练轨迹**（RLDS 格式）
- 与 vanilla LIBERO 完全兼容的 drop-in replacement

### 2.3 七个扰动维度（精确定义）

#### 2.3.1 物体布局 (Objects Layout)
- **O1 — 干扰物体 (Confounding objects):** 从 416 个物体池中随机添加 n 个未见过的干扰物体，通过修改 BDDL 任务描述文件实现
- **O2 — 目标位移 (Target displacement):** 对目标物体初始位置 (x, y, z) 和朝向施加随机扰动，保持语义关系

#### 2.3.2 相机视角 (Camera Viewpoints)
- **C1 — 距离缩放 (Distance scaling):** 沿光轴将相机距离缩放 1.01x-2.00x
- **C2 — 球坐标位置 (Spherical position):** 改变方位角 (delta-theta) 和仰角 (delta-phi)，范围 15-75 度
- **C3 — 朝向扰动 (Orientation perturbation):** 扰动 yaw/pitch/roll，范围 2-10 度

实现：修改 `Problem` 类接口；主要针对第三人称相机（非腕部相机）

#### 2.3.3 机器人初始状态 (Robot Initial States)
- 对机械臂初始关节位置施加随机扰动，幅度 0.1-0.5
- 实现：修改 `Problem` 类接口

#### 2.3.4 语言指令 (Language Instructions)
- **R1 — 干扰改写 (Distraction rewrites):** 添加与任务无关的上下文信息
- **R2 — 常识替换 (Commonsense substitution):** 用常识性替代描述替换物体名称
- **R3 — 推理复杂度 (Reasoning complexity):** 改变多步骤任务的推理复杂度
- 实现：基于 LLM 的指令改写

#### 2.3.5 光照条件 (Light Conditions)
- **L1 — 漫射颜色 (Diffuse color):** RGB 通道漫射光照调整
- **L2 — 方向 (Direction):** 平行光源方向变化
- **L3 — 镜面强度 (Specular intensity):** 镜面高光强度（反射表面）
- **L4 — 阴影 (Shadow casting):** 阴影开关控制
- 实现：修改 MuJoCo 场景 XML 定义文件，注册新场景类

#### 2.3.6 背景纹理 (Background Textures)
- **B1 — 场景纹理 (Scene texture):** 使用 950 张精选纹理通过 XML 场景文件替换环境纹理
- **B2 — 表面纹理 (Surface texture):** 随机改变工作表面纹理（桌面、地板）
- 实现：修改 XML 场景定义文件，添加新纹理资产

#### 2.3.7 传感器噪声 (Sensor Noise)
图像空间后处理（非物理层级）：
- **N1 — 运动模糊 (Motion blur):** kernel 半径 r=5-35，高斯 sigma=2-20，角度 U(-45, 45)度
- **N2 — 高斯模糊 (Gaussian blur):** sigma 1-10
- **N3 — 缩放模糊 (Zoom blur):** 缩放因子 [s_min, s_max, step] 从 [1, 1.11, 0.01] 到 [1, 1.56, 0.03]
- **N4 — 雾 (Fog):** 密度 alpha=0.5-5.0，衰减率 beta=1.3-3.0
- **N5 — 毛玻璃模糊 (Glass blur):** sigma=0.5-2.5，像素位移 delta=1-5，迭代 1-3 次

### 2.4 难度级别 (L1-L5)

按 4 个参考模型（OpenVLA-OFT, pi0, pi0-fast, UniVLA）能否解决分层：
- L1: 4 个都能解决
- L2: 3 个能解决
- L3: 2 个能解决
- L4: 1 个能解决
- L5: 无一能解决

### 2.5 安装和运行

**安装：**
```bash
# 系统依赖
sudo apt install libexpat1 libfontconfig1-dev libmagickwand-dev

# 克隆安装
git clone https://github.com/sylvestf/LIBERO-plus.git
cd LIBERO-plus
pip install -e .
pip install -r extra_requirements.txt

# 如果已装 vanilla LIBERO，需先卸载
pip uninstall -y hf-libero

export MUJOCO_GL=egl
```

**下载资产：**

从 [HuggingFace](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) 下载 `assets.zip`，解压到 `LIBERO-plus/libero/libero/assets/`。

期望结构：
```
libero/libero/assets/
├── articulated_objects/
├── new_objects/
├── scenes/
├── stable_hope_objects/
├── stable_scanned_objects/
├── textures/
├── turbosquid_objects/
├── serving_region.xml
├── wall_frames.stl
└── wall.xml
```

**配置：** 检查 `/root/.libero/config.yaml`。评测时设 `num_trials_per_task: 1`。

任务到扰动类别映射：`.libero/libero/benchmark/task_classification.json`

**LeRobot 评测：**
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

### 2.6 与标准 LIBERO 的关系

LIBERO-Plus 是 vanilla LIBERO 的 **drop-in replacement**：
- 安装在同一个 `libero` Python 包名下（替换原版）
- 相同的 `LiberoEnv` gym 接口
- 相同的相机名称 (`agentview_image`, `robot0_eye_in_hand_image`)
- 相同的观测/动作格式
- 相同的 task suite 名称
- **不能同时安装 vanilla LIBERO 和 LIBERO-Plus**，切换需要先卸载再安装

---

## 3. 数据增强相关

### 3.1 robosuite 内置随机化

LIBERO 基于 robosuite (MuJoCo)，robosuite 提供了 `DomainRandomizationWrapper` 和三个 Modder 类，可用于任何 robosuite 环境包括 LIBERO。

**DomainRandomizationWrapper：**
```python
from robosuite.wrappers import DomainRandomizationWrapper

env = DomainRandomizationWrapper(
    env=base_env,
    seed=42,
    randomize_color=True,        # 几何体/纹理颜色随机化
    randomize_camera=True,       # 相机位置/朝向/FOV
    randomize_lighting=True,     # 光源位置/方向/颜色
    randomize_dynamics=True,     # 物理参数
    randomize_on_reset=True,     # episode 重置时随机化
    randomize_every_n_steps=1,   # rollout 中的频率
)
```

**CameraModder（内置）：**
- 位置扰动：默认 size 0.01
- 旋转扰动（四元数）：默认 size 0.087 (~5 度)
- FOV 扰动：默认 size 5.0 度

**LightingModder（内置）：**
- 位置扰动：默认 size 0.1
- 方向扰动：默认 size 0.35
- 镜面/环境光/漫射扰动：默认 size 0.1
- 开关控制：on/off

**TextureModder（内置）：**
- RGB 颜色随机化 (local interpolation 0.1)
- 纹理模式：RGB, checker, noise, gradient
- 材质属性：反射率、光泽度、镜面反射 (local interpolation 0.2)
- 天空盒随机化（可选）

Demo 脚本：`robosuite/demos/demo_domain_randomization.py`

### 3.2 LIBERO-Plus 扰动可否复用为训练时数据增强

**可以，且论文已经这样做了。** LIBERO-Plus 同时提供评测任务和训练数据集：

**已提供的训练数据：**
- **22,400 条训练轨迹**（过滤后 20,000+），在各种扰动条件下生成
- 分布：2,400 物体布局变体 + 各 4,000 光照/相机/背景/语言/噪声维度
- RLDS 格式存储，LeRobot 格式见 `lerobot/libero_plus`
- 论文证明混合 SFT (mix-SFT) 训练显著提升鲁棒性：OpenVLA-OFT+ 平均 79.6%

**三条数据增强路径：**

**路径 A — 直接使用 LIBERO-Plus 训练数据：**
```bash
lerobot-train \
    --policy.type=smolvla \
    --dataset.repo_id=lerobot/libero_plus \
    --env.type=libero_plus \
    ...
```

**路径 B — 使用 robosuite 内置 DomainRandomizationWrapper 在线增强：**
```python
from robosuite.wrappers import DomainRandomizationWrapper
env = DomainRandomizationWrapper(
    env=libero_env,
    randomize_camera=True,
    randomize_lighting=True,
    randomize_color=True
)
```
在线随机化，每 N 步应用随机扰动。适合训练时增强但可控性较低。

**路径 C — 复用 LIBERO-Plus 扰动代码做自定义增强：**
- 光照/纹理扰动：修改场景 XML + 注册新场景
- 相机扰动：修改 `Problem` 类接口
- 传感器噪声 (N1-N5)：纯图像空间后处理，可直接作为标准数据增强应用于任何存储轨迹，无需重新渲染

**关键区别：**
- robosuite 内置随机化（路径 B）是 **在线** 的，可控性低
- LIBERO-Plus 扰动（路径 C）是 **结构化** 的，有明确参数范围和难度分层，更适合系统性鲁棒性训练
- 传感器噪声 (N1-N5) 是纯图像后处理，可以零成本复用为数据增强

---

## 4. 与 LeRobot 的集成

### 4.1 原生支持

LeRobot **原生支持** LIBERO，是一级基准测试环境。

安装：`pip install -e ".[libero]"`

文档：https://huggingface.co/docs/lerobot/en/libero

HuggingFace 维护了 LIBERO fork：https://github.com/huggingface/lerobot-libero

### 4.2 HuggingFace Hub 数据集

**主要数据集（推荐用于训练）：**

| 数据集 ID | Episodes | 任务数 | 大小 | 说明 |
|-----------|----------|--------|------|------|
| `HuggingFaceVLA/libero` | 148 | 10 | ~1.9 GB | 官方预处理数据集，LeRobot 文档推荐 |
| `lerobot/libero` | 1,693 | 40 | ~1.94 GB | 4 个标准 suite 合并（视频格式, AV1 编码） |
| `physical-intelligence/libero` | 147 | 10 | ~34.9 GB | PI 的转换版本, RLDS 来源, CC-BY-4.0 |
| `lerobot/libero_plus` | — | — | — | LIBERO-Plus 训练数据 |

**每个 suite 的图像数据集：**

| 数据集 ID | 任务数 |
|-----------|--------|
| `lerobot/libero_10_image` | 10 |
| `lerobot/libero_object_image` | 10 |
| `lerobot/libero_spatial_image` | 10 |
| `lerobot/libero_goal_image` | 10 |

**社区数据集：**
- `IPEC-COMMUNITY/libero_90_no_noops_lerobot` — LIBERO-90 去除 no-op 版本

### 4.3 数据格式映射

| LIBERO 字段 | LeRobot 特征 | 类型 | 形状 |
|-------------|-------------|------|------|
| `agentview_image` | `observation.images.image` | Video/Image | (256, 256, 3) |
| `robot0_eye_in_hand_image` | `observation.images.image2` | Video/Image | (256, 256, 3) |
| `observation["state"]` | `observation.state` | float32 | (8,) |
| `action` | `action` | float32 | (7,) |
| `language_instruction` | `task` (task_index) | string/int | — |

LeRobot 元数据：robot_type=`panda`，fps=`10`，视频编码=AV1 yuv420p，表格数据用 Parquet 存储

### 4.4 转换脚本

**方式 A：Physical Intelligence 的 OpenPI 转换脚本（主要）**

脚本路径：[`Physical-Intelligence/openpi/examples/libero/convert_libero_data_to_lerobot.py`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/convert_libero_data_to_lerobot.py)

```bash
# 前置依赖
uv pip install tensorflow tensorflow_datasets

# 原始数据来源
# https://huggingface.co/datasets/openvla/modified_libero_rlds

# 执行转换
uv run examples/libero/convert_libero_data_to_lerobot.py \
  --data_dir /path/to/your/data \
  --push_to_hub
```

处理流程：
1. 读取 4 个 RLDS 数据集：`libero_10_no_noops`, `libero_goal_no_noops`, `libero_object_no_noops`, `libero_spatial_no_noops`
2. 创建 `LeRobotDataset`，robot_type=panda, fps=10
3. 逐 episode 迭代，每步调用 `dataset.add_frame()`
4. 每个 episode 调用 `dataset.save_episode()`
5. 可选推送到 HuggingFace Hub

处理时间：约 30 分钟

**方式 B：通用 HDF5 → LeRobot 转换器**

仓库：https://github.com/anarnuri/hdf5_to_lerobot_converter

支持 LIBERO 原生 HDF5 格式。

**方式 C：直接使用预转换数据集（无需转换）**

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("HuggingFaceVLA/libero")
# 或
dataset = LeRobotDataset("lerobot/libero")
```

### 4.5 端到端训练和评测示例

**训练：**
```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.repo_id=${HF_USER}/libero-test \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --output_dir=./outputs/ \
  --steps=100000 \
  --batch_size=4 \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --eval_freq=1000
```

**评测：**
```bash
lerobot-eval \
  --policy.path="your-policy-id" \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1
```

---

## 5. 关键注意事项

1. **LIBERO-90 数据** 不在标准预转换数据集中。需要用 OpenPI 转换脚本或社区数据集 `IPEC-COMMUNITY/libero_90_no_noops_lerobot`
2. **控制模式** (`relative` vs `absolute`) 必须与策略的动作参数化匹配
3. **vanilla LIBERO 和 LIBERO-Plus 不能同时安装**，两者共用同一 Python 包名
4. LeRobot 中 LIBERO 仅支持 Linux（MuJoCo 渲染需 EGL）
5. LeRobot 格式的图像分辨率为 256x256，而原始 LIBERO 为 128x128 [UNVERIFIED — 需确认是否做了上采样或 LeRobot 环境重新渲染]
6. 原始 LIBERO 采集频率 20Hz，LeRobot 格式为 10Hz（可能做了下采样）[UNVERIFIED — 需确认具体降频策略]
