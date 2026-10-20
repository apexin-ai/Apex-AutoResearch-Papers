# research baseline code survey

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline-code-survey_20260512T142059_result.json`
- **Structured JSON:** [`3b64ef241881b9b0b47c.json`](../../sessions/3b/3b64ef241881b9b0b47c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。产出已写入 `artifacts/baseline_code_survey.md` 并注册。核心结论：

**kvpress**：确认支持 Qwen2ForCausalLM，`pip install kvpress` 即可获得 H2O、SnapKV、TOVA、StreamingLLM 等 30+ 种 press，API 简洁（pipeline 一行调用）。Python 3.10 + PyTorch 2.x + CUDA 12.x 无兼容性问题。

**R-KV**：[Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)，NeurIPS 2025，显式支持 DeepSeek-R1-Distill-Qwen-14B。核心瓶颈是 redundancy scoring 的 **O(B²)** 复杂度——正好是 CARC 要替代的。支持 HuggingFace/vLLM/SGLang 多后端。

**推荐 baseline 选择**：
- **Primary**: H2O（kvpress 内置）+ R-KV（独立 repo）
- **Secondary**: StreamingLLM（凸显 content-aware 优势）、SnapKV、FASA（[ICLR 2026 最新竞品](https://github.com/AMAP-ML/FASA-ICLR2026)）

**CARC 唯一定位**：12 个竞品中唯一同时满足 O(1) + content-aware + recurrence-aware 的方法。

---
