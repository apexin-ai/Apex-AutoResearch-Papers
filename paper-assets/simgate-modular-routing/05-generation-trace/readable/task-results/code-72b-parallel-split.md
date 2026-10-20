# code 72b parallel split

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b-parallel-split_20260517T113603_result.json`
- **Structured JSON:** [`7805e795c2f3c8b12d20.json`](../../sessions/78/7805e795c2f3c8b12d20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都验证通过。

**结果：**

- `src/run_72b_parallel.py` — 主收集脚本，自动检测已完成进度并续跑
  - `--tasks` 指定 task 子集（逗号分隔）
  - `--tp 1` 切换单卡模式（新 96GB 卡用）
  - `--dry-run` 查看计划不执行
  - 默认 11 个 task、20 episodes/task、72B AWQ 模型

- `src/check_72b_progress.sh` — 进度检查，输出未完成 task list 和可直接复制的运行命令

**当前进度：** chemistry-mix 20/20 done, find-animal 6/20 (backbone_eval tmux 仍在跑), 其余 9 个 task 未开始。共 194 episodes 待收集。

**新卡到位后用法：**
```bash
# 先查进度
bash src/check_72b_progress.sh

# 分配给新卡（单卡 TP=1）
python src/run_72b_parallel.py --tp 1 --tasks "freeze,grow-fruit,identify-life-stages-1,identify-life-stages-2,inclined-plane-determine-angle"

# 本机继续跑剩余（TP=2）
python src/run_72b_parallel.py --tasks "find-non-living-thing,lifespan-longest-lived,lifespan-longest-lived-then-shortest-lived,measure-melting-point-unknown-substance"
```

注意：conda 环境需要 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 后再 `python`。

---
