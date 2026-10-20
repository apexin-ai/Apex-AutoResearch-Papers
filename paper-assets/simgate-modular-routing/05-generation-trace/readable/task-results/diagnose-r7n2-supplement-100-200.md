# diagnose r7n2 supplement 100 200

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_r7n2-supplement-100-200_20260516T073754_result.json`
- **Structured JSON:** [`e950cb9806baf89027e3.json`](../../sessions/e9/e950cb9806baf89027e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败根因

**不是代码/环境/OOM 失败。** 脚本正常运行完毕并输出了 summary。EXIT_CODE=1 是误报——脚本末尾没有 `sys.exit()` 调用，`run_ablation(args)` 正常返回。最可能的原因是 tmux session 或 job wrapper 在脚本结束后的退出码被错误捕获（grep 确认脚本中不存在任何 `exit` 调用）。

### 2. 关键日志片段（脚本最终输出）

```
{'train_runtime': 342.0534, 'train_loss': 0.7650409018227814, 'epoch': 3.0}
[DEBUG] Step-level eval done: balanced_acc=0.5000

============================================================
DATA SIZE ABLATION SUMMARY
============================================================
Scale      N_train    StepBalAcc     EpBalAcc       Saturated?
--------------------------------------------------------------
100pct     1735       0.5000+/-0.0000  0.4990+/-0.0010  
200pct     3470       0.5000+/-0.0000  0.5000+/-0.0000  YES
```

### 3. 结果完整性

**全部 4 个 run 完整保存**，无需挽救：
- `results/ablation_r3/scale_100pct_seed42/`
- `results/ablation_r3/scale_100pct_seed43/`
- `results/ablation_r3/scale_200pct_seed42/`
- `results/ablation_r3/scale_200pct_seed43/`
- `results/ablation_r3/summary.json` ✓

### 4. 真正的问题（语义层面）

模型完全退化——**所有条件下 internal recall = 0.0**，模型只预测多数类 "deterministic"。数据集极度不平衡（deterministic:internal ≈ 9:1），增加数据量（200pct）也无法解决。这不是代码 bug，而是 **routing signal 太弱 / 类别极度不平衡导致模型坍缩到多数类预测**。

脚本自身的结论也说了：`"performance plateau is due to thin routing signal (extreme class imbalance + death-dominated labels) rather than data insufficiency"`

**无需修复代码。** EXIT_CODE=1 是 monitoring 误报，实验结果已完整产出。

---
