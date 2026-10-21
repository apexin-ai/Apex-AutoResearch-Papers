# diagnose eval obs only object norm03 seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm03-seed47_20260517T115219_result.json`
- **Structured JSON:** [`940cecd9da135a90ccdd.json`](../../sessions/94/940cecd9da135a90ccdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是结论：

---

## 诊断结果

### 根本原因（两个实验共同）

**`evaluate.py` 没有 W&B 集成，也不写 sentinel 文件。** 监控系统检查三个信号：运行中进程、sentinel 文件、W&B 活动。evaluate.py 只写 JSON 结果文件然后 `sys.exit(0)` 退出。进程正常结束后，监控找不到任何存活信号，连续检查 5 次后自动判定失败。

- `wandb/` 目录完全为空（0 文件）
- 项目中无任何 sentinel 文件
- `evaluate.py` 中无 `wandb` import，无 sentinel 写入逻辑

---

### 实验 1: eval-perdof-object-norm03-seed44-r2

**状态：实际已完成，误报失败。**

- JSON 结果文件已存在：`eval_object_perdof_norm03_seed44.json`（创建于 12:40）
- 结果：overall_success_rate = 0.04（10 tasks × 10 rollouts）
- 无 .log 文件（可能启动时未指定 tee/redirect，或被覆盖）
- 无运行中进程（正常退出）
- 监控看到"进程不存在 + 无 sentinel + 无 W&B" → 判定失败

**结论：假阳性。实验正常完成并输出了结果。**

---

### 实验 2: eval-obs-only-object-norm03-seed47

**状态：当前已被重新启动，正在运行中。**

- PID 617632，GPU 1（CUDA_VISIBLE_DEVICES=1），19:39 启动，state=R (running)
- 占用 ~5.6GB / 24GB VRAM，CPU 155%
- 日志停在 "10 tasks loaded."（16 行），这是正常的——参照同类实验 norm01 seed45，每个 rollout 约 8 分钟，首次进度输出（5 rollouts 后）预计约 40 分钟后出现
- 之前的尝试被监控判定失败（同样因为无 sentinel/W&B），然后被重新启动

**结论：当前运行正常，预计 10-12 小时内完成。之前的"失败"同样是假阳性。**

---

### 环境状态

| 指标 | 状态 |
|------|------|
| GPU | 4× RTX 4090，正常，无 ECC 错误 |
| 磁盘 | root 34%（20G 空闲），data 83%（1.3T 空闲）|
| OOM | dmesg 不可访问（容器限制），但当前内存充裕 |
| 当前 GPU 占用 | GPU0: seed45 norm01, GPU1: seed47 norm03, GPU2: seed46 norm01, GPU3: seed47 norm01 |

---

### 是否可以重跑

- **perdof-norm03-seed44-r2**：不需要重跑，结果已在 `eval_object_perdof_norm03_seed44.json`
- **obs-only-norm03-seed47**：不需要重跑，PID 617632 当前正在运行

### 修复建议

在 `evaluate.py` 末尾（`evaluate(args)` 之后、`sys.exit(0)` 之前）加 sentinel 文件写入，让监控系统能检测到完成状态。类似：

```python
sentinel = Path(args.output_file).with_suffix('.done')
sentinel.write_text('ok')
```

或者在 job 提交时，将 evaluate.py 的调用包装为 `python evaluate.py ... && touch &lt;sentinel_path>`。

---
