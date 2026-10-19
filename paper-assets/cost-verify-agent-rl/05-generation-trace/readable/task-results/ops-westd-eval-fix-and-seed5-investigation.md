# ops westd eval fix and seed5 investigation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_eval_fix_and_seed5_investigation_20260522T083409_result.json`
- **Structured JSON:** [`c5446a788f6392a9e23f.json`](../../sessions/c5/c5446a788f6392a9e23f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重大发现。seed4 已完成，**GPU 1 已释放**。seed4 结果令人警惕：eval_checkpoint.py 报 **6.72%** OOD，而之前 RAGEN eval 报 **30.60%**。这是 4.5 倍差异。

以下是完整报告：

---

## 任务 1：当前 4 个 eval 状态

| Eval | GPU | 进度 | SUCCESS | 状态 |
|------|-----|------|---------|------|
| **seed4_step15** | 1 | 134/134 | 9/134 (6.72%) | ✅ **已完成** |
| **seed5_step10** | 2 | ~123/134 | 19/~123 (~15.4%) | 运行中 |
| **seed6_step15** | 3 | ~82/134 | 14/~82 (~17.1%) | 运行中 |
| **sft_baseline** | 0 | ~99/134 | 14/~99 (~14.1%) | 运行中 |

GPU 1 已空闲（0% util, 3 MiB）。

## 任务 2：seed5 数据差异调查

**结论：eval 方法不一致导致性能暴跌，不是 checkpoint 问题。**

- 统一 pipeline 用 `eval_checkpoint.py` (vLLM)：**HISTORY_LENGTH = 5**（只保留最近 5 轮 obs-action 对）
- 先前 RAGEN eval：**context_window_mode = full**（保留完整历史）
- Checkpoint 相同：都指向 `/root/autodl-tmp/checkpoints/exp029-seed5/global_step_10_hf`
- Temperature 相同：都是 0.4
- seed4 对比证实：RAGEN 30.60% → eval_checkpoint.py **6.72%**（4.5 倍下降）

**根因**：ALFWorld 多步任务需要跟踪完整探索历史。HISTORY_LENGTH=5 导致模型丢失关键上下文（已访问位置、已拾取物品），频繁重复无效动作（seed4 action_is_valid 从 63.67% 降至 38.48%）。

注：table1_ood_summary.md 记录 seed5 为 29.10%（非 37.31%）。37.31% 来源不明。

## 任务 3：7 个崩溃 eval 错误确认

全部同一错误：
```
RuntimeError: Cannot re-initialize CUDA in forked subprocess.
To use CUDA with multiprocessing, you must use the 'spawn' start method
```
vLLM v1 EngineCore 在 forked 子进程中无法重新初始化 CUDA。尽管 eval_checkpoint.py 已设置 `multiprocessing.set_start_method('spawn')`, 但 7 个崩溃的 eval 是从一个已初始化 CUDA 的父进程（并行启动器）fork 出来的。4 个成功的是作为独立进程启动的。

崩溃路径（全部确认）:
1. seed8_step5 → `qwen_exp029_seed8_step5_hf`
2. intervention_c_step5 → `intervention_c_hard_cap_step5_hf`
3. intervention_c_step7 → `intervention_c_hard_cap_step7_hf`
4. c_prime_step5 → `qwen_c_prime_step5_hf`
5. high_kl_step5 → `exp029_seed7_high_kl_step5_hf`
6. high_kl_step7 → `exp029_seed7_high_kl_step7_hf`
7. seed2048_step5 → `qwen_seed2048_step5_hf`

## 任务 4：Checkpoint 路径验证

| Name | Path | 状态 |
|------|------|------|
| seed8_step5 | `/root/autodl-tmp/checkpoints/qwen_exp029_seed8_step5_hf` | ✅ 存在 |
| seed2048_step5 | `/root/autodl-tmp/checkpoints/qwen_seed2048_step5_hf` | ✅ 存在 |
| c_prime_step5 | `/root/autodl-tmp/checkpoints/qwen_c_prime_step5_hf` | ✅ 存在 |
| intervention_c_step5 | `/root/autodl-tmp/checkpoints/intervention_c_hard_cap_step5_hf` | ✅ 存在 |
| intervention_c_step7 | `/root/autodl-tmp/checkpoints/intervention_c_hard_cap_step7_hf` | ✅ 存在 |
| high_kl_step5 | `/root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf` | ✅ 存在 |
| high_kl_step7 | `/root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step7_hf` | ✅ 存在 |

注：`intervention_c` 和 `c_prime` 是**不同的实验**（intervention_c = hard cap 限制, c_prime = trajectory cap 限制），checkpoint 路径不同。

## Round 2 状态

**未启动**。3 个 eval 仍在运行，且：

**⚠️ 关键决策点**：eval_checkpoint.py 的 HISTORY_LENGTH=5 导致所有结果与 RAGEN eval 不可比。seed4 从 30.60% 暴跌到 6.72%。继续用同一脚本跑 Round 2 的 7 个 checkpoint 将产生同样被低估的结果。

建议选项：
1. **修复 HISTORY_LENGTH** → 改为 full context 或至少 20+，重跑所有 11 个 checkpoint
2. **继续当前方法** → 接受 eval_checkpoint.py 的结果作为一致的横向对比基准（虽然绝对值低于 RAGEN，但相对排序可能一致）
3. **改用 RAGEN pipeline** → 用 RAGEN hydra eval 重跑，确保与之前的结果可比

需要你决定如何处理再启动 Round 2。

---
