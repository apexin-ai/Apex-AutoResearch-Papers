# Pipeline Audit: LIBERO-Goal Adaptation

## 1. 数据格式差异

| 维度 | LIBERO-10 | LIBERO-Goal |
|------|-----------|-------------|
| 文件名格式 | `{SCENE}_SCENE{N}_{task}_demo.hdf5` | `{task}_demo.hdf5`（无 scene 前缀） |
| Scene 数量 | 7 unique scenes（KITCHEN 3/4/6/8, LIVING_ROOM 1/2/5/6, STUDY 1） | **1 个共享 scene**（Libero_Tabletop_Manipulation） |
| env_name | 场景特定（如 `Libero_Kitchen_Tabletop_Manipulation`） | 统一 `Libero_Tabletop_Manipulation` |
| BDDL 路径 | `libero_10/SCENE_{task}.bddl` | `libero_goal/{task}.bddl` |
| HDF5 内部结构 | `data/demo_N/{actions,obs,dones,...}` | **完全一致** |
| obs keys | `agentview_rgb, ee_ori, ee_pos, ee_states, eye_in_hand_rgb, gripper_states, joint_states` | **完全一致** |
| language_instruction | 在 `data.attrs['problem_info']` JSON 中 | **完全一致**（同一字段） |
| image shape | (T, 128, 128, 3) | 相同 |
| actions shape | (T, 7) | 相同 |
| demos/task | 50 | 50 |

### LIBERO-Goal 10 个任务（从 HF download cache 推断）
1. `open_the_middle_drawer_of_the_cabinet`
2. `open_the_top_drawer_and_put_the_bowl_inside`
3. `push_the_plate_to_the_front_of_the_stove`
4. `put_the_bowl_on_the_plate`
5. `put_the_bowl_on_the_stove`
6. `put_the_bowl_on_top_of_the_cabinet`
7. `put_the_cream_cheese_in_the_bowl`
8. `put_the_wine_bottle_on_the_rack`
9. `put_the_wine_bottle_on_top_of_the_cabinet`
10. （第 10 个待下载完成后确认）

**关键差异：所有 10 个任务共享同一初始 scene（同桌面、同物体摆放），仅 language goal 不同。** 视觉特征在任务间高度重叠，必须依赖 instruction 编码来区分 goal。

## 2. 需要修改的文件

### extract_features.py — 无需修改 ✅
- `--data_dir` 已参数化，直接传 `libero_goal/` 路径即可
- `task_desc_from_filename()` 的 regex `^[A-Z_]+SCENE\d+_(.+)$` 不匹配 LIBERO-Goal 文件名，但 fallback `stem.replace("_", " ")` 产出正确 instruction（如 "push the plate to the front of the stove"）
- 可选优化：从 HDF5 attrs `problem_info.language_instruction` 直接读取 instruction，而非从文件名推断（更 robust）
- Instruction 已作为 text prompt 传入 OpenVLA processor，hidden states 包含 instruction 信息

### extract_dinov2.py — 无需修改 ✅
- `--data_dir` 参数化，`agentview_rgb` key 一致

### train_probes.py — 需新增 probe 类型 ⚠️
- 现有 5 种 probe 均可直接在 LIBERO-Goal features 上运行（改 `--features_dir` 和 `--data_dir`）
- 但**现有 probe 无法测试 instruction conditioning** — 它们只用 hidden states，不区分 same-scene 不同 goal 的情况
- split_by_task 按 task 做 80/20 split — 适用于 LIBERO-Goal

### 需新增的代码
| 文件 | 改动 | 估计耗时 |
|------|------|----------|
| `train_probes.py` | 新增 `goal_classification` probe type | 3h |
| `train_probes.py` | 新增 `pairwise_goal_discrimination` probe type | 2h |
| `analyze_results.py` / `plot_*.py` | 新增对应可视化 | 1.5h |
| 新建 `download_libero_goal.py`（可选） | 完成下载 + 验证 | 0.5h |

## 3. Instruction-Conditioned Probe 设计方案

### 方案 A: Goal Classification（核心实验，最高优先）

**动机：** LIBERO-Goal 的 10 个任务共享视觉 scene。如果 probe 能从 hidden state 正确分类 goal，说明 instruction 信息被编码进了表征。

**设计：**
- 输入：单帧 hidden state h(t) ∈ R^D
- 输出：10 类 softmax（10 个 goal 之一）
- 架构：Linear probe (D → 10) 或 MLP probe (D → 256 → 10)
- 数据：所有 task 的所有 trajectory 的所有时间步，按 task 做 80/20 split（复用 `split_by_task`）
- 评估：accuracy, macro-F1, per-class accuracy

**预期结果：**
| 模型 | 预期 accuracy | 原因 |
|------|-------------|------|
| OpenVLA trained (last_preaction) | **高 (70-90%)** | Instruction 编码在 text tokens，last_preaction 位置能读到 |
| OpenVLA trained (image_mean) | **中等 (40-60%)** | Image tokens 可能通过 attention 间接编码了部分 instruction |
| OpenVLA untrained | **低 (~10-20%)** | 随机 LLM backbone 不能有效编码 instruction |
| DINO-V2 | **随机 (~10%)** | 纯视觉，无 instruction 输入，same scene 无法区分 |

**这组对比直接证明 "instruction information is in the VLA representation, not derivable from vision alone"。**

### 方案 B: Same-Scene Pairwise Goal Discrimination

