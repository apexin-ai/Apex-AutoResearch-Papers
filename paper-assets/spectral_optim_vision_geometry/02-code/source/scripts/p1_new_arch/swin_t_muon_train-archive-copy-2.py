# checkpoint path migrated to /root/autodl-tmp (root partition is ~30G; checkpoints filled it).
import argparse
import os
import sys
import time

sys.path.insert(0, "/root/spectral_optim_vision_geometry")

import torch
import torch.nn as nn
import timm
from muon import muon_update
from muon_train import SingleGPUMuon, set_seed, get_dataloaders, evaluate
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

SAVE_EPOCHS = {1, 5, 10, 15, 20}


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')



def _norm_param_names(model):
    names = set()
    for mname, mod in model.named_modules():
        if isinstance(mod, (nn.LayerNorm, nn.BatchNorm1d, nn.BatchNorm2d, nn.GroupNorm)):
            for pname, _ in mod.named_parameters():
                names.add(f"{mname}.{pname}" if mname else pname)
    return names


def partition_params(model):
    """Swin-T: patch_embed/head/norm/bias/1D/relative_position_bias -> Adam, rest -> Muon."""
    norm_names = _norm_param_names(model)
    muon_params, adam_params = [], []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        is_adam = (
            name.startswith("head.") or name.startswith("patch_embed.")
            or name in norm_names
            or name.endswith(".bias")
            or param.ndim < 2
            or "relative_position_bias_table" in name
        )
        (adam_params if is_adam else muon_params).append(param)
    return muon_params, adam_params


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    model = timm.create_model("swin_tiny_patch4_window7_224", pretrained=False, num_classes=100).to(device)
    muon_params, adam_params = partition_params(model)
    print(f"Param split: {len(muon_params)} Muon, {len(adam_params)} AdamW", flush=True)

    muon_opt = SingleGPUMuon(muon_params, lr=args.muon_lr, momentum=0.95)
    adam_opt = torch.optim.AdamW(adam_params, lr=3e-4, weight_decay=0.05)
    muon_sched = torch.optim.lr_scheduler.CosineAnnealingLR(muon_opt, T_max=args.epochs)
    adam_sched = torch.optim.lr_scheduler.CosineAnnealingLR(adam_opt, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    lr_tag = str(args.muon_lr).replace(".", "")
    print(f"model=swin_tiny, params={param_count:.1f}M, device={device}, muon_lr={args.muon_lr}, batches/epoch={n_batches_total}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            muon_opt.zero_grad()
            adam_opt.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            muon_opt.step()
            adam_opt.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        muon_sched.step()
        adam_sched.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={epoch_time:.1f}s, muon_lr={muon_sched.get_last_lr()[0]:.6f}", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc

        if epoch in SAVE_EPOCHS or epoch == args.epochs:
            ckpt_path = os.path.join(args.output_dir, f"swin_t_muon_lr{lr_tag}_s{args.seed}_ep{epoch}.pt")
            # _DISK_CHECK_SAVE_INJECTED_
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "muon_optimizer_state": muon_opt.state_dict(),
                "adam_optimizer_state": adam_opt.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "muon_lr": args.muon_lr,
            }, ckpt_path)
            print(f"  checkpoint saved: {ckpt_path}", flush=True)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    # 20ep: python swin_t_muon_train.py --muon-lr {BEST_LR} --epochs 20
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--muon-lr", type=float, default=0.006)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)
    train(args)
