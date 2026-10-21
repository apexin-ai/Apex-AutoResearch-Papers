# ssh check all running status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_running_status_20260521T115310_result.json`
- **Structured JSON:** [`2fd981ba13e880ffb552.json`](../../sessions/2f/2fd981ba13e880ffb552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。汇总如下：

## 实验状态汇总

| exp_id | server | gpu | status | progress | ETA | key_metrics |
|--------|--------|-----|--------|----------|-----|-------------|
| exp_fewnerd_n16_s42_v2 | autodl-5090 | cuda:0 | **RUNNING** | 13% (79984/602368) | ~2h26m | — |
| exp_fewnerd_mf4v2_s42 | autodl-5090 | cuda:1 | **RUNNING** (PID stale) | 83% (250288/301184) | ~19m | — |
| exp_fewnerd_mf4v2_s123 | autodl-5090 | cuda:2 | **RUNNING** (PID stale) | 82% (247096/301184) | ~20m | — |
| exp_e2_pretrained_fewnerd | autodl-5090 | cuda:3 | **RUNNING** (2nd pass) | 9% (3260/37648) of pass 2 | ~38m | — |
| exp_fewnerd_n16_s123 | autodl-5090-c | cuda:0 | **RUNNING** | 12% (74656/602368) | ~2h42m | — |
| exp_conll_n16_s42 | autodl-5090-c | cuda:2 | **COMPLETED** | 100% (3453/3453) | — | 见下方 |
| exp_e2_pretrained_fewnerd_s123 | autodl-5090-c | cuda:3 | **RUNNING** | 38% (115048/301184) | ~2h11m | — |

## 已完成实验：exp_conll_n16_s42 完整指标

```
verdict: PASS
greedy_f1:        0.9080
oracle_f1:        0.9592
oracle_headroom:  0.0512
fleiss_kappa:     0.7620
soft_jaccard:     0.8844
n_instances:      3453

correlation (full):
  FK  vs F1: rho=0.4222  (p=1.4e-119, n=2756)
  SJ  vs F1: rho=0.4414  (p=8.8e-132, n=2756)
  LP  vs F1: rho=0.3144  (auroc=0.7528)

correlation (conditional):
  FK  vs F1: rho=0.3606
  SJ  vs F1: rho=0.3999
  LP  vs F1: rho=0.3709  (auroc=0.8220)

structural_beats_surface: true  (rho_advantage=+0.019)
sample_f1_mean: 0.8673 (std=0.289, 7.8% zero)
n_gold_empty_filtered: 697
n_greedy_f1_zero_filtered: 139
```

## 注意事项

- **PID 不一致**：`exp_fewnerd_mf4v2_s42` 和 `exp_fewnerd_mf4v2_s123` 的注册 PID（13177/13035）已死，实际 VLLM 子进程（27074/27228）仍在运行。registry 需要更新 PID。
- **exp_e2_pretrained_fewnerd**：已完成第一轮 301184 prompts 采样，正在进行第二轮（greedy/eval pass，37648 prompts），约 38 分钟后结束。
- **exp_e2_pretrained_fewnerd_s123**：日志写在 `/tmp/exp_e2_pretrained_fewnerd_s123.log`（非标准路径），不在 `~/runs/` 下。
- **exp_conll_n16_s42**：已完成并释放 GPU 2，registry 状态需更新为 DONE。

---
