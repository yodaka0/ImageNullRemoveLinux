# MDetToolsForJCameraTraps

## What's this：このプログラムについて

This program aims to detect wildlife from camera trap images using [MegaDetector (Beery et al. 2019)](https://github.com/microsoft/CameraTraps) and to extract images in which animals were detected. This document is a minimal description and will be updated as needed.  
このプログラムは、[MegaDetector (Beery et al. 2019)](https://github.com/microsoft/CameraTraps)を利用してカメラトラップ映像から野生動物を検出し、動物が検出された画像を抽出することを目的として作成されました。このドキュメントは現時点では最低限の記述しかされていないため、今後随時更新していく予定です。

このプログラムは、https://github.com/gifu-wildlife/MDetToolsForJCameraTraps を元に作成しました。
 


---

## Get Started：はじめに

<br />

### Prerequisites：環境整備

* OS  
    The following code was tested on Ubuntu.  
    During the test run, .jpg as the image file format.  
    以下のコードはUbuntuで動作確認しています。  
    動作確認時、静止画ファイル形式は.jpgを用いました。

* NVIDIA Driver(if use gpu)
    NVIDAドライバーをインストールする

    Please refer to [NVIDIA Driver Version Check](https://www.nvidia.com/Download/index.aspx?lang=en-us).
    *** is a placeholder. Please enter the recommended nvidia driver version.  
    [NVIDIAドライババージョンチェック](https://www.nvidia.com/Download/index.aspx?lang=en-us)を参照し、***に推奨されるnvidiaドライババージョンを入力した上で実行してください。  

    Check installation.  
    インストール状況の確認。

    ```commandprompt
    nvidia-smi 
    # NVIDIA Driver installation check
    ```

        If nvidia-smi does not work, Try Rebooting.  
        nvidia-smiコマンドが動作しない場合は再起動してみてください。

* Conda

    miniconda(anaconda)をインストール
    https://docs.conda.io/projects/miniconda/en/latest/

    mambaのインストール
    ```commandprompt 
    conda install mamba -c conda-forge
    ```

    condaのパスを通す
    システム環境変数の編集->環境変数->PATH->新規->condaのpathをコピペ


<br />

### Instllation：インストール

1. Clone the Repository：リポジトリの複製
    Download ZIP from <>code and Unzip in any directory of yours. 
    <>codeからZIPをダウンロードし、任意のディレクトリで解凍してください。

2. Move Project Directory：プロジェクトディレクトリへ移動

    ```commandprompt
    cd {ImageNullRemoveLinux-masterのパス}
    ```

3. create conda environment：conda環境の構築

    ```commandprompt
    mamba env create -f environment.yml
    ```
    

  
<br />

4. Download MegaDetector weight file：MegaDetectorの重みファイルのダウンロード

    https://github.com/microsoft/CameraTraps/releases/tag/v5.0
    からmd_v5a.0.0.ptをダウンロード後、ImageNullRemoveLinux\models　内に移動させる


---

## Usage：使い方

<br />

0. ディレクトリの移動

    ```commandprompt
    cd {ImageNullRemoveLinux-masterのパス}
    ```
    
1. conda環境のアクティベート

    ```commandprompt
    conda activate inrl
    ```


2. gpuが使えるか確認 

    ```commandprompt(conda)
    python gpu_check.py
    ```


3. Run MegaDetector  
  MegaDetectorの実行

    ```commandprompt(conda)
    python exec_mdet.py session_root={カメラデータが入ったフォルダの絶対パス}
    ```
4. output
   カメラデータが入ったフォルダと同じ階層にカメラデータが入ったフォルダ_outが作成される。
   カメラデータが入ったフォルダにjsonファイルが保存される。
   カメラデータが入ったフォルダ_outにcsvファイルが保存される

*setting
src/utils/config.py の class MDetConfig:にあるthresholdを変更することで検出の閾値を設定できます(デフォルトは0.2)。

もしエラーが発生したら
AttributeError: ‘Upsample’ object has no attribute ‘recompute_scale_factor’

■解決策

下記のコード修正をすることで解決しました。

修正するファイル：upsampling.py

C:\Users\[ユーザー名]\anaconda3\envs\[仮想環境名]\Lib\site-packages\torch\nn\modules\upsampling.py

修正前

def forward(self, input: Tensor) -> Tensor:

        return F.interpolate(input, self.size, self.scale_factor, self.mode,　self.align_corners,recompute_scale_factor=self.recompute_scale_factor)

修正後

def forward(self, input: Tensor) -> Tensor:

        return F.interpolate(input, self.size, self.scale_factor, self.mode, self.al
