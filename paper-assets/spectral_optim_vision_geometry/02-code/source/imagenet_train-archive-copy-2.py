# ImageNet-1K trainer with AdamW/SOAP/Shampoo optimizers
# Usage: python3 imagenet_train.py --model resnet50 --optimizer adamw --gpu 0
#        python3 imagenet_train.py --model deit_small --optimizer soap --gpu 0
# Data:  /root/autodl-tmp/imagenet/{train,val}/ (ImageFolder format)
import argparse
import os
os.environ["TORCHDYNAMO_DISABLE"] = "1"
import shutil
import random
import time

import numpy as np
import torch
import torch.nn as nn
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from gpu_utils import check_gpu_whitelist


def check_disk_space(path='/', min_gb=2.0):
    os.makedirs(path, exist_ok=True)
    usage = shutil.disk_usage(path)
    free_gb = usage.free / (1024**3)
    if free_gb < min_gb:
        raise RuntimeError(f'Disk space critically low: {free_gb:.1f}G free on {path}. Need >= {min_gb}G.')


def format_lr(lr):
    s = f"{lr:.0e}"
    base, exp = s.split('e')
    return f"{base}e{int(exp)}"


MODEL_REGISTRY = {
    "resnet50": "resnet50",
    "resnet50_ln": "resnet50",
    "deit_small": "deit_small_patch16_224",
    "convnext_tiny": "convnext_tiny",
    "swin_tiny": "swin_tiny_patch4_window7_224",
}


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def replace_bn_with_gn(module):
    for name, child in module.named_children():
        if isinstance(child, nn.BatchNorm2d):
            setattr(module, name, nn.GroupNorm(1, child.num_features))
        else:
            replace_bn_with_gn(child)


IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def get_dataloaders(data_dir, batch_size):
    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    train_ds = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=train_tf)
    val_ds = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=val_tf)
    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                          num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)
    return train_dl, val_dl


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += (model(images).argmax(1) == labels).sum().item()
        total += labels.size(0)
    return 100.0 * correct / total


def train(args):
    os.makedirs(args.output_dir, exist_ok=True)
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    num_classes = 1000
    timm_name = MODEL_REGISTRY[args.model]
    model = timm.create_model(timm_name, pretrained=False, num_classes=num_classes)
    if args.model == "resnet50_ln":
        replace_bn_with_gn(model)
    model = model.to(device)

    if args.optimizer == "adamw":
        lr = args.lr if args.lr is not None else 3e-4
        wd = args.weight_decay if args.weight_decay is not None else 0.05
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "soap":
        from heavyball import SOAP
        lr = args.lr if args.lr is not None else 3e-3
        wd = args.weight_decay if args.weight_decay is not None else 0.01
        optimizer = SOAP(model.parameters(), lr=lr, weight_decay=wd)
    elif args.optimizer == "shampoo":
        from heavyball import KLShampoo
        lr = args.lr if args.lr is not None else 3e-3
        wd = args.weight_decay if args.weight_decay is not None else 0.01
        optimizer = KLShampoo(model.parameters(), lr=lr, weight_decay=wd)

    scheduler = CosineAnnealingLR(optimizer, T_max=args.epochs)
    criterion = nn.CrossEntropyLoss()
    lr_str = format_lr(lr)

    train_dl, val_dl = get_dataloaders(args.data_dir, args.batch_size)

    param_count = sum(p.numel() for p in model.parameters()) / 1e6
    n_batches_total = len(train_dl)
    print(f"model={args.model} ({timm_name}), params={param_count:.1f}M, optimizer={args.optimizer}, "
          f"lr={lr}, wd={wd}, device={device}, batches/epoch={n_batches_total}", flush=True)

    best_acc = 0.0
    ckpt_name = f"{args.model}_{args.optimizer}_s{args.seed}_lr{lr_str}_best.pt"

    for epoch in range(1, args.epochs + 1):
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
            if n_batches % 100 == 0:
                elapsed = time.time() - t0
                print(f"  batch {n_batches}/{n_batches_total}, loss={loss.item():.4f}, elapsed={elapsed:.1f}s", flush=True)
        scheduler.step()

        val_acc = evaluate(model, val_dl, device)
        avg_loss = running_loss / n_batches
        epoch_time = time.time() - t0
        print(f"epoch={epoch}, train_loss={avg_loss:.4f}, val_acc={val_acc:.2f}%, best_val_acc={best_acc:.2f}%, time={epoch_time:.1f}s", flush=True)

        if val_acc > best_acc:
            best_acc = val_acc
            check_disk_space(args.output_dir, min_gb=1.0)
            torch.save({
                "state_dict": model.state_dict(),
                "optimizer_state": optimizer.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc,
            }, os.path.join(args.output_dir, ckpt_name))

    print(f"TRAINING_COMPLETE val_acc={best_acc:.2f}%", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ImageNet-1K trainer (AdamW / SOAP / Shampoo)")
    parser.add_argument("--model", type=str, default="resnet50", choices=list(MODEL_REGISTRY.keys()))
    parser.add_argument("--optimizer", type=str, default="adamw", choices=["adamw", "soap", "shampoo"])
    parser.add_argument("--lr", type=float, default=None, help="Learning rate (default: 3e-4 for AdamW, 3e-3 for SOAP/Shampoo)")
    parser.add_argument("--weight-decay", type=float, default=None, help="Weight decay (default: 0.05 for AdamW, 0.01 for SOAP/Shampoo)")
    parser.add_argument("--epochs", type=int, default=90)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--data-dir", type=str, default="/root/autodl-tmp/imagenet/")
    parser.add_argument("--output-dir", type=str, default="/root/autodl-tmp/checkpoints/spectral_optim/")
    args = parser.parse_args()

    check_gpu_whitelist(args.gpu)
    check_disk_space('/')
    check_disk_space(args.output_dir, min_gb=5.0)
    train(args)
