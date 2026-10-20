# setup fix downloads modelscope

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_fix_downloads_modelscope_20260521T042410_result.json`
- **Structured JSON:** [`d83d466fbe9e5cca240d.json`](../../sessions/d8/d83d466fbe9e5cca240d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 模型 | 方法 | PID | 状态 |
|------|------|-----|------|
| **NORA Spatial** | ModelScope | 529814 | 下载中，~3.5-5 MB/s，已下 397M/4.62G + 368M/2.38G |
| **Phi-3-Vision** | ModelScope | 529928 | 下载中，~5 MB/s，刚启动 |
| **OFT** | aria2c (hf-mirror) | 522184 | 接近完成，14.5G 已下，剩 2 个文件（model-00004 251M/? + action_head 289M/?）|

监控命令：
```
tail -5 /tmp/download_nora_spatial_ms.log
tail -5 /tmp/download_phi3v_ms.log
ls -lh /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10/*.aria2
```

---
