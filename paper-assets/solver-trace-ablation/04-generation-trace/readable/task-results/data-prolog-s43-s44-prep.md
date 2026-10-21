# data prolog s43 s44 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_prolog-s43-s44-prep_20260514T115720_result.json`
- **Structured JSON:** [`676ee5e42b2d1c530327.json`](../../sessions/67/676ee5e42b2d1c530327.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。

```
=== 阻塞原因 ===
ROADMAP 标注"阻塞于数据"是错误的。数据不缺。
真正阻塞：GPU 占用。cuda:0 跑 plan006-prolog-exec-s42，cuda:1 跑 plan009-sft-baseline。

=== 数据状态 ===
训练数据: 存在 — data/train_500_seed42.jsonl（所有 seed 共用同一文件，C001 合规）
Eval 数据: 存在 — data/test_100.jsonl（= test_held_out.jsonl）
Seed 处理: 通过 --seed 参数控制（模型初始化 + 训练随机性），不需要 seed-specific 数据文件

=== 配置状态 ===
- configs/grpo_prolog_exec_only.yaml: 存在，logic_type=prolog, reward_mode=execution_only
- configs/grpo_prolog_exec_sta.yaml: 存在，logic_type=prolog, reward_mode=execution_sta
- eval_sta.py: 已支持 --logic_type prolog（readiness report 说缺失是过期信息）

=== 启动命令（s43/s44 各 4 个实验） ===
# plan006-prolog-exec-s43
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
nohup python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml \
  --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 \
  --wandb_run prolog_exec_s43 > /root/autodl-tmp/outputs/plan006_prolog_exec_s43.log 2>&1 &

# plan006-prolog-exec-s44（同理，--seed 44）
# plan006-prolog-sta-s43（用 grpo_prolog_exec_sta.yaml，--seed 43）
# plan006-prolog-sta-s44（用 grpo_prolog_exec_sta.yaml，--seed 44）

=== 已采取行动 ===
无需生成数据。排查确认：训练数据、eval 数据、配置文件、eval_sta.py Prolog 支持均已就绪。

=== 结论 ===
s43/s44 可以在 GPU 释放后立即开始训练。无数据阻塞。
ROADMAP "阻塞于数据" 标注应更正为"阻塞于 GPU"。
```

---
