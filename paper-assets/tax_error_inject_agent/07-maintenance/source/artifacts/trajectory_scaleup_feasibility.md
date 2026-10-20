# Trajectory Collection Scale-up 评估：500 → 2500

## 1. 收集脚本位置和关键参数

**主脚本**: `/root/autodl-tmp/tax_error_inject_agent/data/collect_trajectories.py`

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--num_trajectories` | 500 | 目标成功轨迹数 |
| `--output_dir` | `data/trajectories/` | 输出目录 |
| `--data_path` | `/root/autodl-tmp/alfworld_data/json_2.1.1/train` | ALFWorld 数据路径 |
| `--workers` | 4 | 并行线程数 |
| `--seed` | 42 | 随机种子 |

- API: GPT-5.2 via `http://47.94.22.126/v1`（OpenAI-compatible endpoint）
- 定价: $2.50/M input tokens, $10.00/M output tokens
- 每 episode 最多 50 步，history window = 10
- **支持 Resume**: `TrajectoryCollector._load_existing()` 加载已有轨迹，自动跳过已处理 game

**注入脚本**: `/root/autodl-tmp/tax_error_inject_agent/data/inject_and_generate.py`

- 4 个注入算子: P1_StepOrderSwap, P2_SubGoalDeletion, C1_ContextTruncation, C4_ObservationMasking
- 默认 `--num_variants=800`，也调 GPT-5.2 生成 recovery demonstration
- 支持 `--dry_run`（仅注入，不调 API）

**格式转换**: `/root/autodl-tmp/tax_error_inject_agent/data/convert_all_v4.py`

- 将 clean trajectories + injected variants 转成 SFT 格式
- 每条轨迹按 step 展开为多个 prompt-response 对

## 2. API 成本预估

### 2a. 轨迹收集成本

| 指标 | 已知值 | 推算 |
|------|--------|------|
| 成功率 | 70.2% (501/714) | — |
| 每次尝试成本 | $0.0124 (=$8.86/714) | — |
| **新增目标** | **2000 条成功** | — |
| 需新增尝试 | 2000 / 0.702 ≈ **2,849 次** | — |
| **收集 API 成本** | — | **~$35.3** |

### 2b. 注入 pipeline 成本

| 指标 | 已知值 | 推算 |
|------|--------|------|
| 已有注入数据 | 760 variants, $2.97 | $0.00391/variant |
| 当前注入密度 | 760/501 = 1.52 variants/traj | — |
| 2500 traj 需要 | 2500 × 1.52 = **3,800 variants** | — |
| 新增 variants | 3,800 - 760 = 3,040 | — |
| **注入 API 成本** | — | **~$11.9** |

### 2c. 总成本

| 项目 | 成本 |
|------|------|
| 轨迹收集（新增 2849 次尝试） | ~$35.3 |
| 注入 pipeline（新增 3040 variants） | ~$11.9 |
| **合计** | **~$47.2** |

## 3. 时间预估

### 3a. 轨迹收集

| 方案 | 时间 |
|------|------|
| 串行 | 2,849 × 7.3s = **5.8h** |
| 4 workers（当前默认） | **~1.5h** |
| 8 workers | **~0.8h** |

并行瓶颈：`env_lock` 序列化 TextWorld 环境创建，但 API 调用是并行的。实测 4 workers 有效加速约 3.5-4x。

### 3b. 注入 pipeline

已知 752 variants 用时约 10 分钟（4 workers）。3,040 新 variants 约 **40 分钟**。

### 3c. 端到端时间

| 阶段 | 时间 |
|------|------|
| 轨迹收集（4 workers） | ~1.5h |
| 注入 + recovery generation | ~0.7h |
| 格式转换 | <1min |
| **数据准备总计** | **~2.2h** |

## 4. ALFWorld 任务池

| 指标 | 数值 |
|------|------|
| 训练集 task 目录数 | 2,435 |
| 总 game 文件数（含多 trial） | **4,639** |
| 脚本过滤条件 | 排除 "movable" + "Sliced" + unsolvable + 非6类任务 |
| 有效 TASK_TYPES | 6 类 |
| 已使用 | 714 games (501 成功 + 213 失败) |

**关键问题：任务池是否够 2500 条？**

- 脚本的 `collect_game_files` 过滤掉 `pick_and_place_with_movable_recep`（365 dirs）和含 "Sliced" 的路径，再过滤 unsolvable
- 过滤后有效 pool 估计 **~3,000-3,500 games**
- 需要 ~3,563 次尝试（含已有 714）
- **风险：任务池可能刚好不够，需要验证**

