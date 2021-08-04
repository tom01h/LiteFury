# LiteFury
Artix-7 100T が M.2 PCIe に載ってるやつです。  
[Amazon.com: RHS Research Litefury Xilinx Artix-7 FPGA M.2 Development Board](https://www.amazon.com/dp/B08BKSVJH5) で買しました。  
下駄も一緒に買いました。

## 環境設定
- セキュアブートを無効にする
- Ubuntu 18.04.4 をインストール
- sudo apt update; sudo apt upgrade
- sudo apt install git build-essential python3-pip
- pip3 install numpy
- Vivado 20.1 をインストール

## デモ試行
### PCIeドライバ
- https://github.com/Xilinx/dma_ip_drivers をクローン
  - エラー対策に SSL がどうのこうの (必要ないかもしれないけど)
    -　[ここを参考に](https://superuser.com/questions/1214116/no-openssl-sign-file-signing-key-pem-leads-to-error-while-loading-kernel-modules/1322832#1322832)
  - 2020.1 ブランチ
  - ファイル修正 (必要ないかもしれないけど)
    ``` 
    --- a/XDMA/linux-kernel/xdma/Makefile
    +++ b/XDMA/linux-kernel/xdma/Makefile
    @@ -32,5 +32,6 @@ clean:
     
     install: all
            $(MAKE) -C $(BUILDSYSTEM_DIR) M=$(PWD) modules_install
    +       depmod -A
    ```
  - dma_ip_drivers/XDMA/linux-kernel/xdma にて sudo make install
  - dma_ip_drivers/XDMA/linux-kernel/tests にて sudo ./load_driver.sh 
- LiteFury は買ってきたままでも試行できる
- https://github.com/RHSResearchLLC/NiteFury-and-LiteFury をクローン
  - ファイル修正
    ```
    --- a/Sample-Projects/Project-0/Host/Host/dma-test-2.py
    +++ b/Sample-Projects/Project-0/Host/Host/dma-test-2.py
    @@ -10,7 +10,7 @@ def mem_test_random():
     
         # This is the only number that should need to change- how many MB to generate
         # 256M16 part is 512MB; 512M16 part is 1024GB
    -    NUM_MB=1024
    +    NUM_MB=512
    ```
  - Sample-Projects/Project-0/Host/Host/ にて sudo python3 dma-test-2.py

### サンプルデザイン合成
買って来たままでも試せたけど、自前の合成も試してみる
まだ…