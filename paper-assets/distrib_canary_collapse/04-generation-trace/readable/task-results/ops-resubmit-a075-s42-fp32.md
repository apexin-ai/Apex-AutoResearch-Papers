# ops resubmit a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit_a075_s42_fp32_20260519T095659_result.json`
- **Structured JSON:** [`8dce4b8b4b72aee243ea.json`](../../sessions/8d/8dce4b8b4b72aee243ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重启成功。

**崩溃原因**：HuggingFace 域名不可达（`[Errno 101] Network is unreachable`，ping 100% packet loss），模型默认缓存目录 (`~/.cache/huggingface`) 无 pythia-410m，导致加载失败。

**修复**：设置 `HF_HOME=/root/autodl-tmp/.hf_cache` + `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1`，使用项目目录下已有的完整缓存。

**重启状态**：
- **PID**: 121667
- **GPU 5**: 6516MiB / 97887MiB, 79% utilization
- Generation 0 (baseline) 已开始训练
- 无 right-padding 警告

---
