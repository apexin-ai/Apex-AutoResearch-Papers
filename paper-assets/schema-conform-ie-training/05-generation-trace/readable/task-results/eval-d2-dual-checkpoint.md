# eval d2 dual checkpoint

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d2_dual_checkpoint_20260513T095648_result.json`
- **Structured JSON:** [`eea13ec204c25f3f56eb.json`](../../sessions/ee/eea13ec204c25f3f56eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All systems running:
- **GPU 0**: D2 ckpt400 eval started, evaluating scierc_test (551 samples)
- **GPU 1**: D1 v4 training at 395/500

Now let me compile the full report.

## D2 Phase 2
- **训练**：完成 (500/500)，耗时 3h17m55s
- **最终 metrics** (step 500): loss=-0.00318, reward=0.5025, reward_std=0.11
- **Step 490 metrics**: reward=0.545
- **checkpoint-400 merge**：成功 → `/root/autodl-tmp/output/formal_D2/checkpoint-400-merged`
- **Eval checkpoint-400**：已启动 (tmux: eval_d2_dual, cuda:0)，正在跑 scierc_test
- **Eval merged**：排在 ckpt400 后面串行（同一 tmux session）

## D1 v4
- **训练**：运行中 (395/500)，~30s/step，预计 ~54 min 后完成 (~18:58 UTC)
- D1 eval 需等训练完成后启动

## eval_C_v2 完整指标

| Metric | scierc_test | crossner_politics | crossner_science |
|--------|------------|-------------------|------------------|
| f1_correctness | 0.2184 | 0.4116 | 0.5329 |
| structural_validity | 0.9964 | 1.0000 | 0.9982 |
| type_conformance | 0.9537 | 0.9997 | 0.9781 |
| relational_constraint | 0.7191 | 0.0000 | 0.0000 |
| structural_completeness | 0.9543 | 0.9932 | 0.9678 |
| entity_f1 | 0.3949 | 0.4158 | 0.5514 |
| relation_f1 | 0.0000 | 0.0000 | 0.0000 |
| valid_json_rate | 0.9964 | 1.0000 | 0.9982 |

注：eval_C_v2 日志标注为 base model eval（加载的是 `/root/autodl-tmp/models/Qwen/Qwen3.5-9B`），输出保存在 `base_zero_shot_v2/`。

## GPU 状态
```
GPU 0: 59% util, 22083/97887 MiB (D2 ckpt400 eval)
GPU 1: 75% util, 54311/97887 MiB (D1 v4 training)
```

---
