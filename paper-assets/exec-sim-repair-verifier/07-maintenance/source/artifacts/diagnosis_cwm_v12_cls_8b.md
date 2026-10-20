# 诊断报告：D056 训练 Early Stop 状态

**日期**: 2026-05-14 ~09:05 (服务器时间)
**服务器**: westd-48478 (seetacloud-westd-4x5090)

---

## 实验 1: repo-level-cwm-v12 (cuda:1)

| 项目 | 值 |
|------|-----|
| 最后 checkpoint | **checkpoint-700** (step 700/6633, epoch 0.317) |
| 日志最后 step | **756/6633** (被 kill 时正在训练) |
| 最佳 checkpoint | checkpoint-500 (eval_loss=0.3066) |
| 训练时长 | ~3:01:00 |
| 退出方式 | EXIT_CODE=137 (SIGKILL) |
| OOM | **无** |

**可用 checkpoint**: 全部 5 个 (300/400/500/600/700) 均含 adapter_model.safetensors，有效。

**日志尾部信息**: ConnectionResetError (multiprocessing resource_sharer)，这是进程被 kill 后的连带错误，非根因。

---

## 实验 2: repo-level-cls-8b-conda (cuda:3)

| 项目 | 值 |
|------|-----|
| 最后 checkpoint | **checkpoint-600** (step 600/6633, epoch 0.271) |
| 日志最后 step | **662/6633** |
| 最佳 checkpoint | checkpoint-200 (eval_loss=0.0796) |
| 训练时长 | ~2:12:38 |
| 退出方式 | 进程消失 (PID 185438 不存在)，log 无 EXIT_CODE 记录 |
| OOM | **无** |

**可用 checkpoint**: 全部 3 个 (200/400/600) 均含 adapter_model.safetensors，有效。

**注意**: eval_loss 在 step 200 后开始上升 (0.0796 → 0.0927 → 0.0937)，checkpoint-200 可能是最优选择。

---

## 实验 3: repo-level-cwm-seed123-conda (cuda:0，D056 列表)

| 项目 | 值 |
|------|-----|
| 最后 checkpoint | **checkpoint-600** (step 600/6633, epoch 0.271) |
| 日志最后 step | **695/6633** |
| 最佳 checkpoint | checkpoint-500 (eval_loss=0.3163) |
| 退出方式 | 进程消失，log 无 EXIT_CODE 记录 |
| OOM | **无** |

**可用 checkpoint**: 全部 5 个 (200-600) 均含 adapter_model.safetensors，有效。

---

## 失败原因判定

**结论: 全部为人为 kill，非 OOM。**

证据:
1. cwm-v12 明确记录 EXIT_CODE=137 (SIGKILL)
2. 三个实验日志均无 OOM 错误信息
3. 所有实验的 loss 曲线正常下降，无异常波动
4. **Eval pipeline 已启动**——4 块 GPU 上有新进程在跑：
   - GPU 0: PID 195531 → `eval_repo_cwm.py` (cwm_seed123_conda/checkpoint-500)
   - GPU 1: PID 195668 → eval 进程
   - GPU 2: PID 194681 → `eval_repo_cls.py` (cls_v5_conda/checkpoint-200)
   - GPU 3: PID 194821 → eval 进程

**与 D056 决策一致**: 训练被 early stop，eval pipeline 已接管所有 GPU。

---

## 各实验进度汇总 (conda 系列)

| 实验 | 最后 step | 进度 | 最佳 ckpt | 状态 |
|------|-----------|------|-----------|------|
| cwm-v12 | 756/6633 | 11.4% | ckpt-500 | killed |
| cls-8b-conda | 662/6633 | 10.0% | ckpt-200 | killed |
| cwm-seed123-conda | 695/6633 | 10.5% | ckpt-500 | killed |
| cls-v5-conda | 643/6633 | 9.7% | — | killed |
