# ssh 14b acceleration eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-acceleration-eval_20260522T211407_result.json`
- **Structured JSON:** [`2b56a4716f9aa42145fc.json`](../../sessions/2b/2b56a4716f9aa42145fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕，汇总如下：

---

## CLS 14B 加速评估报告

### 1. CLS 14B 数据：**用了错误的 70K repo-level 数据**

日志确认：
- `Train file: data/swebench_full/swebench_train.jsonl`
- `Loaded train=70748` → kept 68093 → **6384 steps**
- 速度 ~14s/step → 预计 **24.8h**

根因在 `train_unified.py:306-308`，CLS 模式默认优先加载 `swebench_full/`：
```python
repo_path = os.path.join(args.data_dir, "swebench_full", "swebench_train.jsonl")
train_path = repo_path if os.path.exists(repo_path) else func_path
```
启动命令没传 `--train_file train.jsonl`，自动选了 70K。

### 2. CWM 14B 数据：**正确（15K function-level）**
- `Train file: data/cwm_train.jsonl`
- `Loaded train=15290` → **1434 steps** at ~9.8s/step → 预计 **3.9h**
- 当前 step 294/1434 (20%)，预计还剩 ~3.1h

### 3. 8B CLS function-level：**用的 15K**
- `model-size-scaling-cls8b.log`: `Loaded train=15290`, 1434 steps at ~3.8s/step → ~1.5h
- 说明之前 8B 训练时 `swebench_full/` 目录可能还不存在，或者传了 `--train_file`

### 4. 当前进度
- CLS 14B: step 155/6384 (**2%**)，已跑 ~36 min，**应该立即 kill 重启**
- CWM 14B: step 294/1434 (20%)，正常运行中

### 5. GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 87% | 15.3/32.6 GB | CLS 14B |
| 1 | 0% | 0/32.6 GB | **空闲** |
| 2 | 97% | 14.4/32.6 GB | CWM 14B |
| 3 | 0% | 0/32.6 GB | **空闲** |

### 6. DDP 可行性
- accelerate: **1.13.0** ✓ (需 ≥0.27)
- bitsandbytes: **0.49.2** ✓ (需 ≥0.41)
- 版本满足 QLoRA+DDP 要求

### 7. 推荐方案

**方案 A（强烈推荐）：Kill → 用 15K 数据重启**
- 命令加 `--train_file train.jsonl --val_file val.jsonl`
- 步数 6384 → **1434**（降 4.5x）
- 时间 14s/step × 1434 = **5.6h**
- 仅浪费已跑 36 min，完全在 DDL 内

**方案 B（可选叠加）：DDP 双卡 GPU 0+1**
- 理论 1.5-1.7x 加速 → **~3.3h**
- 但 QLoRA+DDP 有兼容性风险，需测试
- 如果 5.6h 可接受，没必要冒这个险

**方案 C：增大 batch_size**
- GPU 显存还剩 ~17GB，理论可以 bs 2→4
- 但需要 Director 批准参数变更

**结论**：最优路径是方案 A — 立即 kill CLS 14B，加 `--train_file train.jsonl --val_file val.jsonl` 重启。5.6h 完成，无风险。是否立即执行？

---
