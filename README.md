# Duffing map の差分ヒートマップ
## Dependencies
- SciPy (NumPy)
- Pandas
- Matplotlib

## How to use
### xref 軌道計算
```
python calc_traj.py json/dat01.json
```

設定パラメタは以下の通り．
- `x0`: 初期条件
- `params`: 系のパラメタ


### 差分ヒートマップの計算
```
python calc_diff_map.py json/dat01.json
```

設定パラメタは以下の通り．
- `dm_x0`: 初期値領域の始点
- `dm_x1`: 初期値領域の終点
- `resolution`: 解像度

### プロット
```
python plot_diff_map.py json/dat01_diff_map.csv
```

`csv` ファイルがなければエラーを出します．