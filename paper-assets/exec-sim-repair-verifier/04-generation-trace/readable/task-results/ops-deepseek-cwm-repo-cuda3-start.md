# ops deepseek cwm repo cuda3 start

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deepseek-cwm-repo-cuda3-start_20260516T064907_result.json`
- **Structured JSON:** [`6b36e1e415d2d875d93b.json`](../../sessions/6b/6b36e1e415d2d875d93b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是完整报告：

---

## 状态报告

### nvidia-smi 快照

| GPU | Util | Memory |
|-----|------|--------|
| cuda:0 | 99% | 19557/32607 MiB |
| cuda:1 | 81% | 18151/32607 MiB |
| cuda:2 | 97% | 18245/32607 MiB |
| cuda:3 | 95% | 17765/32607 MiB |

### 4 张卡运行情况

| GPU | Run Name | Task | Data | Steps | Progress | LoRA rank |
|-----|----------|------|------|-------|----------|-----------|
| cuda:0 | deepseek-cls-repo-level | cls | swebench_full (70748) | 78/6633 | 1% (~11s/step, ETA ~20h) | **16** |
| cuda:1 | deepseek-cwm-func-level | cwm | cwm_train.jsonl (15290) | ~380/1434 | 26% (~3.5s/step) | **16** |
| cuda:2 | deepseek-cls-func-level | cls | train.jsonl (15290) | ~363/1434 | 25% (~3.7s/step) | **16** |
| cuda:3 | **deepseek-cwm-func-seed123** | cwm | cwm_train.jsonl (15290) | ~302/1434 | 21% (~3.5s/step) | **16** |

**LoRA rank 确认方法**: 所有 4 个训练日志均显示 `trainable params: 16,777,216`，对应 DeepSeek-Coder-6.7B 的 4 modules × 32 layers × 2 × 16 × 4096 = 16,777,216，确认 rank=16。

### 任务 1: cuda:3 启动 deepseek-cwm-repo — **BLOCKED**

两个阻塞点：

1. **cuda:3 已被占用**: 正在运行 `deepseek-cwm-func-seed123`（seed=123, func-level CWM），进度 21%，预计还需 ~60 分钟完成。
2. **数据格式不兼容**: swebench_full 的字段是 `execution_output`，而 `get_target()` 在 CWM 模式下读取的是 `example["target"]`。需要修改 train_unified.py。

swebench_full 字段: `['code', 'error_message', 'execution_output', 'label', 'metadata', 'mutation_type', 'problem_id', 'source', 'test']`

cwm_train.jsonl 字段: `['code', 'test', 'target', 'label', 'source', 'problem_id', 'mutation_type']`

### 任务 3: cuda:0 监控 — 正常

cuda:0 正常训练中 (99% GPU util)，step 78/6633，repo-level cls 数据量大（70748 samples），每步 ~11s，预计总训练时间 ~20 小时。

---

**需要你的决定：**

1. **cuda:3**: 等 cwm-func-seed123 跑完（~1h）再启动 cwm-repo？还是 kill 掉后立即启动？
2. **train_unified.py 修复**: 我可以立刻改 `get_target()` 支持 `execution_output` 字段（向后兼容）。要现在改吗？

---
