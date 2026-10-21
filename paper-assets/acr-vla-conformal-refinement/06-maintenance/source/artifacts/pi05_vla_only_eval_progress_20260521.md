# π0.5 VLA-only Baseline Eval 进度检查 (2026-05-21)

服务器：bjb1-32546，account=root

## 总览

| 实验 | PID | 进程 | 进度 | 最终 SR | 状态 |
|---|---|---|---|---|---|
| eval-pi05-vla-only-object-seed42 | 982849 | **已死** | 10/10 tasks done | **0.0% (0/200)** | EXIT_CODE=0 (完成) |
| eval-pi05-vla-only-object-seed43 | 983128 | **已死** | 10/10 tasks done | **0.0% (0/200)** | EXIT_CODE=0 (完成) |
| eval-pi05-vla-only-object-seed44 | 983472 | **已死** | 10/10 tasks done | **0.0% (0/200)** | EXIT_CODE=0 (完成) |
| eval-pi05-vla-only-spatial-seed42 | 983816 | **已死** | 8 tasks done + 1 task 10/20 | 0.0% (前 8 task) | 中途死亡，无 EXIT_CODE |
| eval-pi05-vla-only-spatial-seed43 | 984171 | **已死** | 8 tasks done + 1 task 10/20 | 0.0% (前 8 task) | 中途死亡，无 EXIT_CODE |
| eval-pi05-vla-only-spatial-seed44 | 984515 | **已死** | 8 tasks done + 1 task 10/20 | 0.0% (前 8 task) | 中途死亡，无 EXIT_CODE |

`ps -p 982849,983128,983472,983816,984171,984515 -o ...` 返回 exit code 1（无匹配 PID）。

## GPU 使用

所有 6 张 GPU (cuda:0-5) 全部空闲：0% 利用率，1 MiB / 24564 MiB 显存使用。

## **Fix 部署状态：部分生效，仍然失败**

每个 log 都报告：

```
[pi05] Fixed 437 vision tower keys
[pi05] Vision tower missing_keys (376): [
  'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.weight',
  'model.paligemma_with_expert.paligemma.model.multi_modal_projector.linear.bias',
  'model.paligemma_with_expert.paligemma.model.language_model.embed_tokens.weight',
  'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.q_proj.weight',
  'model.paligemma_with_expert.paligemma.model.language_model.layers.0.self_attn.k_proj.weight',
  ...
]
```

- ✅ **Vision tower remap 已生效**：437 个 vision_tower.vision_model.* 的 key 被成功 remap 到 vision_tower.*
- ❌ **376 个其他 key 仍 missing**：包括 multi_modal_projector 和 **整个 language_model** 的权重
- 结果：vision tower 加载了真实权重，但 **language model 在随机权重下运行** → 0.0% SR

这是一个 *不同于* 之前怀疑的故障模式。之前以为 fix 完全未部署 → vision tower 随机权重。实际是 fix 修了 vision tower 但 **language_model 的 key 命名仍然不匹配 checkpoint**，导致 LM 完全随机。

`/root/miniconda3/lib/python3.12/site-packages/lerobot/policies/pi05/modeling_pi05.py` 文件 mtime 是 2026-05-21 18:59（在 spatial 实验死后约 4 分钟），暗示有人在实验运行期间替换/重装了 lerobot 包，可能是导致 spatial 进程死亡的直接原因。

## 时间线（北京时区，+0800）

- 10:18 UTC ≈ 18:18 北京：6 个实验启动
- 18:48 北京（~30 分钟后）：3 个 object 实验全部完成，EXIT_CODE=0
- 18:55 北京（~37 分钟后）：3 个 spatial 实验同时在第 9 个 task 的 10/20 rollout 处停止写 log
- 18:59 北京：`modeling_pi05.py` 被修改（可能 pip reinstall 触发）
- 现在 ~19:02-19:03 北京：所有进程已死，GPU 全空

## 关键结论

1. **没有任何实验产生可用的 baseline SR**——全部 0%，因为 language_model 用随机权重运行
2. **Object 实验跑完了**：每个产出 logs/eval_object_vla_only_pi05_seed{42,43,44}.json，但结果不可用
3. **Spatial 实验中途死亡**：spatial-seed{42,43,44} 三个都死在完全相同的位置（第 9 task rollout 10/20），高度怀疑是外部因素（lerobot 包重装）导致集体崩溃
4. **修复方向**：需要在 lerobot pi05 的 load_state_dict 逻辑里追加 `language_model.*` 和 `multi_modal_projector.*` 的 key remap，而不止 vision_tower

## 预估剩余运行时间

不适用 — 全部已停止。需要修复 376-key remap 问题后重启全部 6 个实验。
