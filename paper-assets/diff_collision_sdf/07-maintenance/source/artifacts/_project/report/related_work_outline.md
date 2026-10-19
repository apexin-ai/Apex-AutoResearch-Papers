# Related Work Outline — ColliForce-VLA

## SDF in Robotics

- **DeepSDF** (CVPR 2019): 开创性地用深度网络学习连续 SDF 表示 3D 形状，将任意 3D 坐标映射为有符号距离值。*与本项目关系: ColliForce 中 workspace SDF 的表征方法论基础。*

- **VoxPoser** (CoRL 2023): 用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划，实现语言驱动的 3D 空间约束。*与本项目关系: 启发了用 3D 空间场引导动作生成的思路，但 VoxPoser 是规划时构建，ColliForce 是训练时嵌入。*

- **Robot Geometry as Distance Fields** (Liu et al., 2023): 用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中，实现可微碰撞检测与全身操作。*与本项目关系: 验证了 SDF 在机器人碰撞检测中的可行性和可微性。*

- **iSDF** (RSS 2022): 从流式深度图像持续学习神经 SDF，实现实时机器人场景感知。*与本项目关系: 证明神经 SDF 可实时构建用于机器人感知，ColliForce 的 workspace SDF ground truth 生成可参考其方法。*

- **RAMP** (IROS 2023): 结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测的层次化反应式运动规划。*与本项目关系: 展示 SDF 在 reactive manipulation 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块。*

- **DiffCo** (IEEE T-RO 2021): 全自动可微的非参数碰撞检测模型，通过反向传播提供鲁棒梯度用于轨迹优化。*与本项目关系: 证明碰撞信息可通过梯度传播融入优化，ColliForce 的 SDF 辅助损失本质相同。*

## VLA Safety

- **VLSA/AEGIS** (arXiv 2025): 用 CBF 安全约束层作为 VLA 的即插即用模块实现碰撞回避，不改变 VLA 内部空间表征。*与本项目关系: ColliForce 的核心对比对象——外挂式安全机制 vs. 内在空间表征增强。*

- **SafeVLA** (NeurIPS 2025 Spotlight): 用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。*与本项目关系: 最直接竞品之一，走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督）。*

- **Language-Guided Object-Centric Diffusion Policy** (ICRA 2025): 在 3D 点云上训练 diffusion policy，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。*与本项目关系: 碰撞回避在推理阶段注入，ColliForce 在训练阶段嵌入，设计哲学不同。*

- **CAPE** (arXiv 2025): 通过 context-aware prior 和 guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。*与本项目关系: 推理阶段碰撞回避方法，与 ColliForce 形成 train-time vs. test-time 安全注入的对比。*

- **iKinQP-RL** (arXiv 2024): 用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。*与本项目关系: 运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层。*

- **QDepth-VLA** (arXiv 2025): 用量化深度预测作为 VLA 辅助监督增强空间推理能力。*与本项目关系: 与 ColliForce 的辅助损失思路最相似，但用深度图而非 SDF/occupancy field，缺乏显式碰撞语义。*

- **Spatial Forcing** (ICLR 2026): 隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效。*与本项目关系: ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field，目标更聚焦于碰撞感知。*

## Flow Matching & Diffusion Policy

- **Flow Matching for Generative Modeling** (ICLR 2023): 提出 flow matching 训练范式，通过回归条件向量场构建连续归一化流，比 diffusion 训练更简洁高效。*与本项目关系: π0 使用的核心训练范式，ColliForce 的 gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入。*

- **π0** (arXiv 2024): 基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型，支持灵巧操作等复杂任务。*与本项目关系: ColliForce 的基座架构，在其 action expert 上添加 SDF 辅助监督分支。*

- **RT-2** (arXiv 2023): 将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，确立 VLM→VLA 微调范式。*与本项目关系: VLA 范式奠基工作，ColliForce 在此范式基础上增加 SDF 辅助分支。*

- **OpenVLA** (arXiv 2024): 7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，29 任务上超越 RT-2-X。*与本项目关系: 主要 VLA baseline，可验证 SDF 辅助监督的跨架构通用性。*

- **Octo** (arXiv 2024): 基于 Transformer 的轻量级通用策略，Open X-Embodiment 800k 轨迹训练。*与本项目关系: 轻量级 VLA baseline，可测试 SDF 辅助分支在小模型上的效果。*

## Benchmarks

- **LIBERO** (NeurIPS 2023): 定义了 Spatial/Goal/Object/Long 四个 suite 的终身机器人学习基准，提供标准化任务结构和评估协议。*与本项目关系: SafeLIBERO benchmark 的基础，ColliForce 主要评估平台。*

## 定位总结

ColliForce-VLA 区别于现有 VLA 安全方法（SafeVLA、VLSA、CAPE 等）的核心在于：不依赖外挂安全层或推理时优化，而是通过 SDF 辅助监督在训练阶段将碰撞感知直接嵌入 VLA 的空间表征。相比同样使用辅助损失的 QDepth-VLA 和 Spatial Forcing，ColliForce 将对齐目标特化为 occupancy/SDF field，使模型获得显式碰撞语义而非泛化的深度或 3D 几何信息。这种 train-time 内在化方法在推理时零额外开销，同时受益于 SDF 在机器人碰撞检测领域已被充分验证的表达能力。
