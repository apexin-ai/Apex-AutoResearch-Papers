# π0.5 CRM Checkpoint 来源验证报告

**日期**: 2026-05-26  
**目的**: 回应 Reviewer 关于 π0.5 Goal CRM 评测可能误用 SmolVLA CRM checkpoint 的担忧

---

## 1. Checkpoint 文件清单

### 文件大小与 MD5（三台服务器完全一致）

| Checkpoint | 大小 | MD5 |
|---|---|---|
| `crm_pi05_unified_3suite/crm_best.pt` | 2,484,379 bytes | `25093621fd5158951b2297ca406472f4` |
| `crm_smolvla_3suite_v1/crm_best.pt` | 1,320,219 bytes | `4161c6403b8eb268864b99dd986be784` |

验证服务器: cqa1-32758, bjb1-32546, bjb2-28827（bjb1-18228 端口变更不可达，但 registry 记录的命令行已足够验证）

### 各服务器 checkpoint 存在情况

| 服务器 | crm_pi05_unified_3suite | crm_smolvla_3suite_v1 | 其他 CRM |
|---|---|---|---|
| cqa1-32758 | ✓ | ✓ | crm_unified_4suite_r4 |
| bjb1-32546 | ✓ | ✓ | crm_v3_norm/*, crm_pi05_full/*, crm_loss_variants/*, crm_unified_4suite, crm_unified_4suite_r4 |
| bjb2-28827 | ✓ | ✓ | crm_v3_norm/*, crm_pi05_full/*, crm_openvla_obs_only, crm, crm_unified_4suite_r4 |

---

## 2. 模型维度对比（决定性证据）

```
=== π0.5 CRM (crm_pi05_unified_3suite) ===
  input_mean: torch.Size([2118])    ← obs_dim=2048 + unified_action=70
  net.0.weight: torch.Size([256, 2118])
  total_params: 620,202

=== SmolVLA CRM (crm_smolvla_3suite_v1) ===
  input_mean: torch.Size([990])     ← obs_dim=512 + action_dim*K
  net.0.weight: torch.Size([256, 990])
  total_params: 329,178
```

**两个 checkpoint 输入维度完全不同（2118 vs 990），不可能互换使用——加载错误的 checkpoint 会在第一次前向传播时因维度不匹配而崩溃。**

---

## 3. 当前 RUNNING 的 π0.5 CRM 实验（bjb1-18228）

| Exp ID | Command (关键参数) | Checkpoint |
|---|---|---|
| pi05-crm-k2-long-s42 | `--model pi05 --mode crm_obs_only --obs_dim 2048 --unified_obs_dim 2088` | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` ✓ |
| pi05-crm-k2-long-s43 | 同上 | 同上 ✓ |
| pi05-crm-k2-long-s44 | 同上 | 同上 ✓ |

---

## 4. 已完成 π0.5 CRM 实验 checkpoint 来源（从 registry + 日志）

所有已完成的 π0.5 CRM 实验（共 ~15 个，包含 goal/spatial/object/long 四个 suite）均使用:
- checkpoint: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`
- obs_dim: 2048
- unified_obs_dim: 2088

**日志实证** (cqa1-32758, eval_goal_crm_pi05_seed42.log):
```
[evaluate] args: {..., 'crm_checkpoint': '/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt', 'obs_dim': 2048, 'unified_obs_dim': 2088, ...}
```

**日志实证** (bjb2-28827, nohup_goal_adaptive_pi05_s43.log):
```
[eval] CRM loaded from /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt (615,966 params)
[eval] PI05 features (2048D) passed directly to CRM (no projection)
```

---

## 5. 结论

**π0.5 CRM 实验全部使用了正确的 checkpoint（crm_pi05_unified_3suite/crm_best.pt）。没有任何实验误用 SmolVLA checkpoint。**

理由：
1. 两个 checkpoint 文件大小差异近 2x（2.4MB vs 1.3MB），md5 完全不同
2. 输入维度不同（2118 vs 990），即使误加载也会立即报错，不可能产出结果
3. Registry 中所有 π0.5 实验的 `checkpoint_source` 字段均指向 `crm_pi05_unified_3suite`
4. 多台服务器的 eval 运行日志明确打印了加载的 checkpoint 路径和参数数量（615,966 = 对应 620,202 total - normalization buffers）
5. 日志确认 obs_dim=2048 与 π0.5 模型匹配

**无任何 exp_id 用错 checkpoint。**
