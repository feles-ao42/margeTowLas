import laspy
import numpy as np
import sys

def merge_las_files(file1, file2, output_file):
    # LASファイルを読み込む
    las1 = laspy.read(file1)
    las2 = laspy.read(file2)
    
    # 新しいLASファイルのヘッダーを作成
    header = laspy.LasHeader(point_format=las1.header.point_format.id, version=las1.header.version)
    header.offsets = las1.header.offsets
    header.scales = las1.header.scales
    
    # 点群データを結合
    merged_points = np.concatenate([las1.points.array, las2.points.array])
    
    # 新しいLASデータを作成
    merged_las = laspy.LasData(header)
    merged_las.points = laspy.ScaleAwarePointRecord(
        merged_points, 
        header.point_format,
        scales=header.scales,
        offsets=header.offsets
    )
    
    # 結合したデータを保存
    merged_las.write(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("使用方法: python script.py 入力ファイル1 入力ファイル2 出力ファイル")
        sys.exit(1)
    
    merge_las_files(sys.argv[1], sys.argv[2], sys.argv[3])

