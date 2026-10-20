DCOL E2E DeBERTa v2 (artifacts/dcol_code/)

Files: dcol_model.py(29), dcol_loss.py(65), dcol_dataset.py(58), train_dcol.py(206), eval_dcol.py(138)
Total: 496 lines, modular design.

Note: Uses FP16 GradScaler which may cause overflow (see memory.md). Earlier v1 (dcol_trainer.py) fixed this by removing GradScaler. Merge best of both when plan_008 activates.