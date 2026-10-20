---
loop: 3
reason: idle_timeout
updated: '2026-05-13T05:40:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 cuda:2 和 cuda:3**（cqa1-21977），历史上 mvp-003 因用 cuda:1 被 CRITICAL kill
- **H-gate eval 必须用 merged 模型**，禁止 vLLM LoRA 动态加载（D010 确认 LoRA serving bug：completion 15% vs merged 60%）
- hgate-dpo003-merged 用 nohup 启动（非 submit_training_job），已手动注册 cron 监控 PID 688636
- eval 脚本 `eval_dpo003_merged.sh` 中 GPU_ID 无默认值，必须显式传 `GPU_ID=2` 或 `GPU_ID=3`

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977**，账户 root，工作目录 `/root/democalib`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，非 venv）
- 模型路径：
  - Base: `/root/autodl-tmp/models/Qwen2.5-7B-Instruct/`
  - DPO-003 merged: `/root/autodl-tmp/models/Qwen2.5-7B-DPO003-merged/`（15GB，4 shards）
  - Mistral: `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/`（14GB，已验证完整）
- 活跃进程（重启后需确认是否存活）：
  - hgate-dpo003-merged: 主进程 PID 688636, vLLM PID 688649 (cuda:2 port 8002) + 688650 (cuda:3 port 8003)
  - Group A PID 688675 (run 1-2), Group B PID 688676 (run 3-4)
  - cron 已注册：exp_id=hgate-dpo003-merged, interval=300s
- 日志：`/tmp/hgate-merged-full.log`, `results/hgate_dpo003_merged/group_{a,b}.log`
- Mistral BCP 脚本：`/root/democalib/eval_mistral_bcp.sh`（dry-run 通过，GPU 释放后可跑）

### 3. 📊 当前状态
**hgate-dpo003-merged RUNNING**：双 GPU merged 模型 H-gate eval，4 runs × 20 tasks × 6 variants。启动于 ~01:47 UTC，预计 ~07:00-08:00 UTC 完成。cron 在 ~02:38 UTC 确认 PID 688636 仍存活。

⚠️ **服务器刚重启**——PID 688636 可能已死。下一个"你"启动后**第一件事**是 reconcile_crons 或 SSH 检查进程是否存活。如果死了，需要重新启动 eval。

其余 13 个实验全部 DONE。无 Worker 在跑。无待处理审批。

### 4. 📋 待办
- **hgate-dpo003-merged cron 回调（进程完成）** → 按 on-experiment-done skill 处理：收集 4 runs 的 H2/H3 结果 → 汇总 mean completion/politeness → 对照 H-gate 阈值（H2: politeness ≤45.1%, H3: completion ≥29.6%）→ 更新 registry → 汇报 Director
- **hgate-dpo003-merged 进程死亡（服务器重启导致）** → 确认 cuda:2+cuda:3 空闲 → 检查 results/ 下已完成的 run 数据 → 只重跑缺失的 runs → 用 `GPU_ID=X VLLM_PORT=800X bash eval_dpo003_merged.sh` 重启
- **H2+H3 双 PASS** → Plan A：DPO 校准方法 + BCP 失败作 motivation，启动论文写作
- **H2+H3 双 FAIL** → Plan B：用 Mistral BCP eval 补数据（脚本已就绪 `eval_mistral_bcp.sh`，`GPU_ID=2 bash eval_mistral_bcp.sh`）
- **Mistral BCP 可并行**：如果 H-gate eval 只占一个 GPU，另一个 GPU 可同时跑 Mistral BCP

### 5. 🎯 战略上下文
- **决策链**：BCP FAIL(D003) → DPO 唯一路径(D005) → tokenizer mismatch 修复(D006) → Llama BCP 无效(D007) → vLLM LoRA bug 发现(D010) → merged 模型重跑 eval（当前）
- **核心判断**：diag-lora-merge 证明 DPO-003 merged completion=60% > base 40%，DPO 训练有效。但这只是 5 tasks 的小样本，完整 4×20×6 eval 结果才是 MVP 判定依据
- **易错点**：
  1. 不要用 LoRA serving 跑任何 eval（包括 hgate-dpo001/002 的数据都不可靠）
  2. hgate-dpo001/002/003 的 completion 数据全部标注了 `lora_serving_bug: true`，引用时必须说明不可靠
  3. Mistral tool_call_id 要求恰好 9 位字母数字（chat_template 有 raise_exception），运行时注意
  4. EMNLP ARR deadline 2026-05-25，剩余 12 天，5/16 前必须完成所有数据
