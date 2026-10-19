# setup download accelerate

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_download_accelerate_20260516T101018_result.json`
- **Structured JSON:** [`888592435e89bc021c42.json`](../../sessions/88/888592435e89bc021c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成，文件验证通过。

---

## 结果汇总

| 方案 | 状态 | 速度 |
|------|------|------|
| 方案1: hf_transfer | **失败** — RuntimeError（XET 协议兼容问题） | N/A |
| 方案2: HF 镜像 huggingface-cli | 启动中但被 kill（aria2 已完成） | ~未测到 |
| **方案3: aria2c 16线程** | **成功** | **~1.7 MB/s → 约 1.5 分钟完成 6.5GB** |
| 旧 wget（已 kill） | 太慢 | ~250 KB/s |

**最终使用方案：aria2c 16线程从 hf-mirror.com 下载**

### 文件确认

```
/root/autodl-tmp/checkpoints/pi0_libero/
├── config.json          (1.7K)
├── model.safetensors    (6.6G, 7011549448 bytes ✓)
├── policy_postprocessor.json (448B)
├── policy_preprocessor.json  (1012B)
└── README.md            (3.9K)
```

- safetensors 文件可正常加载，包含 783 个 tensor
- 所有旧的慢下载进程已终止

---
