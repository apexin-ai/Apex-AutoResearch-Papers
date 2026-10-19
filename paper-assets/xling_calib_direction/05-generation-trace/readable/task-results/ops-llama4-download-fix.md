# ops llama4 download fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama4-download-fix_20260521T081649_result.json`
- **Structured JSON:** [`641ab105bbd40a449c79.json`](../../sessions/64/641ab105bbd40a449c79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

1. **ModelScope 可用性**: 有。`RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16` 在 ModelScope 上存在。

2. **采取方案**: 
   - 已 kill HF 下载进程 (PID 67791)
   - 已启动 ModelScope 下载 (PID 69801)，14 个 shard（每个 ~4.6GB，总计 ~65GB），7-8 个并行下载中
   - 当前单 shard 速度 ~0.75-1.4 MB/s，合计吞吐 ~7 MB/s

3. **ETA 预估**: ~65GB / ~7 MB/s ≈ **2.5-3 小时**。速度不算快但稳定在传输，不像 HF 反复超时。磁盘上已有 48GB（之前 HF 下载的部分文件），空间需注意。

监控命令：
```bash
tail -5 /tmp/llama4_modelscope.log
ps -p 69801 -o pid,etime=
du -sh /root/autodl-tmp/models/Llama4-Scout-W4A16/
```

---
