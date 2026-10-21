# westd-34887 实验状态检查

**检查时间**: 2026-05-18 05:57 UTC

---

## 1. qwen14b_bce30_s42_eval

| 项目 | 状态 |
|------|------|
| **状态** | 还在跑 |
| **进程是否存在** | 是 (PID 59122, STAT=Ss+, elapsed 5:09:13) |
| **GPU 是否空闲** | 否 (GPU 0: 93989MiB/97887MiB, 77% util, 278W) |
| **当前进度** | GSM8K generate_until 86% (1137/1319), 14.53s/it, ETA ~44min |
| **错误信息** | 无 |

### 已完成指标
- **WikiText-2 PPL**: 8.7634
- **ARC-c, WinoGrande, MMLU, GSM8K**: 尚未输出（benchmark_eval.py 在所有 task 跑完后才写 results.json）

### 配置
- Model: `/root/autodl-tmp/models/qwen2.5-14b/`
- Checkpoint: `checkpoints/qwen14b_bce30_s42/predictor_bce.pt`
- Sparsity: teal_global, target=0.3
- Model-level sparsity 实际达到: 0.300

### Per-layer sparsity 分配 (TEAL-predictor)
```
Layer 0: 0.363, Layer 1: 0.917, Layer 2: 0.774, Layer 3: 0.629, Layer 4: 0.484
Layer 5: 0.457, Layer 6: 0.500, Layer 7: 0.523, Layer 8: 0.410, Layer 9: 0.168
Layer 10: 0.180, Layer 11: 0.125, Layer 12: 0.082, Layer 13: 0.113, Layer 14: 0.078
Layer 15: 0.105, Layer 16: 0.113, Layer 17: 0.094, Layer 18: 0.113, Layer 19: 0.117
Layer 20: 0.141, Layer 21: 0.133, Layer 22: 0.141, Layer 23: 0.168, Layer 24: 0.125
Layer 25: 0.137, Layer 26: 0.148, Layer 27: 0.172, Layer 28: 0.230, Layer 29: 0.227
Layer 30: 0.207, Layer 31: 0.203, Layer 32: 0.180, Layer 33: 0.238, Layer 34: 0.258
Layer 35: 0.270, Layer 36: 0.344, Layer 37: 0.324, Layer 38: 0.305, Layer 39: 0.340
Layer 40: 0.332, Layer 41: 0.336, Layer 42: 0.340, Layer 43: 0.359, Layer 44: 0.426
Layer 45: 0.492, Layer 46: 0.654, Layer 47: 0.808
```

### Log 最后 5 行
```
Running generate_until requests:  84%|████████▍ | 1105/1319 [4:33:57<52:17, 14.66s/it]
Running generate_until requests:  84%|████████▍ | 1113/1319 [4:35:53<50:12, 14.62s/it]
Running generate_until requests:  85%|████████▍ | 1121/1319 [4:37:50<48:09, 14.59s/it]
Running generate_until requests:  86%|████████▌ | 1129/1319 [4:39:46<46:06, 14.56s/it]
Running generate_until requests:  86%|████████▌ | 1137/1319 [4:41:41<44:05, 14.53s/it]
```

---

## 2. bce_isocompute_v3_s123_eval

| 项目 | 状态 |
|------|------|
| **状态** | 还在跑 |
| **进程是否存在** | 是 (PID 74858, STAT=Rl, elapsed 19:12+) |
| **GPU 是否空闲** | 否 (GPU 1: 66997MiB/97887MiB, 64% util, 237W) |
| **当前进度** | GSM8K generate_until 16% (209/1319), 1.14s/it, ETA ~21min |
| **错误信息** | 无 |

### 已完成指标
- **WikiText-2 PPL**: 28.0627
- **ARC-c, WinoGrande, MMLU, GSM8K**: 尚未输出（benchmark_eval.py 在所有 task 跑完后才写 results.json）

### 配置
- Model: `/root/autodl-tmp/models/llama-3.1-8b`
- Checkpoint: `checkpoints/bce_isocompute_v3_s123/predictor_bce.pt`
- Sparsity: teal_global, target=0.5
- Log 路径: `/root/distill_sparse_swiglu/logs/bce_isocompute_v3_s123_eval.log`

### Log 最后 5 行
```
Running generate_until requests:  14%|█▍        | 185/1319 [03:40<21:29,  1.14s/it]
Running generate_until requests:  15%|█▍        | 193/1319 [03:50<21:21,  1.14s/it]
Running generate_until requests:  15%|█▌        | 201/1319 [03:59<21:16,  1.14s/it]
Running generate_until requests:  16%|█▌        | 209/1319 [04:08<21:05,  1.14s/it]
```

---

## GPU 状态总览

```
GPU 0: NVIDIA RTX PRO 6000 Black | 93989MiB/97887MiB | 77% | PID 59127 (qwen14b eval)
GPU 1: NVIDIA RTX PRO 6000 Black | 66997MiB/97887MiB | 64% | PID 74858 (bce_iso_v3 eval)
```

## tmux sessions
- `qwen14b_bce30_s42_eval` (1 window, created Mon May 18 00:47:49 2026)

---

## 结论

两个实验**均正常运行中**，没有挂掉也没有错误。都处于最后一个 task (GSM8K generate_until) 阶段：
- **qwen14b**: 预计 ~44 分钟后完成 (约 06:41 UTC)
- **bce_isocompute_v3_s123**: 预计 ~21 分钟后完成 (约 06:18 UTC)

完成后 results.json 将写入 `/root/distill_sparse_swiglu/results/benchmark/{exp_id}/results.json`。
