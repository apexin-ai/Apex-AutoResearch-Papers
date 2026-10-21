# diag grasp eval command verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grasp-eval-command-verify_20260515T152338_result.json`
- **Structured JSON:** [`8e0799254817a4285397.json`](../../sessions/8e/8e0799254817a4285397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. 实际运行命令
```
python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096
```
- **未传 `--output_path`**
- **未传 `--seed`**

### 2. eval_gsm8k.py 源码分析

**`--output_path`**: default=None，但有自动生成逻辑：
```python
if args.output_path is None:
    model_name = os.path.basename(args.model_path.rstrip("/"))
    args.output_path = f"results/eval_{model_name}_{mode}.json"
```
→ 会自动保存到 **`/root/recovery_aware_struct_prune/results/eval_pruned_graspune_20_greedy.json`**

**`--seed`**: default=**42** → 即使没传，seed 42 已生效。

### 3. 日志捕获状态

PID 38120 的 fd/1 和 fd/2 都重定向到：
**`/root/recovery_aware_struct_prune/results/eval_grasp_n100.log`**

stdout 正在录。当前进度 **95/100**，~51s/sample，约 **4 分钟后完成**。

注意：`/root/runs/recovery_aware_struct_prune/grasp_baseline_westd.log` 是另一个旧 run（1319 samples），与当前 PID 无关。

### 4. 结论：结果安全

| 项目 | 状态 |
|------|------|
| `--output_path` | 未传但有默认值，JSON 会自动写到 `results/eval_pruned_graspune_20_greedy.json` |
| `--seed 42` | 未传但 default=42，已生效 |
| stdout 日志 | 已重定向到 `results/eval_grasp_n100.log`，不会丢失 |
| 进度 | 95/100，约 4 分钟完成 |
| 50-sample 中间指标 | acc=0.0600, eos_rate=2.00%, avg_len=4018 |

**不需要干预。** 结果会自动保存为 JSON 文件，日志也在录。

---
