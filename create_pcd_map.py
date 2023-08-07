import open3d as o3d
import os

def merge_pcd_files(input_folder, output_file):
    # ディレクトリ内のすべてのpcdファイルを読み込む
    pcd_files = [f for f in os.listdir(input_folder) if f.endswith('.pcd')]
    
    if not pcd_files:
        print("No pcd files found in the input folder.")
        return
    
    # 最初のpcdファイルを読み込む
    full_pcd_path = os.path.join(input_folder, pcd_files[0])
    merged_pcd = o3d.io.read_point_cloud(full_pcd_path)

    # 他のpcdファイルを結合する
    for pcd_file in pcd_files[1:]:
        full_pcd_path = os.path.join(input_folder, pcd_file)
        pcd = o3d.io.read_point_cloud(full_pcd_path)
        merged_pcd += pcd

    # ポイントクラウドのフィルタリング（オプション）
    # 例: Voxelダウンサンプリングを実行する場合
    voxel_size = 0.1
    merged_pcd = merged_pcd.voxel_down_sample(voxel_size)

    # ポイントクラウドのバイナリ形式で保存
    o3d.io.write_point_cloud(output_file, merged_pcd, write_ascii=False)  # バイナリ形式で保存

    print("Merged point cloud saved to:", output_file)

if __name__ == "__main__":
    input_folder = "pcd/"  # pcdファイルの入力フォルダ
    output_file = "pcd/merged_map.pcd"  # 結合されたマップの出力ファイル
    merge_pcd_files(input_folder, output_file)
