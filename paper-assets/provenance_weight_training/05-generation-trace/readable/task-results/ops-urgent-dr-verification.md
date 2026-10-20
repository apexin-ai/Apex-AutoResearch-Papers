# ops urgent dr verification

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_dr_verification_20260525T035404_result.json`
- **Structured JSON:** [`b188061af55977659b87.json`](../../sessions/b1/b188061af55977659b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集，汇报如下：

---

```
1. Eval 已去掉？ YES ✓
```

三个进程命令行均**无** `--eval_data_path` 或 `--eval_steps`：

| 实验 | PID | Resume from | 当前进度 | eval参数 |
|------|-----|-------------|----------|----------|
| q05 | 8049 | checkpoint-5500 | 5678/6103 (93%) | 无 |
| q03 | 8472 | checkpoint-3000 | 3152/6103 (52%) | 无 |
| q07 | 8867 | checkpoint-2500 | 2646/6103 (43%) | 无 |

GPU 显存：GPU 1/2/3 各 45643 MiB / 97887 MiB (~47%)，利用率 99-100%。GPU 0 空闲 (0 MiB)。

```
2. cuda:0 eval 结果？ 已完成 ✓
```

PID 5867/6325 均已退出。Eval 全部跑完，结果：

| 数据集 | Loss | PPL |
|--------|------|-----|
| Holdout | 2.8502 | **17.29** |
| OWT | 2.8916 | **18.02** |
| Wikipedia | 2.7118 | **15.06** |

结果文件已保存在 `/root/provenance_weight_training/eval_results_dr_q05_ckpt5500_{holdout,owt,wiki}.json`。

```
3. Registry 状态？ 需修正
```

| exp_id | 当前 status/conclusion | 实际状态 | 需要操作 |
|--------|----------------------|----------|----------|
| detect_remove_q05_seed42 | DONE/**failed** | PID 8049 在跑 (93%) | → 改回 RUNNING |
| detect_remove_q03_seed42 | RUNNING | PID 8472 在跑 (52%) | OK |
| detect_remove_q07_seed42 | DONE/success | PID 8867 在跑 (43%) | → 可能需改回 RUNNING（这是 kill+resume 后的新进程） |
| eval_dr_q05_ckpt5500 | RUNNING | 已完成 | → 改为 DONE/success |

```
4. q03 新进程？ OK ✓
```

PID 8472 正常运行，step 3152/6103，~2.08s/it。

---

需要我修正 registry 条目吗？需要修正的有：
- `detect_remove_q05_seed42`: DONE/failed → RUNNING
- `detect_remove_q07_seed42`: DONE/success → RUNNING（如果这是 resume 后的新跑）
- `eval_dr_q05_ckpt5500`: RUNNING → DONE/success

---
