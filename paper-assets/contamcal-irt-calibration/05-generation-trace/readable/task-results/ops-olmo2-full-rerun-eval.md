# ops olmo2 full rerun eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_olmo2-full-rerun-eval_20260521T142424_result.json`
- **Structured JSON:** [`6261b952b9a3b4c3eb6b.json`](../../sessions/62/6261b952b9a3b4c3eb6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中。MMLU d000 正在评估，速度 ~21 it/s，14042 items 预计 ~11 分钟/dosage。

**汇报：**

1. **Adapter 路径确认（5/5 ✓）：**
   - `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d000_s42/lora_adapter/`
   - `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42/lora_adapter/`
   - `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d025_s42/lora_adapter/`
   - `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42/lora_adapter/`
   - `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d100_s42/lora_adapter/`
   - 全部 lora_alpha=32 ✓（C006 通过）

2. **evaluate.py 版本确认：** 37775 bytes, md5=`17673bf373f00f83ccc41fc1d355a4cd` ✓

3. **提交命令：**
   ```
   CUDA_VISIBLE_DEVICES=3, GPU cuda:3
   bash /root/contamcal-irt-calibration/scripts/run_olmo2_rerun_eval.sh
   tmux session: eval_olmo2_s42_rerun, PID: 531623
   Log: ~/runs/contamcal-irt-calibration/eval_olmo2_s42_rerun.log
   ```

4. **预计完成时间：** MMLU ~11min × 5 + ARC ~2min × 5 ≈ 65 分钟，加上模型加载开销（首次已加载，后续每个 dosage 需重新加载）≈ **2-2.5 小时**，约 CST 00:30-01:00 完成。

---
