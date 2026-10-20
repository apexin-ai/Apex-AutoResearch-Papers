# deploy a continued and ab reeval

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_a_continued_and_ab_reeval_20260513T173859_result.json`
- **Structured JSON:** [`5cae57c8ba36970aaabf.json`](../../sessions/5c/5cae57c8ba36970aaabf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均正常运行。

## 报告

### 1. GPU 状态
| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 23535 / 97887 MiB | 80% |
| 1 | RTX PRO 6000 Blackwell | 22085 / 97887 MiB | 59% |

### 2. v2 eval 结果
三个 v2 eval 均**未完成**（无 eval_results.json），已被 kill：
- eval_D2_ckpt400_v2：第2个数据集 402/543 (~74%)
- eval_D1_v4_v2：第1个数据集 412/651 (~63%)

### 3. 代码修复验证
- **thinking disable**: train_grpo.py L173/175 ✓, evaluate.py L71/204/206 ✓（前缀注入 `{%- set enable_thinking = false -%}`）
- **relation normalize**: rewards.py L106/141/147 `_normalize_relation` ✓

### 4. A-continued 训练
- tmux session: `train_a_continued`
- PID: **104689** (cuda:0)
- 状态: step 1/500 已完成，~19.5s/step，预计 ~2.7h
- 配置: F1-only reward, LoRA r=64, lr=5e-6, from formal_A/merged

### 5. eval_A_v3 / eval_B_v3
- tmux session: `eval_ab_v3`
- PID: **104831** (cuda:1)
- 状态: eval_A_v3 进行中，scierc_test 14/551，eval_B_v3 待 A 完成后串行启动
- 参数已修正为 `--eval_datasets`

### 6. 日志确认
- train_A_continued.log: 模型加载完毕，LoRA 参数 116M/9B (1.28%)，训练已启动
- eval_A_v3.log: 模型加载完毕，scierc_test 评估进行中

---
