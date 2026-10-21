"""SOAP CIFAR-100 LR Sweep (multi-model support)"""
import os
os.environ["TORCHDYNAMO_DISABLE"] = "1"
import argparse
import time
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from heavyball import SOAP
from gpu_utils import check_gpu_whitelist

BATCH_SIZE = 128
SEED = 42
DATA_ROOT = "/root/spectral_optim_vision_geometry/data"


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def get_dataloaders():
    mean, std = (0.5071, 0.4867, 0.4408), (0.2675, 0.2565, 0.2761)
    train_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    val_tf = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std),
    ])
    train_ds = datasets.CIFAR100(root=DATA_ROOT, train=True, download=False, transform=train_tf)
    val_ds = datasets.CIFAR100(root=DATA_ROOT, train=False, download=False, transform=val_tf)
    train_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True, drop_last=True)
    val_dl = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False, num_workers=4, pin_memory=True)
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


def run_one_lr(model_name, lr, epochs, device, train_dl, val_dl):
    set_seed(SEED)
    model = timm.create_model(model_name, pretrained=False, num_classes=100).to(device)
    n_params = sum(p.numel() for p in model.parameters()) / 1e6
    optimizer = SOAP(model.parameters(), lr=lr, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.CrossEntropyLoss()

    best_acc = 0.0
    for epoch in range(1, epochs + 1):
        model.train()
        running_loss, n = 0.0, 0
        t0 = time.time()
        for images, labels in train_dl:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = criterion(model(images), labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            n += 1
        scheduler.step()
        val_acc = evaluate(model, val_dl, device)
        best_acc = max(best_acc, val_acc)
        print(f"  ep={epoch} loss={running_loss/n:.4f} val_acc={val_acc:.2f}% time={time.time()-t0:.1f}s", flush=True)
    return best_acc, n_params


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--models", type=str, default="resnet50")
    parser.add_argument("--lrs", type=str, default="1e-4,3e-4,1e-3,3e-3,1e-2")
    parser.add_argument("--epochs", type=int, default=5)
    args = parser.parse_args()
    check_gpu_whitelist(args.gpu)

    device = torch.device(f"cuda:{args.gpu}")
    model_names = [m.strip() for m in args.models.split(",")]
    lrs = [float(x) for x in args.lrs.split(",")]

    train_dl, val_dl = get_dataloaders()

    for model_name in model_names:
        print(f"=== SOAP {model_name} C100 LR Sweep ===")
        print(f"LRs: {lrs}, epochs={args.epochs}, bs={BATCH_SIZE}, seed={SEED}")
        print(f"GPU: {torch.cuda.get_device_name(args.gpu)}")
        print()

        results = []
        for lr in lrs:
            print(f"[{model_name} LR={lr}]", flush=True)
            t0 = time.time()
            best, n_params = run_one_lr(model_name, lr, args.epochs, device, train_dl, val_dl)
            elapsed = time.time() - t0
            results.append((lr, best, elapsed))
            print(f"  => best_val_acc={best:.2f}% ({elapsed:.0f}s)\n", flush=True)

        print("=" * 50)
        print(f"SUMMARY: SOAP {model_name} ({n_params:.1f}M params) CIFAR-100 {args.epochs}ep")
        print(f"{'LR':<10} {'Best Val Acc':<15} {'Time':<10}")
        print("-" * 35)
        for lr, acc, t in results:
            print(f"{lr:<10.0e} {acc:<15.2f}% {t:<10.0f}s")
        best_lr, best_acc, _ = max(results, key=lambda x: x[1])
        print(f"\nBest: lr={best_lr:.0e}, val_acc={best_acc:.2f}%")
        print("SWEEP_COMPLETE")


if __name__ == "__main__":
    main()
