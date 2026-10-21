# ops prep qwen7b s0 scp eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-qwen7b-s0-scp-eval_20260520T182835_result.json`
- **Structured JSON:** [`1c48cc99685b08307ede.json`](../../sessions/1c/1c48cc99685b08307ede.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本语法验证通过。

**已准备好的产出：**

| 脚本 | 位置 | 功能 |
|------|------|------|
| `scp_qwen7b_s0_to_westd.sh` | cqa1: `/root/contamcal-irt-calibration/scripts/` | 从 cqa1 直接 scp 5 个 dosage 的 adapter 到 westd（排除 checkpoint-3125，每个 ~170MB） |
| `eval_qwen7b_s0_mmlu.sh` | westd: `/root/contamcal-irt-calibration/scripts/` | cuda:2 上跑 5 个 dosage 的 MMLU 5-shot eval |

**SSH 直连已配置**：在 cqa1 的 `~/.ssh/config` 中添加了 `westd-29999` 条目（cqa1 的公钥已在 westd authorized_keys 中），测试通过。

**训练完成后执行序列：**

1. **C001/C002**: 在 westd cuda:2 上 `nvidia-smi` 确认空闲
2. **cqa1 上执行传输**：`bash /root/contamcal-irt-calibration/scripts/scp_qwen7b_s0_to_westd.sh`（~850MB，预计几分钟）
3. **westd 上启动 eval**：`CUDA_VISIBLE_DEVICES=2 nohup bash /root/contamcal-irt-calibration/scripts/eval_qwen7b_s0_mmlu.sh > /tmp/eval_qwen7b_s0_mmlu.log 2>&1 &`

**合规检查：**
- C006: 两个脚本都验证 `lora_alpha=32`
- C009: eval 脚本验证 evaluate.py md5 = `17673bf373f00f83ccc41fc1d355a4cd`（westd 当前版本，与 s123 结果一致）
- C004: `CUDA_VISIBLE_DEVICES=2` 显式设置

---
