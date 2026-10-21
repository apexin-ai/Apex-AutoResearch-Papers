# code sft s123 sweep submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715_result.json`
- **Structured JSON:** [`c6743d7a52ab050b7e81.json`](../../sessions/c6/c6743d7a52ab050b7e81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 job 正常启动，模型权重加载中。注意 cuda:2 的 Qwen-7B s123 已跳过（全部 5 个 dosage 已存在），直接在加载 OLMo-2。

## 最终报告

### GPU 清理
- 初始状态：4 张 GPU 全部空闲，无进程需要 kill

### 模型 snapshot 路径
| 模型 | 路径 |
|------|------|
| Phi-4 | `/root/autodl-tmp/models/phi-4` |
| Qwen2.5-14B | `/root/autodl-tmp/models/Qwen2.5-14B` |
| Qwen2.5-7B | `/root/autodl-tmp/models/Qwen2.5-7B` |
| Gemma-2-9B | `/root/autodl-tmp/models/gemma-2-9b` |
| OLMo-2-7B | `/root/autodl-tmp/models/OLMo-2-1124-7B` |

（注：模型存储在 `/root/autodl-tmp/models/` 而非 HF cache snapshots 目录；HF cache 只有 refs 没有完整 snapshots）

### 脚本修正说明
任务模板的 CLI 参数与实际 `train_sft.py` 不匹配，已按照已有 s42 训练配置（`train_config.json`）修正：
- `--model_name_or_path` → `--model-name`
- `--dosage` → `--data-path /root/autodl-tmp/sft_data/sft_dosage_{d}.jsonl`
- `--learning_rate 5e-5` → `--lr 5e-5`
- `--bf16` / `--mode augment` → 已移除（不存在的参数）
- batch_size/grad_accum 按模型大小匹配：14B/9B用 bs=1/ga=16，7B用 bs=2/ga=8

### submit_training_job 结果

| Job | GPU | PID | tmux session |
|-----|-----|-----|-------------|
| sft_phi4_s123_sweep | cuda:0 | 179569 | sft_phi4_s123_sweep |
| sft_qwen14b_s123_sweep | cuda:1 | 179720 | sft_qwen14b_s123_sweep |
| sft_qwen7b_olmo2_s123_sweep | cuda:2 | 179905 | sft_qwen7b_olmo2_s123_sweep |
| sft_gemma2_s123_sweep | cuda:3 | 180155 | sft_gemma2_s123_sweep |

### 验证
- 4 个 tmux session 全部运行中
- 日志确认模型正在加载（phi-4 和 qwen14b 用 safetensors 秒加载，olmo2 和 gemma2 逐 shard 加载中）
- **Qwen-7B s123 已自动跳过**（5 个 dosage 全部已存在），cuda:2 直接开始训练 OLMo-2

---
