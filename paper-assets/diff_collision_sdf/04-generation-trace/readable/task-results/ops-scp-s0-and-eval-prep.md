# ops scp s0 and eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_s0_and_eval_prep_20260524T113501_result.json`
- **Structured JSON:** [`8e05416a0a86a3164a52.json`](../../sessions/8e/8e05416a0a86a3164a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**1. SCP 完成 ✓**
- `s0_l005/30000/`: 7.2GB（model.safetensors 7.1G + optimizer 130M + ee_extractor 1.1M + sdf_decoder 1.6M + assets/）
- `s0_l01/30000/`: 7.2GB（同结构）
- 文件与源一致，传输方式：通过 seetacloud 代理 `scp -P 45947 connect.westd.seetacloud.com`

**2. Eval 脚本 ✓**
- 路径：`/root/colliforce-vla/scripts/run_d012_final_eval.sh`
- 语法检查通过
- Batch 1: s0_l005/s0_l01/s1_l005/s1_l01 → cuda:0-3, ports 8000-8003
- Batch 2: s2_l005/s2_l01 → cuda:0-1, ports 8000-8001

**3. 磁盘空间 ✓**
- `/root/autodl-tmp/`: 350GB 总量，140GB 已用，211GB 可用（40%）

---
