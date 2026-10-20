# code gemma27b eval prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma27b_eval_prep_20260522T113711_result.json`
- **Structured JSON:** [`366ad55c7de32b3cc5fe.json`](../../sessions/36/366ad55c7de32b3cc5fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功进入生成阶段。cuda:3 使用 7.6GB / 80% 利用率，正在生成 depth 1（10000 docs, batch_size=32, 313 batches）。

---

## 汇总

### 1. Pipeline 兼容性验证 ✓
- `run_pipeline.py` 完全支持 Gemma-2-27B：`--dtype bf16`（line 647-649 明确标注 "needed for Gemma-2"）、`--skip_generation`、`--model_path`、`device_map="auto"`
- 现有 `run_gemma27b_c4.sh` 已验证两阶段模式可行

### 2. Gemma-27B 生成进度
- 数据目录：`data/exp_gemma27b_c4/`（非 `seed_gemma27b_c4_s42`）
- 当前状态：仅 `depth_0.jsonl`（5000 samples），depth_1+ 正在 cuda:0 上生成

### 3. Phase 2 命令模板 ✓
- 已写入 `/tmp/gemma27b_phase2_cmd.sh`
- 使用 Qwen scorer：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct`
- Gemma-27B Phase 1 完成后，直接 `bash /tmp/gemma27b_phase2_cmd.sh` 即可

### 4. Bootstrap CI 脚本 ✓
- `borderline_bootstrap_ci.py`：N_BOOT=10000, N_PERM=10000，按 case 硬编码
- `crossscorer_bootstrap_ci.py`：cross-scorer 专用，同样 N_BOOT=10000
- 需要为 Gemma-27B 添加对应 case 条目后才能运行

### 5. Pythia-1.4B 10K 实验 ✓ 已启动
- tmux session: `pythia14b_10k`
- 日志: `/tmp/exp_pythia14b_c4_10k.log`
- GPU: cuda:3, 7.6GB VRAM, 80% 利用率
- Phase 1 正在生成 depth 1（10000 samples × 5 depths + Phase 2 Qwen 评分）
- 预估时间：Pythia-1.4B 10K samples × 5 depths ≈ 3-4h（Phase 1），Phase 2 ≈ 1-2h

---
