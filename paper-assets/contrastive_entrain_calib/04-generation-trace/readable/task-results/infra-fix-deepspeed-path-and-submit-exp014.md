# infra fix deepspeed path and submit exp014

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-deepspeed-path-and-submit-exp014_20260518T180330_result.json`
- **Structured JSON:** [`26896ff0adecc8c7a042.json`](../../sessions/26/26896ff0adecc8c7a042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰了。

## 报告

**1. Python 绝对路径**
`/root/miniconda3/bin/python` → 符号链接到 `python3.12`

**2. deepspeed 绝对路径**
`/root/miniconda3/bin/deepspeed`

shebang 为 `#!/root/miniconda3/bin/python`，内容就是调用 `deepspeed.launcher.runner.main()`。

**3. 问题根因**
SSH 登录时的 PATH 是：
```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
**不包含 `/root/miniconda3/bin/`**。`.bashrc` 中也没有 conda 初始化。所以 tmux 里的 sh 找不到 `deepspeed`。

exp-004 能跑是因为 `python` 碰巧不在这个 PATH 里也行（或者用了别的 python），但 `deepspeed` 只存在于 miniconda3/bin 下。

**4. 推荐启动命令**

最可靠的方案是直接用绝对路径（方案B），无需任何 conda activate：

```bash
cd /root/contrastive_entrain_calib/training && /root/miniconda3/bin/deepspeed --num_gpus 2 run_exp014_continuous_probe.py
```

或等价的方案C（通过 python -m）：

```bash
cd /root/contrastive_entrain_calib/training && /root/miniconda3/bin/python -m deepspeed.launcher.runner --num_gpus 2 run_exp014_continuous_probe.py
```

两者效果完全一致（deepspeed 脚本本身就是调 `deepspeed.launcher.runner.main()`）。方案B更简洁，推荐使用。

---
