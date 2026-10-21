# infra qwen72b verify

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen72b-verify_20260521T212121_result.json`
- **Structured JSON:** [`13f29bd120a19c5aa2ce.json`](../../sessions/13/13f29bd120a19c5aa2ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇总：

---

## 1. Qwen-72B (Qwen2.5-72B-Instruct-AWQ) — **就绪**

| 指标 | 结果 |
|------|------|
| Shards | 11/11 |
| 大小 | 39 GB |
| Temp 目录 | 空（干净） |
| 加载时间 | 101.8s（含 81s 引擎初始化 + CUDA graph 捕获 58s） |
| **Pairwise 推理** | **30/30 valid，26.5s** |
| 吞吐 | 196 tok/s input, 62 tok/s output |
| 样例输出 | winner=A, score_a=5, score_b=1/2（正确偏好直接正确答案） |
| 卸载 | OK |

## 2. Llama-70B (Llama-3.1-70B-Instruct-AWQ) — **就绪**

| 指标 | 结果 |
|------|------|
| Shards | 9/9（root 目录完整） |
| 大小 | 39 GB |
| Temp 残留 | `model-00005` 1.31GB（旧中断残留，root 版本 4.89GB 完整） |

## 3. Mistral-Large (Mistral-Large-Instruct-2407-AWQ) — **就绪**

| 指标 | 结果 |
|------|------|
| Shards | 14/14（root 目录完整） |
| 大小 | 62 GB |
| Temp 残留 | `model-00008` 1.61GB（旧中断残留，root 版本 4.85GB 完整） |

## 4. GPU 状态 — **全部空闲**

4x NVIDIA RTX PRO 6000 Blackwell (96GB each), 0 MiB used, 0% utilization.

---

**附注**：Llama 和 Mistral 的 `._____temp/` 各有一个旧下载残留文件，可以安全删除以释放 ~3GB 空间。另有一个 Qwen2.5-32B 的 ModelScope 修复下载正在后台运行（PID 26210）。

---
