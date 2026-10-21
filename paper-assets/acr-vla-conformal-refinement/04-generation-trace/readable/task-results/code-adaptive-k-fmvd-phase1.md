# code adaptive k fmvd phase1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adaptive-k-fmvd-phase1_20260519T164209_result.json`
- **Structured JSON:** [`0fba75bf81a461708376.json`](../../sessions/0f/0fba75bf81a461708376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已完成部署。总结：

**已完成：**
1. **读取代码结构** — 理解了 SmolVLA 的 flow matching denoising 过程（`generate_k_samples_batched` 中的 10-step ODE loop），LIBERO 环境初始化（`load_libero_env`），和 robot state 提取

2. **编写 `calibrate_fmvd.py`** — 创建在 `/root/acr-vla-conformal-refinement/src/calibrate_fmvd.py`
   - `generate_k1_with_fmvd()`: 复制 K=1 denoising loop，在每个 ODE step 记录 `||v_t[:7]||`，计算 FMVD = std(velocity_norms)
   - `compute_k10_variance()`: 用现有 `generate_k_samples_batched(K=10)` 计算 per-DOF variance
   - 两者共享同一个 `encode_prefix` 的 kv_cache
   - 输出 JSON + stdout 统计摘要 + GO/NO-GO 判定

3. **测试验证** — 1 episode 快速测试通过（300 steps, 141s），FMVD 和 K=10 variance 数据正常收集

4. **修复兼容性** — 升级 transformers (4.40.1 → 5.8.1) 解决 lerobot 0.5.1 的导入问题；在脚本中添加 `transformers.masking_utils` 兼容补丁

5. **提交完整任务** — `fmvd-calibration-phase1` 已通过 submit_training_job 提交到 bjb2-28827 cuda:5，n_episodes=5 per task（50 total），预计 ~2h 完成

**下一步：** 等待 job 完成后查看 `logs/fmvd_calibration.json`，检查 Spearman ρ 是否 > 0.3（GO gate）。

---
