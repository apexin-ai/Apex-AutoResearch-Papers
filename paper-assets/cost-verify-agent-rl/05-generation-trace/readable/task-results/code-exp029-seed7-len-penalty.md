# code exp029 seed7 len penalty

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029_seed7_len_penalty_20260521T161605_result.json`
- **Structured JSON:** [`dff3c0ae5dc4b0b37900.json`](../../sessions/df/dff3c0ae5dc4b0b37900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交。汇报：

```
代码修改:
  文件: /root/autodl-tmp/cost-verify-agent-rl/RAGEN/ragen/trainer/agent_trainer.py
  git diff: length penalty 逻辑插入 line 1543 之后（token_level_rewards 赋值之后、compute_advantage 之前）
    - getattr(self.config, "response_length_penalty_coef", 0.0) 读取顶层配置
    - getattr(self.config, "response_length_penalty_threshold", 4096) 读取阈值
    - penalty = -coef * max(0, resp_len - threshold) / threshold，加到最后一个有效 token
  语法检查: SYNTAX OK

配置:
  文件: /root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed7_len_penalty.yaml
  关键参数: seed=999, threshold=1000, coef=0.5, total_steps=7, save_freq=5, CUDA=0,1

提交:
  PID: 495138
  tmux session: exp029_seed7_len_penalty
  log: ~/runs/cost-verify-agent-rl/exp029_seed7_len_penalty.log
```

---
