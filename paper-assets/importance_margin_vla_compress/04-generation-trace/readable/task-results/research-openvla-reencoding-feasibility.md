# research openvla reencoding feasibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla_reencoding_feasibility_20260519T161811_result.json`
- **Structured JSON:** [`31fc6e0be57ba4c98aae.json`](../../sessions/31/31fc6e0be57ba4c98aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告完成，已写入 `artifacts/openvla_reencoding_feasibility.md` 并注册到 manifest。

**核心结论**：

- **可行性 3.5/5** — 技术上可行，但工程和计算投入显著
- **维度差异**: SmolVLA 128 tokens × 960 dim → OpenVLA 256 tokens × 4096 dim，VTC 参数从 ~22M 膨胀到 ~403M
- **最大挑战**: OpenVLA 没有独立 action expert，LLM 直接预测离散 action tokens，必须搭配 LoRA 才能让 LLM 适配压缩后的 token（SmolVLA 可以纯冻结 LLM 因为有独立 expert）
- **代码量**: ~590 行新代码（3 个新文件），VisionTokenCompressor 核心模块可直接复用（维度作为参数传入）
- **计算需求**: 需要 A100 80GB（当前 4090 24GB 不够），预估训练 4-8 天
- **竞品**: Compressor-VLA 已验证类似方案可行（512→160 tokens, 97.1% on LIBERO），是最直接的参考和竞品

---
