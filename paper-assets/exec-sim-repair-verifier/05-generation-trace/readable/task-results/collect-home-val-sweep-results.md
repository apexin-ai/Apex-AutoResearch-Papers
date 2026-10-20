# collect home val sweep results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_home-val-sweep-results_20260514T194656_result.json`
- **Structured JSON:** [`2b2cd450f56697f52086.json`](../../sessions/2b/2b2cd450f56697f52086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整对比表。

---

## Home 服务器全部 Eval 结果汇总

### 重要说明
- **val@2048** 的结果有 **1883 条 unparseable**（20.2%），因为 2048 seq_length 截断了大量输入。这些结果可靠性较低。
- **val@5120** 的 unparseable=0，truncated=234，数据质量好得多。
- **test** 集有 9784 条，unparseable=132。

---

### 一、CLS 4B v5 各 Checkpoint

| Checkpoint | Split | SeqLen | Accuracy | F1_macro | F1_fail | F1_pass | Unparseable |
|-----------|-------|--------|----------|----------|---------|---------|-------------|
| ckpt-600 | val | 2048 | 77.25 | 70.81 | 57.11 | 84.52 | 1883 |
| ckpt-4000 | val | 2048 | 83.32 | 70.26 | 50.56 | 89.97 | 1883 |
| ckpt-4200 | val | 2048 | 82.82 | 69.54 | 49.43 | 89.65 | 1883 |
| ckpt-4400 | val | 2048 | 83.49 | 71.63 | 53.29 | 89.97 | 1883 |
| **ckpt-4600** | **val** | **2048** | **83.63** | **71.72** | **53.36** | **90.07** | 1883 |
| ckpt-600 | test | 2048 | 76.74 | 73.74 | 64.88 | 82.61 | 132 |
| ckpt-4000 | test | 2048 | 81.51 | 72.56 | 56.90 | 88.23 | 132 |
| ckpt-4200 | test | 2048 | 80.64 | 72.10 | 56.66 | 87.54 | 132 |
| ckpt-4400 | test | 2048 | 82.11 | 73.94 | 59.34 | 88.54 | 132 |
| **ckpt-4600** | **test** | **2048** | **82.35** | **74.74** | **60.87** | **88.60** | 132 |

**v5 最优 checkpoint: ckpt-4600**（val 和 test 上均最优）

---

### 二、CLS 4B seed123 各 Checkpoint

| Checkpoint | Split | SeqLen | Accuracy | F1_macro | F1_fail | F1_pass | Unparseable |
|-----------|-------|--------|----------|----------|---------|---------|-------------|
| ckpt-200 | val | 2048 | 62.51 | 55.54 | 37.94 | 73.14 | 1883 |
| ckpt-400 | val | 2048 | 80.72 | 67.03 | 45.78 | 88.27 | 1883 |
| ckpt-600 | val | 2048 | 76.78 | 66.81 | 48.63 | 85.00 | 1883 |
| **ckpt-800** | **val** | **2048** | 81.81 | **69.14** | **49.37** | 88.91 | 1883 |
| ckpt-1000 | val | 2048 | **82.30** | 67.63 | 45.84 | **89.42** | 1883 |
| ckpt-400 | test | 2048 | 75.05 | 67.47 | 51.77 | 83.17 | 132 |
| **ckpt-600** | **test** | **2048** | **80.73** | **77.31** | **68.49** | **86.12** | 132 |
| ckpt-800 | test | 2048 | 74.27 | 66.03 | 49.31 | 82.76 | 132 |
| ckpt-1000 | test | 2048 | 73.14 | 52.10 | 20.36 | 83.85 | 132 |

**seed123 val 上 F1_macro 最优: ckpt-800** (69.14)，但 test 上 **ckpt-600 远远领先** (77.31 F1_macro)。val 和 test 选出的最优 checkpoint 不一致。

---

### 三、CLS 8B（val@5120）

| Model | Checkpoint | Split | SeqLen | Accuracy | F1_macro | F1_fail | F1_pass | Truncated |
|-------|-----------|-------|--------|----------|----------|---------|---------|-----------|
| 8B conda | ckpt-400 | val | 5120 | 80.47 | 75.84 | 65.27 | 86.42 | 234 |
| **8B** | **ckpt-3000** | **val** | **5120** | **89.50** | **84.08** | **74.78** | **93.37** | 234 |

**8B ckpt-3000 是全部结果中的最佳模型。**

---

### 四、CLS 4B v4（baseline）

| Checkpoint | Split | SeqLen | Accuracy | F1_macro | F1_fail | F1_pass | Unparseable |
|-----------|-------|--------|----------|----------|---------|---------|-------------|
| ckpt-200 | val | 2048 | 79.57 | 70.93 | 55.08 | 86.78 | 1883 |
| ckpt-200 | test | 2048 | 66.11 | 56.61 | 36.30 | 76.91 | 132 |

---

### 五、正在运行

| Eval | 进度 | Running Acc |
|------|------|-------------|
| v4 ckpt-2400 val@2048 | 5280/9335 (56.6%) | 83.8% |
| seed123 ckpt-400 val@5120 | 进行中 | ~83.8% |

---

### 关键发现

1. **val@2048 的 20% unparseable 严重扭曲了结果**——val@5120 评估更可靠。目前只有 8B 的两个 checkpoint 跑了 val@5120，4B 模型还需要补跑 val@5120 才能公平对比。
2. **8B ckpt-3000 val@5120: 89.50% acc / 84.08 F1_macro**，显著领先所有 4B 模型。
3. **4B v5 最优 checkpoint 是 ckpt-4600**，val 和 test 一致。
4. **4B seed123 的 val/test 最优 checkpoint 不一致**：val 选 ckpt-800/1000，test 选 ckpt-600。ckpt-600 在 test 上 F1_macro 77.31 表现异常好，可能是过拟合 test 或 val@2048 不够可靠。
5. seed123 ckpt-400 的 val@5120 正在跑，完成后可以更准确地判断 seed123 的最优 checkpoint。

---
