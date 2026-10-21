# ops scp and eval cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-and-eval-cqa1_20260518T203927_result.json`
- **Structured JSON:** [`b906a171924030b3fb4f.json`](../../sessions/b9/b906a171924030b3fb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部传输完成，eval 运行正常。

## 产出报告

### cqa1 环境状态
- **基础模型**: Qwen2.5-7B 已从 hf-mirror.com 下载完成 (15GB, 4 shards)，路径 `/root/autodl-tmp/models/Qwen2.5-7B/`
- **Eval 脚本**: `/root/contamcal-irt-calibration/exp001/evaluate.py` 存在，依赖全部就绪 (peft 0.19, transformers 4.57, torch 2.11, lm_eval 0.4.11)
- **磁盘**: 169GB 总量，~37GB 可用
- **GPU**: RTX 4090 D 24GB 单卡，eval 中使用 16.2GB/24.6GB

### 服务器间连通性
- cqa1 ↔ westd 无法直接互 SSH（SSH key 未配置）
- **解决方案**: 在 cqa1 生成 ed25519 密钥，添加到 westd 的 authorized_keys，通过 `ssh -p 29999 root@connect.westd.seetacloud.com` 建立 SCP 通道

### 传输结果
- **12/12 adapter 全部传输成功**:
  - 10 × Qwen2.5-7B (d000/d005/d025/d050/d100 × s42/s123)，各 165MB
  - 2 × Qwen2.5-14B (d000_s42, d005_s42)，各 274MB
- **tokenizer 兼容性修复**: 所有 10 个 7B adapter 的 `tokenizer_config.json` 移除了 `extra_special_tokens`（list 格式与 transformers 4.57 不兼容）

### Eval 启动状态
- **PID**: 153750 (python evaluate.py)
- **脚本**: `/root/contamcal-irt-calibration/exp001/run_aligned_eval_7B.sh both`
- **CUDA_VISIBLE_DEVICES=0**
- **模式**: original + paraphrase（每个 adapter 跑两轮）
- **Benchmarks**: mmlu, gsm8k, arc_challenge, humaneval
- **当前进度**: d000_s42 的 MMLU original 评估中，~11 it/s
- **日志**: `/root/autodl-tmp/exp001/logs/eval_7b_batch.log`
- **预计总时长**: 10 个 adapter × 2 模式 × ~15 min/run ≈ 5 小时

---
