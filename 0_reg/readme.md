# 0 64bit レジスタアクセスお試し

### ブロックデザインを作る

トップの README を参考になひビバのファイルを準備、`open_project_gui.sh` 実行でプロジェクトが再現されます。

### FPGAに転送とドライバロード

これもトップの README を参考に…

### 実行する

0_reg ディレクトリにて、

```
tom01h@tom01h-Vostro-3250:~/work/LiteFury/0_reg$ sudo python3 test.py 
IP 初期設定
レジスタアクセス
wdata 0xd740177df9145b32
rdata 0xd740177df9145b32
wstrb 0xff
lower 0xf9145b32
upper 0xd740177d
```

