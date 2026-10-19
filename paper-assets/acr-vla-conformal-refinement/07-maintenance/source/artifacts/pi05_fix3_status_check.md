# π0.5 fix3 quicktest 状态检查

**检查时间**: 2026-05-21 12:56 (北京时间)
**服务器**: bjb2-40593

## 进程状态

- **PID**: 831620
- **状态**: ✅ 存活 (STAT=Rl, 运行 15:56)
- **启动时间**: 12:40:41
- **GPU**: GPU-a7c79137 (cuda:0), 占用 13562 MiB
- **CPU**: 337% / 内存 11.3 GB

## 运行配置

```
src/evaluate.py --model pi05 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned \
  --mode vla_only --benchmark object --seed 42 \
  --n_rollouts 5 --K 1 \
  --output_file logs/eval_pi05_quicktest.json
```

- 模式: vla_only
- benchmark: object（10 tasks）
- rollouts/task: 5
- 总 rollouts: 50
- 日志: `/tmp/eval_pi05_quicktest.log`

## 进度

| Task | 状态 | SR |
|------|------|-----|
| 1. alphabet_soup | ✅ 完成 (5/5 rollouts) | **0.0%** (0/5) |
| 2. (running) | 进行中 | — |
| 3-10 | 待执行 | — |

**当前进度**: 1/10 tasks 完成, 估算总耗时 ~2.5h（按 15min/task）

## 关键观察

### ✅ 修复成功的信号
- **vision tower key 重命名生效**: 日志显示 `[pi05] Fixed 437 vision tower keys`，437 个 missing keys 和 437 个 unexpected keys 一一对应（fix3 的核心修复）
- **模型加载成功**: `✓ Loaded state dict from model.safetensors`
- **环境加载正常**: `[eval] 10 tasks loaded`
- **rollout 正常推进**: alphabet_soup 5/5 rollouts 全部跑完，无报错

### ❌ 仍未突破的问题
- **task 1 SR = 0.0%** (0/5)，与之前 fix2 的全量评测结果（0/200）一致
- 即使 vision tower 权重正确加载，模型仍无法完成 object pick-and-place 任务
- **没有 SR > 0% 的突破信号**

### 历史对照
- `eval-pi05-baseline-object-seed42-r2.log`（之前完成的全量评测，200 rollouts）: **0/200 = 0.0%**
- 当前 quicktest 第一个 task：**0/5 = 0.0%**（趋势一致）

## 日志摘要

```
[eval] Loading PI05 from /root/autodl-tmp/models/pi05_libero_finetuned...
✓ Loaded state dict from model.safetensors
Missing keys when loading state dict: 437 keys
Unexpected keys when loading state dict: 437 keys
[pi05] Fixed 437 vision tower keys
[eval] Loading LIBERO object environments...
[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[eval] 10 tasks loaded.
  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/5, success so far: 0/5
[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/5)
```

无 ERROR / Exception / OOM 等异常。

## 其他 π0.5 进程

仅 PID 831619 (父 bash) + 831620 (python 主进程)。无其他并发 π0.5 任务。

## 结论

- **进程健康**: ✅ 正常运行，无崩溃，权重加载修复（437 keys）生效
- **SR 信号**: ❌ 第一个 task 仍是 0%，**fix3 未带来突破**
- **下一步建议**: 等 quicktest 跑完（再 ~2h，约 14:30 完成）确认全部 task 都是 0%。如果确认 fix3 路径下依然全 0%，需要排查 vision tower 权重的语义正确性（key 名对了，但 tensor shape / layout / scale 可能仍有问题），或 action head 解码逻辑
