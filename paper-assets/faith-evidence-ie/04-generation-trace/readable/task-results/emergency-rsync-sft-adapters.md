# emergency rsync sft adapters

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_rsync-sft-adapters_20260520T162342_result.json`
- **Structured JSON:** [`f948793297413459f667.json`](../../sessions/f9/f948793297413459f667.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇报：

**1. RSFT 是否依赖 SFT adapter：是，nested LoRA。**
- `inference.py:90-92`：先用 `PeftModel.from_pretrained()` 加载 SFT adapter 并 merge 到 base model，然后再加载 RSFT adapter
- `inference.py:418-424`：代码会检测如果是 RSFT adapter 但没传 `--sft_adapter` 则报错，明确说 "RSFT/DPO/GRPO adapters are trained on SFT-merged model and MUST be evaluated with --sft_adapter"
- 结论：eval 时 `--sft_adapter` 参数必须指向对应的 SFT adapter 目录

**2. rsync 传输状态：**
- 4 个并行 rsync 已启动（PID 37381-37384），全部活跃
- 当前进度（~2 分钟后）：每个 50-56MB / 4.6GB
- 速度约 ~30MB/min/stream（5 个 rsync 共享跨区带宽）
- 预计总时间：**2-3 小时**（远超预期的 5-15 分钟，因为跨 AutoDL 区域带宽有限且 5 路并行竞争）
- 日志：`/tmp/rsync_sft_{bf16,s43,s44,noevi}.log`

**3. 尚未完成。** rsync 在后台 nohup 运行，不会因 SSH 断开而中断。可稍后用以下命令验证：
```bash
du -sh /root/autodl-tmp/sft_output_qwen3_8b_*/
ls /root/autodl-tmp/sft_output_qwen3_8b_*/adapter_model.safetensors
```

需要我继续定期轮询进度直到完成吗？

---
