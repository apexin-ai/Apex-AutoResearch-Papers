import argparse
import os
import sys
import time

os.environ["TORCHDYNAMO_DISABLE"] = "1"
sys.path.insert(0, "/root/spectral_optim_vision_geometry")

import torch
import torch.nn as nn
import timm
from heavyball import SOAP
from muon_train import set_seed, get_dataloaders, evaluate
import shutil

os.environ.setdefault("TMPDIR", "/root/autodl-tmp/tmp")
os.makedirs(os.environ["TMPDIR"], exist_ok=True)

SAVE_EPOCHS = {1, 5, 10, 15, 20}


def check_disk_space(path='/', min_gb=2.0):
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


def train(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    model = timm.create_model("convnext_tiny", pretrained=False, num_classes=100).to(device)
    optimizer = SOAP(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()

    train_dl, val_dl = get_dataloaders(args.batch_size)
    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model=convnext_tiny, params={param_count:.1f}M, device={device}, optimizer=soap, lr={args.lr}, wd={args.weight_decay}, batches/epoch={n_batches_total}", flush=True)

    os.makedirs(args.output_dir, exist_ok=True)
    best_acc = 0.0
    lr_tag = str(args.lr).replace(".", "")
    start_epoch = 1

    if args.resume and os.path.isfile(args.resume):
        ckpt = torch.load(args.resume, map_location=device, weights_only=False)
        model.load_state_dict(ckpt["state_dict"])
        optimizer.load_state_dict(ckpt["optimizer_state"])
        start_epoch = ckpt["epoch"] + 1
        best_acc = ckpt.get("val_acc", 0.0)
        for _ in range(1, start_epoch):
            scheduler.step()
        print(f"Resumed from {args.resume}, starting at epoch {start_epoch}, best_acc={best_acc:.2f}%", flush=True)

    for epoch in range(start_epoch, args.epochs + 1):
        model.train()
        running_loss, n_batches = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            n_batches += 1
            if n_batches % 50 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        scheduler.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, time={epoch_time:.1f}s", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc

        if epoch in SAVE_EPOCHS or epoch == args.epochs:
            ckpt_path = os.path.join(args.output_dir, f"convnext_t_soap_lr{lr_tag}_s{args.seed}_ep{epoch}.pt")
            _save_free_gb = shutil.disk_usage('/root/autodl-tmp').free / (1024**3)
            if _save_free_gb < 1.0:
                print(f"WARNING: Low disk space on data disk: {_save_free_gb:.1f}G free", flush=True)
            torch.save({
                "state_dict": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
                "train_loss": avg_loss,
                "lr": args.lr,
            }, ckpt_path)
            print(f"  checkpoint saved: {ckpt_path}", flush=True)

    print(f"TRAINING_COMPLETE best_val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    # 20ep: python convnext_t_soap_train.py --lr {BEST_LR} --epochs 20
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--lr", type=float, default=0.003, help="SOAP learning rate (set from sweep result)")
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    parser.add_argument("--resume", type=str, default=None, help="Path to checkpoint to resume from")
    args = parser.parse_args()
    check_disk_space('/')
    check_disk_space('/root/autodl-tmp', min_gb=5.0)
    train(args)
