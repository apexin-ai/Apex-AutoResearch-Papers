# infra diagnose crash

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose-crash_20260514T083835_result.json`
- **Structured JSON:** [`f0c162a5ed44a2ee8fe8.json`](../../sessions/f0/f0c162a5ed44a2ee8fe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：进程还活着，没有消失

**`pgrep -a iterative_train` 返回空是因为进程名显示为 `python`，不是 `iterative_train`。**

nvidia-smi 确认两个进程正在运行：

| 实验 | 原始 PID | 实际 PID | GPU | 显存占用 | GPU 利用率 |
|------|---------|---------|-----|---------|-----------|
| rep_42 | 13678 | 13683 | cuda:0 | 14380MiB / 97887MiB | 44% |
| rep_43 | 13758 | 13763 | cuda:1 | 14380MiB / 97887MiB | 52% |

PID 差异（13678→13683, 13758→13763）说明原始启动脚本 fork 出了 python 子进程。

### 当前进度

两个实验都完成了 gen_0 和 gen_1，**正在跑 gen_2/10（合成数据生成阶段）**：
- `gen_2/` 目录已创建但为空，日志末尾均显示 `Generation 2/10 → Generating synthetic data …`

### Gen 1 指标

| 指标 | rep_42 | rep_43 |
|------|--------|--------|
| perplexity | 55.95 | 55.45 |
| entropy | 1.9085 | 1.9092 |
| effective_rank | 79.6 | 78.4 |
| mauve | 0.0323 | 0.0299 |
| ece | 0.204 | 0.205 |
| distinct_2 | 0.514 | 0.518 |

### 注意事项

1. **MAUVE 极低（~0.03）**：FAISS 发出警告 `clustering 3128 points to 156 centroids: please provide at least 6084 training points`，数据点不足导致 MAUVE 计算不可靠。
2. **日志被淹没**：海量 `right-padding was detected` 警告（>32万字符），建议代码中加 `transformers.logging.set_verbosity_error()` 抑制。
3. **系统健康**：GPU 温度正常（39°C / 41°C），磁盘 8.8G/250G（4%），无异常。

---
