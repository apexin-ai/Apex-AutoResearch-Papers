# Memory — meta_brain_lora_routing

## 战略决策

### [2026-05-17] D014 Pivot：Routing 放弃，转向 Universal LoRA Paper
**决策**：Router F1=0.685 + visual expert < universal → routing 无价值。项目 pivot to "Universal LoRA for VLA Robustness"。
**证据链**：
- Router F1=0.685（远低于 Phase 0 的 0.996，因为 fine-tuned model 对扰动更鲁棒）
- Visual expert (63.3%) < Universal (71.7%) on light_conditions（专用不如通用）
- Physical expert 仅 +3.8pp（噪声范围内）
- Universal r16 是 overall best performer（+15pp on light, +8.8pp on objects_layout）

**影响**：停止 Router 优化/activation collection。Paper 核心变为 Universal LoRA 的鲁棒性改善。

## 确定性修复后的可靠 Eval 数据（3 seeds × 20 eps = 60 eps/condition）

### [2026-05-17] 核心对比表（部分数据仍在收集）
| 条件 | Baseline | Universal r16 | Delta |
|---|---|---|---|
| nominal | 60.0% | 65.0% | +5.0pp |
| background_textures | 78.3% | 78.3% | 0 |
| objects_layout | 58.8% | 67.6% | +8.8pp |
| robot_initial_states | 22.6% | 20.8% | -1.8pp |
| camera_viewpoints | 68.4% | 70.2% | +1.8pp |
| light_conditions | 56.7% | 71.7% | **+15.0pp** |
| sensor_noise | 65.5% | 65.5% | 0 |
| language | 0/0 | 0/0 | 需调查 |

**待补充**：r48 全覆盖、visual/spatial/physical expert 完整结果

### [2026-05-17] Universal r48 训练完成
- final_loss: 0.4302（vs r16 的 0.603，改善 28.7%）
- checkpoint: `/root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/`
- 11M params (0.31%) vs r16 的 3.7M (0.11%)
- Eval 正在跑

## Phase 0 关键发现（历史参考）

### [2026-05-15] PAR Router 在 base model 上完美分类
Phase 0 用 pi0_base（未 fine-tune）收集 activations → F1=0.996。但 fine-tuned pi0_libero_openpi 对扰动更鲁棒，表征差异被压缩 → F1 降至 0.685。这解释了为什么 routing 在 fine-tuned model 上不可行。

### [2026-05-15] First-token pooling, PaliGemma layer 6
Router 最佳配置：first-token pooling, layer 6。K=1 步足够决策。

## Checkpoint 信息

### 正确 base checkpoint
- openpi 官方 fine-tuned: `/root/.cache/openpi/openpi-assets/checkpoints/pi0_libero/` (JAX/Orbax)
- PyTorch 转换: `/root/autodl-tmp/checkpoints/pi0_libero_openpi/` (7GB, 777 keys, bit-exact)

### v3 LoRA checkpoints
- visual r16: `/root/autodl-tmp/checkpoints/v3_lora_visual_r16/v3lora_visual_r16/final/`
- spatial r16: `/root/autodl-tmp/checkpoints/v3_lora_spatial_r16/v3lora_spatial_r16/final/`
- physical r16: `/root/autodl-tmp/checkpoints/v3_lora_physical_r16/v3lora_physical_r16/final/`
- universal r16: `/root/autodl-tmp/checkpoints/v3_lora_universal_r16/v3lora_universal_r16/final/`
- universal r48: `/root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/`

## 环境与约束

### LIBERO-Plus 扰动结构
| 后缀 | 变化内容 | PAR 类别 |
|------|---------|----------|
| `_table_N`/`_tb_N` | 桌面+墙壁纹理 | visual |
| `_add_N` | 添加 distractor 物体 | spatial |
| `_language_N` | 语言改写 | language |
| robot_initial_states | 机械臂初始位置 | physical |

### 关键教训
- `lerobot/pi0_libero` 是 BASE MODEL，不能用
- jaxtyping 0.2.36 + beartype 0.22.9 需要 `jaxtyping_disable = True`
- PI0 flow-matching 推理 torch.normal() 必须 seed（否则方差 15pp）
- 根分区只有 30GB，数据/checkpoint 放 `/root/autodl-tmp/`
- eval 脚本已修复确定性：torch.manual_seed + cudnn.deterministic
