# infra gemma disk cleanup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gemma-disk-cleanup_20260519T073526_result.json`
- **Structured JSON:** [`5bcbb76386132990aa46.json`](../../sessions/5b/5bcbb76386132990aa46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 成功运行！Gemma-3-27B-IT 在 cuda:3, 端口 8003 上可用。

## 任务完成报告

**磁盘清理：**
- phi-4-reasoning 删除（19G 已释放）
- gemma 缓存清理（16G .cache 内 incomplete 文件 + 3G .temp 文件）
- 总计释放：~35G

**Gemma 模型修复：**
- 原始状态：仅 5/12 shard（缺少 1,3,6,8,9,10,11）
- 下载方式：aria2c 16 连接从 ModelScope CDN 逐个下载
- 挑战：HuggingFace 直连不通（Network unreachable），hf-mirror.com 的 Xet CDN 极慢（60KB/s），ModelScope 并行下载空间不足
- 最终所有 12 个 shard 完整

**vLLM 状态：**
- 运行在 tmux session `exp062_vllm`
- GPU: cuda:3（RTX PRO 6000 Blackwell, 98GB 显存）
- 端口: 8003
- API 测试通过：`/v1/models` 返回正常

**磁盘剩余：** /root/autodl-tmp 约 5.8G 可用（250G 盘，245G 使用）

---
