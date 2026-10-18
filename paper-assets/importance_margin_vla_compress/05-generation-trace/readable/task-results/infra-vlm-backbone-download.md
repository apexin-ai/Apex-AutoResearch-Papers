# infra vlm backbone download

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_vlm-backbone-download_20260515T130217_result.json`
- **Structured JSON:** [`eaa6454f1b69b8010fbe.json`](../../sessions/ea/eaa6454f1b69b8010fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载和验证全部完成。

## 产出报告

1. **下载状态**: 成功
2. **下载耗时**: ~127 秒（ModelScope 阶段），总耗时约 12 分钟（含 HF 尝试和切换）
3. **验证结果**: 
   - model_type: `smolvlm`
   - 参数量: 507.5M，489 个 tensor
   - config 和 safetensors 均可正常加载
4. **使用了备选方案**: 
   - HuggingFace 直连和 hf-mirror.com 均因 xet-bridge 超时/极慢失败
   - 最终通过 **ModelScope** 国内 CDN 下载 model.safetensors（18 MB/s），其余小文件通过 hf-mirror 完成
   - model.safetensors 通过 symlink 从 ModelScope cache 链接到 HF cache snapshot 目录

---
