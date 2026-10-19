# 诊断：eval-supp-obj-reconvla-s47

## 失败原因
**伪失败（false positive）**——eval 脚本实际正常完成，cron 误判。脚本 return_code=0，结果 JSON 已写入磁盘，但脚本未发送 sentinel 文件 / W&B 信号，cron 监控误判为 "process dead"。

## 日志摘要
日志 `/tmp/eval_obj_reconvla_s47.log`（6132 bytes，最后写入 2026-05-24 20:26:33）显示完整 10 个 task × 20 rollout 全部跑完，无 Error / Exception / Traceback。

末尾关键行：
```
[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 95.0% (19/20)

============================================================
Overall success rate (reconvla): 76.5% (153/200)
============================================================
[eval] Results saved to logs/eval_object_reconvla_seed47.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
```

结果 JSON `logs/eval_object_reconvla_seed47.json`（1504 bytes，20:26 写入）完好，包含 per-task 成功率与 `overall_success_rate: 0.765`。

## 环境状态
- **GPU 4**：`memory.used=1 MiB / 24564 MiB`，`util=0%`——进程已完全退出，显存释放正常，无残留
- **磁盘**：根分区 `/` 26G/30G（86%，紧但未满），`/root/autodl-tmp` 115G/250G（46%，充足）
- **tmux session**：`tmux ls` 在 ssh_read_only 白名单外无法直接查；从 GPU 0% 利用率和日志已结束推断 session 应已自然退出（或仅剩空 shell）
- **日志中无 OOM / CUDA error / killed 痕迹**

## 建议
**无需重试，无需修复代码。** 实验已成功产出可用结果：
- per-task 成功率全部可读，overall = 76.5%（153/200，seed=47）
- 直接将 `logs/eval_object_reconvla_seed47.json` 纳入 supp 结果表即可

后续动作（优先级排序）：
1. 在 cron 配置中为 `evaluate.py` 的 reconvla 模式补一行写 sentinel（如 `Path("sentinels/<job>.done").touch()`），消除未来同类伪失败
2. 若不想改代码，把该 job 的 cron health-check 规则从"无 sentinel 即失败"改为"return_code==0 且产物 JSON 存在即成功"
3. 根分区 86% 已偏紧，留意是否还有日志/HF cache 在根分区，必要时清理或迁到 `/root/autodl-tmp`
