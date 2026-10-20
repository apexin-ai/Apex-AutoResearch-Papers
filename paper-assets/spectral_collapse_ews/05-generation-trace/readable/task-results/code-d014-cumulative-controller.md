# code d014 cumulative controller

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d014_cumulative_controller_20260517T163947_result.json`
- **Structured JSON:** [`4fbe0bb2a8a338dfa7ba.json`](../../sessions/4f/4fbe0bb2a8a338dfa7ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。产出汇总：

---

## Task 1: controller.py cumulative mode

`/root/spectral_collapse_ews/src/controller.py` — 新增 `signal_mode` 参数 (默认 `"per_gen"`)

关键 diff：
- `__init__` 新增 `signal_mode="per_gen"` 参数，存 `self.signal_mode`
- `update()` 中 EMA 和 delta 计算按模式分支：
  - **per_gen**: 原有 EMA 逻辑不变，`delta = (S̃_prev - S̃_cur) / |S̃_0|`
  - **cumulative**: 跳过 EMA (`S_tilde = S_t`)，`delta = max(0, (S_0 - S_t) / |S_0|)`
- `get_state()` 新增 `signal_mode` 字段

## Task 2: run_phase1.py --signal_mode

- L87: `parser.add_argument("--signal_mode", ...)` choices=`['per_gen', 'cumulative']`
- L138: `config.controller_signal_mode = args.signal_mode`
- L141 (pipeline.py): `signal_mode=config.controller_signal_mode` 传入 controller
- L52 (config.py): `controller_signal_mode: str = "per_gen"` 默认值

## Task 3: Dry-run 对比表

```
=== per_gen (k=20, tau=0.002) ===
Gen   S_input     delta       trig   ratio    B_rem    real    synth
0     2366.68     --          --     --       4.5000   --      --
1     (none)      --          --     0.5000   4.0000   25000   25000
2     2464.76     -0.020721   False  0.5000   3.5000   25000   25000
3     2469.93     -0.011453   False  0.5000   3.0000   25000   25000
4     2440.57     +0.000476   False  0.5000   2.5000   25000   25000
5     2405.05     +0.007742   True   0.6148   1.8852   30742   19258
6     2370.17     +0.011240   True   0.6561   1.2291   32804   17196
7     2335.17     +0.013014   True   0.6300   0.5991   31499   18501
8     2304.19     +0.013052   True   0.3991   0.2000   19955   30045
9     2252.12     +0.017527   True   0.2000   0.0000   10000   40000

=== cumulative (k=5, tau=0.01) ===
Gen   S_input     delta       trig   ratio    B_rem    real    synth
0     2366.68     --          --     --       4.5000   --      --
1     (none)      --          --     0.5000   4.0000   25000   25000
2     2464.76     0.000000    False  0.5000   3.5000   25000   25000
3     2469.93     0.000000    False  0.5000   3.0000   25000   25000
4     2440.57     0.000000    False  0.5000   2.5000   25000   25000
5     2405.05     0.000000    False  0.5000   2.0000   25000   25000
6     2370.17     0.000000    False  0.5000   1.5000   25000   25000
7     2335.17     0.013314    True   0.5166   0.9834   25828   24172
8     2304.19     0.026404    True   0.5737   0.4097   28687   21313
9     2252.12     0.048405    True   0.4097   0.0000   20484   29516
```

**对比结论**：
- **per_gen** 从 Gen 5 开始触发（EMA 探测到 inter-gen 下降），早触发但 k=20 导致前期耗尽预算，Gen 8-9 被迫降至 r_min=0.20
- **cumulative** 从 Gen 7 开始触发（log_det 跌破 Gen 0 baseline 后才有正 delta），触发更晚但 delta 单调增长，信号更稳定。预算分配更集中在真正需要的后期
- cumulative 模式下 Gen 7-9 的总 real 样本 = 75,000 vs per_gen 的 Gen 5-9 总 real = 105,000，但 per_gen 在 Gen 8-9 被预算约束压到 r_min

## Task 4: 脚本状态

- **launch_exp_004.sh**: 存在，`fixed_mix --seed 42 --gpu 0 --generations 10`
- **eval_hellaswag.py**: 存在于 `/root/spectral_collapse_ews/eval_hellaswag.py`
- **Phase 0 Gen 9 checkpoint**: 不存在。`/root/autodl-tmp/` 下无 `phase0*gen_9` 目录或 safetensors 文件。需要确认 Phase 0 checkpoints 是否已被清理或存储在其他位置。

---
