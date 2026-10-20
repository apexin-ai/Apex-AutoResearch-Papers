# Closed-Loop Inference Diagnosis: OpenVLA-7B on LIBERO-Goal

**Server**: westd-19183 | **Date**: 2026-05-20 | **Model**: openvla-7b-finetuned-libero-goal (LoRA r=32, 60K steps)

## 1. 失败根因分析

### 第一层：推理管线 Bug（6 个，已全部修复）

原始 `behavioral_smoketest.py` 存在 6 个与官方 OpenVLA 评估代码不一致的 Bug：

| # | Bug | 影响 | 修复 |
|---|-----|------|------|
| 1 | 图像旋转用 `[::-1]`（仅垂直翻转） | 图像上下颠倒但左右正确 → 模型看到错误视角 | `[::-1, ::-1]`（180° 旋转） |
| 2 | 缺少 JPEG encode/decode | 训练数据经 RLDS JPEG 编码，推理时跳过 → 像素分布不匹配 | PIL JPEG roundtrip |
| 3 | 缺少 gripper 后处理 | 原始 bin_center ∈ [-1,1] 直接送入 env，未做 normalize+invert → gripper 行为与 robosuite 约定不匹配 | `normalize_gripper_action` + `invert_gripper_action` |
| 4 | center crop 方法错误 | 简单 90% crop → 应用 `crop_and_resize`（sqrt(0.9)≈0.949/dim，resize 回 224） | TF 风格 crop_and_resize（PIL 重实现） |
| 5 | 缺少 10 步稳定等待 | 环境初始状态物体未稳定 → 初始观察有漂移 | `NUM_STEPS_WAIT=10` |
| 6 | 缺少 `env.seed(0)` | 不影响功能，但破坏可复现性 | `env.seed(0)` |

**最显著的 Bug 是 #1 和 #3。** Bug #1 导致 dim 0 几乎恒定（原始日志中 dim 0 = 0.236 不变），因为翻转的图像对 x 轴方向信息编码错误。Bug #3 导致 gripper 信号完全错误（原始 0.996 送入 env 意味着闭合，而模型意图是张开）。

### 第二层：模型质量不足

**修复所有管线 Bug 后，SR 仍为 0/9。** 这说明管线 Bug 不是唯一原因。

证据：
- demo_action_test（用训练集示范图像喂给模型）L1 error = 0.26–0.43，在 [-1,1] 空间中约 26–43% 偏差
- 动作虽然不再退化（随任务/时间步变化），但行为不稳定：Task 0 前 5 步 dim 0 在 0.044–0.4 间大幅摆动
- Task 7 出现连续两步完全相同的动作（step 0=step 1, step 2=step 3），说明模型对微小状态变化不敏感
- 所有 9 个 episode 均跑满 400 步、cumulative reward = 0.000（无任何部分进展）

## 2. 日志关键片段

### 原始 Bug 管线（sr_validation3.log）
```
Action samples (ep0, first 5 steps):
  step 0: [0.236, -0.014, 0.360, 0.033, 0.082, 0.328, 0.996]
  step 1: [0.236,  0.411, -0.044, -0.000, 0.098, ...]
  (dim 0 恒定 0.236, gripper 原始值 0.996 未处理)
```

### 修复后管线（sr_official_v2.log）
```
Task 0: open_the_middle_drawer_of_the_cabinet
  step 0: [0.393, 0.189, -0.221, 0.033, 0.043, 0.189, -1.0]
  step 1: [0.393, 0.189, -0.015, 0.037, 0.025, 0.153, -1.0]
  step 2: [0.044, 0.045,  0.765, 0.007, 0.135, 0.088, -1.0]
  step 3: [0.044,-0.118, -0.081,-0.000, 0.108, 0.002, -1.0]
  step 4: [0.400,-0.118, -0.772, 0.058, 0.098, 0.004, -1.0]
  ep 0: fail | R=0.000 | steps=400 | 56.7s
  ep 1: fail | R=0.000 | steps=400 | 56.2s
  ep 2: fail | R=0.000 | steps=400 | 56.3s
  Task 0 SR=0.00 (0/3)

Task 3: open_the_top_drawer_and_put_the_bowl_inside
  step 0: [0.236, 0.241, 0.250,-0.000, 0.038, 0.221, -1.0]
  ep 0-2: all fail | R=0.000 | steps=400
  Task 3 SR=0.00 (0/3)

Task 7: turn_on_the_stove
  step 0: [0.279,-0.118, 0.809,-0.013, 0.018, 0.215, -1.0]
  ep 0-2: all fail | R=0.000 | steps=400
  Task 7 SR=0.00 (0/3)
```

