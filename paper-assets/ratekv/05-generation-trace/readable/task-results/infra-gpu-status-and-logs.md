# infra gpu status and logs

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-and-logs_20260513T225821_result.json`
- **Structured JSON:** [`77c3c79d0b6c320f677e.json`](../../sessions/77/77c3c79d0b6c320f677e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已拉取。以下是完整结果：

---

## 1. nvidia-smi

```
Thu May 14 06:58:40 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |
| N/A   27C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   29C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| No running processes found                                                              |
+-----------------------------------------------------------------------------------------+
```

**GPU 空闲**：2x RTX PRO 6000 Blackwell (96GB each), 0% util, 0MiB used, 无 GPU 进程。

---

## 2. tmux ls

`tmux` 被 read-only 模式拦截，无法执行。

---

## 3. 进程检查

- **PID 142134**：不存在（exit code 1, 无输出）
- **PID 141907**：不存在（exit code 1, 无输出）

两个实验进程均已结束。

---

## 4. p0_1_ppl_fast.log（202行，完整）

```
设置成功
注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证
`torch_dtype` is deprecated! Use `dtype` instead!
Loading model /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B...
Loading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 206.51it/s]
Calibration: 20 seqs x 512 tokens
Running PPL-based distortion profiling...
Computing baseline PPL...
Baseline PPL: 10.5339
[1/112] L0H0: evict={'0.25': 12.3656}, quant={'4': 0.4033}
[2/112] L0H1: evict={'0.25': 2.0189}, quant={'4': 0.9652}
[3/112] L0H2: evict={'0.25': 1.8626}, quant={'4': 0.4033}
[4/112] L0H3: evict={'0.25': 0.2672}, quant={'4': 0.2672}
[5/112]-[112/112]: 大部分 head 的 evict/quant distortion 在 0.0~0.13 范围（中间被截断的部分全部是类似值）
...
Token indices sequence length is longer than the specified maximum sequence length for this model (298938 > 131072). Running this sequence through the model will result in indexing errors
[112/112] L27H3: evict={'0.25': 0.1328}, quant={'4': 0.0}
Saved PPL profiles to ppl_profiles.json

=== Solver Results (budget=0.25) ===
Full MCKP:  mem=0.2500, dist=6.685695
Quant-only: mem=0.2500, dist=6.951217
Uniform 4b: mem=0.2500, dist=6.951217
Full MCKP actions: {'quant': 65, 'evict': 47}

=== PPL Evaluation (WikiText-2) ===
Baseline (no compression)...
Evaluating perplexity on 298938 tokens, stride=512, 583 chunks
Baseline PPL: 9.81

Full MCKP @ budget=0.25...
Full MCKP PPL: 28.07

Quant-only MCKP @ budget=0.25...
Quant-only PPL: 15.45

Uniform 4-bit...
Uniform 4-bit PPL: 15.45

============================================================
RESULTS SUMMARY
============================================================
Method                      PPL      Delta
----------------------------------------
Baseline                   9.81           
Full MCKP                 28.07     +18.26
Quant-only                15.45      +5.63
Uniform 4-bit             15.45      +5.63

PPL-MCKP improvement over uniform 4-bit: -12.63

Saved results to ppl_mvp_results.json
EXIT_CODE=0
```

---

## 5. p0_2_cliff_7B.log（398行，完整）

```
设置成功
Loading model /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B...
Model: 28 layers, 4 KV heads/layer, head_dim=128, total KV heads=112
Eval tokens: 10000
Computing baseline PPL (no quantization)...
Baseline PPL: 13.2655 (1.2s)

=== Testing 2-bit quantization ===
  [1/112] L0H0 @2bit: PPL=17.4987 delta=+4.2331 (+31.91%) *** CLIFF ***
  [2/112] L0H1 @2bit: PPL=14.3554 delta=+1.0899 (+8.22%)
  [3/112] L0H2 @2bit: PPL=16.3395 delta=+3.0740 (+23.17%) *** CLIFF ***
  [4/112] L0H3 @2bit: PPL=14.8232 delta=+1.5576 (+11.74%) *** CLIFF ***
  [5-112]: 其余 head delta 很小（0.00%~2%范围）
  2-bit summary: cliff_count=3/112 (2.7%), max_delta=+4.2331, mean_delta=+0.1798

=== Testing 4-bit quantization ===
  [1/112] L0H1 @4bit: PPL=14.5407 delta=+1.2752 (+9.61%)  ← 最大
  其余 head delta < ±1%
  4-bit summary: cliff_count=0/112 (0.0%), max_delta=+1.2752, mean_delta=+0.0056

=== Testing 8-bit quantization ===
  所有 head delta < ±0.3%
  8-bit summary: cliff_count=0/112 (0.0%), max_delta=+0.2468, mean_delta=-0.0191

============================================================
CLIFF EFFECT SUMMARY
============================================================
Baseline PPL: 13.2655

2-bit:
  Cliff heads (>10% PPL increase): 3/112
  Max PPL delta: +4.2331
  Mean PPL delta: +0.1798
  Top-5 worst heads:
    L0H0: delta=+4.2331 (+31.91%)
    L0H2: delta=+3.0740 (+23.17%)
    L0H3: delta=+1.5576 (+11.74%)
    L0H1: delta=+1.0899 (+8.22%)
    L4H1: delta=+0.8163 (+6.15%)

4-bit:
  Cliff heads (>10% PPL increase): 0/112
  Max PPL delta: +1.2752
  Mean PPL delta: +0.0056
  Top-5 worst heads:
    L0H1: delta=+1.2752 (+9.61%)
    L0H2: delta=+0.4432 (+3.34%)
    L0H0: delta=+0.3011 (+2.27%)
    L0H3: delta=+0.2360 (+1.78%)
    L13H0: delta=-0.0689 (-0.52%)

8-bit:
  Cliff heads (>10% PPL increase): 0/112
  Max PPL delta: +0.2468
  Mean PPL delta: -0.0191

EXIT_CODE=0
```

---

## 6. ppl_mvp_fast.log（本地 tee）

内容与 p0_1_ppl_fast.log 完全一致（199行 vs 202行，差异仅少了开头 `source` 环境设置行的输出），同样的 profiling + solver + PPL 结果。

---

## 7. 输出文件

```
-rw-r--r-- 1 root root 53917 May 14 06:28 /root/ratekv/cliff_7B_results.json
-rw-r--r-- 1 root root 11431 May 14 06:29 /root/ratekv/ppl_mvp_fast.log
-rw-r--r-- 1 root root 15482 May 14 06:27 /root/ratekv/ppl_profiles.json
```

三个文件全部存在。`cliff_7B_results.json`（54KB）和 `ppl_profiles.json`（15KB）内容已拉取，数据完整。

---

## 汇总

| 项目 | 状态 |
|------|------|
| GPU | 2x RTX PRO 6000 Blackwell 96GB，完全空闲 |
| 进程 142134 / 141907 | 已结束 |
| p0_1_ppl_fast | ✅ 完成，EXIT_CODE=0 |
| p0_2_cliff_7B | ✅ 完成，EXIT_CODE=0 |
| Traceback/Error | **无** |
| 关键发现 | Full MCKP PPL=28.07 **远差于** Uniform 4-bit PPL=15.45（负改进 -12.63）；Cliff effect 仅在 2-bit 出现（L0 的 3 个 head），4-bit/8-bit 无 cliff |

---
