# prep exp003s2 and eval check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp003s2-and-eval-check_20260519T192406_result.json`
- **Structured JSON:** [`04259e2304c42d7b675e.json`](../../sessions/04/04259e2304c42d7b675e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。

```
=== Task A: scp 连通性 ===
LoRA adapter 大小: 952MB (其中 adapter_model.safetensors=118MB, global_step2000 优化器状态=820MB)
eval 只需 adapter 文件: ~120MB (adapter_config.json + adapter_model.safetensors)

28034 → 29046 直连 scp: 不可行
  - 两台服务器均无 ~/.ssh/config 配置对方
  - 28034 无 SSH 私钥, authorized_keys 为空 (0 bytes)
  - 均在 SeetaCloud NAT 后, 无法互相直连

替代方案: 通过 agent 机器中转
  1. MCP ssh_execute 在 28034 上 cat adapter 文件 → 但 118MB 太大不适合
  2. 推荐: 在 28034 上用 ssh_execute 配置 29046 的 SSH key, 再 scp
     - 29046 有 id_rsa.pub, 把它加到 28034 的 authorized_keys
     - 但两台机器均在 NAT 后, 仍需跳板机, 配置复杂
  3. 最实用: 用 agent 机器做 scp 中转 (scp 28034→local→29046)

29046 磁盘: 根分区仅 1.1G 剩余, autodl-tmp 211G 剩余
  → adapter 必须放 /root/autodl-tmp/ 下

=== Task B: exp-003-s2 脚本 ===
脚本路径: /root/contrastive_entrain_calib/training/run_exp003s2_r3only.py
与 exp-003 diff:
  - seed: 42 → 43
  - output_dir: exp003_r3only_seed1 → exp003_r3only_seed2
  其余参数完全相同
import 验证: OK
现有 exp003 checkpoints: /root/autodl-tmp/checkpoints/exp003_r3only_seed1 (无冲突)
启动命令参数: server="westd-29046", account="root",
  script_path="/root/contrastive_entrain_calib/training/run_exp003s2_r3only.py"
```

---
