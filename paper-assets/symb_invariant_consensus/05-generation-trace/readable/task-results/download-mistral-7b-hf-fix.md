# download mistral 7b hf fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_mistral-7b-hf-fix_20260516T194106_result.json`
- **Structured JSON:** [`fae98467b08432964b54.json`](../../sessions/fa/fae98467b08432964b54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载状态确认：

**状态**：正常下载中
- **PID**: 236801 (运行中)
- **当前速度**: ~1 MB/s（2 个并行流各 ~0.5 MB/s）
- **已下载**: ~325 MB / ~14.5 GB
- **预计完成**: ~4 小时后（约 UTC 07:50，DDL 前 4 小时）
- **无认证错误**: Mistral 模型不需要 token，只是速度受限速影响

**已完成**:
- 截断的 ModelScope 文件已清理
- vLLM 启动脚本已创建：`/root/symb_invariant_consensus/scripts/start_vllm_mistral_7b.sh`

**5 个文件在下载**（3 个 safetensors + tokenizer.json + 1 其他），hf_transfer 并行下载中。

下载将在后台持续运行，无需干预。如果需要后续检查进度：
```bash
du -sh /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/.cache/
tail -5 /tmp/dl_mistral_hf.log
ps -p 236801 -o pid=
```

---