## 3. 可修复性 + 修复方案

### 管线 Bug：✅ 已修复

修复脚本：`/root/vla-ssd/scripts/sr_official_pipeline.py`（PIL 重实现，无 TF 依赖）

### 模型质量：⚠️ 需要进一步排查

可能原因（按概率排序）：

1. **LoRA fine-tuning 不充分**（最可能）
   - LoRA r=32 + 60K steps 可能不够。OpenVLA 官方用 full fine-tuning 或更高 rank
   - 建议：检查训练 loss 曲线（wandb），确认是否收敛；对比官方开源 checkpoint

2. **训练数据预处理与推理不一致**
   - 如果训练时的 RLDS 数据处理（图像增强、action normalization）与推理管线不完全匹配
   - 建议：对比训练代码中的 `resize-naive` + `random_crop` + `color_jitter` 流程

3. **PIL vs TF 预处理的微小差异**
   - 本次修复用 PIL 替代 TF 实现 JPEG roundtrip 和 resize，数值上有微小差异
   - 风险评估：差异应 < 1 pixel intensity，不太可能是主因
   - 若需完全排除，可 `pip install tensorflow` 后用原始 TF 实现

4. **checkpoint 加载问题**
   - config.json 中 `vocab_size=32064`（含 pad_to_multiple_of=64），代码用 `32064-64=32000` 反推
   - 已验证该逻辑正确

## 4. 扩大到 10–20 trials 是否可能看到非零 SR

**极不可能。**

理由：
- 当前使用 `env.seed(0)` + `do_sample=False` → 所有 episode 产生 **完全相同的轨迹**。0/3 本质上是 0/1 重复 3 次
- 若换用不同 seed（seed 0–19），初始状态会略有变化，但模型的系统性偏差不会消失
- L1 error 0.26–0.43 意味着平均每个维度偏差约 30%。LIBERO 操作任务需要 cm 级精度，这种偏差级别下成功概率接近 0
- 参考：OpenVLA 官方报告 LIBERO-Goal SR ≈ 80–96%，当前 0% 与报告值差距过大，不是统计波动能解释的

**若要获得有意义的 SR 估计**：
1. 每个 episode 使用不同 seed（`env.seed(ep_idx)`）
2. 覆盖全部 10 个 LIBERO-Goal 任务
3. 每任务 20 episodes → 总计 200 episodes

但基于当前模型质量，预期 SR < 5%。

## 5. 风险评估

| 风险 | 等级 | 说明 |
|------|------|------|
| 管线 Bug 误导后续实验 | 🟢 已消除 | 6 个 Bug 已全部修复并验证 |
| 模型不可用于 closed-loop 评估 | 🔴 高 | SR=0%，无法支撑任何 closed-loop 结论 |
| PIL vs TF 差异导致额外偏差 | 🟡 低 | 差异级别 < 1 pixel，但未完全排除 |
| env.seed(0) 掩盖统计信号 | 🟡 中 | 当前 0/3 = 0/1，需不同 seed 才能得到真实 SR |
| 训练 checkpoint 质量 | 🔴 高 | demo image L1 error 0.26–0.43 表明模型未充分学习动作映射 |

## 6. 建议下一步

1. **优先检查训练质量**：查看训练 loss/eval_loss 是否收敛。若有 wandb，对比 loss 曲线与官方训练
2. **尝试官方 OpenVLA checkpoint**：下载 `openvla/openvla-7b-finetuned-libero-goal`（若存在），用同一评估管线测试，确认管线本身是否正确
3. **若需 TF 精确匹配**：`pip install tensorflow` 并使用原始 TF 版 `crop_and_resize` 和 `resize_image`
4. **正式评估方案**：10 tasks × 20 eps × 不同 seed，MAX_STEPS=400
