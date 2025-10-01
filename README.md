# Config Encoder

这个项目包含一个Python脚本，用于将source.json文件编码为Base58格式，并将结果保存在config.json中。

## 文件说明

- `source.json`: 原始JSON数据文件
- `encode_config.py`: 将source.json编码为Base58的Python脚本
- `config.json`: 包含Base58编码数据的输出文件
- `requirements.txt`: 项目依赖
- `.github/workflows/update-config.yml`: GitHub Actions工作流文件，每7天自动运行一次编码脚本

## 使用方法

1. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

2. 运行编码脚本:
   ```
   python encode_config.py
   ```

## GitHub Actions

工作流会每7天自动运行一次，将source.json编码为Base58并更新config.json文件。