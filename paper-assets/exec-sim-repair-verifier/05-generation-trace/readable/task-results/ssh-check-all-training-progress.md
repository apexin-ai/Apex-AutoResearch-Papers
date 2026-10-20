# ssh check all training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-all-training-progress_20260520T063435_result.json`
- **Structured JSON:** [`f1fb1ecfbb84faa6846d.json`](../../sessions/f1/f1fb1ecfbb84faa6846d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

```
=== GPU 状态 ===
0, NVIDIA GeForce RTX 5090, 99 %, 21255 MiB, 32607 MiB
1, NVIDIA GeForce RTX 5090, 100 %, 0 MiB, 32607 MiB
2, NVIDIA GeForce RTX 5090, 100 %, 20001 MiB, 32607 MiB
3, NVIDIA GeForce RTX 5090, 97 %, 31261 MiB, 32607 MiB

=== Compute Apps ===
886278, GPU-fc6e3c91 (GPU 0), 21246 MiB
925638, GPU-19c6fdd6 (GPU 2), 19992 MiB
886352, GPU-02eb6271 (GPU 3), 31252 MiB
```

---

## GPU 2: DeepSeek CWM s123-v2 (PID 925633)

```
进程状态: ALIVE, 运行时间 01:11:34
命令: train_unified.py --task cwm --model deepseek-coder-6.7b-instruct
      --seed 123 --output_dir checkpoints_deepseek_cwm_repo_s123_v2
      --max_seq_length 2048 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --epochs 3

checkpoint dir training.log: NO_LOG (不存在)

tmux log (deepseek-cwm-repo-s123-train-v2.log):
  训练进度: 470/12627 (3.7%)
  已运行: ~1:02:34
  速度: ~8.09s/it
  Train samples: 67343 (dropped 3405/70748), val: 1896
  LoRA targets: q_proj, k_proj, v_proj, o_proj
  Trainable params: 16,777,216 / 6,757,289,984 (0.25%)
```

---

## GPU 0: Qwen CWM s123-v4

```
日志文件: qwen3-8b-cwm-repo-s123-train-v4.log

训练进度: 816/6633 (12.3%)
已运行: ~5:18:41
速度: ~12.04s/it
刚完成一轮 val eval (9335 items, 耗时 ~19min), 已恢复训练
```

---

## GPU 3: Qwen CWM s456-v3

```
日志文件: qwen3-8b-cwm-repo-s456-train-v3.log

训练进度: 838/6633 (12.6%)
已运行: ~5:18:28
速度: ~11.92s/it
刚完成一轮 val eval (9335 items, 耗时 ~19min), 已恢复训练
```

---

## GPU 1: hung check

```
index, utilization.gpu, memory.used, temperature.gpu
1, 100 %, 0 MiB, 42°C

无 compute app 在 GPU 1 上运行。
100% 利用率 + 0 MiB 显存 + 无进程 → 异常状态。
```

---

## 引用验证结果

**VeRPO** — **真实存在**
- 标题: VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation
- arXiv ID: [2601.03525](https://arxiv.org/abs/2601.03525)
- 内容: RL框架，通过加权部分成功构建密集奖励，用于代码生成

**ExecVerify** — **真实存在**
- 标题: ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning
- arXiv ID: [2603.11226](https://arxiv.org/pdf/2603.11226)
- 作者: Lingxiao Tang et al. (浙江大学 & UCL)
- 内容: 利用执行轨迹的可验证白盒奖励进行代码执行推理的RL方法

---
