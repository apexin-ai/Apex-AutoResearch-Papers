# train dpo 003 fixb

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_dpo-003-fixb_20260512T182135_result.json`
- **Structured JSON:** [`9ec2970ce10970ae7470.json`](../../sessions/9e/9ec2970ce10970ae7470.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 48 已过。Metrics 因 Python nohup 缓冲延迟只显示到 ~step 33，但进度条正常推进。可以给出报告了。

---

## dpo-003 启动报告

### 1. Tokenization 验证
- **test_v3_tokenization.py**: 0/3126 mismatch (chosen + rejected), **PASS**
- EOS 处理正确：0/1563 缺失
- train_dpo_v3.py 内置检查："Tokenization alignment check PASSED (first example)"

### 2. 训练启动
| 项目 | 值 |
|------|-----|
| PID | 299960 |
| GPU | cuda:2 (19391/24564 MiB) |
| batch_size | 1 (OOM with 4, grad_accum=4, effective=4) |
| total_steps | 1173 |
| speed | ~4.3 s/step |
| wandb | disabled (未登录) |

### 3. 前 ~50 steps 早期指标（step 1-33 有 metrics 输出，step 48 进度条确认）

| 指标 | 观测值 | 目标 | 状态 |
|------|--------|------|------|
| mismatch 警告 | 0 | 0 | **PASS** |
| loss | 0.669-0.718 (avg ~0.693) | < 0.68 | **尚早** |
| accuracy | 0.0-1.0 (avg ~0.52) | > 0.55 | **尚早** |

**注意**：warmup_ratio=0.1 → warmup 前 117 steps。当前 lr 仅 ~1.3e-7（峰值 5e-7 的 26%）。loss/accuracy 在 warmup 期间接近随机水平 (ln2=0.693) 是正常的。真正的信号要到 warmup 结束（~step 120）后才会显现。

关键是 **mismatch=0 已确认**——这正是 v3 要修复的核心问题。

### 4. 预计训练时长
- 1173 steps × 4.3 s/step ≈ **84 分钟 (~1h 24min)**
- 进度条 ETA: ~1h 17min（与估算一致）
- 预计完成时间：~03:50 UTC

### 5. 注册状态
- dpo-003 已注册 registry，status=RUNNING，parent=dpo-002
- cron 监控已设置（每 8 分钟检查）
- cuda:3 上 dpo-002 未受影响（23201 MiB 稳定）

---
