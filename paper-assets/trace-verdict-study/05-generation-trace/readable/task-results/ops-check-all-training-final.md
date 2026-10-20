# ops check all training final

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-training-final_20260515T010732_result.json`
- **Structured JSON:** [`a04d1b4cebf0491dcab3.json`](../../sessions/a0/a04d1b4cebf0491dcab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有已有的 predictions 目录，bootstrap_compare.py 需要加载模型推理，超时。直接基于 eval_results.json 汇总。

---

## GPU 状态
- cuda:0: 空闲（49GB VRAM 占用但无活跃进程，残留显存未释放）
- cuda:1: 空闲

## full_trace_seed42_v2
- 状态: **完成**
- exit code: 0
- accuracy: **28.40%** ⚠️ 严重异常——低于 majority baseline (71.5%)
- 训练时长: 2h11m (444 steps, 3 epochs)
- train_loss: 0.0373, eval_loss: 0.0820
- eval_mean_token_accuracy: 98.4%（token 级很高，但分类结果崩了）
- 问题诊断: pass_recall=8.5%, fail_recall=78.5%——模型几乎全部预测 "fail"

完整 eval_results:
```json
{
  "accuracy": 0.2840,
  "majority_baseline": 0.7151,
  "lift": -0.4311,
  "pass_precision": 0.923, "pass_recall": 0.085, "pass_f1": 0.155,
  "fail_precision": 0.445, "fail_recall": 0.785, "fail_f1": 0.568,
  "n": 1190
}
```

## vota_seed42_v4
- 状态: **完成**
- exit code: 0
- accuracy: **99.16%**
- 训练时长: 2h16m (444 steps, 3 epochs)
- train_loss: 0.0460, eval_loss: 0.0842
- eval_mean_token_accuracy: 98.3%

完整 eval_results:
```json
{
  "accuracy": 0.9916,
  "majority_baseline": 0.7151,
  "lift": +0.2765,
  "pass_precision": 1.000, "pass_recall": 0.988, "pass_f1": 0.994,
  "fail_precision": 0.971, "fail_recall": 1.000, "fail_f1": 0.985,
  "n": 1190
}
```

## MVP 三条件对比
| 条件 | Accuracy | Lift vs no_trace |
|------|----------|-----------------|
| no_trace | 75.13% | — |
| vota | 99.16% | **+24.03%** |
| full_trace | 28.40% | **-46.73%** ⚠️ |

- bootstrap CI 未跑（脚本需要模型推理，超时）
- vota 的 95% CI: [98.57%, 99.66%]

## MVP 判定: **PARTIAL PASS / 需要排查 full_trace**

VOTA 条件大幅超过 baseline（+24%，CI 不含 0），单独看 VOTA 是强 PASS。

但 **full_trace 条件严重异常**——accuracy 仅 28.4%，远低于 majority baseline。token-level accuracy 98.4% 说明模型学会了生成正确格式的 token，但**分类决策层崩溃**（几乎全预测 fail）。可能原因：
1. eval 脚本的 label extraction 逻辑与 full_trace 的输出格式不匹配（最可能）
2. full_trace 格式中 verdict token 位置不同，提取时取错了位置
3. 训练数据 label 映射问题

**建议**: 检查 full_trace eval 的 prediction extraction 逻辑——token accuracy 98.4% 但分类 accuracy 28.4% 几乎必然是 label parsing 的 bug，而非模型本身的问题。

---
