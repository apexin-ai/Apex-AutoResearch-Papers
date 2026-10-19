# research spatial physical data collection

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_spatial-physical-data-collection_20260515T170342_result.json`
- **Structured JSON:** [`370c807e7095cd1a470a.json`](../../sessions/37/370c807e7095cd1a470a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是结论。

---

## 结论

### 1. LIBERO-Plus Assets 状态
- **没有下载进程在运行**
- 核心 assets 已存在：`/root/LIBERO-plus/libero/libero/assets/` = 415MB, 1415 个 XML 文件
- `_add_N` 变体（objects_layout）的额外物体 XML **部分缺失**——和 Phase 0 的 58/90 失败一致

### 2. 能否不依赖 LIBERO-Plus 特殊 assets？

| 扰动类型 | 结论 | 原因 |
|-----------|------|------|
| **Physical (robot_initial_states)** | **能** | 只需基础 BDDL + 不同 init_state 索引（50个，shape [50,92]），不需要任何额外 assets |
| **Spatial (objects_layout)** | **能，但需换方法** | LIBERO-Plus 原生的 `_add_N` 方式需要缺失的物体 XML。但可以用 `bddl_operators.py` 的 `perturb_region_info()` 对已有物体做位置扰动，不需新 assets |

### 3. 具体实现方案

**Physical LoRA — robot_initial_states：**
- 使用基础 BDDL 文件创建环境
- `init_states` 文件有 50 个不同状态；state 0 是 nominal，state 1-49 有不同 robot joint 配置（joint 差异 ~0.04 rad）
- 350 个 `_view_*_initstate_N` 任务已注册在 benchmark 中
- 实现方式：基础 BDDL + `env.set_init_state(init_states[trial_idx])` 其中 `trial_idx > 0`

**Spatial LoRA — objects_layout：**
- 使用 `/root/LIBERO-plus/libero/randomizer/bddl_operators.py` 中的 `perturb_region_info()`
- 参数：`delta_region_centroid_xy`, `delta_region_half_len`, `delta_yaw_rotation`
- 流程：加载基础 BDDL → `load_bddl_file()` → 修改 region_infos → `save_bddl_file()` → 用新 BDDL 创建环境
- 这是**纯位置扰动**（比添加干扰物更切合"spatial"语义）

**Expert Demo 收集策略：**
LIBERO 没有 scripted/oracle policy。用 **π₀ rollout + success filtering**：
1. 在扰动环境跑 π₀
2. 成功的 episode 保存 (obs, action) 轨迹作为 expert demo
3. 失败的丢弃
4. Phase 0 的 30 个 robot_initial_states 和 32 个 objects_layout 已经证明 π₀ 在扰动下有一定成功率

### 4. 推荐数据采集方案

```bash
# 不需要等 LIBERO-Plus assets 下载
# 直接用以下方式收集

# Physical (robot_initial_states): 
# - 用 10 个基础 task × 49 个 non-zero init_states × 重复3次
# - 预计成功率 ~30-50%，跑 ~300 eps 收集 ~100-150 成功 demos
# - 预计耗时: ~2-3 小时（GPU 推理）

# Spatial (objects_layout via perturb_region_info):
# - 用 10 个基础 task × 10 个位置扰动 × 重复3次
# - 预计成功率 ~20-40%，跑 ~300 eps 收集 ~60-120 成功 demos
# - 预计耗时: ~2-3 小时
```

**下一步**：需要写一个 `collect_expert_demos.py` 脚本，核心改动：
1. 保存完整 (obs, action) 轨迹而非 activations
2. 对 spatial：调用 `perturb_region_info()` 生成扰动 BDDL
3. 对 physical：使用不同 init_state 索引
4. 只保留 `success=True` 的 episodes

---
