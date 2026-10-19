# code eval script prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_script_prep_20260516T025014_result.json`
- **Structured JSON:** [`e76838ad2a411b25bd74.json`](../../sessions/e7/e76838ad2a411b25bd74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。汇总结果：

---

## 1. eval 脚本状态

**`/root/acib/scripts/run_acib_eval.sh` 已存在且完备**，语法验证通过。覆盖：
- 4 suites nominal (libero_spatial, libero_object, libero_goal, libero_10)
- 50 episodes/suite
- 接受 `&lt;checkpoint_dir> &lt;gpu_id> [seed_label]` 参数
- 输出到 `&lt;checkpoint_dir>/eval[_&lt;seed_label>]/&lt;suite>_nominal/`
- 失败不中断、每 suite 打印成功率、写 summary.txt

用法：
```bash
bash /root/acib/scripts/run_acib_eval.sh /root/acib/outputs/acib_v5_div_reg 0 seed1
bash /root/acib/scripts/run_acib_eval.sh /root/acib/outputs/acib_v5_div_reg_seed2 1 seed2
```

## 2. LIBERO-Plus 扰动评测：**不可用**

深入排查了 lerobot 和 libero 底层库：
- `lerobot/envs/libero.py` 无扰动参数
- libero benchmark 只有 5 个标准 suites（spatial, object, goal, 10, 90），无扰动变体
- libero 有 `textures.py` 但仅用于场景初始化，非运行时扰动
- 现有脚本已明确注释：*"The strings 'baseline_plus' / 'smolvla_libero_plus' refer to a different pretrained HF model, not a perturbation suite"*

如需视觉扰动鲁棒性测试，需自行实现（如修改 MuJoCo XML texture/lighting、注入 camera noise 等）。

## 3. Baseline 已有结果

| Suite | baseline_std | baseline_plus |
|-------|-------------|---------------|
| libero_spatial | 66.0% (330/500) | 81.6% (408/500) |
| libero_object | 67.8% (339/500) | 88.8% (444/500) |
| libero_goal | 76.4% (382/500) | 87.8% (439/500) |
| libero_10 | MISSING | **正在跑** |

## 4. 训练进度

- **seed 1** (`acib_v5_div_reg`): step 4700/20000, 0.9 steps/s → 预计 ~15:40 UTC 完成
- **seed 2** (`acib_v5_div_reg_seed2`): step 200/20000, 0.8 steps/s → 预计 ~17:45 UTC 完成
- 两个都在 cuda:0 上跑（seed1 正在训练，seed2 刚启动）

eval 脚本已就绪，训练完成后直接启动即可。

---