验证方法（不修改数据，仅读取）：
```bash
cd /root/autodl-tmp/tax_error_inject_agent
python3 -c "
from data.collect_trajectories import collect_game_files
games = collect_game_files('/root/autodl-tmp/alfworld_data/json_2.1.1/train')
total = sum(len(g) for g in games.values())
for t, g in sorted(games.items()):
    print(f'  {t}: {len(g)}')
print(f'Total valid: {total}')
"
```

**额外注意：** 脚本的 overshoot factor 为 1.15（`num_to_attempt = num_trajectories * 1.15`），对于 70.2% 成功率来说不够。需要改为至少 1.43 或直接设更大的 `--num_trajectories`。

## 5. 训练规模预估

### 5a. 数据量对比

| 数据集 | 500 traj (当前) | 2500 traj (目标) | 倍数 |
|--------|----------------|-----------------|------|
| Clean trajectories | 501 | 2,500 | 5.0x |
| Vanilla SFT samples | 4,358 | ~21,750 | 5.0x |
| Injected variants | 760 | ~3,800 | 5.0x |
| Injected SFT samples | 4,671 | ~23,180 | 5.0x |
| **TaxEI SFT total** | **9,029** | **~44,930** | **5.0x** |
| Random SFT total | 9,029 | ~44,930 | 5.0x |

每条轨迹展开为 ~8.7 个 SFT samples（按 step 拆分）。每个注入 variant 展开为 ~6.1 个 SFT samples。

### 5b. 训练时间预估

基于已有训练日志（Qwen3-8B + LoRA, 1 GPU RTX 5090, batch=1, grad_accum=16, 3 epochs）：

- 训练速度: ~5.0 s/step, throughput ~3.14 samples/sec
- 内存: 22.5 GB

| 数据集 | 样本数 | Steps (1 GPU) | 时间 (1 GPU) | 时间 (4 GPU DDP) |
|--------|--------|---------------|-------------|-----------------|
| Vanilla (当前) | 4,358 | 819 | ~1.1h | ~17min |
| TaxEI (当前) | 9,029 | 1,695 | ~2.4h | ~36min |
| **Vanilla (2500)** | **21,750** | **4,080** | **~5.7h** | **~1.4h** |
| **TaxEI (2500)** | **44,930** | **8,427** | **~11.7h** | **~2.9h** |

3 个变体（vanilla + taxei + random）完整训练：
- 1 GPU 串行: ~29.1h
- 4 GPU 并行（1 job/GPU）: ~11.7h（最慢的 taxei/random 决定总时间）
- 4 GPU DDP（每次用 4 GPU 跑 1 job）: 3 jobs × ~2.9h = ~8.7h

多 seed 实验（5 seeds × 3 variants = 15 runs）：
- 4 GPU 并行: 15 × 11.7h / 4 = **~43.9h ≈ 1.8 天**
- 4 GPU DDP: 15 × 2.9h / 1 = **~43.5h ≈ 1.8 天**（DDP 占满所有 GPU，无法并行跑多 job）

## 6. 风险和建议

### 高风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| **任务池耗尽** | 有效 pool ~3000-3500，需要 ~3563 次尝试，可能不够 | 先运行 `collect_game_files` 确认实际 pool 大小；如不够，考虑放宽 "Sliced" 过滤或允许同 task 不同 trial |
| **Overshoot factor 不足** | 脚本默认 1.15，但 70.2% 成功率需要 1.43+ | 修改脚本或设 `--num_trajectories=3600` 让脚本采样足够多 game |

### 中风险

| 风险 | 影响 | 缓解 |
|------|------|------|
| API rate limit | 第三方 endpoint 可能限流 | 先用 8 workers 小批量测试；保持 4 workers 最安全 |
| 磁盘空间 | 当前数据 ~45MB，5x 后 ~225MB，不是问题 | 确认 `/root/autodl-tmp/` 剩余空间 |
| 训练时间长 | 多 seed 完整实验需 ~1.8 天 GPU 时间 | 先跑 1 seed 验证效果，再决定是否跑满 5 seeds |

### 建议

1. **先验证任务池大小**：运行 `collect_game_files` 确认过滤后 pool 是否 ≥3563
2. **分阶段收集**：先收到 1000，评估效果趋势，再决定是否继续到 2500
3. **修改 overshoot**：将收集脚本的 overshoot factor 从 1.15 改为 1.5
4. **增量输出**：收集到新 output_dir，与已有数据合并，避免覆盖
5. **成本控制**：总 API 成本 ~$47，可控；主要成本是 GPU 训练时间（~1.8 天）
