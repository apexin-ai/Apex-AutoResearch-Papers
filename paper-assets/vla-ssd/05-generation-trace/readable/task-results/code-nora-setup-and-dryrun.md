# code nora setup and dryrun

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nora_setup_and_dryrun_20260521T002441_result.json`
- **Structured JSON:** [`d23d703552a7ad6d60a7.json`](../../sessions/d2/d23d703552a7ad6d60a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个步骤完成。总结：

---

**NORA VLA 分析环境搭建完成** (westd-19183, cuda:1)

**已完成：**
1. SmolVLA 残留清理，释放 ~3GB + HF 缓存清理释放 ~6GB
2. 独立 venv 环境 (`/root/autodl-tmp/vla-ssd/envs/nora/`)，transformers=4.50.0，base env 的 4.48.3 未受影响
3. NORA checkpoint 下载完成 (7.5GB, 2 shards)
4. Qwen2.5-VL-3B-Instruct base 下载完成 (7.5GB, 2 shards)
5. 架构分析：36 层, hidden=2048, GQA 16h/2kv, 32 层 ViT 视觉编码器
6. Token layout：LIBERO 128×128 → 25 image tokens (5×5), 总 53 tokens
7. Dry-run 成功：10 timesteps, L0/L_last hidden states + attention 提取正常

**关键发现：**
- NORA 与 OpenVLA 差异显著：GQA vs MHA, 动态 vs 固定图像 tokens, M-RoPE, FAST+ 2048 action tokens
- L0 readout std=0.026 vs L_last readout std=3.699 → 深层表征 enrichment 与 OpenVLA 一致
- 需要 `AutoModelForImageTextToText` 加载，不同于 OpenVLA/TracVLA

**报告：** `artifacts/nora_analysis_report.md`

---
