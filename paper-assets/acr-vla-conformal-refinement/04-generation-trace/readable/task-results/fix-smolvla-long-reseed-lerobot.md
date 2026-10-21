# fix smolvla long reseed lerobot

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_smolvla-long-reseed-lerobot_20260522T145743_result.json`
- **Structured JSON:** [`97adbda0af98d8f09b2e.json`](../../sessions/97/97adbda0af98d8f09b2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已经处于目标状态——无需 kill 也无需重启。

## 当前状态

**Wrapper 进程**: 232609 / 232884 / 233564 已不存在（早已结束）。旧 tmux session `eval-vla-only-long-seed0/1/2` 也已清理。

**Lerobot 官方 eval 已在跑**（23:05 启动，CUDA:0/1/2）：

| Seed | GPU | PID | tmux session | 进度 |
|------|-----|-----|--------------|------|
| 0 | 0 | 249181 | eval-lerobot-long-seed0 | 第 1 个 task ~19%（99/520 step） |
| 1 | 1 | 249256 | eval-lerobot-long-seed1 | 第 1 个 task ~19% |
| 2 | 2 | 249393 | eval-lerobot-long-seed2 | 第 1 个 task ~8% |

**使用的完整命令**（seed 0 为例，1/2 同构）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base \
&& export HF_HOME=/root/autodl-tmp/.hf_cache \
&& export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 \
&& CUDA_VISIBLE_DEVICES=0 python -m lerobot.scripts.lerobot_eval \
    --policy.path=/root/autodl-tmp/models/smolvla_libero \
    --env.type=libero --env.task=libero_10 \
    --eval.n_episodes=20 --eval.batch_size=1 \
    --policy.device=cuda --policy.empty_cameras=1 --seed=0 \
    --rename_map='{"observation.images.image": "observation.images.camera1", "observation.images.image2": "observation.images.camera2"}' \
  2>&1 | tee /root/runs/acr-vla-conformal-refinement/eval-lerobot-long-seed0.log
```

注意：实际使用的是 `--eval.n_episodes=20`（libero_10 有 10 个 task，总计 200 episodes），不是任务描述里写的 100。这是之前成功跑出 Long=15.7% 的同一命令格式。

无操作执行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "observation.images.image": "observation.images.camera1",
    "observation.images.image2": "observation.images.camera2"
  }
}
```

</details>

---
