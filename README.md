# PointCloud2 To Pcd

ROSのPointCloud2形式の情報をpcdファイルに変換する

## ROS launchの起動

---

```bash
roslaunch sample_to_pcd.launch
```


## 作成したpcdファイル郡のリネーム

---

以降は `./pcd/` にpcdファイル群が存在するものとする <br>

```bash
python3 change_file_name.py
```

`p_{番号}.pcd` ファイルに変換される <br>


## pcdファイルの統合

---

```bash
python3 create_pcd_map.py
```

`./pcd/merge_map.pcd` が生成される<br>
