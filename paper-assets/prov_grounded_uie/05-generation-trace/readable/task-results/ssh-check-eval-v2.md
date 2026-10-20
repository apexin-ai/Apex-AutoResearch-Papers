# ssh check eval v2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-v2_20260512T212443_result.json`
- **Structured JSON:** [`8a6f6de312f256280806.json`](../../sessions/8a/8a6f6de312f256280806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 进程状态：**卡死（hung）**

| 实验 | PID | 运行时间 | 状态 |
|------|-----|----------|------|
| SFT Eval (evaluate.py) | 17840 | 6h21m+ | `R` (running) 但无进展 |
| Posthoc NLI (rerank_nli.py) | 17369 | 6h22m+ | `R` (running) 但无进展 |

### 诊断证据

**零产出**：两个进程在整个生命周期内只写了 ~900 bytes（仅初始日志），结果文件不存在，进度日志从未输出第一条 `[50/985]`。

**IO 完全冻结**：在 ~10 分钟观测窗口内，两个进程的 `rchar/wchar/syscr/syscw` 完全不变，但 CPU 时间持续增长（各消耗 ~6.3h 单核 CPU）。

**模型信息**：
- Qwen3-8B (8.2B params, 16GB bf16)
- GPU: RTX PRO 6000 Blackwell × 8 (PID 17840 用 GPU 0, PID 17369 用 GPU 1)
- PyTorch 2.10.0+cu128

**根因分析**：进程在模型加载完成后（checkpoint shards 100%）、第一次 `model.generate()` 调用处卡住。可能原因：
1. **Blackwell 架构首次 CUDA 内核 JIT 编译** — PyTorch/NVRTC 需要为新架构（SM 120）编译内核，纯 CPU 操作，可能耗时数小时
2. **transformers + Qwen3 `trust_remote_code` 兼容性问题** — 很新的 PyTorch 2.10 + 很新的 GPU + 很新的 transformers 4.57.6 可能存在边缘 bug

### 建议

**kill 两个进程，然后分步排查**：
1. 先跑单样本快速测试：`python evaluate.py --model_path ./outputs/sft/merged --eval_file ./data/docred_dev.jsonl --max_eval_samples 1` 观察是否能完成
2. 如果单样本也卡死，尝试启用 flash attention（去掉 `--no_use_flash_attention`）或降低 batch_size 到 1
3. 如果是 JIT 编译问题，首次运行后内核会被缓存，后续运行应该快很多

要我 kill 这两个进程吗？

---
