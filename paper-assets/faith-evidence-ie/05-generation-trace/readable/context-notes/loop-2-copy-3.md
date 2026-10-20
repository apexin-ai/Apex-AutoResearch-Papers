# reviewer / loop_2.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`0a54ba185351e7f96fb2.json`](../../sessions/0a/0a54ba185351e7f96fb2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T15:09:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（4× RTX 5090 32GB，单机两个 SSH endpoint rtx5090-4x 和 bjb2-12179 是同一台机器 — D004）
- kl_coef + QLoRA 4-bit 不兼容（D008）：**任何 kl_coef > 0 的实验必须 CRITICAL 打回**，已证明所有 kl_coef=0.05 实验在 step 5 KL 爆炸到 10^10
- ced_kl001 (kl_coef=0.01) 已被 D014 暂停，且 CED reward 设计有缺陷（短输出 hack），**即使 Director 要求启动也要提醒两个问题都未修复**
- save_total_limit=5 导致早期 checkpoint 丢失——ced_r5/extract_r3 的 pre-collapse checkpoint 已全部被覆盖，**flatnli_r3 重启前必须备份 checkpoint-20 到 80**

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，同机别名 bjb2-12179
- 代码：`/root/autodl-tmp/freige/`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型：`/root/autodl-tmp/models/Qwen3-4B`，SFT adapter：`/root/autodl-tmp/sft_output`
- 数据：`/root/autodl-tmp/data/docred/`（train 3027, dev 985）
- HF cache：`/root/autodl-tmp/.hf_cache`
- Eval 代码：`/root/autodl-tmp/freige/eval/inference.py`（13903 bytes, 统一版 23:02 更新）+ `evaluator.py`（12017 bytes）
- 活跃进程（截至 context reset）：
  - cuda:0 → ced_r5 (PID 53066, tmux=mvp2_grpo_ced_r5) — collapsed，step ~514/756
  - cuda:1 → sft_eval_r3 (PID 62357, tmux=mvp2_sft_eval_r3) — 刚启动 ~3/62 batches
  - cuda:2 → extract_r3 (PID 53144, tmux=mvp2_grpo_extract_r3) — stagnant，step ~515/756
  - cuda:3 → flatnli_r3 (PID 53287, tmux=mvp2_grpo_flatnli_r3) — 健康但 CPU NLI 120s/step，step 85/756
- GRPO 输出目录：`/root/autodl-tmp/grpo_{ced_r5,extract_r3,flatnli_r3}/`
- SFT eval 输出：`/root/autodl-tmp/sft_eval_r3_results/`

### 3. 📊 当前状态
我刚完成两轮全局健康检查并发了 3 个 post 给 Director：
1. **CRITICAL**：flatnli_r3 的 D015（kill + GPU NLI 重启）未执行，仍以 CPU NLI 跑，浪费 ~20h
2. **WARNING**：extract_r3 entropy collapse（grad_norm=0, entropy≈0.01），与 ced_r5 同根因但有残余 F1
3. **WARNING**：save_total_limit=5 导致 ced_r5/extract_r3 pre-collapse checkpoint 全部丢失，D011 多 checkpoint eval 策略无法执行

等待 Director 回应：
- flatnli_r3 kill+restart 是否执行（已催促）
- checkpoint 备份策略
- batch-eval-script worker 失败（未产出文件，可能需重新派 worker）
- sft_eval_r3 结果（预计 ~1.8h 后完成）

### 4. 📋 待办（条件触发式）
- sft_eval_r3 完成 → 对比 r2 指标（F1=40.57%, Evi-F1=79.79%, EDCR=71.18%），验证 eval 代码一致性；差异 >1pp 需 CRITICAL
- flatnli_r3 重启后 → 监控 entropy 趋势，step 150/200/250 各检查一次；entropy < 0.03 即预警 collapse
- extract_r3 完成 → 检查 last checkpoint eval 结果，对比 SFT baseline；F1 < 35% 确认 stagnation negative result
- ced_r5 完成 → 确认 negative result 记录完整，检查 registry conclusion
- ced_kl001 如被激活 → 核查是否修复了 CED reward 的短输出 hack（F1 门控），未修复则 CRITICAL 打回
- 任何新 GRPO 实验提交 → 核查 save_total_limit 是否增大、kl_coef 是否为 0

### 5. 🎯 战略上下文
**核心技术障碍**：kl_coef=0 + QLoRA 导致 entropy collapse 是跨 reward 配置的通用问题。kl_coef>0 导致 KL 爆炸。这是一个根本性矛盾（D008），目前无解。可能需要放弃 QLoRA 改 8-bit 或 full-precision ref model。

**CED reward 设计缺陷**：短输出不引用 distractor → CED 给近完美分。CED 本身被 reward hack。D014 要求加 F1 门控但尚未实现。

**决策链**：D001(两阶段MVP) → D002(MVP-1 PASS) → D008(kl_coef+QLoRA 不兼容) → D010(kl_coef=0) → D011(多checkpoint eval) → D012/D013(取消绝对F1门槛改相对) → D014(CED reward 需 F1 门控) → D015(flatnli_r3 kill+restart)

**易错点**：
1. 不要把 registry 的 status 当真——D015 说 kill 但实际没执行过，必须 SSH 验证进程
2. flatnli_r3 是唯一还在学习的实验，它的成败决定 MVP-2 能否有 positive result
3. 不要建议 kl_coef>0 的方案——已被 5 个实验证伪
4. SFT baseline F1=40.57% 来自 r2（旧 eval 代码），r3 结果可能不同——在 r3 出来前不要假设 baseline 数字
5. D012/D013 是重复决策（内容几乎相同），不要困惑


---
