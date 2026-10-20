# code plan004 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-prep_20260514T111444_result.json`
- **Structured JSON:** [`f65b12218b368e138701.json`](../../sessions/f6/f65b12218b368e138701.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。以下是 plan004 的完整产出报告。

---

## Plan004 准备完成

### 配置文件
`/root/solver-trace-ablation/configs/grpo_fast_isr_ablation.yaml`

### 启动命令
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py --config configs/grpo_fast_isr_ablation.yaml > /tmp/plan004_fast_isr.log 2>&1 &
```

### 代码改动
`scripts/train_grpo.py` 第 211-216 行，新增 `execution_fast_sta` reward mode：
- 调用 `_fast_fn`（即 `fast_sta_reward`）替代 `_full_fn`（即 `sta_reward`）
- argparse choices 已同步更新

### O(1) vs O(N) ISR 关键区别

| | O(N) `sta_reward` | O(1) `fast_sta_reward` |
|---|---|---|
| 函数 | `compute_isr(run_sta(...))` | `fast_isr_fol(...)` |
| solver 调用数 | 1 + N（N=前提数） | 2（固定） |
| 返回值域 | [0, 1] 连续（necessary/total） | {0, 1} 二值 |
| 判定逻辑 | 逐条删除前提，检查每条是否必要 | 仅检查：结论是否为重言式（无前提可证） |
| 丢失的信息 | — | 部分冗余（5条前提中3条必要 → ISR=0.6，但 fast 返回 1.0） |

这正是 plan004 要证明的：O(1) 近似把连续 ISR 信号压缩为二值，在训练中无法区分"部分冗余"和"完全必要"的 formalization，导致 reward signal 退化。

### 预计 GPU 时间
~4-5 小时（500 steps, K=8, Qwen3-4B）。O(1) ISR 每样本只需 2 次 solver 调用，比 O(N) 快约 3-5x，但 GPU 时间主要受模型 forward/backward 约束。

### 注意
- 两张 GPU 当前均被占用，需等 plan006 完成释放 cuda:0 后再提交
- Dry-run 无法执行（GPU 内存不足），但语法验证、AST 解析、import 检查均通过

---
