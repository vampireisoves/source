import json
import base58
import os

def encode_json_to_base58(input_file, output_file):
    """将JSON文件编码为Base58并保存到新文件"""
    try:
        # 读取source.json文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 将JSON数据转换为字符串并编码为字节
        json_string = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
        json_bytes = json_string.encode('utf-8')
        
        # 使用Base58编码
        encoded_data = base58.b58encode(json_bytes).decode('utf-8')
        
        # 直接将编码后的数据写入config.json文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encoded_data)
        
        print(f"成功将 {input_file} 编码为Base58并保存到 {output_file}")
        return True
        
    except Exception as e:
        print(f"编码过程中出现错误: {e}")
        return False

if __name__ == "__main__":
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 定义输入和输出文件路径
    input_file = os.path.join(current_dir, "source.json")
    output_file = os.path.join(current_dir, "config.json")
    
    # 执行编码
    encode_json_to_base58(input_file, output_file)
