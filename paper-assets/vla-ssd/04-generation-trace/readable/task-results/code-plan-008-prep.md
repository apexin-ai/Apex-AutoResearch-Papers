# code plan 008 prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_008_prep_20260515T231944_result.json`
- **Structured JSON:** [`c3bafeae8916a305ea49.json`](../../sessions/c3/c3bafeae8916a305ea49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Everything verified. Here's the summary:

---

## 产出

### 脚本路径
- **Feature extraction**: `/root/vla-ssd/scripts/extract_features_rand_inst.py`
- **RSA comparison**: `/root/vla-ssd/scripts/rsa_instruction_control.py`

### Dry-run 验证
全部 3 种模式通过:
- `random` (seed=0): 生成 "civoq tixe mef wugi di wapon"，所有 task 用同一字符串
- `shuffled`: 每个 task 独立 word-level shuffle（如 "open the middle drawer..." → "of middle the open the drawer cabinet"）
- `wrong_task`: cyclic shift（task i 用 task i+1 的 instruction）

Output shape 正确: `(T, 33, 4096)` for both `last_preaction` and `image_mean`.

RSA 脚本验证: normal=0.4888 vs empty=0.4723 at layer 16，与已有结果一致。

### GPU 时间预估
单次 extraction (10 tasks × 50 demos): **~48 min** (基于已有 trained_libero_goal 的文件时间戳)

| 模式 | 运行次数 | 单次时间 |
|------|---------|---------|
| random (3 seeds) | 3 | 48 min × 3 = 144 min |
| shuffled | 1 | 48 min |
| wrong_task | 1 | 48 min |
| **合计** | **5** | **~240 min (4h)** |

利用 2 GPU 并行可缩短至 **~2.5h**:
- Batch 1 (gpu0 + gpu1): random_s0 + random_s1
- Batch 2 (gpu0 + gpu1): random_s2 + shuffled
- Batch 3 (gpu0): wrong_task

RSA 计算 (CPU-only): ~30s/layer × 33 layers × 7 conditions ≈ **~10 min**

### 推荐执行命令

```bash
cd /root/vla-ssd
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Batch 1: 两GPU并行
nohup python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0 > /tmp/rand_s0.log 2>&1 &
nohup python scripts/extract_features_rand_inst.py --instruction_mode random --seed 1 --gpu 1 > /tmp/rand_s1.log 2>&1 &

# Batch 2: 等 Batch 1 完成后
nohup python scripts/extract_features_rand_inst.py --instruction_mode random --seed 2 --gpu 0 > /tmp/rand_s2.log 2>&1 &
nohup python scripts/extract_features_rand_inst.py --instruction_mode shuffled --gpu 1 > /tmp/shuffled.log 2>&1 &

# Batch 3: 等 Batch 2 完成后
nohup python scripts/extract_features_rand_inst.py --instruction_mode wrong_task --gpu 0 > /tmp/wrong_task.log 2>&1 &

# RSA 分析（全部 extraction 完成后）
python scripts/rsa_instruction_control.py
python scripts/rsa_instruction_control.py --token_type image_mean
```

---