**动机：** 更细粒度地测试 instruction 编码 — 给定同一 scene 下两个不同 goal 的 hidden states，判断哪个属于哪个 goal。

**设计：**
- 输入：|h_goal_A(t) - h_goal_B(t')| ∈ R^D（两个不同 goal 的帧差）
- 输出：binary — 是否 goal_A 在先（或更一般：哪个是 goal_A）
- 采样：从 10 个 goal 中取 C(10,2)=45 对，每对采样若干帧对
- 评估：AUC, accuracy

**预期：**
- OpenVLA trained: AUC > 0.8
- DINO-V2: AUC ≈ 0.5（随机）

### 方案 C: Cross-Goal Temporal Distance Breakdown

**动机：** 复用已有 temporal_distance probe 框架，增加 cross-goal 分析维度。

**设计：**
- 同一 temporal_distance probe，但在 LIBERO-Goal 上分析时增加维度：
  - **Within-goal TD**: 同一 goal 内的帧对 → 应该与 LIBERO-10 表现类似
  - **Cross-goal TD**: 不同 goal 的帧对（同 scene）→ 如果模型编码了 goal，跨 goal 帧对的 distance 应更大/更不可预测
- 无需新架构，只需新的分析脚本
- 评估：within-goal ρ vs cross-goal ρ 的差异

**预期：**
- OpenVLA trained: within-goal ρ 高，cross-goal ρ 低 → 编码了 goal-specific 进度信息
- DINO-V2: within/cross-goal ρ 无显著差异 → 不区分 goal

### 推荐优先级
1. **方案 A**（goal classification）— 最直接、最有说服力的证据
2. **方案 C**（cross-goal TD breakdown）— 复用已有代码，低成本高收益
3. **方案 B**（pairwise discrimination）— 补充性实验

## 4. Scene Overlap 分析

### LIBERO-10 vs LIBERO-Goal Scene 交集

**LIBERO-10 scenes (from filenames):**
- KITCHEN_SCENE3, KITCHEN_SCENE4, KITCHEN_SCENE6, KITCHEN_SCENE8
- LIVING_ROOM_SCENE1, LIVING_ROOM_SCENE2, LIVING_ROOM_SCENE5, LIVING_ROOM_SCENE6
- STUDY_SCENE1

**LIBERO-Goal scene:**
- 单一 scene: `Libero_Tabletop_Manipulation`
- BDDL 路径: `libero_goal/{task}.bddl`
- 任务涉及 kitchen 物品 (plate, stove, cabinet, drawer, bowl, wine bottle, cream cheese)

**结论：LIBERO-Goal 的 scene 与 LIBERO-10 的 9 个 scene 均不相同。**
- LIBERO-Goal 使用独立的 tabletop manipulation scene
- LIBERO-10 的 kitchen scene 有编号 (KITCHEN_SCENE3 等)，LIBERO-Goal 无编号
- env_name 不同：`Libero_Tabletop_Manipulation` vs `Libero_Kitchen_Tabletop_Manipulation` 等

### Fine-tune 影响评估

OpenVLA checkpoint 是在 LIBERO-10 fine-tune 的（10 个 scene）。LIBERO-Goal 的 scene 不在 fine-tune 集中。

**影响程度：中等偏低**
- 对 probing 实验：影响不大。Probing 测的是 "representation 编码了什么"，不要求 policy 执行准确。即使 fine-tune scene 不同，7B VLM 的通用视觉理解 + instruction following 能力足够产生有意义的表征。
- 对实验严谨性：如果 LIBERO-Goal 上 probing 效果差，需要排除 "scene 不在 fine-tune 分布内" 的混淆因素。
- **缓解方案：** 如果需要，可在 LIBERO-Goal 上额外 fine-tune OpenVLA。但建议先用当前 checkpoint 跑，如果 goal classification 显著高于 chance，就说明 instruction conditioning 在 out-of-distribution scene 上也成立（更强的结论）。

## 5. 预估工作量

| 阶段 | 任务 | 耗时 |
|------|------|------|
| 数据准备 | 完成 LIBERO-Goal 下载（当前仅 1/10 完整） | 0.5h + 下载等待 |
| 特征提取 | OpenVLA trained + untrained on LIBERO-Goal | 2h GPU time |
| 特征提取 | DINO-V2 on LIBERO-Goal | 0.5h GPU time |
| 代码开发 | Goal classification probe (方案 A) | 3h |
| 代码开发 | Cross-goal TD analysis (方案 C) | 1.5h |
| 代码开发 | Pairwise discrimination (方案 B, optional) | 2h |
| 实验运行 | 全部 probe × 3 模型 × 33 层 | 2h GPU time |
| 分析可视化 | 结果分析 + 画图 | 2h |
| **总计** | | **~13h**（其中 ~4.5h 是 GPU 等待时间） |

## 6. 阻塞项

1. **LIBERO-Goal 下载未完成** — 10 个任务中仅 1 个 HDF5 完整（`push_the_plate_to_the_front_of_the_stove`），3 个 .part 文件在写入中，`put_the_bowl_on_the_plate` 文件 0 字节（损坏或未开始）。需先完成下载。
2. **第 10 个任务名待确认** — 从 lock 文件只能看到 9 个任务名，需下载完成后验证。
3. **OpenVLA fine-tune scope** — 如果后续需要在 LIBERO-Goal scene 上 fine-tune OpenVLA，需额外 GPU 时间（约 4-8h A6000）。
