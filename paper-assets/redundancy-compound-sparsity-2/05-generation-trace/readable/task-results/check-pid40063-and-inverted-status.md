# check pid40063 and inverted status

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pid40063_and_inverted_status_20260512T164210_result.json`
- **Structured JSON:** [`332f56dbdb9dc97bca68.json`](../../sessions/33/332f56dbdb9dc97bca68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

### 1. PID 40063

**`analysis_gamma_sweep.py`**，不是 inverted EMA 实验。

```
PID 40063 — python analysis_gamma_sweep.py --model /root/carc/models/DeepSeek-R1-Distill-Qwen-14B --gpu 0 --output /root/carc/analysis_gamma_sweep_results.json
```

启动于 00:33，CPU 102%，占用 GPU 0 显存 35946 MiB，运行约 9 分钟。

---

### 2. GPU 进程

| PID | 脚本 | GPU | 显存 |
|-----|------|-----|------|
| 39560 | `run_inverted_ema.py` | GPU 0 | 29360 MiB |
| 40063 | `analysis_gamma_sweep.py` | GPU 0 | 35946 MiB |
| 39080 | `run_inverted_ema_wikitext.py` | GPU 1 | 32704 MiB |

### 3. GPU 概况

| GPU | 利用率 | 显存占用/总量 |
|-----|--------|--------------|
| 0 | 96% | 65320 / 97887 MiB |
| 1 | 27% | 32713 / 97887 MiB |

GPU 0 上跑了两个进程（inverted_ema reasoning + gamma_sweep），显存已用 67%。GPU 1 只跑 wikitext。

---

### 4. Inverted EMA Reasoning 日志（GPU 0, PID 39560）

```
Generating 20 reasoning traces...
Generating traces:  40%|████      | 8/20 [09:04<13:53, 69.44s/it]
```

**进度 8/20 (40%)**，预计还需约 14 分钟。

---

### 5. Inverted EMA WikiText 日志（GPU 1, PID 39080）

WikiText 实验跑得更快，已完成 `full` 策略的 eval（PPL=7.1822），现在在跑 `inverted_ema_0.9` 策略：

```
full: PPL=7.1822  (273.9s) ✅ 完成
inverted_ema_0.9: prefill 50%|█████ | 26/52 — 正在进行
```

---

### 6. 结果文件

`/root/carc/results/` 中只有之前的文件，inverted EMA 的结果文件尚未生成：

```
a2_attn_vs_ema.json      (7175 bytes)
a2_reasoning_traces.json (14468 bytes)
```

- `inverted_ema_results.json` — 不存在
- `inverted_ema_wikitext_results.json` — 不存在

---

### 7. Seed 检查

两个脚本中均**没有** `manual_seed` 或 `random.seed`。结果不可复现。

---

### 总结

- **PID 40063 是 `analysis_gamma_sweep.py`**，不是 inverted EMA 实验，且与 `run_inverted_ema.py` 共享 GPU 0（可能互相拖慢）
- Reasoning 实验 40% (8/20)，预计 ~14 分钟完成
- WikiText 实验已完成 full baseline (PPL=7.1822)，正在跑 inverted_ema_0.9 策略 prefill 阶段
- 两个脚本都没设 seed

---
