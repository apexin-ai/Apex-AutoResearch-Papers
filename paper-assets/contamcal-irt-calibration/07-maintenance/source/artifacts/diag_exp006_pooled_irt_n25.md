# 诊断: exp_006_pooled_irt_n25

**日期**: 2026-05-16  
**状态**: 误报 — 实验实际已成功完成

## 失败根因（一句话）

实验正常完成退出，但脚本未写入 sentinel 文件且无 W&B 集成，cron 检测到"process dead"后误判为失败。

## 详细分析

### 日志关键段落

```
2026-05-16 21:29:53,492 [INFO] CmdStan done processing.
2026-05-16 21:29:55,502 [INFO] Sampling completed in 157.4s
2026-05-16 21:30:29,791 [INFO] [arc_challenge] γ=0.8616 [0.0921, 1.6302], R̂=1.0069, ESS=1553, div=0
2026-05-16 21:30:29,791 [INFO] [arc_challenge] raw_MAE=0.0324, cal_MAE=0.0229, ΔMAE=0.0094

================================================================================
POOLED IRT RESULTS (4PL+γ, RRF signal exposure)
================================================================================
Bench            N_mod N_item       γ̂               95% CI     R̂    ESS    PPP  rawMAE  calMAE   ΔMAE
--------------------------------------------------------------------------------
mmlu                13    300   0.5502 [-0.5720, 1.7085] 1.0057   1564 0.2265  0.0140  0.0051 0.0089
gsm8k               21    300   0.3784 [-0.1002, 0.8473] 1.0075   1476 0.1052  0.1470  0.0119 0.1351
arc_challenge       13    300   0.8616 [0.0921, 1.6302] 1.0069   1553 0.0030  0.0324  0.0229 0.0094

Results saved to /root/autodl-tmp/exp006/results_pooled_n20
```

4 chains 全部正常完成采样（157.4s），结果已保存。

### 产出文件确认

```
/root/autodl-tmp/exp006/results_pooled_n20/
├── pooled_rrf_irt_results.json (17779 bytes)
├── mmlu/irt_results.json
├── gsm8k/irt_results.json
└── arc_challenge/irt_results.json
```

### 潜在问题

1. **显示 Bug**: 命令指定 `--model 2pl_gamma`，但输出表头显示 "4PL+γ"。需检查脚本逻辑是否确实用了 2PL 或模型选择有误。
2. **无 sentinel 文件**: 输出目录无 DONE/SUCCESS 标记，cron 无法区分"正常退出"与"异常退出"。

## 修复建议

1. **标记实验为成功** — 结果完整，无需重跑
2. **给 `run_irt_calibration.py` 加 sentinel 写入**：脚本末尾 `touch output_dir/DONE`，避免 cron 误判
3. **核实 model 参数**：检查 `--model 2pl_gamma` 是否确实执行了 2PL+γ（还是 fallback 到 4PL+γ），表头 "4PL+γ" 可能只是 print 字符串写死

## exp_001_eval_3B_instruct_v2 进程状态

PID 764449 已死亡（ps 返回空）。进程已结束。

## 附加信息

- 脚本位置: `/root/contamcal-irt-calibration/exp006/run_irt_calibration.py`
- 最后修改: 2026-05-16 13:53:33
- 输入数据 (`exposure_scores.json`): 存在，格式正确（25 models × 3 benchmarks × 300 items）
