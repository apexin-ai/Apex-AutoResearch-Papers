# code qwen seeds expansion

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-seeds-expansion_20260521T062925_result.json`
- **Structured JSON:** [`581fe3c70ff172f9efc7.json`](../../sessions/58/581fe3c70ff172f9efc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**GPU 状态**
| GPU | 当前任务 | 状态 |
|-----|---------|------|
| cuda:0 | Mistral eval (4进程) | 96% util, 23.4G |
| cuda:1 | eval_lz.py + **clean_s4 训练** (新) | 已启动，~2.1s/it |
| cuda:2 | GRPO 训练 | 46% (3221/7021)，~2h15m |
| cuda:3 | eval_with_ht.py + **clean_s5 训练** (新) | 已启动，~2.2s/it |

**已完成操作**
1. 修复 train.py：移除 `os.environ["CUDA_VISIBLE_DEVICES"]` 覆盖，添加 clean_s4=301 / clean_s5=302 到 SEED_MAP
2. 创建数据目录，复用 clean_s1 的 5000 samples
3. 启动训练：PID=85670 (cuda:1) / PID=86218 (cuda:3)，939 steps，~2.1s/step，预计 ~35min 完成
4. Registry 已注册并标记 RUNNING

**注意**: cuda:1 和 cuda:3 各有一个 eval 进程共存（eval_lz.py 和 eval_with_ht.py），显存充足（98G 卡），但 GPU 利用率较高，可能略微影响训练速度。日志路径：`/tmp/train_clean_s4.log` 和 `/tmp/train_clean_s5.log`。

---
