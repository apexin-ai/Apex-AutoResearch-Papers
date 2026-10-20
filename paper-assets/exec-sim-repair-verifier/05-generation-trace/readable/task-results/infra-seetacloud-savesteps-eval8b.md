# infra seetacloud savesteps eval8b

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_seetacloud-savesteps-eval8b_20260512T160140_result.json`
- **Structured JSON:** [`6f58138bacf892b00ff4.json`](../../sessions/6f/6f58138bacf892b00ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## 1. save_strategy / save_steps 配置

| 脚本 | save_strategy | save_steps | save_total_limit |
|------|--------------|------------|-----------------|
| `train_repo_verifier.py` (L249) | `"epoch"` (dryrun 时 `"no"`) | 未设置 | 2 |
| `train_repo_cwm.py` (L247) | `"epoch"` (dryrun 时 `"no"`) | 未设置 | 2 |

两个脚本都按 epoch 保存，save_total_limit=2，配置正常。无 D024 违规风险。

## 2. repo-level 训练状态

**⚠️ 两个训练进程均已崩溃，所有 GPU 空闲。**

- GPU 0-3：全部 0 MiB / 0% 利用率
- 无 `train_repo` 相关 python 进程在运行
- **两个 log 相同错误**（EXIT_CODE=1）：
  ```
  ValueError: type of {...} unknown: &lt;class 'dict'>. Should be one of a python, numpy, or pytorch object.
  ```
  崩溃位置：DataCollator 的 `__call__` → `tokenizer.pad()` 收到了 dict 而非 tensor。两个脚本都在 0% 进度（0/6633）就挂了。

## 3. 8B CLS eval JSON

| seed | checkpoint 路径 | accuracy | fail_f1 | pass_f1 |
|------|----------------|----------|---------|---------|
| seed42 | `checkpoints_cls8b/best` | **90.48** | 90.06 | 90.86 |
| seed123 | `checkpoints_cls8b_seed123/best` | **89.37** | 89.19 | 89.54 |

- `eval_cls8b_seed42.json` — **新生成** ✅
- `eval_cls8b_seed123.json` — 已存在，内容有效 ✅
- 两个 eval 均无 unparseable predictions

## 4. checkpoint 路径列表

```
/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best          # CLS 8B seed42
/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best  # CLS 8B seed123
/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b/best          # CWM 8B (default seed)
/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed123/best  # CWM 8B seed123
/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed456/best  # CWM 8B seed456
/home/sonny/exec-sim-repair-verifier/checkpoints/best                # CLS default
/home/sonny/exec-sim-repair-verifier/checkpoints_cls_seed0/best      # CLS seed0
/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed123/best    # CWM seed123
/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed789/best    # CWM seed789
/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls/           # repo-level CLS (无 best/)
/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cwm/           # repo-level CWM (无 best/)
```

---
