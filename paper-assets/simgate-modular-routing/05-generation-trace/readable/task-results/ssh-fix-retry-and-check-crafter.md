# ssh fix retry and check crafter

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-retry-and-check-crafter_20260518T041530_result.json`
- **Structured JSON:** [`9346b1b0800c42286703.json`](../../sessions/93/9346b1b0800c42286703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 全部释放（0MiB），清理完成。

---

## 汇报

### 问题 1：retry-dose-response — dry-run 成功

**根因修复确认**：加 `--served-model-name Qwen2.5-7B-Instruct` 后，`/v1/models` 返回短名，API 调用无 404。

**Dry-run 结果**：3 个 task 跑通（chemistry-mix、find-animal、freeze），每个 task 的 5 次 trial 均正常完成 LLM 调用。游戏结果均为 FAIL 属于正常（max-steps=5 太少）。

**正式运行的 vLLM 启动命令**（关键修复行加粗）：
```bash
CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 /root/miniconda3/bin/python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
  --served-model-name Qwen2.5-7B-Instruct \    # ← 修复点
  --port 8000 --gpu-memory-utilization 0.9 --trust-remote-code
```

**正式实验命令**：
```bash
/root/miniconda3/bin/python run_retry_dose_response.py --n-values 1,5,10
```

---

### 问题 2：Crafter 文件位置 — 存在

`crafter_pilot/` 目录存在于 westb-14838：

```
/root/autodl-tmp/simgate-modular-routing/crafter_pilot/
├── config.py
├── episode_runner.py
├── llm_agent.py
├── text_wrapper.py
├── results/
└── __pycache__/
```

crafter 包已安装（无 `__version__` 属性但 import 成功）。Reviewer 在另一台服务器找不到可能是因为代码只在 westb-14838 上存在。

---
