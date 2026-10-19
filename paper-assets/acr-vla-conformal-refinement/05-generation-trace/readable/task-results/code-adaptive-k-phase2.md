# code adaptive k phase2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adaptive-k-phase2_20260519T082102_result.json`
- **Structured JSON:** [`b1f32b28c03bac460164.json`](../../sessions/b1/b1f32b28c03bac460164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Implementation complete. Here's the summary:

---

## 代码结构

### 修改的文件

**1. `src/smolvla_wrapper.py`** — 新增 2 个方法：
- `generate_adaptive_k_samples(past_key_values, prefix_pad_masks, threshold, k_init=2, k_full=5)` — 核心 adaptive K 采样逻辑
- `get_obs_features_and_samples_adaptive(...)` — 端到端封装（preprocessing + encoding + adaptive sampling）

**2. `src/evaluate.py`** — 6 处修改：
- `parse_args`: 新增 `--adaptive_k`, `--adaptive_threshold`, `--k_init`, `--k_full` 4 个参数
- 新增 `select_action_crm_adaptive` 函数（CGS+CRM pipeline 的 adaptive 版本）
- `evaluate()` 中初始化 `cgs_map` = {k_init: CGS, k_full: CGS}，支持变 K
- Rollout 循环中添加 adaptive 分支，收集 per-step metadata
- 汇总输出 `adaptive_stats`（fast_path_ratio, avg_actual_k, mean_l2_distance）
- 输出文件名包含 adaptive 参数 tag

**3. `src/calibrate_threshold.py`** — 新文件：
- 加载 SmolVLA，跑 N 步收集 K=10 样本
- 计算所有 pairwise L2 距离
- 输出 percentile 分布和推荐 threshold（conservative/balanced/aggressive）

### Adaptive K 逻辑

1. 生成 `k_init=2` 个样本（batched denoising，复用 KV cache）
2. 计算两个样本间 L2 距离：`||a1 - a2||` 在 7D action dims 上，across chunk_size=50 timesteps 取 mean
3. 若 `mean_l2 < threshold` → **fast path**：返回 2 个样本
4. 否则 → **full path**：额外生成 `k_full - k_init = 3` 个样本（第二次 KV cache expansion），拼接后返回 5 个样本
5. CGS 使用 `cgs_map[actual_k]` 匹配实际样本数（CGS 内部有 K 维度断言）

### 需要 Director 决策的点

1. **Threshold 默认值**：当前 default=0.1，实际值需要通过 `calibrate_threshold.py` 在目标 benchmark 上校准后确定
2. **B>1 branching 策略**：当前使用 conservative 策略（任一 batch element disagreement 就走 full path）。eval 场景 B=1 无影响
3. **Full path 额外开销**：full path 需要两次 KV expansion + 两次 denoising loop。如果想避免第二次 KV expansion 的开销，可以改为一次性 expand K=k_full 但只对前 k_init 个样本先做 denoising check（需要更大的架构改动）

---
