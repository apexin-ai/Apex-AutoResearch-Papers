# prep para aligned eval 3B s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_para_aligned_eval_3B_s42_20260516T051734_result.json`
- **Structured JSON:** [`6c4f50df7393a2e94d63.json`](../../sessions/6c/6c4f50df7393a2e94d63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本内容和参数格式全部正确。

## 报告

| Dose | Checkpoint 路径 | lora_alpha | 状态 |
|------|----------------|-----------|------|
| d000 | `Qwen2.5-3B_d000_a32_s42/lora_adapter` (symlink → d000_s42) | 32 | OK |
| d005 | `Qwen2.5-3B_d005_s42/lora_adapter` | 32 | OK |
| d100 | `Qwen2.5-3B_d100_a32_s42_v3/lora_adapter` | 32 | OK |

- **Paraphrase 数据**：4 个 benchmark JSON 全部就位（mmlu/gsm8k/arc_challenge/humaneval）
- **Symlink**：`d000_a32_s42 → d000_s42` 已存在，无需操作
- **命令验证**：`evaluate.py --help` 确认所有参数（`--paraphrase-dir`, `--mc-format aligned`, `--adapter-path`）格式正确
- **脚本位置**：`/root/contamcal-irt-calibration/exp001/run_3B_s42_para_aligned.sh`

**使用方式**（提交时注意 C001/C002/C004）：
```bash
# 在 tmux 中运行，GPU 号根据实际空闲情况填写
bash run_3B_s42_para_aligned.sh d000 &lt;GPU_ID>
bash run_3B_s42_para_aligned.sh d005 &lt;GPU_ID>
bash run_3B_s42_para_aligned.sh d100 &lt;GPU_ID>
```

---
